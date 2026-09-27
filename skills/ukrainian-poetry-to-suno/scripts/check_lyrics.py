#!/usr/bin/env python3
"""
Pre-flight checker for Ukrainian song lyrics going into Suno v6-mini / Google Flow Music.

Catches the mechanical mistakes that silently ruin a generation:
  * delivery cues or instruments inside (parentheses) -> the model SINGS them;
  * over-marked stress (моЯ, прИйде) or unmarked risky words (випадок -> вИпадок);
  * lyrics too long for v6 (quality drops past ~3000 chars), long "rushing" lines;
  * chorus arriving too late, a single chorus, a hook that never repeats, Verse 2 copying Verse 1;
  * unbalanced brackets;
  * Style / Exclude fields over the limit, negations in Style ("no drums").

Usage:
  python check_lyrics.py lyrics.txt
  python check_lyrics.py lyrics.txt --style "darkwave, 120 bpm, ..." --exclude "cheesy pop, ..."
  cat lyrics.txt | python check_lyrics.py -

Exit code 1 if there are errors (warnings alone exit 0). Standard library only.
"""

import argparse
import re
import sys

# --- Stress marking (uppercase stressed vowel) -------------------------------------------
# Mark ONLY these three categories. Everything else stays lowercase: over-marking makes the
# vocal stilted and trains the reader to ignore the marks.
HOMOGRAPHS = """
зАмок замОк зАмку замкА дорОга дорОги дорОгу дорОгою дорогА дорогИй дорОге мУка мУки мукА
плАчу плачУ бІлизна білизнА нАголос наголОс оргАн Орган атлАс Атлас обрАзи Образи обрАза Образ
""".split()
ANTI_RUSSIAN = """
вИпадок вИпадку вИпадки чорнОзем чорнОзему одИннадцять чотирнАдцять листопАд листопАда
рукОпис перЕпис довІдник фартУх ненАвисть ненАвидіти пізнАння читАння завдАння принестИ
перенестИ вИрок новИй новА новЕ старИй старА босИй босА
""".split()
MOBILE_SHIFTS = """
зЕмлю зЕмлі рУку рУки хОдиш хОдить хОдять несУ несЕш
""".split()

ALLOWED_MARKED = {w.lower(): w for w in HOMOGRAPHS + ANTI_RUSSIAN + MOBILE_SHIFTS}
# Words an audio model is likely to mispronounce if left unmarked (subset worth flagging).
RISKY_UNMARKED = {w.lower(): w for w in ANTI_RUSSIAN + MOBILE_SHIFTS}

UPPER_VOWELS = set("АЕЄИІЇОУЮЯ")
WORD_RE = re.compile(r"[А-ЯЄІЇҐа-яєіїґ'’]+")

# --- Parentheses ---------------------------------------------------------------------------
DELIVERY_CUES = [
    "whispered", "whisper", "belted", "falsetto", "screamed", "growl", "ad-lib", "ad lib",
    "vocal runs", "building intensity", "key change", "half-time feel", "half time feel",
    "harmonized", "layered harmonies", "spoken", "spoken word", "acapella", "melisma",
    "pause", "fading out", "fade out", "stripped back", "breathy delivery",
]
UK_DELIVERY_CUES = ["шепіт", "фальцет", "речитатив", "пауза", "луна"]
INSTRUMENT_WORDS = [
    "guitar", "bass", "bassline", "drums", "synth", "piano", "strings", "cello", "riff",
    "808", "reverb", "distortion", "arpeggio", "percussion", "bandura", "sopilka", "bpm",
    "гітара", "бас", "барабани", "синтезатор", "соло",
]
SECTION_RE = re.compile(r"^\s*\[([^\]]*)\]\s*$")

STYLE_NEGATION_RE = re.compile(r"\b(no|without|avoid|not)\s+\w+", re.I)

LYRICS_HARD_LIMIT = 5000
LYRICS_SOFT_LIMIT = 3000   # v6: past ~3000 chars the model tends to rush or drop sections
STYLE_HARD_LIMIT = 1000
EXCLUDE_HARD_LIMIT = 1000
MAX_WORDS_PER_LINE = 9     # longer lines -> "lyrics rushing"
MAX_SUNG_LINES_BEFORE_CHORUS = 16  # rough proxy for "first chorus by ~50 seconds"


def is_delivery_cue(text: str) -> bool:
    t = text.strip().lower().rstrip(".!")
    for cue in DELIVERY_CUES:
        if t == cue or t.startswith(cue + ",") or t.startswith(cue + " "):
            return True
    return t in UK_DELIVERY_CUES


def check_parentheses(lines, errors):
    for n, line in enumerate(lines, 1):
        for content in re.findall(r"\(([^()]*)\)", line):
            low = content.lower()
            if is_delivery_cue(content):
                errors.append(
                    f"line {n}: '({content})' is a delivery cue — Suno/Flow will SING it. "
                    f"Use '[{content.strip().capitalize()}]' on its own line or put it in the section tag."
                )
            elif any(re.search(r"\b" + re.escape(w) + r"\b", low) for w in INSTRUMENT_WORDS):
                errors.append(
                    f"line {n}: '({content})' describes instruments — it will be sung. Move it into [square brackets]."
                )


def check_brackets(text, errors):
    for a, b in (("[", "]"), ("(", ")")):
        if text.count(a) != text.count(b):
            errors.append(f"unbalanced {a}{b}: {text.count(a)} '{a}' vs {text.count(b)} '{b}'")
    if re.search(r"\[\s*\]", text):
        errors.append("empty [] tag found")


def check_stress(lines, warnings):
    over, risky = [], []
    for n, line in enumerate(lines, 1):
        if SECTION_RE.match(line):
            continue
        sung = re.sub(r"\[[^\]]*\]", "", line)
        for word in WORD_RE.findall(sung):
            inner = [c for c in word[1:] if c in UPPER_VOWELS]
            has_lower = any(c.islower() for c in word)
            low = word.lower()
            if len(inner) == 1 and has_lower:
                if low not in ALLOWED_MARKED:
                    over.append(f"{word} (line {n})")
            elif not inner and low in RISKY_UNMARKED:
                risky.append(f"{word} -> {RISKY_UNMARKED[low]} (line {n})")
    if over:
        warnings.append(
            "stress marked outside the 3 categories (homograph / Russian-stress trap / mobile shift) — "
            "lowercase these: " + ", ".join(over[:15]) + (" ..." if len(over) > 15 else "")
        )
    if risky:
        warnings.append("likely mispronounced, consider marking: " + ", ".join(risky[:15]))


def check_structure(lines, warnings):
    sung_before_chorus = 0
    chorus_found = False
    long_lines = []
    for n, line in enumerate(lines, 1):
        m = SECTION_RE.match(line)
        if m:
            tag = m.group(1).lower()
            if "chorus" in tag or "приспів" in tag or tag.startswith("hook"):
                chorus_found = True
            continue
        sung = re.sub(r"\[[^\]]*\]|\([^)]*\)", "", line).strip()
        if not sung:
            continue
        if not chorus_found:
            sung_before_chorus += 1
        words = len(sung.split())
        if words > MAX_WORDS_PER_LINE:
            long_lines.append(f"line {n} ({words} words)")
    if not chorus_found:
        warnings.append("no [Chorus] tag — v6 structures songs better with explicit sections")
    elif sung_before_chorus > MAX_SUNG_LINES_BEFORE_CHORUS:
        warnings.append(
            f"{sung_before_chorus} sung lines before the first chorus — it will likely land after ~50s; shorten Verse 1"
        )
    if long_lines:
        warnings.append(
            f"lines over {MAX_WORDS_PER_LINE} words tend to make the vocal rush: " + ", ".join(long_lines[:10])
        )


def _sections(lines):
    """Split lyrics into [(tag_lower, [sung lines])] by standalone [Section] tags."""
    sections, current = [], ("", [])
    for line in lines:
        m = SECTION_RE.match(line)
        if m:
            sections.append(current)
            current = (m.group(1).lower(), [])
            continue
        sung = re.sub(r"\[[^\]]*\]", "", line).strip()
        if sung:
            current[1].append(sung)
    sections.append(current)
    return [s for s in sections if s[0] or s[1]]


def _norm(line):
    return re.sub(r"[^\w\s]", "", line.lower()).strip()


def check_song_craft(lines, warnings):
    """Measurable parts of the world-class song criteria (references/world-class-song-criteria.md)."""
    sections = _sections(lines)
    chorus_tags = [tag for tag, _ in sections if "chorus" in tag or "приспів" in tag]
    if len(chorus_tags) == 1:
        warnings.append("only one chorus — strong songs usually have 2–3 (criterion 2: the hook must return)")

    counts = {}
    for _, sung in sections:
        for line in sung:
            key = _norm(re.sub(r"\([^)]*\)", "", line))
            if len(key.split()) >= 2:
                counts[key] = counts.get(key, 0) + 1
    if counts and max(counts.values()) < 3:
        warnings.append("no lyric line repeats 3+ times — the hook/title may be too weak to stick (criterion 2)")

    verses = [sung for tag, sung in sections if tag.startswith("verse") or tag.startswith("куплет")]
    if len(verses) >= 2:
        first = {_norm(l) for l in verses[0]}
        repeated = [l for l in verses[1] if _norm(l) in first]
        if len(repeated) >= max(2, len(verses[1]) // 2):
            warnings.append("Verse 2 largely repeats Verse 1 — verses should move the story forward (criterion 5)")


def check_lengths(text, style, exclude, errors, warnings):
    n = len(text)
    if n > LYRICS_HARD_LIMIT:
        errors.append(f"lyrics are {n} chars — Suno hard limit is {LYRICS_HARD_LIMIT}")
    elif n > LYRICS_SOFT_LIMIT:
        warnings.append(f"lyrics are {n} chars — past ~{LYRICS_SOFT_LIMIT} v6 tends to rush or skip sections")
    if style is not None:
        s = len(style)
        if s > STYLE_HARD_LIMIT:
            errors.append(f"Style is {s} chars — hard limit {STYLE_HARD_LIMIT}")
        elif s > 250:
            warnings.append(f"Style is {s} chars — v6 weighs the first tags most; a tight 80–200 char prompt is easier to steer")
        if STYLE_NEGATION_RE.search(style):
            warnings.append("Style contains a negation ('no …'/'without …') — put unwanted elements in Exclude instead")
        if re.search(r"[А-ЯЄІЇҐа-яєіїґ]", style):
            warnings.append("Style contains Cyrillic — write Style tags in English; keep Ukrainian for the lyrics")
    if exclude is not None and len(exclude) > EXCLUDE_HARD_LIMIT:
        errors.append(f"Exclude is {len(exclude)} chars — hard limit {EXCLUDE_HARD_LIMIT}")


def check(text, style=None, exclude=None):
    errors, warnings = [], []
    lines = text.splitlines()
    check_brackets(text, errors)
    check_parentheses(lines, errors)
    check_stress(lines, warnings)
    check_structure(lines, warnings)
    check_song_craft(lines, warnings)
    check_lengths(text, style, exclude, errors, warnings)
    return errors, warnings


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("lyrics", help="lyrics file, or '-' for stdin")
    ap.add_argument("--style", help="Style of Music field text")
    ap.add_argument("--exclude", help="Exclude Styles field text")
    args = ap.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    text = sys.stdin.read() if args.lyrics == "-" else open(args.lyrics, encoding="utf-8").read()
    errors, warnings = check(text, args.style, args.exclude)
    for e in errors:
        print(f"ERROR   {e}")
    for w in warnings:
        print(f"WARNING {w}")
    if not errors and not warnings:
        print("OK — no mechanical issues found. Still read it aloud before generating.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

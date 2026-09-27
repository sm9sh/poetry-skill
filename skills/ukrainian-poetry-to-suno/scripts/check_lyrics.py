#!/usr/bin/env python3
"""
Pre-flight checker for Ukrainian song lyrics going into Suno v6-mini or Lyria 3.5 (Google Flow Music).

Catches the mechanical mistakes that silently ruin a generation:
  * delivery cues, instruments or any English words inside (parentheses) -> the model SINGS them;
  * over-marked stress (моЯ, прИйде) or unmarked risky words (випадок -> вИпадок),
    including words logged in references/suno-lessons.md after real generations;
  * lyrics too long (v6 quality drops past ~3000 chars; Lyria 3.5 tracks run ~3 min), long "rushing" lines;
  * syllable mismatch between matching lines of Verse 1 and Verse 2 (the melody repeats, the text must fit);
  * chorus arriving too late, a single chorus, a hook that never repeats, Verse 2 copying Verse 1;
  * unbalanced brackets;
  * Style / Exclude over the limit, negations or Cyrillic in Style; tag-list or bracketed Lyria prompts.

Usage:
  python check_lyrics.py lyrics.txt --style "darkwave, 120 bpm, ..." --exclude "cheesy pop, ..."
  python check_lyrics.py lyrics.txt --platform lyria --prompt "A slow cinematic ambient piece at 65 bpm..."
  python check_lyrics.py fragment.txt --section      # a single fixed section: skip whole-song checks
  python check_lyrics.py lyrics.txt --syllables      # also print syllables per sung line
  cat lyrics.txt | python check_lyrics.py -

Exit code 1 if there are errors (warnings alone exit 0). Standard library only.
"""

import argparse
import pathlib
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

LESSONS_FILE = pathlib.Path(__file__).resolve().parent.parent / "references" / "suno-lessons.md"
LESSON_LINE_RE = re.compile(r"^\s*-\s*([А-ЯЄІЇҐа-яєіїґ'’]+)\s*->\s*([А-ЯЄІЇҐа-яєіїґ'’]+)")


def load_lessons(path=LESSONS_FILE):
    """Words logged as mispronounced after real generations: '- слово -> слОво — date, model, note'."""
    words = []
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return words
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    for line in text.splitlines():
        m = LESSON_LINE_RE.match(line)
        if m and m.group(1).lower() == m.group(2).lower():
            words.append(m.group(2))
    return words


LESSON_WORDS = load_lessons()
ALLOWED_MARKED = {w.lower(): w for w in HOMOGRAPHS + ANTI_RUSSIAN + MOBILE_SHIFTS + LESSON_WORDS}
# Words an audio model is likely to mispronounce if left unmarked.
RISKY_UNMARKED = {w.lower(): w for w in ANTI_RUSSIAN + MOBILE_SHIFTS + LESSON_WORDS}

VOWELS = set("аеєиіїоуюяАЕЄИІЇОУЮЯ")
UPPER_VOWELS = set("АЕЄИІЇОУЮЯ")
WORD_RE = re.compile(r"[А-ЯЄІЇҐа-яєіїґ'’]+")

# --- Parentheses ---------------------------------------------------------------------------
DELIVERY_CUES = [
    "whispered", "whisper", "belted", "falsetto", "screamed", "growl", "ad-lib", "ad lib",
    "vocal runs", "building intensity", "key change", "half-time feel", "half time feel",
    "harmonized", "layered harmonies", "spoken", "spoken word", "acapella", "melisma",
    "pause", "fading out", "fade out", "stripped back", "breathy delivery", "intimate",
]
UK_DELIVERY_CUES = ["шепіт", "фальцет", "речитатив", "пауза", "луна"]
INSTRUMENT_WORDS = [
    "guitar", "bass", "bassline", "drums", "synth", "piano", "strings", "cello", "riff",
    "808", "reverb", "distortion", "arpeggio", "percussion", "bandura", "sopilka", "bpm",
    "гітара", "бас", "барабани", "синтезатор", "соло",
]
# English sounds that are fine to sing as backing vocals.
VOCALIZATIONS = {"ooh", "oh", "ah", "aah", "oo", "yeah", "hey", "la", "na", "woah", "whoa",
                 "mm", "mmm", "uh", "hmm", "ha", "eh", "ay", "ey", "ya", "yo"}
SECTION_RE = re.compile(r"^\s*\[([^\]]*)\]\s*$")

STYLE_NEGATION_RE = re.compile(r"\b(no|without|avoid|not)\s+\w+", re.I)

LYRICS_HARD_LIMIT = 5000
LYRICS_SOFT_LIMIT = 3000   # v6: past ~3000 chars the model tends to rush or drop sections
LYRIA_SOFT_LIMIT = 1800    # Lyria 3.5 tracks run up to ~3 minutes
STYLE_HARD_LIMIT = 1000
EXCLUDE_HARD_LIMIT = 1000
MAX_WORDS_PER_LINE = 9     # longer lines -> "lyrics rushing"
MAX_SUNG_LINES_BEFORE_CHORUS = 16  # rough proxy for "first chorus by ~50 seconds"
SYLLABLE_TOLERANCE = 2     # matching lines of V1 and V2 may differ by this much


def syllables(text):
    return sum(1 for c in text if c in VOWELS)


def sung_text(line):
    """The words the model will sing on this line (tags removed, parentheses kept)."""
    return re.sub(r"\[[^\]]*\]", "", line).strip()


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
            latin_words = re.findall(r"[a-z][a-z'-]*", low)
            if is_delivery_cue(content):
                errors.append(
                    f"line {n}: '({content})' is a delivery cue — Suno/Lyria will SING it. "
                    f"Use '[{content.strip().capitalize()}]' on its own line or put it in the section tag."
                )
            elif any(re.search(r"\b" + re.escape(w) + r"\b", low) for w in INSTRUMENT_WORDS):
                errors.append(
                    f"line {n}: '({content})' describes instruments — it will be sung. Move it into [square brackets]."
                )
            elif latin_words and not all(w.strip("-") in VOCALIZATIONS for w in latin_words):
                errors.append(
                    f"line {n}: '({content})' is English inside parentheses — it will be sung. "
                    f"If it is an instruction, move it into [square brackets]."
                )


TRAILING_ECHO_RE = re.compile(r"\(([^()]*)\)\s*[.!?…]*\s*$")


def check_echo_spam(lines, warnings):
    """Short (echo!) shouts after most lines of a section break the legato and sound comic."""
    for tag, sung in _sections(lines):
        echoes = [s for s in sung
                  if (m := TRAILING_ECHO_RE.search(s)) and len(m.group(1).split()) <= 3
                  and TRAILING_ECHO_RE.sub("", s).strip()]
        if len(echoes) >= 3 and len(echoes) * 2 >= len(sung):
            warnings.append(
                f"[{tag or 'untagged'}]: {len(echoes)} of {len(sung)} lines end with a short (echo) — "
                f"keep backing vocals rare and melodic; drop the per-line shouts"
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
        for word in WORD_RE.findall(sung_text(line)):
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


def _sections(lines):
    """Split lyrics into [(tag_lower, [sung lines])] by standalone [Section] tags."""
    sections, current = [], ("", [])
    for line in lines:
        m = SECTION_RE.match(line)
        if m:
            sections.append(current)
            current = (m.group(1).lower(), [])
            continue
        sung = sung_text(line)
        if sung:
            current[1].append(sung)
    sections.append(current)
    return [s for s in sections if s[0] or s[1]]


def _norm(line):
    return re.sub(r"[^\w\s]", "", line.lower()).strip()


def _is_chorus(tag):
    return "chorus" in tag or "приспів" in tag or tag.startswith("hook")


def _is_verse(tag):
    return tag.startswith("verse") or tag.startswith("куплет")


def check_structure(lines, warnings, whole_song=True):
    sung_before_chorus = 0
    chorus_found = False
    long_lines = []
    for n, line in enumerate(lines, 1):
        m = SECTION_RE.match(line)
        if m:
            if _is_chorus(m.group(1).lower()):
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
    if whole_song:
        if not chorus_found:
            warnings.append("no [Chorus] tag — v6 and Lyria structure songs better with explicit sections")
        elif sung_before_chorus > MAX_SUNG_LINES_BEFORE_CHORUS:
            warnings.append(
                f"{sung_before_chorus} sung lines before the first chorus — it will likely land after ~50s; shorten Verse 1"
            )
    if long_lines:
        warnings.append(
            f"lines over {MAX_WORDS_PER_LINE} words tend to make the vocal rush: " + ", ".join(long_lines[:10])
        )


def check_song_craft(lines, warnings):
    """Measurable parts of the world-class song criteria (references/world-class-song-criteria.md)."""
    sections = _sections(lines)
    chorus_tags = [tag for tag, _ in sections if _is_chorus(tag)]
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

    verses = [sung for tag, sung in sections if _is_verse(tag)]
    if len(verses) >= 2:
        first = {_norm(l) for l in verses[0]}
        repeated = [l for l in verses[1] if _norm(l) in first]
        if len(repeated) >= max(2, len(verses[1]) // 2):
            warnings.append("Verse 2 largely repeats Verse 1 — verses should move the story forward (criterion 5)")


def check_symmetry(lines, warnings):
    """Matching lines of Verse 1 and Verse 2 should have (nearly) the same syllable count (criterion 8)."""
    verses = [sung for tag, sung in _sections(lines) if _is_verse(tag)]
    if len(verses) < 2:
        return
    v1 = [re.sub(r"\([^)]*\)", "", l).strip() for l in verses[0]]
    v2 = [re.sub(r"\([^)]*\)", "", l).strip() for l in verses[1]]
    v1, v2 = [l for l in v1 if l], [l for l in v2 if l]
    if len(v1) != len(v2):
        warnings.append(
            f"Verse 1 has {len(v1)} sung lines and Verse 2 has {len(v2)} — the verse melody repeats, keep the line count equal"
        )
    diffs = []
    for i, (a, b) in enumerate(zip(v1, v2), 1):
        sa, sb = syllables(a), syllables(b)
        if abs(sa - sb) > SYLLABLE_TOLERANCE:
            diffs.append(f"line {i}: {sa} vs {sb}")
    if diffs:
        warnings.append("Verse 1 / Verse 2 syllable mismatch (criterion 8): " + "; ".join(diffs))


def check_lengths(text, style, exclude, errors, warnings, platform="suno"):
    n = len(text)
    if n > LYRICS_HARD_LIMIT:
        errors.append(f"lyrics are {n} chars — Suno hard limit is {LYRICS_HARD_LIMIT}")
    elif platform == "lyria" and n > LYRIA_SOFT_LIMIT:
        warnings.append(f"lyrics are {n} chars — Lyria 3.5 tracks run up to ~3 min; shorten verses or drop a section")
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
        if style.strip().lower().startswith("ukrainian"):
            warnings.append("Style starts with 'ukrainian' — lead with the Western genre; the first tags weigh most")
    if exclude is not None and len(exclude) > EXCLUDE_HARD_LIMIT:
        errors.append(f"Exclude is {len(exclude)} chars — hard limit {EXCLUDE_HARD_LIMIT}")


def check_lyria_prompt(prompt, warnings):
    """Lyria 3.5 takes a natural-language English prompt, not a tag list."""
    if re.search(r"[\[\]()]", prompt):
        warnings.append("Lyria prompt contains brackets — write plain sentences; tags belong in the lyrics")
    sentences = [s for s in re.split(r"[.!?]+", prompt) if s.strip()]
    commas = prompt.count(",")
    if len(sentences) < 2 and commas >= 5:
        warnings.append("Lyria prompt looks like a tag list — describe concept, instruments, vocal and dynamics in 2–4 sentences")
    if STYLE_NEGATION_RE.search(prompt):
        warnings.append("Lyria prompt contains a negation — describe what you want instead")
    if re.search(r"[А-ЯЄІЇҐа-яєіїґ]", prompt):
        warnings.append("Lyria prompt contains Cyrillic — write the prompt in English; keep Ukrainian for the lyrics")
    if not re.search(r"\b\d{2,3}\s*bpm\b|\btempo\b|\bslow\b|\bfast\b|\bmid-tempo\b", prompt, re.I):
        warnings.append("Lyria prompt has no tempo — add BPM or a tempo word")


def check(text, style=None, exclude=None, platform="suno", prompt=None, section=False):
    errors, warnings = [], []
    lines = text.splitlines()
    check_brackets(text, errors)
    check_parentheses(lines, errors)
    check_echo_spam(lines, warnings)
    check_stress(lines, warnings)
    check_structure(lines, warnings, whole_song=not section)
    if not section:
        check_song_craft(lines, warnings)
        check_symmetry(lines, warnings)
    check_lengths(text, style, exclude, errors, warnings, platform)
    if platform == "lyria" and prompt is not None:
        check_lyria_prompt(prompt, warnings)
    return errors, warnings


def syllable_report(text):
    out = []
    for tag, sung in _sections(text.splitlines()):
        out.append(f"[{tag}]" if tag else "[—]")
        for line in sung:
            core = re.sub(r"\([^)]*\)", "", line).strip()
            if core:
                out.append(f"  {syllables(core):>2}  {line}")
    return "\n".join(out)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("lyrics", help="lyrics file, or '-' for stdin")
    ap.add_argument("--platform", choices=["suno", "lyria"], default="suno")
    ap.add_argument("--style", help="Suno: Style of Music field text")
    ap.add_argument("--exclude", help="Suno: Exclude Styles field text")
    ap.add_argument("--prompt", help="Lyria 3.5: the natural-language prompt")
    ap.add_argument("--section", action="store_true", help="checking a single section: skip whole-song checks")
    ap.add_argument("--syllables", action="store_true", help="print syllables per sung line")
    args = ap.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    text = sys.stdin.read() if args.lyrics == "-" else open(args.lyrics, encoding="utf-8").read()
    errors, warnings = check(text, args.style, args.exclude, args.platform, args.prompt, args.section)
    if args.syllables:
        print(syllable_report(text) + "\n")
    for e in errors:
        print(f"ERROR   {e}")
    for w in warnings:
        print(f"WARNING {w}")
    if not errors and not warnings:
        print("OK — no mechanical issues found. Still read it aloud before generating.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

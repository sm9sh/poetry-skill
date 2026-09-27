#!/usr/bin/env python3
"""
Scansion helper for Ukrainian verse: syllables, stress pattern, best-fitting meter,
line-by-line deviations and clausulae.

Stress sources (in order):
  1. marks in the text — combining acute (за́мок) or an uppercase stressed vowel (замОк);
  2. optional dictionary (--auto-stress): pip install --no-deps ukrainian-word-stress marisa-trie
     (~50 MB; the dictionary leaves true homographs unmarked, so mark those yourself);
  3. monosyllables are treated as "may or may not carry stress" and never count as errors.

Usage:
  python scan_meter.py poem.txt
  python scan_meter.py poem.txt --auto-stress
  python scan_meter.py poem.txt --meter amphibrach
  cat poem.txt | python scan_meter.py -

The report is diagnostic (exit code 0). Read it, then fix the lines it flags.
"""

import argparse
import re
import sys

VOWELS = set("аеєиіїоуюяАЕЄИІЇОУЮЯ")
UPPER_VOWELS = set("АЕЄИІЇОУЮЯ")
ACUTE = "́"
WORD_RE = re.compile(r"[А-ЯЄІЇҐа-яєіїґ'’́]+")

# name: (foot size, 1-based position of the first strong syllable)
METERS = {
    "iamb": (2, 2),
    "trochee": (2, 1),
    "dactyl": (3, 1),
    "amphibrach": (3, 2),
    "anapest": (3, 3),
}
METER_UK = {
    "iamb": "ямб", "trochee": "хорей", "dactyl": "дактиль",
    "amphibrach": "амфібрахій", "anapest": "анапест", "dolnik": "дольник",
}
CLAUSULA = {0: "Ч", 1: "Ж", 2: "Д"}
# Two-syllable function words usually lose their stress in verse; never count them as errors.
WEAK_WORDS = {"уже", "або", "адже", "якщо", "ніби", "наче", "мовби", "аби", "хоча", "проте",
              "щоби", "немов", "тому", "отже", "лише", "усе", "чи то", "мене", "тебе", "себе"}


def load_stressifier():
    try:
        from ukrainian_word_stress import Stressifier, StressSymbol, Disambiguation
    except ImportError:
        return None
    return Stressifier(stress_symbol=StressSymbol.CombiningAcuteAccent,
                       disambiguation=Disambiguation.Dictionary)


def word_stress(word, auto):
    """Return (syllables, stressed_syllable_index or None, source)."""
    vowel_positions = [i for i, c in enumerate(word) if c in VOWELS]
    n = len(vowel_positions)
    if n == 0:
        return 0, None, "none"
    if ACUTE in word:
        idx = word.index(ACUTE) - 1
        if idx in vowel_positions:
            return n, vowel_positions.index(idx), "mark"
    upper_inner = [i for i in vowel_positions if word[i] in UPPER_VOWELS and i > 0]
    has_lower = any(c.islower() for c in word)
    if len(upper_inner) == 1 and has_lower:
        return n, vowel_positions.index(upper_inner[0]), "mark"
    if word[0] in UPPER_VOWELS and has_lower and n > 1 and word[1:].islower() and word[0] != word[0].lower():
        pass  # sentence-initial capital: ambiguous, fall through
    if n == 1:
        return 1, 0, "mono"
    if auto is not None:
        stressed = auto(word.lower())
        if ACUTE in stressed:
            idx = stressed.index(ACUTE) - 1
            vp = [i for i, c in enumerate(stressed) if c in VOWELS]
            if idx in vp:
                return n, vp.index(idx), "dict"
    return n, None, "unknown"


def scan_line(line, auto):
    syll = 0
    strong, optional, unknown = [], [], []
    for word in WORD_RE.findall(line):
        n, s, src = word_stress(word, auto)
        if n == 0:
            continue
        if s is not None:
            pos = syll + s + 1
            free = src == "mono" or word.lower().replace(ACUTE, "") in WEAK_WORDS
            (optional if free else strong).append(pos)
        else:
            unknown.append(word)
        syll += n
    return syll, strong, optional, unknown


def meter_violations(strong, meter):
    k, first = METERS[meter]
    return [p for p in strong if p >= first and (p - first) % k != 0 or p < first and p != first]


def dolnik_ok(strong):
    stresses = sorted(strong)
    return len(stresses) >= 2 and all(1 <= b - a - 1 <= 2 for a, b in zip(stresses, stresses[1:]))


def pattern(syll, strong, optional):
    return "".join("—" if i in strong else ("·" if i in optional else "U") for i in range(1, syll + 1))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("poem", help="poem file, or '-' for stdin")
    ap.add_argument("--meter", choices=sorted(METERS), help="check against this meter instead of the best fit")
    ap.add_argument("--auto-stress", action="store_true", help="fill missing stresses from the dictionary")
    args = ap.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    text = sys.stdin.read() if args.poem == "-" else open(args.poem, encoding="utf-8").read()

    auto = None
    if args.auto_stress:
        auto = load_stressifier()
        if auto is None:
            print("NOTE: ukrainian-word-stress is not installed; using only the marks in the text.\n"
                  "      pip install --no-deps ukrainian-word-stress marisa-trie\n")

    lines = []
    for raw in text.splitlines():
        line = re.sub(r"\[[^\]]*\]|\([^)]*\)", "", raw).strip()
        if raw.strip().startswith("[") and not line:
            continue
        lines.append(line)

    scanned = [scan_line(l, auto) if l else None for l in lines]
    verse = [s for s in scanned if s]
    if not verse:
        print("No verse lines found.")
        return 0

    totals = {m: sum(len(meter_violations(s[1], m)) for s in verse) for m in METERS}
    known = sum(len(s[1]) for s in verse)
    best = args.meter or min(totals, key=totals.get)
    dolnik_lines = sum(1 for s in verse if dolnik_ok(s[1]))
    label = best
    if not args.meter and totals[best] > max(2, len(verse) // 3) and dolnik_lines >= 0.7 * len(verse):
        label = "dolnik"

    print(f"Meter: {METER_UK[label]} ({label})" + ("" if args.meter else " — best fit")
          + f" | stress-bearing words scanned: {known}"
          + (f" | violations against {METER_UK[best]}: {totals[best]}" if label != "dolnik" else ""))
    print("Legend: — stressed, U unstressed, · monosyllable (free); Ч/Ж/Д = masculine/feminine/dactylic ending\n")

    stanza_clausulae, all_stanzas = [], []
    for line, s in zip(lines, scanned):
        if not s:
            if stanza_clausulae:
                all_stanzas.append(stanza_clausulae)
            stanza_clausulae = []
            print()
            continue
        syll, strong, optional, unknown = s
        words = WORD_RE.findall(line)
        last_word_known = bool(words) and word_stress(words[-1], auto)[1] is not None
        last = max(strong + optional) if strong + optional else None
        clausula = CLAUSULA.get(syll - last, "Г") if (last and last_word_known) else "?"
        stanza_clausulae.append(clausula)
        flags = []
        if label != "dolnik":
            bad = meter_violations(strong, best)
            initial = [p for p in bad if p == 1]
            bad = [p for p in bad if p != 1]
            if bad:
                flags.append(f"stress off the beat at syllable(s) {bad}")
            if initial:
                flags.append("stress on the first syllable (line-initial shift — usually acceptable)")
        elif not dolnik_ok(strong):
            flags.append("interval outside 1–2 syllables")
        if unknown:
            flags.append("unknown stress: " + ", ".join(unknown[:4]))
        print(f"{syll:>3} {clausula}  {pattern(syll, strong, optional):<20} {line}")
        for f in flags:
            print(f"        ! {f}")
    if stanza_clausulae:
        all_stanzas.append(stanza_clausulae)

    counts = [s[0] for s in verse]
    print("\nSyllables per line:", counts)
    for i, st in enumerate(all_stanzas, 1):
        scheme = "".join(st)
        note = "  ! uniform endings — monotonous unless intended" if len(st) >= 4 and len(set(st)) == 1 else ""
        print(f"Stanza {i} clausulae: {scheme}{note}")
    unknown_total = sum(len(s[3]) for s in verse)
    if unknown_total:
        print(f"\n{unknown_total} word(s) without known stress — mark them (acute or uppercase vowel) "
              "or run with --auto-stress for a more reliable scan.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

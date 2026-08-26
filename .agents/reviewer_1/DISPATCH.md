## 2026-08-26T10:00:10Z

You are Reviewer 1 (Ukrainian Poetic & Linguistic Reviewer).
Your working directory is `d:/poetry-skill/.agents/reviewer_1`.
You MUST read `d:/poetry-skill/.agents/ORIGINAL_REQUEST.md`, `d:/poetry-skill/.agents/PROJECT.md`, and `d:/poetry-skill/TEST_READY.md` before starting work.
Project root: `d:/poetry-skill`.

Task:
Perform an exhaustive, objective review of the Ukrainian Poetry skill and all related materials (`skills/ukrainian-poetry/`, `SKILL.md`, `references/`, tests, rubrics, and root mirrors).

Review Criteria:
1. Versification completeness: verify Dactyl (`— U U`), Dolnik, Taktovik, Kolomyika 14-syllable (4+4+6), Blank verse, Sonnet with volta, Rondo, Triolet, and Terza Rima.
2. Stress & accentuation rules: verify mobile stress, homographs (зАмок/замОк), anti-Russian misaccentuation blacklist, and Ukrainian phonetic euphony (у/в, і/й, з/із/зі).
3. Rhyme quality: verify heterogeneous rhyme requirement, assonance/dissonance rules, and strict prohibition of grammatical rhymes (verb-verb, same-case adj-adj) and diminutive suffixes.
4. Linguistic registers & anti-sharovarshchyna: verify 6 authentic registers and strict anti-kitsch filter.
5. Run the test suite: execute `py -3 tests/run_tests.py --tier 1` and `py -3 tests/run_tests.py --tier 2` (or `--all`) and inspect results.

Deliverables:
- Maintain `progress.md` with `Last visited:` timestamps.
- Write your comprehensive review report to `d:/poetry-skill/.agents/reviewer_1/review.md`.
- Write your formal handoff to `d:/poetry-skill/.agents/reviewer_1/handoff.md` with clear verdict (APPROVE or REQUEST_CHANGES).
- Message parent upon completion.

# Tests

What the automated tests check, and what they cannot.

**They check mechanics.** Scripts the skills call (`check_lyrics.py`, `scan_meter.py`), the bracket / metatag rules, Style and Exclude limits, and that every song shown in the docs passes the same checks a delivered song must pass.

**They do not check quality.** Whether a poem is good or a song works is judged on real prompts with the evals in `evals/` (with-skill vs baseline, blind judge). A green test run says the tooling and documentation are consistent, nothing more.

## Run

```bash
python tests/run_tests.py --all      # unit tests + tier suites (what CI runs)
python tests/run_tests.py --unit     # unit tests only
python tests/run_tests.py --tier 2   # one tier suite
python tests/run_tests.py --test TC_T2_01_Taboo_6Words_Ban
```

Windows: `py -3 tests/run_tests.py --all` or `.\tests\run_tests.ps1 -Tier All`. A JSON report is written to `tests/reports/test_report.json` (gitignored).

Install the optional stress dictionary (`pip install --no-deps ukrainian-word-stress marisa-trie`) to also run the checks against the real dictionary; without it they are skipped and the rest runs on a stub dictionary.

## Unit tests

| File | What it checks |
|---|---|
| `test_examples_playground.py` | `check_lyrics.py` (craft checks, modes, lessons journal, stress marks, dictionary), `scan_meter.py` on accented meter fixtures, the success / failure examples in `examples/` |
| `test_repo_integrity.py` | Real repo files: agents in `.claude-plugin/plugin.json` exist with valid frontmatter and are listed in `openai.yaml`; no plugin command shadows a skill; every lyrics block in `skills/` and `examples/success/` passes the bracket validator and `check_lyrics.py` |
| `test_metatag_validator.py` | Bracket rules: section and instrument tags in `[...]`, delivery cues in `[...]`, nothing but sung words in `(...)`, mismatched brackets, prose in tags |
| `test_suno_validator.py` | Style / Exclude: length caps, metadata labels, artist names, Exclude field |
| `test_run_evals.py` | `evals/run_evals.py` with a fake `claude`: stream parsing, blind A/B mapping, a full generate → check → judge → report round, reading iteration-1 scores |
| `test_validators.py` | Heuristic poetry checks used by the tier suites: inversions, filler words, cliché rhymes, sensory grounding, taboo words, rubric deductions — defects caught, clean text not flagged |

## Tier suites

JSON fixtures in `tests/tier*/`, run through the validators in `tests/validator/` and the 100-point rubric (`rubric_scorer.py`; pass ≥ 85 for poetry, ≥ 88 for Suno style).

| Tier | Folder | Content |
|---|---|---|
| 1 | `tier1_feature_coverage/` | Meters, non-syllabo-tonic verse, fixed forms, registers, genres, vocal timbres, Exclude vectors |
| 2 | `tier2_boundary_corner/` | Taboo pressure, strict meters, kolomyika caesura, compact Style, homographs, conflicting constraints |
| 3 | `tier3_cross_feature/` | Register × genre × vocal combinations, full brief → lyrics → prompt pipeline |
| 4 | `tier4_real_world/` | Release-style briefs |

The fixtures are hand-written; they keep the validators from regressing, they are not evidence that generated output is good.

## Adding a test

- A new rule in `check_lyrics.py` or `scan_meter.py` → a case in `test_examples_playground.py` (one input that must be flagged, one that must pass).
- A new lyrics example in the docs → nothing to add: `test_repo_integrity.py` picks it up and checks it.
- A quality question ("does the skill write better X?") → an eval in `evals/evals.json`, not a unit test.

## Other

- `tests/sync_ecosystem.py` regenerates the `.agents/skills/` mirror; CI fails if it is out of date.

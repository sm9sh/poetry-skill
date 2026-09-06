# Task Assignment: Worker M5 (Verification, Test Suite Expansion & Global Ecosystem Sync)

## Working Directory
d:\poetry-skill\.agents\worker_m5

## Context & Request
- Read `d:\poetry-skill\ORIGINAL_REQUEST.md` (specifically section ## 2026-09-06T09:42:47Z).
- Directives: `d:\poetry-skill\AGENTS.md`, `d:\poetry-skill\GEMINI.md`.
- Read Scope: `d:\poetry-skill\.agents\orchestrator_3\SCOPE.md`.
- Read Explorer 3 Blueprint: `d:\poetry-skill\.agents\explorer_survey_3\handoff.md` (Section 4.3 Test Suite Expansion).

## Mandatory Integrity Warning
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

## Exclusive Write Ownership
You exclusively own:
- Updating `tests/tier4_real_world/test_real_world_scenarios.json` to add 3 new test cases (`TC_T4_07`, `TC_T4_08`, `TC_T4_09`) corresponding to the 3 production playground scenarios (`suno-darkwave-postpunk`, `udio-triphop-downtempo`, `flowmusic-cinematic-ambient`), expanding the JSON suite to 78 tests.
- Creating/formalizing `tests/test_examples_playground.py` to unit-test that all 6 playground files in `examples/success/` and `examples/failures/` exist, are non-empty, adhere to bracket/parentheses rules, and conform to Ukrainian stress and platform prompt length constraints.
- Running `py -3 tests/sync_ecosystem.py` and verifying that:
  a) All canonical skills in `skills/` (including `poetry-qa-bot.md`, `openai.yaml`, updated `skills/poetry-skill/SKILL.md`, and relocated references) are synced to `.agents/skills/` and `C:\Users\sm9sh\.gemini\config\plugins\poetry-skill\`.
  b) NO mirror files are generated in the repository root `d:\poetry-skill\`.
- Running `py -3 tests/run_tests.py --all` and verifying 100% passing tests (78+ tests, 0 failures, 0 errors, exit code 0).
- Running `py -3 tests/audit_challenger2_empirical.py` and `py -3 -m unittest tests/test_adversarial_challenger2.py`.

## Verification Required
- Document all executed commands, terminal outputs, test counts, and sync status in `d:\poetry-skill\.agents\worker_m5\handoff.md`.
- Report back when done with send_message.

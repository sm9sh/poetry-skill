# Execution Plan

## Objectives
Implement requirements from `ORIGINAL_REQUEST.md`:
1. R1: Integration of 6 poetic principles into `skills/ukrainian-poetry/SKILL.md`, `skills/ukrainian-poetry/references/full-guide.md`, `skills/ukrainian-poetry/references/rubric.md`, `skills/poetry-skill/SKILL.md`, and `AGENTS.md`.
2. R2: Creation of 5 specialized subagents in `skills/ukrainian-poetry/agents/` (imagery architect, emotional critic, prosody phonics master, conciseness editor, form synthesizer), their registration, and pipeline definition.
3. R3: Integration into validator & scoring system (`tests/validator/poetic_validator.py`, `tests/validator/rubric_scorer.py`, test cases), keeping 100% compatibility with `ukrainian-poetry-to-suno`.
4. R4: Verification & Acceptance: `py -3 tests/run_tests.py --all` passes 100% with 0 errors and >=95/100 average score.

## Phases
- Phase 0: Survey & Mapping (3 parallel Explorers)
- Phase 1: PROJECT.md & Milestone Architecture
- Phase 2: Implementation of Milestones (R1, R2, R3) via Worker cycles
- Phase 3: Review, Adversarial Challenge, and Forensic Integrity Audit
- Phase 4: Full E2E Test Suite Run & Handoff

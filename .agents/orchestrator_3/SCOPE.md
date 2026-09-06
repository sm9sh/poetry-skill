# Project Scope: Finalization of Poetry-Skill Ecosystem Residual Tasks

## Architecture
- **Canonical Skill Repositories**:
  - `skills/poetry-skill/` (Unified orchestrator)
  - `skills/ukrainian-poetry/` (Poetry generation, prosody, 6 core principles, agents, references)
  - `skills/ukrainian-poetry-to-suno/` (Multi-platform AI music prompts, metatags, 10 Quality Gates, DAW mixing, references)
- **Agent Mirror & Global Plugin**:
  - `.agents/skills/` (Agent runtime skills mirror)
  - `C:\Users\sm9sh\.gemini\config\plugins\poetry-skill\` (Global user Gemini plugin)
- **Validation & Test Harness**:
  - `tests/` (Tier 1-4 deterministic test runner, validators, adversarial challenger suites)
  - `examples/` (`examples/success/` and `examples/failures/` prompt playground)

## Feature Inventory
| # | Feature | Description | Milestone | Source |
|---|---------|-------------|-----------|--------|
| 1 | Root Cleanup | Delete 16 redundant root mirror files and root `packs/` directory | M1 | ORIGINAL_REQUEST R1 [DONE] |
| 2 | Relocate Ukrainian Guides | Move `ukrainian-poetry-skill-uk.md` & `ukrainian-poetry-skill-lite.md` to `skills/ukrainian-poetry/references/` | M1 | ORIGINAL_REQUEST R1 [DONE] |
| 3 | Sync Refactoring | Remove `ROOT_MIRRORS` & `sync_root_mirrors()` from `tests/sync_ecosystem.py` | M1 | ORIGINAL_REQUEST R1 [DONE] |
| 4 | Doc Reference Pruning | Update links in `INSTALL.md` and `tests/audit_challenger2_empirical.py` | M1 | ORIGINAL_REQUEST R1 [DONE] |
| 5 | Poetry QA Bot Specification | Create `poetry-qa-bot.md` in `skills/` and `.agents/skills/` with 6-section schema & 100-pt penalty matrix | M2 | ORIGINAL_REQUEST R2 [DONE] |
| 6 | Poetry QA Bot Registration | Register `poetry-qa-bot` in `skills/` and `.agents/skills/` `openai.yaml` | M2 | ORIGINAL_REQUEST R2 [DONE] |
| 7 | Poetry QA Bot Schema Test | Update `tests/test_adversarial_challenger2.py` with `poetry-qa-bot.md` | M2 | ORIGINAL_REQUEST R2 [DONE] |
| 8 | End-to-End Song Pipeline | Add `## 3. End-to-End Song Creation Pipeline` to `skills/poetry-skill/SKILL.md` and mirror | M3 | ORIGINAL_REQUEST R3 [DONE] |
| 9 | Prompt Playground Success | Create 3 production scenarios: Suno Darkwave, Udio Trip-Hop, Flow Music Ambient | M4 | ORIGINAL_REQUEST R4 [DONE] |
| 10| Prompt Playground Failures | Create 3 failure remediation guides: lyrics-rushing, robotic-vocals, true-peak | M4 | ORIGINAL_REQUEST R4 [DONE] |
| 11| Test Expansion to 78+ tests| Add new scenarios in `tests/` to reach 78+ passing tests with 100% success rate | M5 | Verification & Testing [DONE] |
| 12| Sync Verification | Run `tests/sync_ecosystem.py` and verify root cleanliness and global plugin sync | M5 | Verification & Testing [DONE] |
| 13| Metatag Remediation | Fix Output Contract bracket syntax in `music-lyrics-architect.md` & add `test_22` | M5 | Challenger 2 / Gate 2 [DONE] |

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| M1 | Root Cleanup & Sync Refactoring | Purge 16 root files, relocate Ukrainian guides, refactor sync script, update doc links | None | DONE |
| M2 | Poetry QA Bot Subagent | Create `poetry-qa-bot.md` and register in `openai.yaml` in both locations | None | DONE |
| M3 | End-to-End Song Creation Bridge | Add unified 6-stage pipeline protocol to `skills/poetry-skill/SKILL.md` | M2 | DONE |
| M4 | Prompt Playground | Create `examples/success/` and `examples/failures/` directories and 6 guide files | None | DONE |
| M5 | Test Suite & Ecosystem Sync | Expand test suite to 78+ tests, execute full test runner, verify ecosystem sync | M1, M2, M3, M4 | DONE |

## Interface Contracts
### ukrainian-poetry ↔ poetry-qa-bot
- Input: `poem_text: string`, `target_form: string`, `target_meter: string`, `register: enum`, `passing_threshold: int`
- Output: 7-dimension scorecard, itemized defect log (deductions D01-D14), prosodic scansion map, prioritized remediation blueprint.
- Threshold: $\ge 90/100$ PASS, $<85/100$ FAIL with subagent routing.

### poetry-qa-bot ↔ music-lyrics-architect (Stage 2 ➔ Stage 3)
- Passing audited poem with verified meter and literary accents passed to song architecture.
- Structural metatags in `[Square Brackets]`, vocal delivery / ad-libs strictly in `(Round Parentheses)`.
- Syllable symmetry: 8-8-8-8 / 10-8-10-8 for downbeat stability; Spoken Prosody Test; capitalized stress vowels.

### music-lyrics-architect ➔ music-prompt-synthesizer (Stage 3 ➔ Stage 4)
- Formatted lyrics + Acoustic DNA passed for platform prompt synthesis:
  - Suno v4.5/v5.5: Method 1 (First 5 Words) + Method 2 (HookGenius Tag Matrix) + Exclude Vector.
  - Udio v4: $\le 250$ chars prompt with `*stars*` inpainting markup + Context Length config.
  - Google Flow Music: Conversational Agent mode prompt + Spaces config.

### Generation ➔ DAW / Mastering Verification (Stages 5–6)
- 10 AI Quality Gates verification.
- DAW Stem separation, Bass Split at 200 Hz, Tchad Blake parallel drum distortion directly to Master Fader.
- Loud mastering at $-1\text{ dBTP}$ with True Peak limiting OFF (or $-14\text{ LUFS}$ if $-2\text{ dBTP}$ mandatory).

## Code Layout
- `skills/ukrainian-poetry/agents/poetry-qa-bot.md`
- `skills/ukrainian-poetry/agents/openai.yaml`
- `skills/ukrainian-poetry/references/ukrainian-poetry-skill-uk.md`
- `skills/ukrainian-poetry/references/ukrainian-poetry-skill-lite.md`
- `skills/ukrainian-poetry/SKILL.md`
- `skills/poetry-skill/SKILL.md`
- `skills/ukrainian-poetry-to-suno/agents/music-lyrics-architect.md`
- `examples/success/suno-darkwave-postpunk.md`
- `examples/success/udio-triphop-downtempo.md`
- `examples/success/flowmusic-cinematic-ambient.md`
- `examples/failures/lyrics-rushing-fix.md`
- `examples/failures/robotic-vocals-fix.md`
- `examples/failures/true-peak-clipping-fix.md`
- `tests/sync_ecosystem.py`
- `tests/test_examples_playground.py`
- `tests/test_adversarial_challenger2.py`
- `tests/tier4_real_world/test_real_world_scenarios.json`
- `tests/audit_challenger2_empirical.py`
- `INSTALL.md`

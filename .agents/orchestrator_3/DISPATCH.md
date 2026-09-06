# DISPATCH Log

## 2026-09-06T09:43:44Z
You are the Project Orchestrator (orchestrator_3) for the poetry-skill repository.

## Identity & Workspace
- Working directory: d:\poetry-skill\.agents\orchestrator_3
- Repository root: d:\poetry-skill
- Request file: d:\poetry-skill\ORIGINAL_REQUEST.md (see section ## 2026-09-06T09:42:47Z)
- Directives: d:\poetry-skill\AGENTS.md, GEMINI.md

## Mission & Requirements
Execute the user request to finalize the residual tasks of the poetry-skill ecosystem:

### R1. Root Cleanup & Sync Refactoring
- Delete the 16 redundant mirror files from the root directory:
  `ukrainian-poetry-skill.md`, `ukrainian-poetry-to-suno.md`, `lyrics-to-suno-template.md`, `song-structure-pack.md`, `suno-prompt-anti-patterns.md`, `prompt-builder.md`, `reference-to-style-cheatsheet.md`, `mood-to-style-map.md`, `suno-style-rubric.md`, `reference-breakdown-examples.md`, `ukrainian-song-scenarios.md`, `suno-prompt-tests.md`, `ukrainian-poetry-skill-rubric.md`, `ukrainian-poetry-skill-input-template.md`, `ukrainian-poetry-skill-stress-pack.md`, `ukrainian-poetry-skill-tests.md` and the root folder `packs/`.
- Update `tests/sync_ecosystem.py`: remove the logic copying files to the root. The script must exclusively sync canonical skills between `skills/`, `.agents/skills/`, and the global Gemini plugin directory (`C:\Users\sm9sh\.gemini\config\plugins\poetry-skill\`).
- Move or relocate `ukrainian-poetry-skill-uk.md` and `ukrainian-poetry-skill-lite.md` into appropriate folders (e.g. `docs/` or `skills/ukrainian-poetry/references/`), removing them from the root so no loose guides remain in the root directory.
- Check and update all references in `README.md`, `README.en.md`, `HOWTO.md`, `INSTALL.md`, and other docs to point to canonical paths inside `.agents/skills/` or `skills/`, eliminating all broken links to deleted root files.

### R2. Quality Assurance Agent: Poetry QA Bot
- Create the subagent specification file `poetry-qa-bot.md` in `skills/ukrainian-poetry/agents/` and `.agents/skills/ukrainian-poetry/agents/`.
- Register the agent in `skills/ukrainian-poetry/agents/openai.yaml` and `.agents/skills/ukrainian-poetry/agents/openai.yaml`.
- The agent must act as an autonomous auditor: evaluate verse for compliance with the 6 core poetic principles, apply the 100-point penalty rubric from `rubric.md`, and return a detailed scoring report with points per criterion and actionable step-by-step recommendations for improvement. Follow standard subagent specification format (Role, Boundaries, Contracts, Heuristics, Output format, Edge cases).

### R3. End-to-End Song Creation Bridge
- Update the main orchestrator skill `skills/poetry-skill/SKILL.md` and `.agents/skills/poetry-skill/SKILL.md` by adding section `## End-to-End Song Creation Pipeline`.
- Document the unified end-to-end protocol:
  "Idea / theme -> verse generation (ukrainian-poetry) -> quality audit (poetry-qa-bot) -> lyrics adaptation & Spoken Prosody Test (music-lyrics-architect) -> platform selection & prompt synthesis (music-prompt-synthesizer: Suno / Udio / Flow Music) -> 10 AI Quality Gates verification -> DAW stem mixing recommendations (music-daw-mastering-critic)".

### R4. Prompt Playground (Examples & Failure Analyses)
- Create directory `examples/` with subdirectories `examples/success/` and `examples/failures/`.
- `examples/success/` must contain at least 3 production-grade end-to-end scenarios:
  1. Darkwave / Post-Punk track for Suno v4.5/v5.5 (accented verse + prompt + excludes).
  2. Trip-Hop track for Udio v4 (lyrics + 250-char prompt + Inpainting `*stars*` markup + Context Length).
  3. Cinematic Ambient track for Google Flow Music Lyria 3.5 (conversational agent prompt + space description).
- `examples/failures/` must contain typical error breakdowns and remediation guides:
  1. `lyrics-rushing-fix.md`: rapid vocal delivery fix via `(half-time feel)` and 4–8 words/line limits.
  2. `robotic-vocals-fix.md`: eliminating plastic/sterile vocals via Vocal Triple-Stack.
  3. `true-peak-clipping-fix.md`: preventing inter-sample clipping on streaming services.

### Verification & Testing
- Ensure `py -3 tests/run_tests.py --all` executes cleanly with exit code 0 (100% passing tests, 75+ tests, 0 errors). If any tests need updating or new tests need to be added to reflect the cleaned root and new components, update them appropriately.
- Run `py -3 tests/sync_ecosystem.py` and verify it does NOT generate any mirror files in the root.
- Ensure all changes are synchronized to `.agents/skills/` and `C:\Users\sm9sh\.gemini\config\plugins\poetry-skill\`.

## Operational Discipline
- Initialize and maintain `d:\poetry-skill\.agents\orchestrator_3\BRIEFING.md` and `d:\poetry-skill\.agents\orchestrator_3\progress.md`.
- Decompose and execute tasks methodically, utilizing specialized workers or subagents as needed.
- When finished, write your handoff report to `d:\poetry-skill\.agents\orchestrator_3\handoff.md` and send a message back to Sentinel with your completion summary.

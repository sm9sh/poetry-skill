# Task Assignment: Worker M1 (Root Cleanup & Sync Refactoring)

## Working Directory
d:\poetry-skill\.agents\worker_m1

## Context & Request
- Read `d:\poetry-skill\ORIGINAL_REQUEST.md` (specifically section ## 2026-09-06T09:42:47Z).
- Directives: `d:\poetry-skill\AGENTS.md`, `d:\poetry-skill\GEMINI.md`.
- Read Explorer 1 findings: `d:\poetry-skill\.agents\explorer_survey_1\handoff.md`.
- Read Scope: `d:\poetry-skill\.agents\orchestrator_3\SCOPE.md`.

## Mandatory Integrity Warning
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

## Exclusive Write Ownership
You exclusively own:
- Deleting the 16 redundant root files:
  `ukrainian-poetry-skill.md`, `ukrainian-poetry-to-suno.md`, `lyrics-to-suno-template.md`, `song-structure-pack.md`, `suno-prompt-anti-patterns.md`, `prompt-builder.md`, `reference-to-style-cheatsheet.md`, `mood-to-style-map.md`, `suno-style-rubric.md`, `reference-breakdown-examples.md`, `ukrainian-song-scenarios.md`, `suno-prompt-tests.md`, `ukrainian-poetry-skill-rubric.md`, `ukrainian-poetry-skill-input-template.md`, `ukrainian-poetry-skill-stress-pack.md`, `ukrainian-poetry-skill-tests.md`
- Deleting the root folder `packs/`
- Relocating `ukrainian-poetry-skill-uk.md` and `ukrainian-poetry-skill-lite.md` to `skills/ukrainian-poetry/references/` (and ensure they are also copied to `.agents/skills/ukrainian-poetry/references/` or synced)
- Updating reference table in `skills/ukrainian-poetry/SKILL.md` and `.agents/skills/ukrainian-poetry/SKILL.md` to index the two relocated guides
- Refactoring `tests/sync_ecosystem.py`: completely remove `ROOT_MIRRORS` and `sync_root_mirrors()` so root is never repopulated with mirrors. Ensure clean sync between `skills/`, `.agents/skills/`, and `C:\Users\sm9sh\.gemini\config\plugins\poetry-skill\`. Handle upstream path for `ai-music-generation-meta-spec-v8.md`.
- Updating references in `INSTALL.md` (lines 19-21) and `tests/audit_challenger2_empirical.py` (lines 89-95, 209-210) to point to canonical paths.

## Verification Required
- Run `py -3 tests/sync_ecosystem.py` and verify NO files are created at root.
- Verify `git status` or file listing at root has NO redundant mirror files or `packs/`.
- Run `py -3 tests/audit_challenger2_empirical.py` and ensure it passes.
- Document all commands and results in `d:\poetry-skill\.agents\worker_m1\handoff.md`.

## 2026-09-06T09:50:09Z

<USER_REQUEST>
You are Worker M1 assigned to Milestone 1: Root Cleanup & Sync Refactoring.
Your working directory is d:\poetry-skill\.agents\worker_m1.
Read your instructions in d:\poetry-skill\.agents\worker_m1\DISPATCH.md.
Also read d:\poetry-skill\ORIGINAL_REQUEST.md (specifically section ## 2026-09-06T09:42:47Z), AGENTS.md, GEMINI.md, and d:\poetry-skill\.agents\explorer_survey_1\handoff.md.

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

Execute Milestone 1:
1. Delete the 16 redundant root mirror files and the root `packs/` folder.
2. Relocate `ukrainian-poetry-skill-uk.md` and `ukrainian-poetry-skill-lite.md` to `skills/ukrainian-poetry/references/` (and `.agents/skills/ukrainian-poetry/references/`).
3. Update reference table in `skills/ukrainian-poetry/SKILL.md` and `.agents/skills/ukrainian-poetry/SKILL.md`.
4. Refactor `tests/sync_ecosystem.py`: remove ROOT_MIRRORS and sync_root_mirrors() so root is never repopulated with mirrors. Ensure clean sync between `skills/`, `.agents/skills/`, and the global plugin.
5. Update stale references in `INSTALL.md` and `tests/audit_challenger2_empirical.py`.
6. Run `py -3 tests/sync_ecosystem.py` and verify no files are created at root. Run `py -3 tests/audit_challenger2_empirical.py`.
7. Write your report to d:\poetry-skill\.agents\worker_m1\handoff.md and report back via send_message.
</USER_REQUEST>

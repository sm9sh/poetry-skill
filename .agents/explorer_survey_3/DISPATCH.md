# Task Assignment: Explorer Survey 3 (Prompt Playground & Test Suite / Global Plugin Analysis)

## Working Directory
d:\poetry-skill\.agents\explorer_survey_3

## Context & Request
- Read `d:\poetry-skill\ORIGINAL_REQUEST.md` (specifically section ## 2026-09-06T09:42:47Z).
- Directives: `d:\poetry-skill\AGENTS.md`, `d:\poetry-skill\GEMINI.md`.

## Mission
Analyze R4 (Prompt Playground) and Verification/Testing:
1. For R4 (Prompt Playground):
   - Check if `examples/` exists and how existing guides / scenarios are formatted (check `skills/ukrainian-poetry-to-suno/references/`).
   - Define exact specifications for `examples/success/`:
     1) Darkwave / Post-Punk for Suno v4.5/v5.5 (accented verse + prompt + excludes).
     2) Trip-Hop for Udio v4 (lyrics + 250-char prompt + Inpainting `*stars*` markup + Context Length).
     3) Cinematic Ambient for Google Flow Music Lyria 3.5 (conversational agent prompt + space description).
   - Define exact specifications for `examples/failures/`:
     1) `lyrics-rushing-fix.md` ((half-time feel) and 4-8 words/line).
     2) `robotic-vocals-fix.md` (Vocal Triple-Stack: Character + Delivery + FX).
     3) `true-peak-clipping-fix.md` (inter-sample clipping, TP limiting OFF at -1 dBTP, LUFS targets).
2. For Verification, Tests & Global Sync:
   - Inspect `tests/run_tests.py` and all test modules under `tests/`. How many tests currently run? What do they assert?
   - Inspect global plugin directory `C:\Users\sm9sh\.gemini\config\plugins\poetry-skill\` and ensure sync requirements are identified.
   - Identify what new tests or test updates are needed to reach 75+ tests and 100% pass rate.

## Output
Write your comprehensive analysis report to `d:\poetry-skill\.agents\explorer_survey_3\handoff.md`.
Report back when done with send_message.

## 2026-09-06T09:44:14Z

<USER_REQUEST>
You are Explorer 3 investigating R4 (Prompt Playground) and Verification / Testing.
Your working directory is d:\poetry-skill\.agents\explorer_survey_3.
Read your instructions in d:\poetry-skill\.agents\explorer_survey_3\DISPATCH.md.
Also read d:\poetry-skill\ORIGINAL_REQUEST.md (specifically section ## 2026-09-06T09:42:47Z), AGENTS.md, and GEMINI.md.
Investigate examples/ directory, scenarios, failure analyses specifications, existing test suites in tests/, and global plugin sync at C:\Users\sm9sh\.gemini\config\plugins\poetry-skill\.
Write a comprehensive report to d:\poetry-skill\.agents\explorer_survey_3\handoff.md detailing content for examples/success/, examples/failures/, test suite expansion (to 75+ tests), and sync checks.
When done, notify orchestrator_3 via send_message.
</USER_REQUEST>

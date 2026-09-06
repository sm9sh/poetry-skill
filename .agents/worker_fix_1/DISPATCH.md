# Task Assignment: Worker Fix 1 (Bracket & Metatag Remediation in music-lyrics-architect.md)

## Working Directory
d:\poetry-skill\.agents\worker_fix_1

## Context & Request
- Read `d:\poetry-skill\ORIGINAL_REQUEST.md` (specifically section ## 2026-09-06T09:42:47Z).
- Directives: `d:\poetry-skill\AGENTS.md`, `d:\poetry-skill\GEMINI.md`.
- Read Explorer Fix 1 Report: `d:\poetry-skill\.agents\explorer_fix_1\handoff.md`.
- Read Patch: `d:\poetry-skill\.agents\explorer_fix_1\remediation.patch`.

## Mandatory Integrity Warning
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

## Exclusive Write Ownership
You exclusively own:
- `skills/ukrainian-poetry-to-suno/agents/music-lyrics-architect.md`
- `tests/test_adversarial_challenger2.py`

## Instructions
1. Update `skills/ukrainian-poetry-to-suno/agents/music-lyrics-architect.md`:
   Replace lines 49–70 so that:
   - Rule 5 refers to canonical inline vocal gestures in parentheses: `(whispered)`, `(belted)`, `(falsetto)`, `(screamed)`, `(ad-lib)`, `(building intensity)`, `(key change)`, `(half-time feel)`, `(harmonized)`, `(луна)`.
   - The Output Contract block uses proper compound square brackets for arrangement cues and round parentheses only for vocal gestures:
     ```markdown
     # Output Contract
     ```markdown
     ## 🎼 AI-Optimized Lyrics

     [Intro - ambient build]

     [Verse 1 - rhythmic staccato]
     (whispered)
     Line one text hEre
     Line two text hEre

     [Chorus - soaring legato]
     (belted)
     Line one of chOrus
     Line two of chOrus

     [Outro - fade out]
     ```
     ```
2. In `tests/test_adversarial_challenger2.py`, add regression test `test_22_music_subagents_and_metatags` asserting that `MetatagValidator` passes on all subagents in `skills/ukrainian-poetry-to-suno/agents/`.
3. Run `py -3 tests/sync_ecosystem.py` to synchronize `.agents/skills/` and `C:\Users\sm9sh\.gemini\config\plugins\poetry-skill\`.
4. Run:
   - `py -3 -m unittest tests/test_adversarial_challenger2.py`
   - `py -3 tests/audit_challenger2_empirical.py`
   - `py -3 tests/run_tests.py --all`
5. Write your report to `d:\poetry-skill\.agents\worker_fix_1\handoff.md` and report back via send_message.

## 2026-09-06T10:06:20Z
<USER_REQUEST>
You are Worker Fix 1 assigned to remediate the bracket/metatag violation in music-lyrics-architect.md.
Your working directory is d:\poetry-skill\.agents\worker_fix_1.
Read your instructions in d:\poetry-skill\.agents\worker_fix_1\DISPATCH.md.
Also read d:\poetry-skill\ORIGINAL_REQUEST.md (specifically section ## 2026-09-06T09:42:47Z), AGENTS.md, GEMINI.md, and d:\poetry-skill\.agents\explorer_fix_1\handoff.md.

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

Execute the remediation:
1. Apply the patch or update skills/ukrainian-poetry-to-suno/agents/music-lyrics-architect.md lines 49-70 using the compliant specification from Explorer Fix 1.
2. Add regression test test_22_music_subagents_and_metatags to tests/test_adversarial_challenger2.py.
3. Run `py -3 tests/sync_ecosystem.py` to sync to .agents/skills/ and C:\Users\sm9sh\.gemini\config\plugins\poetry-skill\.
4. Run `py -3 -m unittest tests/test_adversarial_challenger2.py`, `py -3 tests/audit_challenger2_empirical.py`, and `py -3 tests/run_tests.py --all`.
5. Write your report to d:\poetry-skill\.agents\worker_fix_1\handoff.md and report back via send_message.
</USER_REQUEST>

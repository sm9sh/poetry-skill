# Task Assignment: Worker M4 (Prompt Playground: Examples & Failure Analyses)

## Working Directory
d:\poetry-skill\.agents\worker_m4

## Context & Request
- Read `d:\poetry-skill\ORIGINAL_REQUEST.md` (specifically section ## 2026-09-06T09:42:47Z).
- Directives: `d:\poetry-skill\AGENTS.md`, `d:\poetry-skill\GEMINI.md`.
- Read Explorer 3 findings & blueprints: `d:\poetry-skill\.agents\explorer_survey_3\handoff.md`.
- Read Scope: `d:\poetry-skill\.agents\orchestrator_3\SCOPE.md`.

## Mandatory Integrity Warning
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

## Exclusive Write Ownership
You exclusively own:
- Creating directory `examples/` with subdirectories `examples/success/` and `examples/failures/`.
- Implementing `examples/success/suno-darkwave-postpunk.md` (Ukrainian post-punk/darkwave, Suno v4.5/v5.5, accented verse with capitalized stressed vowels `вИпадок`, `дорОга`, `чорнОзем`, dual prompts Method 1 & 2, exclude vector, 10 Quality Gates checklist).
- Implementing `examples/success/udio-triphop-downtempo.md` (Ukrainian trip-hop/downtempo, Udio v4, <=250-char prompt, inpainting `*stars*` markup, Context Length engineering, 48 kHz stereo, lyrics).
- Implementing `examples/success/flowmusic-cinematic-ambient.md` (Ukrainian cinematic ambient/spoken-word, Google Flow Music Lyria 3.5, conversational agent prompt, spaces configuration, section replace, vocal/instrument dynamics).
- Implementing `examples/failures/lyrics-rushing-fix.md` (rapid vocal delivery breakdown, root causes, before/after lyrics with `(half-time feel)` and 4-8 words/line).
- Implementing `examples/failures/robotic-vocals-fix.md` (sterile/plastic vocals breakdown, Vocal Triple-Stack: Character + Delivery + FX, before/after prompt matrix).
- Implementing `examples/failures/true-peak-clipping-fix.md` (inter-sample clipping breakdown, True Peak limiting OFF at -1 dBTP for loud masters -6..-8 LUFS, -14 LUFS target if -2 dBTP mandatory).

## Verification Required
- Check that all 6 files exist, contain complete non-dummy content conforming to `AGENTS.md` and Explorer 3 blueprint.
- Verify Ukrainian lyrics follow the 6 Poetic Principles and have correct stress capitalization.
- Verify prompt lengths comply with platform constraints (Suno 80-180 chars, Udio <=250 chars).
- Document all files and validation in `d:\poetry-skill\.agents\worker_m4\handoff.md`.

- Report back when done with send_message.

## 2026-09-06T09:50:09Z
You are Worker M4 assigned to Milestone 4: Prompt Playground (Examples & Failure Analyses).
Your working directory is d:\poetry-skill\.agents\worker_m4.
Read your instructions in d:\poetry-skill\.agents\worker_m4\DISPATCH.md.
Also read d:\poetry-skill\ORIGINAL_REQUEST.md (specifically section ## 2026-09-06T09:42:47Z), AGENTS.md, GEMINI.md, and d:\poetry-skill\.agents\explorer_survey_3\handoff.md.

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

Execute Milestone 4:
1. Create `examples/` with subdirectories `examples/success/` and `examples/failures/`.
2. Implement `examples/success/suno-darkwave-postpunk.md` (full Ukrainian post-punk/darkwave scenario with accented lyrics, prompts, exclude vectors, 10 Quality Gates checklist).
3. Implement `examples/success/udio-triphop-downtempo.md` (full Ukrainian trip-hop scenario with Udio v4 <=250-char prompt, inpainting *stars* markup, Context Length engineering, 48 kHz, lyrics).
4. Implement `examples/success/flowmusic-cinematic-ambient.md` (full Ukrainian cinematic ambient scenario with Google Flow Music Lyria 3.5 conversational prompt, spaces, section replace).
5. Implement `examples/failures/lyrics-rushing-fix.md` (rapid vocal delivery diagnosis, half-time feel, 4-8 words/line).
6. Implement `examples/failures/robotic-vocals-fix.md` (sterile/plastic vocals diagnosis, Vocal Triple-Stack: Character + Delivery + FX).
7. Implement `examples/failures/true-peak-clipping-fix.md` (inter-sample clipping diagnosis, True Peak limiting OFF at -1 dBTP for loud masters, -14 LUFS target).
8. Verify all 6 files are complete, non-dummy, follow AGENTS.md directives and Explorer 3 blueprint.
9. Write your report to d:\poetry-skill\.agents\worker_m4\handoff.md and report back via send_message.

# Task Assignment: Explorer Survey 2 (Poetry QA Bot & End-to-End Pipeline Analysis)

## Working Directory
d:\poetry-skill\.agents\explorer_survey_2

## Context & Request
- Read `d:\poetry-skill\ORIGINAL_REQUEST.md` (specifically section ## 2026-09-06T09:42:47Z).
- Directives: `d:\poetry-skill\AGENTS.md`, `d:\poetry-skill\GEMINI.md`.

## Mission
Analyze R2 & R3:
1. For R2 (Poetry QA Bot):
   - Inspect existing subagents in `skills/ukrainian-poetry/agents/` and `.agents/skills/ukrainian-poetry/agents/` (e.g., `poetry-imagery-architect.md`, `poetry-emotional-critic.md`, `poetry-prosody-phonics.md`, `poetry-conciseness-editor.md`, `poetry-form-synthesizer.md`). Note their format: Role, Boundaries, Contracts, Heuristics, Output format, Edge cases.
   - Inspect `skills/ukrainian-poetry/agents/openai.yaml` and `.agents/skills/ukrainian-poetry/agents/openai.yaml` to see how subagents are registered.
   - Inspect `skills/ukrainian-poetry/references/rubric.md` and `AGENTS.md` (6 core poetic principles + 100-point penalty rubric).
   - Define exact specification requirements for `poetry-qa-bot.md`.
2. For R3 (End-to-End Song Creation Bridge):
   - Inspect `skills/poetry-skill/SKILL.md` and `.agents/skills/poetry-skill/SKILL.md`.
   - Determine how section `## End-to-End Song Creation Pipeline` should be structured and placed.
   - Trace the pipeline stages: Idea / theme -> verse generation (ukrainian-poetry) -> quality audit (poetry-qa-bot) -> lyrics adaptation & Spoken Prosody Test (music-lyrics-architect) -> platform selection & prompt synthesis (music-prompt-synthesizer: Suno / Udio / Flow Music) -> 10 AI Quality Gates verification -> DAW stem mixing recommendations (music-daw-mastering-critic).

## Output
Write your comprehensive analysis report to `d:\poetry-skill\.agents\explorer_survey_2\handoff.md`.
Report back when done with send_message.

## 2026-09-06T09:44:14Z
<USER_REQUEST>
You are Explorer 2 investigating R2 (Poetry QA Bot) and R3 (End-to-End Song Creation Bridge).
Your working directory is d:\poetry-skill\.agents\explorer_survey_2.
Read your instructions in d:\poetry-skill\.agents\explorer_survey_2\DISPATCH.md.
Also read d:\poetry-skill\ORIGINAL_REQUEST.md (specifically section ## 2026-09-06T09:42:47Z), AGENTS.md, and GEMINI.md.
Investigate existing agents in skills/ukrainian-poetry/agents/ and .agents/skills/ukrainian-poetry/agents/, openai.yaml registration, rubric.md 100-point penalty rubric, and skills/poetry-skill/SKILL.md.
Write a comprehensive report to d:\poetry-skill\.agents\explorer_survey_2\handoff.md with detailed designs for poetry-qa-bot.md, openai.yaml, and ## End-to-End Song Creation Pipeline.
When done, notify orchestrator_3 via send_message.
</USER_REQUEST>

# Task Assignment: Worker M2_M3 (Poetry QA Bot & End-to-End Song Pipeline)

## 2026-09-06T09:50:00Z

## Working Directory
d:\poetry-skill\.agents\worker_m2_m3

## Context & Request
- Read `d:\poetry-skill\ORIGINAL_REQUEST.md` (specifically section ## 2026-09-06T09:42:47Z).
- Directives: `d:\poetry-skill\AGENTS.md`, `d:\poetry-skill\GEMINI.md`.
- Read Explorer 2 findings & blueprints: `d:\poetry-skill\.agents\explorer_survey_2\handoff.md`.
- Read Scope: `d:\poetry-skill\.agents\orchestrator_3\SCOPE.md`.

## Mandatory Integrity Warning
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

## Exclusive Write Ownership
You exclusively own:
- Creating `skills/ukrainian-poetry/agents/poetry-qa-bot.md` and `.agents/skills/ukrainian-poetry/agents/poetry-qa-bot.md` exactly according to the blueprint in `d:\poetry-skill\.agents\explorer_survey_2\handoff.md` Section 4.1 (6-section canonical schema, YAML frontmatter, 100-point rubric, 14-defect penalty matrix, remediation routing).
- Updating `skills/ukrainian-poetry/agents/openai.yaml` and `.agents/skills/ukrainian-poetry/agents/openai.yaml` to register `poetry-qa-bot` (see blueprint in Section 4.2 of Explorer 2 handoff).
- Updating `tests/test_adversarial_challenger2.py` line 451 to include `"poetry-qa-bot.md"` in the expected agents list.
- Updating `skills/poetry-skill/SKILL.md` and `.agents/skills/poetry-skill/SKILL.md` with section `## 3. End-to-End Song Creation Pipeline` (see blueprint in Section 4.3 of Explorer 2 handoff) with the full 6-stage protocol, ASCII architecture diagram, data contracts, and updating routing table and quick references.

## Verification Required
- Run `py -3 -m unittest tests/test_adversarial_challenger2.py` and verify all tests pass (including subagent schema and openai.yaml registration tests).
- Verify both `skills/` and `.agents/skills/` copies are in exact sync.
- Document all commands and results in `d:\poetry-skill\.agents\worker_m2_m3\handoff.md`.
- Report back when done with send_message.

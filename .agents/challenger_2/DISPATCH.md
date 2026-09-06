# Task Assignment: Challenger 2 (Adversarial Schema, Contracts & Rubric Verifier)

## Working Directory
d:\poetry-skill\.agents\challenger_2

## Context & Request
- Read `d:\poetry-skill\ORIGINAL_REQUEST.md` (specifically section ## 2026-09-06T09:42:47Z).
- Directives: `d:\poetry-skill\AGENTS.md`, `d:\poetry-skill\GEMINI.md`.
- Read Scope: `d:\poetry-skill\.agents\orchestrator_3\SCOPE.md`.

## Mission
Adversarially challenge and verify the subagent schema, contract integrity, and playground units:
1. Run `py -3 -m unittest tests/test_adversarial_challenger2.py`. Assert that all 21 tests pass including schema validation for all 6 subagents in `skills/ukrainian-poetry/agents/`.
2. Run `py -3 -m unittest tests/test_examples_playground.py`. Assert that all 9 unit tests pass.
3. Test edge cases of `poetry-qa-bot.md`: ensure contract specifies behavior for free verse, kolomyika, historical styles, and song metatags.
4. Verify that brackets vs parentheses rule is 100% adhered to across all markdown templates.
5. Emit your verdict: **APPROVE** or **REQUEST_CHANGES** in `d:\poetry-skill\.agents\challenger_2\handoff.md`.
6. Report back when done with send_message.


## 2026-09-06T09:59:45Z
You are Challenger 2 assigned to adversarially challenge schemas, contracts, rubric rules, and playground unit tests.
Your working directory is d:\poetry-skill\.agents\challenger_2.
Read your instructions in d:\poetry-skill\.agents\challenger_2\DISPATCH.md.
Also read d:\poetry-skill\ORIGINAL_REQUEST.md (specifically section ## 2026-09-06T09:42:47Z), AGENTS.md, GEMINI.md, and d:\poetry-skill\.agents\orchestrator_3\SCOPE.md.
Run tests/test_adversarial_challenger2.py and tests/test_examples_playground.py.
Test edge cases of poetry-qa-bot and bracket/parentheses rules across all files.
Write your verdict (APPROVE or REQUEST_CHANGES) and full report to d:\poetry-skill\.agents\challenger_2\handoff.md.
Report back via send_message.

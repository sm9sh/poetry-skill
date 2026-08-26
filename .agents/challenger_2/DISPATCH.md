## 2026-08-26T10:00:11Z

You are Challenger 2 (Suno AI Music Prompt Adversarial Stress-Tester).
Your working directory is `d:/poetry-skill/.agents/challenger_2`.
You MUST read `d:/poetry-skill/.agents/ORIGINAL_REQUEST.md`, `d:/poetry-skill/.agents/PROJECT.md`, and `d:/poetry-skill/TEST_READY.md` before starting work.
Project root: `d:/poetry-skill`.

Task:
Adversarially challenge and stress-test the Suno AI conversion skill, prompt builder, genre mappings, and arrangement templates.

Stress-Test Focus:
1. Test strict character budget bounds under heavy multi-instrumentation constraints (<=120 characters compressed).
2. Test extreme tempo contrasts (60 BPM ambient drone vs 180 BPM metalcore blast beats).
3. Test conflicting multi-constraint prompts (e.g., whispered lullaby metalcore with Ukrainian white voice).
4. Test cross-feature combinations (Tier 3) and real-world production scenarios (Tier 4).
5. Execute the test runner `py -3 tests/run_tests.py --tier 3` and `py -3 tests/run_tests.py --tier 4` (or `--all`).

Deliverables:
- Maintain `progress.md` with `Last visited:` timestamps.
- Write your adversarial challenge report to `d:/poetry-skill/.agents/challenger_2/challenge_report.md`.
- Write your formal handoff to `d:/poetry-skill/.agents/challenger_2/handoff.md` with clear verdict (APPROVE or REQUEST_CHANGES).
- Message parent upon completion.

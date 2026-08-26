## 2026-08-26T09:45:00Z

You are Worker E2E (E2E Testing Track & Test Infrastructure Specialist).
Your working directory is `d:/poetry-skill/.agents/worker_e2e`.
You MUST read `d:/poetry-skill/.agents/ORIGINAL_REQUEST.md` and `d:/poetry-skill/.agents/PROJECT.md` before starting work.
Read the findings in `d:/poetry-skill/.agents/explorer_survey_3/analysis.md`.
Project root: `d:/poetry-skill`.

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

File Write Ownership (You exclusively own these files):
- `TEST_INFRA.md` (at project root)
- `TEST_READY.md` (at project root, publish when suite is complete)
- `tests/` directory (create test cases, validation harnesses, automated verification scripts)

Tasks (Implement Feature F17):
1. **Create `TEST_INFRA.md`**: Master testing architecture covering methodology (Category-Partition, BVA, Pairwise, Real-World Workloads), Feature Inventory mapping (F1-F18), Tier 1-4 breakdown, and scoring rubrics.
2. **Build Automated / Deterministic Validation Harness** in `tests/`:
   - Create a test runner script (e.g. `tests/run_tests.py` or `tests/run_tests.ps1`) that programmatically validates:
     - Style field character count <= 180 chars (optimal 80-150).
     - No non-musical metadata leakage (`Language:`, `Theme:` forbidden in style box).
     - Standard bracketed metatag compliance (`[Intro]`, `[Verse]`, `[Chorus]`, etc.).
     - No banned Russianism / Surzhyk tokens in poetry generated outputs.
     - Clausula alternation compliance and meter consistency checks.
3. **Implement 4-Tier Test Suite in `tests/`**:
   - **Tier 1: Feature Coverage** (>=5 test cases per feature area covering all versification meters, non-syllabo-tonics, fixed forms, registers, Suno genres, vocal timbres, and negative prompts).
   - **Tier 2: Boundary & Corner Cases** (Rare meters like Dactyl/Anapest, 6-word taboo bans, extreme BPM 60 vs 180, 120-char strict Style Box cap, mobile stress homographs like зАмок/замОк).
   - **Tier 3: Cross-Feature Combinations** (Pairwise combinations: Brief -> Lyrics -> Suno Custom Mode Prompt; Folk lyrics + Dark Synth; Cossack Baroque + Melodic Metalcore; Chamber Intimate + Neoclassical Bandura).
   - **Tier 4: Real-World Application Scenarios** (5+ realistic production briefs: e.g. Commercial Folk-Pop Single, Cinematic War Memorial Anthem, Animated Children's Song, Melodic Metalcore Anthem, Ambient Spoken-Word Track).
4. **Execute the Test Harness**: Run the test runner on all test cases and existing test files to establish baseline metrics and verify framework functionality.
5. **Publish `TEST_READY.md`**: Complete coverage table, test runner execution instructions, and test checklist.

Deliverables:
- Maintain `progress.md` with `Last visited:` timestamps.
- Ensure all test files, test runner scripts, `TEST_INFRA.md`, and `TEST_READY.md` are created and fully functional.
- Write a complete 5-component handoff report to `d:/poetry-skill/.agents/worker_e2e/handoff.md`.
- Message parent upon completion.

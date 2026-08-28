## 2026-08-28T08:45:29Z

You are worker_m1 assigned to implement Milestone M1: Integration of 6 Poetic Principles into Skills, Guides, Rubric, and Global Directives.

Your working directory is `d:\poetry-skill\.agents\worker_m1`.
You MUST read `d:\poetry-skill\ORIGINAL_REQUEST.md` and `d:\poetry-skill\PROJECT.md` before starting.
Also review the comprehensive survey and blueprint at `d:\poetry-skill\.agents\survey_explorer_1\survey_r1.md`.

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

Files owned exclusively by you in this milestone:
1. `d:\poetry-skill\skills\ukrainian-poetry\SKILL.md`
2. `d:\poetry-skill\skills\ukrainian-poetry\references\full-guide.md`
3. `d:\poetry-skill\skills\ukrainian-poetry\references\rubric.md`
4. `d:\poetry-skill\skills\poetry-skill\SKILL.md`
5. `d:\poetry-skill\AGENTS.md`

Tasks:
1. Update `AGENTS.md`:
   - Enforce the 6 Poetic Principles as foundational law under Ukrainian Poetry Directives:
     1. Свіжа образність та метафоричність
     2. Емоційна глибина та щирість
     3. Ритмічна та звукова гармонія
     4. Лаконічність і вага слова (заборона штучних інверсій та займенників-заповнювачів)
     5. Оригінальність ракурсу
     6. Органічна єдність форми та змісту
2. Update `skills/poetry-skill/SKILL.md`:
   - Integrate the 6 poetic standards into Core Directives.
3. Update `skills/ukrainian-poetry/SKILL.md`:
   - Embed a dedicated section `## 6 Core Poetic Principles (Фундаментальні принципи майстерності)` with rules, positive examples, and anti-patterns.
   - Update `Task Workflow` to incorporate the 6 principles into generation and self-editing.
   - Add explicit prohibitions against artificial syntactic inversions and filler words in `Rhyme Architecture` and `Self-Edit Checklist`.
4. Update `skills/ukrainian-poetry/references/full-guide.md`:
   - Completely revamp Section 1 to exhaustively detail all 6 principles with theoretical explanations, rules, anti-patterns, and before/after transformation examples.
   - Add a dedicated subsection on Phonics & Soundscapes (фоніка, звукопис, алітерація, асонанс).
   - Add clear guidelines on natural Ukrainian word order and eliminating artificial inversions for rhyme.
5. Update `skills/ukrainian-poetry/references/rubric.md`:
   - Map the 100-point rubric and 7 dimensions directly to the 6 principles.
   - Add explicit deduction categories in the penalty matrix for artificial inversions (-3 to -6 pts), filler pronouns/padding (-2 to -5 pts), and declarative emotion statements (-3 to -6 pts).

Verification:
- Run `py -3 tests/run_tests.py --all` to verify that existing test suites pass with 0 errors and >=95/100 average score.
- Record the exact command and test output in your handoff report.

Write your changes report to `d:\poetry-skill\.agents\worker_m1\changes_m1.md` and complete handoff to `d:\poetry-skill\.agents\worker_m1\handoff.md`.
Send a completion message back to parent when done.

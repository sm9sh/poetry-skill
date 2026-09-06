# Task Assignment: Forensic Auditor (Integrity Forensics)

## Working Directory
d:\poetry-skill\.agents\auditor_1

## Context & Request
- Read `d:\poetry-skill\ORIGINAL_REQUEST.md` (specifically section ## 2026-09-06T09:42:47Z).
- Directives: `d:\poetry-skill\AGENTS.md`, `d:\poetry-skill\GEMINI.md`.
- Read Scope: `d:\poetry-skill\.agents\orchestrator_3\SCOPE.md`.

## Mission
Conduct a thorough forensic audit of the entire solution for integrity violations:
1. Static Code Analysis:
   - Check all new and modified files (`skills/ukrainian-poetry/agents/poetry-qa-bot.md`, `skills/poetry-skill/SKILL.md`, `examples/*`, `tests/sync_ecosystem.py`, `tests/test_examples_playground.py`).
   - Check for hardcoded test results, fake pass values, dummy/facade implementations, or bypassed checks.
2. Authentic Content Check:
   - Verify that all lyrics in `examples/success/` are complete, authentic Ukrainian poetry following the 6 Principles, with real stress accents and genuine artistic depth.
   - Verify that all failure guides in `examples/failures/` contain real, substantive diagnostics and actionable engineering advice.
   - Verify that `poetry-qa-bot.md` is a complete, functioning autonomous auditor specification.
3. Root Directory Cleanliness:
   - Verify that root directory contains zero mirror files and no `packs/` folder.
4. Binary Audit Verdict:
   - Emit either **CLEAN** (no cheating, no facades, authentic logic) or **INTEGRITY VIOLATION**.
    - Write full audit report to `d:\poetry-skill\.agents\auditor_1\handoff.md`.
    - Report back when done with send_message.

## 2026-09-06T09:59:45Z
You are Forensic Auditor 1 assigned to conduct an independent integrity forensics audit.
Your working directory is d:\poetry-skill\.agents\auditor_1.
Read your instructions in d:\poetry-skill\.agents\auditor_1\DISPATCH.md.
Also read d:\poetry-skill\ORIGINAL_REQUEST.md (specifically section ## 2026-09-06T09:42:47Z), AGENTS.md, GEMINI.md, and d:\poetry-skill\.agents\orchestrator_3\SCOPE.md.
Conduct static and runtime integrity checks across all new/modified files. Check for hardcoding, facades, dummy data, or circumvented checks. Check that root is genuinely clean and lyrics are authentic.
Write your binary verdict (CLEAN or INTEGRITY VIOLATION) and full report to d:\poetry-skill\.agents\auditor_1\handoff.md.
Report back via send_message.

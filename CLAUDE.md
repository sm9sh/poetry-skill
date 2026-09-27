# CLAUDE.md — Claude Assistant Guide

Read and follow @AGENTS.md.

## Quick Skill Triggers
- Poetry / versification tasks: `skills/ukrainian-poetry/SKILL.md`.
- Songs for Suno v6-mini / Google Flow Music: `skills/ukrainian-poetry-to-suno/SKILL.md`.

## Verification & Testing
```bash
python3 tests/run_tests.py --all      # Linux / macOS
py -3 tests/run_tests.py --all        # Windows
```
After editing anything in `skills/`, refresh the runtime mirror: `python3 tests/sync_ecosystem.py` (the global Gemini plugin copy only syncs on Windows).

# Design Document: AGENTS.md as Single Source of Truth (SSOT)

**Date**: 2026-08-26  
**Status**: Proposed / Under Review  
**Topic**: Establishing `AGENTS.md` as the canonical Single Source of Truth with lightweight trampoline pointers across agent environments (Claude, Antigravity, Cursor).

---

## 1. Context & Motivation

This repository provides two AI skills (`ukrainian-poetry` and `ukrainian-poetry-to-suno`). Different AI assistant platforms look for specific configuration files:
- Anthropic Claude / Claude Code looks for `CLAUDE.md`.
- Google Antigravity / Gemini CLI looks for `GEMINI.md` or `AGENTS.md`.
- Cursor IDE looks for `.cursorrules` and `.cursor/rules/*.mdc`.
- OpenAI Codex / General Agents look for `AGENTS.md`.

To prevent duplication and rule drift across multiple files, `AGENTS.md` will serve as the canonical **Single Source of Truth (SSOT)**. All other platform files will act as lightweight **pointer/trampoline files** referencing `AGENTS.md`.

---

## 2. Architecture & File Layout

```
d:/poetry-skill/
├── AGENTS.md                  <-- [CANONICAL SSOT: Full rules, guidelines, test commands]
│
├── CLAUDE.md                  <-- [POINTER: Transcludes @AGENTS.md, Claude Code commands]
├── GEMINI.md                  <-- [POINTER: Transcludes AGENTS.md, Antigravity directives]
├── .cursorrules               <-- [POINTER: References AGENTS.md, Cursor context]
└── .cursor/rules/
    └── ukrainian-poetry.mdc   <-- [POINTER: References AGENTS.md]
```

---

## 3. Component Details

### 3.1 `AGENTS.md` (Canonical SSOT)
Contains:
1. **Core Purpose**: Ecosystem overview for Ukrainian poetry and Suno prompt engineering.
2. **Operational Directives**:
   - `ukrainian-poetry`: Ukrainian syntax, syllabo-tonic/dolnik/verlibre versification, accentuation scansion, non-trivial heterogeneous rhymes, anti-sharovarshchyna.
   - `ukrainian-poetry-to-suno`: Western musical genre standard, strict 80–180 character token budget, bracketed metatags, anti-local-pop Exclude vectors.
3. **Reference Navigation**: Links to `skills/ukrainian-poetry/SKILL.md`, `skills/ukrainian-poetry-to-suno/SKILL.md`, and all `references/`.
4. **Verification**: Automated test command (`py -3 tests/run_tests.py --all`).

### 3.2 Pointer Files
Each pointer file:
- Clearly identifies the target assistant.
- Instructs the assistant to read and apply `@AGENTS.md` unconditionally.
- Provides specific assistant execution shortcuts (e.g. Claude test running, Cursor auto-context).

---

## 4. Verification & Testing

1. **Automated Test Suite**: Execute `py -3 tests/run_tests.py --all` to verify that all 59 tests continue to pass with 100% success rate.
2. **Global Plugin Synchronization**: Synchronize the updated files to `~/.gemini/config/plugins/poetry-skill/`.

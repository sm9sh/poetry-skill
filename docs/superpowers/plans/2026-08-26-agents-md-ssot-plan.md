# AGENTS.md Single Source of Truth (SSOT) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Establish `AGENTS.md` as the canonical Single Source of Truth for all Ukrainian poetry and Suno music prompt guidelines, while converting platform-specific files (`CLAUDE.md`, `GEMINI.md`, `.cursorrules`, `.cursor/rules/ukrainian-poetry.mdc`) into clean, lightweight pointer trampolines.

**Architecture:** A single master markdown file (`AGENTS.md`) containing all behavioral directives, rules, skill links, and test commands, with thin pointer files directing Claude, Antigravity, and Cursor agents to load and apply `AGENTS.md`.

**Tech Stack:** Markdown, Python 3 test runner, Git, PowerShell.

## Global Constraints

- `AGENTS.md` is the only file where poetry and Suno prompt directives are defined.
- `CLAUDE.md`, `GEMINI.md`, and `.cursorrules` must reference `@AGENTS.md` and contain only tool-specific execution hooks.
- All 59 automated test cases in `tests/run_tests.py` must pass with 100% success rate.
- All updated files must be synchronized to the global Antigravity plugin directory `~/.gemini/config/plugins/poetry-skill/`.

---

### Task 1: Consolidate Canonical Directives into `AGENTS.md`

**Files:**
- Modify: `d:\poetry-skill\AGENTS.md`

**Interfaces:**
- Produces: Complete master documentation including poetry versification rules, Suno Western genre standards, reference index, and verification commands.

- [ ] **Step 1: Write the updated canonical `AGENTS.md` content**

```markdown
# AGENTS.md — Global Agent Directives for Ukrainian Poetry & Suno Prompting

This repository is an AI Skills ecosystem for authentic Ukrainian poetry generation and production-grade Suno AI / Flow Music prompt engineering.

## Operational Directives

### 1. Ukrainian Poetry Directives (`ukrainian-poetry`)
- **Authenticity First**: Ukrainian syntax, idiomatic expressions, natural word order. Never translate word-for-word from Russian or English.
- **Rhythm & Meter Integrity**: When requested in syllabo-tonic (Iamb, Trochee, Dactyl, Amphibrach, Anapest), non-syllabo-tonic (Dolnik, Taktovik, Kolomyika), or Blank Verse, strictly maintain syllable counts, stresses, and caesuras.
- **Rhyme Discipline**: Avoid banal grammatical rhymes (verb-verb, feminine adjective pairs, diminutive suffixes). Use heterogeneous, acoustic, and slant rhymes.
- **Stress Disambiguation**: Use acute accents (`\u0301`) or capitalization to resolve homographs (*зАмок* vs *замОк*).
- **Zero Sharovarshchyna**: Reject tourist-folk kitsch, pseudo-Cossack cliches, and sentimental Russian-style romance tropes.

### 2. Suno Music Generation Directives (`ukrainian-poetry-to-suno`)
- **Western Genre Anchor**: Musically target Western contemporary and classic genres (UK/US Post-Punk, Darkwave, Synthwave, Trip-Hop, Minimalist Alt-Pop, Shoegaze, Progressive Metalcore, Melodic Techno, Ambient). Music must sound like a top-tier global release, not regional/provincial pop.
- **Token Economy**: `Style of Music` must be strictly **80–180 characters** (optimal 80–150).
- **Field Separation**:
  - `Style of Music`: English Western genre descriptors, BPM, vocal timbre, instruments, production feel.
  - `Lyrics`: Ukrainian text with bracketed metatags (`[Intro]`, `[Verse 1]`, `[Chorus]`, `[Drop]`, `[Outro]`) and parenthetical backing cues `(луна)`.
  - `Exclude`: Anti-local-pop and anti-artifact suppression tokens (`cheesy regional pop, post-soviet schlager, wedding synth brass, cheap accordion, generic euro-pop, metallic highs, muddy bass`).
- **De-identification**: Never output direct artist names or copyright phrases (`in the style of...`).

## Reference Index & Skill Files
- Poetry Skill: `skills/ukrainian-poetry/SKILL.md`
- Suno Conversion Skill: `skills/ukrainian-poetry-to-suno/SKILL.md`
- Reference & Style Cheatsheet: `skills/ukrainian-poetry-to-suno/references/reference-to-style-cheatsheet.md`
- Mood to Style Map: `skills/ukrainian-poetry-to-suno/references/mood-to-style-map.md`
- Prompt Builder: `skills/ukrainian-poetry-to-suno/references/prompt-builder.md`

## Verification & Testing
Run deterministic test suites (Python 3 standard library):
```bash
py -3 tests/run_tests.py --all
```
```

- [ ] **Step 2: Save `AGENTS.md` and verify syntax**

---

### Task 2: Refactor Platform Pointer Files (`CLAUDE.md`, `GEMINI.md`, `.cursorrules`)

**Files:**
- Modify: `d:\poetry-skill\CLAUDE.md`
- Modify: `d:\poetry-skill\GEMINI.md`
- Modify: `d:\poetry-skill\.cursorrules`
- Modify: `d:\poetry-skill\.cursor\rules\ukrainian-poetry.mdc`

**Interfaces:**
- Consumes: Canonical directives in `AGENTS.md`.
- Produces: Minimal trampoline pointers for Claude Code, Antigravity, and Cursor.

- [ ] **Step 1: Update `CLAUDE.md` as pointer**

```markdown
# CLAUDE.md — Claude Assistant Guide

Please read and strictly follow @AGENTS.md for all operational rules, Ukrainian poetry standards, and Suno AI music prompting guidelines.

## Quick Skill Triggers
- Poetry / Versification tasks: Read and apply `skills/ukrainian-poetry/SKILL.md`.
- Suno AI / Flow Music prompting: Read and apply `skills/ukrainian-poetry-to-suno/SKILL.md`.

## Verification & Testing
Run tests via Python 3:
```bash
py -3 tests/run_tests.py --all
```
```

- [ ] **Step 2: Update `GEMINI.md` as pointer**

```markdown
# GEMINI.md — Antigravity & Gemini Agent Configuration

Please read and strictly follow @AGENTS.md for all operational directives, Ukrainian poetry generation, and Suno AI music prompt engineering.

## Rules
- Apply `skills/ukrainian-poetry/SKILL.md` for poetry tasks.
- Apply `skills/ukrainian-poetry-to-suno/SKILL.md` for Suno prompt tasks.
- Run tests: `py -3 tests/run_tests.py --all`
```

- [ ] **Step 3: Update `.cursorrules` and `.cursor/rules/ukrainian-poetry.mdc`**

```markdown
# Cursor Rules
Read and adhere to @AGENTS.md for all Ukrainian poetry and Suno music prompt generation rules.
- Poetry: skills/ukrainian-poetry/SKILL.md
- Suno: skills/ukrainian-poetry-to-suno/SKILL.md
- Tests: py -3 tests/run_tests.py --all
```

---

### Task 3: Synchronize to Antigravity Global Plugin Directory

**Files:**
- Synchronize: `d:\poetry-skill\*` -> `C:\Users\sm9sh\.gemini\config\plugins\poetry-skill\`

- [ ] **Step 1: Execute synchronization command**

```powershell
$dest = 'C:\Users\sm9sh\.gemini\config\plugins\poetry-skill'
Copy-Item -Recurse -Force 'D:\poetry-skill\skills\*' "$dest\skills"
Copy-Item -Force 'D:\poetry-skill\AGENTS.md' "$dest\"
Copy-Item -Force 'D:\poetry-skill\GEMINI.md' "$dest\"
Copy-Item -Force 'D:\poetry-skill\CLAUDE.md' "$dest\"
Copy-Item -Force 'D:\poetry-skill\INSTALL.md' "$dest\"
```

---

### Task 4: Run Test Suite Verification

**Files:**
- Test: `d:\poetry-skill\tests\run_tests.py`

- [ ] **Step 1: Execute all test suites**

Run: `py -3 tests/run_tests.py --all`  
Expected: 59 passed, 0 failed (100% success rate).

# Project: Ukrainian Poetry Skills & 5 Subagents Ecosystem

## Architecture
This project extends the Ukrainian Poetry & Suno Prompting ecosystem (`poetry-skill`) with 6 fundamental principles of poetic craftsmanship and 5 specialized subagent personas, integrated across the skill instructions, reference guides, agent definitions, deterministic validators, and test suites.

```
                  ┌─────────────────────────────────────────────────┐
                  │                 Master Router                   │
                  │           (skills/poetry-skill/SKILL.md)        │
                  │                   (AGENTS.md)                   │
                  └──────────────┬──────────────────┬───────────────┘
                                 │                  │
           ┌─────────────────────▼───────┐   ┌──────▼───────────────────────┐
           │   ukrainian-poetry (Core)   │   │  ukrainian-poetry-to-suno    │
           │  (6 Poetic Craft Principles)│   │  (Suno Prompt Engineering)   │
           └──────────────┬──────────────┘   └──────────────────────────────┘
                          │
          ┌───────────────┴───────────────────────────────┐
          │  5 Specialized Subagents Pipeline             │
          │  (skills/ukrainian-poetry/agents/*.md)        │
          │                                               │
          │  1. poetry-imagery-architect (Образотворець)  │
          │  2. poetry-emotional-critic (Критик щирості)  │
          │  3. poetry-prosody-phonics (Майстер фоніки)   │
          │  4. poetry-conciseness-editor (Редактор)      │
          │  5. poetry-form-synthesizer (Синтезатор)      │
          └───────────────┬───────────────────────────────┘
                          │
          ┌───────────────▼───────────────────────────────┐
          │  Validation & Scoring Engine                  │
          │  (tests/validator/poetic_validator.py)        │
          │  (tests/validator/rubric_scorer.py)           │
          │  (skills/ukrainian-poetry/references/rubric.md│
          └───────────────┬───────────────────────────────┘
                          │
          ┌───────────────▼───────────────────────────────┐
          │  Deterministic Test Suite (62 Tests)          │
          │  (tests/run_tests.py --all)                   │
          └───────────────────────────────────────────────┘
```

---

## Feature Inventory

| # | Feature | Description | Milestone | Status | Source |
|---|---------|-------------|-----------|--------|--------|
| 1 | 6 Poetic Principles in `SKILL.md` | Formalize 6 principles in Ukrainian poetry core skill with rules, self-edit checklist, and anti-patterns | M1 | DONE | ORIGINAL_REQUEST R1 |
| 2 | 6 Principles in `full-guide.md` | Deep dive theory, before/after examples, acoustic phonics, and anti-inversion rules in reference guide | M1 | DONE | ORIGINAL_REQUEST R1 |
| 3 | 6 Principles in `rubric.md` | Align 100-point rubric breakdown and penalty deductions with the 6 principles | M1 | DONE | ORIGINAL_REQUEST R1 |
| 4 | Master Directives in `AGENTS.md` & `poetry-skill/SKILL.md` | Update repository SSOT and top-level skill router with the 6 mandatory quality standards | M1 | DONE | ORIGINAL_REQUEST R1 |
| 5 | `poetry-imagery-architect` | Subagent persona: tactile imagery, fresh metaphors, anti-cliche guardrails | M2 | DONE | ORIGINAL_REQUEST R2 |
| 6 | `poetry-emotional-critic` | Subagent persona: sincerity, zero-pathos, anti-moralizing, psychological micro-details | M2 | DONE | ORIGINAL_REQUEST R2 |
| 7 | `poetry-prosody-phonics` | Subagent persona: meter consistency, stress accuracy, acoustic euphony (у/в, і/й), heterogeneous rhymes | M2 | DONE | ORIGINAL_REQUEST R2 |
| 8 | `poetry-conciseness-editor` | Subagent persona: word economy, anti-water, eliminating filler pronouns and artificial inversions | M2 | DONE | ORIGINAL_REQUEST R2 |
| 9 | `poetry-form-synthesizer` | Subagent persona: form-content harmony, paradoxical endings, novel perspective, pipeline aggregation | M2 | DONE | ORIGINAL_REQUEST R2 |
| 10 | Pipeline Orchestration & Subagent Registration | Register 5 subagents in `openai.yaml`, commands, and define sequential/modular pipeline flow | M2 | DONE | ORIGINAL_REQUEST R2 |
| 11 | Poetic Validator Updates | Implement deterministic checks for artificial inversions, filler pronouns/words, and sensory details | M3 | DONE | ORIGINAL_REQUEST R3 |
| 12 | Rubric Scorer Calibration | Update `RubricScorer.score_poetry` with refined 7-dimension scoring logic and penalty bounds | M3 | DONE | ORIGINAL_REQUEST R3 |
| 13 | Test Suite Enhancements | Update/add test scenarios for new criteria while ensuring 100% backward compatibility with Suno pipeline | M3 | DONE | ORIGINAL_REQUEST R3 |
| 14 | E2E Regression & Quality Verification | Full test suite execution (`py -3 tests/run_tests.py --all`): 62 tests pass, 0 errors, >=95/100 avg score | M4 | DONE | ORIGINAL_REQUEST Acceptance |

---

## Milestones

| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| M1 | R1: Skill & Reference Integration | `skills/ukrainian-poetry/SKILL.md`, `references/full-guide.md`, `references/rubric.md`, `skills/poetry-skill/SKILL.md`, `AGENTS.md` | none | DONE |
| M2 | R2: 5 Subagents & Pipeline | `skills/ukrainian-poetry/agents/*.md`, `openai.yaml`, `skills/ukrainian-poetry/SKILL.md`, `AGENTS.md` | M1 | DONE |
| M3 | R3: Validator & Rubric Scorer | `tests/validator/poetic_validator.py`, `tests/validator/rubric_scorer.py`, `tests/` | M1, M2 | DONE |
| M4 | R4: E2E Verification & Final Audit | Full test suite execution, multi-agent review, challenger validation, forensic integrity audit | M1, M2, M3 | DONE |

---

## Interface Contracts

### 1. 6 Poetic Principles Standard
1. **Свіжа образність та метафоричність**: Show, don't tell; authorial unexpected metaphors; tactile sensory anchors; zero hackneyed cliches (*кров-любов*, *троянди-сльози*).
2. **Емоційна глибина та щирість**: Authentic psychological truth; zero theatrical pathos or moralizing sermonizing; micro-details instead of loud declarations.
3. **Ритмічна та звукова гармонія**: Breathing prosody; rich heterogeneous, acoustic, and slant rhymes; deliberate phonics (alliteration, assonance, soundscapes).
4. **Лаконічність і вага слова**: High semantic compression; zero filler pronouns (*цей, той, свій*) or rhythmic padding (*і ось*, *ну от*); zero artificial inversions for rhyme.
5. **Оригінальність ракурсу**: Unconventional perspective on universal themes; paradoxical or open endings; shifting focus from macro-abstractions to revealing micro-details.
6. **Органічна єдність форми та змісту**: Form (meter, stanza structure, caesura, enjambment, speed) intrinsically mirrors emotional dynamics and theme.

### 2. Subagent Contract Interface
Every subagent specification in `skills/ukrainian-poetry/agents/` adheres to:
- YAML Frontmatter: `name`, `description`, `<example>`, negative constraints, `model: gemini-2.5-pro`, `temperature: 0.7`.
- Markdown Sections:
  1. `Role & Identity` (Ukrainian name and mission)
  2. `Scope & Boundaries` (what it does and does NOT do)
  3. `Input Contract` (raw prompt, poem draft, metadata)
  4. `Operational Rules & Heuristics` (concrete actionable checks, `❌ До ➔ ✅ Після` transformations)
  5. `Output Contract` (5-part structured report: critique, sensory/prosodic/stylistic analysis, proposed edits, metrics)
  6. `Edge-Case Handling` (archaic/folk styles, song lyrics, verlibres, blank verse)

### 3. Validator & Scorer Interface
- `PoeticValidator`: Pure Python 3 standard library; methods return `(passed: bool, message: str, details: dict)`.
  - `check_artificial_inversions(text, mode)`
  - `check_filler_words_and_pronouns(text, mode)`
  - `check_cliche_rhymes(text)`
  - `evaluate_sensory_grounding(text)`
- `RubricScorer.score_poetry(text, poetic_res, mode, is_free_verse)`: Returns dict with 7 dimension scores and `total_score` in `[0.0, 100.0]`. Passing threshold `>= 85.0`, suite average `>= 95.0` (achieved `98.1 / 100`).

---

## Code Layout

- `AGENTS.md` — Global repository SSOT directives.
- `skills/poetry-skill/SKILL.md` — Master ecosystem skill router.
- `skills/ukrainian-poetry/SKILL.md` — Core Ukrainian poetry skill instruction.
- `skills/ukrainian-poetry/references/full-guide.md` — In-depth guide & reference manual.
- `skills/ukrainian-poetry/references/rubric.md` — 100-point evaluation rubric.
- `skills/ukrainian-poetry/agents/` — 5 specialized subagent prompt files:
  - `poetry-imagery-architect.md`
  - `poetry-emotional-critic.md`
  - `poetry-prosody-phonics.md`
  - `poetry-conciseness-editor.md`
  - `poetry-form-synthesizer.md`
  - `openai.yaml` — Agent registry definition.
- `tests/validator/poetic_validator.py` — Deterministic poetic validation engine.
- `tests/validator/rubric_scorer.py` — 100-point rubric scoring engine.
- `tests/validator/style_validator.py` & `metatag_validator.py` — Suno prompt validators.
- `tests/run_tests.py` — Test runner.
- `tests/tier1_feature_coverage/` through `tests/tier4_real_world/` — Test case definitions (62 tests).
- `tests/test_adversarial_challenger1.py` & `tests/test_adversarial_challenger2.py` — Adversarial test suites.

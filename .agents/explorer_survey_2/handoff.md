# Handoff Report: Explorer Survey 2 — Poetry QA Bot (R2) & End-to-End Song Creation Bridge (R3)

**Author**: Explorer 2  
**Working Directory**: `d:\poetry-skill\.agents\explorer_survey_2`  
**Date**: 2026-09-06  
**Parent / Recipient**: `orchestrator_3` (`79ba3c17-08be-449c-b213-0cd03aa4a10d`)  
**Scope**: Detailed Investigation, Gap Analysis, and Complete Architectural Blueprints for:
1. **R2: Poetry QA Bot (`poetry-qa-bot.md` and `openai.yaml`)**
2. **R3: End-to-End Song Creation Pipeline in `skills/poetry-skill/SKILL.md`**

---

## 1. Observation

### 1.1 Source Directives & Original Requirements
Directives extracted from `d:\poetry-skill\ORIGINAL_REQUEST.md` (Section `## 2026-09-06T09:42:47Z`, lines 122–130):
> **R2. Агент контролю якості Poetry QA Bot**:
> - Створити файл специфікації субагента `poetry-qa-bot.md` у `skills/ukrainian-poetry/agents/` та `.agents/skills/ukrainian-poetry/agents/`.
> - Зареєструвати агента у `skills/ukrainian-poetry/agents/openai.yaml` та `.agents/skills/ukrainian-poetry/agents/openai.yaml`.
> - Агент повинен діяти як автономний аудитор: приймати віршований текст, сканувати його на відповідність 6 принципам майстерності, застосовувати 100-бальну матрицю штрафів з `rubric.md` та повертати деталізований скоринг-звіт із балами по кожному критерію і конкретними покроковими рекомендаціями щодо покращення.
>
> **R3. Наскрізний пайплайн створення пісні (End-to-End Song Creation Bridge)**:
> - Оновити головний оркестратор `skills/poetry-skill/SKILL.md` та `.agents/skills/poetry-skill/SKILL.md`, додавши розділ `## End-to-End Song Creation Pipeline`.
> - Задокументувати повний єдиний протокол: «Ідея / тема → генерація вірша (ukrainian-poetry) → аудит якості (poetry-qa-bot) → адаптація лірики та Spoken Prosody Test (music-lyrics-architect) → вибір платформи та синтез промптів (music-prompt-synthesizer: Suno / Udio / Flow Music) → перевірка 10 AI Quality Gates → рекомендації DAW-зведення (music-daw-mastering-critic)».

### 1.2 Inspection of Existing Subagents (`skills/ukrainian-poetry/agents/`)
Inspection of the 5 existing subagents reveals a strict, standardized structural pattern:
1. `poetry-imagery-architect.md` (148 lines, 10,804 bytes)
2. `poetry-emotional-critic.md` (136 lines, 9,503 bytes)
3. `poetry-prosody-phonics.md` (197 lines, 14,444 bytes)
4. `poetry-conciseness-editor.md` (141 lines, 9,892 bytes)
5. `poetry-form-synthesizer.md` (159 lines, 11,320 bytes)

Every agent specification strictly adheres to:
- **YAML Frontmatter**:
  - `name`: string identifier
  - `description`: multiline summary containing `<example>...</example>` block and `Do NOT use this agent for:` negative boundary bullet points.
  - `model`: `gemini-2.5-pro`
  - `temperature`: float (0.2–0.7 depending on role determinism)
  - `max_output_tokens`: `4096`
- **Mandatory Markdown Headings (6 canonical sections)**:
  - `## 1. Role & Identity`: Ukrainian title, core mission, guiding principles from the 6 Core Principles, philosophical grounding.
  - `## 2. Scope & Boundaries`: `### What This Agent Owns` vs `### What This Agent Does NOT Do (Boundaries)`.
  - `## 3. Input Contract`: YAML codeblock defining schema, types, descriptions, and constraints.
  - `## 4. Operational Rules & Heuristics`: Detailed transformation rules, tables, anti-patterns (`❌` vs `✅`).
  - `## 5. Output Contract`: Markdown codeblock defining the exact structure of emitted outputs.
  - `## 6. Edge-Case Handling`: Explicit edge cases (e.g. classical forms, free verse, folk meters, song adaptation).

### 1.3 Inspection of Subagent Test Constraints (`tests/test_adversarial_challenger2.py`)
Lines 446–507 of `tests/test_adversarial_challenger2.py` programmatically enforce the subagent structure:
- Lines 451–457: List of expected agents.
- Lines 459–466: Mandatory sections array:
  `["## 1. Role & Identity", "## 2. Scope & Boundaries", "## 3. Input Contract", "## 4. Operational Rules & Heuristics", "## 5. Output Contract", "## 6. Edge-Case Handling"]`.
- Lines 483–489: Assertions for frontmatter keys (`name:`, `description:`, `<example>`, `Do NOT use this agent for:`, `model: gemini-2.5-pro`, `temperature:`, `max_output_tokens:`).
- Lines 496–498: Assertion that Section 3 contains ````yaml` and Section 5 contains ````markdown`.
- Lines 500–506: Assertion that `openai.yaml` exists and registers each agent name.

### 1.4 Inspection of `openai.yaml`
In `skills/ukrainian-poetry/agents/openai.yaml` (lines 1–31):
```yaml
interface:
  display_name: "Ukrainian Poetry"
  short_description: "Write, analyze, and refine authentic Ukrainian poetry with 6 core principles"
  default_prompt: "Use $ukrainian-poetry to write a natural Ukrainian poem from this topic."

agents:
  poetry-imagery-architect: ...
  poetry-emotional-critic: ...
  poetry-prosody-phonics: ...
  poetry-conciseness-editor: ...
  poetry-form-synthesizer: ...
```
Each entry requires:
- `display_name`: string (e.g., `"Poetry QA Bot (Аудитор якості)"`)
- `short_description`: string
- `default_prompt`: string (e.g., `"Use $poetry-qa-bot to audit this Ukrainian poem against the 6 core principles..."`)

### 1.5 Inspection of Evaluation Rubric & Penalty Matrix (`skills/ukrainian-poetry/references/rubric.md`)
The rubric defines 7 core dimensions (total 100 points) and a 14-item penalty deduction matrix:
- **Dimension 1: Природність української мови, наголоси й синтаксис (П4)** — 25 балів
- **Dimension 2: Свіжа образність, тактильна конкретика та показ (П1)** — 20 балів
- **Dimension 3: Метроритмічна дисципліна, дихання та єдність форми/змісту (П3/6)** — 15 балів
- **Dimension 4: Рима, клаузули, фоніка та звукова гармонія (П3)** — 10 балів
- **Dimension 5: Емоційна глибина, щирість та автентичність регістру (П2)** — 10 балів
- **Dimension 6: Оригінальність ракурсу, сила й парадоксальний резонанс фіналу (П5)** — 10 балів
- **Dimension 7: Антиштампи, антишароварщина та авторська самобутність (П1/5)** — 10 балів
- **Penalty Matrix (Deductions)**:
  1. *Метричний збій*: -5 to -15 pts
  2. *Хибний наголос (Русизм)*: -5 to -10 pts per case (`випАдок`, `чорнозЕм`, `новИй`, `одИннадцять`, `листопАд`)
  3. *Змішування омографів*: -5 pts (`замОк` vs `зАмок`)
  4. *Однорідна дієслівна рима*: -3 to -8 pts (`знати-кохати`)
  5. *Пестливі суфікси в римі*: -4 pts (`-очка/-енька`)
  6. *Банальна пара з блекліста*: -5 pts (`любов-кров`, `доля-воля`, `день-пень`)
  7. *Штучна синтаксична інверсія*: -3 to -6 pts (`«сонце ясне зійшло»`, `«погляд свій сумний підвів»`)
  8. *Займенники-заповнювачі / "вода"*: -2 to -5 pts (`я, мій, цей, той, свій, вже, ось`)
  9. *Декларування емоцій*: -3 to -6 pts (Telling instead of showing)
  10. *Фальшивий / театральний пафос*: -5 to -10 pts (Hysteria, exclamation storms)
  11. *Моралізаторський фінал*: -5 pts (`«пам'ятай завжди»`, `«і я збагнув, що треба жити»`)
  12. *Шароварщина та кітч*: -10 pts (Souvenir pseudo-patriotism)
  13. *Синтаксична калька*: -5 to -15 pts (`по вечорах`, `приймати участь`)
  14. *Монотонні клаузули*: -3 to -5 pts (Blocks of `ЖЖЖЖ` or `ЧЧЧЧ`)
- Scoring logic verified in Python: `tests/validator/rubric_scorer.py` (lines 41–157).

### 1.6 Inspection of Music Subagents (`skills/ukrainian-poetry-to-suno/agents/`)
We observed that the music generation module has its own 4 subagents registered in `skills/ukrainian-poetry-to-suno/agents/openai.yaml`:
- `music-reference-engineer` (Reference DNA extraction, Step 1)
- `music-lyrics-architect` (AI song lyrics adaptation, Spoken Prosody Test, Step 2)
- `music-prompt-synthesizer` (Multi-platform prompt generation: Suno/Udio/Flow Music, Step 3)
- `music-daw-mastering-critic` (DAW stem mixing & True Peak mastering audit, Steps 4–6)

### 1.7 Current Master Orchestrator (`skills/poetry-skill/SKILL.md`)
Currently, `skills/poetry-skill/SKILL.md` (68 lines) has:
- Section 1: `## 1. Sub-Skill Routing` (3-row table)
- Section 2: `## 2. Core Directives Summary`
- Section 3: `## 3. Quick Reference`
Missing: An explicit, actionable, step-by-step protocol section detailing the unified multi-agent bridge between Ukrainian poetry creation and AI music production.

### 1.8 Baseline Test Suite Execution
Execution command: `py -3 tests/run_tests.py --all`
Result: **75 test cases, 75 passed, 0 failed, 0 errors, 100% success rate** (Average Poetry Score: 98.2/100, Average Suno Score: 99.8/100).

---

## 2. Logic Chain

1. **Schema and Contract Synchronization**:
   - `test_adversarial_challenger2.py` enforces that all agents in `skills/ukrainian-poetry/agents/` must have exact YAML frontmatter keys, 6 specific section headings, a ````yaml` input block, and a ````markdown` output block.
   - Therefore, `poetry-qa-bot.md` must be designed with 100% adherence to this exact schema to prevent test regressions.

2. **Functional Boundary: Synthesizer vs QA Bot**:
   - `poetry-form-synthesizer` is a *creative assembler and mediator* that harmonizes outputs from upstream specialists during generation and self-evaluates a new draft.
   - `poetry-qa-bot` is an *autonomous, neutral quality auditor*. It does not create poems or negotiate artistic compromises. Instead, it ingests ANY poem, scans it forensically against the 6 principles and 14 penalty categories, outputs a detailed scorecard, and produces a prioritized, actionable remediation blueprint with exact line-by-line rewrite recipes and subagent delegation tags.
   - Operating temperature must be set to deterministic low (`0.2`).

3. **Autonomous Rubric Scorer Integration**:
   - The bot's logic must mirror both the human evaluation standards of `skills/ukrainian-poetry/references/rubric.md` and the programmatic rules in `tests/validator/rubric_scorer.py`.
   - The scorecard must provide the 7 dimension scores, itemize every defect with exact line numbers and penalty deductions, state the final score / 100, and evaluate Pass/Fail against the Master-level threshold ($\ge 90/100$).

4. **Bridging Ukrainian Poetry & AI Music Generation (R3)**:
   - The user request requires a unified end-to-end song creation bridge linking the two major halves of the repository.
   - The sequence is strictly sequential:
     $$\text{Idea} \longrightarrow \text{Poem Generation (ukrainian-poetry)} \longrightarrow \text{Quality Audit (poetry-qa-bot)} \longrightarrow \text{Lyrics Adaptation (music-lyrics-architect)} \longrightarrow \text{Platform Prompts (music-prompt-synthesizer)} \longrightarrow \text{10 Quality Gates} \longrightarrow \text{DAW/Mastering (music-daw-mastering-critic)}$$
   - This bridge must be documented as Section `## 3. End-to-End Song Creation Pipeline` in `skills/poetry-skill/SKILL.md` (and `.agents/skills/poetry-skill/SKILL.md`), detailing data contracts, artifact flow, timing rules, bracket conventions, and remediation loops.

---

## 3. Caveats

1. **Dual Directory Synchronization**:
   - The repository maintains canonical skills in `skills/` and agent-visible copies in `.agents/skills/`. Any new agent file or skill edit must be written to both directories, or synchronized via `tests/sync_ecosystem.py`.
2. **Read-Only Explorer Scope**:
   - As an Explorer agent, I am presenting the complete, verified, drop-in designs within this report. The actual implementation edits must be applied by the designated Worker/Editor agent or during the orchestration phase.
3. **Test Suite Scope**:
   - When `poetry-qa-bot.md` is added, `tests/test_adversarial_challenger2.py` should be updated to include `"poetry-qa-bot.md"` in its `expected_agents` array (line 451) so that its schema is continuously protected by automated CI tests.

---

## 4. Conclusion & Detailed Designs

Below are the complete, production-ready specifications and file contents ready for drop-in implementation.

---

### Design 4.1: Complete Specification for `poetry-qa-bot.md`
**Target Paths**:
- `d:\poetry-skill\skills\ukrainian-poetry\agents\poetry-qa-bot.md`
- `d:\poetry-skill\.agents\skills\ukrainian-poetry\agents\poetry-qa-bot.md`

```markdown
---
name: poetry-qa-bot
description: |
  Autonomous Ukrainian poetry quality assurance auditor (Аудитор поетичної якості).
  Conducts forensic scansion, audits compliance with the 6 Core Poetic Principles, applies the 100-point penalty rubric from references/rubric.md, and outputs an itemized scorecard with prioritized remediation recipes.
  
  <example>
  orchestrator: dispatches poetry-qa-bot on a draft containing "випАдок", forced inversion "погляд свій сумний підвів", and cliché "кров-любов".
  output: detects 3 defects, deducts 18 penalty points, outputs 7-dimension scorecard (82/100 FAIL), and delivers line-by-line remediation recipes with specialist routing.
  </example>

  Do NOT use this agent for:
  - Generating initial poetic drafts from scratch (use ukrainian-poetry or poetry-imagery-architect)
  - Creative stanza expansion or artistic assembly (use poetry-form-synthesizer)
  - Converting poems into AI music prompt styles or metatags (use skills/ukrainian-poetry-to-suno)
  - DAW audio stem engineering and mastering audits (use music-daw-mastering-critic)
model: gemini-2.5-pro
temperature: 0.2
max_output_tokens: 4096
---

# Poetry QA Bot (Аудитор поетичної якості)

## 1. Role & Identity

**Ukrainian Title**: Автономний аудитор поетичної якості та відповідності 6 принципам  
**Core Mission**: Conduct an objective, forensic, and uncompromising quality audit of Ukrainian poetic texts against all **6 Core Poetic Principles**, apply the strict 100-point penalty rubric from `references/rubric.md`, calculate exact dimension scores and itemized penalty deductions, and deliver an actionable step-by-step remediation blueprint.  
**Guiding Principles**: All 6 Core Principles:
1. **Свіжа образність та метафоричність (Fresh Imagery & Metaphoricity)**
2. **Емоційна глибина та щирість (Emotional Depth & Sincerity)**
3. **Ритмічна та звукова гармонія (Rhythmic & Phonic Harmony)**
4. **Лаконічність і вага слова (Conciseness & Word Weight)**
5. **Оригінальність ракурсу (Originality of Perspective)**
6. **Органічна єдність форми та змісту (Organic Unity of Form & Content)**

Poetry QA Bot діє як безсторонній верховний контролер поетичної якості. На відміну від творчих агентів-генераторів, QA Bot не шукає естетичних компромісів: він виявляє найменші порушення орфоепії, приховані русизми, збої метра, штучні інверсії, баластні слова та фальшивий пафос, гарантуючи відповідність тексту найвищому рівню майстерності (Master-level $\ge 90/100$).

---

## 2. Scope & Boundaries

### What This Agent Owns:
- **Forensic Prosodic & Metric Scansion**: Auditing foot regularity, syllable count variance, ictus stability (iamb, trochee, dactyl, amphibrach, anapest, dolnik, taktovik, kolomyika, verlibre cadence), and natural pyrrhic distribution.
- **Normative Stress & Accentuation Audit**: Detecting Russianized stress displacements (*випАдок*, *чорнозЕм*, *новИй*, *одИннадцять*, *листопАд*) and homograph confusion (*зАмок* vs *замОк*, *плАчу* vs *плачУ*).
- **Acoustic Euphony & Phonotactics Check**: Enforcing alternation rules for `у/в`, `і/й`, `з/із/зі`, checking for hiatus (unpleasant vowel collisions), and flagging harsh consonant clumping.
- **Rhyme Taxonomy & Clausula Audit**: Penalizing primitive verb-verb rhymes (*знати-кохати*), suffixal diminutives (*-очка/-енька*), blacklist cliché pairs (*кров-любов*, *доля-воля*), and monotonic clausula blocks (`ЖЖЖЖ`/`ЧЧЧЧ`).
- **Syntax & Natural Word Order Audit**: Strictly identifying and penalizing artificial inversions created to force end-rhymes (*«сонце ясне зійшло»*, *«погляд свій сумний підвів»*).
- **Conciseness & Padding Purge**: Detecting rhythmic filler pronouns (*я, мій, твій, цей, той, свій*), empty particles (*ось, от, то, ж*), and redundant adverbs (*вже, так, дуже*).
- **Sensory Tactility & Anti-Abstraction Audit**: Detecting abstract emotional declarations (*«душа плаче»*, *«серце палає»*) and verifying physical "show-don't-tell" realia.
- **Emotional Sincerity & Anti-Pathos Audit**: Excising theatrical melodrama, exclamation storms, and preachy/moralizing conclusions (*«і я збагнув, що треба жити»*).
- **Anti-Sharovarshchyna & Kitsch Filter**: Purging tourist souvenir patriotism and pseudo-folk clichés.
- **100-Point Scorecard Computation**: Calculating scores across all 7 dimensions and applying the 14-item deduction matrix.
- **Remediation Routing Engine**: Providing exact line-by-line correction recipes and delegating fixes to specialized pipeline agents.

### What This Agent Does NOT Do (Boundaries):
- Does NOT write original poems from scratch (delegated to `ukrainian-poetry` or specialist pipeline).
- Does NOT rewrite the full poem arbitrarily; it suggests surgical line replacements while preserving the author's vision.
- Does NOT construct music style prompts or exclude tags (delegated to `skills/ukrainian-poetry-to-suno`).
- Does NOT audit post-generation audio stems, mixing phase, or mastering LUFS (delegated to `music-daw-mastering-critic`).

---

## 3. Input Contract

```yaml
poem_text: string            # Mandatory: Complete Ukrainian poetic text to audit
target_form: string          # Optional: Expected form (regular | sonnet | blank-verse | kolomyika | dolnik | taktovik | verlibre)
target_meter: string         # Optional: Expected meter (iamb | trochee | dactyl | amphibrach | anapest | dolnik | kolomyika | free)
register: enum               # Optional: contemporary-urban | chamber-intimate | philosophical-neoclassical | baroque-cossack | folk-authentic | children-playful
passing_threshold: integer   # Default: 90 (Master-level standard) or 85 (minimum acceptable)
context_or_intent: string    # Optional: Original prompt or thematic brief for context verification
```

---

## 4. Operational Rules & Heuristics

### 4.1 Six-Principle Audit Matrix

| Principle | Inspection Focus | Verification Standard | Failure Trigger |
| :--- | :--- | :--- | :--- |
| **П1: Свіжа образність** | Sensory anchors across 5 modalities; fresh authorial metaphors. | "Show, don't tell"; physical objects with weight, texture, temperature. | Abstract declarations (*«серце болить»*, *«душа плаче»*); worn tropes (*«море сліз»*). |
| **П2: Емоційна глибина** | Sincerity, psychological nuance, understated dignity (*тиха лірика*). | Restrained empathy; actions speak for emotions; zero theatricality. | Melodrama, hysteria, exclamation marks (`!`, `!!!`), pedagogical moralizing. |
| **П3: Звукова гармонія** | Metric foot consistency; orthoepic stresses; heterogeneous rhymes; euphony. | Verified stresses (*вИпадок*); cross-grammatical rhymes; balanced `у/в`, `і/й`. | Broken meter; Russianized stresses; verb-verb rhymes; hiatus; consonant clumping. |
| **П4: Лаконічність і вага** | High semantic density; natural Ukrainian phrase melody; zero padding. | Inviolable natural word order; every word carries indispensable meaning. | Artificial inversions for rhyme; filler pronouns (*цей, той, свій*) to pad foot count. |
| **П5: Оригінальність ракурсу** | Novel authorial angle; defamiliarization (*очуднення*); micro-focus. | Focus on revealing micro-details; open, lingering, or paradoxical endings. | Predictable cliches; panoramic banality; naive didactic conclusion (*«треба жити»*). |
| **П6: Єдність форми й змісту**| Harmony between rhythm/stanza dynamics and psychological state. | Tempo, caesuras, and line breaks mirror the emotional tension. | Mismatched form (e.g. bouncy playful trochee with diminutives for tragic grief). |

### 4.2 The 14-Category Penalty Deduction Matrix

Every detected defect incurs an immutable deduction from the 100-point total:

| Code | Defect Category | Detailed Description & Trigger | Deduction |
| :--- | :--- | :--- | :--- |
| **D01** | **Метричний збій** | Syllable drop/addition, broken foot skeleton, high variance in syllabo-tonics. | **-5 to -15 pts** |
| **D02** | **Хибний наголос (Русизм)** | Orthoepic stress error (*випАдок*, *чорнозЕм*, *новИй*, *одИннадцять*, *листопАд*). | **-5 to -10 pts / each** |
| **D03** | **Змішування омографів** | Accidental stress homograph confusion (*замОк* vs *зАмок*, *плАчу* vs *плачУ*). | **-5 pts** |
| **D04** | **Однорідна дієслівна рима** | Grammatical verb-verb pairs (*знати-кохати*, *прийшла-розцвіла*, *летять-горять*).| **-3 to -8 pts** |
| **D05** | **Пестливі суфікси в римі** | Diminutives used merely to force rhyme (*-очка/-ечка*, *-енька/-онька*). | **-4 pts** |
| **D06** | **Банальна пара з блекліста** | Forbidden cliché rhymes (*любов-кров*, *доля-воля*, *серце-перце*, *день-пень*). | **-5 pts** |
| **D07** | **Штучна синтаксична інверсія**| Unnatural distorted word order forced for rhyme (*«погляд свій сумний підвів»*). | **-3 to -6 pts** |
| **D08** | **Займенники-заповнювачі** | Rhythmic padding words (*я, мій, цей, той, свій, вже, ось, то, ж*). | **-2 to -5 pts** |
| **D09** | **Декларування емоцій** | Abstract telling instead of showing (*«моє серце розривається від болю»*). | **-3 to -6 pts** |
| **D10** | **Фальшивий / гучний пафос** | Operatic declamation, emotional hysteria, poster slogans. | **-5 to -10 pts** |
| **D11** | **Моралізаторський фінал** | Preachy, didactical conclusion (*«пам'ятай завжди»*, *«і я збагнув, що треба жити»*).| **-5 pts** |
| **D12** | **Шароварщина та кітч** | Souvenir decorative pseudo-patriotism (*калина-гопак-сало* as kitsch decor). | **-10 pts** |
| **D13** | **Синтаксична калька** | Structural Russianisms (*по вечорах*, *приймати участь*, *на протязі часу*). | **-5 to -15 pts** |
| **D14** | **Монотонні клаузули** | 4-line blocks of unvaried line endings (`ЖЖЖЖ` or `ЧЧЧЧ`). | **-3 to -5 pts** |

### 4.3 Deterministic Scansion Protocol
1. **Syllabic Scansion**: Count vowels per line. Mark non-syllabic `й` and ignore soft signs (`ь`).
2. **Stress Verification**: Compare against normative Ukrainian orthoepic dictionaries. Flag Russianized stresses immediately.
3. **Ictus & Interval Scansion**:
   - Syllabo-tonic: verify regular feet + valid pyrrhics (`U U`).
   - Dolnik: ensure unstressed intervals between ictuses are strictly 1 or 2 syllables.
   - Kolomyika: enforce `(4+4)+6` structure with mandatory caesura after syllable 8.
4. **Euphony Verification**: Check alternating `у/в`, `і/й`, `з/із/зі`. Flag hiatus ($>1$ vowel clash at word boundary).
5. **Rhyme & Clausula Classification**: Classify parts of speech in rhymes. Ensure alternating endings (`ЖЧЖЧ`).
6. **Syntax & Lexical Density Check**: Flag inverted phrases and measure filler token density.
7. **Score Calculation**: Subtract deductions from dimension ceilings; compute total score.

### 4.4 Remediation Routing Engine
When defects are detected, QA Bot assigns remediation tasks to the specialized subagents:
- Metric or Stress Defects (`D01`, `D02`, `D03`, `D04`, `D14`) $\to$ Route to `poetry-prosody-phonics`.
- Inversions and Filler Padding (`D07`, `D08`, `D13`) $\to$ Route to `poetry-conciseness-editor`.
- Abstract Clichés & Telling (`D06`, `D09`, `D12`) $\to$ Route to `poetry-imagery-architect`.
- Pathos & Didactic Conclusions (`D10`, `D11`) $\to$ Route to `poetry-emotional-critic`.
- Global Architectural Re-assembly $\to$ Route to `poetry-form-synthesizer`.

---

## 5. Output Contract

Poetry QA Bot outputs a structured, actionable markdown audit report:

```markdown
# 📋 Звіт контролю якості поетичного твору (Poetry QA Audit Report)

### 1. Загальний вердикт (Executive Summary)
- **Підсумковий бал**: [Score] / 100
- **Статус**: [PASS (Master-level $\ge 90$) | CONDITIONAL PASS (85–89) | FAIL ($<85$)]
- **Головний дефект / вузьке місце**: [One-line summary of key issue or "Жодних критичних дефектів не виявлено"]

### 2. Оцінна відомість за 7 вимірами (Dimension Scorecard)
======================================================
ОЦІННА ВІДОМІСТЬ УКРАЇНСЬКОЇ ПОЕЗІЇ (6 ПРИНЦИПІВ)
======================================================
1. Природність мови, наголоси й синтаксис (П4): [X] / 25
2. Образність, конкретика й показ (П1):         [X] / 20
3. Ритм, рядкоподіл і єдність форми/змісту (П3/6): [X] / 15
4. Рима, клаузули та звукопис/фоніка (П3):      [X] / 10
5. Емоційна глибина, щирість і регістр (П2):    [X] / 10
6. Оригінальність ракурсу та сила фіналу (П5):  [X] / 10
7. Антиштампи, антишароварщина й самобутність (П1/5): [X] / 10
------------------------------------------------------
Проміжний бал:                                  [Subtotal] / 100
Штрафні відрахування (дефекти):                -[Deductions] балів
------------------------------------------------------
ЗАГАЛЬНИЙ ПІДСУМКОВИЙ БАЛ:                      [Final Score] / 100
======================================================
Рівень якості: [Master-level (90-100) | Production-ready (80-89) | Needs Revision (<80)]

### 3. Деталізований реєстр виявлених дефектів (Itemized Defect Log)
- **[Code: DXX]** [Рядок X]: ❌ "[Quoted text]" — [Diagnosis: e.g. Хибний наголос / Штучна інверсія] (Штраф: -Y балів)
- *(Або "Дефектів не виявлено — текст чистий")*

### 4. Просодична карта та сканування (Scansion & Phonics Map)
- Рядок 1: [Склади: X] | [Метрична схема: U — U — ...] | [Клаузула: Ж]
- Рядок 2: [Склади: Y] | [Метрична схема: U — U — ...] | [Клаузула: Ч]
- Схема римування: [e.g. ABAB (перехресне), пари: дієслово+іменник, опорні приголосні: ...]
- Евфонія: [Аналіз чергування у/в, і/й, відсутність зяяння]

### 5. Покроковий план виправлення (Prioritized Remediation Blueprint)
1. **[Пріоритет 1 - Мова/Наголоси]**: Рядок X: ❌ "[Original]" ➔ ✅ "[Remediated Line]"
   - *Пояснення*: [Чому запропонований варіант усуває дефект і зберігає метр]
   - *Відповідальний сабагент*: `poetry-prosody-phonics`
2. **[Пріоритет 2 - Синтаксис/Інверсії]**: Рядок Y: ❌ "[Original]" ➔ ✅ "[Remediated Line]"
   - *Пояснення*: [Відновлення природного порядку слів]
   - *Відповідальний сабагент*: `poetry-conciseness-editor`
3. **[Пріоритет 3 - Образність/Антикліше]**: Рядок Z: ❌ "[Original]" ➔ ✅ "[Remediated Line]"
   - *Пояснення*: [Заміна абстрактної декларації на тактильну деталь]
   - *Відповідальний сабагент*: `poetry-imagery-architect`
```

---

## 6. Edge-Case Handling

1. **Верлібр (Free Verse)**:
   - Не штрафувати за різну довжину рядків (`D01`), якщо дотримано синтагматичного дихання та змістової ваги анжамбеманів.
   - Розділ «Рима» оцінювати за внутрішньою фонікою, алітераціями, асонансами та звукописною атмосферою.
2. **Автентична коломийка та фольклорні метри**:
   - Строго контролювати складову формулу `(4+4)+6` з обов'язковою цезурою після 8-го складу.
   - Відрізняти автентичну народну мову від сувенірного лубка (`шароварщини`).
3. **Історичні та барокові тексти**:
   - Відрізняти навмисну барокову стилізацію (Сковорода, козацьке бароко: *«всякому городу нрав і права»*) від випадкових сучасних суржикізмів чи синтаксичних русизмів.
4. **Тексти для музичної генерації (Lyrics Handshake)**:
   - Якщо вірш призначено для Suno/Udio, ігнорувати структурні службові теги в дужках `[Verse]`, `[Chorus]` при підрахунку складів, проте суворо перевіряти наголоси слів у круглих дужках бек-вокалу `(луна)`.
```

---

### Design 4.2: Updates for `openai.yaml`
**Target Paths**:
- `d:\poetry-skill\skills\ukrainian-poetry\agents\openai.yaml`
- `d:\poetry-skill\.agents\skills\ukrainian-poetry\agents\openai.yaml`

Add the `poetry-qa-bot` registration block under `agents:`:

```yaml
  poetry-qa-bot:
    display_name: "Poetry QA Bot (Аудитор якості)"
    short_description: "Autonomous quality audit against 6 core principles, 100-point rubric scoring, and remediation blueprint"
    default_prompt: "Use $poetry-qa-bot to audit this Ukrainian poem against the 6 core principles, apply the 100-point deduction rubric, and output a detailed scorecard with step-by-step fixes."
```

Full updated `openai.yaml` content:

```yaml
interface:
  display_name: "Ukrainian Poetry"
  short_description: "Write, analyze, and refine authentic Ukrainian poetry with 6 core principles"
  default_prompt: "Use $ukrainian-poetry to write a natural Ukrainian poem from this topic."

agents:
  poetry-imagery-architect:
    display_name: "Poetry Imagery Architect (Образотворець)"
    short_description: "Tactile imagery, sensory grounding, fresh metaphors, and anti-cliché audit"
    default_prompt: "Use $poetry-imagery-architect to inject sensory tactility, eliminate abstract cliches, and ground this Ukrainian poetic draft in physical detail."

  poetry-emotional-critic:
    display_name: "Poetry Emotional Critic (Критик щирості)"
    short_description: "Emotional sincerity audit, zero false pathos, anti-moralizing, and psychological depth"
    default_prompt: "Use $poetry-emotional-critic to audit emotional sincerity, strip false melodrama and preachy didactics from this Ukrainian poetic draft."

  poetry-prosody-phonics:
    display_name: "Poetry Prosody & Phonics (Майстер фоніки та просодії)"
    short_description: "Metric scansion, Ukrainian stress norms, euphony (у/в, і/й), and heterogeneous rhyming"
    default_prompt: "Use $poetry-prosody-phonics to scan meter, verify orthoepic stresses, enforce euphony laws, and check heterogeneous rhymes in this Ukrainian poetic draft."

  poetry-conciseness-editor:
    display_name: "Poetry Conciseness Editor (Редактор лаконічності)"
    short_description: "Semantic compression, filler word purge, and elimination of artificial inversions"
    default_prompt: "Use $poetry-conciseness-editor to remove filler pronouns, eliminate artificial syntactic inversions, and restore natural Ukrainian word order."

  poetry-form-synthesizer:
    display_name: "Poetry Form Synthesizer (Архітектор форми та ракурсу)"
    short_description: "Form-content harmony, defamiliarized perspective, resonant endings, pipeline arbitration, and 100-point rubric scoring"
    default_prompt: "Use $poetry-form-synthesizer to harmonize form and content, craft a resonant non-moralizing ending, reconcile subagent edits, and score against the 100-point rubric."

  poetry-qa-bot:
    display_name: "Poetry QA Bot (Аудитор якості)"
    short_description: "Autonomous quality audit against 6 core principles, 100-point rubric scoring, and remediation blueprint"
    default_prompt: "Use $poetry-qa-bot to audit this Ukrainian poem against the 6 core principles, apply the 100-point deduction rubric, and output a detailed scorecard with step-by-step fixes."
```

---

### Design 4.3: Specification for `## End-to-End Song Creation Pipeline` in `skills/poetry-skill/SKILL.md`
**Target Paths**:
- `d:\poetry-skill\skills\poetry-skill\SKILL.md`
- `d:\poetry-skill\.agents\skills\poetry-skill\SKILL.md`

Insert this comprehensive section directly between Section 2 (`## 2. Core Directives Summary`) and Section 3 (`## 3. Quick Reference`), and renumber Quick Reference to `## 4. Quick Reference`. Also update the routing table in Section 1.

```markdown
## 3. End-to-End Song Creation Pipeline

The **End-to-End Song Creation Pipeline** is the unified master protocol connecting Ukrainian literary poetic creation with production-grade AI music generation across **Suno AI (v4.5/v5.5)**, **Udio AI (v4)**, and **Google Flow Music (Lyria 3.5)**, followed by engineering DAW stem post-production and True Peak streaming distribution.

### 3.1 Unified Architecture Flowchart

```text
               ┌─────────────────────────────────────────────────────────┐
               │              USER CREATIVE BRIEF / THEME                │
               └───────────────────────────┬─────────────────────────────┘
                                           │
                                           ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ STAGE 1: Ukrainian Poetry Generation (skills/ukrainian-poetry)                         │
│ • Subagents Pipeline: Imagery Architect ➔ Emotional Critic ➔ Prosody & Phonics ➔       │
│   Conciseness Editor ➔ Form Synthesizer                                                │
│ • Output: Authentic Ukrainian Poem grounded in 6 Core Poetic Principles                │
└──────────────────────────────────────────┬─────────────────────────────────────────────┘
                                           │ raw_poem
                                           ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ STAGE 2: Autonomous Poetic Quality Audit (poetry-qa-bot)                               │
│ • Forensic scan against 6 Principles + 14-Category Penalty Deduction Matrix            │
│ • Mandatory Quality Gate: Score must be ≥ 90/100 (Master-level) or ≥ 85/100            │
│ • [Loop if < 85/90]: Itemized remediation blueprint routed to specialist subagents     │
└──────────────────────────────────────────┬─────────────────────────────────────────────┘
                                           │ verified_poem (Score ≥ 90)
                                           ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ STAGE 3: Lyrics Adaptation & Spoken Prosody Test (music-lyrics-architect)             │
│ • Structural arrangement: [Intro], [Verse 1], [Pre-Chorus], [Chorus], [Outro]          │
│ • Backing vocals / Delivery gestures strictly in (Round Parentheses)                   │
│ • Syllable symmetry enforcement (8-8-8-8, 10-8-10-8) to prevent vocal rushing          │
│ • Spoken Prosody Test + AI Stress Capitalization (вИпадок, дорОга, моЯ)                 │
│ • Spatial Contrast: Verse Staccato (crisp) vs Chorus Legato (open soaring vowels)      │
│ • 5-Second Rule ([Vocal Intro]) & 50-Second Chorus Rule                                │
└──────────────────────────────────────────┬─────────────────────────────────────────────┘
                                           │ optimized_lyrics + acoustic_dna
                                           ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ STAGE 4: Platform Selection & Prompt Synthesis (music-prompt-synthesizer)              │
│ • Western Genre Anchor (Post-Punk, Darkwave, Trip-Hop, Minimal Alt-Pop, Shoegaze, etc.)│
│ • Multi-Platform Synthesized Prompts:                                                  │
│   - Suno v4.5/v5.5: Method 1 (First 5 Words) & Method 2 (HookGenius 5-Module Matrix)   │
│   - Udio v4: ≤ 250 chars prompt, 48 kHz stereo, inpainting *stars* syntax, Context Len │
│   - Google Flow Music: Conversational Agent mode, Spaces, Section Replace, AI Cover    │
│ • Anti-Local-Pop Exclude Vector & Complete De-identification (zero artist leaks)       │
└──────────────────────────────────────────┬─────────────────────────────────────────────┘
                                           │ audio_prompts + lyrics_box + extensions_roadmap
                                           ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ STAGE 5: The 10 AI Quality Gates Verification                                          │
│ • Gates 1–6 (Pre-Gen / Arrangement): Anti-Skip 5s, 50s Chorus, Spoken Prosody,        │
│   Spatial Contrast, Vance Powell Verse 2 Expansion, Breakdown (15-20s) & Mega-Chorus   │
│ • Gates 7–10 (DAW / Mastering / Ads): Low-End Split Bass, Tchad Blake Distortion to     │
│   Master Fader, True Peak -1 dBTP / -14 LUFS, Single-Only Ad Traffic                   │
└──────────────────────────────────────────┬─────────────────────────────────────────────┘
                                           │ audio_generation + stem_exports
                                           ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ STAGE 6: Professional DAW Stem Engineering & Mastering (music-daw-mastering-critic)    │
│ • Step 5 Stem Mixing: Separation (Moises/RipX/LALAL), Kick/Bass phase alignment,       │
│   surgical frequency unmasking (Trackspacer), Split Bass Compression (<200Hz brickwall │
│   vs >200Hz saturated), Tchad Blake distortion to Master Fader, Mid-Side vocal ducking │
│ • Step 6 Mastering: -1 dBTP with TP Limiting OFF for loud masters (-6..-8 LUFS);       │
│   Genre Skip Rate monitoring (Pop >48%, Electronic >37%, Rock >31%, universal >45%);   │
│   Single-only ad spend (no Playlist Placement Trap), Spotify Canvas / Discovery Mode   │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

### 3.2 Detailed Protocol Across the 6 Stages

#### Stage 1: Thematic Inception to Authentic Ukrainian Verse
- **Tool / Subagent**: `skills/ukrainian-poetry/SKILL.md` (and 5 specialized personas: `poetry-imagery-architect`, `poetry-emotional-critic`, `poetry-prosody-phonics`, `poetry-conciseness-editor`, `poetry-form-synthesizer`).
- **Standard**: Strictly enforce the **6 Core Poetic Principles**:
  1. *Fresh Imagery*: Concrete tactile details across 5 sensory channels; zero dead metaphors (*«кров-любов»*, *«серце палає»*).
  2. *Emotional Sincerity*: Restrained psychological truth; zero theatrical pathos or didactic sermonizing.
  3. *Prosodic Harmony*: Syllabo-tonic, dolnik, or kolomyika cadence; normative literary stresses (*вИпадок*); rich heterogeneous rhymes; balanced euphony (`у/в`, `і/й`, `з/із/зі`).
  4. *Conciseness & Word Weight*: High semantic density; zero filler pronouns (*цей, той, свій*) or padding particles; **zero artificial syntactic inversions for rhyme**.
  5. *Original Perspective*: Novel authorial angle; micro-detail focus; lingering, open, or paradoxical endings.
  6. *Form-Content Unity*: Rhythm and stanza structure organically body forth the psychological state.

#### Stage 2: Autonomous Quality Audit (Poetry QA Bot)
- **Tool / Subagent**: `skills/ukrainian-poetry/agents/poetry-qa-bot.md`.
- **Function**: Autonomous pre-flight audit before any musical resources are expended.
- **Verification Standard**:
  - Scans poem text against the 7 dimensions from `references/rubric.md` (Ceiling: 100 points).
  - Evaluates against the 14-defect penalty deduction matrix:
    - *Metric breakdown (`D01`)*: -5 to -15 pts
    - *Russianized stress (`D02`)*: -5 to -10 pts per case
    - *Homograph confusion (`D03`)*: -5 pts
    - *Verb-verb rhymes (`D04`)*: -3 to -8 pts
    - *Diminutive rhymes (`D05`)*: -4 pts
    - *Blacklist cliché rhymes (`D06`)*: -5 pts
    - *Artificial inversions (`D07`)*: -3 to -6 pts
    - *Filler padding (`D08`)*: -2 to -5 pts
    - *Abstract emotion telling (`D09`)*: -3 to -6 pts
    - *Theatrical pathos (`D10`)*: -5 to -10 pts
    - *Didactic moralizing ending (`D11`)*: -5 pts
    - *Sharovarshchyna / kitsch (`D12`)*: -10 pts
    - *Syntactic calques (`D13`)*: -5 to -15 pts
    - *Monotonic clausulae (`D14`)*: -3 to -5 pts
  - **Passing Gate**: Poem must score **$\ge 90/100$ (Master-level)** or at least **$\ge 85/100$**. If score is below threshold, execute the **Remediation Blueprint** before proceeding to Stage 3.

#### Stage 3: Song Lyrics Adaptation & Prosodic Alignment
- **Tool / Subagent**: `skills/ukrainian-poetry-to-suno/agents/music-lyrics-architect.md`.
- **Arrangement Conventions**:
  - `[Square Brackets]`: Silent structural and arrangement cues for audio models (`[Intro]`, `[Vocal Intro]`, `[Verse 1]`, `[Pre-Chorus]`, `[Chorus]`, `[Verse 2 - add driving tambourine, shaker]`, `[Breakdown]`, `[Mega-Chorus]`, `[Outro]`).
  - `(Round Parentheses)`: Sung vocal delivery cues, backing vocals, and ad-libs `(whispered)`, `(belted)`, `(falsetto)`, `(screamed)`, `(ad-lib)`, `(building intensity)`, `(key change)`, `(half-time feel)`, `(harmonized)`, `(луна)`. **Never place instrumental cues in parentheses.**
- **Syllable Symmetry**: Standardize foot counts (e.g. 8-8-8-8 or 10-8-10-8) to eliminate AI vocal rushing or rhythmic stumbling.
- **Spoken Prosody Test**: Read aloud at speaking cadence; if words stumble, rebalance syllable count.
- **Ukrainian Stress Capitalization**: Mark stressed vowels in non-obvious words and homographs (`вИпадок`, `чорнОзем`, `прИйде`, `заспівАй`, `моЯ`, `землЯ`, `зЕмлю`, `дорОга` vs `дорогА`, `зАмок` vs `замОк`).
- **Spatial Contrast**: Staccato verses (consonant-rich, punchy rhythm) vs Legato chorus (open, soaring vowels `Ooooh, Aaah`).
- **Timing Directives**: First 5 seconds must feature vocal presence or hook (`[Vocal Intro]`); first Chorus must land $\le 50$ seconds. Cognitive melody limit: $\le 3\text{--}4$ melodic themes per track.

#### Stage 4: Platform Selection & Multi-Platform Prompt Synthesis
- **Tool / Subagent**: `skills/ukrainian-poetry-to-suno/agents/music-prompt-synthesizer.md`.
- **Western Genre Anchor**: All prompt design must target contemporary/classic Western genres (Post-Punk, Darkwave, Synthwave, Trip-Hop, Minimalist Alt-Pop, Shoegaze, Progressive Metalcore, Melodic Techno, Ambient).
- **Platform Synthesizers**:
  1. **Suno AI (v4.5 / v5.5)**:
     - *Method 1 (Conversational Paragraph)*: Apply «First 5 Words» rule ($80\%$ model attention on opening descriptors).
     - *Method 2 (HookGenius Tag Matrix)*: 5 modules (Genre, Mood, Vocal Triple-Stack, Instruments, Production/BPM). Style box: 80–180 characters.
     - *Anti-Pattern Fixes*: Lyrics Rushing $\to$ `(half-time feel)` + 4–8 words/line; Sterile Vocals $\to$ Vocal Triple-Stack (**Character** + **Delivery** + **FX**); Negation Trap $\to$ Positive hyper-specificity.
  2. **Udio AI (v4)**:
     - 48 kHz stereo, up to 10 min continuous track, concise prompt $\le 250$ chars.
     - Context Length management (10–15s for abrupt transitions vs max for continuity).
     - Inpainting syntax `*stars*` for surgical line/word replacement.
  3. **Google Flow Music (Lyria 3.5)**:
     - Conversational Agent mode (`[Concept & Style] + [Artist/Vibe Ref] + [Instruments] + [Dynamics/Vocals]`).
     - Spaces, Turntable, Section-level Replace editing, AI Cover, Gemini Omni Flash synced video clips.
- **Exclude Vector**: Enforce universal anti-local-pop tokens (`cheesy regional pop, post-soviet schlager, wedding synth brass, cheap accordion, generic euro-pop, metallic highs, muddy bass`).
- **De-identification**: Zero artist names or copyrighted strings.

#### Stage 5: 10 AI Quality Gates Verification
Every song asset must pass the **10 AI Quality Gates Matrix** before publication:
- **Gate 1 (Anti-Skip First 5s)**: Live human voice or hook present $\le 5$s.
- **Gate 2 (50s Chorus Rule)**: Full chorus arrives $\le 50$s.
- **Gate 3 (Spoken Prosody & Stress)**: Spoken Prosody test passes; capital accents (`вИпадок`, `дорОга`).
- **Gate 4 (Spatial Contrast)**: Verse Staccato vs Chorus Legato.
- **Gate 5 (Verse 2 Development)**: Vance Powell arrangement expansion (tambourine, shaker, backing vocals).
- **Gate 6 (Breakdown & Climax)**: 15–20s energy drop (`[Breakdown]`) followed by `[Mega-Chorus]`.
- **Gate 7 (Low-End Split Bass)**: Sub $<200\text{ Hz}$ brickwall mono vs Mid-High $>200\text{ Hz}$ dynamic saturated; Kick dynamic sidechain unmasking.
- **Gate 8 (Tchad Blake Drum Distortion)**: Parallel crushed drum aux routed **directly to Master Fader** (bypassing Drum Bus).
- **Gate 9 (Mastering True Peak)**: Loud masters ($-6\dots-8\text{ LUFS}$) set to $-1\text{ dBTP}$ with True Peak limiting OFF (or $-14\text{ LUFS}$ if $-2\text{ dBTP}$ is strictly mandatory).
- **Gate 10 (Single-Only Ad Traffic)**: Ad spend directed strictly to target single (Abolishing Playlist Placement Trap).

#### Stage 6: Professional DAW Stem Engineering & Mastering
- **Tool / Subagent**: `skills/ukrainian-poetry-to-suno/agents/music-daw-mastering-critic.md`.
- **Step 5 DAW Stem Engineering**:
  - Stem extraction via Moises Pro, RipX DAW, or LALAL.AI.
  - Mono Kick & Bass phase alignment / polarity inversion check.
  - Surgical frequency unmasking via dynamic sidechain EQ (Trackspacer / Neutron Unmask) ducking bass 2–3 dB during kick hits.
  - Split Bass Compression: Sub-bass $<200\text{ Hz}$ brickwall limited; Mid-High $>200\text{ Hz}$ dynamic saturated.
  - Tchad Blake Parallel Drum Distortion: Routed directly to Master Fader to preserve Drum Bus headroom.
  - Dynamic Mid-Side Vocal Reverb Sidechain: Reverb ducked 3–6 dB during active vocal presence in Mid channel only.
- **Step 6 Mastering & Streaming Viability**:
  - True Peak headroom protection ($-1\text{ dBTP}$).
  - Skip Rate monitoring against Spotify 2026 thresholds (Pop $>48\%$, Hip-hop $>44\%$, Electronic $>37\%$, Indie rock $>31\%$, universal alarm $>45\%$).
  - Target Completion Rate $>55\text{--}60\%$, Save Rate $\ge 20\%$.
  - Single-only smart links, Spotify Canvas (8s visual loops), Marquee, Discovery Mode.

---

### 3.3 End-to-End Pipeline Data Contract

```yaml
# Unified Data Flow across the 6 Stages
pipeline_execution:
  stage_1_poetry:
    input:
      brief: string                      # Creative prompt, theme, emotional atmosphere
      register: enum                    # contemporary-urban | chamber-intimate | neoclassical | folk | etc.
      form: string                      # iamb | dolnik | kolomyika | verlibre | etc.
    output:
      raw_poem: string                  # Publication-grade poem adhering to 6 Principles

  stage_2_audit:
    input:
      poem_text: stage_1.raw_poem
      passing_threshold: 90
    output:
      total_score: float                # Target: ≥ 90/100
      is_passing: boolean
      deductions: list[string]          # Detailed defect list
      remediation_plan: list[string]    # If not passing, step-by-step fix recipes

  stage_3_lyrics:
    input:
      raw_poetry: stage_2.verified_poem
      structure_template: "Verse-Chorus-Verse-Chorus-Bridge-MegaChorus-Outro"
    output:
      optimized_lyrics: string          # Syllable-symmetric lines with [Metatags] and (Gestures)
      stress_capitalized: boolean       # Stressed vowels marked (вИпадок, дорОга)
      spoken_prosody_passed: boolean

  stage_4_prompts:
    input:
      lyrics: stage_3.optimized_lyrics
      western_genre: string             # e.g., 'ukrainian darkwave post-punk'
      target_platforms: ["suno", "udio", "flow_music"]
    output:
      suno_prompt:
        style_box: string               # Method 1 or Method 2 (80-180 chars)
        lyrics_box: string              # Full lyrics with metatags and vocal gestures
        exclude_prompt: string          # Anti-local-pop and anti-artifact tokens
      udio_prompt:
        prompt_text: string             # ≤ 250 chars dense tags
        inpainting_syntax: string       # *stars* markup
      flow_music_prompt:
        agent_command: string           # Natural language prompt for Lyria 3.5

  stage_5_quality_gates:
    input:
      prompts: stage_4.prompts
      lyrics: stage_3.optimized_lyrics
    output:
      gates_1_to_6_status: boolean      # Structural and prosodic pre-flight verification
      gates_7_to_10_status: boolean     # Mixing and mastering pre-flight verification

  stage_6_daw_mastering:
    input:
      generated_audio_stems: list[string]
      target_loudness_lufs: float       # -6 to -8 LUFS (or -14 LUFS if mandatory)
    output:
      stem_mixing_checklist: object     # Low-end split, unmasking, Tchad Blake aux
      mastering_spec: object            # -1 dBTP ceiling, True Peak limiter OFF
      streaming_retention_plan: object  # Canvas, single-only campaigns, skip rate targets
```
```

#### Updated Section 1 Routing Table in `skills/poetry-skill/SKILL.md`
Update row 3 in the table of Section 1 to point to the new section:

```markdown
| Task Type | Trigger / Intent | Sub-Skill to Load |
|---|---|---|
| **Poetry & Versification** | Writing poems, sonnets, dolnik, taktovik, kolomyika, editing rhymes, stress scansion, Ukrainian lyrical texts | `skills/ukrainian-poetry/SKILL.md` |
| **Multi-Platform AI Music Prompts** | Converting poems/briefs to Suno Custom Mode, Udio v4, Flow Music Lyria 3.5, style prompts, Western genre arrangements, metatags | `skills/ukrainian-poetry-to-suno/SKILL.md` |
| **End-to-End Songwriting & Production** | Generating Ukrainian lyrics + creating matching multi-platform prompts + DAW stem engineering roadmap | Execute Section 3: **End-to-End Song Creation Pipeline** |
```

---

## 5. Verification Method

To independently verify the designs and ensure zero regressions across the codebase:

1. **Automated Subagent Schema Test**:
   Run the Challenger 2 test suite:
   ```bash
   py -3 -m unittest tests.test_adversarial_challenger2.TestChallenger2Robustness.test_20_subagent_files_and_yaml_frontmatter_schema
   ```
   *Expected result*: After adding `poetry-qa-bot.md` to `skills/ukrainian-poetry/agents/` and updating `expected_agents` in `test_adversarial_challenger2.py`, all frontmatter assertions, mandatory section checks, and yaml/markdown block assertions PASS with code 0.

2. **Full Repository Test Suite**:
   Run the complete test suite:
   ```bash
   py -3 tests/run_tests.py --all
   ```
   *Expected result*: All 75 test cases execute and PASS with code 0, maintaining an average poetry score $\ge 95/100$ and zero regressions.

3. **File Mirror & Ecosystem Synchronization Verification**:
   Verify that both `skills/` and `.agents/skills/` reflect identical agent specifications and skill definitions.

4. **Invalidation Conditions**:
   - Any omission of the 6 mandatory sections in `poetry-qa-bot.md`.
   - Any failure of `openai.yaml` to register `poetry-qa-bot`.
   - Broken markdown parsing or missing ````yaml` / ````markdown` contract blocks.
   - Any regression causing `py -3 tests/run_tests.py --all` to fail or exit with a non-zero status.

---
*End of Handoff Report — Ready for Orchestrator Review and Implementation Delegation.*

# Survey & Architectural Design for Requirement R2: 5 Specialized Subagents and Pipeline

**Explorer**: `survey_explorer_2`  
**Date**: 2026-08-28  
**Scope**: Requirement R2 (5 Subagent Personas & Pipeline Orchestration) in `poetry-skill`  
**Target Directory**: `d:\poetry-skill`  

---

## 1. Executive Summary & Problem Scope

The objective of Requirement R2 is to design, specify, and integrate **5 specialized subagent personas** and an **orchestrated poetic pipeline** into the `poetry-skill` ecosystem. 

Currently, Ukrainian poetry generation is handled as a single monolithic process inside `skills/ukrainian-poetry/SKILL.md`. While the skill guidelines are comprehensive, complex poetic creation requires discrete cognitive specializations to guarantee that none of the 6 fundamental poetic principles (fresh imagery, emotional sincerity, rhythmic/phonic harmony, word conciseness, non-trivial perspective, and organic form-content unity) are compromised during composition.

This survey establishes:
1. The **directory layout and specification standard** for agent personas within `skills/ukrainian-poetry/agents/`.
2. Detailed **architectural profiles for the 5 specialized subagents** (Ukrainian naming, mission, heuristic guardrails, input/output contracts, and edge-case handling).
3. The **multi-agent pipeline orchestration engine** supporting 5-stage sequential execution, single-specialist dispatch, iterative synthesizer loops, and downstream integration with `ukrainian-poetry-to-suno`.
4. The **system registration strategy** across `SKILL.md`, `AGENTS.md`, `openai.yaml`, and system command interfaces.

---

## 2. Directory Layout & Codebase Structure

### 2.1 Current Directory State
Inspection of the existing workspace reveals:
- `skills/ukrainian-poetry/`: Contains `SKILL.md`, `references/` (full-guide, rubric, input-templates, tests, stress-tests), and `agents/`.
- `skills/ukrainian-poetry/agents/`: Currently contains only `openai.yaml` (5 lines describing a generic single prompt).
- `skills/poetry-skill/SKILL.md`: Master skill router bridging poetry versification and Suno music prompt engineering.
- `AGENTS.md`: Canonical Single Source of Truth (SSOT) defining global agent directives, anti-calques, and test suites.

### 2.2 Target Architecture for `skills/ukrainian-poetry/agents/`
To maintain modularity and seamless agent execution across Antigravity, Claude Code, and Codex frameworks, subagents must be implemented as dedicated markdown specification files with standardized YAML frontmatter and unified contract sections:

```text
skills/
├── ukrainian-poetry/
│   ├── SKILL.md                                 <-- Updated with Subagent Pipeline routing
│   ├── agents/
│   │   ├── openai.yaml                          <-- Multi-agent interface registry
│   │   ├── poetry-imagery-architect.md          <-- Образотворець
│   │   ├── poetry-emotional-critic.md           <-- Критик щирості
│   │   ├── poetry-prosody-phonics.md            <-- Майстер фоніки та просодії
│   │   ├── poetry-conciseness-editor.md         <-- Редактор лаконічності
│   │   └── poetry-form-synthesizer.md           <-- Архітектор форми та ракурсу
│   └── references/
│       ├── full-guide.md                        <-- 6 principles & agent roles
│       ├── rubric.md                            <-- 100-point scoring rubric
│       └── input-templates.md                   <-- Pipeline invocation templates
├── poetry-skill/
│   └── SKILL.md                                 <-- Unified entry point & router
└── ukrainian-poetry-to-suno/
    └── ...                                      <-- Suno music prompt engine
```

---

## 3. The 5 Specialized Subagents: Detailed Specifications

Each subagent embodies a distinct poetic discipline with clear boundaries, avoiding role overlap while covering the entire poetic creation lifecycle.

```
┌────────────────────────────────────────────────────────────────────────┐
│                   5 SPECIALIZED SUBAGENT PERSONAS                      │
├──────────────────────────┬─────────────────────────────────────────────┤
│ poetry-imagery-architect │ Образотворець / Сенсорний архітектор        │
│ poetry-emotional-critic  │ Критик щирості / Аудитор емоційної глибини  │
│ poetry-prosody-phonics   │ Майстер фоніки та просодії                  │
│ poetry-conciseness-editor│ Редактор лаконічності та природного порядку │
│ poetry-form-synthesizer  │ Архітектор форми, ракурсу та головний збирач│
└──────────────────────────┴─────────────────────────────────────────────┘
```

---

### 3.1 Subagent 1: `poetry-imagery-architect` (**Образотворець**)

- **Ukrainian Identity**: Образотворець / Майстер сенсорної деталі та свіжої метафори
- **Primary Mission**: Ensures high sensory tactility (sight, sound, smell, texture, taste, kinesthetics, temperature), discovers and eradicates dead poetic clichés and abstract noise, enforcing the "Show, Don't Tell" principle.
- **Principles Owned**:
  - **Principle 1**: Свіжа образність та метафоричність (Fresh Imagery & Metaphors).
  - **Principle 5**: Оригінальність ракурсу на рівні мікродеталей (Micro-detail focus).
- **Core Heuristics & Guardrails**:
  1. *Show, Don't Tell*: Transform declarative statements of emotion (*«мені було сумно й самотньо»*) into tactile physical actions (*«пальці примерзають до іржавого ключа у замку»*).
  2. *Anti-Cliché Scanner*: Eject hackneyed tropes (*«кров-любов», «троянди-сльози», «крила надії», «вогонь душі», «тягар розлуки», «золоті ниви»*).
  3. *Sensory Palette Balance*: Ensure at least 2 distinct sensory channels per stanza (e.g. tactile cold + visual shadow, or olfactory smoke + acoustic resonance).
  4. *De-Abstraction*: Ground abstract nouns (*душа, серце, доля, вічність, біль*) into concrete physical correlatives.
- **Input Contract**:
  - `draft_text` (string): Current verse or poem draft.
  - `register` (string): Style register (`contemporary-urban`, `chamber-intimate`, `philosophical-neoclassical`, `baroque-cossack`, `folk-authentic`, `children-playful`).
  - `image_density` (enum): `sparse | balanced | rich`.
- **Output Contract**:
  - `cliche_findings`: List of identified clichés with line numbers.
  - `sensory_density_score`: 0–10 rating based on concrete vs abstract tokens.
  - `imagery_enhancements`: Line-by-line replacement proposals with rationale.
  - `revised_draft`: Rewritten text with tactile imagery preserving meter.
- **Edge Cases**:
  - *Sparse/Minimalist Poetry*: Do not overload with hyper-metaphoric clutter when a transparent, haiku-like minimalism is requested.
  - *Philosophical/Abstract Themes*: Ground high philosophy in sculptural physical emblems (e.g. Skovorodian/Zerovian stone, water, brass, chisel).

---

### 3.2 Subagent 2: `poetry-emotional-critic` (**Критик щирості**)

- **Ukrainian Identity**: Критик щирості / Аудитор емоційної глибини та автентичності
- **Primary Mission**: Eliminates artificial melodrama, hollow pathos, theatrical declamation, sentimental kitsch, and moralizing didactics, ensuring authentic emotional resonance through psychological truth and understatement (*тиха лірика*).
- **Principles Owned**:
  - **Principle 2**: Емоційна глибина та щирість (Emotional Depth & Sincerity).
  - **Anti-Sharovarshchyna & Anti-Kitsch**: Freedom from postcard patriotism and sentimental posturing.
- **Core Heuristics & Guardrails**:
  1. *Zero False Pathos*: Detect and strip exclamation point storms (`!!!`), melodramatic sighing (*«О, горе мені!», «Чому ж, о чому?..»*), and pompous operatic chest-beating.
  2. *Anti-Didactic Filter*: Strictly forbid moralizing summary endings (*«І я збагнув мораль», «Тож любіть життя», «Пам'ятайте завжди»*).
  3. *Power of Understatement (Мистецтво недомовленості)*: Replace direct emotional shouting with subtle behavioral gestures, quiet domestic pauses, and unresolved psychological tension.
  4. *Anti-Sharovarshchyna Audit*: Purge tourist-souvenir folk tokens used as decorative wallpaper (*гопак, сало, шаровари, сувенірна калина*).
- **Input Contract**:
  - `draft_text` (string): Poetic draft.
  - `mode` (string): `lyrical | reflective | patriotic | dramatic | chamber-intimate | etc.`
  - `target_tone` (string): Requested psychological temperature (`whispered`, `stoic`, `elegiac`, `ironic`, `grave`).
- **Output Contract**:
  - `pathos_audit`: Detailed list of detected melodramatic markers, didacticism, or theatrical posture.
  - `sincerity_score`: 0–10 score of emotional authenticity.
  - `critique_summary`: Diagnostic explanation of why specific passages ring hollow.
  - `restrained_revision`: Curated draft with genuine emotional depth and grounded dignity.
- **Edge Cases**:
  - *Patriotic/Civil Poetry*: Balance solemn gravity and tragic grief without crossing into bombastic rally slogans or sentimental melodrama.
  - *Humorous/Children's Poetry*: Preserve playfulness without descending into moralistic preaching.

---

### 3.3 Subagent 3: `poetry-prosody-phonics` (**Майстер фоніки та просодії**)

- **Ukrainian Identity**: Майстер фоніки та просодії / Просодичний інженер
- **Primary Mission**: Enforces mathematical metric stability across all versification systems (syllabo-tonic, dolnik, taktovik, kolomyika, blank verse, verlibre), orthoepic stress accuracy (zero Russianisms), Ukrainian euphonic harmony (`у/в`, `і/й`, `з/із/зі`), clausula alternation (`ЖЧЖЧ`), and rich heterogeneous rhyming.
- **Principles Owned**:
  - **Principle 3**: Ритмічна та звукова гармонія (Rhythmic & Sound Harmony: Meter, Breath, Rhyme, Phonics).
- **Core Heuristics & Guardrails**:
  1. *Metric Scansion & Foot Verification*:
     - Syllabo-tonic (Iamb, Trochee, Dactyl, Amphibrach, Anapest): Verify foot counts and natural pyrrhic substitutions (`U U`).
     - Dolnik: Fixed ictuses (stresses) with unstressed intervals strictly between 1 and 2 syllables.
     - Kolomyika: Exact 14-syllable line `(4 + 4) + 6` with mandatory caesura after 8th syllable.
  2. *Orthoepic Accentuation & Stress Disambiguation*:
     - Strictly enforce literary Ukrainian stresses (*вИпадок, чорнОзем, одИннадцять, чотирнАдцять, листопАд, рукОпис, ненАвисть, новИй, читАння*).
     - Disambiguate homographs (*зАмок* vs *замОк*, *нАголос* vs *наголОс*).
  3. *Laws of Ukrainian Euphony (Милозвучність)*:
     - `у/в` alternation (use `у` between consonants, `в` after vowels before consonants).
     - `і/й` alternation (syllabic vowel `і` vs glide `й`).
     - Preposition alternations (`з / із / зі / зо`). Eject hiatus and awkward consonant clusters.
  4. *Heterogeneous Rhyme Requirement*:
     - Mandate cross-grammatical rhymes (verb+noun, noun+adverb, adj+pronoun).
     - Strict blacklist: No verb-verb (*знати-кохати*), no noun-noun identical cases (*картина-стежина*), no diminutive suffixes (*-очка/-енька*).
  5. *Sound Architecture (Звукопис)*:
     - Cultivate rich pre-tonic supporting consonants (*т-р-ава — т-р-ива, д-з-він — на-з-догін*), purposeful alliteration and vocalic assonance.
- **Input Contract**:
  - `draft_text` (string): Draft to scan.
  - `form` (string): `free | sonnet | blank-verse | dolnik | kolomyika | regular`
  - `meter` (string): `iamb | trochee | dactyl | amphibrach | anapest | dolnik | kolomyika | free`
  - `rhyme_scheme` (string): `ABAB | AABB | ABBA | chain | heterogeneous-approximate | unrhymed`
  - `clausula_pattern` (string): `ЖЧЖЧ | ЧЖЧЖ | free | etc.`
- **Output Contract**:
  - `scansion_diagram`: Line-by-line syllable count, foot notation, stress scansion, and clausula tags (`Ж / Ч / Д`).
  - `prosodic_violations`: Detailed errors (broken feet, bad stresses, euphony glitches, banal rhymes).
  - `phonetic_harmony_score`: 0–10 rating.
  - `scanned_and_corrected_draft`: Metric and euphonic clean version.
- **Edge Cases**:
  - *Free Verse (Верлібр)*: Evaluates syntagmatic breath units, enjambment tension, and acoustic assonance rather than fixed feet.
  - *Blank Verse (Білий вірш)*: Enforces strict unrhymed 5-foot or 6-foot iamb without accidental rhymes.

---

### 3.4 Subagent 4: `poetry-conciseness-editor` (**Редактор лаконічності**)

- **Ukrainian Identity**: Редактор лаконічності та ваги слова
- **Primary Mission**: Eliminates padding, redundant filler words (stop-words, vacuous pronouns, particle clutter), corrects unnatural syntactic inversions forced by rhyme, and restores native Ukrainian word order, maximizing semantic compression and energy-per-word ratio.
- **Principles Owned**:
  - **Principle 4**: Лаконічність і вага слова (Conciseness & Semantic Density).
  - **Natural Ukrainian Syntax**: Zero forced inversions for rhyme.
- **Core Heuristics & Guardrails**:
  1. *Stop-Word & Filler Purge*: Strip parasitic fillers inserted solely to pad syllable counts (*«якийсь там», «ось», «вже», «ж», «собі», «дуже», «мій/твоя»* when obvious from context).
  2. *Anti-Forced Inversion*: Eliminate unnatural, twisted word order that violates Ukrainian syntactic flow just to force a rhyme at line's end (e.g. *«Я у садочок вчора пішов, / Там милу квіточку собі знайшов»* ➔ *«Учора я зайшов у сад / й знайшов там квітку»*).
  3. *Semantic Compression*: Compress diluted 4-line stanzas into 2 muscular, razor-sharp lines when the thought is stretched thin.
  4. *Lexical Weight Criterion*: Every word must carry sensory, emotional, or rhythmic necessity. If a word can be removed without harming meaning or cadence, it must be removed.
- **Input Contract**:
  - `draft_text` (string): Poetic draft.
  - `strictness` (enum): `moderate | high | aggressive`.
  - `preserved_meter`: Target meter that must remain intact after compression.
- **Output Contract**:
  - `redundancy_audit`: Identified fillers, unnecessary pronouns, and artificial inversions.
  - `compression_ratio`: Word count before vs after, semantic efficiency score (0–10).
  - `syntax_realignments`: Before/after line comparisons showing restored natural syntax.
  - `concise_draft`: Tightly compressed draft with maximum lexical weight.
- **Edge Cases**:
  - *Fixed Syllable Counts*: When deleting filler syllables in strict meter, replace them with meaningful adjectives, evocative adverbs, or punchier verbs rather than leaving a metric deficit.
  - *Baroque/Ornate Registers*: Allow deliberate syntactic complexity when authentic to 17th-century style, while ensuring it remains authentic rather than calqued.

---

### 3.5 Subagent 5: `poetry-form-synthesizer` (**Архітектор форми та ракурсу**)

- **Ukrainian Identity**: Архітектор форми, ракурсу та фінального синтезу
- **Primary Mission**: Controls the organic unity of form and content, crafts non-trivial perspectives and paradoxical/resonant endings, reconciles competing recommendations from all subagents, performs the final master assembly, and scores the poem against the 100-point rubric.
- **Principles Owned**:
  - **Principle 5**: Оригінальність ракурсу (Originality of Perspective & Non-trivial Angle).
  - **Principle 6**: Органічна єдність форми та змісту (Organic Unity of Form & Content).
- **Core Heuristics & Guardrails**:
  1. *Form-Content Resonance*: Match structural form to psychological state (e.g. anxiety ➔ staccato dolnik/taktovik; philosophical meditation ➔ neoclassical sonnet or sweeping blank verse; tragedy ➔ duma recitative or solemn dactyl).
  2. *Defamiliarization & Perspective Shift (Очуднення)*: Shift the angle from expected macro-abstractions to unexpected micro-perspectives, paradoxes, or overlooked details.
  3. *Volta & Resonant Ending Architecture*: Ensure the poem culminates in a resonant sensory image, philosophical question, or startling paradox rather than a flat summary.
  4. *Master Pipeline Reconciliation*: Act as the supreme arbiter resolving trade-offs (e.g. if conciseness compression broke a rhyme, or imagery expansion broke meter).
  5. *100-Point Rubric Scoring*: Compute the final objective score across all 7 rubric dimensions in `rubric.md`.
- **Input Contract**:
  - `initial_prompt`: User request, theme, parameters.
  - `agent_outputs`: Iterative drafts, scansion reports, and critique from Subagents 1–4.
  - `rubric_standard`: Reference to `references/rubric.md`.
- **Output Contract**:
  - `final_poem`: The complete, polished master poem ready for publication/release.
  - `synthesis_rationale`: Brief explanation of form choice, perspective shift, and volta.
  - `rubric_scorecard`: Full 100-point breakdown table with dimension scores and deductions.
- **Edge Cases**:
  - *Suno AI Lyrics Target*: When intended for musical generation, formats stanza tags (`[Verse]`, `[Chorus]`, `[Drop]`) and vocal cues without degrading literary quality.

---

## 4. Subagent Specification Architecture & File Format

All 5 subagent files in `skills/ukrainian-poetry/agents/` must follow a unified markdown schema with YAML frontmatter:

```markdown
---
name: poetry-imagery-architect
description: |
  Ukrainian poetry specialist for sensory tactility, concrete imagery, and cliché eradication.
  Audits poetic drafts for dead metaphors and abstract noise, replacing them with visceral, show-don't-tell sensory details.
  
  <example>
  orchestrator: dispatches poetry-imagery-architect on draft with "любов-кров" and abstract sorrow.
  output: detects clichés, replaces abstract feelings with physical key freezing in door, returns enhanced draft.
  </example>

  Do NOT use this agent for:
  - Metric scansion and stress checking (use poetry-prosody-phonics)
  - Emotional pathos filtering (use poetry-emotional-critic)
  - Word compression and inversion fixing (use poetry-conciseness-editor)
  - Final master assembly (use poetry-form-synthesizer)
model: gemini-2.5-pro
temperature: 0.7
max_output_tokens: 4096
---

# Poetry Imagery Architect (Образотворець)

[System prompt body with Role, Scope, Constraints, Rules, Heuristics, Input/Output Contracts, and Edge-Case Handling]
```

---

## 5. Pipeline Orchestration & Execution Flows

### 5.1 The 5-Stage Sequential Pipeline (Waterfall)

The primary pipeline executes a sequential refinement cascade from raw thematic draft to master publication-grade poem:

```
[ USER BRIEF / PARAMETERS ]
             │
             ▼
┌─────────────────────────┐
│ 0. Initial Draft Engine │ ──> Generates structural draft baseline
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ 1. Imagery Architect    │ ──> Injects sensory tactility; strips dead clichés
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ 2. Emotional Critic     │ ──> Eliminates false pathos, didactics & melodrama
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ 3. Prosody & Phonics    │ ──> Enforces meter, literary stresses & rich rhymes
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ 4. Conciseness Editor   │ ──> Purges stop-words, water & forced inversions
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ 5. Form Synthesizer     │ ──> Harmonizes form/content, crafts volta & scores
└────────────┬────────────┘
             │
             ▼
[ MASTER UKRAINIAN POEM ] (Score >= 95 / 100)
```

---

### 5.2 Dynamic & Targeted Invocation Modes

The pipeline supports three operational modes:

1. **Full Sequential Pipeline Mode (`--pipeline=full`)**:
   - Default for creating new poems from scratch or doing deep end-to-end rewrites.
   - All 5 subagents execute in strict order with intermediate handoffs.

2. **Targeted Specialist Mode (`--agent=<name>`)**:
   - Dispatches a single specialist agent to address a specific user need:
     - `/ukrainian-poetry --agent=prosody`: Scans and fixes meter, stresses, and rhymes.
     - `/ukrainian-poetry --agent=imagery`: Enhances sensory details and removes clichés.
     - `/ukrainian-poetry --agent=critic`: Checks emotional sincerity and strips preachiness.
     - `/ukrainian-poetry --agent=conciseness`: Condenses text and restores natural word order.

3. **Iterative Synthesizer Feedback Loop (`--loop=iterative`)**:
   - If `poetry-form-synthesizer` detects that conciseness edits disrupted prosodic rhythm, or prosodic changes introduced a cliché, it can route a specific stanza back for a targeted micro-pass before final scoring:

```
                  ┌───────────────────────────────┐
                  │ 5. poetry-form-synthesizer    │
                  └───────────────┬───────────────┘
                                  │
                   Is Rubric Score < 95 or Conflict?
                   ├── Yes (Meter issue) ──> [Stage 3: Prosody micro-pass]
                   ├── Yes (Cliché issue) ──> [Stage 1: Imagery micro-pass]
                   └── No (Score >= 95)  ──> [Emit Master Poem + Scorecard]
```

---

### 5.3 Suno AI Music Generation Pipeline Integration

When a poem is intended for musical production via Suno AI / Flow Music:
1. The **5 Subagents Pipeline** produces the master Ukrainian lyrics.
2. The `poetry-form-synthesizer` applies structural song brackets (`[Intro]`, `[Verse 1]`, `[Chorus]`, `[Drop]`, `[Outro]`) and backing cues `(луна)`.
3. The resulting lyrics are handed off to `skills/ukrainian-poetry-to-suno/` to generate the matching Western genre style box (80–180 chars) and anti-local-pop Exclude vectors.

---

## 6. System Registration & Discoverability

To ensure subagents are discoverable by AI orchestrators and command handlers, they must be registered across 5 key touchpoints:

| Touchpoint / File | Registration Role & Action |
| :--- | :--- |
| `skills/ukrainian-poetry/agents/openai.yaml` | Multi-agent interface manifest declaring all 5 subagents with display names, descriptions, and default prompts. |
| `skills/ukrainian-poetry/SKILL.md` | New **Subagents & Pipeline** section documenting personas, roles, triggers, and execution modes. |
| `skills/poetry-skill/SKILL.md` | Updated master routing table directing tasks to specialized poetry subagents or Suno workflows. |
| `AGENTS.md` (Canonical SSOT) | Core operational directives for all 5 subagents and pipeline execution rules. |
| `commands/ukrainian-poetry.md` & `commands/poetry-skill.md` | Command protocols documenting pipeline execution and subagent arguments. |

---

## 7. Integration with Validation Engine (`rubric.md` & `tests/`)

The 5 subagents directly mirror and safeguard the 7 scoring dimensions in `references/rubric.md`:

```
┌──────────────────────────────────────┬────────────────────────────────────┐
│ Rubric Dimension (Max 100 Pts)       │ Safeguarding Subagent Persona      │
├──────────────────────────────────────┼────────────────────────────────────┤
│ 1. Linguistic Naturalness (25 pts)   │ poetry-prosody-phonics /           │
│                                      │ poetry-conciseness-editor          │
│ 2. Imagery & Concreteness (20 pts)   │ poetry-imagery-architect           │
│ 3. Rhythm & Line-Breaks (15 pts)     │ poetry-prosody-phonics             │
│ 4. Rhyme & Sound Design (10 pts)     │ poetry-prosody-phonics             │
│ 5. Tonal Integrity (10 pts)          │ poetry-emotional-critic            │
│ 6. Ending Strength & Volta (10 pts)  │ poetry-form-synthesizer            │
│ 7. Anti-Cliche & Guardrails (10 pts) │ poetry-imagery-architect /         │
│                                      │ poetry-emotional-critic            │
└──────────────────────────────────────┴────────────────────────────────────┘
```

Deterministic test suites in `tests/` (`poetic_validator.py`, `rubric_scorer.py`, `run_tests.py`) will automatically validate the output of the pipeline against the 85+ passing threshold (with master poems consistently targeting 95–100/100).

---

## 8. Concrete Implementation Plan for R2

When moving from survey to implementation, the required work is cleanly partitioned into:

1. **Create 5 Subagent Markdown Files**:
   - `skills/ukrainian-poetry/agents/poetry-imagery-architect.md`
   - `skills/ukrainian-poetry/agents/poetry-emotional-critic.md`
   - `skills/ukrainian-poetry/agents/poetry-prosody-phonics.md`
   - `skills/ukrainian-poetry/agents/poetry-conciseness-editor.md`
   - `skills/ukrainian-poetry/agents/poetry-form-synthesizer.md`
2. **Update Agent Registry**:
   - `skills/ukrainian-poetry/agents/openai.yaml`
3. **Update Master Skill Files & Directives**:
   - `skills/ukrainian-poetry/SKILL.md` (add section on Subagents & Pipeline)
   - `skills/poetry-skill/SKILL.md` (update routing table)
   - `AGENTS.md` (update SSOT directives)
   - `commands/ukrainian-poetry.md` and `commands/poetry-skill.md`
4. **Validation & Testing**:
   - Run `py -3 tests/run_tests.py --all` to verify zero regression across existing 59 tests.

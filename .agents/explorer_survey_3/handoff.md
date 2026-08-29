# Handoff Report — Explorer 3: Validators, Test Suites & Plugin Sync Survey

**Author**: Explorer 3 (Validators, Tests & Plugin Sync Survey)  
**Date**: 2026-08-29T22:18:45+03:00  
**Working Directory**: `d:\poetry-skill\.agents\explorer_survey_3`  
**Target Scope**: `tests/run_tests.py`, `tests/validator/*`, `tests/*`, `.agents/skills/*`, `skills/*`, `C:\Users\sm9sh\.gemini\config\plugins\poetry-skill\*`  
**Authoritative Specs**: `ai-music-generation-meta-spec-v8.md`, `ORIGINAL_REQUEST.md`, `AGENTS.md`

---

## 1. Observation

### 1.1 Test Runner & Current Baseline Execution
- **Command**: `py -3 tests/run_tests.py --all`
- **Current Execution Status**:
  - Total Test Cases: **63** (Tier 1: 34, Tier 2: 9, Tier 3: 6, Tier 4: 6, Unit + Challengers: 8)
  - Passed: **63 / 63** (100.0% Success Rate)
  - Failed: **0**
  - Warnings: **32**
  - Unit & Challenge Suites: `PASSED (All Unit + Challenger 1 & 2 Tests OK)`
  - Average Poetry Rubric Score: **98.2 / 100** (Passing threshold: >= 85.0 / Target >= 95.0)
  - Average Suno Rubric Score: **99.9 / 100** (Passing threshold: >= 88.0)
- **Observed File Path**: `d:\poetry-skill\tests\run_tests.py` (593 lines)
  - Lines 30–31: `from validator import StyleValidator, MetatagValidator, PoeticValidator, RubricScorer`
  - Lines 80–127: Poetic validation & rubric scoring assertions (`no_surzhyk`, `no_kitsch`, `no_inversions`, `no_filler_words`, `no_cliche_rhymes`, `require_sensory_grounding`, `banned_words`).
  - Lines 130–140: Metatag & song structure validation (`require_intro_or_verse`, `require_chorus`, `valid_metatags`).
  - Lines 142–194: Style prompt validation (`max_chars`, `strict_compact`, `forbidden_references`, `no_metadata_leak`, `no_artist_leak`, `valid_exclude`).
  - Lines 384–529: Deterministic unit tests covering inversions, baroque exemption, filler words, cliché rhymes, sensory grounding, flawed poem rubric penalties, compound metatags, parenthetical instrumental interception, and Challenger 1, 2, and Final suites.

---

### 1.2 Metatag Validation Engine (`tests/validator/metatag_validator.py`)
- **Observed File Path**: `d:\poetry-skill\tests\validator\metatag_validator.py` (207 lines)
- **Current Structural Prefixes** (Lines 29–43):
  ```python
  STRUCTURAL_PREFIXES = [
      "intro", "verse", "pre-chorus", "pre chorus", "chorus", "post-chorus",
      "post chorus", "bridge", "drop", "build-up", "buildup", "build",
      "instrumental", "instrumental break", "instrumental solo", "guitar solo",
      "bandura solo", "sopilka solo", "synth solo", "bass solo", "drum solo",
      "solo", "interlude", "breakdown", "break", "hook", "refrain",
      "spoken word", "spoken", "whisper", "whispering", "chant",
      "polyphonic chant", "outro", "fade out", "fadeout", "fade", "end",
      "ending", "climax", "silence", "pause",
      # Ukrainian equivalents
      "інтро", "куплет", "передприспів", "приспів", "післяприспів",
      "міст", "бридж", "дроп", "програш", "інструментал", "соло",
      "соло гітари", "соло бандури", "соло сопілки", "речитатив",
      "декламація", "шепіт", "аутро", "кінцівка", "фінал", "затихання"
  ]
  ```
- **Current Parenthetical Check** (Lines 46–53, 156–165):
  - `INSTRUMENTAL_KEYWORDS_IN_PARENS`: `["riff", "bassline", "telecaster", "guitar", "bandura", "sopilka", "synth", "drums", "percussion", "arpeggio", "arpeggios", "staccato", "legato", "buildup", "breakdown", "distortion", "reverb", "808", "sub bass", "beat", "solo", "tempo", "bpm", "fade out", "drone", "strings", "cello", "brass", "piano", "organ", "groove", "drop", "бас", "гітара", "барабани", "соло", "дроп", "синтезатор"]`.
  - Blocks instrumental cues from appearing in parentheses `(...)` so audio AI models won't vocalize them.
- **Spec v8 Delta Required**:
  - `ai-music-generation-meta-spec-v8.md` Section 5.1 & Table 5.1 introduces:
    - `[Vocal Intro]` / `[Vocal Intro - dynamic acapella, dry and close]`
    - `[Beat Drop]` / `[Beat Drop - heavy fuzz bass, punchy driving drums]`
    - `[Mega-Chorus]` / `[Mega-Chorus - maximum energy, layered harmonies, guitars clashing]`
    - `[Verse 2 - add driving tambourine, shaker, backing vocals]` (Vance Powell development)
    - Ukrainian equivalents: `[Вокальне інтро]`, `[Біт дроп]`, `[Мега-приспів]`.
  - Spec v8 Section 5.2 introduces 9 inline vocal gestures in parentheses:
    - `(whispered)` / `(whispered, intimate)`
    - `(belted)` / `(belted, powerful)`
    - `(falsetto)`
    - `(screamed)` / `(growl)`
    - `(ad-lib)` / `(vocal runs)`
    - `(building intensity)`
    - `(key change)`
    - `(half-time feel)`
    - `(harmonized)` / `(layered harmonies)`
    - Ukrainian backing vocals: `(луна)`, `(ніколи знов)`, `(веди, дорОга)`.

---

### 1.3 Style / Suno Validation Engine (`tests/validator/style_validator.py` & `suno_validator.py`)
- **Observed File Path**: `d:\poetry-skill\tests\validator\style_validator.py` (258 lines)
- **Current Naming & Structure**:
  - Contains `StyleValidator`, `StyleValidationResult`.
  - `FORBIDDEN_METADATA_LABELS` (Lines 29–42): `Language:`, `Theme:`, `Topic:`, `BPM:`, `Genre:`, etc.
  - `BANNED_ARTISTS` (Lines 45–55): 30+ Ukrainian & global artists.
  - `BANNED_REFERENCE_PHRASES` (Lines 57–69): `in the style of`, `sounds like`, `cover of`, `tribute to`, `similar to`.
  - `VAGUE_EXCLUDE_TOKENS` (Lines 72–76): `sadness`, `depression`, `bad quality`, `noise`.
  - `validate_style_prompt` (Lines 87–173): max_chars=180, strict_compact=120, token check.
- **Spec v8 Delta Required**:
  - `suno_validator.py` is referenced in ORIGINAL_REQUEST.md. An explicit re-export wrapper `tests/validator/suno_validator.py` (`SunoValidator = StyleValidator`) is needed to support both naming schemes.
  - **Two-Method Prompt Support**:
    - Method 1 (Conversational Paragraph): English prose with **"First 5 Words" rule** (`[Genre & Subgenre] + [Vocal Character] + [Instruments] + [Mood/Energy] + [Aesthetic & BPM]`).
    - Method 2 (Tag-Based Matrix): HookGenius 5 modules (`[1. Genre/Subgenre], [2. Mood/Energy], [3. Vocal Triple-Stack], [4. Lead Instruments], [5. Production Aesthetic, BPM]`).
  - **The Negation Trap**:
    - Warn/flag negative constructions inside Style box (`"no drums"`, `"without guitar"`, `"no bass"`).
  - **Multi-Platform Support**:
    - Suno v4.5/v5.5: 80–180 chars optimal, up to 1000 chars max.
    - Udio v4: up to 250 chars (optimal 80–250), context length (10–15s for transitions vs max), inpainting syntax `*stars*`.
    - Google Flow Music (Lyria 3.5): Conversational Agent Mode, 500 daily credits, commercial rights.

---

### 1.4 Poetic Validator & Rubric Scorer (`poetic_validator.py` & `rubric_scorer.py`)
- **Observed File Paths**:
  - `d:\poetry-skill\tests\validator\poetic_validator.py` (959 lines)
  - `d:\poetry-skill\tests\validator\rubric_scorer.py` (251 lines)
- **Current State**:
  - Codifies 6 Core Poetic Principles:
    - Principle 1 (Fresh Imagery & Sensory Grounding): `evaluate_sensory_grounding` (5 sensory categories: tactile, acoustic, visual, thermal, olfactory_gustatory).
    - Principle 2 (Emotional Depth & Sincerity): `DIDACTIC_ENDING_PATTERNS` moralizing deduction (-6 pts).
    - Principle 3 (Rhythmic & Phonic Harmony): meter scansion, heterogeneous rhymes, clausula analysis, euphony (`у/в`, `і/й`, `з/із/зі`).
    - Principle 4 (Conciseness & Word Weight): `check_artificial_inversions` and `check_filler_words_and_pronouns`.
    - Principle 5 (Original Perspective): anti-cliche checks.
    - Principle 6 (Organic Unity of Form & Content): register and form-meter alignment.
  - Capital stressed vowels (`вИпадок`, `чорнОзем`, `прИйде`, `заспівАй`, `дорОга`, `зАмок`, `замОк`, `плАчу`, `плачУ`) are recognized in syllable counting and prosodic checks.
- **Spec v8 Delta Required**:
  - `RubricScorer.score_suno_style`: add recognition for new structural metatags (`[Vocal Intro]`, `[Beat Drop]`, `[Mega-Chorus]`) and inline vocal gestures.
  - Add 10 AI Quality Gates validation scoring helper (`score_ai_quality_gates` or `validate_quality_gates`).

---

### 1.5 Test Suites & Adversarial Test Files
- **Observed Test Files**:
  - `tests/tier1_feature_coverage/` (7 files: meters, non-syllabo-tonic, fixed forms, registers, suno genres, vocal timbres, negative prompts)
  - `tests/tier2_boundary_corner/` (1 file: test_boundary_cases.json)
  - `tests/tier3_cross_feature/` (1 file: test_cross_combinations.json)
  - `tests/tier4_real_world/` (1 file: test_real_world_scenarios.json)
  - `tests/test_adversarial_challenger1.py` (410 lines)
  - `tests/test_adversarial_challenger2.py` (532 lines)
  - `tests/test_adversarial_final.py` (539 lines)
  - `tests/adversarial_suno_stress_test.py`
- **Spec v8 Delta Required**:
  - Expand test cases to cover:
    - Conversational Paragraph vs HookGenius Tag-Based Matrix.
    - Udio v4 prompt structure, Context Length, and inpainting asterisks `*stars*`.
    - Google Flow Music Lyria 3.5 conversational prompt, Spaces & Turntable.
    - Vance Powell Verse 2 development tag `[Verse 2 - add driving tambourine, shaker, backing vocals]`.
    - 10 AI Quality Gates checklist assertions.

---

### 1.6 Plugin Synchronization Survey
- **Locations Surveyed**:
  1. `d:\poetry-skill\skills\` (42 files)
  2. `d:\poetry-skill\.agents\skills\` (42 files)
  3. `C:\Users\sm9sh\.gemini\config\plugins\poetry-skill\` (52 files total: 5 root md/json files, 3 command files, 42 skill files in `skills/`)
  4. Root repository files in `d:\poetry-skill\`: `AGENTS.md`, `GEMINI.md`, `CLAUDE.md`, `INSTALL.md`, `plugin.json`, `lyrics-to-suno-template.md`, `song-structure-pack.md`, `suno-prompt-anti-patterns.md`, `prompt-builder.md`, `reference-to-style-cheatsheet.md`, `mood-to-style-map.md`, `reference-breakdown-examples.md`, `ukrainian-song-scenarios.md`, `ukrainian-poetry-to-suno.md`, `ukrainian-poetry-skill.md`.

---

## 2. Logic Chain

```
[Observation 1.1: Test Baseline]
63 tests passing, 0 failures, 100% success rate on py -3 tests/run_tests.py --all.
                    │
                    ▼
[Observation 1.2: Metatag Validator]
STRUCTURAL_PREFIXES lacks 'vocal intro', 'beat drop', 'mega-chorus'.
INSTRUMENTAL_KEYWORDS_IN_PARENS blocks instrumental text in (), but 9 new inline vocal gestures must be recognized.
                    │
                    ▼
[Logic Step 1: Metatag Update Map]
Add prefixes: 'vocal intro', 'beat drop', 'mega-chorus', 'mega chorus', 'вокальне інтро', 'біт дроп', 'мега-приспів', 'мегаприспів'.
Whitelist and validate 9 inline vocal gestures in parentheses: (whispered), (belted), (falsetto), (screamed), (ad-lib), (building intensity), (key change), (half-time feel), (harmonized).
                    │
                    ▼
[Observation 1.3: Style / Suno Validator]
Module is named style_validator.py; user prompt references suno_validator.py.
Only comma-separated style prompts are currently supported without warnings; Conversational Paragraph (Method 1) and Udio/Flow multi-platform bounds are needed.
                    │
                    ▼
[Logic Step 2: Style / Suno Update Map]
Create tests/validator/suno_validator.py as transparent re-export of StyleValidator.
Add platform support (suno, udio, flow).
Add Method 1 Conversational Paragraph ('First 5 Words' rule) & Method 2 Tag-Based Matrix (HookGenius 5 modules).
Add The Negation Trap detection ('no drums' -> warn/flag, suggest Exclude or positive descriptors).
                    │
                    ▼
[Observation 1.4: Poetic & Rubric Integrity]
6 Poetic Principles and uppercase stress vowels (вИпадок, дорОга) are already fully operational in poetic_validator.py.
Rubric scorer evaluates 7 poetry dimensions and 8 Suno style dimensions.
                    │
                    ▼
[Logic Step 3: Poetic & Rubric Update Map]
Preserve 100% of poetic_validator.py checks without any regression.
Enhance RubricScorer to reward new v8 metatags and vocal gestures.
Add 10 AI Quality Gates evaluation logic.
                    │
                    ▼
[Observation 1.5 & 1.6: Tests & Sync Inventory]
Skill directory (42 files) is mirrored across d:\poetry-skill\skills, d:\poetry-skill\.agents\skills, and C:\Users\sm9sh\.gemini\config\plugins\poetry-skill\skills.
Root symmetric documentation files must be synchronized.
                    │
                    ▼
[Logic Step 4: Full Sync Mapping]
Define precise sync checklist for all 42 skill files + root configs across repository and global plugin directory.
```

---

## 3. Caveats

1. **No Source Code Modifications by Explorer**: As an explorer subagent, all source code modifications are purely surveyed and mapped out; actual editing of source files in `tests/`, `skills/`, and `plugins/` will be executed by designated worker/implementer agents.
2. **Platform Audio Engines**: While Suno v4.5/v5.5, Udio v4, and Google Flow Music Lyria 3.5 have different character limits (up to 1000 chars in Suno/Udio UI), the optimal density for prompt attention remains 80–180 characters (or 8–15 tags, or concise 200-char paragraph). The validator must enforce this as recommended/optimal while allowing up to platform limits with appropriate warnings.
3. **No Caveats on Python 3 Compatibility**: Pure Python 3 standard library with zero third-party dependencies (`re`, `json`, `pathlib`, `unicodedata`, `argparse`, `unittest`) ensures 100% portability across all operating systems.

---

## 4. Conclusion & Actionable Update Mapping

### 4.1 File-by-File Update Specification

| Component | Target File | Specific Updates Required |
| :--- | :--- | :--- |
| **Metatag Validator** | `tests/validator/metatag_validator.py` | 1. Add `"vocal intro"`, `"beat drop"`, `"mega-chorus"`, `"mega chorus"`, `"вокальне інтро"`, `"біт дроп"`, `"мега-приспів"`, `"мегаприспів"` to `STRUCTURAL_PREFIXES`.<br>2. Add `CANONICAL_INLINE_VOCAL_GESTURES` list and support for 9 inline gestures in `(...)`: `(whispered)`, `(belted)`, `(falsetto)`, `(screamed)`, `(ad-lib)`, `(building intensity)`, `(key change)`, `(half-time feel)`, `(harmonized)`.<br>3. Verify bracket `[...]` vs parentheses `(...)` segregation.<br>4. Add metrics for vocal gestures and compound tags. |
| **Suno / Style Validator** | `tests/validator/style_validator.py`<br>`tests/validator/suno_validator.py`<br>`tests/validator/__init__.py` | 1. Create `tests/validator/suno_validator.py` re-exporting `StyleValidator` as `SunoValidator`.<br>2. Update `__init__.py` to export `SunoValidator`.<br>3. Add Method 1 Conversational Paragraph parsing (First 5 Words rule).<br>4. Add Method 2 HookGenius Tag-Based Matrix (5 modules).<br>5. Add Negation Trap detection (`"no drums"`, `"without guitar"`).<br>6. Add multi-platform validation for Udio v4 (Context Length, `*stars*`) and Google Flow Music (Lyria 3.5 conversational mode). |
| **Poetic Validator** | `tests/validator/poetic_validator.py` | 1. Maintain 100% compliance with 6 Poetic Principles.<br>2. Ensure uppercase vowel stress (`вИпадок`, `дорОга`, `замОк`, `зАмок`) and inpainting asterisks (`*static sky*`) pass prosodic validation without regressions. |
| **Rubric Scorer** | `tests/validator/rubric_scorer.py` | 1. Update `score_suno_style` to recognize new v8 metatags and inline vocal gestures.<br>2. Add `score_ai_quality_gates` or helper evaluating the 10 AI Quality Gates. |
| **Test Runner & Suites** | `tests/run_tests.py`<br>`tests/tier1_feature_coverage/*`<br>`tests/tier2_boundary_corner/*`<br>`tests/tier3_cross_feature/*`<br>`tests/tier4_real_world/*` | 1. Update `run_tests.py` unit tests for new metatags, vocal gestures, negation trap, and multi-platform prompts.<br>2. Add test cases in Tier 1–4 suites covering v8 features.<br>3. Guarantee 100% pass with 0 errors on `py -3 tests/run_tests.py --all`. |
| **Sync Inventory** | `skills/`<br>`.agents/skills/`<br>`C:\Users\sm9sh\.gemini\config\plugins\poetry-skill\` | Synchronize all 42 skill files + root configs (`AGENTS.md`, `GEMINI.md`, `CLAUDE.md`, `INSTALL.md`, `plugin.json`, `commands/`, `lyrics-to-suno-template.md`, `song-structure-pack.md`, `suno-prompt-anti-patterns.md`, `prompt-builder.md`, `reference-to-style-cheatsheet.md`, `mood-to-style-map.md`, `reference-breakdown-examples.md`, `ukrainian-song-scenarios.md`, `ukrainian-poetry-to-suno.md`, `ukrainian-poetry-skill.md`). |

---

### 4.2 Detailed Sync Inventory

#### Set A: Root Documentation & Commands
- `AGENTS.md`
- `GEMINI.md`
- `CLAUDE.md`
- `INSTALL.md`
- `plugin.json`
- `commands/poetry-skill.md`
- `commands/ukrainian-poetry-to-suno.md`
- `commands/ukrainian-poetry.md`

#### Set B: Root Templates & Reference Packs
- `lyrics-to-suno-template.md`
- `song-structure-pack.md`
- `suno-prompt-anti-patterns.md`
- `prompt-builder.md`
- `reference-to-style-cheatsheet.md`
- `mood-to-style-map.md`
- `reference-breakdown-examples.md`
- `ukrainian-song-scenarios.md`
- `ukrainian-poetry-to-suno.md`
- `ukrainian-poetry-skill.md`

#### Set C: Skill Directories (Sync: `skills/` <-> `.agents/skills/` <-> `C:\Users\sm9sh\.gemini\config\plugins\poetry-skill\skills/`)
1. `poetry-skill/`
   - `SKILL.md`
2. `ukrainian-poetry/`
   - `SKILL.md`
   - `agents/openai.yaml`
   - `agents/poetry-conciseness-editor.md`
   - `agents/poetry-emotional-critic.md`
   - `agents/poetry-form-synthesizer.md`
   - `agents/poetry-imagery-architect.md`
   - `agents/poetry-prosody-phonics.md`
   - `references/full-guide.md`
   - `references/input-templates.md`
   - `references/rubric.md`
   - `references/stress-tests.md`
   - `references/tests.md`
3. `ukrainian-poetry-to-suno/`
   - `SKILL.md`
   - `agents/openai.yaml`
   - `references/full-guide.md`
   - `references/lyrics-to-suno-template.md`
   - `references/mood-to-style-map.md`
   - `references/prompt-builder.md`
   - `references/reference-breakdown-examples.md`
   - `references/reference-to-style-cheatsheet.md`
   - `references/rubric.md`
   - `references/song-structure-pack.md`
   - `references/suno-prompt-anti-patterns.md`
   - `references/tests.md`
   - `references/ukrainian-song-scenarios.md`
   - `references/packs/README.md`
   - `references/packs/dark-pack.md`
   - `references/packs/female-vocal-pack.md`
   - `references/packs/male-vocal-pack.md`
   - `references/packs/sad-pack.md`
   - `references/packs/suno-reference-prompt-pack-uk.md`
   - `references/packs/suno-reference-prompt-pack.md`
   - `references/packs/uplifting-pack.md`

---

## 5. Verification Method

### 5.1 Deterministic Test Suite Commands
1. **Full Test Suite Execution**:
   ```bash
   py -3 tests/run_tests.py --all
   ```
   - **Expected Outcome**: Exit code 0, 0 failed tests, 100% pass rate, Average Poetry Score >= 95/100, Average Suno Score >= 95/100.
2. **Dedicated Validator Engine Unit Tests**:
   ```bash
   py -3 tests/run_tests.py --unit
   ```
   - **Expected Outcome**: Passes all unit checks including Challenger 1, Challenger 2, and Final adversarial tests.
3. **Specific Tier Validations**:
   ```bash
   py -3 tests/run_tests.py --tier 1
   py -3 tests/run_tests.py --tier 2
   py -3 tests/run_tests.py --tier 3
   py -3 tests/run_tests.py --tier 4
   ```

### 5.2 File & Integrity Inspections
1. Verify `tests/validator/suno_validator.py` exists and exports `SunoValidator = StyleValidator`.
2. Inspect `tests/validator/metatag_validator.py` to confirm `STRUCTURAL_PREFIXES` includes `vocal intro`, `beat drop`, `mega-chorus` and valid parenthetical vocal gestures are supported.
3. Check that `.agents/skills/` and `C:\Users\sm9sh\.gemini\config\plugins\poetry-skill\` contain all identical 42 skill files with 0 missing files.

### 5.3 Invalidation Conditions
- Any test failure in `py -3 tests/run_tests.py --all`.
- Any regression in the 6 Core Poetic Principles or syllable counting of capital stressed vowels (`вИпадок`, `дорОга`).
- Any syntax rejection of valid compound metatags (`[Intro - Staccato cutting telecaster riff, driving bassline]`, `[Verse 2 - add driving tambourine, shaker, backing vocals]`) or inline vocal gestures `(whispered)`, `(belted)`, `(falsetto)`, `(ad-lib)`.
- Discrepancy in file count or content between `skills/`, `.agents/skills/`, and `C:\Users\sm9sh\.gemini\config\plugins\poetry-skill\`.


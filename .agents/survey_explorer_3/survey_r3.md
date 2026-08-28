# Survey & Technical Specification: Requirement R3 — Validation, Rubric Scoring & Test Suite

**Author**: `survey_explorer_3`  
**Date**: 2026-08-28  
**Scope**: Codebase audit, architecture analysis, and integration blueprint for Requirement R3 (Validation, Rubric Scoring, Test Suite, and Suno Interoperability).

---

## 1. Executive Summary

Requirement R3 mandates the enhancement of the validation and scoring engine of `poetry-skill` to programmatically enforce the **6 Fundamental Poetic Principles**:
1. **Свіжа образність та метафоричність** (Fresh Imagery & Sensory Grounding vs Cliches)
2. **Емоційна глибина та щирість** (Emotional Depth & Sincerity vs Melodramatic Pathos)
3. **Ритмічна та звукова гармонія** (Rhythmic & Phonic Euphony vs Mechanical Padding)
4. **Лаконічність і вага слова** (Conciseness & Word Density vs Artificial Inversions & Filler Pronouns)
5. **Оригінальність ракурсу** (Original Perspective & Paradoxical Resolution vs Didactic Moralizing)
6. **Органічна єдність форми та змісту** (Organic Unity of Form & Content)

### Baseline Execution Metrics
- **Test Harness**: `py -3 tests/run_tests.py --all`
- **Total Test Cases**: 59 test cases across 4 tiers
- **Current Pass Rate**: **100% (59/59 passed, 0 failed, 31 warnings)**
- **Average Poetry Rubric Score**: **98.2 / 100** (passing threshold: >= 85.0 / 100)
- **Average Suno Rubric Score**: **99.9 / 100** (passing threshold: >= 88.0 / 100)
- **Execution Speed**: ~2.5s execution across all 10 suite files in Python 3.

---

## 2. In-Depth Architectural Analysis of Current Test & Validation Engine

The testing and validation subsystem is located under `tests/` and structured into distinct modular components:

```
tests/
├── run_tests.py                          # Master E2E runner, CLI harness & reporter
├── run_tests.ps1                         # PowerShell test trigger wrapper
├── adversarial_suno_stress_test.py       # Suno stress harness (token economy, boundary cases)
├── test_adversarial_challenger1.py       # Poetic stress harness (homographs, taboo bans, meters)
├── test_adversarial_final.py             # Final adversarial harness (Unicode diacritics, caesura)
├── validator/
│   ├── __init__.py                       # Package exports (PoeticValidator, RubricScorer, etc.)
│   ├── poetic_validator.py               # Deterministic Ukrainian versification & linguistic engine
│   ├── rubric_scorer.py                  # 100-point rubric scoring engine (Poetry & Suno)
│   ├── style_validator.py                # Suno Style prompt token economy & purity validator
│   └── metatag_validator.py              # Suno bracketed metatag & structure validator
├── tier1_feature_coverage/               # 7 JSON suites (39 tests: meters, genres, registers, forms)
├── tier2_boundary_corner/                # 1 JSON suite (8 tests: taboo bans, BPM extremes, 120-cap)
├── tier3_cross_feature/                  # 1 JSON suite (6 tests: full E2E pipeline combinations)
├── tier4_real_world/                     # 1 JSON suite (6 tests: production commercial briefs)
└── reports/
    └── test_report.json                  # Detailed execution log & breakdown
```

### 2.1 `tests/validator/poetic_validator.py`
The `PoeticValidator` class provides deterministic, rule-based linguistic and prosodic checks without relying on heavy external dependencies:
1. **Unicode-Aware Syllable Counting (`count_syllables`)**:
   - Strips bracketed tags `[...]` and parenthetical backing vocals `(...)`.
   - Strips combining Unicode diacritics (`[\u0300-\u036f]`), ensuring acute accents (`\u0301`) do not corrupt syllable counts.
   - Counts Ukrainian vowels against `UKR_VOWELS = set("аеєиіїоуюяАЕЄИІЇОУЮЯ")`.
2. **Surzhyk and Russianism Filtering (`check_surzhyk_and_russianisms`)**:
   - 29 compiled regex patterns in `SURZHYK_DICTIONARY` detecting calques (*самий кращий*, *приймати участь*, *на протязі дня*, *являється*, *слідуючий*, *получається*).
3. **Taboo Word Bans & Inflectional Matching (`check_taboo_words`)**:
   - `TABOO_STEM_MAP` covering 8 core abstract cliches (*душа, серце, доля, вічність, життя, кохання, сльози, біль*) with morphological inflection stems.
4. **Anti-Sharovarshchyna Guardrail (`check_sharovarshchyna`)**:
   - Rejects unprompted kitsch tokens (*шаровари, шароварщина, сало, горілка, кунтуш, чуприна*) in non-folk registers.
5. **Stress Homograph Validation (`check_stress_homographs`)**:
   - 13 canonical Ukrainian homograph pairs (*замок, білизна, наголос, обід, мука, дорога, атлас, орган, плачу, образи, бігом, визнання, потяг*).
   - Validates whether explicit acute accent marks (`\u0301`) or capital stress notations are applied.
6. **Clausula Cadence & Rhyme Analysis (`classify_clausula`, `check_clausula_alternation`, `check_grammatical_rhymes`)**:
   - Classifies line endings into Masculine (M), Feminine (F), Dactylic (D), or Unknown (U).
   - Verifies 4-line stanza alternation patterns (`FMFM`, `MFMF`, `FFMM`, `MMFF`, `FMMF`, `MFFM`).
   - Detects cheap grammatical verb-verb (`-ати/-яти`, `-ить/-їть`) and suffix-suffix (`-ами/-ями`, `-ості/-істю`, `-ного/-ному`) rhymes.
7. **Meter Scansion Engine (`check_meter_consistency`)**:
   - Supports Syllabo-Tonic binary (Iamb, Trochee) with variance threshold `<= 1.5`.
   - Supports Syllabo-Tonic ternary (Dactyl, Amphibrach, Anapest) with variance threshold `<= 2.0`.
   - Supports Non-Syllabo-Tonic (Dolnik, Taktovik) with accentual bounds.
   - Supports 14-syllable Kolomyika with strict 4+4+6 caesura verification.

### 2.2 `tests/validator/rubric_scorer.py`
The `RubricScorer` implements programmatic evaluation aligned with the 100-point rubric in `skills/ukrainian-poetry/references/rubric.md`:

| Dimension | Max Points | Current Calculation & Deductions |
| :--- | :---: | :--- |
| **1. Linguistic Naturalness** | 25 | Deducts 10 pts per Surzhyk error (max -20 pts). |
| **2. Imagery & Concreteness** | 20 | Deducts 8 pts if line count < 4. |
| **3. Rhythm & Line Breaks** | 15 | Deducts 6 pts if syllable variance > 4 in syllabo-tonic verse. |
| **4. Rhyme & Sound Design** | 10 | Deducts 2 pts per cheap grammatical rhyme (max -6 pts); 10 pts default for free verse. |
| **5. Tonal Integrity** | 10 | Deducts 5 pts for register mismatch errors. |
| **6. Ending Strength** | 10 | Deducts 6 pts for didactic / moralizing patterns in final 2 lines (`DIDACTIC_ENDING_PATTERNS`). |
| **7. Anti-Cliche Guardrails** | 10 | Deducts 5 pts per taboo word (max -10 pts); deducts 5 pts for kitsch/sharovarshchyna. |
| **Total** | **100** | **Passing threshold >= 85.0 / 100** |

### 2.3 `tests/run_tests.py` and Test Suite Execution
`run_tests.py` serves as the test orchestrator:
- Dispatches test cases to `PoeticValidator`, `MetatagValidator`, and `StyleValidator`.
- Computes `poetry_rubric` and `suno_rubric` scores.
- Evaluates test assertions (`no_surzhyk`, `no_kitsch`, `banned_words`, `expected_meter`, `valid_metatags`, `no_metadata_leak`, `no_artist_leak`).
- Generates JSON summary reports to `tests/reports/test_report.json`.

---

## 3. Integration Blueprint for New Criteria (Requirement R3)

To fully integrate the 6 Poetic Principles into `PoeticValidator` and `RubricScorer`, three new deterministic check modules must be introduced alongside rubric re-weighting:

```
                  ┌─────────────────────────────────────────────────────────┐
                  │                 PoeticValidator Engine                  │
                  └──────────────────────────┬──────────────────────────────┘
                                             │
      ┌──────────────────────────────────────┼──────────────────────────────────────┐
      │                                      │                                      │
      ▼                                      ▼                                      ▼
┌───────────────────────────┐  ┌───────────────────────────┐  ┌───────────────────────────┐
│ 1. Artificial Inversions  │  │  2. Filler Pronouns &     │  │  3. Sensory Details &     │
│    (Штучні інверсії)      │  │     Rhythmic Crutches     │  │     Fresh Imagery vs      │
│                           │  │     (Заповнювачі метра)   │  │     Banal Clichés         │
└─────────────┬─────────────┘  └─────────────┬─────────────┘  └─────────────┬─────────────┘
              │                              │                              │
              ▼                              ▼                              ▼
      [PoeticValidator.              [PoeticValidator.              [PoeticValidator.
    check_artificial_inversions]   check_filler_words_and_pronouns] check_cliche_rhymes_and_metaphors]
              │                              │                              │
              └──────────────────────────────┼──────────────────────────────┘
                                             │
                                             ▼
                  ┌─────────────────────────────────────────────────────────┐
                  │          RubricScorer (100-Point Evaluation)            │
                  ├─────────────────────────────────────────────────────────┤
                  │ 1. Linguistic Naturalness & Syntax: 25 pts (Inversions) │
                  │ 2. Imagery & Sensory Concreteness: 20 pts (Sensory lex) │
                  │ 3. Rhythm & Word Weight: 15 pts (Filler crutches)       │
                  │ 4. Rhyme & Sound Design: 10 pts (Phonics/heterogeneity) │
                  │ 5. Emotional Depth & Tonal Sincerity: 10 pts (Anti-path)│
                  │ 6. Perspective & Ending Strength: 10 pts (Anti-didactic)│
                  │ 7. Anti-Cliche & Anti-Sharovarshchyna: 10 pts (Taboos)  │
                  └─────────────────────────────────────────────────────────┘
```

---

### 3.1 Criterion A: Artificial Inversions (Штучні синтаксичні інверсії заради рими)

#### Poetic Rationale
Ukrainian has flexible word order, but poetry of high quality preserves **natural phrasing** and organic syntactic breathing. Artificial inversion occurs when an author distorts normal Ukrainian word order solely to place a rhyming token at the end of a line (e.g. putting personal pronouns or inverted clitics at the cadence).

#### Anti-Patterns to Detect
1. **Verb + Postpositive Subject Pronoun at line end**:
   - *побачив я*, *пішов ти*, *сказала вона*, *знаємо ми*, *кричать вони*.
   - Natural phrasing: *я побачив*, *ти пішов*, *вона сказала*.
2. **Inverted Possessive Pronoun at line end**:
   - *рука моя*, *очей твоїх*, *в оселі твоїй*, *на серці моїм* (when used repeatedly as a mechanical rhyming device).
3. **Dislocated Auxiliaries & Subordinators at line end**:
   - *щоб сказати тобі*, *додому щоб іти*, *який був він*.

#### Implementation Strategy in `PoeticValidator`
```python
# Regex patterns for artificial line-end inversions
ARTIFICIAL_INVERSION_PATTERNS = [
    # Verb + Personal Pronoun at line end (past/present/future inflections + pronoun)
    (r"\b([а-яіїєґА-ЯІЇЄҐ]+(в|ла|ло|ли|ю|єш|є|ємо|єте|ить|ять|уть|нув|нула|нуло|нули))\s+(я|ти|він|вона|воно|ми|ви|вони)\s*$", 
     "Штучна інверсія 'дієслово + особовий займенник' у кінці рядка заради рими"),
    # Conjunction / Particle dislocation at line end
    (r"\b([а-яіїєґА-ЯІЇЄҐ]+)\s+(що|щоб|як|мов|немов|ніби|бо)\s*$", 
     "Синтаксичний розрив сполучника в кінці рядка"),
]
```
- **Validator Method**: `PoeticValidator.check_artificial_inversions(poem_text: str, mode: str = "general") -> List[Dict[str, Any]]`
- **Output**: Returns detected line numbers, offending tokens, and natural word order suggestions.
- **Scorer Mapping**: Deducts **2.0 pts per inversion** (max -6.0 pts) under `linguistic_naturalness` (Dimension 1).

---

### 3.2 Criterion B: Filler Pronouns & Rhythmic Crutches (Зайві займенники-заповнювачі заради метра)

#### Poetic Rationale
Weak poetry frequently inserts semantically empty monosyllabic particles and redundant personal pronouns to pad syllable counts and force feet to fit a mechanical meter ("вода" заради розміру).

#### Anti-Patterns to Detect
1. **Pleonastic Particle Clusters**:
   - *і ось*, *ну от*, *але ж бо*, *та й ось*, *то ж бо*, *а я ось*.
2. **Excessive 1st/2nd Person Pronoun Density**:
   - 4 or more occurrences of (*я, ти, мій, твій, мені, тобі, мене, тебе*) within a single 4-line stanza without syntactic necessity.
3. **Pleonastic Demonstrative Padding**:
   - *у цей же день*, *в ту саму мить*, *той самий час*.

#### Implementation Strategy in `PoeticValidator`
```python
FILLER_RHYTHMIC_CRUTCHES = [
    r"\b(і\s+ось)\b",
    r"\b(ну\s+от)\b",
    r"\b(але\s+ж\s+бо)\b",
    r"\b(та\s+й\s+ось)\b",
    r"\b(то\s+ж\s+бо)\b",
    r"\b(а\s+я\s+ось)\b",
    r"\b(вже\s+ж\s+бо)\b",
]
```
- **Validator Method**: `PoeticValidator.check_filler_words_and_pronouns(poem_text: str) -> List[Dict[str, Any]]`
- **Output**: Returns detected padding tokens and stanza-level pronoun density metric.
- **Scorer Mapping**: Deducts **2.0 pts per filler cluster** (max -4.0 pts) under `rhythm_line_breaks` (Dimension 3).

---

### 3.3 Criterion C: Sensory Details & Fresh Imagery vs Banal Cliches (Сенсорні деталі vs кліше/абстракції)

#### Poetic Rationale
Authentic Ukrainian poetry avoids abstract emotional noise (*душа плаче*, *серце крається*, *туга-розлука*) and roots imagery in **tactile, acoustic, visual, and physical reality** (Show, Don't Tell).

#### Anti-Patterns & Blacklist Pairs
- **Banal Rhyme Pairs**:
  - *кров - любов*, *серце - перце*, *доля - воля*, *ніч - віч*, *зорі - морі*, *сльози - морози*, *туга - розлука*, *день - пень*, *рано - кохано*.
- **Abstract Declarations without Sensory Grounding**:
  - *моя любов безмежна*, *душа горить у вічності*, *серце плаче від болю*.

#### Positive Sensory Lexicon Categories
- **Tactile**: *іржа, мідь, вапно, гравій, холодний шовк, шорсткий, глина, волога шкіра*.
- **Acoustic**: *рип, шелест, скрегіт, свист, гул, дзенькіт, тріск, луна*.
- **Visual & Atmospheric**: *попіл, морок, бурштин, слюда, полин, чад, відблиск*.

#### Implementation Strategy in `PoeticValidator`
```python
BANAL_RHYME_BLACKLIST = [
    ("любов", "кров"), ("серце", "перце"), ("доля", "воля"),
    ("ніч", "віч"), ("зорі", "морі"), ("сльози", "морози"),
    ("туга", "розлука"), ("день", "пень"), ("рано", "кохано"),
]

SENSORY_LEXICON = {
    "tactile": ["іржа", "мідь", "вапно", "гравій", "шовк", "шорстк", "глин", "шкір", "льод", "криг", "холод", "тепл"],
    "acoustic": ["рип", "шелест", "скрегіт", "свист", "гул", "дзеньк", "тріск", "лун", "дзвін", "гомін"],
    "visual_atmospheric": ["попіл", "морок", "бурштин", "слюд", "полин", "чад", "відблиск", "дим", "смол", "тінь"],
}
```
- **Validator Method**: `PoeticValidator.check_cliche_rhymes(poem_text: str) -> List[Tuple[str, str]]`
- **Validator Method**: `PoeticValidator.evaluate_sensory_grounding(poem_text: str) -> Dict[str, Any]`
- **Scorer Mapping**:
  - Deducts **4.0 pts per blacklisted cliché rhyme** under `anti_cliche_guardrails` (Dimension 7).
  - Evaluates `imagery_concreteness` (Dimension 2): awards full points (20/20) for sensory grounding; deducts **3.0 pts** if text is purely abstract.

---

## 4. Updated 100-Point Rubric Specification (Aligned with R1/R3)

The programmatic rubric calculation in `RubricScorer.score_poetry` directly mirrors the updated specification in `rubric.md`:

```text
========================================================================================
100-POINT UKRAINIAN POETRY RUBRIC SPECIFICATION (REFINED)
========================================================================================
1. Linguistic Naturalness & Syntax (Природність мови та синтаксис):         ___ / 25
   - Native syntax, correct accents, euphony (у/в, і/й).
   - Zero Surzhyk / Russianisms.
   - Zero artificial inversions for rhyme forced endings.
   - Deductions: -10 pts per Surzhyk; -2 pts per artificial inversion (max -6 pts).

2. Imagery & Sensory Concreteness (Образність і тактильна конкретика):       ___ / 20
   - Show, Don't Tell: tactile, acoustic, visual physical textures.
   - Fresh metaphors vs abstract emotional declarations.
   - Deductions: -8 pts if lines < 4; -3 pts if devoid of sensory textures.

3. Rhythm & Word Weight (Ритмічна дисципліна та вага слова):               ___ / 15
   - Strict meter stability (Syllabo-tonic, Dolnik intervals, Kolomyika 4+4+6).
   - Absence of filler pronouns & rhythmic crutches (вода заради метра).
   - Deductions: -6 pts for syllable variance > 4; -2 pts per filler crutch (max -4 pts).

4. Rhyme, Phonics & Sound Design (Рима, фоніка та звукопис):               ___ / 10
   - Heterogeneous rhymes (noun+verb, adverb+noun), rich consonant support.
   - Assonances, alliterations, clean clausula alternation.
   - Deductions: -2 pts per cheap grammatical rhyme (max -6 pts).

5. Emotional Depth & Tonal Sincerity (Емоційна глибина та щирість):        ___ / 10
   - Zero fake pathos, zero theatrical melodrama, zero mentor moralizing.
   - Sustained register authenticity.
   - Deductions: -5 pts for register inconsistency.

6. Original Perspective & Ending Resonance (Ракурс і резонанс фіналу):     ___ / 10
   - Novel angle on themes, paradoxical twist, micro-detail focus.
   - Zero didactic/moralizing conclusions (висновок простий, треба жити).
   - Deductions: -6 pts for didactic ending patterns.

7. Anti-Cliche & Anti-Sharovarshchyna (Антиштампи та антишароварщина):      ___ / 10
   - Zero banned taboo words (душа, серце, доля, вічність, життя, кохання).
   - Zero kitsch / sharovarshchyna tokens.
   - Zero blacklisted cliché rhyme pairs (кров-любов, серце-перце).
   - Deductions: -5 pts per taboo word; -5 pts for kitsch; -4 pts per cliché rhyme.
----------------------------------------------------------------------------------------
TOTAL SCORE:                                                                ___ / 100
PASSING THRESHOLD:                                                          >= 85 / 100
========================================================================================
```

---

## 5. Interaction with `ukrainian-poetry-to-suno` & Backward Compatibility

### 5.1 Pipeline Interoperability Analysis
In cross-feature combinations (Tier 3) and real-world scenarios (Tier 4), poetic lyrics flow into Suno AI prompts:
1. **Input Payload**: Contains `style_of_music`, `lyrics` (with bracketed structural metatags `[Intro]`, `[Verse]`, `[Chorus]`), and `exclude`.
2. **Tag Stripping**: `PoeticValidator.get_lines_without_tags` strips `[...]` lines and parenthetical backing cues `(...)`.
3. **Parallel Validation**:
   - `PoeticValidator` checks lyrics for meter, rhymes, inversions, fillers, and taboos.
   - `MetatagValidator` verifies bracket syntax and section flow.
   - `StyleValidator` verifies character economy (80–180 chars), metadata purity, and de-identification.
   - `RubricScorer.score_poetry` and `RubricScorer.score_suno_style` calculate independent 100-point scores.

### 5.2 Backward Compatibility & Zero-Regression Guarantee
- **Existing 59 Test Cases**: All 59 tests in Tier 1 through Tier 4 currently pass with an average poetry score of **98.2/100**.
- **Tuning Heuristics**: The new checks (artificial inversions, filler crutches, sensory grounding) must be calibrated so that legitimate poetic inversions in classical/folk forms (e.g. *TC_T1_REG_04_Cossack_Baroque*, *TC_T1_FIX_01_Petrarchan_Sonnet*) are recognized without generating false-positive errors.
- **Pass Threshold**: All existing suites must maintain `>= 95/100` average rubric score.

---

## 6. Detailed Recommendations for Dev/Implementation Phase

1. **Update `tests/validator/poetic_validator.py`**:
   - Add `check_artificial_inversions` with line-end pronoun and syntactic dislocation heuristics.
   - Add `check_filler_words_and_pronouns` with particle cluster matching and pronoun density calculation.
   - Add `check_cliche_rhymes` and `evaluate_sensory_grounding` with sensory lexicon.
   - Expose metrics in `PoeticValidationResult.metrics`: `inversion_count`, `filler_count`, `cliche_rhyme_count`, `sensory_score`.
2. **Update `tests/validator/rubric_scorer.py`**:
   - Wire new metrics into `score_poetry`:
     - Deduct for artificial inversions in Dimension 1.
     - Deduct for filler rhythmic crutches in Dimension 3.
     - Deduct for cliché rhymes and score sensory grounding in Dimensions 2 & 7.
3. **Update `skills/ukrainian-poetry/references/rubric.md`**:
   - Update markdown documentation to align with refined 100-point criteria and deduction table.
4. **Expand Test Suites (`tests/tier*`)**:
   - Add dedicated test cases covering the new criteria (e.g. detecting and rejecting artificial inversions, verifying fresh sensory imagery).
5. **Verify Full Test Suite**:
   - Execute `py -3 tests/run_tests.py --all` ensuring 100% pass rate, 0 errors, and average poetry score `>= 95/100`.

---

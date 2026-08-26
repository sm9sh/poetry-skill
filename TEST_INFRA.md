# TEST_INFRA: Ukrainian Poetry & Suno AI Test Architecture & Validation Framework

**Document Version**: 2.0.0  
**Status**: ACTIVE / CANONICAL  
**Target Milestone**: E2E Track (Feature F17) & Final Verification (Feature F18)  
**Author**: Worker E2E (E2E Testing Track & Test Infrastructure Specialist)  

---

## 1. Executive Summary & Testing Philosophy

The Ukrainian Poetry and Suno AI Skill System (`ukrainian-poetry` and `ukrainian-poetry-to-suno`) constitutes a high-precision dual-engine creative generation pipeline. To ensure oral authenticity, prosodic correctness, acoustic viability, and prompt-token efficiency without hallucinations or kitsch, testing is governed by an automated, multi-tiered, deterministic validation framework coupled with a 100-point evaluation rubric.

### 1.1 Core Testing Principles
1. **Zero Hallucination Tolerance**: Strict programmatic verification of metatags, character caps, and token isolation between musical style and lyrics.
2. **Linguistic Authenticity First**: Programmatic detection of Russianisms, Surzhyk calques, stress distortions (*переакцентуація*), and cheap grammatical rhyming.
3. **Acoustic Token Economy**: Strict character-budget enforcement (<=180 chars absolute, optimal 80-150 chars, strict <=120 chars in compact mode) with zero metadata contamination (`Language:`, `Theme:`, `BPM:` as text labels inside style box strictly forbidden).
4. **Deterministic Rigor + Heuristic Scoring**: Automated static assertions for pass/fail gating combined with multi-dimensional 100-point rubric scoring.

---

## 2. Testing Methodologies

The test architecture incorporates four complementary software testing methodologies adapted for generative prompt engineering and natural language versification:

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                         MASTER TESTING METHODOLOGIES                             │
├────────────────────────┬─────────────────────────────────────────────────────────┤
│ 1. Category-Partition  │ Deconstructs input parameters (meters, registers,       │
│    Method (TSL)        │ genres, timbres) into discrete categories & partitions. │
├────────────────────────┼─────────────────────────────────────────────────────────┤
│ 2. Boundary Value      │ Tests limits: 120-char style cap, 180-char max cap,     │
│    Analysis (BVA)      │ 60 vs 180 BPM, 2-line haiku vs 32-line ballad, caesura. │
├────────────────────────┼─────────────────────────────────────────────────────────┤
│ 3. Pairwise Testing    │ Orthogonal combinations across 4 feature dimensions     │
│    (Combinatorial)     │ (Poetic Register × Music Genre × Vocal × Structure).    │
├────────────────────────┼─────────────────────────────────────────────────────────┤
│ 4. Real-World          │ Production-grade briefs reflecting actual commercial,   │
│    Workloads           │ broadcast, cinematic, and educational song releases.    │
└────────────────────────┴─────────────────────────────────────────────────────────┘
```

### 2.1 Category-Partition Method (TSL)
Inputs are partitioned into orthogonal equivalence classes across both domains:
- **Versification Systems**: Syllabo-Tonic (Iamb, Trochee, Dactyl, Amphibrach, Anapest), Non-Syllabo-Tonic (Dolnik 3/4-stress, Taktovik, Kolomyika 14-syllable), Fixed Forms (Sonnet, Rondo, Triolet, Terza Rima), Free Verse (*Верлібр*), Blank Verse (*Білий вірш*).
- **Poetic Registers**: Urban/Contemporary, Intimate/Chamber, Neoclassical, Cossack Baroque, Authentic Folk/Carpathian, Children/Playful.
- **Suno Music Genres**: Ethno-Chaos, Post-Punk / Coldwave, Dark Synth / Cyberpunk, Trap-Folk, Melodic Metalcore, Shoegaze / Dream Pop, Ethno-Rock, Neoclassical Bandura.
- **Vocal Timbres**: White Voice (*білий голос*), Intimate Breathy, Spoken Melodeclamation, Extreme Vocals (Growl/Scream), Modern Autotuned Trap.
- **Structural Dynamics**: Standard Verse-Chorus, Acoustic-to-Drop, Multi-Vocal Duet, Accelerando / Tempo Shift, Spoken-to-Belted.

### 2.2 Boundary Value Analysis (BVA)
Boundary conditions stress the outer operating envelopes of the models:
- **Style Field Lengths**: 
  - Sub-nominal: <40 characters (under-specified style).
  - Strict Compact Cap: 100–120 characters (optimal for Suno v3/v4 token retention).
  - Standard Cap: 120–180 characters.
  - Hard Limit Violation: >180 characters (flagged as prompt truncation failure).
- **Tempo Boundaries**: 45–60 BPM (ultra-slow ambient/drone) vs 170–190 BPM (cyber-folk dnb/metalcore).
- **Structural Lengths**: 2 stanzas (8 lines) vs 8 stanzas (32 lines) with metrical persistence.
- **Stress-Sensitive Homographs**: Disambiguation under metrical pressure (e.g. `зАмок` vs `замОк`, `мукА` vs `мУка`, `дорОга` vs `дорогА`).

### 2.3 Pairwise Combinatorial Matrix
Pairwise testing systematically validates orthogonal interactions to prevent failure modes where a valid poetic register clashes with a modern music prompt:
- `[Folk Register]` × `[Dark Synth / Industrial]` × `[Female White Voice]`
- `[Cossack Baroque]` × `[Melodic Metalcore]` × `[Harsh/Clean Dual Vocal]`
- `[Chamber Intimate]` × `[Neoclassical Bandura]` × `[Whispered Delivery]`
- `[Urban Contemporary]` × `[Shoegaze / Dream Pop]` × `[Reverb-Drenched Male Vocal]`
- `[Bilingual UA/EN]` × `[Modern Pop-Rock]` × `[Clean Radio Vocal]`

### 2.4 Real-World Application Workloads
Simulates end-to-end commercial workflows with full briefs, lyrical generation, metatag arrangements, and dual-field Suno prompts for real production scenarios.

---

## 3. Feature Inventory Traceability Matrix (F1–F18)

| Feature ID | Feature Name | Test Tier | Primary Test Cases | Automated Assertion Module |
|---|---|---|---|---|
| **F1** | Dactyl & Ternary Meters | Tier 1, Tier 2 | `TC_T1_MET_03`, `TC_T2_02` | `poetic_validator.py` (3-syllable foot rhythm scanner) |
| **F2** | Non-Syllabo-Tonic (Dolnik, Taktovik, Kolomyika) | Tier 1, Tier 2 | `TC_T1_NST_01`–`04`, `TC_T2_04` | `poetic_validator.py` (Stress interval & 4+4+6 caesura) |
| **F3** | Blank Verse (*Білий вірш*) | Tier 1 | `TC_T1_NST_05` | `poetic_validator.py` (Strict meter, unrhymed clausulae) |
| **F4** | Fixed Poetic Forms (Sonnet, Rondo, Triolet, Terza Rima) | Tier 1 | `TC_T1_FIX_01`–`05` | `poetic_validator.py` (Stanza & rhyme topology checker) |
| **F5** | Clausula Alternation & Line Cadence | Tier 1, Tier 2 | `TC_T1_MET_01`–`05`, `TC_T2_03` | `poetic_validator.py` (F/M/D clausula cadence scanner) |
| **F6** | Stress & Mobile Accentuation Engine | Tier 2 | `TC_T2_07` | `poetic_validator.py` (Homograph dictionary & stress checker) |
| **F7** | Heterogeneous Rhyme & Anti-Grammatical Blacklist | Tier 1, Tier 2 | `TC_T1_MET_01`, `TC_T2_01` | `poetic_validator.py` (Cross-POS rhyme classifier) |
| **F8** | 6 Authentic Registers & Anti-Sharovarshchyna | Tier 1, Tier 4 | `TC_T1_REG_01`–`06`, `TC_T4_01`–`04` | `poetic_validator.py` (Kitsch & register vocabulary scanner) |
| **F9** | Style Prompt Token Economy (80–180 Chars) | Tier 1, Tier 2 | `TC_T1_GEN_01`–`08`, `TC_T2_05` | `style_validator.py` (Length, character-budget & metadata filter) |
| **F10** | Bracketed Metatag Syntax & Arrangement | Tier 1, Tier 3 | `TC_T1_GEN_01`–`08`, `TC_T3_01`–`05` | `metatag_validator.py` (Bracket syntax, valid tags, no prose) |
| **F11** | 8-Genre Modern Ukrainian Music Taxonomy | Tier 1, Tier 3 | `TC_T1_GEN_01`–`08`, `TC_T3_01`–`03` | `style_validator.py` (Genre taxonomy & acoustic descriptors) |
| **F12** | Authentic Vocal Timbre & White Voice Directives | Tier 1, Tier 3 | `TC_T1_VOC_01`–`05`, `TC_T3_02` | `style_validator.py` (Vocal timbre token enforcement) |
| **F13** | Acoustic Anti-Artifact Negative Prompting | Tier 1 | `TC_T1_NEG_01`–`05` | `style_validator.py` (Exclude acoustic vector verification) |
| **F14** | Prompt Packs Modernization & Overhaul | Tier 1, Tier 3 | `TC_T1_GEN_01`–`08`, `TC_T3_01` | `style_validator.py` (Pack style compliance) |
| **F15** | Cross-Skill Synchronization & Deduplication | Tier 3 | `TC_T3_01` (Full Pipeline) | Multi-module harness |
| **F16** | Enhanced 100-Point Poetic & Suno Rubrics | All Tiers | All Test Suites | `rubric_scorer.py` (Algorithmic & heuristic scoring) |
| **F17** | 4-Tier E2E Test Suite Infrastructure | All Tiers | `tests/run_tests.py` | Complete test framework & CLI runner |
| **F18** | Final E2E Suite Verification & Adversarial Pass | All Tiers + Adversarial | `tests/run_tests.py --all` | Test runner suite gatekeeper (100% Pass) |

---

## 4. 4-Tier Test Suite Architecture

```
========================================================================================
                              4-TIER E2E TEST SUITE
========================================================================================

  TIER 1: FEATURE COVERAGE (Unit & Component Level — >=5 Tests per Area)
  ├── 1.1 Versification Meters (Iamb, Trochee, Dactyl, Amphibrach, Anapest) [5 tests]
  ├── 1.2 Non-Syllabo-Tonic Verse (Dolnik 3/4-stress, Taktovik, Kolomyika, Free Verse) [5 tests]
  ├── 1.3 Fixed Poetic Forms (Sonnet, Shakespearean Sonnet, Rondo, Triolet, Terza Rima) [5 tests]
  ├── 1.4 Authentic Registers (Urban, Intimate, Neoclassical, Baroque, Folk, Children) [6 tests]
  ├── 1.5 Suno Music Taxonomy (8 Modern Ukrainian Genres) [8 tests]
  ├── 1.6 Vocal Timbres & Performance Directives [5 tests]
  └── 1.7 Acoustic Negative Prompting & Anti-Artifact Vectors [5 tests]

  TIER 2: BOUNDARY & CORNER CASES (Extreme Stress & Constraints)
  ├── TC_T2_01: Six-Word Taboo Pressure (No душа, серце, доля, вічність, життя, кохання)
  ├── TC_T2_02: Strict 3-Foot Dactyl with Feminine/Masculine Alternation
  ├── TC_T2_03: Strict 3-Foot Anapest with Consistent Cadence
  ├── TC_T2_04: 14-Syllable Kolomyika with Mandatory 4+4+6 Caesura
  ├── TC_T2_05: Strict <=120 Character Multi-Instrument Style Box Compression
  ├── TC_T2_06: Extreme Tempo Contrast Handling (60 BPM Drone vs 180 BPM Metalcore)
  ├── TC_T2_07: Stress Homograph Disambiguation (зАмок/замОк, мукА/мУка, дорогА/дорОга)
  └── TC_T2_08: Conflicting Multi-Constraint Resolution (Whispered Lullaby Metalcore)

  TIER 3: CROSS-FEATURE COMBINATIONS (Pairwise & Multi-Skill Pipeline)
  ├── TC_T3_01: Full Pipeline E2E (Brief -> Dolnik Lyrics -> Metatags -> Suno Prompt -> Validation)
  ├── TC_T3_02: Folk Carpathian Lyrics + Cyber Dark Synthwave Production
  ├── TC_T3_03: Cossack Baroque Register + Modern Melodic Metalcore
  ├── TC_T3_04: Chamber Intimate Whisper + Neoclassical Bandura & Cello
  ├── TC_T3_05: Bilingual UA/EN Radio Pop-Rock Crossover Hook
  └── TC_T3_06: Multi-Stage Dynamics (Acoustic Bandura Verse -> Massive Electronic Trap Drop)

  TIER 4: REAL-WORLD APPLICATION SCENARIOS (Production Release Briefs)
  ├── TC_T4_01: Commercial Radio Single / Viral Folk-Pop Track
  ├── TC_T4_02: Cinematic Film / Game Soundtrack (Dark Ambient Spoken-Word)
  ├── TC_T4_03: Children's Animated Series Nature Song
  ├── TC_T4_04: Modern Melodic Metalcore Existential Anthem
  ├── TC_T4_05: Intimate Lo-Fi Spoken-Word Poetry Track
  └── TC_T4_06: Neoclassical Symphonic Bandura Ballad
========================================================================================
```

---

## 5. Automated / Deterministic Validation Harness

The validation harness is located in `tests/` and comprises dedicated Python validation engines with zero external runtime dependencies.

### 5.1 Style Validator (`tests/validator/style_validator.py`)
Validates Suno AI `Style of Music` prompts and `Exclude` negative vectors:
- **Character Budget Rule**:
  - `Style of Music` length <= 180 characters (Flagged ERROR if >180 chars).
  - Compact Mode `Style of Music` length <= 120 characters.
  - Optimal range: 80–150 characters (Warning if <40 characters).
- **Metadata Leakage Prevention**:
  - Rejects prompts containing text labels: `Language:`, `Theme:`, `Topic:`, `Story:`, `BPM:`, `Title:`, `Lyrics:`.
- **Anti-Infringement & Reference De-Identification**:
  - Prohibits direct artist/band names (e.g. `Okean Elzy`, `DakhaBrakha`, `Go_A`, `Kalush`, `Hardkiss`, `Onuka`, `Antytila`, `Boombox`, etc.).
  - Prohibits copyright-triggering phrases (`in the style of`, `sounds like`, `cover of`).
- **Exclude Vector Concreteness**:
  - Verifies that `Exclude` fields contain specific acoustic/genre tokens (e.g. `heavy distortion, brass, acoustic guitar`) rather than vague emotional words (`sadness, bad vibes`).

### 5.2 Metatag & Song Structure Validator (`tests/validator/metatag_validator.py`)
Validates Suno Custom Mode lyrical arrangement and section tags:
- **Bracket Metatag Compliance**:
  - All structural headers must follow bracketed syntax: `[Intro]`, `[Verse]`, `[Verse 1]`, `[Verse 2]`, `[Pre-Chorus]`, `[Chorus]`, `[Bridge]`, `[Drop]`, `[Instrumental Break]`, `[Guitar Solo]`, `[Spoken Word]`, `[Whisper]`, `[Outro]`, `[Hook]`, `[Fade Out]`, `[End]`.
  - Canonical Ukrainian translations permitted: `[Інтро]`, `[Куплет]`, `[Куплет 1]`, `[Передприспів]`, `[Приспів]`, `[Бридж]`, `[Дроп]`, `[Соло]`, `[Аутро]`.
- **Anti-Prose / Anti-Hallucination Guardrail**:
  - Rejects prose descriptions inside brackets (e.g. `[Slow acoustic guitar that weeps softly]` is rejected; must be `[Acoustic Guitar Solo]`).
- **Backing Vocal Syntax**:
  - Parentheses reserved exclusively for backing vocals, echoes, harmonies, or ad-libs: `(луна)`, `(бек-вокал)`, `(harmony)`, `(oh-oh)`.

### 5.3 Poetic & Linguistic Validator (`tests/validator/poetic_validator.py`)
Performs deterministic scansion, clausula analysis, linguistic hygiene, and rhyme verification:
- **Syllable Counting Engine**: Accurate count of Ukrainian vowels (`а, е, є, и, і, ї, о, у, ю, я`).
- **Clausula Cadence Classifier**:
  - Masculine (`Ч` / `M`): Stress on the last syllable (`...води́`).
  - Feminine (`Ж` / `F`): Stress on the penultimate syllable (`...до́му`).
  - Dactylic (`Д` / `D`): Stress on the 3rd syllable from the end (`...не́бокрай`).
  - Validates alternating patterns (e.g. `ЖЧЖЧ` / `FMFM`, `ЖЖЧЖЖЧ`).
- **Rhythm & Metrical Scansion**:
  - Binary meters: Iamb (`U —`), Trochee (`— U`).
  - Ternary meters: Dactyl (`— U U`), Amphibrach (`U — U`), Anapest (`U U —`).
  - Non-syllabo-tonic: Dolnik inter-ictic interval calculation (1–3 unstressed syllables between accents); Kolomyika 14-syllable `4 + 4 + 6` format with required caesura.
- **Banned Russianisms & Surzhyk Filter**:
  - Scans for banned tokens with automatic correction mapping:
    - `самий кращий` -> `найкращий`
    - `більше чим` -> `більше ніж / за`
    - `в кінці кінців` -> `зрештою / кінець кінцем`
    - `приймати участь` -> `брати участь`
    - `получається` -> `виходить`
    - `слідуючий` -> `наступний`
    - `являється` -> `є`
    - `на протязі` -> `протягом`
    - `вірніше` -> `точніше`
- **Anti-Sharovarshchyna Filter**:
  - Flags unprompted insertion of ethnographic kitsch (`шаровари`, `горілка`, `сало`, `шароварщина`, `кунтуш`) in modern/urban/intimate contexts.
- **Taboo Lexicon Filter**:
  - Enforces negative word constraints (e.g. forbidding `душа`, `серце`, `доля`, `вічність`, `життя`, `кохання` when explicitly requested).
- **Rhyme Classification Engine**:
  - Flags cheap grammatical rhymes (verb-verb pairs like `робити-любити`, `палає-страждає`; identical adjective case endings).
  - Rewards heterogeneous cross-grammatical and acoustic/slant rhymes.
- **Stress Homograph Disambiguation**:
  - Verifies correct stress markings for homographs (`зАмок` = fortress vs `замОк` = lock; `обід` = lunch vs `обі́д` = wheel rim; `мукА` = flour vs `мУка` = agony).

### 5.4 100-Point Rubric Scorer (`tests/validator/rubric_scorer.py`)
Computes algorithmic and heuristic scores across the official 100-point rubrics with granular deductions.

---

## 6. 100-Point Scoring Rubrics

### 6.1 Ukrainian Poetry 100-Point Rubric

| Dimension | Points | Description | Penalty Triggers |
|---|---|---|---|
| **1. Linguistic Naturalness & Idiomatic Ukrainian** | 25 pts | Native phrasing, idiomatic syntax, correct prepositional rection. | Surzhyk / Russianism (-10 pts per violation); Syntactic calque (-5 pts); Unnatural word order (-3 pts). |
| **2. Imagery & Concreteness** | 20 pts | Tactile, sensory, physical details; absence of abstract padding. | Vague abstract filler (-5 pts); Greeting-card cliches (-5 pts). |
| **3. Rhythm & Metrical Integrity** | 15 pts | Stable cadence, meaningful line breaks, oral musicality. | Syllable count mismatch in strict meter (-5 pts); Metrical drift (-4 pts); Awkward oral cadence (-3 pts). |
| **4. Rhyme & Sound Design** | 10 pts | Heterogeneous rhymes, acoustic richness, non-grammatical pairs. | Cheap verb-verb rhyme (-3 pts per pair); Identical suffix rhyme (-2 pts); Forced syntactic inversion (-3 pts). |
| **5. Tonal Integrity & Register** | 10 pts | Stable register matching the chosen mode. | Accidental comical or pathetic slip (-4 pts); Register inconsistency (-3 pts). |
| **6. Ending Strength & Closure** | 10 pts | Resonant, open, image-led finale without preaching. | Moralizing conclusion / didactics (-6 pts); Clichéd wrap-up line (-4 pts). |
| **7. Anti-Cliche & Guardrails** | 10 pts | Absence of banned words and unprompted kitsch. | Violation of negative word ban (-10 pts); Unprompted sharovarshchyna (-5 pts). |
| **TOTAL** | **100 pts** | Minimum Acceptance Threshold: **85 pts** |

### 6.2 Suno Style Prompt 100-Point Rubric

| Dimension | Points | Description | Penalty Triggers |
|---|---|---|---|
| **1. Musical Concreteness & Genre Identity** | 20 pts | Specific subgenre, clear sonic markers, concrete instrumentation. | Vague descriptors ("good music", "epic song") (-10 pts); Missing key instruments (-5 pts). |
| **2. Token Economy & Character Budget** | 15 pts | High signal-to-noise ratio, length <= 180 chars (optimal 80-150). | Length > 180 chars (-15 pts); Token bloat / conversational padding (-5 pts). |
| **3. Reference De-Identification & Safety** | 20 pts | 100% deconstructed acoustic traits; zero copyright triggers. | Leaked artist / band name (-20 pts); "in the style of" phrasing (-15 pts). |
| **4. Structural Metatag Compliance** | 10 pts | Standard bracketed tags `[Verse]`, `[Chorus]`, parenthetical backing. | Prose inside brackets (-5 pts); Invalid / unparseable tags (-4 pts). |
| **5. Style Field Purity (No Metadata Leak)** | 10 pts | Style box contains ONLY acoustic directives; zero lyrics/themes. | `Language:`, `Theme:`, `Story:` in Style box (-10 pts); Plot summary in Style (-6 pts). |
| **6. Ukrainian Acoustic Authenticity** | 10 pts | Modern Ukrainian sonic markers without tourist kitsch. | Unprompted polka / tourist accordion in modern pop (-5 pts); Missing vocal timbre (-3 pts). |
| **7. Exclude Field Precision** | 10 pts | Specific negative acoustic instruments/genres. | Vague emotional negatives ("sadness, bad vibes") (-6 pts); Empty Exclude when needed (-3 pts). |
| **8. Custom Mode Tripartite Split** | 5 pts | Flawless separation of `Lyrics`, `Style of music`, and `Exclude`. | Missing Custom Mode block separation (-5 pts). |
| **TOTAL** | **100 pts** | Minimum Acceptance Threshold: **88 pts** |

---

## 7. Test Execution & Reporting Protocol

### 7.1 Running Tests via CLI

```powershell
# Run the complete test suite across all 4 tiers
py -3 tests/run_tests.py --all

# Run a specific tier
py -3 tests/run_tests.py --tier 1
py -3 tests/run_tests.py --tier 2
py -3 tests/run_tests.py --tier 3
py -3 tests/run_tests.py --tier 4

# Run a single targeted test case
py -3 tests/run_tests.py --test TC_T2_01_Taboo_6Words_Ban

# Generate structured JSON report
py -3 tests/run_tests.py --all --json --report-file tests/reports/test_report.json

# Using PowerShell wrapper
.\tests\run_tests.ps1 -Tier All
```

### 7.2 Pass/Fail Criteria & Quality Gate
- **100% Deterministic Pass Rate**: Zero hard assertion failures across all Tiers 1–4.
- **Rubric Score Threshold**: Every test case must achieve >= 85/100 on Poetic Rubric and >= 88/100 on Suno Style Rubric.
- **Backward Compatibility**: All existing baseline tests in `skills/ukrainian-poetry/references/tests.md`, `skills/ukrainian-poetry/references/stress-tests.md`, and `skills/ukrainian-poetry-to-suno/references/tests.md` must pass with zero regressions.

---

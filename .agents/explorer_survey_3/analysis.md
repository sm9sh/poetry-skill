# Comprehensive Audit & Feature Exploration: Edge Cases, Test Suites, Repository Architecture & E2E Validation Framework

**Author**: Explorer 3 (Edge Case, Stress-Test & Test Infra Specialization)  
**Date**: 2026-08-26  
**Scope**: Full repository audit across `d:/poetry-skill`, evaluating all existing test suites, edge cases, failure modes, layout redundancy, and validation mechanisms for Ukrainian poetry and Suno AI music skills.

---

## 1. Executive Summary & Scope Overview

This audit investigates the repository structure, test infrastructure, edge case coverage, and architectural failure modes across both the `ukrainian-poetry` and `ukrainian-poetry-to-suno` skills.

### Key Audit Findings
1. **Pervasive Layout Redundancy**: 22 files in the project root are exact duplicates (verified by byte-for-byte MD5 hash) of files located inside `skills/ukrainian-poetry/references/`, `skills/ukrainian-poetry-to-suno/references/`, and `skills/ukrainian-poetry-to-suno/references/packs/`. This creates an acute risk of desynchronization during upgrades.
2. **Test Suite Coverage Gaps**: Existing test suites (`ukrainian-poetry-skill-tests.md`, `ukrainian-poetry-skill-stress-pack.md`, `suno-prompt-tests.md`) provide good baseline checks for simple lyric forms and standard prompt generation, but completely lack coverage for:
   - Complex syllabo-tonic meters (dactyl, anapest, trochee with caesura, logaoedics, classical sonnet/terza rima forms).
   - Accentual verse and dolnik (vital for modern rock, hip-hop, and spoken-word lyrics).
   - Multilingual/code-switching lyrics (UA/EN bilingual hooks, dialectal textures).
   - Multi-stage dynamic song structures (acoustic-to-electronic drops, tempo accelerandos, spoken-word interludes).
   - Strict Suno character/token cap limits (120-char Style box vs 1000-char extended field).
   - Conflicting multi-constraint resolution.
3. **Identified Failure Modes**: Cataloged 14 distinct failure modes (7 Poetic/Linguistic: FM-P1 to FM-P7; 7 Suno/Musical: FM-S1 to FM-S7) where current instructions fail to prevent hallucinated stresses, grammatical rhyme spam, topic leakage into style boxes, metatag misinterpretation, or caricatured folk stylization.
4. **Architectural Solution**: Designed a formal 4-Tier End-to-End (E2E) Testing Framework, deterministic sanity checking suite, LLM-as-a-Judge scoring rubric, and a backward compatibility baseline to guarantee zero regressions.

---

## 2. Repository Structure & File Redundancy Audit

### 2.1 File Inventory & MD5 Duplication Matrix

An exhaustive cryptographic audit of the repository (`Get-FileHash -Algorithm MD5`) revealed 22 exact duplicate pairs between the root directory and the modular `skills/` directories.

| # | Root File Path | Canonical Target Path in `skills/` | MD5 Hash | Status |
|---|---|---|---|---|
| 1 | `packs/dark-pack.md` | `skills/ukrainian-poetry-to-suno/references/packs/dark-pack.md` | `6ADB99E36BAA709323DDA09F9F8327CB` | 100% Duplicate |
| 2 | `packs/female-vocal-pack.md` | `skills/ukrainian-poetry-to-suno/references/packs/female-vocal-pack.md` | `67FE5A065D9D88B6128635912DAC49B7` | 100% Duplicate |
| 3 | `packs/male-vocal-pack.md` | `skills/ukrainian-poetry-to-suno/references/packs/male-vocal-pack.md` | `7662BA92AEA3BA2C1EE23679CCB6BCE2` | 100% Duplicate |
| 4 | `packs/README.md` | `skills/ukrainian-poetry-to-suno/references/packs/README.md` | `646311306B62BF19FB8C5DEE0D1EA7B9` | 100% Duplicate |
| 5 | `packs/sad-pack.md` | `skills/ukrainian-poetry-to-suno/references/packs/sad-pack.md` | `FA8F23F2A1C257B2C19E3CCBA334FF5E` | 100% Duplicate |
| 6 | `packs/suno-reference-prompt-pack-uk.md` | `skills/ukrainian-poetry-to-suno/references/packs/suno-reference-prompt-pack-uk.md` | `493CC66329DFDFC2112E54B46E1E597D` | 100% Duplicate |
| 7 | `packs/suno-reference-prompt-pack.md` | `skills/ukrainian-poetry-to-suno/references/packs/suno-reference-prompt-pack.md` | `0625A8B8D9C29149ADDDE688BE044C09` | 100% Duplicate |
| 8 | `packs/uplifting-pack.md` | `skills/ukrainian-poetry-to-suno/references/packs/uplifting-pack.md` | `849AA710D837DAE688B430D8FC41DAD3` | 100% Duplicate |
| 9 | `lyrics-to-suno-template.md` | `skills/ukrainian-poetry-to-suno/references/lyrics-to-suno-template.md` | `3ABB529A22458DCC8E583742C59B5AB3` | 100% Duplicate |
| 10 | `mood-to-style-map.md` | `skills/ukrainian-poetry-to-suno/references/mood-to-style-map.md` | `BF7120F8236D4D04789713941E93B969` | 100% Duplicate |
| 11 | `prompt-builder.md` | `skills/ukrainian-poetry-to-suno/references/prompt-builder.md` | `FD0EC2AC87F31521F81D330D030D3F7D` | 100% Duplicate |
| 12 | `reference-breakdown-examples.md` | `skills/ukrainian-poetry-to-suno/references/reference-breakdown-examples.md` | `01D6A4B09BBE583429E8CE84C566130E` | 100% Duplicate |
| 13 | `reference-to-style-cheatsheet.md` | `skills/ukrainian-poetry-to-suno/references/reference-to-style-cheatsheet.md` | `26EDB905EA2C07763502F866DAF9ED90` | 100% Duplicate |
| 14 | `song-structure-pack.md` | `skills/ukrainian-poetry-to-suno/references/song-structure-pack.md` | `86AFFD4125C2015D670C6D6044EFC3F7` | 100% Duplicate |
| 15 | `suno-prompt-anti-patterns.md` | `skills/ukrainian-poetry-to-suno/references/suno-prompt-anti-patterns.md` | `55BD882D9BD44CA65E927CAC808416EF` | 100% Duplicate |
| 16 | `suno-prompt-tests.md` | `skills/ukrainian-poetry-to-suno/references/tests.md` | `0558D8E84AD31D1E57BC10BBFBC4A65D` | 100% Duplicate |
| 17 | `suno-style-rubric.md` | `skills/ukrainian-poetry-to-suno/references/rubric.md` | `DE373842B410E9E3D0247BE89E745ECA` | 100% Duplicate |
| 18 | `ukrainian-song-scenarios.md` | `skills/ukrainian-poetry-to-suno/references/ukrainian-song-scenarios.md` | `AA9C89E7805925E478199DDB9D4AF5F3` | 100% Duplicate |
| 19 | `ukrainian-poetry-skill-input-template.md` | `skills/ukrainian-poetry/references/input-templates.md` | `4B604B25B69EA83F78887A56CFCE1872` | 100% Duplicate |
| 20 | `ukrainian-poetry-skill-rubric.md` | `skills/ukrainian-poetry/references/rubric.md` | `637F1556A81A423ADB5AD9D13CAEFA50` | 100% Duplicate |
| 21 | `ukrainian-poetry-skill-stress-pack.md` | `skills/ukrainian-poetry/references/stress-tests.md` | `3B36E7E6EA1DB49FCE3236FD93F853BD` | 100% Duplicate |
| 22 | `ukrainian-poetry-skill-tests.md` | `skills/ukrainian-poetry/references/tests.md` | `A079A2488B966217DE2FCF578EF6CDDC` | 100% Duplicate |

### 2.2 Divergent Legacy Files & Inconsistencies

Beyond exact duplicates, several legacy variants exist across root, `skills/`, and `source/`:
- **Ukrainian Poetry Full Guides**:
  - `skills/ukrainian-poetry/references/full-guide.md` (24,607 bytes, 509 lines) contains the Ukrainian full guide including prompt templates.
  - `ukrainian-poetry-skill-uk.md` (20,927 bytes, 433 lines) in root omits the prompt templates section.
  - `source/legacy-skills/ukrainian-poetry.md` (25,090 bytes, 514 lines) has a YAML header and slight differences.
  - `ukrainian-poetry-skill.md` in root (12,906 bytes) is an English version of the guide.
  - `ukrainian-poetry-skill-lite.md` in root (3,028 bytes) is a truncated prompt template.
- **Suno Full Guides**:
  - `skills/ukrainian-poetry-to-suno/references/full-guide.md` (14,072 bytes) vs `ukrainian-poetry-to-suno.md` in root (14,072 bytes) vs `source/legacy-skills/ukrainian-poetry-to-suno.md` (14,147 bytes with YAML header).

### 2.3 Synchronization Risks & Canonical Architecture Recommendation
- **Risk**: Editing a file in `skills/.../references/` without updating the root copy (or vice versa) results in prompt drift, contradictory instructions, and broken tests.
- **Canonical Standard**:
  - The single source of truth MUST be the modular skill directories:
    - `skills/ukrainian-poetry/SKILL.md` and `skills/ukrainian-poetry/references/*`
    - `skills/ukrainian-poetry-to-suno/SKILL.md` and `skills/ukrainian-poetry-to-suno/references/*`
  - The root directory should contain only standard repository metadata (`README.md`, `README.en.md`, `HOWTO.md`, `INSTALL.md`, `VERSION.md`, `PROJECT.md`, `TEST_INFRA.md`). Root reference duplicates should either be soft links, unified documentation exports, or cleaned up to prevent drift.

---

## 3. Existing Test Suite Audit & Deep Gap Analysis

### 3.1 Inventory of Current Test Suites

| Suite Name | File Location | Test Count | Focus Area |
|---|---|---|---|
| **Ukrainian Poetry Tests** | `skills/ukrainian-poetry/references/tests.md` | 21 tests | Base lyrical, free-verse, rhyme, children, patriotic, tone, iamb, amphibrach, anti-cliches, editing. |
| **Ukrainian Poetry Stress Pack** | `skills/ukrainian-poetry/references/stress-tests.md` | 15 tests | Negative vocabulary bans, strict stanza counts, minimalism, weak text repair, prose compression. |
| **Suno Prompt Tests** | `skills/ukrainian-poetry-to-suno/references/tests.md` | 16 tests | Topic->Prompt, Lyrics->Prompt, Reference de-identification, Custom Mode split, Glossary usage, Exclude precision. |

### 3.2 Detailed Gap Analysis

While the existing tests establish basic sanity, they fail to stress the skills against real-world production demands. The table below details the 8 primary coverage gaps:

```
+---------------------------------------------------------------------------------------------------+
|                                  CRITICAL TEST SUITE COVERAGE GAPS                                |
+------------------------------------+--------------------------------------------------------------+
| 1. Complex & Rare Metrical Forms   | No tests for Dactyl, Anapest, Trochee with caesura, Logaoedic|
|                                    | verse, Sonnet, Terza Rima, Triolet, Octave, or Ballad meter. |
+------------------------------------+--------------------------------------------------------------+
| 2. Accentual Verse & Dolnik        | No tests for stress-count verse (2-4 stresses, 1-3 unstressed|
|                                    | intervals), vital for modern rock, rap, and spoken word.     |
+------------------------------------+--------------------------------------------------------------+
| 3. Multilingual & Code-Switching   | No tests for Ukrainian-English bilingual radio hooks, Latin  |
|                                    | phrases, or regional dialectal phonetics.                    |
+------------------------------------+--------------------------------------------------------------+
| 4. Complex Rhyme Topologies        | No tests for internal rhymes, assonance/dissonance chains,    |
|                                    | hyper-dactylic rhymes, or tautological/homonymic rhymes.     |
+------------------------------------+--------------------------------------------------------------+
| 5. Multi-Phase Structural Shifts   | No tests for dynamic song shifts (Acoustic -> Electronic     |
|                                    | Drop, Half-Time -> Double-Time, Tempo Accelerando).          |
+------------------------------------+--------------------------------------------------------------+
| 6. Dynamic Vocal Mode Transitions  | No tests for multi-vocal switching ([Spoken Word] verse into |
|                                    | [Belted Chorus] into [Polyphonic Chant Outro]).             |
+------------------------------------+--------------------------------------------------------------+
| 7. Suno Token/Character Economy    | No tests verifying strict <=120 char Style Box limit or tag  |
|                                    | priority weighting under character cap truncation.           |
+------------------------------------+--------------------------------------------------------------+
| 8. Conflicting Constraint Handling | No tests evaluating resolution of polarizing inputs (e.g.    |
|                                    | "intimate acoustic whispering death metal anthem").          |
+------------------------------------+--------------------------------------------------------------+
```

---

## 4. Edge Case Taxonomy & Failure Modes Catalog

The audit identified 14 recurring failure modes where current skill instructions and prompt construction yield degraded, hallucinated, or unmusical outputs.

### 4.1 Linguistic & Poetic Failure Modes (FM-P1 to FM-P7)

#### FM-P1: Lexical Stress Distortion / Accentuation Distortion (`Переакцентуація`)
- **Description**: The LLM arbitrarily shifts natural Ukrainian word stress to satisfy a rigid syllabo-tonic foot or rhyme scheme.
- **Example / Violation**: Stressing `ві́кна` as `вікна́`, `ро́блю` as `роблю́`, `було́` as `бу́ло`, `твоє́го` as `твого́`, `руки́` as `ру́ки`.
- **Root Cause**: LLMs generate text token-by-token without an explicit phonological/stress-dictionary verification step.
- **Impact**: Destroys oral authenticity; unlistenable when sung or recited.
- **Mitigation / Guardrail**: Instruct skill to prioritize natural Ukrainian stress above metrical rigidity ("if meter conflicts with stress, weaken the meter, not the accentuation").

#### FM-P2: Grammatical / Cheap Rhyme Proliferation (`Дієслівно-граматичний спам`)
- **Description**: Over-reliance on identical parts of speech and inflectional suffixes to form rhymes.
- **Example / Violation**: Verb-verb pairs (`робити-любити`, `страждає-палає`, `чекати-знати`), noun-case pairs (`ночі-очі`, `житті-бутті`, `руками-сльозами`).
- **Root Cause**: Inability to explore cross-categorical (noun + verb, adjective + adverb) acoustic affinities without explicit constraints.
- **Impact**: Amateurish, sing-song greeting-card tone.
- **Mitigation / Guardrail**: Add explicit negative rule against same-grammatical-ending rhyming; enforce acoustic/imperfect/slant rhymes.

#### FM-P3: Pseudo-Folk Tropes & Unprompted Sharovarshchyna (`Шароварщина`)
- **Description**: Automatic injection of folk trinkets into contemporary, urban, or intimate poems.
- **Example / Violation**: Inserting `калина`, `сопілка`, `козак`, `вишиванка`, `віночок`, `гай` into a modern electronic or urban metro poem.
- **Root Cause**: Training bias associating the token "Ukrainian" with 19th-century ethnographic cliches.
- **Impact**: Tonal dissonance, superficial kitsch.
- **Mitigation / Guardrail**: Strict guardrail banning unprompted ethnographic tropes unless explicitly requested in `folk` mode.

#### FM-P4: Abstract Sloganizing & Patriotic Pathos (`Абстрактно-лозунговий пафос`)
- **Description**: Reverting to rhetorical shouting, heroic cliches, and propaganda phrases in patriotic/memorial requests.
- **Example / Violation**: `Ми переможемо ворогів`, `Герої не вмирають ніколи`, `Свята земля за нас стоїть`.
- **Root Cause**: High frequency of slogans in web text related to Ukrainian defense.
- **Impact**: Devalues genuine emotional gravity; sounds like an official press release rather than moving poetry.
- **Mitigation / Guardrail**: Ground dignity in land, daily labor, tactile objects (bread, clay, silent window, tools), and human endurance without capital-letter abstractions.

#### FM-P5: Syntactic Calques & Translation Artifacts (`Кальки та чужорідний синтаксис`)
- **Description**: Syntactic structures borrowed from Russian or English that violate Ukrainian idioms.
- **Example / Violation**: `більше чим` (instead of `більше за / ніж`), `самий кращий` (instead of `найкращий`), `я є тим хто` (calque of "I am the one who").
- **Root Cause**: Multilingual cross-lingual representation interference in neural weights.
- **Impact**: Destroys natural syntactic flow and native musicality.
- **Mitigation / Guardrail**: Enforce native Ukrainian prepositional rection, synthetic comparatives, and verbal aspect discipline.

#### FM-P6: Moralizing / Explanatory Finales (`Повчальний фінал`)
- **Description**: Concluding a poem with an explicit moral, thesis, or summary lesson.
- **Example / Violation**: `І я збагнув у цей момент святий, що треба просто жити й вірити...`
- **Root Cause**: RLHF instruction-following models naturally gravitate toward summarizing conclusions.
- **Impact**: Ruptures the aesthetic experience; leaves a patronizing aftertaste.
- **Mitigation / Guardrail**: Require ending on an open sensory image, lingering physical detail, or unanswered gesture.

#### FM-P7: Metrical Entropy & Syllabo-Tonic Drift (`Метрична ентропія`)
- **Description**: A poem starts in a strict 4-foot iamb and unexpectedly degrades into 3-foot anapest or irregular free prose in stanza 3.
- **Root Cause**: Attention degradation across long generation sequences without foot-by-foot schema reinforcement.
- **Impact**: Rhythmic breakdown; impossible for a musician or AI model to establish a steady groove.
- **Mitigation / Guardrail**: Explicit syllable counting and caesura notation per line in formal modes.

---

### 4.2 Suno Musical Failure Modes (FM-S1 to FM-S7)

#### FM-S1: Style Field Tag Truncation & Token Bloat (`Обрізання тегів через ліміт`)
- **Description**: Generating overlong prose descriptions in Suno's `Style of Music` field (>120-150 characters), causing Suno to silently truncate critical production tokens at the end.
- **Example / Violation**: `Style of music: A beautiful emotional Ukrainian indie pop song with subtle acoustic guitar, warm analog synthesizer pads, intimate breathy female vocals, pulsing modern bassline, crisp drums, and a slow emotional build into a wide anthemic chorus` (248 chars -> truncated by Suno v3/v4).
- **Impact**: Vital tags (`wide anthemic chorus`, `crisp drums`) are lost; Suno generates generic filler.
- **Mitigation / Guardrail**: Enforce strict `<120 character` Short Style Box format prioritizing: `[Genre], [Mood/Energy], [Vocal], [2 Key Instruments], [Production]`.

#### FM-S2: Lyrical / Topic Leakage into Style Field (`Витік сюжету/лірики в поле Style`)
- **Description**: Injecting narrative plot points or lyric themes into the music style box.
- **Example / Violation**: `Style of music: Ukrainian song about waiting for someone in the rain at a tram stop with hot coffee`
- **Impact**: Suno's audio model interprets narrative English/Ukrainian words as acoustic tokens, resulting in distorted voices, sound effects of rain overpowering vocals, or garbled output.
- **Mitigation / Guardrail**: Strict separation of concerns: Plot/Topic belongs exclusively in `Lyrics` / song brief; `Style of music` must contain ONLY genre, tempo, instruments, vocal timbre, and production directives.

#### FM-S3: Direct Reference Infringement / Hallucination (`Прямі згадки артистів / 'in the style of'`)
- **Description**: Outputting style prompts containing actual band/artist names or phrases like `in the style of Okean Elzy` or `like DakhaBrakha`.
- **Impact**: Triggers Suno's automated copyright/safety moderation filter, causing generation rejection or severe audio watermarking.
- **Mitigation / Guardrail**: Deconstruct every reference into pure acoustic traits (`warm baritone vocal, ringing overdriven guitar chords, driving 6/8 pop-rock groove, organic Hammond organ lift`).

#### FM-S4: Exclude Field Ineffectiveness / Vague Negatives (`Неефективний Exclude`)
- **Description**: Populating `Exclude` with abstract emotional labels instead of concrete acoustic instruments/genres.
- **Example / Violation**: `Exclude: sadness, bad vibes, boring music, darkness` (Does nothing in Suno's latent space).
- **Impact**: Zero filtering effect; Suno generates unwanted brass, distortion, or synthetic drops anyway.
- **Mitigation / Guardrail**: `Exclude` must contain specific acoustic tokens: `heavy distortion, brass section, trap hi-hats, autotune, edm drop, acoustic guitar`.

#### FM-S5: Metatag Hallucination & Syntactic Misplacement (`Некоректні метатеги`)
- **Description**: Using descriptive prose inside brackets (`[Slow guitar solo with emotional weeping sound]`) or embedding vocal directives inside lyric lines (`(she whispers quietly) Тиша в кімнаті`).
- **Impact**: Suno sings the descriptive text as literal lyrics instead of playing an instrument or changing vocal style.
- **Mitigation / Guardrail**: Enforce recognized standard metatags: `[Verse]`, `[Pre-Chorus]`, `[Chorus]`, `[Drop]`, `[Instrumental Break]`, `[Guitar Solo]`, `[Bridge]`, `[Outro]`, `[Spoken Word]`, `[Whisper]`.

#### FM-S6: Acoustic-Genre Mismatch & Caricature Folk (`Карикатурний фолк`)
- **Description**: Requesting "Ukrainian electronic pop" and receiving generic accordion polka because prompt specified `Ukrainian folk music`.
- **Impact**: Outdated, cheesy tourist-trap sound design.
- **Mitigation / Guardrail**: Use precise sound engineering descriptors: `modern Ukrainian folk-pop, Carpathian vocal inflections, drone harmony, modal synth bass, dry modern electronic drums`.

#### FM-S7: Vocal Timbre / Language Friction (`Мовно-вокальний конфлікт`)
- **Description**: Suno singing Ukrainian lyrics with an American country twang or robotic autotune due to missing vocal timbre directives.
- **Impact**: Distorted pronunciation, illegible Ukrainian lyrics.
- **Mitigation / Guardrail**: Always specify vocal timbre and language marker: `intimate natural Ukrainian vocal delivery, clear diction, authentic Slavic vocal cadence`.

---

## 5. 4-Tier E2E Testing Framework & Runner Architecture

To validate both skills systematically, we establish an objective 4-Tier Testing Architecture.

```
========================================================================================
                              4-TIER E2E TESTING ARCHITECTURE
========================================================================================
  TIER 1: FEATURE COVERAGE (Core Mechanics & Unit Behaviors)
  - 9 Poetic Modes (Lyrical, Free-verse, Rhymed, Folk, Children, Patriotic, Greeting, Humorous, Reflective)
  - 5 Suno Conversion Workflows (Topic->Prompt, Lyrics->Prompt, Reference->Style, Custom Split, Exclude)
  --------------------------------------------------------------------------------------
  TIER 2: BOUNDARY & CORNER CASES (Stress & Constraint Limits)
  - Length Extremes (2-line Haiku vs 32-line Ballad; 30-char Style Box vs 1000-char Extended)
  - Forbidden Lexicon Pressure (All 6 taboo words banned: душа, серце, доля, вічність, життя, кохання)
  - Rare Meters (Dactyl, Anapest, Trochee 14-syllable Kolomyika, Logaoedics)
  - Extreme Tempo Contrasts (45 BPM Ambient Drone vs 175 BPM Cyber-Folk Drum'n'Bass)
  --------------------------------------------------------------------------------------
  TIER 3: CROSS-FEATURE COMBINATIONS (Multi-Skill Pipeline)
  - Full E2E Chain: Raw Brief -> Ukrainian Poem -> Song Metatags -> Suno Custom Setup -> Quality Check
  - Hybrid Genre + Dual Vocal + Dynamic Transition ([Acoustic Verse] -> [Electronic Cyber-Drop])
  - Bilingual Code-Switching (Ukrainian Verse + English Radio Chorus Hook)
  --------------------------------------------------------------------------------------
  TIER 4: REAL-WORLD APPLICATION SCENARIOS (Production-Grade Releases)
  - Scenario 1: Commercial Radio Single / Viral Folk-Pop Track
  - Scenario 2: Cinematic Film / Game Soundtrack (Dark Ambient Spoken-Word)
  - Scenario 3: Children's Animated Series Theme Song
  - Scenario 4: Dignified Memorial / War Chronicle Anthem
========================================================================================
```

### 5.1 Tier 1: Feature Coverage (Core Mechanics)
- **TC-T1-P01 to P09**: Unit verification of each of the 9 modes in `ukrainian-poetry/SKILL.md` (Lyrical, Free-verse, Rhymed, Folk, Children, Patriotic, Greeting, Humorous, Reflective).
- **TC-T1-S01 to S05**: Unit verification of the 5 Suno conversion workflows (Topic to prompt, Poem/lyrics to prompt, Reference deconstruction, Custom mode tripartite split, Exclude mapping).

### 5.2 Tier 2: Boundary & Corner Cases (Extreme Stress)
- **TC-T2-01 (Six-Word Taboo Pressure)**: Ukrainian love lyric strictly forbidding `душа`, `серце`, `доля`, `вічність`, `життя`, `кохання`.
- **TC-T2-02 (Rare Meter - Strict Dactyl)**: 3 stanzas of pure 3-foot dactyl (`- U U | - U U | - U U`) with feminine/masculine alternating rhymes.
- **TC-T2-03 (Folk Kolomyika Caesura)**: Strict 14-syllable lines structured as `4 + 4 + 6` with mandatory mid-line caesura.
- **TC-T2-04 (Suno 120-Char Style Box Cap)**: Generating a comprehensive multi-instrument style prompt packed into <= 120 characters without losing core sound markers.
- **TC-T2-05 (Extreme Tempo Contrast)**: Transitioning from 50 BPM slow drone into 160 BPM drum'n'bass folk-rock using metatags.
- **TC-T2-06 (Conflicting Multi-Constraint Resolution)**: Request asking for "intimate whisper folk metal anthem with acoustic lullaby drops" — skill must resolve conflict gracefully without adjective bloat.

### 5.3 Tier 3: Cross-Feature Combinations (End-to-End Pipeline)
- **TC-T3-01 (Full Pipeline E2E)**:
  - Input: User brief for a song about late night urban solitude.
  - Step 1 (`ukrainian-poetry`): Produce a 16-line poem in accentual dolnik with vivid sensory imagery and no cliches.
  - Step 2 (`ukrainian-poetry-to-suno`): Structure the poem with standard Suno metatags (`[Verse 1]`, `[Pre-Chorus]`, `[Chorus]`, `[Verse 2]`, `[Bridge]`, `[Chorus]`, `[Outro]`).
  - Step 3 (`ukrainian-poetry-to-suno`): Generate a safe style prompt (<120 chars) and precise Exclude field.
  - Step 4 (Validation Gate): Run deterministic sanity check + 100-point rubric evaluation.
- **TC-T3-02 (Hybrid Sound Design & Dual Vocal)**: Intimate acoustic female verse transitioning into massive electronic male/female duet chorus.
- **TC-T3-03 (Bilingual Code-Switching)**: Ukrainian poetic verses with English crossover radio chorus hook.

### 5.4 Tier 4: Real-World Production Scenarios
- **TC-T4-01 (Viral Commercial Folk-Pop)**: High-energy modern Ukrainian track combining sopilka/bandura hooks with clean pop production, punchy 808s, and singable chorus.
- **TC-T4-02 (Cinematic Soundtrack / Dark Spoken-Word)**: Moody post-rock/dark ambient track featuring spoken-word verse over atmospheric cello/synths, building into a soaring instrumental climax.
- **TC-T4-03 (Children's Educational Song)**: Playful, rhythmic, simple trochaic lyrics about nature with bright acoustic-pop instrumentation and zero didactic condescension.
- **TC-T4-04 (Dignified Memorial Anthem)**: Solemn acoustic-orchestral piece about remembrance, land, and endurance; strictly avoiding slogans, bombast, or propaganda tropes.

---

## 6. Automated Validation & Evaluation Architecture

To ensure objectivity and repeatability, testing combines deterministic static checks with LLM-as-a-Judge rubric scoring.

### 6.1 Deterministic Sanity Checks (Automated Assertions)

```python
# Conceptual Test Runner Architecture
def run_sanity_checks(generated_output, constraints):
    # 1. Banned Vocabulary Check
    for word in constraints.get("banned_words", []):
        assert word.lower() not in generated_output.lower(), f"Violation: Banned word '{word}' found."

    # 2. Reference Leak Check (Anti-Infringement)
    for ref in constraints.get("forbidden_references", []):
        assert ref.lower() not in generated_output["style_of_music"].lower(), f"Leak: Artist '{ref}' leaked into Style box."
    assert "in the style of" not in generated_output["style_of_music"].lower()

    # 3. Token & Character Cap Check
    if "max_style_chars" in constraints:
        assert len(generated_output["style_of_music"]) <= constraints["max_style_chars"], \
            f"Cap Exceeded: Style box is {len(generated_output['style_of_music'])} chars (max {constraints['max_style_chars']})."

    # 4. Custom Mode Structural Split
    if constraints.get("require_custom_mode_split"):
        assert "Lyrics:" in generated_output and "Style of music:" in generated_output
        assert len(generated_output["style_of_music"]) > 0

    # 5. Metatag Syntax Verification
    valid_metatags = ["[Verse", "[Chorus", "[Pre-Chorus", "[Bridge", "[Outro", "[Intro", "[Drop", "[Instrumental"]
    for tag in re.findall(r"\[.*?\]", generated_output.get("lyrics", "")):
        assert any(tag.startswith(v) for v in valid_metatags), f"Invalid metatag syntax: '{tag}'."
```

### 6.2 100-Point Scoring Rubrics

#### Ukrainian Poetry 100-Point Rubric
- **Natural Ukrainian Phrasing (25 pts)**: Idiomatic diction, zero calques, natural word order.
- **Imagery & Concreteness (20 pts)**: Tactile, sensory details; absence of abstract filler.
- **Rhythm & Line Breaks (15 pts)**: Organic cadence, meaningful enjambment, readability aloud.
- **Rhyme & Sound Design (10 pts)**: Audible, fresh, non-grammatical rhymes (or acoustic flow in free verse).
- **Tonal Integrity (10 pts)**: Stable register matching the chosen mode without unintended comedic/solemn shifts.
- **Ending Strength (10 pts)**: Resonant, open, image-led finale with zero didactic moralizing.
- **Anti-Cliche Guardrails (10 pts)**: Zero forbidden words, absence of unprompted sharovarshchyna.

#### Suno Style Prompt 100-Point Rubric
- **Musical Concreteness (20 pts)**: Specific genre, distinct sonic markers, clear acoustic identity.
- **Controllability & Economy (15 pts)**: High signal-to-noise ratio, <120 char style box efficiency, zero token bloat.
- **Safe Reference Abstraction (20 pts)**: Accurate capture of reference vibe with 100% de-identification.
- **Safety & Compliance (10 pts)**: Zero artist/song names, zero "in the style of" phrasing.
- **Style Language Quality (10 pts)**: Clean, professional audio production descriptors.
- **Ukrainian Authenticity (10 pts)**: Contemporary Ukrainian sonic markers without tourist kitsch.
- **Exclude Precision (10 pts)**: Concrete negative instruments/genres rather than vague emotions.
- **Custom Mode Tripartite Split (5 pts)**: Flawless separation of `Lyrics`, `Style of music`, and `Exclude`.

---

## 7. Backward Compatibility Baseline & Regression Protection

To guarantee that future skill improvements introduce zero regressions:

### 7.1 Baseline Acceptance Criteria
1. **Existing Test Suite Regression Threshold**:
   - All 21 standard tests in `ukrainian-poetry/references/tests.md` must achieve a score `>= 85/100` on the updated rubric.
   - All 15 stress tests in `ukrainian-poetry/references/stress-tests.md` must pass with 0 hard negative violations.
   - All 16 Suno prompt tests in `ukrainian-poetry-to-suno/references/tests.md` must generate clean tripartite custom blocks with 0 artist name leaks.
2. **Interface & Parameter Contract Stability**:
   - The input parameter signature (`topic`, `mood`, `audience`, `length`, `mode`, `rhyme`, `meter`, `register`, `image_density`, `ending_strength`) must remain fully supported.
   - Default fallback behavior (short, lyrical, light rhyme, neutral-contemporary) must be preserved when parameters are omitted.
3. **Output Mode Guarantees**:
   - Default output for poetry remains the clean poem text without intrusive commentary unless requested.
   - Default output for Suno conversion remains the `Short prompt` and `Extended prompt` pair, with optional `Custom Mode` blocks.

---

## 8. Prioritized Implementation Roadmap

Based on the audit, the following prioritized execution tasks are recommended for the implementation team:

1. **Repository Layout Cleanup (Priority: High)**:
   - Consolidate all reference files and prompt packs exclusively inside `skills/ukrainian-poetry/references/` and `skills/ukrainian-poetry-to-suno/references/`.
   - Eliminate or synchronize redundant root-level copies to maintain a single source of truth.
2. **Skill Instruction Hardening (Priority: High)**:
   - Upgrade `skills/ukrainian-poetry/SKILL.md` with explicit stress-preservation rules, dolnik/accentual verse guidance, and non-grammatical rhyme mechanics.
   - Upgrade `skills/ukrainian-poetry-to-suno/SKILL.md` with strict <=120 character Style Box constraints, token priority ordering, and standard metatag rules.
3. **Reference File Expansion (Priority: Medium)**:
   - Add dedicated cheatsheets for modern Ukrainian genres (indie pop, dark pop, post-punk, cinematic ambient, trap-folk).
   - Add reference guides for dolnik meters, caesura structures, and stress management.
4. **4-Tier E2E Test Suite Implementation (Priority: High)**:
   - Create `skills/ukrainian-poetry/references/e2e-tests.md` and `skills/ukrainian-poetry-to-suno/references/e2e-tests.md` implementing the 4-tier test architecture.
   - Establish automated sanity check scripts and validation rubrics.

---

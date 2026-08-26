# Project: Ukrainian Poetry & Suno AI Skill System Overhaul

## Architecture
The system consists of two synergistic AI skills and shared reference ecosystems:
1. `ukrainian-poetry`: Poetic and lyric generation adhering strictly to authentic Ukrainian versification (syllabo-tonic, tonic/dolnik/kolomyika, free verse, blank verse), stress/accentuation fidelity, rich heterogeneous rhyming, diverse linguistic registers, and strict anti-sharovarshchyna/anti-calque guardrails.
2. `ukrainian-poetry-to-suno`: Prompt engineering and structural arrangement conversion system translating Ukrainian themes, lyrics, and references into production-grade Suno AI Custom Mode prompts with 80-180 character token efficiency, bracketed metatag syntax, 8 modern Ukrainian music genres, acoustic anti-artifact negative prompting, and vocal timbre directives.
3. Shared Reference & Cheatsheet Layer: Canonical guides, mood-to-style maps, cheatsheets, prompt packs, 100-point evaluation rubrics, and automated/deterministic test suites.

```
                  [User Input / Creative Brief]
                                │
                                ▼
               ┌─────────────────────────────────┐
               │     ukrainian-poetry Skill      │
               │  - Versification & Meter Engine │
               │  - Stress & Mobile Accent Guard │
               │  - Heterogeneous Rhyme System   │
               │  - Anti-Sharovarshchyna Filter  │
               └────────────────┬────────────────┘
                                │ (Structured Lyrics + Prosodic Metatags)
                                ▼
               ┌─────────────────────────────────┐
               │   ukrainian-poetry-to-suno      │
               │  - Token-Optimized Style Box    │
               │  - Section Metatags & Dynamics  │
               │  - 8-Genre Modern UKR Taxonomy  │
               │  - Anti-Artifact Exclude Vector │
               └────────────────┬────────────────┘
                                │
                                ▼
                   [Suno AI Custom Mode Ready]
```

## Feature Inventory
| # | Feature | Description | Milestone | Source | Status |
|---|---------|-------------|-----------|--------|--------|
| F1 | Dactyl & Ternary Meter Integration | Add dactyl (`— U U`) and full ternary meter guidance to SKILL.md and input templates | M1 | Survey R1 | DONE |
| F2 | Non-Syllabo-Tonic Systems (Dolnik, Taktovik, Kolomyika) | Codify operational rules, inter-ictic intervals, and 14-syllable (4+4+6) Kolomyika verse | M1 | Survey R1 | DONE |
| F3 | Blank Verse (Білий вірш) Codification | Codify unrhymed syllabo-tonic verse distinct from free verse (verlibre) | M1 | Survey R1 | DONE |
| F4 | Fixed Poetic Forms (Sonnet, Rondo, Triolet, Terza Rima) | Codify structural rules, stanza division, rhyme schemes, and volta requirements | M1 | Survey R1 | DONE |
| F5 | Clausula Alternation & Line-Ending Cadence | Codify masculine, feminine, dactylic clausulae and alternating schemes (`ЖЧЖЧ`) | M1 | Survey R1 | DONE |
| F6 | Stress & Mobile Accentuation Engine | Catalog mobile stress, dual accents, homographs (зАмок/замОк), and anti-Russian stress blacklist | M1 | Survey R1 | DONE |
| F7 | Heterogeneous Rhyme & Anti-Grammatical Blacklist | Enforce cross-grammatical rhyming; blacklist verb-verb, identical adjective endings, and diminutive suffixes | M1 | Survey R1 | DONE |
| F8 | 6 Authentic Registers & Anti-Sharovarshchyna | Codify Urban, Intimate, Neoclassical, Baroque, Folk, Children registers; strict anti-kitsch filter | M1 | Survey R1 | DONE |
| F9 | Style Prompt Token Economy (80-180 Chars) | Enforce concise English style tags; eliminate metadata pollution (`Language/Theme`) | M2 | Survey R2 | DONE |
| F10 | Bracketed Metatag Syntax & Arrangement | Standardize `[Intro]`, `[Verse]`, `[Chorus]`, `[Drop]`, `[Outro]`, `(backing)` across all templates | M2 | Survey R2 | DONE |
| F11 | 8-Genre Modern Ukrainian Music Taxonomy | Codify Ethno-Chaos, Post-Punk, Dark Synth, Trap-Folk, Metalcore, Shoegaze, Ethno-Rock, Bandura | M2 | Survey R2 | DONE |
| F12 | Authentic Vocal Timbre & White Voice Directives | Codify White Voice (*білий голос*), spoken melodeclamation, extreme vocals, autotune styling | M2 | Survey R2 | DONE |
| F13 | Acoustic Anti-Artifact Negative Prompting | Codify Exclude vectors suppressing metallic treble, muddy bass, garbled audio, and reverb wash | M2 | Survey R2 | DONE |
| F14 | Prompt Packs Modernization & Overhaul | Overhaul all 7 packs (`dark`, `female`, `male`, `sad`, `uplifting`, `uk-ref`, `ref-pack`) | M2 | Survey R2 | DONE |
| F15 | Cross-Skill Synchronization & Deduplication | Align root reference files and `skills/.../references/` canonical sources without divergence | M3 | Survey R3 | DONE |
| F16 | Enhanced 100-Point Poetic & Suno Rubrics | Add explicit deductions for meter breakage, stress errors, sharovarshchyna, and token truncation | M3 | Survey R1/R2/R3 | DONE |
| F17 | 4-Tier E2E Test Suite Infrastructure | Comprehensive test suite covering Tiers 1-4 with validation runner and scoring rubrics | E2E Track | Survey R3 | DONE |
| F18 | Final E2E Suite Verification & Adversarial Pass | Verify 100% pass rate across Tiers 1-4 + Tier 5 adversarial stress testing | M4 | Survey R3 | DONE |

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| E2E | E2E Testing Suite Track | Design test runner, create comprehensive 4-Tier test suite (Tiers 1-4), publish TEST_READY.md | Survey Phase Complete | DONE |
| M1 | Ukrainian Poetry Skill & References Overhaul | Implement F1-F8 in `skills/ukrainian-poetry/SKILL.md`, `full-guide.md`, `input-templates.md`, `rubric.md` | Survey Phase Complete | DONE |
| M2 | Suno AI Skill & Prompt Packs Overhaul | Implement F9-F14 in `skills/ukrainian-poetry-to-suno/SKILL.md`, `references/`, `packs/` | Survey Phase Complete | DONE |
| M3 | Cross-Skill Integration, Cheatsheets & Root Sync | Implement F15-F16, synchronize root cheatsheets/packs, ensure zero divergence | M1, M2 | DONE |
| M4 | Final E2E Suite Pass & Adversarial Hardening | Implement F18: Pass 100% of E2E test suite (Tiers 1-4) and Tier 5 Adversarial Hardening | E2E, M3 | DONE |

## Interface Contracts
### `ukrainian-poetry` ↔ `ukrainian-poetry-to-suno`
- **Output Format of Poetry Skill**:
  - Lyrics formatted strictly with stanza groupings and optional structural annotations.
  - Section headers must use standard Suno metatag naming conventions (e.g., `[Куплет 1]` / `[Verse 1]`, `[Приспів]` / `[Chorus]`, `[Міст]` / `[Bridge]`).
  - Stresses must be strictly verified according to literary standard Ukrainian, with acute accent / capitalized markers permitted for homograph resolution.
  - Backing vocals, echoes, and harmonies must be encased in parentheses: `(луна)`, `(бек-вокал)`.
- **Input Consumption by Suno Conversion Skill**:
  - Takes raw or structured Ukrainian lyrics, creative briefs, or reference artists.
  - Maps poetic cadence and mood directly to modern musical subgenres and BPM ranges.
  - Produces dual-field Custom Mode payloads:
    1. `Style of Music`: Strictly English tokens, <= 180 characters (optimal 80-150), no metadata leakage (`Language:`, `Theme:` strictly forbidden in style box).
    2. `Lyrics Box`: Structured with parseable `[Bracketed]` metatags, parenthetical backing cues, and dynamic performance transitions.
    3. `Exclude / Negative Prompt`: Targeted anti-genre and anti-artifact suppression tokens.

## Code Layout
- Canonical Poetry Skill: `skills/ukrainian-poetry/`
  - `SKILL.md`: Core skill entry point and instructions
  - `references/full-guide.md`: Comprehensive theoretical and operational guide
  - `references/input-templates.md`: Structured user input templates and parameters
  - `references/rubric.md`: 100-point evaluation and scansion rubric
  - `references/tests.md`: Standard test suite
  - `references/stress-tests.md`: Stress test scenarios
- Canonical Suno Skill: `skills/ukrainian-poetry-to-suno/`
  - `SKILL.md`: Core skill entry point and instructions
  - `references/full-guide.md`: Comprehensive Suno conversion guide
  - `references/prompt-builder.md`: Modular style prompt composition rules
  - `references/mood-to-style-map.md`: Mood and emotion to genre mapping
  - `references/reference-to-style-cheatsheet.md`: Ukrainian artist and sonic reference cheatsheet
  - `references/reference-breakdown-examples.md`: Reference breakdown examples
  - `references/lyrics-to-suno-template.md`: Full song arrangement templates
  - `references/song-structure-pack.md`: Metatag structural templates
  - `references/packs/`: The 7 specialized prompt packs
- E2E Test Suite & Infrastructure:
  - `TEST_INFRA.md`: Master E2E testing architecture and coverage matrix
  - `tests/`: Automated / deterministic test cases across Tiers 1-4 & validator engines
  - `TEST_READY.md`: Signal from E2E Testing Track when ready

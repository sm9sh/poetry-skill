# Ukrainian Poetry & Suno AI Skill Ecosystem (v2.0.0)

A comprehensive AI skill ecosystem for generating, auditing, verifying, and transforming authentic Ukrainian poetry into production-grade prompts for **Suno AI** (v3.5 / v4).

---

## 1. System Architecture

The architecture connects two specialized AI skills with a shared reference foundation, 100-point evaluation rubrics, and a 4-tier automated E2E testing framework:

```text
                  [User Input / Creative Brief]
                                │
                                ▼
               ┌─────────────────────────────────┐
               │     ukrainian-poetry Skill      │
               │  - Syllabo-Tonic & Dolnik       │
               │  - 14-Syllable Kolomyika Verse  │
               │  - Mobile Stress & Homographs   │
               │  - Heterogeneous Rhymes         │
               │  - 6 Registers & Anti-Kitsch    │
               └────────────────┬────────────────┘
                                │ (Structured Lyrics + Prosodic Metatags)
                                ▼
               ┌─────────────────────────────────┐
               │   ukrainian-poetry-to-suno      │
               │  - 80–180 Char Token Economy    │
               │  - Metatags [Verse]/[Chorus]    │
               │  - 8 Modern Ukrainian Genres    │
               │  - Acoustic Exclude Vectors     │
               └────────────────┬────────────────┘
                                │
                                ▼
                   [Suno AI Custom Mode Ready]
```

---

## 2. Repository Structure

### 2.1 Canonical Skills (Runtime-Ready)
- `skills/ukrainian-poetry/`:
  - `SKILL.md` — main poetry skill entrypoint
  - `references/full-guide.md` — comprehensive versification, scansion, and accentuation reference
  - `references/input-templates.md` — structured input prompt templates
  - `references/rubric.md` — 100-point poetry evaluation rubric
  - `references/tests.md` — standardized test suite (27 scenarios)
  - `references/stress-tests.md` — hardened stress tests (22 scenarios)
- `skills/ukrainian-poetry-to-suno/`:
  - `SKILL.md` — main Suno conversion skill entrypoint
  - `references/full-guide.md` — comprehensive Suno prompt engineering guide
  - `references/prompt-builder.md` — modular 6-part prompt builder (80–180 chars)
  - `references/mood-to-style-map.md` — mapping emotions and BPMs to genres
  - `references/reference-to-style-cheatsheet.md` — Ukrainian artist reference translation cheatsheet
  - `references/reference-breakdown-examples.md` — detailed reference breakdown examples
  - `references/lyrics-to-suno-template.md` — song structure and arrangement templates
  - `references/song-structure-pack.md` — metatag arrangement templates with backing vocals
  - `references/suno-prompt-anti-patterns.md` — prompt anti-patterns and error correction
  - `references/rubric.md` — 100-point Suno style prompt evaluation rubric
  - `references/tests.md` — Suno prompt test suite (12 scenarios)
  - `references/packs/` — 7 specialized prompt packs (`dark`, `female`, `male`, `sad`, `uplifting`, `uk-ref`, `ref-pack`)

### 2.2 Root References & Standalone Documents
- `ukrainian-poetry-skill.md` — standalone comprehensive English guide for poetry
- `ukrainian-poetry-skill-uk.md` — standalone comprehensive Ukrainian guide for poetry
- `ukrainian-poetry-skill-lite.md` — compact lite version for fast local runs
- `ukrainian-poetry-to-suno.md` — standalone Suno conversion guide
- `ukrainian-poetry-skill-rubric.md` — mirror of the 100-point poetry rubric
- `suno-style-rubric.md` — mirror of the 100-point Suno rubric
- `packs/` — synchronized root Suno prompt packs
- `INSTALL.md` — runner integration instructions

### 2.3 Automated 4-Tier E2E Test Infrastructure
- `tests/run_tests.py` — master test runner (59 test cases, 100% pass rate)
- `tests/run_tests.ps1` — PowerShell wrapper
- `tests/validator/` — deterministic rhythm, stress, style, metatag, and rubric validation engines
- `TEST_INFRA.md` — complete test architecture and coverage matrix

---

## 3. Key Features

### 3.1 Ukrainian Versification & Linguistic Fidelity
- **5 Syllabo-Tonic Meters**: Iamb (`U —`), Trochee (`— U`), Dactyl (`— U U`), Amphibrach (`U — U`), Anapest (`U U —`) with natural pyrrhic substitutions.
- **Non-Syllabo-Tonic Systems**: Dolnik (1–2 syllable intervals), Taktovik (1–3 syllables), Accentual verse, 14-syllable Kolomyika `(4+4)+6` with mandatory caesura after syllable 8.
- **Blank Verse vs Free Verse**: Strict distinction between unrhymed metric iambic blank verse and cadence-driven verlibre.
- **Fixed Classical Forms**: Petrarchan/Shakespearean Sonnets with mandatory Volta at line 9, Rondo, Triolet, Terza Rima.
- **Mobile Stress & Homographs**: Standard literary orthoepy (*вИпадок*, *чорнОзем*, *новИй*, *одИннадцять*), homograph disambiguation (*зАмок/замОк*, *дорогА/дорОга*).
- **Heterogeneous Rhyming**: Cross-grammatical rhyming (verb+noun, noun+adverb) with zero tolerance for same-part-of-speech or diminutive clichés.
- **6 Authentic Registers**: Contemporary Urban, Chamber Intimate, Philosophical Neoclassical, Cossack Baroque (17th c.), Authentic Folk/Ritual, Children's Playful.
- **Anti-Sharovarshchyna**: Complete ban on tourist souvenir clichés and decorative folk kitsch.

### 3.2 Suno AI Music Prompt Engineering
- **Token Economy (80–180 Characters)**: Optimal character window preventing prompt dilution and generic pop-rock averaging.
- **Clean Field Separation**: Zero metadata leakage (`Language:`, `Theme:`) inside the style box; English musical descriptors with authentic cultural acoustic anchors (`bandura`, `sopilka`, `white voice`).
- **Bracketed Metatags**: Standardized `[Intro]`, `[Verse]`, `[Pre-Chorus]`, `[Chorus]`, `[Drop]`, `[Outro]` and parenthetical backing cues `(...)`.
- **8 Modern Ukrainian Music Genres**: Ethno-Chaos, Post-Punk, Dark Synth, Trap-Folk, Melodic Metalcore, Shoegaze, Ethno-Rock, Neoclassical Bandura.
- **Authentic Vocal Timbres**: White Voice (*білий голос*), intimate breathy falsetto, post-punk baritone, spoken melodeclamation, extreme metalcore growls/cleans, stylized trap autotune.
- **Acoustic Anti-Artifact Negative Vectors**: Suppression of metallic treble sibilance, boomy sub-bass, cavernous reverb, and diffusion haze.

---

## 4. Quick Start

### Running the E2E Test Suite
```powershell
# Run all 59 tests
py -3 tests/run_tests.py --all

# Run a specific tier (e.g. Tier 1 or Tier 3)
py -3 tests/run_tests.py --tier 1
```

### Generating a Song (Custom Mode)
1. Generate authentic Ukrainian lyrics using `skills/ukrainian-poetry/`.
2. Convert the lyrics and mood into Suno format with `skills/ukrainian-poetry-to-suno/`.
3. Paste the generated `Style of Music` (80–180 chars), `Lyrics` (with bracketed metatags), and `Exclude` into Suno AI Custom Mode.

# Version History

## v2.0.0 - 2026-08-26

Major Architecture Overhaul, Complete Versification & Suno AI Engine Upgrade, and 4-Tier Automated E2E Test Suite.

### Added
- **Versification & Meter Engine (Features F1–F5)**:
  - 5 Syllabo-Tonic meters with pyrrhic substitution mechanics (Iamb, Trochee, Dactyl, Amphibrach, Anapest).
  - Non-syllabo-tonic systems: 3/4-stress Dolnik, Taktovik, Accentual verse, and 14-syllable `(4+4)+6` Kolomyika verse with mandatory caesura.
  - Blank verse (*білий вірш*) codification distinct from free verse (*верлібр*).
  - Fixed forms: Italian/Shakespearean Sonnets with mandatory Volta at line 9, Rondo, Triolet, Terza Rima.
  - Clausulae alternation rules (`ЖЧЖЧ`, `ЧЖЧЖ`, `ЖЖЧЖ`, `ДЧДЧ`).
- **Stress & Linguistic Fidelity Engine (Features F6–F8)**:
  - Mobile stress paradigm catalog and 10+ stress homograph disambiguation pairs (*зАмок/замОк*, *дорогА/дорОга*, *мукА/мУка*).
  - Anti-Russian misaccentuation blacklist (*вИпадок*, *чорнОзем*, *новИй*, *одИннадцять*, *листопАд*, *рукОпис*).
  - Heterogeneous cross-grammatical rhyming mandates with strict blacklist of verb-verb, adjective-adjective, and diminutive suffixes.
  - 6 Authentic Registers: Contemporary Urban, Chamber Intimate, Philosophical Neoclassical, Cossack Baroque, Folk Authentic, Children's Playful.
  - Strict anti-sharovarshchyna guardrails and Russianism/Surzhyk correction catalog.
- **Suno AI Music Prompt Engineering Engine (Features F9–F14)**:
  - Strict **80–180 character token economy** (~15–30 tokens) with left-to-right positional priority.
  - Clean field separation: complete elimination of metadata leakage (`Language:`, `Theme:`) from style prompts.
  - Standardized bracketed metatags (`[Intro]`, `[Verse]`, `[Pre-Chorus]`, `[Chorus]`, `[Drop]`, `[Outro]`) and parenthetical backing vocal syntax `(...)`.
  - **8-Genre Modern Ukrainian Music Taxonomy**: Ethno-Chaos, Post-Punk, Dark Synth, Trap-Folk, Melodic Metalcore, Shoegaze, Ethno-Rock, Neoclassical Bandura.
  - Authentic vocal timbre directives: White Voice (*білий голос*), intimate breathy, post-punk baritone, spoken melodeclamation, extreme metalcore growl/clean, modern autotuned trap.
  - Acoustic anti-artifact negative prompting: concrete Exclude vectors suppressing metallic treble, muddy bass, and diffusion blur.
- **4-Tier E2E Test Suite & Infrastructure (Feature F17)**:
  - Master test runner (`tests/run_tests.py` and `tests/run_tests.ps1`) executing 59 test cases across Tiers 1–4 with 100% pass rate.
  - Deterministic validation engines in `tests/validator/`: `StyleValidator`, `MetatagValidator`, `PoeticValidator`, `RubricScorer`.
  - Master architecture and coverage matrix: `TEST_INFRA.md`.
- **Synchronized Ecosystem & 100-Point Rubrics (Features F15, F16)**:
  - Complete synchronization of root `packs/*` and root reference mirrors with canonical sources in `skills/`.
  - Standalone single-file documentation upgraded in `ukrainian-poetry-skill.md`, `ukrainian-poetry-skill-uk.md`, `ukrainian-poetry-skill-lite.md`, and `ukrainian-poetry-to-suno.md`.
  - Comprehensive 100-point evaluation rubrics with explicit deduction matrices for both poetry and Suno music prompt engineering.

### Changed
- All 7 specialized prompt packs (`dark`, `female`, `male`, `sad`, `uplifting`, `uk-ref`, `ref-pack`) overhauled with 80–180 char style bounds, bracketed metatags, and zero metadata leakage.
- `suno-reference-prompt-pack-uk.md` standardized to English musical style descriptors with Ukrainian lyrics, resolving the localization degradation paradox.
- `README.md`, `README.en.md`, and `HOWTO.md` updated to reflect the full v2.0.0 system architecture and automated test workflows.

---

## v1.2.0 - 2026-04-28

Best-practice folder-based skill packaging.

### Added
- `skills/ukrainian-poetry/SKILL.md`
- `skills/ukrainian-poetry/agents/openai.yaml`
- `skills/ukrainian-poetry/references/`
- `skills/ukrainian-poetry-to-suno/SKILL.md`
- `skills/ukrainian-poetry-to-suno/agents/openai.yaml`
- `skills/ukrainian-poetry-to-suno/references/`
- `source/legacy-skills/` for archived single-file runtime entrypoints

### Changed
- canonical runtime entrypoints are now folder-based skills, not standalone `.md` files
- large examples, rubrics, tests, prompt packs, and full legacy guides moved behind `references/`
- `SKILL.md` files now use concise progressive-disclosure instructions and `Use when...` trigger descriptions
- install docs now point to `skills/ukrainian-poetry/` and `skills/ukrainian-poetry-to-suno/`

### Removed
- duplicate standalone skill files from the top level of `skills/`

---

## v1.1.0 - 2026-04-23

Documentation and packaging update for runtime-ready skill loading.

### Added
- canonical `skills/` directory
- `skills/ukrainian-poetry.md`
- `skills/ukrainian-poetry-to-suno.md`
- `skills/README.md`
- `INSTALL.md` with generic integration examples for different runner setups

### Changed
- `README.md` now points to `skills/` as the canonical runtime entry point
- `README.en.md` now points to `skills/` as the canonical runtime entry point
- `HOWTO.md` now points to `skills/` and `INSTALL.md`

### Notes
- original root skill files remain in place as source versions and documentation assets

---

## v1.0.0 - 2026-04-19

Initial local release of the Ukrainian poetry skill pack.

### Included files
- `ukrainian-poetry-skill.md`
- `ukrainian-poetry-skill-uk.md`
- `ukrainian-poetry-skill-lite.md`
- `ukrainian-poetry-skill-input-template.md`
- `ukrainian-poetry-skill-tests.md`
- `ukrainian-poetry-skill-stress-pack.md`
- `ukrainian-poetry-skill-rubric.md`
- `ukrainian-poetry-to-suno.md`
- `lyrics-to-suno-template.md`
- `suno-prompt-tests.md`
- `suno-style-rubric.md`
- `reference-to-style-cheatsheet.md`
- `reference-breakdown-examples.md`
- `mood-to-style-map.md`
- `suno-prompt-anti-patterns.md`
- `song-structure-pack.md`
- `prompt-builder.md`
- `ukrainian-song-scenarios.md`
- `packs/suno-reference-prompt-pack.md`
- `packs/suno-reference-prompt-pack-uk.md`
- `packs/female-vocal-pack.md`
- `packs/male-vocal-pack.md`
- `packs/sad-pack.md`
- `packs/dark-pack.md`
- `packs/uplifting-pack.md`
- `README.md`
- `README.en.md`

### Main features
- full Ukrainian poetry skill with mode-based behavior
- fully Ukrainian localized version
- compact lite version for faster local runs
- prompt input templates
- basic tests and advanced stress tests
- scoring rubric for quality evaluation
- separate Suno prompt conversion module
- lyrics-to-Suno templates and tests
- reference-based safe style extraction from artist/song inputs
- Suno help-center prompt recommendations integrated into the Suno module and templates
- Suno style evaluation rubric
- reference-to-style conversion cheatsheet
- reference breakdown examples
- mood-to-style mapping
- Suno prompt anti-pattern guide
- song structure template pack
- block-based prompt builder
- Ukrainian song scenario library
- ready-made Suno reference prompt pack focused on pop and rock
- Ukrainian-language pop/rock Suno prompt pack
- female vocal Suno prompt pack
- male vocal Suno prompt pack
- local documentation in Ukrainian and English

# Version History

## v4.0.0 - 2026-09-27

Refocus on the core goal — quality Ukrainian poems and their adaptation into songs for **Suno v6-mini** and **Google Flow Music (Lyria 3.5)**.

### Added
- `references/poem-to-song-adaptation.md` — poem → song workflow (keep vs adapt mode, hook, song form, syllable matching, singable vowels) with a full worked example.
- `references/platforms.md` — dated platform facts: Suno v6 family (v6-mini default, Variety slider, limits), Flow Music (Lyria 3.5), Udio status.
- `references/post-production.md` — DAW, mastering, release and Gates 7–10, now loaded only on request.
- `scripts/check_lyrics.py` — stdlib pre-flight checker for lyrics / Style / Exclude.
- `evals/` — real-prompt evals for with-skill vs without-skill comparison.

### Changed
- Vocal delivery cues (`[Whispered]`, `[Key Change]`, `[Half-time feel]`…) moved from `( )` to `[ ]` everywhere: Suno and Flow Music sing parenthesized text. Validator now rejects cues in parentheses.
- Stress capitals limited to three categories in all examples and references; removed over-marking (`моЯ`, `прИйде`, …).
- Fixed the attested stress-variant table (`колИсь`, `нікОли`, `святИй` are the norms; Russian `рЕка`, `такЖе` removed).
- Suno target updated from v4.5/v5.5 (retired 2026-09-09) to v6-mini.
- Skill descriptions rewritten with Ukrainian trigger phrases; poetry agent pipeline changed to drafts → critic notes → single revision.
- `AGENTS.md` condensed to core rules (was ~15 KB loaded into every session).
- Meter fixtures rewritten to follow the skill's own rules.

- Rule: no rare, archaic, dialect or invented words unless the user explicitly asks (AGENTS.md, both skills, rubric deduction, agents).
- Rule: every song for AI passes 12 world-class song criteria (research on chart hits, songwriting-competition standards, Berklee / Pattison prosody) — `references/world-class-song-criteria.md`; `check_lyrics.py` now flags a single chorus, a non-repeating hook and a copied Verse 2.
- Poetry Quality Checklist extended to 16 items from authoritative sources (Pound, Eliot, Frost, Kooser, Theune, Franko, Potebnja, Gasparov, Poetry Society): literal clarity, composition, the turn, discovery, subtext, line breaks, title; objective correlative and semantic halo of meter added to existing items; rubric deductions added — `references/quality-criteria.md`.
- Rule: every poem and song lyric passes the Quality Checklist (6 principles + living vocabulary + language correctness + brief) before output.

### Removed
- `CLAUDE.md`, `GEMINI.md` (rules live in `AGENTS.md`).
- `skills/poetry-skill` router skill (overlapped with the two real skills; `/poetry-skill` command kept).
- Agent work artifacts under `.agents/` (handoffs, audits, surveys); `.agents/skills/` mirror kept.

## v3.0.0 - 2026-09-06

Multi-platform AI Music Generation Upgrade (Suno v4.5/v5.5, Udio v4, Google Flow Music Lyria 3.5), 6-Step Production Lifecycle Architecture, and 10 AI Quality Gates.

### Added
- **Multi-platform expansion**: Support for Suno v4.5/v5.5, Udio v4, and Google Flow Music Lyria 3.5.
- **6-Step Production Lifecycle Architecture**.
- **10 AI Quality Gates Matrix** for comprehensive quality control.
- **Western Genre Anchor** with an updated 8-genre taxonomy.
- **Vocal Triple-Stack** formula for complex vocal arrangements.
- **AI Conductor extensions roadmap** (Seed → Extend → Breakdown → Mega-Chorus → Outro).
- **DAW stem mixing checklist** (Split Bass, Tchad Blake distortion, Mid-Side reverb sidechain).
- **Mastering guide** avoiding the True Peak trap (-1 dBTP for -6..-8 LUFS).
- **Streaming distribution rules** (Skip Rate thresholds, Playlist Placement Trap elimination).
- **4 new music production subagents** for Suno, Udio, and Flow Music.
- **Udio + Flow Music validators** to ensure output quality.
- **Metatag grammar**: Strict rules for brackets vs parentheses, 9 canonical inline vocal gestures.
- **Suno Method 1 (Conversational) and Method 2 (HookGenius Tag Matrix)** workflow integration.
- **AGENTS.md** established as the Single Source of Truth for system architecture.

### Changed
- Updated `README.md`, `README.en.md`, and `HOWTO.md` to reflect multi-platform ecosystem.

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

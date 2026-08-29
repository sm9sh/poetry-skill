# Project: AI Music Alchemy & Prompt Engineer v8 Integration

## Architecture
This project integrates the authoritative specification `ai-music-generation-meta-spec-v8.md` into the `poetry-skill` repository.
The architecture unites:
1. **6-Step AI Music Lifecycle**: Reverse Engineering -> AI Lyrics & Melodic Math -> Multi-Platform Prompting -> AI Conductor Extensions -> DAW Stem Mixing -> Mastering & Streaming Distribution.
2. **Multi-Platform Matrix**: Suno AI (v4.5/v5.5 Method 1 & 2), Udio AI (v4 48kHz, Context Length, Inpainting `*stars*`, Pro license), Google Flow Music (Lyria 3.5 Conversational Agent, Spaces, Turntable, Section Replace, AI Cover, Gemini Omni Flash video sync, 500 daily credits).
3. **10 AI Quality Gates**: Verification matrix across composition, prosody, generation, stem mixing, mastering, and marketing.
4. **Metatag & Phonics Rules**: Square brackets `[...]` for silent structural/arrangement cues; round parentheses `(...)` exclusively for vocals, backing vocals, and 9 canonical inline vocal gestures (`(whispered)`, `(belted)`, `(falsetto)`, `(screamed)`, `(ad-lib)`, `(building intensity)`, `(key change)`, `(half-time feel)`, `(harmonized)`).
5. **Ukrainian Poetic Integrity**: Full preservation of 6 Core Poetic Principles, capitalized stressed vowels (`вИпадок`, `дорОга`), zero grammatical rhyming, and natural syntax.

## Feature Inventory
| # | Feature | Description | Milestone | Source |
|---|---------|-------------|-----------|--------|
| 1 | Step 1 Reverse Engineering | Genre hybrid, BPM, Key, Vocal Triple-Stack, Melodic Math hooks, bracketed layout | M1 | meta-spec v8 |
| 2 | Step 2 AI-Optimized Lyrics | Syllable symmetry, Spoken Prosody Test, Staccato vs Legato, 5s Rule, 50s Chorus Rule, Melodic Previews, Glue Hooks, <=3-4 melodies | M1 | meta-spec v8 |
| 3 | Step 3 Suno v4.5/v5.5 Prompting | Method 1 First 5 Words & Method 2 HookGenius Tag Matrix 5 modules, My Taste, Voices, Custom Models, Failure Modes | M1 | meta-spec v8 |
| 4 | Step 3 Udio v4 Prompting | 48kHz stereo, Context Length 10-15s vs max, Inpainting `*stars*`, Pro licensing rights ($30/mo) | M1 | meta-spec v8 |
| 5 | Step 3 Flow Music Lyria 3.5 | Conversational Agent, Spaces, Turntable, Section Replace, AI Cover, Gemini Omni Flash sync, 500 daily credits | M1 | meta-spec v8 |
| 6 | Step 4 AI Conductor Extensions | Seed 30-50s, Extend, Vance Powell Verse 2 development (tambourine/shaker/backing), Breakdown 15-20s & Mega-Chorus, Outro <=20s | M1 | meta-spec v8 |
| 7 | Step 5 DAW Stem Post-Production | Stem splitting, Phase alignment mono check, dynamic sidechain unmasking, Bass Split Compression (<200Hz brickwall vs >200Hz saturated), Tchad Blake parallel drum distortion directly to Master Fader, Mid-Side Reverb sidechain | M1 | meta-spec v8 |
| 8 | Step 6 Mastering & Distribution | Mastering without True Peak trap (-1 dBTP for -6..-8 LUFS with TP limiting disabled, or -14 LUFS for -2 dBTP), genre skip rate thresholds (Pop >48%, Hip-hop >44%, Electronic >37%, Indie rock >31%, alarm >45%), Playlist Placement Trap elimination (single-only ads), Spotify Canvas/Marquee/Discovery Mode | M1 | meta-spec v8 |
| 9 | 10 AI Quality Gates Table | Full 10-gate quality matrix (Anti-Skip 5s, 50s Chorus, Spoken Prosody, Staccato/Legato, Verse 2 Development, Breakdown/Mega-Chorus, Low-End Split Compression, Tchad Blake Distortion to Master, True Peak Mastering, Single-Only Ads) | M1, M2 | meta-spec v8 |
| 10 | Global Directives Sync | Update AGENTS.md, GEMINI.md, skills/poetry-skill/SKILL.md with v8 directives and constraints | M1 | ORIGINAL_REQUEST |
| 11 | Metatag Grammar & Inline Gestures | Expand song-structure-pack.md, lyrics-to-suno-template.md, suno-prompt-anti-patterns.md with 9 inline gestures in `(...)` and structural tags in `[...]` | M2 | meta-spec v8 |
| 12 | Root Files Synchronization | Synchronize root mirror files (`ukrainian-poetry-to-suno.md`, `ukrainian-poetry-skill.md`, `lyrics-to-suno-template.md`, `song-structure-pack.md`, `suno-prompt-anti-patterns.md`, `suno-style-rubric.md`) | M2 | ORIGINAL_REQUEST |
| 13 | Validator Extension | Update `tests/validator/metatag_validator.py` and `tests/validator/suno_validator.py` to support new structural prefixes and whitelist inline gestures in parentheses | M3 | meta-spec v8 |
| 14 | Test Suite Verification | Run `py -3 tests/run_tests.py --all` ensuring 100% pass (63+ tests, 0 errors, high rubric scores) | M3 | ORIGINAL_REQUEST |
| 15 | Local & Global Plugin Sync | Copy updated skills and directives to `.agents/skills/` and `C:\Users\sm9sh\.gemini\config\plugins\poetry-skill\` | M4 | ORIGINAL_REQUEST |
| 16 | Post-Implementation 3-Agent Audit | 3 specialized auditor agents: Prompt & Platform Spec Auditor, Audio Engineering & Distribution Auditor, Ukrainian Poetry & Cross-System Integrity Auditor | M5 | ORIGINAL_REQUEST R4 |

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| 1 | M1: Skills & Reference Guides Update | Update `skills/ukrainian-poetry-to-suno/`, `skills/poetry-skill/`, `AGENTS.md`, `GEMINI.md` | none | DONE |
| 2 | M2: Root Mirrored Files & Template Packs Sync | Update root templates, song-structure-pack, anti-patterns, rubric | M1 | DONE |
| 3 | M3: Validators, Test Suite Sync & Test Pass | Update `tests/validator/`, verify 100% tests pass on `py -3 tests/run_tests.py --all` | M2 | DONE |
| 4 | M4: Ecosystem & Global Plugin Sync | Synchronize to `.agents/skills/` and `C:\Users\sm9sh\.gemini\config\plugins\poetry-skill\` | M3 | DONE |
| 5 | M5: Post-Implementation 3-Agent Audit | Dispatch 3 independent specialized auditors to verify compliance with zero findings | M4 | DONE |

## Interface Contracts
### `skills/ukrainian-poetry-to-suno` ↔ `tests/validator/metatag_validator.py`
- Structural tags in `[...]`: `[Intro]`, `[Vocal Intro]`, `[Beat Drop]`, `[Verse]`, `[Verse 1]`, `[Verse 2]`, `[Pre-Chorus]`, `[Chorus]`, `[Post-Chorus]`, `[Instrumental Break]`, `[Bridge]`, `[Breakdown]`, `[Mega-Chorus]`, `[Outro]`, `[End]`.
- Inline vocal gestures in `(...)`: `(whispered)`, `(belted)`, `(falsetto)`, `(screamed)`, `(ad-lib)`, `(building intensity)`, `(key change)`, `(half-time feel)`, `(harmonized)` alongside backing vocal words/echoes.
- Disallowed in `(...)`: instrumental/arrangement keywords like `(guitar solo)`, `(drum roll)`, `(synthesizer)`, `(drop)`, etc.

### `skills/ukrainian-poetry` ↔ `skills/ukrainian-poetry-to-suno`
- Poetry module output adheres to 6 Poetic Principles and capitalizes stressed vowels on non-obvious/homographic words (`вИпадок`, `дорОга`, `моЯ`, `землЯ`, `зЕмлю`).
- Suno module consumes Ukrainian poetic lyrics, validates Spoken Prosody and syllable balance, wraps arrangement instructions in `[...]`, and applies Western sonic aesthetics in prompt generation.

## Code Layout
- `skills/ukrainian-poetry-to-suno/SKILL.md`: Main entry point for AI music generation skill.
- `skills/ukrainian-poetry-to-suno/references/`: Reference manuals (`full-guide.md`, `prompt-builder.md`, `mood-to-style-map.md`, `reference-to-style-cheatsheet.md`, `song-structure-pack.md`, `lyrics-to-suno-template.md`, `suno-prompt-anti-patterns.md`, `rubric.md`).
- Root mirrored documentation: `ukrainian-poetry-to-suno.md`, `ukrainian-poetry-skill.md`, `lyrics-to-suno-template.md`, `song-structure-pack.md`, `suno-prompt-anti-patterns.md`, `suno-style-rubric.md`.
- `AGENTS.md`, `GEMINI.md`: Root configuration directives.
- `tests/`: Test runners and validators (`tests/run_tests.py`, `tests/validator/*.py`).
- Global Plugin Path: `C:\Users\sm9sh\.gemini\config\plugins\poetry-skill\`.

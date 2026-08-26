# CLAUDE.md — Ukrainian Poetry & Suno Music Skills Guide

This repository provides two specialized agent skills:
1. `ukrainian-poetry` (`skills/ukrainian-poetry/SKILL.md`): Ukrainian versification, syllabo-tonic/tonic/free verse, stress scansion, and heterogeneous rhyming.
2. `ukrainian-poetry-to-suno` (`skills/ukrainian-poetry-to-suno/SKILL.md`): Suno AI & Flow Music prompt engineering targeting Western musical genres with Ukrainian lyrics.

## Skill Discovery & Triggers

- **When writing/editing Ukrainian poems, verses, lyrics, or rhymes**:
  - Read and apply `skills/ukrainian-poetry/SKILL.md`.
  - Follow strict Ukrainian accentuation, non-trivial rhymes (avoid verb-verb rhymes), and authentic registers (Urban, Intimate, Neoclassical, Baroque, Folk).
  - Avoid calques, surzhyk, and sharovarshchyna.
- **When creating Suno AI music prompts from Ukrainian themes, poems, or references**:
  - Read and apply `skills/ukrainian-poetry-to-suno/SKILL.md`.
  - Enforce the **Western Genre Rule**: All musical sound design must strictly target Western genres (Post-Punk, Darkwave, Synthwave, Trip-Hop, Alt-Pop, Shoegaze, Progressive Metalcore, Melodic Techno, Ambient).
  - Keep `Style of Music` strictly between **80–180 characters** (optimal 80–150), comma-delimited, strictly English tokens, zero metadata leakage (`Language:`, `Theme:` forbidden in style box).
  - Format `Lyrics` with standard bracketed metatags (`[Verse 1]`, `[Chorus]`, `[Drop]`, `[Outro]`) and parenthetical backing vocals `(луна)`.
  - Always include strict anti-local-pop and anti-artifact suppression in `Exclude`: `cheesy regional pop, post-soviet schlager, wedding synth brass, cheap accordion, generic euro-pop, metallic highs`.

## Reference Navigation

- Poetic Theory & Rules: `skills/ukrainian-poetry/references/full-guide.md`
- Stress & Stress Homographs: `skills/ukrainian-poetry/references/rubric.md`
- Western References & Style Mapping: `skills/ukrainian-poetry-to-suno/references/reference-to-style-cheatsheet.md`
- Mood-to-Genre Map: `skills/ukrainian-poetry-to-suno/references/mood-to-style-map.md`
- Prompt Builder: `skills/ukrainian-poetry-to-suno/references/prompt-builder.md`

## Verification & Testing

Run deterministic test suites (Python 3 standard library):
```bash
py -3 tests/run_tests.py --all
```

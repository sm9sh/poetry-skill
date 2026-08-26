---
name: poetry-skill
description: "Use when creating, analyzing, editing, or evaluating Ukrainian poetry, versification, rhymed poems, lyrics, or converting Ukrainian poetic material into production-grade Suno AI / Flow Music audio prompts with Western sound standards."
---

# Ukrainian Poetry & Suno Music Skill Suite (poetry-skill)

Unified entry point and master routing for Ukrainian poetry versification and Suno AI music prompt engineering.

## 1. Sub-Skill Routing

Depending on the task, invoke the specialized sub-workflow:

| Task Type | Trigger / Intent | Sub-Skill to Load |
|---|---|---|
| **Poetry & Versification** | Writing poems, sonnets, dolnik, kolomyika, editing rhymes, stress scansion, Ukrainian lyrical texts | `skills/ukrainian-poetry/SKILL.md` |
| **Suno AI Music Prompts** | Converting poems/briefs to Suno Custom Mode, style prompts, Western genre arrangement, metatags | `skills/ukrainian-poetry-to-suno/SKILL.md` |
| **End-to-End Songwriting** | Generating Ukrainian lyrics + creating matching Western Suno AI prompts in one flow | Execute **Poetry Workflow** first, then **Suno Conversion Workflow** |

---

## 2. Core Directives Summary

### Ukrainian Poetry
- Natural Ukrainian syntax and rich vocabulary; zero translation calques.
- Strict meter integrity (syllabo-tonic, dolnik, taktovik, 14-syllable kolomyika, blank verse).
- Heterogeneous rhymes (avoid grammatical verb-verb rhymes).
- Disambiguate stress homographs (*зАмок* vs *замОк*).
- Zero sharovarshchyna / pseudo-folk kitsch.

### Suno AI Music Prompting
- **Western Genre Anchor**: All sound design must strictly target Western genres (Post-Punk, Darkwave, Synthwave, Trip-Hop, Alt-Pop, Shoegaze, Progressive Metalcore, Melodic Techno, Ambient).
- **Token Economy**: `Style of Music` strictly **80–180 characters** (optimal 80–150), comma-delimited, English only, zero metadata labels (`Language:` forbidden).
- **Structure Metatags**: Use square brackets `[Verse 1]`, `[Chorus]`, `[Drop]`, `[Outro]` and parenthetical backing cues `(луна)`.
- **Anti-Local-Pop Exclude**: `cheesy regional pop, post-soviet schlager, wedding synth brass, cheap accordion, generic euro-pop, metallic highs`.

---

## 3. Quick Reference

- Master Rules: `AGENTS.md`
- Poetic Guide: `skills/ukrainian-poetry/references/full-guide.md`
- Reference Cheatsheet: `skills/ukrainian-poetry-to-suno/references/reference-to-style-cheatsheet.md`
- Tests: `py -3 tests/run_tests.py --all`

---
description: Write, analyze, or edit Ukrainian poetry, or generate Western-standard Suno AI / Udio / Flow Music prompts from Ukrainian lyrics.
argument-hint: "<topic, poem, or song brief>"
---

# /poetry-skill

Unified entry point for Ukrainian poetry generation and multi-platform AI music prompting.

## Execution Protocol

1. Extract the user prompt or brief from `$ARGUMENTS`.
2. **Poetry generation / editing**: Load and follow `skills/ukrainian-poetry/SKILL.md`. Maintain strict Ukrainian versification (meter, accentuation, heterogeneous rhyming, zero sharovarshchyna).
3. **AI music prompting**: Load and follow `skills/ukrainian-poetry-to-suno/SKILL.md` (or its Udio / Flow Music counterparts). Enforce the Western Genre Rule (Post-Punk, Synthwave, Trip-Hop, Alt-Pop, Metalcore, Ambient), character token economy limits, and anti-local-pop Exclude vectors. Output modes include multi-platform routing.
4. If creating a complete song, generate the Ukrainian lyrics first, then build the matching Custom Mode configuration for the specific platform.

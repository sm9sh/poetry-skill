---
description: Write, analyze, or edit Ukrainian poetry, or generate Western-standard Suno AI music prompts from Ukrainian lyrics.
argument-hint: "<topic, poem, or song brief>"
---

# /poetry-skill

Unified entry point for Ukrainian poetry generation and Suno AI music prompting.

## Execution Protocol

1. Extract the user prompt or brief from `$ARGUMENTS`.
2. **Poetry generation / editing**: Load and follow `skills/ukrainian-poetry/SKILL.md`. Maintain strict Ukrainian versification (meter, accentuation, heterogeneous rhyming, zero sharovarshchyna).
3. **Suno AI music prompting**: Load and follow `skills/ukrainian-poetry-to-suno/SKILL.md`. Enforce the Western Genre Rule (Post-Punk, Synthwave, Trip-Hop, Alt-Pop, Metalcore, Ambient), 80-180 character token economy, and anti-local-pop Exclude vectors.
4. If creating a complete song, generate the Ukrainian lyrics first, then build the matching Suno AI Custom Mode configuration.

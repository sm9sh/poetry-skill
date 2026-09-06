---
description: Generate production-grade Western-style Suno AI, Udio v4, and Flow Music prompts for Ukrainian songs.
argument-hint: "<lyrics, mood, genre, reference, or platform>"
---

# /ukrainian-poetry-to-suno

Directly invokes the multi-platform AI prompt engineering workflow.

## Execution Protocol

1. Load `skills/ukrainian-poetry-to-suno/SKILL.md`.
2. Generate payload for the chosen platform (or multi-platform):
   - **Suno AI**: Generate Custom Mode payload (`Style of Music`: 80-180 characters, English Western genre tokens).
   - **Udio v4**: Generate Udio prompt formula (250 chars max, Context Length optimization, Inpainting *stars*).
   - **Flow Music**: Generate conversational agent mode prompts for Flow Music Lyria 3.5.
3. `Lyrics`: Ukrainian text with strict metatag grammar (brackets for structure like `[Verse]`, `[Chorus]`, parentheses for backing vocals). Ensure 9 canonical inline vocal gestures are used correctly.
4. `Exclude`: Anti-local-pop and anti-artifact vectors.

---
description: Generate production-grade Western-style Suno AI / Flow Music prompts for Ukrainian songs.
argument-hint: "<lyrics, mood, genre, or reference>"
---

# /ukrainian-poetry-to-suno

Directly invokes the Suno AI prompt engineering workflow.

## Execution Protocol

1. Load `skills/ukrainian-poetry-to-suno/SKILL.md`.
2. Generate Suno Custom Mode payload:
   - `Style of Music`: 80-180 characters, English Western genre tokens.
   - `Lyrics`: Ukrainian text with bracketed metatags (`[Verse]`, `[Chorus]`, `[Drop]`).
   - `Exclude`: Anti-local-pop and anti-artifact vectors.

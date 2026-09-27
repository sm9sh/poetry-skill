# Ukrainian Poetry & AI Songs (v4.0.0)

Two skills for AI agents (Claude Code, Gemini / Antigravity, Cursor, Codex):

| Skill | What it does |
|---|---|
| `skills/ukrainian-poetry/` | Writes, edits and scores Ukrainian poetry: fresh imagery, sincerity, correct stress and euphony, cross-grammatical rhymes, natural word order, form that fits the feeling. |
| `skills/ukrainian-poetry-to-suno/` | Turns a poem or idea into a song for **Suno v6-mini** (primary) and **Google Flow Music (Lyria 3.5)**: song form and hook, `[...]` / `(...)` markup, stress marks, Style and Exclude. |

Shared rules: `AGENTS.md`.

## Quick start
- "Write a poem about …" → poetry skill.
- "Turn this poem into a darkwave song for Suno" → the poem is adapted and you get Style / Exclude / Lyrics blocks. In Suno set **Variety = Off** so your Style is used verbatim.
- Check lyrics manually:
  ```bash
  python skills/ukrainian-poetry-to-suno/scripts/check_lyrics.py lyrics.txt --style "darkwave, ..." --exclude "cheesy pop, ..."
  ```

Key rule: Suno and Flow Music **sing** anything in `(parentheses)`; all cues (`[Whispered]`, `[Key Change]`) go in `[square brackets]`.

## Layout
- `skills/` — source of truth; `.agents/skills/` — runtime mirror (`python tests/sync_ecosystem.py`).
- `skills/ukrainian-poetry-to-suno/references/platforms.md` — dated platform facts.
- `examples/`, `tests/` (`python tests/run_tests.py --all`), `evals/` (real-prompt quality evals).

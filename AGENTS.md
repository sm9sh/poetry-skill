# AGENTS.md — Ukrainian Poetry & AI Song Skills

This repository holds two skills:

| Skill | What it does | Entry |
|---|---|---|
| `ukrainian-poetry` | Writes, edits and scores Ukrainian poetry | `skills/ukrainian-poetry/SKILL.md` |
| `ukrainian-poetry-to-suno` | Adapts poems into songs for **Suno v6-mini** (primary) and **Lyria 3.5** (Google Flow Music): song form, markup, stress, Style / Exclude prompts | `skills/ukrainian-poetry-to-suno/SKILL.md` |

Load the relevant `SKILL.md` for the task. The end-to-end workflow — routing, pipelines for poem / edit / song / generation fix, quality gates and conflict priorities — is in `docs/PIPELINE.md`. The rules below are the non-negotiable core shared by both skills; details, examples and word lists live in the skills and their `references/`.

## Poetry — 6 core principles

1. **Fresh imagery** — show through concrete sensory detail and action; no worn clichés (*кров — любов*, *серце палає*, *душа плаче*).
2. **Sincerity** — psychological truth and restraint; no pathos or moralizing (*«і я збагнув, що треба жити»*).
3. **Rhythm & sound** — a breathing meter (syllabo-tonic, dolnik, taktovik, kolomyika, blank verse, verlibre); cross-grammatical rhymes, no verb-verb or diminutive rhymes; Ukrainian euphony (`у/в`, `і/й`, `з/із/зі`).
4. **Word weight** — no filler pronouns (*цей, той, свій, вже, ось*) or padding; no inversions made only to force a rhyme — change the rhyme, not the syntax.
5. **Original angle** — micro-detail over macro-abstraction; open or paradoxical endings, not morals.
6. **Form = content** — meter, stanza, line breaks and tempo embody the feeling.

- **Living vocabulary** — do not use rare, archaic, dialect or invented words unless the user explicitly asks for them. Every word should be understandable to a contemporary reader (or listener) without a dictionary; if a common word breaks the meter, rework the line.
- **Mandatory quality check** — every poem and every song lyric is checked against the 16-item Quality Checklist in `skills/ukrainian-poetry/SKILL.md` before it is shown to the user: the 6 principles, living vocabulary, language correctness, the user's brief, literal clarity, composition, the turn (1–12 mandatory), plus discovery, subtext, line breaks and title (13–16; line breaks mandatory in free verse). Rationale and sources: `skills/ukrainian-poetry/references/quality-criteria.md`. Anything that fails is fixed and re-checked first. No exceptions for short pieces or quick edits.

## Songs — core rules

- **Target Suno v6-mini** (the free v6 model; all pre-v6 Suno models were retired on 2026-09-09) unless the user names another platform. Platform facts: `skills/ukrainian-poetry-to-suno/references/platforms.md`.
- **Mandatory world-class song check** — every song for AI, before it is shown to the user, passes the 12 world-class song criteria (`skills/ukrainian-poetry-to-suno/references/world-class-song-criteria.md`: central idea, title-hook, fast entry, verse/chorus contrast, verse development, specific-yet-relatable, easy on the ear, singability; plus compound hook, repetition with variation, stable/unstable form, fresh angle) and `check_lyrics.py`. Criteria 1–8 are mandatory; anything that fails is fixed and re-checked first.
- **Adapt, don't paste**: a poem becomes a song via hook, song form, equal line lengths and singable vowels (`references/poem-to-song-adaptation.md`). In songs, repeating the hook is a device, not padding.
- **Brackets**: `[Square]` for sections, instruments, dynamics **and vocal delivery** (`[Whispered]`, `[Key Change]`). `(Round)` only for words that should be **sung** as backing vocals / echoes — Suno and Lyria 3.5 sing whatever is in parentheses.
- **Stress marks** (uppercase stressed vowel) only in song lyrics for audio models, and only for homographs (`замОк`), Russian-stress traps (`вИпадок`), and non-obvious mobile shifts (`рУку`). Never in regular poetry; never on obvious words (*моя, земля, прийде*).
- **Attested poetic / folk stress variants**: at most 2 per poem or song, with a nameable source.
- **Sound**: Western contemporary genres (post-punk, darkwave, synthwave, trip-hop, alt-pop, shoegaze, metalcore, melodic techno, ambient). Keep regional pop / schlager / sharovarshchyna out via genre anchors and Exclude.
- **Style**: English tags, 80–200 chars, most important first; no negations (use Exclude); no artist names or song titles.
- Run `python skills/ukrainian-poetry-to-suno/scripts/check_lyrics.py` on lyrics before delivering.
- Mixing, mastering and release advice only when asked (`references/post-production.md`).

## Repository

- `skills/` is the source of truth. `.agents/skills/` is a runtime mirror — regenerate it with `python tests/sync_ecosystem.py`; don't edit it by hand.
- Tests: `python tests/run_tests.py --all` (Windows: `py -3 tests/run_tests.py --all`).
- Real-prompt evals for judging output quality: `evals/evals.json`.

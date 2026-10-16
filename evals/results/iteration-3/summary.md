# Evals — iteration 3

Baseline: `none` · trigger: `invoke` · generation model: `default`

| Eval | Task | With skill | Baseline | Winner | Prev. with skill | check_lyrics errors (skill / base) |
|---|---|---|---|---|---|---|
| 1 | father-fence-chamber | 8 | 4 | skill | 6.75 | — |
| 2 | fix-draft-rhymes | 7 | 2 | skill | 6.75 | — |
| 3 | sonnet-volta | 7 | 0.5 | skill | 5.75 | — |
| 4 | kolomyika-humor | 6.75 | 3 | skill | 6.25 | — |
| 5 | poem-to-darkwave-suno | 6.5 | 5.25 | skill | 6.5 | 0 / 0 |
| 6 | brief-to-song-flow | 5.75 | 4.75 | skill | 7.25 | 0 / 0 |
| 7 | keep-text-mode | 6.75 | 4.75 | skill | 7 | 0 / 0 |
| 8 | fix-generation-problems | 7.5 | 3.5 | skill | 5.5 | 0 / 0 |

**Skill wins 8, baseline wins 0, ties 0. Average: with skill 6.91, baseline 3.47.**
Previous iteration, with skill: 6.47 on 8 evals.

## Triggering

- eval 1 (father-fence-chamber): expected `ukrainian-poetry`, used ['ukrainian-poetry'] — invoked
- eval 2 (fix-draft-rhymes): expected `ukrainian-poetry`, used ['ukrainian-poetry'] — invoked
- eval 3 (sonnet-volta): expected `ukrainian-poetry`, used ['ukrainian-poetry'] — invoked
- eval 4 (kolomyika-humor): expected `ukrainian-poetry`, used ['ukrainian-poetry'] — invoked
- eval 5 (poem-to-darkwave-suno): expected `ukrainian-poetry-to-suno`, used ['ukrainian-poetry-to-suno'] — invoked
- eval 6 (brief-to-song-flow): expected `ukrainian-poetry-to-suno`, used ['ukrainian-poetry-to-suno'] — invoked
- eval 7 (keep-text-mode): expected `ukrainian-poetry-to-suno`, used ['ukrainian-poetry-to-suno'] — invoked
- eval 8 (fix-generation-problems): expected `ukrainian-poetry-to-suno`, used ['ukrainian-poetry-to-suno'] — invoked
- eval 9 (negative-english-poem): expected `none`, used none — ok
- eval 10 (negative-music-theory): expected `none`, used none — ok

Cost of this round: $2.57.

Next: listen to the song evals in Suno v6-mini / Lyria 3.5, note what lost and why in README.md.

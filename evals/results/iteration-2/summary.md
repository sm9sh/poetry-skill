# Evals — iteration 2

Baseline: `none` · trigger: `invoke` · generation model: `default`

| Eval | Task | With skill | Baseline | Winner | Prev. with skill | check_lyrics errors (skill / base) |
|---|---|---|---|---|---|---|
| 1 | father-fence-chamber | 6.75 | 8 | baseline | 8.5 | — |
| 2 | fix-draft-rhymes | 6.75 | 2.5 | skill | 7.5 | — |
| 3 | sonnet-volta | 5.75 | 3.75 | skill | 7.5 | — |
| 4 | kolomyika-humor | 6.25 | 3 | skill | 8 | — |
| 5 | poem-to-darkwave-suno | 6.5 | 5.5 | skill | 8.5 | 0 / 0 |
| 6 | brief-to-song-flow | 7.25 | 3 | skill | 9 | 0 / 0 |
| 7 | keep-text-mode | 7 | 4.5 | skill | 8 | 0 / 0 |
| 8 | fix-generation-problems | 5.5 | 4.5 | skill | 8.5 | 0 / 0 |

**Skill wins 7, baseline wins 1, ties 0. Average: with skill 6.47, baseline 4.34.**
Previous iteration, with skill: 8.19 on 8 evals.
Note: the previous iteration had a different judge (unknown vs default/5134928a/both-orders), so compare wins and the pairs themselves, not absolute scores.

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

Cost of this round: $2.86.

Next: listen to the song evals in Suno v6-mini / Lyria 3.5, note what lost and why in README.md.

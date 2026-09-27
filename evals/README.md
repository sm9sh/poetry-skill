# Evals

`tests/` checks validators and fixed fixtures. It cannot tell whether the skills make the model write **better** poems and songs. These evals can.

How to run a round:
1. For each prompt in `evals.json`, generate an answer **with** the skills and **without** them (or with the previous skill version from git).
2. Shuffle the pairs and judge them blind: which poem is better? which song sheet would you paste into Suno?
3. For song evals, actually generate in Suno v6-mini / Flow Music and listen: stress, sung instructions and rushing only show up in audio.
4. Pass lyrics through `python skills/ukrainian-poetry-to-suno/scripts/check_lyrics.py` to catch mechanical errors.
5. Write down what lost and why, then change the skill — prefer explaining the reason in the skill over adding another MUST.

Evals 9–10 are negative controls: the skills should not trigger.

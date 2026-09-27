# Production Scenario: Ukrainian Trip-Hop / Downtempo (Suno v6-mini)

**File**: `examples/success/suno-triphop-downtempo.md`
**Platform**: Suno v6-mini — Custom Mode, Variety: Off
**Genre Anchor**: Bristol-era trip-hop / downtempo
**Tempo**: 82 BPM
**Vocal Profile**: breathy female alto, close-mic, conversational phrasing

---

## 1. Concept

**Song «Прослухати знов».** Central idea: someone keeps the last 30-second voice message of a person who is gone, and plays it again every morning. The loss is never named; it is carried by objects and by one line in Verse 2 («і мовчиш уже рік підряд»).

- **Title-hook:** «Прослухати знов» — the phone's own button label, 5 syllables, opens every chorus.
- **Turn:** the bridge promises to let go «after this time», and the final chorus breaks the promise («і ще раз. Останній. Чесно.»).
- **Why trip-hop:** slow dusty breakbeat and dub bass leave room for a half-spoken vocal; the song lives in the pauses.

---

## 2. Style & Exclude (Suno v6-mini)

### Style (Suno v6-mini, Variety: Off)

```text
trip-hop, downtempo, melancholic, breathy female alto vocal, close-mic, dusty vinyl breakbeat, warm rhodes, deep dub sub bass, tape delay, 82 bpm
```

### Exclude

```text
cheesy regional pop, generic euro-pop, edm drop, aggressive vocals, bright acoustic strumming, heavy autotune
```

---

## 3. Lyrics

```text
[Intro - vinyl crackle, muted rhodes chords, phone voicemail beep]

[Verse 1 - intimate close-mic, dusty breakbeat enters]
Шоста ранку. Чайник закипів.
Телефон — екраном до стіни.
Я його не видалив, не зміг:
лиш тридцять секунд — і знову ти.

[Chorus - deep dub sub bass, lush tape delay, breathy vocal]
Прослухати знов —
тридцять секунд твого сміху.
Прослухати знов,
як ти просиш купити хліба.
(прослухати знов)

[Verse 2 - add soft cello and shaker]
Там на фоні — трамвай і злива,
ти смієшся чомусь невпопад,
а потім: «Скоро передзвоню» —
і мовчиш уже рік підряд.

[Chorus - deep dub sub bass, lush tape delay, breathy vocal]
Прослухати знов —
тридцять секунд твого сміху.
Прослухати знов,
як ти просиш купити хліба.
(прослухати знов)

[Bridge - stripped back, rhodes and voice only, half-time feel]
Кажуть, треба відпустити.
Я відпущу. Після цього разу.

[Final Chorus - full band, layered harmonies]
Прослухати знов —
тридцять секунд твого сміху.
Прослухати знов —
і ще раз. Останній. Чесно.
(прослухати знов)

[Outro - tape delay fades, voicemail beep]
[End]
```

---

## 4. Why It Works

| Criterion | How the song meets it |
|---|---|
| Central idea | A kept voicemail = refusing to let go; everything in the song serves that. |
| Title-hook | «Прослухати знов» opens every chorus and returns as a sung echo — 9 times in total. |
| Fast entry | 2-second intro, voice at once, chorus after 4 lines (~35 s at 82 BPM). |
| Contrast | Verses are concrete and near-spoken; the chorus stretches on long vowels (*знов*, *сміху*). |
| Development | V1: the morning ritual. V2: what is on the recording — and the year of silence. |
| Specific yet relatable | Kettle, phone face-down, tram and rain in the background — anyone who kept a message recognises it. |
| Turn | The bridge promise and its break in the final chorus. |
| Stress | No marks needed — no word falls into the three risky categories (homographs, Russian-stress traps, non-obvious shifts). |
| Parentheses | Only the sung echo *(прослухати знов)*; all delivery cues sit in `[...]`. |

Check before generating:

```bash
python skills/ukrainian-poetry-to-suno/scripts/check_lyrics.py lyrics.txt \
  --style "trip-hop, downtempo, ..." --exclude "cheesy regional pop, ..."
```

Post-production (stems, mastering, release) — only if needed: `skills/ukrainian-poetry-to-suno/references/post-production.md`.

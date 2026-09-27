# Production Scenario: Ukrainian Cinematic Ambient / Spoken Word (Lyria 3.5)

**File**: `examples/success/lyria-cinematic-ambient.md`
**Platform**: Lyria 3.5 (Google Flow Music) — natural-language prompt + lyrics
**Genre Anchor**: cinematic ambient / neoclassical spoken word
**Tempo**: 65 BPM, about 3 minutes (Lyria 3.5 tracks run up to ~3 min)
**Vocal Profile**: low warm male spoken voice in verses; soft sung female voice in the chorus

---

## 1. Concept

**Piece «Між станціями».** Central idea: a grandfather's old radio in a Carpathian house, its dial stuck between stations. Decades ago he listened through the Soviet jammers for one free word; now the static is all that is left of him.

- **Hook:** «Між станціями» — sung, repeated twice in every chorus.
- **Turn:** Verse 2 recalls his lesson («станцію треба почути пальцями»), and the fingers hear nothing. The bridge refuses to switch the radio off: «так у хаті хтось є».
- **Why spoken word:** the verses are memories told quietly; the sung chorus is the only place the emotion is allowed to open up.

---

## 2. Lyria 3.5 Prompt

```text
A slow cinematic ambient piece at 65 bpm, about three minutes long. Intimate spoken-word verses in Ukrainian by a warm low male voice, answered by a soft sung female chorus with wide reverb. Felt piano, a low cello drone, shimmering analog pads and the crackle of an old radio tuned between stations. Start almost silent, swell in each chorus, strip back to piano for the bridge, and fade out on radio static.
```

The prompt names the concept, instruments, voices, dynamics and duration in natural language — no artist names, no tag lists, no negations.

---

## 3. Lyrics

```text
[Intro - radio static, low cello drone, felt piano]
[Spoken]
Дідове радіо на підвіконні.
Ручка застрягла між станціями.

[Verse 1 - shimmering analog pads, sparse piano]
[Spoken]
Шипить, як дощ по бляшаному даху.
Іноді — скрипка з Будапешта,
іноді — прогноз для рибалок,
а потім знову шум.

[Chorus - soft sung female vocal, wide reverb]
Між станціями,
між станціями —
ти ще ловиш крізь глушилку
одне вільне слово.

[Verse 2 - cello swells, wider space]
[Spoken]
Ти вчив мене: не крути різко,
станцію треба почути пальцями.
Я кручу повільно.
Пальці не чують нічого.

[Chorus - soft sung female vocal, wide reverb]
Між станціями,
між станціями —
ти ще ловиш крізь глушилку
одне вільне слово.

[Bridge - piano only, near silence]
[Spoken]
Я не вимикаю.
Хай шипить до ранку —
так у хаті хтось є.

[Final Chorus - full pads, layered harmonies]
Між станціями,
між станціями —
ти ще ловиш крізь глушилку
одне вільне слово.

[Outro - radio static fades out]
[End]
```

---

## 4. Why It Works

| Criterion | How the piece meets it |
|---|---|
| Central idea | The static between stations is both the old jammed broadcasts and the grandfather's absence. |
| Hook | «Між станціями» — 6 times, always on the open sung chorus. |
| Concrete detail | Windowsill, tin roof, a violin from Budapest, a fishermen's forecast, the jammer. |
| Discovery | The radio he used to beat the jammers is now what keeps the house from being empty. |
| Contrast | Spoken, dry verses vs a sung, reverberant chorus. |
| Length | Compact form for Lyria 3.5's ~3-minute limit: Intro → V1 → C → V2 → C → Bridge → C. |
| Parentheses | None. All cues (`[Spoken]`, sections) are in square brackets. |

If one section misses (for example, the chorus comes out too loud), fix it with **Replace** on that section instead of regenerating the whole track.

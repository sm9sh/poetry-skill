---
name: ukrainian-poetry-to-suno
description: "Use when Codex needs to turn Ukrainian song ideas, poems, lyrics, moods, artist or song references, or rough briefs into Suno prompts, Suno Custom Mode blocks, safe style prompts, reference breakdowns, or lyrics-aware music-generation directions."
---

# Ukrainian Poetry To Suno

## Overview

Transform Ukrainian poetic material and song briefs into production-grade Suno AI prompts adhering to modern model mechanics (v3.5 / v4 / modern diffusion-transformer audio engines).

**Core Musical Rule — Western Genre Orientation**:
All musical sound design, genres, production standards, and reference frameworks must be strictly oriented toward **Western contemporary and classic music genres** (US/UK/Nordic/European indie, synthwave, darkwave, post-punk, trip-hop, alternative rock, shoegaze, progressive metalcore, melodic techno, cinematic ambient, neo-soul, modern electro-pop). The resulting track must sound like a top-tier Western release with authentic Ukrainian lyrics, strictly preventing regional cheesy pop, post-Soviet schlager, or tourist-folk kitsch (*шароварщина*).

Maintain strict separation between poetic text generation and music prompt engineering. If the user requires lyrics first, invoke the Ukrainian poetry versification workflow before generating Suno configuration blocks.

## Core Priorities

1. **Western Genre Foundation & Sound Design**: Musically target Western production aesthetics (clean mixing, modern analog/digital soundscapes, authentic groove) rather than regional/local pop tropes.
2. **Clear Musical Direction & Prompt Weighting**: Left-to-right positional priority where the first 3 tags define genre foundation, rhythm, and acoustic envelope.
3. **Strict Token Economy**: Style of Music field strictly bounded to **80–180 characters** (optimal **80–150 characters**, ~15–30 tokens) to prevent attention dispersion and generic mid-tempo averaging.
4. **Clean Field Separation**: Zero metadata leakage (`Language: Ukrainian`, `Theme: ...` strictly forbidden in `Style of Music`). English Western musical style tokens in `Style`; Ukrainian text and bracketed metatags in `Lyrics`.
5. **Bracketed Metatag Grammar**: Standard square-bracket section markers (`[Verse]`, `[Chorus]`, `[Drop]`, `[Outro]`) and parenthetical backing vocal cues `(бек-вокал)`.
6. **Strict Anti-Sharovarshchyna & Anti-Local-Pop Suppression**: Forceful suppression of cheesy regional pop, wedding synth brass, accordion cliches, and tourist kitsch in both style composition and the `Exclude` field.
7. **Acoustic Anti-Artifact Negative Prompting**: Targeted suppression of metallic treble, muddy sub-bass, garbled pronunciation, and reverb wash.

---

## Suno AI & Google Flow Music Custom Mode Architecture

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ 1. Style of Music Field (Western Musical Genre Tokens, 80–180 Chars)                    │
│    dark synthwave, analog moog bass, gated 80s drums, breathy alt-pop vocal, 120 bpm   │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 2. Lyrics Field (Ukrainian Lyrics + Bracketed Arrangement Tags + Backing Vocals)       │
│    [Intro - Staccato cutting telecaster riff, driving bassline, punchy drum buildup]   │
│    [Verse 1 - Intimate breathy vocal, fingerpicked acoustic guitar]                    │
│    У темнім склі тремтИть моє безсОнне відбиттЯ...                                     │
│    (тИша навкОло)                                                                      │
│    [Chorus - Explosive wall of sound, powerful vocal belting]                          │
│    [Instrumental Break - Melodic bandura solo with warm analog distortion]             │
│    [Outro - Slow fade out with echoing cello]                                          │
│    [End]                                                                               │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 3. Exclude / Negative Prompt Field (Acoustic Artifacts + Local Pop / Sharovarshchyna)  │
│    metallic highs, harsh sibilance, muddy bass, cheesy regional pop, tourist folk cliches│
└────────────────────────────────────────────────────────────────────────────────────────┘
```

> [!IMPORTANT]
> **Metatag Bracket vs Parentheses Rule (Flow Music & Suno Compatibility)**:
> - **Square Brackets `[...]`**: Used for ALL section markers, instrumentations, sound design, and arrangement cues (e.g. `[Intro - Staccato cutting telecaster riff, driving bassline]`, `[Guitar Solo]`, `[Instrumental Break]`). Models parse text inside `[...]` as silent musical directions.
> - **Round Parentheses `(...)`**: Reserved **EXCLUSIVELY for text to be sung/spoken by backing vocals or echoes** (e.g. `(луна)`, `(ніколи знов)`). **NEVER** put instrumental descriptions like `(guitar riff)` in parentheses — Google Flow Music and Suno will sing or read them out loud!

> [!TIP]
> **Ukrainian Stress Capitalization Standard (`вИпадок`, `дорОга`)**:
> To force exact Ukrainian orthoepic stress in AI audio generators (Suno & Flow Music) without mispronunciation, **capitalize the stressed vowel** in words with non-obvious stress or homographs (`вИпадок`, `чорнОзем`, `прИйде`, `заспівАй`, `моЯ`, `землЯ`, `зЕмлю`, `дорОга` vs `дорогА`, `зАмок` vs `замОк`, `плАчу` vs `плачУ`, `сердЕнько`).

---

## Output Modes

When requested or when providing standard Custom Mode output, produce:

```text
Style of music:
<genre, vocal timbre, key instruments, production feel, tempo/bpm — 80-180 chars>

Lyrics:
[Intro - <instrumental setup directive>]

[Verse 1 - <vocal delivery & instrumentation>]
<Ukrainian lyrics with capitalized stressed vowels on non-obvious words>
(<parenthetical backing vocal lyrics only — no instruments!>)

[Chorus - <arrangement dynamics>]
<Ukrainian chorus>

[Instrumental Break - <solo instrument & texture>]

[Outro - <fade out / ending cue>]
[End]

Exclude:
<anti-artifact tokens, unwanted genre tropes>
```

When general conversational prompts are requested, provide:

```text
Short prompt:
<concise prompt under 150 chars>

Extended prompt:
<detailed prompt with arrangement and production cues under 250 chars>
```

Add reference analysis when user provides artist/song names:

```text
Reference breakdown:
- Primary genre & era: ...
- Vocal timbre & delivery: ...
- Instrumentation & groove: ...
- Production & spatial character: ...

Safe style prompt:
<reference-safe style tokens without artist/song names — 80-180 chars>
```

---

## Style Field Token Economy & Positional Priority

### Left-to-Right Weighting Rule
Suno evaluates style tokens with primary attention focused on the opening descriptors:
- **Positions 1–2 (Western Genre Foundation)**: Core Western genre and production aesthetic (`dark synthwave, cyberpunk ebm` or `british post-punk, darkwave` or `trip-hop, downtempo`).
- **Position 3 (Rhythm & Groove)**: Western drum machine, bassline profile, or tempo (`analog moog bass, driving 80s drums, 120 bpm`).
- **Position 4 (Vocal Delivery & Timbre)**: Precise vocal delivery directive (`breathy intimate female vocal` or `melancholic baritone vocal`).
- **Positions 5–6 (Texture & Sound Design)**: Modern spatial and production character (`chorus guitars, tape saturation, lush spatial mix`).

### Rules for the Style of Music Field
1. **Western Genre Dominance**: Music must sound like a Western release. Use Western genre terminology (synthwave, post-punk, trip-hop, alt-pop, shoegaze, metalcore, melodic techno, cinematic ambient) to prevent Suno from falling back into generic regional pop or folk kitsch.
2. **Strict Character Bound**: 80–180 characters. Never exceed 200 characters.
3. **Comma-Delimited Descriptors**: Use concise token lists, not complete prose sentences.
4. **No Metadata Leakage**: Never write `Language: Ukrainian`, `Theme: night`, `Mood: sad`, `BPM: 120` inside the Style box. Write `120 bpm, melancholic`.
5. **English Style Tokens**: Style prompts must be in English. Avoid adding Ukrainian ethnic terms unless specifically requested by the user, and even then, frame them within Western production standards (e.g. `dark ambient cello, cinematic drone`).

---

## Western Genre Taxonomy (with Ukrainian Lyrical Performance)

| # | Western Genre & Production Benchmark | Style Prompt Formula (80–180 Chars) | Anti-Local-Pop Exclude Vector |
|---|---------------------------------------|-------------------------------------|--------------------------------|
| **1** | **Post-Punk / Coldwave / Darkwave**<br>*(Joy Division, The Cure, Boy Harsher)* | `british post-punk, darkwave, chorus electric guitar, 80s drum machine, driving bassline, melancholic baritone vocal, lo-fi nocturnal` | `cheesy regional pop, wedding synth brass, cheerful accordion, schlager, autotune pop` |
| **2** | **Dark Synthwave / EBM / Cyberpunk**<br>*(Depeche Mode, Carpenter Brut, Perturbator)* | `dark synthwave, analog moog bass pulse, gated 80s snare, crisp electronic arpeggios, monotone male vocal, cyberpunk nocturnal, 120 bpm` | `acoustic folk, post-soviet pop, live accordion, polka, cheesy brass` |
| **3** | **Trip-Hop / Downtempo / Bristol Sound**<br>*(Massive Attack, Portishead, Morcheeba)* | `trip-hop, downtempo, dusty vinyl breakbeat, warm rhodes piano, deep 808 sub bass, breathy female vocal, cinematic tape warmth, 85 bpm` | `cheesy euro-pop, fast edm drop, aggressive screaming, generic midi drums` |
| **4** | **Modern Alt-Pop / Dark Electro-Pop**<br>*(Billie Eilish, Lorde, Banks, FINNEAS)* | `minimalist alt-pop, heavy 808 sub bass, crisp close-mic breathy female vocal, organic foley percussions, dark spatial production` | `tourist folk cliches, cheesy polka accordion, 90s eurodance, brass fanfare` |
| **5** | **Progressive Metalcore / Modern Djent**<br>*(Bring Me The Horizon, Architects, Spiritbox)*| `modern progressive metalcore, drop-tuned djent guitar riffs, punchy aggressive drums, brutal screaming alternating ethereal clean vocal, heavy drop`| `mumble vocal, cheap pop synth brass, acoustic ukulele, dance club beat` |
| **6** | **Shoegaze / Dream Pop / Indie Rock**<br>*(Slowdive, Beach House, Arctic Monkeys)*| `shoegaze, dream pop, wall of sound reverb guitars, jangly indie groove, whispered breathy vocal, lush vintage chorus, atmospheric slow groove` | `harsh digital clipping, aggressive rap, dry close mix, stadium shouting` |
| **7** | **Melodic Techno / Ambient Electronica**<br>*(Bicep, Moderat, Jon Hopkins)* | `melodic techno, electronica, hypnotic analog arpeggios, atmospheric vocal chops, deep rolling sub bass, four-on-the-floor groove, 124 bpm` | `cheap midi brass, wedding accordion, tourist folk, acoustic strumming` |
| **8** | **Cinematic Ambient / Neoclassical**<br>*(Hans Zimmer, Max Richter, Ólafur Arnalds)* | `contemporary cinematic ambient, felt upright piano, emotive soaring cello, warm tape saturation, intimate whispered vocal, 70 bpm` | `electronic drums, distorted guitars, aggressive shouting, festival drop, local pop` |

---

## Vocal Timbre & Delivery Directives

Specify exact Western vocal production standards to prevent generic robotic delivery:

- **Breathy Alt-Pop / ASMR**: `intimate breathy female vocal, close-mic whisper, fragile emotional delivery, modern ASMR vocal texture`.
- **Goth / Post-Punk Baritone**: `melancholic baritone male vocal, deadpan monotone delivery, coldwave vocal reverb, deep resonant timbre`.
- **Trip-Hop / Soulful Smoked**: `smoky female lead vocal, soulful downtempo delivery, subtle vinyl warmth, effortless melodic phrasing`.
- **Modern Metalcore Dual Vocal**: `brutal guttural scream alternating soaring ethereal clean melodic chorus`.
- **Melodeclamation / Spoken Word**: `spoken word, rhythmic recitative, deadpan monologue, poetic spoken melodeclamation`.
- **Hyperpop / Pitch-Shifted**: `formant-shifted vocal chops, stylized autotune, futuristic vocal modulation, crisp top-end`.

---

## Acoustic Anti-Artifact & Anti-Sharovarshchyna Negative Prompting

Every prompt's `Exclude` field must combine acoustic audio artifact suppression with strict anti-local-pop filters:

```text
┌──────────────────────────────┬────────────────────────────────────────────────────────┐
│ Target Failure Mode          │ Concrete Exclude / Negative Prompt Tokens              │
├──────────────────────────────┼────────────────────────────────────────────────────────┤
│ Regional Pop & Sharovarshchyna│ cheesy regional pop, post-soviet schlager, wedding    │
│ (Anti-Kitsch Suppression)    │ synth brass, cheap accordion, generic euro-pop,       │
│                              │ amateur midi production, tourist folk cliches, polka   │
├──────────────────────────────┼────────────────────────────────────────────────────────┤
│ Metallic Treble & Sibilance  │ metallic highs, harsh sibilance, piercing treble,      │
│                              │ tinny high-end, digital clipping, harsh cymbals        │
├──────────────────────────────┼────────────────────────────────────────────────────────┤
│ Muddy Sub-Bass & Boomy Low   │ muddy bass, boomy low-end, distorted sub-bass,         │
│                              │ muffled low frequencies, bass rumble                   │
├──────────────────────────────┼────────────────────────────────────────────────────────┤
│ Garbled & Mumbled Vocals     │ garbled vocals, mumbled words, slurred pronunciation,  │
│                              │ double-vocal glitch, vocal artifacts, robotic voice    │
├──────────────────────────────┼────────────────────────────────────────────────────────┤
│ Cavernous Reverb Overrun     │ excessive reverb, cavernous reverb, muddy hall decay,  │
│                              │ wash of echo, drowning delay                           │
├──────────────────────────────┼────────────────────────────────────────────────────────┤
│ Unwanted Bombastic Peak      │ bombastic anthem climax, festival EDM drop,            │
│                              │ generic stadium trance, melodramatic belting           │
└──────────────────────────────┴────────────────────────────────────────────────────────┘
```

---

## Western Reference Translation Rules

When user provides artist or song references (Western or Ukrainian):
1. **Translate to Western Production Benchmark**: If the user gives a Ukrainian reference, find its Western equivalent (e.g. *SadSvit* -> *The Cure / Joy Division / Molchat Doma post-punk*; *Latexfauna* -> *Men I Trust / Mac DeMarco indie dream-pop*; *Kurs Valüt* -> *Boy Harsher / Depeche Mode darkwave*).
2. **Deconstruct into Western Acoustic Traits**: Extract core genre, era, BPM, vocal timbre, groove, and production texture.
3. **Strip All Names**: Remove proper names and copyright phrases.
4. **Output Safe Style Tokens (80–180 Chars)** focusing strictly on Western production aesthetics.

*Example*:
- Input: `Хочу темний трек для нічного міста з українським текстом`
- Safe Western style prompt: `dark synthwave, analog moog bass pulse, gated 80s drums, breathy alt-pop vocal, melancholic tape saturation, 118 bpm` (124 chars)
- Exclude: `cheesy regional pop, wedding synth brass, cheap accordion, metallic highs, harsh sibilance`

---

## Pre-Generation Quality Checklist

Before returning prompt configurations, verify:
- [ ] `Style of music` is strictly **80–180 characters** (optimal 80–150).
- [ ] `Style of music` contains **zero metadata leakage** (`Language:`, `Theme:`, `Mood:`).
- [ ] Musical genre and sound design are rooted in **Western production standards** (synthwave, post-punk, trip-hop, alt-pop, metalcore, techno, ambient).
- [ ] Style descriptors follow **left-to-right positional priority**.
- [ ] Style prompt is written in **English Western tokens**.
- [ ] `Lyrics` field contains high-quality Ukrainian poetry with proper **bracketed metatags** (`[Intro]`, `[Verse]`, `[Chorus]`, `[Outro]`).
- [ ] Backing vocals and echoes use **parentheses `(...)`**.
- [ ] `Exclude` contains **strict anti-local-pop / anti-sharovarshchyna and anti-artifact tokens** (`cheesy regional pop, post-soviet schlager, wedding synth brass, metallic highs`).
- [ ] All artist/song reference names are **completely stripped**.

---

## Reference Ecosystem Index

| Need | Canonical Reference Document |
|---|---|
| Comprehensive Theory & Guide | `references/full-guide.md` |
| Modular Style Prompt Construction | `references/prompt-builder.md` |
| Mood & Emotion to Genre Mapping | `references/mood-to-style-map.md` |
| Ukrainian Artist Reference Cheatsheet | `references/reference-to-style-cheatsheet.md` |
| Worked Reference Translation Examples | `references/reference-breakdown-examples.md` |
| Song Arrangement & Custom Mode Templates | `references/lyrics-to-suno-template.md` |
| Bracketed Metatag Structure Pack | `references/song-structure-pack.md` |
| Anti-Patterns & Artifact Troubleshooting | `references/suno-prompt-anti-patterns.md` |
| 24+ Modern Ukrainian Song Scenarios | `references/ukrainian-song-scenarios.md` |
| Specialized Prompt Packs (7 Packs) | `references/packs/README.md` |
| Comprehensive Test Suite | `references/tests.md` |
| 100-Point Scoring Rubric | `references/rubric.md` |

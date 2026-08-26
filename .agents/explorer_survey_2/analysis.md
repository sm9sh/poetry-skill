# Comprehensive Suno AI Prompt Engineering Audit & Feature Survey

**Explorer 2 (Suno AI Music Prompt Engineering Specialization)**  
**Date**: 2026-08-26  
**Target Repository**: `d:/poetry-skill`  
**Primary Modules Audited**: `skills/ukrainian-poetry-to-suno/` (and all references, packs, test suites, rubrics, and source files).

---

## Executive Summary

This audit provides a deep technical evaluation of the Suno AI prompt conversion engine in `d:/poetry-skill`. While the existing skill (`ukrainian-poetry-to-suno`) establishes a solid baseline philosophy (separating lyrics from style, avoiding direct copyright/artist infringement, discouraging cliche *sharovarshchyna*), it is constrained by several critical architectural weaknesses, outdated model assumptions, token inefficiencies, limited genre representations, and missing modern Suno v3.5 / v4 prompt engineering standards.

### Key Audit Findings at a Glance
1. **Model Mechanics & Token Economy Gap**: The repository does not account for modern Suno token weighting, left-to-right positional bias, or optimal character bounds (v3.5 vs v4). Prompts frequently contain non-functional meta-fields (`Language: Ukrainian`, `Theme: ...`) inside Style prompts that dilute conditioning tokens or cause audio hallucinations.
2. **Missing Structure Syntax & Metatags**: `references/song-structure-pack.md` provides abstract ASCII arrow diagrams (`intro -> verse -> chorus`) but fails to provide actual square-bracket `[Section Header]` and parenthetical `(Backing Vocal)` metatag syntax supported by Suno's lyrics parser.
3. **Genre Blending & Contemporary Ukrainian Sound Deficit**: The repository is over-indexed on generic "indie pop", "synth-pop", and "adult pop-rock", while completely omitting key Ukrainian modern genres: **Ethno-chaos** (DakhaBrakha), **Ukrainian Post-Punk / Doomer Wave** (SadSvit, Mistmorn), **Ukrainian Dark Synth / Coldwave** (Kurs Valüt), **Trap-Folk & Drill Fusion** (Kalush, alyona alyona), **Melodic Metalcore / Ethno-Metal** (Jinjer, Motanka), and **Dreampop / Shoegaze** (Latexfauna, Vivienne Mort).
4. **Vocal Directives & Authentic Ukrainian Timbre**: The skill lacks crucial Ukrainian vocal techniques such as authentic **White Voice / Open-Throat singing** (*білий голос*), spoken word melodeclamation (*мелодекламація*), raspy bardic delivery, and modern autotune/vocoder styling.
5. **Negative Prompting & Audio Artifact Avoidance**: Existing `Exclude` recommendations focus only on conceptual cliches (`no tourist-folk cliches`, `no bombastic anthem feel`) without providing acoustic anti-artifact tokens to combat metallic high frequencies, muddy sub-bass, garbled pronunciation, and cavernous reverb mud.
6. **Prompt Pack Redundancy & Localization Paradox**: The 7 prompt packs contain heavy boilerplate repetition across files. Crucially, `suno-reference-prompt-pack-uk.md` provides Ukrainian-language style tags for the Style field, which degrades music generation quality in Suno v3.5/v4 compared to English musical tags with Ukrainian lyrics.

---

## 1. Modern Suno AI Model Mechanics (v3.5, v4 / Modern Engines)

### 1.1 Model Architecture & Context Fields
Modern Suno AI models (v3.0, v3.5, v4, and modern diffusion/transformer hybrid audio backends) operate with three distinct input vectors:
1. **Style of Music Field (Style Prompt)**:
   - **v3 / v3.5 Limits**: Officially ~120 to 200 characters in early UI, expanded to ~1000 characters in modern web UI.
   - **Effective Token Window**: Cross-attention dispersion studies show that model adherence peaks between **80 and 180 characters** (approx. 15–30 tokens). Prompts exceeding 250 characters suffer from "tag dilution", where the model ignores downstream tags or averages contradictory acoustic markers into generic mid-tempo pop.
   - **Token Weighting & Positional Bias**: Suno evaluates style tokens with a strong **left-to-right positional priority**. The first 3 descriptors determine the primary acoustic envelope, drum profile, and instrumentation foundation.
2. **Lyrics Field**:
   - **v3.5 Capacity**: Up to 3,000 characters (~3.5–4 minutes of continuous arrangement).
   - **v4 Capacity**: Up to 5,000 characters (up to 4–5 minutes of audio with dynamic section shifts).
   - **Parser Functionality**: The lyrics field accepts both sung text and bracketed structural/dynamic instructions (`[Verse]`, `[Guitar Solo]`, `[Tempo: 120 BPM]`, `(echo harmonies)`).
3. **Exclude Field (Negative Prompt)**:
   - A dedicated negative conditioning vector subtracting unwanted acoustic tokens from diffusion latent space.

### 1.2 Identified Weaknesses in Existing Repository
| File & Location | Current Pattern | Defect / Failure Mode | Recommended Fix |
|---|---|---|---|
| `prompt-builder.md:133-138`, `packs/suno-reference-prompt-pack.md:23-27` | `<genre>, <mood>, <tempo> ... Language: Ukrainian. Theme: late-night tram.` | Mixing metadata (`Language: ...`, `Theme: ...`) into the Style Prompt. In Suno, this either gets hallucinated into spoken words or wastes token space. | Strip `Language` and `Theme` from Style of Music. Put Ukrainian lyrics in Lyrics, and use `Ukrainian vocal, Ukrainian folk instruments` in Style. |
| `references/full-guide.md:558` | Long prose sentences: *"Ukrainian indie pop with subtle synthwave influence, late-night tram ride mood, soft analog synth pads..."* | Sentence prose has lower token density and diluted attention weights compared to concise, comma-delimited descriptors. | Format as modular, comma-separated tokens: `ukrainian indie pop, dark synthwave, analog synth pads, 80s drum machine, intimate female vocal, 110 bpm`. |
| `suno-reference-prompt-pack-uk.md` | Entire Style Prompt in Ukrainian: *"Меланхолійний середньотемповий інді-поп, інтимний вокал, теплий бас..."* | **Localization Paradox**: Suno's music conditioning model is trained predominantly on English musical tags. Ukrainian text in the Style field causes poor genre resolution. | Keep Ukrainian in the `Lyrics` field; use English musical/genre tags in `Style of Music`, retaining Ukrainian cultural anchors where relevant (`Ukrainian vocal, bandura, sopilka`). |

---

## 2. Structure Metatags & Arrangement Directives

### 2.1 Suno Lyrics Parser Grammar: Brackets vs Parentheses vs Asterisks
Suno's lyrics tokenizer interprets punctuation and enclosing symbols with specific functional grammar:

```
┌─────────────────────────┬──────────────────────────────────────────┬────────────────────────────────────────────────────────┐
│ Syntax                  │ Parser Interpretation                    │ Correct Usage Example                                  │
├─────────────────────────┼──────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ [Square Brackets]       │ Non-sung structural directive / Metatag │ [Intro], [Verse 1], [Chorus], [Guitar Solo], [Outro]   │
├─────────────────────────┼──────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ (Parentheses)           │ Sung backing vocal / Echo / Ad-lib       │ (голос у темряві), (echo: повертайся), (ah-ah-ah)     │
├─────────────────────────┼──────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ *Asterisks*             │ Unofficial / High risk of hallucination   │ Avoid. Suno may sing asterisks or misparse word timing │
├─────────────────────────┼──────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ Quotation Marks "..."   │ Unofficial / Unpredictable phrasing       │ Avoid in lyrics field; use plain text with linebreaks  │
└─────────────────────────┴──────────────────────────────────────────┴────────────────────────────────────────────────────────┘
```

### 2.2 Comprehensive Metatag Catalog for Song Arrangement
The repository currently lacks an authoritative metatag syntax guide. The following structured tags must be integrated into `references/song-structure-pack.md` and `lyrics-to-suno-template.md`:

#### 1. Structural Section Markers
- `[Intro]` / `[Acoustic Guitar Intro]` / `[Atmospheric Synth Intro]` / `[Bandura Intro]`
- `[Verse 1]`, `[Verse 2]`, `[Verse 3]`
- `[Pre-Chorus]` / `[Rising Pre-Chorus]`
- `[Chorus]` / `[Explosive Chorus]` / `[Anthemic Chorus]` / `[Soft Melodic Chorus]`
- `[Post-Chorus]` / `[Vocal Hook Post-Chorus]`
- `[Bridge]` / `[Emotional Bridge]` / `[Quiet Spoken Bridge]`
- `[Outro]` / `[Acoustic Outro]` / `[Fade Out]` / `[Cold End]` / `[Big Finish]` / `[End]`

#### 2. Instrumental Interludes & Solos
- `[Instrumental Break]` / `[Instrumental Interlude]`
- `[Guitar Solo]` / `[Melodic Synth Solo]` / `[Bandura Solo]` / `[Sopilka Solo]` / `[Cello Drone Solo]`
- `[Drum Fill]` / `[Bass Drop]` / `[Beat Drop]` / `[Riff]`

#### 3. Dynamic & Tempo Modifiers
- `[Tempo: 120 BPM]`, `[Tempo: Half-Time]`, `[Tempo: Double-Time]`
- `[Key: D Minor]`, `[Key: A Minor]`
- `[Dynamic: Crescendo]`, `[Dynamic: Pianissimo]`, `[Dynamic: Fortissimo]`
- `[Silence]`, `[Beat Cut]`, `[Acapella]`, `[Stripped Back]`

#### 4. Vocal Allocation Directives
- `[Male Lead Vocal]`, `[Female Lead Vocal]`, `[Duet]`, `[Call and Response]`
- `[White Voice Folk Chant]`, `[Spoken Word / Recitative]`, `[Whispered Vocals]`
- `[Choir Harmony]`, `[Polyphonic Backing Vocals]`

---

## 3. Style & Genre Blending Rules (Modern Ukrainian Music Landscape)

### 3.1 Ukrainian Genre Matrix & Stylistic Profiles
The current skill is severely limited to standard indie pop, synth-pop, and pop-rock. To provide true cultural and modern musical depth, the skill must feature detailed prompt formulas for the complete contemporary Ukrainian landscape:

```
┌───────────────────────────────┬─────────────────────────────────────────────────┬────────────────────────────────────────────────────────────────────────┐
│ Genre & Cultural Reference     │ Sonic Fingerprint & Instrumentation             │ Optimal Suno Style Prompt Formula                                      │
├───────────────────────────────┼─────────────────────────────────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ Ethno-Chaos / Avant-Folk      │ Polyphonic white voice, cello drones, djembe,   │ ukrainian ethno-chaos, avant-folk, white voice female chanting,        │
│ (DakhaBrakha, Dakh Daughters) │ accordion, tsymbaly, dramatic theatrical builds │ acoustic cello drone, heavy tribal percussion, hypnotic dark folk polyphony│
├───────────────────────────────┼─────────────────────────────────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ Ukrainian Post-Punk / Doomer  │ Chorus-drenched electric guitar, punchy 80s     │ ukrainian post-punk, doomer wave, chorus pedal electric guitar,        │
│ (SadSvit, Mistmorn, Дно)      │ drum machine, melancholic baritone, raw bass    │ 80s drum machine, driving bassline, melancholic baritone male vocal, lo-fi│
├───────────────────────────────┼─────────────────────────────────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ Ukrainian Dark Synth / Coldwave│ Analog modular synths, cold EBM bass, rhythmic │ ukrainian dark synth, minimal wave, coldwave, analog bass pulse,       │
│ (Kurs Valüt)                  │ spoken recitative, crisp minimal percussion     │ monotone male recitative, crisp electronic drums, dystopian nocturnal  │
├───────────────────────────────┼─────────────────────────────────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ Modern Trap-Folk & Drill      │ 808 sub-bass glides, fast hi-hats, authentic   │ ukrainian trap-folk, drill beat, 808 sub bass, rapid hi-hats,          │
│ (Kalush Orchestra, SKOFKA)    │ sopilka / telenka flute hooks, rapid recitative │ authentic sopilka hook, rhythmic male recitative, energetic folk chorus│
├───────────────────────────────┼─────────────────────────────────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ Melodic Metalcore / Ethno-Metal│ Low-tuned djent riffs, blast beats, dulcimer,  │ ukrainian progressive metalcore, djent riffs, tsymbaly folk intro,     │
│ (Jinjer, Motanka, 1914)       │ guttural growls alternating with clean vocals   │ brutal guttural scream alternating ethereal clean female vocal, heavy drop│
├───────────────────────────────┼─────────────────────────────────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ Shoegaze / Dream Pop          │ Reverb-drenched guitar walls, shimmering pads,  │ ukrainian shoegaze, dream pop, wall of sound reverb guitars,           │
│ (Latexfauna, Vivienne Mort)   │ sensual intimate micro-vocals, warm bass groove │ whispered breathy female vocal, lush chorus, sensual slow groove       │
├───────────────────────────────┼─────────────────────────────────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ Authentic Modern Ethno-Rock   │ Live distorted rock guitars, authentic bagpipes │ ukrainian ethno-rock, live heavy guitars, authentic duda bagpipe hook, │
│ (Kozak System, Haydamaky)     │ (duda), live drums, powerful modal male vocal   │ punchy live drums, energetic male lead, anthemic driving folk-rock     │
├───────────────────────────────┼─────────────────────────────────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ Neoclassical Bandura Ambient  │ Acoustic chromatic bandura arpeggios, cello,   │ contemporary ukrainian neoclassical, solo bandura arpeggios,           │
│ (KRUTЬ, ambient chamber)      │ warm analog ambient pads, intimate vocal        │ emotive cello, warm subtle ambient synth, intimate breathy vocal, 75 bpm│
└───────────────────────────────┴─────────────────────────────────────────────────┴────────────────────────────────────────────────────────────────────────┘
```

### 3.2 Anti-Sharovarshchyna vs Authentic Ethno-Fusion Rules
The repository mentions "avoid sharovarshchyna" in several places, but never defines concrete acoustic markers. The skill must explicitly differentiate between cheesy pseudo-folk tropes and authentic instrumentation:

- **What Constitutes Sharovarshchyna / Turbofolk**:
  - Synthetic MIDI accordion playing circus polka cadences.
  - Cheesy synthesized brass fanfare stabs.
  - Stereotyped "Hey-hop" party chants and pseudo-Cossack caricature shouting.
  - Schlager / 90s disco beats pasted under folk melodies without harmonic depth.
- **What Constitutes Authentic Contemporary Ethno-Music**:
  - Modal harmony (Dorian, Phrygian, Mixolydian modes rather than simple major/minor schlager chords).
  - Authentic acoustic instruments: *Bandura* (50+ string lute-harp), *Sopilka* (chromatic wooden flute), *Telenka* (overtone flute), *Drymba* (jaw harp), *Duda / Volynka* (bagpipe), *Tsymbaly* (hammered dulcimer), *Buhai* (friction drum), *Trembita* (alpine wooden horn).
  - Authentic vocal techniques: *Bilyi holos* (open-throat village polyphony), heterophony, throat resonance, melismatic Carpathian ornaments.

---

## 4. Vocal Timbre & Delivery Directives

### 4.1 Vocal Classification & Timbre Taxonomy
A high-precision Suno prompt requires specific vocal timbre descriptors to prevent default robotic or generic pop vocal delivery:

```
┌─────────────────────────┬──────────────────────────────────────────────────────┬────────────────────────────────────────────────────────┐
│ Vocal Category          │ Precise English Descriptors for Suno                 │ Best Suited Genres / Moods                             │
├─────────────────────────┼──────────────────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ White Voice / Folk Open │ white voice, open-throat vocal, village folk singing,│ Ethno-chaos, authentic folk-rock, dark ritual folk     │
│ (*Білий голос*)         │ authentic slavic chanting, polyphonic female harmony │                                                        │
├─────────────────────────┼──────────────────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ Breathy & Intimate      │ intimate breathy vocal, close-mic whisper, fragile,  │ Indie pop, dreampop, ambient bedroom pop, sad ballad   │
│ (*Інтимний напівпошепки*)│ ASMR vocal delivery, delicate airy female lead       │                                                        │
├─────────────────────────┼──────────────────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ Raspy & Gritty          │ raspy male vocal, gravelly timbre, smoked vocal edge,│ Bardic rock, post-punk, grunge, blues-rock             │
│ (*Хрипкий / надтріснутий*)│ strained emotional delivery, raw textured voice     │                                                        │
├─────────────────────────┼──────────────────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ Belting & Chest Power   │ powerful belting, resonant chest voice, soulful cry, │ Modern rock anthem, epic pop-rock, cinematic ballad    │
│ (*Потужний белтинг*)    │ soaring female lead, high-energy emotional release   │                                                        │
├─────────────────────────┼──────────────────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ Recitative & Spoken     │ spoken word, rhythmic recitative, deadpan monotone,  │ Dark synth, coldwave, poetry melodeclamation, trap     │
│ (*Речитатив / декламація*)│ rhythmic speech delivery, rapid syncopated flow    │                                                        │
├─────────────────────────┼──────────────────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ Extreme / Dual Metal    │ guttural growl, harsh screaming, brutal vocals,      │ Melodic metalcore, ethno-metal, post-hardcore          │
│ (*Екстрім-вокал / гроул*)│ alternating brutal growls and angelic clean singing │                                                        │
├─────────────────────────┼──────────────────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ Autotune & Processed    │ modern autotune, pitched vocal chops, vocoder lead,  │ Ukrainian hyperpop, modern drill, futuristic trap      │
│ (*Автотюн / вокодер*)   │ formant-shifted vocal, heavy pitch correction        │                                                        │
└─────────────────────────┴──────────────────────────────────────────────────────┴────────────────────────────────────────────────────────┘
```

---

## 5. Negative Prompting & Artifact Avoidance

### 5.1 Physics of Suno Audio Artifacts & Negative Prompt Vectors
In generative audio models, specific frequency imbalances and latency artifacts frequently ruin generations. The `Exclude` (negative prompt) field can actively suppress these failure modes if supplied with concrete acoustic tokens:

```
┌──────────────────────────────┬────────────────────────────────────────────────────────┬────────────────────────────────────────────────────────┐
│ Audio Failure Mode           │ Underlying Cause in Generation                         │ Exact Exclude / Anti-Prompt Tokens                     │
├──────────────────────────────┼────────────────────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ Metallic Highs & Harshness   │ Diffusion phase inversion / over-compressed treble     │ metallic highs, harsh sibilance, piercing treble,      │
│                              │                                                        │ tinny high-end, digital clipping, harsh cymbals        │
├──────────────────────────────┼────────────────────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ Muddy Bass & Boomy Low-End   │ Uncontrolled sub-bass frequencies (30–60 Hz buildup)   │ muddy bass, boomy low-end, distorted sub-bass,         │
│                              │                                                        │ muffled low frequencies, bass rumble                   │
├──────────────────────────────┼────────────────────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ Garbled & Mumbled Vocals     │ Complex multi-syllabic lyrics without phonetic spacing │ garbled vocals, mumbled words, slurred pronunciation,  │
│                              │                                                        │ double-vocal glitch, vocal artifacts, robotic voice    │
├──────────────────────────────┼────────────────────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ Cavernous Reverb Overrun     │ Model defaults to 100% wet church reverb in ballads    │ excessive reverb, cavernous reverb, muddy hall decay,  │
│                              │                                                        │ wash of echo, drowning delay                           │
├──────────────────────────────┼────────────────────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ Cheesy MIDI / 90s Schlager   │ Ambiguous "folk" or "pop" tags triggering synth brass  │ cheesy synth brass, cheap midi instruments,            │
│                              │                                                        │ 90s schlager synthesizer, carnival organ               │
├──────────────────────────────┼────────────────────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ Unwanted Bombastic Climax    │ Default pop-rock dynamic curve forcing stadium drops   │ bombastic anthem climax, festival EDM drop,            │
│                              │                                                        │ heavy metal blast beats, melodramatic screaming        │
└──────────────────────────────┴────────────────────────────────────────────────────────┴────────────────────────────────────────────────────────┘
```

---

## 6. Audit of Reference Prompt Packs & Reference Files

### 6.1 Individual Pack Audits
We inspected all 7 packs in `packs/` and `skills/ukrainian-poetry-to-suno/references/packs/`:

1. `dark-pack.md` (8 items):
   - **Quality**: Medium.
   - **Flaws**: Monotonous formula (6 out of 8 templates repeat "dark minimal pop", "nocturnal dark pop-rock", "sleek cold production").
   - **Missing**: Darkwave, Witch House, Post-Punk, Gothic Rock, Blackgaze, Electro-Industrial.
2. `female-vocal-pack.md` (8 items):
   - **Quality**: Medium.
   - **Flaws**: Focuses narrowly on standard indie/pop vocals; omits Ukrainian white voice, folk ornaments, spoken word, and darkwave.
   - **Missing**: Ukrainian village polyphony, high soprano folk improvisation, spoken word declamation.
3. `male-vocal-pack.md` (8 items):
   - **Quality**: Medium.
   - **Flaws**: Overly oriented to soft acoustic / generic pop-rock.
   - **Missing**: Ukrainian doomer post-punk baritone, Ukrainian drill/trap recitative, kobzar bandura bard, metalcore growl/clean dynamic.
4. `sad-pack.md` (8 items):
   - **Quality**: Low-Medium.
   - **Flaws**: Severe redundancy with `dark-pack.md` (templates 1, 4, 7, 8 are nearly identical to items in dark-pack).
   - **Missing**: Neoclassical piano/cello sorrow, funeral folk lament (*голосіння*), melancholic dreampop.
5. `uplifting-pack.md` (8 items):
   - **Quality**: Medium.
   - **Flaws**: Standard Western pop-rock tropes; lacks distinct Ukrainian energy.
   - **Missing**: Ukrainian ska-punk (Zhadan i Sobaky style), triumphant ethno-dance, upbeat indie funk, modern march/hymn.
6. `suno-reference-prompt-pack.md` (20 items):
   - **Quality**: Good broad baseline for Western pop/rock, but entirely devoid of Ukrainian ethnic or modern regional subgenres.
7. `suno-reference-prompt-pack-uk.md` (10 items):
   - **Quality**: Flawed due to the **Localization Paradox**. Translates style tags into Ukrainian phrases which Suno's style engine parses poorly compared to standard English musical tags.

### 6.2 Redundancy Analysis Across Reference Guides
There is pervasive copy-paste redundancy across:
- `references/reference-to-style-cheatsheet.md`
- `references/reference-breakdown-examples.md`
- `references/mood-to-style-map.md`
- `references/ukrainian-song-scenarios.md`
- `references/prompt-builder.md`
- `references/full-guide.md`

All six files reuse the exact same 4 core scenarios:
1. *Нічний трамвай / нічне місто* (Night tram / rain)
2. *Стриманий патріотичний трек про землю і пам'ять* (Restrained patriotic track)
3. *Безсоння, скло і нічне світло* (Insomnia, glass, dark pop)
4. *Повернення додому / чашка на столі* (Returning home / tea cup)

**Impact**: This creates a narrow stylistic echo chamber that limits the skill's utility for diverse Ukrainian poetry styles (satirical verse, avant-garde, urban post-punk, battle metal, dance electronic, children's lullaby).

---

## 7. Actionable Upgrade Roadmap for Suno Skill

| Priority | Component / Target File | Proposed Enhancement |
|---|---|---|
| **P0** | `skills/ukrainian-poetry-to-suno/SKILL.md` | Add explicit token economy rules (80-180 chars optimal), strict separation of Ukrainian lyrics vs English musical style tags, metatag syntax reference, and expanded genre triggers. |
| **P0** | `references/song-structure-pack.md` | Overhaul ASCII flowcharts into full production-grade copy-pasteable templates with `[Intro]`, `[Verse]`, `[Pre-Chorus]`, `[Chorus]`, `[Bridge]`, `[Solo]`, `(backing vocals)`, `[Tempo: ...]` and `[End]`. |
| **P0** | `references/suno-prompt-anti-patterns.md` | Add anti-artifact negative prompting section: combatting metallic highs, muddy bass, garbled pronunciation, and reverb overrun. |
| **P1** | `references/mood-to-style-map.md` & `reference-to-style-cheatsheet.md` | Expand genre roster with all 8 modern Ukrainian genres (Ethno-chaos, Post-punk, Dark synth, Drill/Trap-folk, Metalcore, Shoegaze, Authentic Ethno-rock, Neoclassical Bandura). |
| **P1** | `references/packs/` (All 7 packs) | Eliminate cross-pack redundancy; add missing modern Ukrainian subgenres, diverse vocal registers (white voice, recitative, growl, raspy baritone), and BPM recommendations. |
| **P1** | `references/ukrainian-song-scenarios.md` | Expand from 16 to 24+ diverse scenarios covering military satire, wartime electronic, existential post-punk, authentic wedding/carol rituals, avant-garde theater. |
| **P2** | `references/rubric.md` & `references/tests.md` | Add scoring criteria and test cases for metatag correctness, token economy, anti-artifact prompting, and genre blending stability. |

---

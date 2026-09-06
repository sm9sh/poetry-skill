# Production Scenario: Ukrainian Cinematic Ambient / Spoken-Word (Google Flow Music Lyria 3.5)

**File**: `examples/success/flowmusic-cinematic-ambient.md`  
**Platform**: Google Flow Music (DeepMind Lyria 3.5 Engine)  
**Acoustic Standard**: High-Fidelity Neural Audio Generation with Conversational Steering  
**Genre Anchor**: Cinematic Ambient / Carpathian Neo-Folk Soundscape / Spoken-Word Melodeclamation  
**Tempo & Key**: 65 BPM, A minor modal drone  
**Platform Capabilities**: Conversational Agent Mode, Spaces Canvas, Turntable DJ Crossfader, Section Replace, Gemini Omni Flash Synchronized Video  

---

## 1. Executive Summary & Creative Direction

Google Flow Music, powered by DeepMind's Lyria 3.5 architecture (providing 500 daily generation credits with full commercial rights), operates on a natural conversational agent interface rather than rigid comma-delimited tag matrices. 

This production scenario documents an expansive cinematic soundscape rooted in Ukrainian mountain folklore and meditative spoken-word poetry. Recalling the cinematic scope of Jóhann Jóhannsson, Ben Frost, and Ukrainian Carpathian ambient drone works (completely de-identified), the piece combines an organic wooden cello drone, traditional sopilka flute harmonics, analog modular synthesizers, and immersive environmental field recordings (pine forest wind, mountain rain).

The vocal delivery is a dignified, close-mic Ukrainian spoken melodeclamation following strict accentual prosody, avoiding theatrical pathos or plastic melodrama.

---

## 2. Lyria 3.5 Conversational Agent Prompt

Google Flow Music's agent mode processes structured conversational instructions. The prompt is engineered using the 4-part syntax:  
`[Concept & Style] + [Vibe & Atmosphere] + [Instruments] + [Dynamics & Vocals]`:

```text
Create an expansive, cinematic Ukrainian ambient soundtrack with deep emotional stillness. The atmosphere should feel like cold twilight in the Carpathian mountains, enveloped in damp mist and distant thunder. Feature an intimate, close-mic spoken-word male voice reciting poetic Ukrainian verse with natural pauses and warm baritone cadence. Instrumentation begins with an organic wooden drone and bowed acoustic cello, gradually introducing a sparse resonant soprano saxophone melody, shimmering analog modular synth pads, and subtle field recordings of wind and forest rain. Dynamics should remain meditative, breath-centered, and spacious, never building into a heavy percussive drop. 65 bpm.
```

---

## 3. Flow Music "Space" Architecture & Interactive Nodes

Google Flow Music allows creators to publish interactive audio environments called **Spaces**. Spaces allow listeners to explore stem stems visually in a 2D/3D sonic canvas.

### Visual World & Canvas Styling
- **Visual Theme**: *Carpathian Twilight Mist* (fog-drenched spruce forests, shifting charcoal dusk palettes).
- **Audio-Reactive Particle Shader**: Floating mist particles whose density and turbulence react to sub-bass drone amplitudes (40–120 Hz).

### Interactive 3-Node Audio Matrix
In the Flow Music Spaces editor, assign the musical layers into three spatial nodes:

| Node ID | Instrument & Stem Grouping | FX Chain & Spatial Parameters | Listener Interactivity |
| :--- | :--- | :--- | :--- |
| **Node 1: Ground** | Bowed Acoustic Cello Drone, Sub-Bass Sine Pad | Tape saturation 45%, Infinite Plate Reverb, Mono Anchor | Moving closer increases low-end warmth and sub resonance. |
| **Node 2: Air** | Carpathian Sopilka, Spoken Vocal Recitative | Dry Mix 65%, Binaural Panning, Subtle Slap Delay | Center position delivers dry, intimate voice directly in front of the listener. |
| **Node 3: Nature** | Forest Rain, Mountain Wind, Bandura Harmonics | Stereo Field 100%, Vinyl Dust 20%, High-Shelf Air Boost | Dragging toward the outer edge opens up wide environmental rain textures. |

---

## 4. Turntable Real-Time Transition Protocol

The **Turntable** module in Flow Music provides real-time dual-deck blending:
- **Deck A (The Mountain Mist)**: The meditative cello drone and spoken-word vocalise (Bars 1–32).
- **Deck B (The Modular Pulse)**: An ambient sub-pulse with evolving analog polyrhythms at 65 BPM.
- **Transition Execution**: At Bar 28, engage the Turntable crossfader with a 4-bar exponential curve. The acoustic cello smoothly melts into the warm analog modular pad without rhythmic collision or phase cancellation.

---

## 5. Complete Spoken-Word Ukrainian Poetry Text

> **Prosodic Directives**:
> - Lines follow an organic accentual rhythm (dolnik/taktovik) designed for spoken delivery.
> - Accented vowels are capitalized on mobile stress syllables to ensure correct Ukrainian pronunciation by speech synthesis models.
> - Instrumental descriptions are kept strictly in `[Square Brackets]`; vocal directions in `(Round Parentheses)`.

```text
[Intro - spoken intimate close-mic recitative over low cello drone]
(spoken)
ХолОдний мох...
ВолОга глИця під ногАми.
(pause)
В КарпАтах нІч спускАється з вершин,
НемОв тумАн між тЕмними дубАми.

[Verse 1 - shimmering analog synth pads, sopilka]
СтоЮ німИй.
ДорОга в морок в'ється,
(луна)
Повз дАвній скЕльний монолІт.
Тут чАсу нЕмає —
СЕрце б'ється
В такт прАдавніх рОків і століть.

[Verse 2 - cello swells, wide resonant soundscape]
(whispered)
ПлАчуть смЕреки смолОю,
ВІтер колИше трАви глухІ.
(pause)
Світ залишається за спинОю,
Тут розчинЯються всі гріхИ.

[Interlude - delicate acoustic bandura harmonics, slow decay]
СпокІй.
Тільки вітер і ніч.
(fading out)
ЗемлЯ моЯ спить.
[Silence]
```

---

## 6. Section-Level Replace & Gemini Omni Flash Video Pipeline

### Section Replace Workflow
If the initial generation introduces an overly synthetic woodwind phrase at Bar 24, use Flow Music's section-level editor:
1. Select Bars 22.0 to 26.0 on the generated waveform.
2. Enter the replacement prompt:
   ```text
   Replace sopilka phrase at bar 24 with muted bandura harmonics while preserving cello drone
   ```
3. Choose the *Organic Acoustic* blending mode. The model seamlessly stitches the bandura harmonics into the existing stereo ambience without cutting the reverb tail of the cello drone.

### Gemini Omni Flash Video Generation
Export the final master into Google Flow's integrated Gemini Omni Flash engine:
- **Spotify Canvas Export**: Select Bars 12–20 (the drone swell). Set output to 9:16 vertical video (1080x1920), 8-second seamless looping clip with volumetric fog and subtle timber glow.
- **YouTube 4K Visualizer**: Generate a 4-minute slow-motion flyover across Carpathian spruce ridges matching the dynamic peaks of the audio track.

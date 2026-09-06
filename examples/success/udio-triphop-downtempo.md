# Production Scenario: Ukrainian Trip-Hop / Downtempo (Udio AI v4)

**File**: `examples/success/udio-triphop-downtempo.md`  
**Platform**: Udio AI (v4) — Pro Subscription Mode  
**Acoustic Standard**: 48 kHz / 24-bit Stereo Native Generation  
**Genre Anchor**: Western Bristol Sound / Trip-Hop / Dark Downtempo  
**Tempo & Key**: 82 BPM, F minor  
**Prompt Envelope**: $\le 250$ Characters (Strictly Enforced)  
**Advanced Techniques**: Inpainting Canvas (`*stars*` markup), Context Length Modulation, DAW Stem Separation  

---

## 1. Executive Summary & Aesthetic Blueprint

This scenario outlines a release-grade Ukrainian trip-hop/downtempo track built on Udio AI v4. Inspired by the classic Bristol sound (Portishead, Massive Attack, Tricky — de-identified) fused with intimate Ukrainian poetic imagery, the composition pairs a dusty syncopated breakbeat, sub-octave dub bass, and tremolo Fender Rhodes chords with an intimate, breathy female alto vocal.

Udio v4 offers native 48 kHz stereo generation, long track rendering up to 10 minutes, and nuanced section-level inpainting. This guide demonstrates how to exploit Udio's unique toolset: strict 250-character prompt constraints, precise `*stars*` inpainting tags, and context length engineering to maintain harmonic coherence while transitioning between energetic breakbeats and sparse atmospheric breakdowns.

---

## 2. Udio v4 Prompt Specification ($\le 250$ Characters)

Udio enforces a hard 250-character limit on its style/generation prompt. To maximize fidelity, every token must be acoustically decisive:

### Master Generation Prompt
```text
ukrainian trip-hop, downtempo, 82 bpm, *breathy intimate female vocal*, heavy vinyl dust, hypnotic Rhodes piano, syncopated breakbeat, dub bass, dark cinema atmosphere, vintage tape saturation
```
- **Character Count**: 198 characters (52-character safety margin below the 250-character cap).
- **Inpainting Asterisks**: The `*breathy intimate female vocal*` syntax primes Udio's neural cross-attention mechanism for vocal texture modification in inpainting passes.

---

## 3. Context Length Engineering

Udio allows producers to configure the **Context Length** window (the amount of preceding audio the neural network references when generating an extension or replacement):

| Section Transition | Optimal Context Length | Acoustic Rationale & Engineering Goal |
| :--- | :---: | :--- |
| **Intro $\to$ Verse 1** | **30 seconds** | Locks the Rhodes chord progression and vinyl noise floor into place before the vocal enters. |
| **Verse 1 $\to$ Chorus** | **1 minute (Max)** | Carries harmonic memory, tempo continuity, and melodic motifs across the build into the chorus. |
| **Chorus $\to$ Verse 2** | **1 minute (Max)** | Ensures the verse beat locks back into the groove established in Verse 1 without tempo drift. |
| **Verse 2 $\to$ Breakdown** | **10–15 seconds (Minimal)** | **Critical Transition**: A short window dumps the rhythmic momentum of the breakbeat, allowing the breakdown to drop instantly into an ambient, percussion-free sub-bass and vocal space. |
| **Breakdown $\to$ Mega-Chorus** | **30 seconds** | Balances the intimacy of the breakdown with an explosive re-introduction of the full drum break. |

---

## 4. Inpainting Canvas Workflow (`*stars*` Syntax)

Udio v4 features an audio inpainting canvas for replacing specific phrases, words, or instrumental licks without regenerating the entire track.

### The Problem: Syllable Clutter in Verse 1
In an initial generation of Verse 1, bar 19 contained the line:
```text
Шукаю спокій у диму
```
The model sang this with generic pop phrasing, lacking breath and tactile presence.

### The 4-Step Inpainting Procedure:
1. **Highlight Region**: In the Udio timeline, highlight bars 18.2 to 21.1 (the exact vocal phrase).
2. **Set Inpainting Prompt**: Update the generation box to isolate the targeted timbre:
   ```text
   ukrainian trip-hop, 82 bpm, *whispered husky alto delivery*, Rhodes piano, tape hiss
   ```
3. **Apply Inpainting Lyrics Markup**: Surround the modified phrase with asterisks in the lyrics box:
   ```text
   Шукаю спокій, *чую теплий шепіт*, крізь нічний туман.
   ```
4. **Context Length**: Set Context to **20 seconds** to blend the ambient tails smoothly.
5. **Render & Audition**: Select the best of 2 generated variations that cleanly embeds the whispered vocalise into the Rhodes texture.

---

## 5. Complete Ukrainian Lyrics & Arrangement Architecture

```text
[Intro - vinyl crackle, solo muted Fender Rhodes chords, 82 bpm]

[Verse 1 - intimate close-mic, syncopated dusty breakbeat]
ШорсткИй вельвЕт, осІнній дим над склом,
Гаряча кАва, зАпах полинУ.
Холодний дОщ стікАє за вікнОм,
Я тихо мікрофОн свій увімкнУ.
*Шукаю спокій, чую теплий шепіт*,
(шепіт)
В калюжах тОне блИск ліхтарів.
Ніч розливАє свій спокІйний трепет,
Без зайвих жестів і фальшИвих слів.

[Chorus - deep dub sub-bass, lush stereo tape delay]
(breathy alto)
Ооо-ооо, падає крапля на граніт,
(harmonized)
Світить імла крізь німий політ.
Ооо-ооо, змито сліди тривожних літ,
Тут зупинився втомлений світ.

[Verse 2 - add subtle acoustic cello and shaker]
(half-time feel)
Торкнусь долОні, срібна темрятА,
(луна)
В моїй кімнАті затишок нічнИй.
МовчАть удвох спокІйні ворота,
І вітер дИше, лагідний, живИй.

[Breakdown - vinyl crackle and isolated Rhodes solo]
(whispered)
Тільки дим.
(whispered)
Тільки звук.

[Outro - slow tape delay fade out]
(луна)
Падає крапля на граніт...
[End]
```

---

## 6. DAW Stem Engineering & Mixing (48 kHz Studio Pipeline)

Because Udio outputs 48 kHz stereo audio, stem separation yields significantly higher fidelity with fewer artifacts than 32 kHz or 44.1 kHz sources:

### 1. Stem Separation
Export the full-length Udio render as 24-bit/48 kHz WAV. Separate into 4 individual stems (Drums, Bass, Vocals, Other/Instruments) using **RipX DAW** or **Moises Pro**.

### 2. Low-End Architecture (Bass & Kick Separation)
- **Sub-Bass (20–90 Hz)**:
  - Route the Bass stem through a low-pass filter at 90 Hz.
  - Insert a mono utility plugin to collapse low frequencies below 120 Hz to 100% Mono.
  - Apply FabFilter Pro-C 2 with an optical compressor profile (smooth leveling, 3 dB gain reduction).
- **Mid-Bass Saturation (90–350 Hz)**:
  - High-pass the second bass lane at 90 Hz. Apply Soundtoys Decapitator (Style E, Drive 3.0) for warm tape saturation, making the Rhodes bass notes audible on smartphone speakers.
- **Dynamic Kick Unmasking**:
  - Insert Trackspacer on the Sub-Bass channel keyed to the Kick drum stem. Set reduction to 20% (approx 2.5 dB ducking) centered at 60 Hz.

### 3. Tchad Blake Drum Parallel Bus
- Trip-hop drums require weight and grit without destroying master bus dynamics.
- Send the Drum stem to an Aux track with an aggressive compressor (e.g. Empirical Labs Distressor in 1:1 "Nuke" mode or Soundtoys Devil-Loc).
- **Route this Aux track DIRECTLY to the Master Fader**, bypassing the drum subgroup bus. Blend it in at -14 dB for instantaneous snare punch and room dirt.

### 4. Mid-Side Vocal Reverb Ducking
- Insert a stereo plate reverb (e.g. Valhalla VintageVerb) on an Aux return.
- Insert a dynamic EQ on the reverb return, set to Mid channel processing only.
- Sidechain the dynamic EQ to the dry Lead Vocal stem, pulling down the reverb return between 1 kHz and 5 kHz by 4 dB whenever the singer is active. This keeps the lead vocal ultra-intimate and intelligible while providing expansive stereo tail width.

### 5. Mastering & True Peak Discipline
- **Loud Master Target**: -8.0 LUFS integrated.
- **Ceiling**: **-1.0 dBTP** with True Peak limiting **OFF**.
- *Alternative Target (Broadcast / Audiophile)*: -14.0 LUFS integrated with ceiling at **-2.0 dBTP** and True Peak limiting **ON**.

# Diagnostic & Remediation Guide: Eliminating Robotic & Sterile AI Vocals

**File**: `examples/failures/robotic-vocals-fix.md`  
**Failure Mode**: Sterile, Synthetic, or Heavily Autotuned Vocals ("Пластмасовий вокал")  
**Target Platforms**: Suno AI (v4.5 / v5.5), Udio AI (v4), Google Flow Music (Lyria 3.5)  
**Severity**: High (Destroys human emotional resonance, flags the track immediately as cheap amateur AI generation)  

---

## 1. Symptom Diagnosis & Auditory Indicators

One of the most persistent artifacts in generative AI music is the **Sterile/Robotic Vocal** phenomenon:

### Auditory Symptoms:
- The voice exhibits an unconvincing, plastic sheen reminiscent of harsh robotic pitch-correction plugins or flat text-to-speech (TTS) engines.
- Complete absence of micro-dynamics: no audible breath intakes, no vocal fry, no tactile close-mic intimacy.
- Sibilants ("с", "ц", "ш", "щ") sound metallic, brittle, or phasey, cutting harshly through the mix.
- Across both verse and chorus, the vocal retains the exact same static timbre and spatial positioning, creating fatigue for the listener.

---

## 2. Root Cause Analysis

Generative diffusion models rely on style prompts to navigate their latent timbre space. When provided with generic or underspecified vocal prompts, the model defaults to the mathematical mean of its training set — which is often heavily processed, hyper-compressed commercial pop vocals.

| Root Cause Factor | Latent Neural Mechanism | Acoustic Consequence |
| :--- | :--- | :--- |
| **1. Minimalist Vocal Tags** | Generic tokens like `male vocal`, `singer`, or `female vocal`. | Model selects generic autotuned pop archetype without distinctive timbre. |
| **2. Lack of Delivery Descriptors** | Omitting microphone technique and physical dynamics. | Model defaults to maximum digital compression without human micro-dynamics. |
| **3. Lack of Analog Acoustic Cues** | Omitting analog hardware, tape saturation, or room acoustic anchors. | Resulting signal lacks harmonic richness and analog warmth, creating digital "hollowness". |
| **4. Flat Spatial Dimension** | No distinction between verse and chorus spatial processing. | Produces static, 2D "karaoke track" feel with zero dynamic contrast. |

---

## 3. The Deterministic 4-Step Remediation Protocol

To engineer lifelike, emotionally arresting vocals with human presence, execute this 4-step protocol:

### Step 1: Deploy the Mandatory Vocal Triple-Stack
Replace single-word vocal tags with a 3-dimensional vocal specification across all generation prompts:

```text
[Vocal Triple-Stack] = [1. Character / Timbre] + [2. Delivery / Mic Technique] + [3. Production / FX Chain]
```

1. **Character / Timbre**:
   - `raw raspy male baritone`, `husky breathy female alto`, `warm chest-resonant tenor`, `dynamic low-mid vocal texture`.
2. **Delivery / Mic Technique**:
   - `intimate conversational close-mic`, `unhurried deliberate phrasing`, `dry recitative`, `spoken prosody`.
3. **Production / FX Chain**:
   - `vintage tape slap delay`, `mild tube saturation`, `dry room acoustics`, `warm analog pre-amp`.

### Step 2: Inject Dynamic Inline Vocal Gestures
Instruct the model on vocal inflection section by section using round parentheses `(...)`:
- Verse: `(whispered)`, `(spoken)`, `(breathy delivery)`
- Chorus: `(belted)`, `(falsetto)`, `(harmonized)`, `(soaring vocalise)`
- Transitions: `(building intensity)`, `(ad-lib)`, `(луна)`

### Step 3: Enforce Spatial Contrast (Quality Gate 4)
- **Verse**: Intimate, dry, centered, and physically close to the listener's ear (`dry close vocal`).
- **Chorus**: Explosive, wide, double-tracked, and reverberant (`layered vocal harmonies, wide stereo reverb`).

### Step 4: Add Anti-Plastic Negative Vectors
In the Exclude Vector (Negative Prompt), explicitly suppress synthetic vocal artifacts:
```text
robotic autotune, metallic vocal sheen, harsh sibilance, midi plastic vocals, sterile highs, digital vocoder
```

---

## 4. Empirical Before vs. After Demonstration

### The Broken Input (Produces Flat, Plastic Pop Vocals)

**Style Prompt**:
```text
ukrainian indie pop, sad song, male vocal, acoustic guitar
```

**Lyrics Box**:
```text
[Verse 1]
Я чекаю на тебе тут під дощем,
Ти не прийшла і на серці біль.
```

**Auditory Result**:
- The vocal emerges with high-pitched, heavily quantized pitch-correction.
- Zero breath sounds; consonants sound like synthesized plastic samples.
- The voice sits on top of the guitar like a low-budget karaoke recording.

---

### The Remediated Input (Organic, Rich, Human Presence)

**Style Prompt (HookGenius Tag Matrix — 164 Chars)**:
```text
ukrainian indie folk, 96 bpm, raw raspy male baritone, intimate conversational close-mic, warm analog tape saturation, acoustic nylon guitar, dry studio room drums
```

**Exclude Vector**:
```text
robotic autotune, metallic vocal sheen, harsh sibilance, midi plastic vocals, sterile highs, cheap synth
```

**Lyrics Box**:
```text
[Vocal Intro - dynamic acapella, dry and intimate]
(whispered)
Чекаю тут...

[Verse 1 - dry close-mic, unhurried phrasing]
(intimate)
ШорсткЕ вапнО тримАє ніч,
Холодний дОщ стікАє в сад.
(pause)
Вогонь згасАє серед пліч,
І нЕма бІльше вороття назАд.

[Pre-Chorus - building emotional warmth]
(building intensity)
Я чую крок, лунА дзвенить...

[Chorus - explosive emotional release, layered harmonies]
(belted)
Ооо-ааа, лети, мій бОлю, крізь туман!
(harmonized)
Розвій у попіл давній страх!
Ооо-ааа, минає морок і обман,
(луна)
І сонце сходить на стежках!
```

**Auditory Result**:
- **Intro**: The whispered acapella opens with palpable proximity, breathing textures, and vocal fry.
- **Verse**: The voice sounds like an authentic human singer leaning into a vintage Neumann U47 microphone, saturated through an analog tube console.
- **Chorus**: Explodes into wide, authentic stereo double-tracking with zero synthetic pitch quantization.

---

## 5. DAW Post-Processing for Vocal Stems

After separating AI stems via RipX or Moises Pro:
1. **De-Essing**: Insert a dynamic de-esser (e.g. FabFilter Pro-DS) centered at 6.8 kHz to eliminate AI high-frequency sibilant sizzle.
2. **Warmth Induction**: Apply tape saturation (e.g. UAD Studer A800 or Soundtoys Decapitator Style A) boosting second-order harmonics between 200 Hz and 800 Hz.
3. **Resonance Taming**: Use Soothe2 or baby audio Smooth Operator to dynamically suppress static metallic resonances between 2.5 kHz and 4.5 kHz.

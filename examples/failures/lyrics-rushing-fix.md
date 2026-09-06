# Diagnostic & Remediation Guide: Eliminating AI Vocal Rushing & Auctioneer Delivery

**File**: `examples/failures/lyrics-rushing-fix.md`  
**Failure Mode**: Rapid Vocal Delivery / Auctioneer Syndrome ("Вокальна скоромовка")  
**Target Platforms**: Suno AI (v4.5 / v5.5), Udio AI (v4), Google Flow Music (Lyria 3.5)  
**Severity**: High (Renders lyrics unintelligible, triggers unnatural syllable slurring and rhythmic desynchronization)  

---

## 1. Symptom Diagnosis & Auditory Indicators

When an AI music generator encounters structural lyric flaws, it frequently lapses into **Lyrics Rushing** (colloquially known as "Auctioneer Syndrome" or "вокальна скоромовка").

### Auditory Symptoms:
- The singer attempts to cram 12–18 words into a single musical bar, sounding like an auctioneer or an agitated fast-talker rather than a musical artist.
- Vowels are swallowed, consonants collide into unnatural digital clicks, and metric stresses are violently displaced.
- The voice rushes ahead of the beat, collapsing the musical groove and forcing the rhythm section to stutter.
- In severe instances, the model loses pitch accuracy, degenerating into chaotic, breathless semi-spoken gibberish.

---

## 2. Root Cause Analysis

Neural audio generation models (transformers and diffusion acoustic decoders) calculate vocal cadence based on tempo (BPM) and line length. The model attempts to resolve a complete lyrical line within the harmonic boundary of a 2-bar or 4-bar chord progression.

| Root Cause Factor | Underlying Mechanism | Failure Threshold |
| :--- | :--- | :--- |
| **1. Run-On Line Length** | Model tries to squeeze too much text before the chord changes. | $>8\text{ words}$ or $>11\text{ syllables}$ per line. |
| **2. High Tempo Mismatch** | High BPM (e.g. 135–150 BPM) paired with standard narrative phrasing. | $>125\text{ BPM}$ without half-time subdivisions. |
| **3. Absence of Metric Caesuras** | Continuous stream of syllables without breathing pauses or rest marks. | $>4\text{ consecutive lines}$ with zero rhythmic pauses. |
| **4. Lack of Downbeat Anchors** | Asymmetrical meter (e.g. 14 syllables followed by 6 syllables) causing erratic phrasing. | Syllable variance $>2$ between rhyming lines. |

---

## 3. The Deterministic 4-Step Remediation Protocol

To permanently resolve vocal rushing across Suno, Udio, and Google Flow Music, execute these four corrective steps:

### Step 1: Enforce the 4–8 Word & 8–10 Syllable Hard Ceiling
Every line in verses and pre-choruses must be strictly capped at **4 to 8 words** and **8 to 10 syllables**. If an idea takes 16 syllables, divide it across two distinct lines.

### Step 2: Inject the Inline `(half-time feel)` Gesture
Inject the vocal pacing gesture `(half-time feel)` immediately before the dense stanza. This signals the acoustic decoder to stretch vowel durations and phrase over half-time kick/snare subdivisions.

### Step 3: Insert Strategic Rest & Breath Metatags
Use `(pause)` inline or `[Short Instrumental Fill]` between couplets. This provides the generative model with the acoustic headroom needed to reset its phoneme alignment window.

### Step 4: Re-Anchor Style Tempo or Drum Groove
In the Style Box / Prompt, reduce the BPM anchor or specify a halftime rhythmic pocket:
- Instead of: `fast tempo, 140 bpm, energetic drums`
- Use: `132 bpm, half-time drum groove, unhurried downbeat phrasing, deliberate cadence`

---

## 4. Empirical Before vs. After Demonstration

### The Broken Input (Triggers Severe Rushing)
```text
[Verse 1]
Я довго блукав серед цих темних нічних вулиць міста і шукав хоч якусь відповідь на всі свої болючі питання
Але навколо був тільки холодний дощ і мокрий асфальт який блищав під тьмяними ліхтарями мовчазного проспекту
І ніхто не міг мені сказати куди мені далі йти серед цього безмежного і мертвого міського туману
```
- **Word Count**: 18–19 words per line.
- **Syllable Count**: 36–38 syllables per line.
- **Acoustic Result**: The AI singer frantically raps the phrase in a high-pitched, slurred monotone, exhausting its phrasing envelope before bar 3 and clipping the instrumental transition.

---

### The Remediated Input (Pristine Rhythmic Cadence)
```text
[Verse 1 - cold driving chorus bassline, sparse 808 hi-hats]
(half-time feel)
БлукАю в тЕмряві нічнІй,
Де мОкрий блИскає асфАльт.
(pause)
ЛіхтАр тримАє прОмінь свій,
І хОлод крИє цей базАльт.

[Short Instrumental Fill - 2 bars]

(half-time feel)
ШорсткЕ вапнО німИх спорУд,
ЗабУтий чАсу передзвІн.
(pause)
І вИпадок змивАє бруд
З холодних цеглянИх голІн.
```
- **Word Count**: 4–5 words per line.
- **Syllable Count**: Strict 8-8-8-8 iambic balance.
- **Acoustic Result**: Flawless, deliberate baritone phrasing. Every syllable sits securely on the 808 snare pocket, with breathing space and natural emotional gravity.

---

## 5. The Spoken Prosody Test (Pre-Generation Verification)

Before submitting any lyrics to an AI music generation model, perform the mandatory **Spoken Prosody Test**:

1. **Set a Metronome**: Set a digital metronome to your target tempo (e.g. 132 BPM).
2. **Read Aloud at Half-Speed**: Read your lyrics aloud, tapping your hand strictly on beats 1 and 3 (the half-time backbeat).
3. **Observe Breathing**: Can you comfortably breathe between every second line without gasping or truncating words?
4. **Stress Alignment**: Do your natural spoken accents fall on downbeats? Ensure stressed vowels are capitalized (`блукАю`, `тЕмряві`, `асфАльт`) to eliminate phonetic ambiguity.
5. **Pass Standard**: If you stumble or feel forced to accelerate your speech, the line is too long. Split it immediately.

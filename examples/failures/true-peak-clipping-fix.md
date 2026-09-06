# Diagnostic & Remediation Guide: Resolving True Peak Distortion & Inter-Sample Clipping

**File**: `examples/failures/true-peak-clipping-fix.md`  
**Failure Mode**: Inter-Sample Clipping & Transcoding Distortion ("Пастка True Peak")  
**Target Platforms**: Spotify, Apple Music, YouTube Music, Tidal, Tidal HiFi, Streaming Lossy Codecs  
**Severity**: Critical (Causes audible digital distortion, crunchy transients, and squashed dynamics on streaming distribution)  

---

## 1. Symptom Diagnosis & Auditory Indicators

Producers frequently encounter a frustrating paradox when preparing AI-generated tracks for streaming release:
The mix sounds loud, clean, and punchy inside the DAW. However, once uploaded to Spotify or Apple Music, the track exhibits:
- **Crunchy, distorted transients** on kick drums and snare hits.
- **Harsh, sizzly distortion** on vocal sibilants ("с", "ц", "ш") and cymbals.
- **Unnatural dynamic pumping**, where the entire mix chokes whenever a sub-bass note hits.
- **Loss of punch and stereo imaging**, leaving the mix sounding muddy and fatigued compared to commercial Western chart releases.

---

## 2. The True Peak Mastering Trap Explained

The primary culprit behind this degradation is the **True Peak Mastering Trap**:

### How the Trap Occurs:
1. Conventional internet mastering advice often dictates: *"Always leave True Peak Limiting ON and set your ceiling to -2.0 dBTP (or -1.0 dBTP) while matching commercial loudness (-7 to -8 LUFS)."*
2. **The Flaw**: True Peak limiters rely on mathematical oversampling interpolation filters (typically 4x or 8x oversampling) to detect reconstructed inter-sample peaks (ISPs).
3. When a loud, modern commercial master (-6 to -8 LUFS) is fed into an active True Peak limiter, the oversampling algorithm detects phantom reconstructed peaks. The limiter aggressively clamps down on transients that do not actually clip standard D/A converters.
4. **The Acoustic Result**: Transients are smeared, punch is destroyed, and the limiter introduces severe intermodulation distortion and pumping artifacts directly into the master WAV file.
5. Furthermore, when streaming platforms transcode this compromised WAV into lossy codecs (Ogg Vorbis 320 kbps, AAC 256 kbps), the codec's psychoacoustic filters exacerbate the distortion.

---

## 3. The Streaming Codec Overshoot Reality

| Codec & Bitrate | Typical ISP Reconstruction Overshoot | Required Ceiling Margin |
| :--- | :---: | :---: |
| **WAV (Lossless 24-bit / 48 kHz)** | 0.0 dB (Direct digital representation) | -0.2 dB |
| **Apple Music (AAC 256 kbps)** | +0.3 dB to +0.6 dB | -1.0 dBTP |
| **Spotify (Ogg Vorbis 320 kbps)** | +0.4 dB to +0.8 dB | -1.0 dBTP |
| **YouTube Music (Opus 160 kbps)** | +0.5 dB to +0.9 dB | -1.0 dBTP |

**Conclusion**: Setting your output ceiling to **-1.0 dBTP** provides complete protection against lossy transcoding oversaturations without needing to engage dynamic-crushing True Peak limiting.

---

## 4. The Deterministic 5-Step Remediation Protocol

To achieve loud, pristine, distortion-free streaming masters, execute this 5-step engineering protocol:

### Step 1: Turn OFF True Peak Limiting
In your mastering limiter (e.g., FabFilter Pro-L 2, iZotope Ozone Maximizer, Sonnox Oxford Limiter), toggle the **True Peak Limiting / ISP mode to OFF**. Use standard sample-peak detection with modern transparent attack/release algorithms (*Modern*, *Dynamic*, or *Transparent* styles).

### Step 2: Calibrate Ceiling Based on Target Loudness Profile

| Target Loudness Profile | Integrated LUFS | Limiter Ceiling | True Peak Mode | Target Environment |
| :--- | :---: | :---: | :---: | :--- |
| **Loud Commercial Single** | **-6.5 to -8.0 LUFS** | **-1.0 dBTP** (or -0.2 dB) | **OFF** | Club, Radio, Modern Spotify/Apple Single |
| **Dynamic Indie / Alt-Rock** | **-10.0 to -12.0 LUFS** | **-1.0 dBTP** | **OFF / 4x** | High dynamic range, organic acoustic depth |
| **Strict Broadcast (EBU R128)** | **-14.0 LUFS** | **-2.0 dBTP** | **ON** | Television broadcast, official European festivals |

> **Crucial Rule**: Target -14.0 LUFS with -2.0 dBTP True Peak limiting **ONLY** when required by strict classical or broadcast standards. For competitive Western darkwave, post-punk, trap-folk, or metalcore singles, target **-7 to -8 LUFS** with ceiling at **-1.0 dBTP** and TP **OFF**.

### Step 3: Enforce Low-End Split Compression (Quality Gate 7)
AI stems often feature excessive out-of-phase low rumble that triggers early limiter pumping.
1. Split the Bass stem at **200 Hz**:
   - **Sub-Bass (<200 Hz)**: Force to 100% Mono. Apply brickwall hard-knee limiting (10:1 ratio, fast attack, 40 ms release) clamping gain reduction to $\le 3\text{ dB}$.
   - **Mid-High Bass (>200 Hz)**: Leave in stereo. Apply warm analog saturation (Soundtoys Decapitator or FabFilter Saturn 2) to generate harmonic overtones.
2. **Kick Unmasking**: Insert dynamic sidechain EQ (Trackspacer or FabFilter Pro-Q 3) on the bass stem, ducking the sub-bass by 2.5 dB centered at the kick drum's fundamental frequency (typically 55–65 Hz).

### Step 4: Tchad Blake Parallel Drum Distortion Direct to Master (Quality Gate 8)
To make drums hit hard without eating up the master limiter's headroom:
1. Create a parallel Aux track for the drums.
2. Insert an extreme analog distortion unit (e.g. Soundtoys Devil-Loc, Empirical Labs Distressor, or SansAmp).
3. **Crucial Routing**: Route the output of this parallel distortion track **DIRECTLY to the Master Fader**, bypassing the drum subgroup bus and its compressor.
4. Blend this Aux at -12 to -16 dB. It injects sustained energy and decay grit without increasing the master peak transient ceiling.

### Step 5: Dynamic Mid-Side Vocal Reverb Ducking
1. Send the Lead Vocal to a stereo reverb return.
2. Place a dynamic EQ on the reverb Aux configured to process the **Mid channel only**.
3. Sidechain this dynamic EQ to the dry vocal stem, ducking the reverb's mid frequencies (1 kHz to 5 kHz) by 3 to 6 dB during active singing phrases.
4. This clears massive dynamic headroom in the center of the mix, allowing the master limiter to run cleaner without squashing the vocal.

---

## 5. Master Verification & Quality Gate 9 Checklist

Before exporting the final distribution master, verify these metrics using Youlean Loudness Meter or iZotope Insight:

- [ ] **Integrated Loudness**: Matches targeted genre profile (-7.0 to -8.0 LUFS for commercial single).
- [ ] **Short-Term Loudness**: Never exceeds -5.5 LUFS during the chorus climax.
- [ ] **Max True Peak**: Ceiling set to -1.0 dBTP (peak readout does not exceed -0.8 dBTP on test transcode).
- [ ] **Low-End Mono Phase Correlation**: Lows below 120 Hz show a constant +1.0 correlation meter reading.
- [ ] **Codec Audition Test**: Audition track through Apple AAC and Spotify Ogg Vorbis transcode previews (via Sonnox Fraunhofer Pro-Codec or Ozone Codec Preview); zero audible clipping or crunchy sibilants.

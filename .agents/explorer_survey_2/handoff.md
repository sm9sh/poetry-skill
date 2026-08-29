# Handoff Report — Explorer 2: Templates & Audio Engineering Survey

## Executive Summary
This survey provides an exhaustive audit and gap analysis of all template files, root guides, and audio engineering specifications in the `poetry-skill` repository against the authoritative `ai-music-generation-meta-spec-v8.md`. It maps all required updates for:
1. The expanded Metatag Grammar & Inline Vocal Gestures library (`[...]` vs `(...)`).
2. The 10 AI Quality Gates complete definitions and failure-remediation matrices.
3. Step 4: The AI Conductor Generation Roadmap (Seed 30–50s, Vance Powell Verse 2 development, Breakdown & Mega-Chorus, Outro $\le$ 20s).
4. Step 5: Professional DAW Stem Engineering (Stem splitting, Kick/Bass phase alignment, dynamic sidechain unmasking, Sub/Mid-High Split Bass Compression, Tchad Blake parallel drum distortion routed directly to Master Fader bypassing Drum Bus, dynamic Mid-Side Reverb sidechaining).
5. Step 6: Mastering & Algorithmic Streaming Distribution (True Peak trap elimination: -1 dBTP for -6..-8 LUFS without TP limiting or -14 LUFS for -2 dBTP; genre skip rate thresholds; single-only ad traffic to eliminate the Playlist Placement Trap; Spotify Canvas, Marquee, Discovery Mode).

---

## 1. Observation

### 1.1 Root & Skill Template Files Current State
Direct inspection of repository files revealed the following exact states and line numbers:

1. **`ukrainian-poetry-to-suno.md` (and `skills/ukrainian-poetry-to-suno/references/full-guide.md`)**:
   - *Current Lines 1–209*: Contains basic Custom Mode architecture (Style 80–180 chars, Lyrics with bracket tags and parentheses, Exclude vectors, 8-genre taxonomy, Ukrainian stress capitalization).
   - *Gaps Observed*:
     - Completely lacks the 6-step lifecycle architecture diagram.
     - Lacks Step 1 (Reverse Engineering: Vocal Triple-Stack [Character+Delivery+FX], Melodic Math hooks, key of track, harmonic tension).
     - Lacks Step 2 (AI-Optimized Lyrics Writing: syllable symmetry, Spoken Prosody Test, Staccato vs Legato spatial contrast, 5-Second Rule, 50-Second Chorus Rule, Melodic Previews, Glue Hooks, Cognitive melody limits $\le$ 3–4).
     - Lacks Step 3 Multi-Platform Prompt Engineering details (Suno v4.5/v5.5 Conversational "First 5 Words" rule, HookGenius 5-module matrix, My Taste, Voices cloning, Custom Models, Failure modes; Udio v4 48 kHz stereo, Context Length 10–15s vs max, Inpainting `*stars*`; Flow Music Lyria 3.5 Conversational Agent, Spaces, Turntable, Section-level replace editing, AI Cover, Gemini Omni Flash video sync, 500 daily credits).
     - Lacks Step 4 (The AI Conductor: Seed, Extend, Vance Powell Verse 2 development, Breakdown & Mega-Chorus, Outro $\le$ 20s).
     - Lacks Step 5 (DAW Stem Engineering: Split Bass Compression, Phase alignment, Kick/Bass unmasking, Tchad Blake parallel distortion to Master Fader, Mid-Side Reverb sidechaining).
     - Lacks Step 6 (Mastering True Peak trap elimination, genre skip rate thresholds, single-only ads, Spotify Canvas/Marquee/Discovery Mode).
     - Lacks the complete 10 AI Quality Gates table.

2. **`lyrics-to-suno-template.md` (and `skills/ukrainian-poetry-to-suno/references/lyrics-to-suno-template.md`)**:
   - *Current Lines 1–258*: Focuses on basic Custom Mode copy-paste templates (80–180 char style box, basic section markers `[Intro]`, `[Verse 1]`, `[Pre-Chorus]`, `[Chorus]`, `[Instrumental Break]`, `[Bridge]`, `[Outro]`).
   - *Gaps Observed*:
     - Does not showcase the complete library of inline vocal gestures in round parentheses: `(whispered)`, `(belted)`, `(falsetto)`, `(screamed)`, `(ad-lib)`, `(building intensity)`, `(key change)`, `(half-time feel)`, `(harmonized)`.
     - Does not demonstrate Step 4 Vance Powell Verse 2 development tag (`[Verse 2 - add driving tambourine, shaker, backing vocals]`), `[Vocal Intro]`, `[Beat Drop]`, `[Breakdown]`, or `[Mega-Chorus]`.
     - Lacks multi-platform template blocks for Suno v4.5/v5.5 (Conversational Paragraph vs Tag-Based Matrix), Udio v4 (with Context Length notes & Inpainting `*stars*`), and Google Flow Music (Conversational Agent format).

3. **`song-structure-pack.md` (and `skills/ukrainian-poetry-to-suno/references/song-structure-pack.md`)**:
   - *Current Lines 1–352*: Lists syntax grammar table, standard metatag list, and 8 genre structure templates.
   - *Gaps Observed*:
     - Section 1 Syntax table (Lines 9–27) mentions `*Зірочки*` as "Уникати. Модель може вимовляти зірочки вголос" without explaining that in **Udio v4 Inpainting**, `*stars*` is the official syntax for vocal regeneration/inpainting!
     - Lacks dedicated subsection for inline vocal gestures in `(...)` (`(whispered)`, `(belted)`, `(falsetto)`, `(screamed)`, `(ad-lib)`, `(building intensity)`, `(key change)`, `(half-time feel)`, `(harmonized)`).
     - Missing modern meta-spec v8 tags: `[Vocal Intro]`, `[Beat Drop]`, `[Mega-Chorus]`, `[Breakdown]`, `[Post-Chorus]`.
     - Templates do not embed Vance Powell Verse 2 development or Breakdown/Mega-Chorus dynamics.

4. **`suno-prompt-anti-patterns.md` (and `skills/ukrainian-poetry-to-suno/references/suno-prompt-anti-patterns.md`)**:
   - *Current Lines 1–162*: Outlines 10 prompt anti-patterns (Token overflow, metadata leakage, Ukrainian in style box, parentheses hallucination, stress shifting, arrows, conflicting styles, copyright naming, empty exclude, provincial kitsch).
   - *Gaps Observed*:
     - Missing meta-spec v8 Failure Modes: **Lyrics Rushing** (vocal speedup on long lines $\rightarrow$ fix: 4–8 words per line, moderate BPM, `(half-time feel)`), **Robotic/Sterile Vocals** ($\rightarrow$ fix: Vocal Triple-Stack), and **The Negation Trap** (Suno ignores "no drums" $\rightarrow$ fix: hyper-specific positive tags `purely acoustic, solo piano, isolated vocals, sparse`).
     - Missing the **True Peak Mastering Trap** (-2 dBTP double specification trap on loud masters).
     - Missing the **Playlist Placement Trap** (driving cold ad traffic to artist playlists instead of single-only smart links).

5. **`ukrainian-poetry-skill.md`**:
   - *Current Lines 1–581*: Focuses on 6 poetic principles, Ukrainian versification, prosody, meters, forms, and subagents.
   - *Gaps Observed*: Needs explicit reference links to the new 6-step AI music lifecycle, Spoken Prosody Test, and Melodic Math rules when poetry is intended for AI song conversion.

6. **`skills/ukrainian-poetry-to-suno/SKILL.md` & `skills/poetry-skill/SKILL.md`**:
   - *Current Content*: Outlines Custom Mode basics, Western genre anchoring, token economy.
   - *Gaps Observed*: Needs full synchronization with 6-step lifecycle, multi-platform prompt engineering (Suno v4.5/v5.5, Udio v4, Flow Music Lyria 3.5), 10 AI Quality Gates, DAW post-production, and True Peak mastering standards.

7. **`tests/validator/metatag_validator.py`**:
   - *Current Lines 27–60, 154–166*: Validates `[...]` tags against `STRUCTURAL_PREFIXES` and flags `INSTRUMENTAL_KEYWORDS_IN_PARENS` inside `(...)`.
   - *Gaps Observed*:
     - `STRUCTURAL_PREFIXES` should explicitly recognize `vocal intro`, `beat drop`, `mega-chorus`, `mega chorus`, `мега-приспів`, `мегаприспів`, `вокальне інтро`.
     - `INSTRUMENTAL_KEYWORDS_IN_PARENS` must not accidentally flag valid inline vocal gestures such as `(half-time feel)`, `(building intensity)`, `(key change)`, `(harmonized)`, `(whispered)`, `(belted)`, `(falsetto)`, `(screamed)`, `(ad-lib)`, `(vocal runs)` when they contain words like `half-time` or `key` or `feel`.

---

## 2. Logic Chain

### 2.1 Logic Chain: Metatag Syntax & Inline Vocal Gestures
1. **Observation**: Meta-spec v8 distinguishes between:
   - Structural & arrangement cues in square brackets `[...]` (processed silently by audio engines).
   - Backing vocals, echoes, and inline vocal delivery gestures in round parentheses `(...)` (vocalized or executed by the vocal synthesis engine).
2. **Inference**:
   - In Suno and Google Flow Music, text in `(...)` is fed to the vocal phoneme/timbre generator.
   - Therefore, putting `(guitar solo)` or `(drum buildup)` causes the singer to sing the words "guitar solo".
   - Conversely, vocal performance directives that directly modulate the vocal delivery—such as `(whispered)`, `(belted)`, `(falsetto)`, `(screamed)`, `(ad-lib)`, `(building intensity)`, `(key change)`, `(half-time feel)`, `(harmonized)`—are intended as inline performance modifiers embedded directly before/after lyrical phrases.
3. **Required Action**:
   - Update `song-structure-pack.md`, `lyrics-to-suno-template.md`, `ukrainian-poetry-to-suno.md`, and `suno-prompt-anti-patterns.md` to document the exact 9 canonical inline vocal gestures in `(...)` alongside bracketed structural tags `[...]`.
   - Update `tests/validator/metatag_validator.py` so that regex/keyword matching explicitly whitelists these 9 inline vocal gestures while maintaining strict prohibition against instrumental keywords inside `(...)`.

### 2.2 Logic Chain: The 10 AI Quality Gates
1. **Observation**: Meta-spec v8 defines a strict, 10-gate quality control table spanning the entire production pipeline (composition, prosody, generation, DAW post-production, mastering, and marketing).
2. **Inference**:
   - A song cannot be declared production-ready if it fails any of these 10 objective acoustic or structural gates.
   - Each gate has a precise detection criterion and a deterministic remediation procedure.
3. **Required Action**:
   - Integrate the complete 10 AI Quality Gates table into `ukrainian-poetry-to-suno.md`, `skills/ukrainian-poetry-to-suno/references/full-guide.md`, `suno-style-rubric.md`, and `skills/ukrainian-poetry-to-suno/SKILL.md`.

### 2.3 Logic Chain: Step 4 — The AI Conductor Generation Roadmap
1. **Observation**: Generating a full 3–4 minute song in a single prompt causes arrangement fatigue, structural collapse, and vocal rushing.
2. **Inference**:
   - Professional results require modular generation using iterative extensions (`Extend`):
     - **Seed (30–50s)**: Hook-first intro (5-Second Rule), verify groove and vocal tone.
     - **Verse & Pre-Chorus**: Build momentum to the first chorus within 50s.
     - **Verse 2 Development (Vance Powell)**: Add percussion (tambourine, shaker), backing vocals, or stereo guitar riffs so the second verse is not a static duplicate of Verse 1.
     - **Breakdown & Mega-Chorus**: 15–20s energy drop (vocal + sub-bass only) followed by an explosive climax with layered harmonies and clashing guitars.
     - **Concise Outro ($\le$ 20s)**: Prevent listeners from dropping off at the end of the track.
3. **Required Action**:
   - Embed this step-by-step roadmap into all guides, prompt templates, and scenario walkthroughs.

### 2.4 Logic Chain: Step 5 — DAW Post-Production Engineering
1. **Observation**: Raw AI audio generations contain low-end phase cancellations, frequency masking between kick and bass, sterile dynamics, and mono/stereo reverb clutter.
2. **Inference**:
   - 6 specific DAW engineering techniques elevate AI stems to commercial release quality:
     1. *Stem Splitting*: Moises, RipX, LALAL.AI into Vocals, Bass, Drums, Other.
     2. *Phase Optimization*: Check Kick & Bass in Mono; invert polarity or apply alignment plugins (FUSER) to recover lost low-end punch.
     3. *Dynamic Frequency Unmasking*: Sidechain dynamic EQ (Trackspacer / Neutron Unmask) on Bass ducking specific frequencies during Kick hits.
     4. *Split Compression on Bass*: Sub-channel (<200 Hz) with brickwall limiting for solid bedrock; Mid-High channel (>200 Hz) with analog saturation and dynamic compression for string attack.
     5. *Tchad Blake Parallel Drum Distortion*: Heavily saturated/crushed parallel drums routed **directly to Master Fader**, deliberately bypassing the Drum Bus to preserve mix headroom.
     6. *Dynamic Mid-Side Reverb Sidechaining*: Duck vocal reverb 3–6 dB via sidechain from dry lead vocal, applied in Mid-Side mode so center reverb ducks for vocal intelligibility while stereo sides remain lush.
3. **Required Action**:
   - Document the full DAW engineering protocol in `ukrainian-poetry-to-suno.md`, `skills/ukrainian-poetry-to-suno/references/full-guide.md`, and `skills/ukrainian-poetry-to-suno/SKILL.md`.

### 2.5 Logic Chain: Step 6 — Mastering & Algorithmic Streaming Distribution
1. **Observation**:
   - Loud masters (-6..-8 LUFS) forced to meet -2 dBTP True Peak ceilings suffer harsh inter-sample distortion.
   - Algorithmic discovery on Spotify is governed by strict Skip Rate thresholds, Completion Rates (55–60%), Save Rates (>20%), and ad traffic routing.
2. **Inference**:
   - *Mastering Rule*: For loud commercial masters (-6..-8 LUFS), disable True Peak limiting and set ceiling to **-1 dBTP** (or -0.2 dB for transient punch). If -2 dBTP is strictly required, master at **-14 LUFS** (or -8 LUFS safe).
   - *Genre Skip Rate Thresholds (Spotify 2026)*:
     - Pop: >48%
     - Hip-Hop: >44%
     - Electronic: >37%
     - Indie Rock: >31%
     - Absolute Alarm: >45% (completely terminates algorithmic recommendations).
   - *Playlist Placement Trap*: Directing cold Meta Ads traffic to an artist playlist results in rapid skips across the catalog, degrading the artist's algorithmic standing. Cold ad traffic must point exclusively to a single target track.
   - *Spotify Native Tools*: Utilize Spotify Canvas (8s video loop, +5% retention), Marquee (full-screen recs, 15% intent), and Discovery Mode.
3. **Required Action**:
   - Integrate these mastering, algorithmic, and distribution specifications into all relevant reference guides and checklists.

---

## 3. Detailed Specification Mapping Tables

### 3.1 Complete 10 AI Quality Gates Definition & Remediation Matrix

| Gate # | Name & Scope | Pass Criteria (Verification Standard) | Failure Condition | Deterministic Remediation Action |
| :--- | :--- | :--- | :--- | :--- |
| **Gate 1** | **Anti-Skip (First 5s)** | Live human voice, vocal hook, or recognizable signature sound starts within the first 5 seconds. | Track opens with a long, generic instrumental buildup (>5s). | Regenerate the Seed block using `[Vocal Intro - dynamic acapella]` or `[Hook Intro]`. |
| **Gate 2** | **«Правило 50 секунд» (50s Chorus Rule)** | Main chorus hook with full energy and lyrical thesis lands within the first 50 seconds. | First chorus delayed past 0:50 due to verbose verses or multiple pre-choruses. | Shorten Verse 1 lines, eliminate filler couplets, and re-generate initial segment. |
| **Gate 3** | **Spoken Prosody & Stress** | Lyrics pass the Spoken Prosody Test when read aloud naturally; all stressed vowels on homographs/mobile accents are capitalized (`вИпадок`, `дорОга`). | Words distorted by AI accentuation or forced unnatural stress to fit meter/rhyme. | Rebalance syllable counts; apply Udio Inpainting (`*words*`) or Flow Music Section Replace. |
| **Gate 4** | **Spatial Contrast (Staccato vs Legato)** | Distinct spatial contrast: Verse is rhythmic, crisp, staccato; Chorus features soaring, open-vowel legato (`Ooooh`, `Aaah`). | Chorus sounds flat, narrow, and rhythmically identical to verses. | Insert open vowel extensions in chorus lyrics and update tag to `[Chorus - explosive open wide space]`. |
| **Gate 5** | **Verse 2 Development (Vance Powell)** | Verse 2 introduces new arrangement elements (percussion, shaker, tambourine, backing harmonies, guitar counter-melodies). | Verse 2 is an exact acoustic copy of Verse 1 (causing cognitive listener fatigue). | Extend after Chorus 1 using `[Verse 2 - add driving tambourine, shaker, backing vocals]`. |
| **Gate 6** | **Breakdown & Mega-Chorus** | Dynamic 15–20s energy drop (`[Breakdown]`) before exploding into a multi-layered climax (`[Mega-Chorus]`). | Final section lacks dynamic reset and sounds emotionally flat. | Re-extend finale: insert `[Breakdown - vocal and sub-bass only]` followed by `[Mega-Chorus - maximum energy]`. |
| **Gate 7** | **Low-End Split Compression (DAW)** | Bass split into Sub (<200 Hz brickwall limited) and Mid-High (>200 Hz saturated); dynamic sidechain unmasking keyed to Kick. | Muddy low end, bass masking kick transients, uncontrolled sub-bass rumble. | Split bass stem at 200 Hz; apply Trackspacer / Neutron dynamic EQ on bass keyed to Kick. |
| **Gate 8** | **Tchad Blake Distortion Routing (DAW)** | Parallel crushed/distorted drum channels routed directly to Master Fader, bypassing Drum Bus. | Parallel distortion sent through Drum Bus, choking bus compressor and killing mix headroom. | Reroute parallel distortion auxiliary tracks directly to Master Fader. |
| **Gate 9** | **Mastering True Peak Trap** | Loud masters (-6..-8 LUFS) have TP limiting disabled with ceiling at -1 dBTP (or -14 LUFS if -2 dBTP required). | Harsh inter-sample clipping or limiter pumping caused by forcing -2 dBTP on loud masters. | Disable True Peak limiting; set limiter ceiling to -1 dBTP or lower master to -14 LUFS. |
| **Gate 10** | **Single-Only Ad Traffic** | Paid advertising (Meta/TikTok ads) directed exclusively to a single-track link / smart link. | Cold ad traffic directed to artist playlist, causing cascading catalog skips. | Retarget all cold ad campaigns to dedicated single URLs. |

---

### 3.2 Metatag Grammar & Inline Vocal Gestures Library

#### Structural & Arrangement Tags `[Square Brackets]` (Parsed as Silent Directives)
- `[Intro]` / `[Atmospheric Synth Intro]`
- `[Vocal Intro - dynamic acapella, dry and close]`
- `[Beat Drop - heavy fuzz bass, punchy driving drums]`
- `[Verse 1 - rhythmic, dry vocals, clean muted guitar]`
- `[Pre-Chorus - building intensity, rising snare roll]`
- `[Chorus - explosive, epic harmonies, wide stereo]`
- `[Verse 2 - add driving tambourine, shaker, backing vocals]`
- `[Post-Chorus - rhythmic vocal chops, synth arpeggio]`
- `[Instrumental Break - gritty fuzz slide guitar solo]`
- `[Bridge - acoustic, stripped-back, warm Rhodes chords]`
- `[Breakdown - vocal and sub-bass only, intimate, dry]`
- `[Mega-Chorus - maximum energy, layered harmonies, guitars clashing]`
- `[Outro - fading out, solo analog synth, tape hiss]`
- `[End]` / `[Cold End]` / `[Abrupt Cut]`
- `[Tempo: 120 BPM]`, `[Dynamic: Crescendo]`, `[Acapella]`, `[Stripped Back]`

#### Inline Vocal Gestures & Delivery Modifiers `(Round Parentheses)` (Vocalized / Performed by AI Vocalist)
- `(whispered)` / `(whispered, intimate)` — Shifts vocal delivery to intimate close-mic whisper (verses, breakdown).
- `(belted)` / `(belted, powerful)` — Demands open-throat chest voice belting on high emotional peaks (chorus climax).
- `(falsetto)` — Triggers fragile, airy high-register vocal delivery.
- `(screamed)` / `(growl)` — Triggers extreme harsh vocal expression (metalcore, post-punk peaks).
- `(ad-lib)` / `(vocal runs)` — Directs background vocal improvisation and melodic ornamentation.
- `(building intensity)` — Gradually increases vocal aggression, volume, and urgency.
- `(key change)` — Signals melodic/harmonic tonal modulation into the climax.
- `(half-time feel)` — Decelerates vocal phrasing rhythm by 50% relative to the underlying beat (fixes lyrical rushing).
- `(harmonized)` / `(layered harmonies)` — Engages multi-part vocal polyphony on key hook words.
- Backing vocal lyrics & stereo echoes: `(луна)`, `(ніколи знов)`, `(разом у темряві)`.

---

### 3.3 Audio Engineering & Distribution Technical Specification

#### DAW Stem Post-Production Checklist
1. **Stem Separation**: Split master audio into 4+ stems (Vocals, Bass, Drums, Other) via Moises Pro, RipX DAW, or LALAL.AI.
2. **Phase Optimization**:
   - Sum Kick and Bass stems to Mono.
   - Flip Bass phase polarity ($180^\circ$); evaluate low-end sum. Select the polarity with maximum low-frequency power.
   - Optional: Apply *Sound Radix Auto-Align* or *FUSER* to dynamically resolve phase interaction.
3. **Dynamic Unmasking**:
   - Insert dynamic EQ (*Trackspacer* at 10–25% or *iZotope Neutron 4 Unmask*) on Bass track.
   - Route Kick drum into sidechain input to carve out 50–100 Hz space on every kick transient.
4. **Bass Split Compression**:
   - Duplicate Bass track into two parallel channels:
     - **Sub-Bass Channel**: LPF at 200 Hz. Apply Brickwall Limiter (Pro-L2 / FabFilter) with 3–6 dB gain reduction to lock sub-energy into a solid foundation.
     - **Mid-High Bass Channel**: HPF at 200 Hz. Apply analog saturation (*Soundtoys Decapitator* / *Saturn 2*) and dynamic musical compression (*1176* 4:1, fast attack/release) for string bite.
5. **Tchad Blake Parallel Drum Distortion Routing**:
   - Send drums to parallel auxiliary channel loaded with aggressive distortion (*SansAmp PSA-1*, *Soundtoys Devil-Loc*, or *Decapitator*).
   - **Crucial Routing Rule**: Route the auxiliary output **directly to Master Fader**, bypassing the Drum Bus compressor to preserve mix headroom.
6. **Dynamic Mid-Side Reverb Sidechaining**:
   - Place stereo reverb (*Valhalla VintageVerb* / *FabFilter Pro-R*) on vocal aux bus.
   - Insert dynamic compressor/EQ on reverb aux keyed to dry Lead Vocal.
   - Configure sidechain in Mid-Side mode to attenuate Mid channel by 3–6 dB during singing, while leaving Side channels wide and intact.

#### Mastering & Streaming Distribution Standards
1. **True Peak Trap Elimination**:
   - *Loud Masters (-6 to -8 LUFS)*: Disable True Peak limiting in master limiter; set ceiling to **-1 dBTP** (or -0.2 dB for maximum transient impact).
   - *Standard Masters (-14 LUFS)*: Safe for -2 dBTP ceiling without inducing limiter distortion.
2. **Spotify 2026 Algorithmic Thresholds**:
   - **Skip Rate Targets by Genre**:
     - *Pop*: $< 48\%$ (critical failure above 48%).
     - *Hip-Hop*: $< 44\%$ (critical failure above 44%).
     - *Electronic*: $< 37\%$ (critical failure above 37%).
     - *Indie Rock*: $< 31\%$ (critical failure above 31%).
     - *Universal Alarm Threshold*: $\ge 45\%$ across any genre terminates algorithmic playlisting (*Discover Weekly*, *Release Radar*, *Radio*).
   - **Completion Rate**: Target $55–60\%+$ (song length optimized to 2:30–4:00 min; Outro $\le 20$s).
   - **Save Rate**: $\ge 20\%$ triggers algorithmic playlist promotion.
3. **Eliminating the Playlist Placement Trap**:
   - Never direct paid ad traffic (Meta Ads / TikTok Ads) to an artist playlist.
   - Direct cold ad traffic exclusively to single-track URLs.
4. **Spotify Native Visual & Promo Ecosystem**:
   - **Spotify Canvas**: 8-second 9:16 vertical looping video (+5% stream completion, +145% track shares).
   - **Spotify Marquee**: Full-screen sponsored recommendations for high-intent audience conversion (15% intent rate).
   - **Spotify Discovery Mode**: Algorithmic radio and autoplay promotion.

---

## 4. File-by-File Required Changes Inventory

| Target File Path | Required Updates & Content Additions |
| :--- | :--- |
| `d:\poetry-skill\ukrainian-poetry-to-suno.md` & `skills/ukrainian-poetry-to-suno/references/full-guide.md` | - Add 6-step lifecycle architecture diagram.<br>- Add Step 1 (Reverse Engineering: Vocal Triple-Stack, Melodic Math, Key/Tension).<br>- Add Step 2 (AI-Optimized Lyrics: Spoken Prosody Test, Staccato vs Legato, 5-Second Rule, 50s Chorus Rule, Previews, Glue Hooks).<br>- Add Step 3 Multi-Platform specs (Suno v4.5/v5.5 Conversational & HookGenius Tag-Based, Udio v4 Context Length & Inpainting `*stars*`, Flow Music Lyria 3.5 Spaces/Turntable/Omni Flash).<br>- Add Step 4 (The AI Conductor: Seed, Extend, Vance Powell Verse 2, Breakdown & Mega-Chorus, Outro $\le$ 20s).<br>- Add Step 5 (DAW Post-Production: Split Compression, Phase, Unmasking, Tchad Blake parallel distortion to Master Fader, Mid-Side Reverb Sc).<br>- Add Step 6 (Mastering without True Peak trap, genre skip rates, Single-only ads, Spotify Canvas/Marquee/Discovery Mode).<br>- Add full 10 AI Quality Gates table. |
| `d:\poetry-skill\lyrics-to-suno-template.md` & `skills/ukrainian-poetry-to-suno/references/lyrics-to-suno-template.md` | - Add complete table of inline vocal gestures in `(...)`: `(whispered)`, `(belted)`, `(falsetto)`, `(screamed)`, `(ad-lib)`, `(building intensity)`, `(key change)`, `(half-time feel)`, `(harmonized)`.<br>- Add multi-platform Custom Mode templates for Suno v4.5/v5.5 (Conversational & Tag-Based), Udio v4 (with Context Length & Inpainting), and Google Flow Music (Conversational Agent).<br>- Update lyrics templates to demonstrate Vance Powell Verse 2 development and Breakdown/Mega-Chorus. |
| `d:\poetry-skill\song-structure-pack.md` & `skills/ukrainian-poetry-to-suno/references/song-structure-pack.md` | - Clarify `*stars*` notation: forbidden in Suno/Flow lyrics, but standard syntax for **Udio v4 Inpainting** vocal regeneration.<br>- Add dedicated reference table for 9 inline vocal gestures in `(...)`.<br>- Add new structural metatags: `[Vocal Intro]`, `[Beat Drop]`, `[Post-Chorus]`, `[Breakdown]`, `[Mega-Chorus]`.<br>- Update the 8 genre structural templates to embed Vance Powell Verse 2 development and dynamic breakdowns. |
| `d:\poetry-skill\suno-prompt-anti-patterns.md` & `skills/ukrainian-poetry-to-suno/references/suno-prompt-anti-patterns.md` | - Add Meta-Spec v8 Failure Modes: **Lyrics Rushing** (fix: 4–8 words/line, `(half-time feel)`), **Robotic/Sterile Vocals** (fix: Vocal Triple-Stack), **The Negation Trap** (fix: hyper-specific positive tags).<br>- Add **The Mastering True Peak Trap** (forcing -2 dBTP on loud masters).<br>- Add **The Playlist Placement Trap** (sending cold ad traffic to playlists). |
| `d:\poetry-skill\ukrainian-poetry-skill.md` | - Add explicit cross-reference pointers to the 6-step AI music lifecycle, Spoken Prosody Test, Melodic Math, and 10 Quality Gates. |
| `d:\poetry-skill\skills\ukrainian-poetry-to-suno\SKILL.md` | - Synchronize skill overview, core priorities, and output modes with the full 6-step lifecycle, multi-platform prompt matrix, and 10 Quality Gates. |
| `d:\poetry-skill\skills\poetry-skill\SKILL.md` | - Update master routing table and directives to include Suno v4.5/v5.5, Udio v4, Flow Music Lyria 3.5, and DAW engineering standards. |
| `d:\poetry-skill\AGENTS.md` & `d:\poetry-skill\GEMINI.md` | - Update operational directives with 6-step lifecycle summary, inline vocal gestures `(...)`, 10 AI Quality Gates, and DAW/Mastering standards. |
| `d:\poetry-skill\tests\validator\metatag_validator.py` | - Add `vocal intro`, `beat drop`, `mega-chorus`, `mega chorus`, `мега-приспів`, `мегаприспів`, `вокальне інтро` to `STRUCTURAL_PREFIXES`.<br>- Add regex whitelist to permit valid inline vocal gestures in `(...)` while continuing to catch disallowed instrumental keywords in `(...)`. |

---

## 5. Caveats
- No direct code edits have been committed in this turn (exploration and survey phase only).
- All 63 existing tests pass with 0 errors. The proposed validator and template updates must maintain 100% backward compatibility with existing tests.

---

## 6. Conclusion
The survey confirms that `ai-music-generation-meta-spec-v8.md` provides an exhaustive, mathematically and acoustically rigorous expansion of the audio prompt engineering ecosystem. The repository currently possesses solid fundamentals (8-genre taxonomy, Ukrainian stress capitalization, bracket/paren separation) but requires a comprehensive upgrade across all root files, skill definitions, templates, anti-pattern guides, and validator whitelists to incorporate the 6-step lifecycle, multi-platform matrices (Suno v4.5/v5.5, Udio v4, Flow Music Lyria 3.5), 10 AI Quality Gates, DAW post-production techniques, and mastering/distribution protocols.

---

## 7. Verification Method
1. **File Consistency Check**: Inspect target files after edits using `view_file` to ensure all 6 steps, 10 Quality Gates, and metatags are represented without discrepancy.
2. **Deterministic Test Execution**: Run the Python test suite:
   ```bash
   py -3 tests/run_tests.py --all
   ```
   *Expected Result*: 63+ tests pass with exit code 0, 0 failures, 100% success rate.
3. **Validator Regex Verification**: Verify that `tests/validator/metatag_validator.py` accepts valid inline gestures like `(whispered)` or `(half-time feel)` and valid tags like `[Vocal Intro]` or `[Mega-Chorus]` without throwing errors.

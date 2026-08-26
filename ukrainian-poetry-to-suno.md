---
name: ukrainian-poetry-to-suno
description: "Converts Ukrainian song ideas, poems, or lyrics into production-grade Suno AI prompts: 80-180 character token-optimized Style tags, bracketed metatags [Intro]/[Verse]/[Chorus]/[Drop], parenthetical backing cues, 8 modern Ukrainian music genres, and acoustic anti-artifact negative vectors."
---

# Ukrainian Poetry To Suno v2 (Production Audio Prompting System)

Use this skill when you need to:
- Convert a Ukrainian poem, theme, or lyric draft into production-ready **Suno AI / Flow Music Custom Mode** prompts.
- Strictly ground the musical style, arrangement, and production in **Western contemporary and classic genres** (UK/US/Nordic/European Post-Punk, Darkwave, Synthwave, Trip-Hop, Alt-Pop, Shoegaze, Progressive Metalcore, Melodic Techno, Cinematic Ambient).
- Guarantee that generated tracks sound like authentic Western releases with Ukrainian vocals, completely eliminating regional cheesy pop, post-Soviet schlager, and tourist-folk kitsch (*шароварщина*).
- Translate Ukrainian or Western artist and track references into safe, non-infringing Western stylistic formulas.
- Optimize the `Style of Music` field within the strict **80–180 character token budget** without metadata leakage.
- Format lyrics with bracketed structural metatags (`[Verse]`, `[Chorus]`, `[Drop]`, `[Outro]`) and parenthetical backing cues `(луна)`.
- Formulate acoustic anti-artifact and anti-local-pop `Exclude` vectors.

---

## 1. Suno Custom Mode Architecture

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ 1. Style of Music Field (Western Genre Descriptors, 80–180 Chars)                      │
│    dark synthwave, analog moog bass, gated 80s drums, breathy alt-pop vocal, 120 bpm   │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 2. Lyrics Field (Ukrainian Lyrics + Bracketed Metatags + Parenthetical Harmonies)      │
│    [Intro]                                                                             │
│    [Verse 1]                                                                           │
│    У темнім склі тремтить моє безсонне відбиття...                                     │
│    (тиша навколо)                                                                      │
│    [Chorus]                                                                            │
│    [Outro]                                                                             │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 3. Exclude / Negative Prompt Field (Acoustic Artifacts + Local Pop / Sharovarshchyna)  │
│    metallic highs, harsh sibilance, muddy bass, cheesy regional pop, tourist folk cliches│
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Core Operational Rules

### 2.1 Strict Token Economy (80–180 Characters)
Suno v3.5 and v4 diffusion-transformer conditioning operates optimally on **80–180 characters** (~15–30 tokens):
- **Too short (<60 chars)**: Defaults to generic mid-tempo pop-rock averaging.
- **Optimal (80–150 chars)**: Maximum prompt adhesion, tight frequency control, and audible genre separation.
- **Hard Max (180 chars)**: Anything beyond 180 characters risks attention dispersion and token truncation.

### 2.2 Left-to-Right Positional Priority
Suno's cross-attention assigns highest weight to initial tokens. Always order your prompt:
`[Primary Genre / Hybrid] -> [Tempo / Groove / BPM] -> [Vocal Timbre] -> [Key Instruments] -> [Production Aesthetic] -> [Dynamics]`

### 2.3 Clean Field Separation & Zero Metadata Leakage
- **FORBIDDEN in Style Box**: `Language: Ukrainian`, `Theme: Cossack`, `Mood: Melancholic`, `Lyrics by: ...`. Any text labels inside the style box degrade audio synthesis into mud.
- Put **only English musical descriptors** with authentic cultural acoustic anchors (e.g. `bandura`, `sopilka`, `white voice`) in `Style of Music`.
- Put **Ukrainian language lyrics and bracketed metatags** in the `Lyrics` box.

---

## 3. The 8 Modern Ukrainian Music Genres

| Genre | Key Stylistic Descriptors | BPM Range | Typical Instruments | Canonical Reference Anchor |
| :--- | :--- | :--- | :--- | :--- |
| **Ethno-Chaos / Avant-Folk** | `ukrainian ethno-chaos, avant-folk, polyphonic chanting, driving acoustic groove` | 115–130 BPM | Cello drone, djembe, drymba, accordion | DakhaBrakha |
| **Post-Punk / Coldwave** | `ukrainian post-punk, doomer coldwave, chorus bassline, jangly guitar, monotone baritone` | 125–140 BPM | Melodic chorus bass, reverb guitar, 80s drums | SadSvit |
| **Dark Synth / Cyberpunk** | `dark synthwave, coldwave, analog bass arpeggio, aggressive electro beat, deadpan vocal` | 120–135 BPM | Modular analog synths, punchy drum machine | Kurs Valüt |
| **Trap-Folk / Drill** | `modern trap-folk, 808 sub bass, rapid-fire flow, traditional sopilka hook, syncopated beat` | 130–145 BPM | Sopilka, distorted 808, rolling hi-hats | Kalush |
| **Melodic Metalcore** | `progressive metalcore, drop-tuned heavy riffs, blast beats, dual harsh growl and soaring clean` | 140–170 BPM | 7-string down-tuned guitars, double-kick bass | Jinjer |
| **Shoegaze / Dream Pop** | `dream pop, ethereal shoegaze, wall of sound guitar fuzz, shimmering reverb, breathy falsetto` | 95–115 BPM | Reverb-drenched offset guitars, tape delay | Latexfauna |
| **Ethno-Rock / Punk** | `energetic ethno-rock, driving punk rhythm, brass section, sopilka riffs, gritty male rock lead` | 130–155 BPM | Electric guitar, brass horn section, sopilka | Kozak System |
| **Neoclassical Bandura** | `neoclassical ambient, cinematic ballad, acoustic bandura plucking, warm cello, intimate whisper` | 70–90 BPM | Bandura, chamber cello, subtle piano | KRUTЬ |

---

## 4. Vocal Timbre Directives

To achieve authentic vocal textures, specify exact delivery modes:
- **White Voice (*Білий голос*)**: `authentic white voice, open-throat polyphonic female vocal, raw piercing folk delivery`.
- **Intimate Breathy Chamber**: `intimate breathy female vocal, close-mic, delicate whisper, emotional nuance`.
- **Post-Punk Monotone Baritone**: `deep monotone baritone, detached cold delivery, subtle reverb wash`.
- **Spoken-Word Melodeclamation**: `spoken-word recitation, rhythmic melodeclamation, poetic cadence over ambient textures`.
- **Extreme Dual Metalcore**: `dynamic vocal contrast, savage guttural growls and screams with soaring melodic clean chorus`.
- **Modern Melodic Trap Autotune**: `melodic autotuned trap vocal, stylized pitch correction, rhythmic syncopated flow`.

---

## 5. Structural Metatags & Arrangement Grammar

### 5.1 Standard Bracketed Metatags
Use bracketed headers to control structural transitions in the `Lyrics` box:
- `[Intro]` / `[Instrumental Intro]`
- `[Verse 1]` / `[Verse 2]` (Куплет)
- `[Pre-Chorus]` (Передприспів — builds dynamic tension)
- `[Chorus]` (Приспів — full melodic energy)
- `[Post-Chorus]`
- `[Bridge]` (Міст — melodic/harmonic contrast)
- `[Guitar Solo]` / `[Sopilka Solo]` / `[Bandura Solo]`
- `[Beat Drop]` / `[Drop]` (Electronic/Trap explosion)
- `[Outro]` / `[Fade Out]` / `[End]`

### 5.2 Backing Vocals & Choral Echoes
- Use **parentheses `(...)`** inside verses and choruses for sung backing vocals, harmonies, and echoing repetitions:
  ```text
  [Verse 1]
  Там, де тумани стеляться на схилах,
  (густі тумани)
  Ми чуєм шепіт вікових дібров.
  (вічний шепіт)
  ```

---

## 6. Acoustic Anti-Artifact Negative Prompting

AI generative diffusion can produce audio artifacts. Use the `Exclude` field to sanitize output:

**Standard Anti-Artifact Exclusion Vector**:
```text
metallic highs, harsh sibilance, piercing treble, muddy bass, boomy low-end, garbled vocals, excessive reverb wash, cheesy synth brass
```

**Genre-Specific Exclusions**:
- *For Modern Ethno*: `Exclude: tourist folk polka, midi brass, wedding accordion, cabaret kitsch`
- *For Intimate Acoustic*: `Exclude: heavy drums, distorted guitars, harsh electronic drops, auto-tune`
- *For Synthwave / Cyberpunk*: `Exclude: acoustic guitar, organic drums, brass horns, orchestral strings`
- *For Metalcore*: `Exclude: poppy synth, acoustic guitar, soft autotune, dance beats`

---

## 7. Modular 6-Part Style Formula & Reference Translation

### 7.1 Formula Builder (80–180 Characters)
`[Genre / Subgenre] + [Tempo / Groove] + [Vocal Directives] + [Key Instruments] + [Production Texture] + [Dynamics]`

*Example*:
`ukrainian post-punk, coldwave, 130 bpm, monotone male baritone, melodic chorus bass, jangly reverb guitar, analog drum machine` (127 chars)

### 7.2 Reference-to-Style Translation Protocol
When given an artist or song name as a reference:
1. **Analyze**: Identify rhythm, vocal style, dominant instruments, and spatial reverb.
2. **De-name**: Strip all artist names, album titles, and song titles.
3. **Synthesize**: Map into the 6-part English formula with Ukrainian cultural anchors.

*Example*:
- *Input Reference*: «SadSvit — Касета»
- *Safe Style Output*: `ukrainian post-punk, doomer coldwave, 132 bpm, monotone baritone vocal, melodic chorus bassline, jangly electric guitar, 80s analog beat` (139 chars)
- *Exclude*: `metallic highs, modern hyperpop, acoustic accordion, heavy metal distortion`

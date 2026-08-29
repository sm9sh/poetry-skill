# AGENTS.md — Global Agent Directives for Ukrainian Poetry & Multi-Platform AI Music Generation

This repository is an AI Skills ecosystem for authentic Ukrainian poetry generation, versification, and production-grade AI music prompt engineering across **Suno AI (v4.5 / v5.5)**, **Udio AI (v4)**, and **Google Flow Music (Lyria 3.5)**, incorporating professional DAW stem post-production, algorithmic streaming mastering, and the **10 AI Quality Gates**.

## Operational Directives

### 1. Ukrainian Poetry Directives (`ukrainian-poetry`)
All models and agents generating, editing, or evaluating Ukrainian poetry MUST strictly enforce the **6 Core Poetic Principles (Фундаментальні принципи поетичної майстерності)** as foundational quality standards:

1. **Свіжа образність та метафоричність (Fresh Imagery & Metaphoricity)**:
   - "Show, don't tell" through concrete physical detail, sensory anchors (sight, sound, touch, smell, temperature), and action rather than abstract declarations of emotion.
   - Categorical rejection of worn-out cliches and sentimental tropes (*«кров — любов»*, *«троянди — сльози»*, *«серце палає»*, *«душа плаче»*).
2. **Емоційна глибина та щирість (Emotional Depth & Sincerity)**:
   - Rooted in psychological truth, restraint, and genuine human empathy.
   - Zero theatrical pathos, plastic sentimentality, or preachy moralizing (*«і я збагнув, що треба жити»*).
3. **Ритмічна та звукова гармонія (Rhythmic & Phonic Harmony)**:
   - Audible, breathing prosodic flow (syllabo-tonic, dolnik, taktovik, 14-syllable kolomyika, blank verse, or verlibre).
   - Rich heterogeneous cross-grammatical rhymes (verb+noun, noun+adverb) with pre-tonic supporting consonants; zero grammatical verb-verb or diminutive rhymes.
   - Conscious phonics & soundscapes (alliteration, assonance, Potebnja's inner form of words) and strict adherence to Ukrainian euphony (`у/в`, `і/й`, `з/із/зі`, no hiatus).
4. **Лаконічність і вага слова (Conciseness & Word Weight)**:
   - Maximum semantic density («словам тісно, думкам просторо»).
   - Zero rhythmic padding or filler pronouns (*цей, той, свій, я, вже, ось*) inserted merely to fill foot counts.
   - Strict prohibition against artificial syntactic inversions (*«сонце ясне зійшло»*, *«погляд свій сумний підвів»*) used to force end-rhymes; natural Ukrainian word order is inviolable.
5. **Оригінальність ракурсу (Originality of Perspective)**:
   - Unconventional authorial angle on universal themes; shifting focus from macro-abstractions to revealing micro-details.
   - Paradoxical, lingering, or open endings that avoid trivial closures or moral conclusions.
6. **Органічна єдність форми та змісту (Organic Unity of Form & Content)**:
   - External form (meter, stanza structure, tempo, caesuras, enjambment, line raggedness or smoothness) must intrinsically embody the emotional state and theme.
   - Form is never arbitrary decoration — it is the living body of the poem.

### 2. Multi-Platform AI Music Generation Directives (`ukrainian-poetry-to-suno`)
All music generation, song architecture, prompt crafting, and post-production MUST follow the **6-Step Production Lifecycle** from `ai-music-generation-meta-spec-v8.md`:

- **Western Genre Anchor**: Musically target Western contemporary and classic genres (UK/US Post-Punk, Darkwave, Synthwave, Trip-Hop, Minimalist Alt-Pop, Shoegaze, Progressive Metalcore, Melodic Techno, Ambient). Music must sound like a top-tier global release, not regional/provincial pop.
- **Step 1 — Deep Reference Reverse Engineering**: Extract Genre Hybrid, BPM Range (tempo anchor), Key/Tension, Sonic Aesthetic & Palette (`lo-fi tape hiss`, `warm console`), Vocal Triple-Stack (**Character** + **Delivery** + **FX**), and Melodic Math hooks (Melodic Previews, Glue Hooks, Nano Hooks).
- **Step 2 — AI-Optimized Lyrics Writing**:
  - Syllable symmetry (e.g. 8-8-8-8, 10-8-10-8) forcing downbeat alignment.
  - Spoken Prosody Test (reading aloud naturally before generation).
  - Spatial contrast: Verse Staccato (consonant-rich, punchy) vs Chorus Legato (open soaring vowels `Ooooh, Aaah`).
  - 5-Second Rule (`[Vocal Intro]`) & 50-Second Chorus Rule (first chorus arrives $\le 50$s). Cognitive limit $\le 3\text{--}4$ melodic themes.
- **Step 3 — Multi-Platform Prompt Engineering**:
  - **Suno AI (v4.5 / v5.5)**: Style limit 1000 chars, lyrics limit 5000 chars (optimal style 80–180 chars / 8–15 tags). Dual prompt methods: **Method 1 Conversational Paragraph** with «First 5 Words» rule ($80\%$ attention on opening descriptors) & **Method 2 HookGenius Tag Matrix** (5 modules: Genre, Mood, Vocal Triple-Stack, Instruments, Production/BPM). System features: *My Taste*, *Voices* cloning, *Custom Models*. Failure mode fixes: Lyrics Rushing $\to$ 4–8 words/line + `(half-time feel)`; Sterile Vocals $\to$ Vocal Triple-Stack; Negation Trap $\to$ positive hyper-specificity (`purely acoustic, solo piano, isolated vocals`). Commercial rights on Pro ($10/mo) / Premier ($30/mo).
  - **Udio AI (v4)**: 48 kHz stereo, up to 10 min continuous track, Context Length up to 15 min (10–15s for abrupt transitions vs max for continuity). Inpainting syntax `*stars*` for word/line replacement. Commercial rights strictly on Pro ($30/mo).
  - **Google Flow Music (Lyria 3.5)**: DeepMind Lyria 3.5 engine; 500 daily free credits with commercial rights (MusicFX closed July 31, 2026). Conversational Agent mode (`[Concept & Style] + [Artist/Vibe Ref] + [Instruments] + [Dynamics/Vocals]`). *Spaces* (in-browser music apps), *Turntable* (DJ mixing), Section-level *Replace* editing, *AI Cover*, *Gemini Omni Flash* synchronized video clips.
- **Step 4 — The AI Conductor Extensions Roadmap**: Seed 30–50s $\to$ Extend $\to$ Vance Powell Verse 2 development (`[Verse 2 - add driving tambourine, shaker, backing vocals]`) $\to$ Breakdown 15–20s (`[Breakdown - vocal and sub-bass only]`) & Mega-Chorus (`[Mega-Chorus - maximum energy, layered harmonies]`) $\to$ Outro $\le 20$s.
- **Step 5 — Engineering DAW Stem Mixing**:
  - Stem splitting via Moises Pro, RipX DAW, or LALAL.AI.
  - Kick & Bass mono phase alignment / polarity inversion check.
  - Dynamic frequency unmasking via dynamic sidechain EQ (Trackspacer / Neutron Unmask) ducking bass during kick hits.
  - Split Compression for Bass: Sub-Bass $<200\text{ Hz}$ brickwall limited vs Mid-High $>200\text{ Hz}$ dynamic saturated compression.
  - Tchad Blake Parallel Drum Distortion: Distorted drums routed **directly to Master Fader** (bypassing Drum Bus) to protect headroom.
  - Dynamic Mid-Side Vocal Reverb Sidechain: Reverb ducked 3–6 dB during active singing in Mid channel only.
- **Step 6 — Mastering & Algorithmic Streaming Distribution**:
  - Mastering without True Peak trap: Disable True Peak limiting and set ceiling to **-1 dBTP** (or -0.2 dB) for loud masters ($-6\dots-8\text{ LUFS}$); target $-14\text{ LUFS}$ only if $-2\text{ dBTP}$ is strictly mandatory.
  - Genre Skip Rate Thresholds (Spotify 2026): Pop $>48\%$, Hip-hop $>44\%$, Electronic $>37\%$, Indie rock $>31\%$, universal alarm $>45\%$. Completion rate $>55\text{--}60\%$, Save rate $>20\%$.
  - Abolish Playlist Placement Trap: Direct ad spend solely to individual target singles, never to artist playlists. Spotify Canvas (8s loops), Marquee, Discovery Mode.
- **Strict Parentheses vs Brackets Rule**:
  - `[Square Brackets]`: Used for ALL structural, instrumentation, and arrangement instructions. Models parse them as audio directing cues without singing them.
  - `(Round Parentheses)`: Used **EXCLUSIVELY for backing vocals, ad-libs, and vocal delivery gestures** `(whispered)`, `(belted)`, `(falsetto)`, `(screamed)`, `(ad-lib)`, `(building intensity)`, `(key change)`, `(half-time feel)`, `(harmonized)`, `(луна)`, `(ніколи знов)`. Never put instrumental descriptions in parentheses because Google Flow Music and Suno will vocalize/sing them out loud!
- **Ukrainian Stress Standard for Audio AI Models**:
  - Capitalize the stressed vowel on non-obvious words, homographs, and mobile accents: `вИпадок`, `чорнОзем`, `прИйде`, `заспівАй`, `моЯ`, `землЯ`, `зЕмлю`, `дорОга` vs `дорогА`, `зАмок` vs `замОк`, `плАчу` vs `плачУ`, `сердЕнько`, `одИннадцять`, `листопАд`.
- **Exclude Vector**: Anti-local-pop and anti-artifact suppression tokens (`cheesy regional pop, post-soviet schlager, wedding synth brass, cheap accordion, generic euro-pop, metallic highs, muddy bass`).
- **De-identification**: Never output direct artist names or copyright phrases (`in the style of...`).

### 3. The 10 AI Quality Gates Matrix

| Gate # | Scope & Target | Verification Standard | Deterministic Remediation |
| :--- | :--- | :--- | :--- |
| **Gate 1** | **Anti-Skip (First 5s)** | Live human voice or signature hook in first 5 seconds. | Regenerate Seed with `[Vocal Intro - dynamic acapella]`. |
| **Gate 2** | **50s Chorus Rule** | First full chorus lands $\le 50$ seconds. | Shorten Verse 1 lines, eliminate filler couplets. |
| **Gate 3** | **Spoken Prosody & Stress** | Spoken Prosody Test passes; capitalized stressed vowels (`вИпадок`, `дорОга`). | Rebalance syllable counts; Udio Inpainting `*words*` / Flow Replace. |
| **Gate 4** | **Spatial Contrast** | Verse Staccato (crisp) vs Chorus Legato (open soaring `Ooooh, Aaah`). | Insert open vowels; set `[Chorus - explosive open wide space]`. |
| **Gate 5** | **Verse 2 Development** | Verse 2 adds new arrangement elements (percussion, backing, guitars). | Extend after Chorus 1 with `[Verse 2 - add driving tambourine, shaker, backing vocals]`. |
| **Gate 6** | **Breakdown & Climax** | 15–20s energy drop (`[Breakdown]`) before exploding into `[Mega-Chorus]`. | Re-extend finale with `[Breakdown]` followed by `[Mega-Chorus]`. |
| **Gate 7** | **Low-End Split Bass (DAW)** | Sub $<200\text{ Hz}$ brickwall limited; Mid-High $>200\text{ Hz}$ saturated; Kick unmasking. | Split bass stem at 200 Hz; dynamic sidechain EQ keyed to Kick. |
| **Gate 8** | **Tchad Blake Distortion (DAW)** | Parallel crushed drums routed directly to Master Fader, bypassing Drum Bus. | Reroute parallel distortion aux directly to Master Fader. |
| **Gate 9** | **Mastering True Peak** | Loud masters ($-6\dots-8\text{ LUFS}$) set to $-1\text{ dBTP}$ with TP limiting OFF (or $-14\text{ LUFS}$ if $-2\text{ dBTP}$). | Disable TP limiting; set ceiling to $-1\text{ dBTP}$ or lower master to $-14\text{ LUFS}$. |
| **Gate 10** | **Single-Only Ad Traffic** | Paid advertising directed strictly to target single, avoiding Playlist Placement Trap. | Point all cold ad campaigns to dedicated single smart links. |

## Specialized Subagents Pipeline (`skills/ukrainian-poetry/agents/`)
For multi-stage poetic refinement, the ecosystem utilizes 5 specialized personas:
1. `poetry-imagery-architect` (**Образотворець**): Tactile imagery, sensory anchors, fresh metaphors, anti-cliche guardrails.
2. `poetry-emotional-critic` (**Критик щирості**): Sincerity audit, zero pathos, anti-moralizing, psychological nuance.
3. `poetry-prosody-phonics` (**Майстер фоніки та просодії**): Metric scansion, stress accuracy, acoustic euphony (`у/в`, `і/й`), heterogeneous rhymes, phonics.
4. `poetry-conciseness-editor` (**Редактор лаконічності**): Semantic compression, removal of filler words/pronouns, elimination of artificial inversions.
5. `poetry-form-synthesizer` (**Архітектор форми та ракурсу**): Form-content harmony, paradoxical perspective, final assembly.

## Reference Index & Skill Files
- Poetry Skill: `skills/ukrainian-poetry/SKILL.md`
- Subagents Pipeline: `skills/ukrainian-poetry/agents/`
- Full Poetic Guide: `skills/ukrainian-poetry/references/full-guide.md`
- 100-Point Poetic Rubric: `skills/ukrainian-poetry/references/rubric.md`
- Multi-Platform Music Generation Skill: `skills/ukrainian-poetry-to-suno/SKILL.md`
- Comprehensive Engineering Manual: `skills/ukrainian-poetry-to-suno/references/full-guide.md`
- Multi-Platform Prompt Builder: `skills/ukrainian-poetry-to-suno/references/prompt-builder.md`
- Reference & Style Cheatsheet: `skills/ukrainian-poetry-to-suno/references/reference-to-style-cheatsheet.md`
- Mood to Style Map: `skills/ukrainian-poetry-to-suno/references/mood-to-style-map.md`
- Song Structure & Metatag Pack: `skills/ukrainian-poetry-to-suno/references/song-structure-pack.md`
- Lyrics & Multi-Platform Templates: `skills/ukrainian-poetry-to-suno/references/lyrics-to-suno-template.md`
- Anti-Patterns & Failure Modes: `skills/ukrainian-poetry-to-suno/references/suno-prompt-anti-patterns.md`
- 100-Point Suno & Quality Gates Rubric: `skills/ukrainian-poetry-to-suno/references/rubric.md`

## Verification & Testing
Run deterministic test suites (Python 3 standard library):
```bash
py -3 tests/run_tests.py --all
```

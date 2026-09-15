---
name: poetry-skill
description: "Use when creating, analyzing, editing, or evaluating Ukrainian poetry, versification, rhymed poems, lyrics, or converting Ukrainian poetic material into production-grade Suno AI (v4.5/v5.5), Udio AI (v4), or Google Flow Music (Lyria 3.5) audio prompts with Western sound standards, DAW stem mixing, and streaming distribution."
---

# Ukrainian Poetry & AI Music Generation Skill Suite (poetry-skill)

Unified entry point and master routing for authentic Ukrainian poetry versification and production-grade AI music generation across **Suno AI (v4.5 / v5.5)**, **Udio AI (v4)**, and **Google Flow Music (Lyria 3.5)**, incorporating engineering DAW post-production, algorithmic streaming mastering, and the **10 AI Quality Gates**.

## 1. Sub-Skill Routing

Depending on the task, invoke the specialized sub-workflow:

| Task Type | Trigger / Intent | Sub-Skill to Load |
|---|---|---|
| **Poetry & Versification** | Writing poems, sonnets, dolnik, taktovik, kolomyika, editing rhymes, stress scansion, Ukrainian lyrical texts | `skills/ukrainian-poetry/SKILL.md` |
| **Multi-Platform AI Music Prompts** | Converting poems/briefs to Suno Custom Mode, Udio v4, Flow Music Lyria 3.5, style prompts, Western genre arrangements, metatags | `skills/ukrainian-poetry-to-suno/SKILL.md` |
| **End-to-End Songwriting & Production** | Generating Ukrainian lyrics + creating matching multi-platform prompts + DAW stem engineering roadmap | Execute Section 3: **End-to-End Song Creation Pipeline** |

---

## 2. Core Directives Summary

### Ukrainian Poetry (6 Poetic Standards & 5 Subagents)
1. **Свіжа образність та метафоричність**: Показ через дію й тактильну деталь замість декларацій; нуль затертих штампів (*«кров-любов»*, *«серце палає»*).
2. **Емоційна глибина та щирість**: Справжній психологізм, відсутність фальшивого пафосу, театральщини та моралізаторства.
3. **Ритмічна та звукова гармонія**: Живе дихання розміру (силабо-тоніка, дольник, верлібр), багаті різнорідні рими, фоніка (асонанси, алітерації, звукопис) та закони евфонії (`у/в`, `і/й`, `з/із/зі`).
4. **Лаконічність і вага слова**: Максимальна смислова компресія; нуль "води" та займенників-заповнювачів; сувора заборона штучних синтаксичних інверсій заради рими.
5. **Оригінальність ракурсу**: Нетривіальний авторський погляд на вічні теми, мікро-фокус, парадоксальні або відкриті фінали.
6. **Органічна єдність форми та змісту**: Метр, строфіка та динаміка пауз є природним відбитком теми та внутрішнього стану.
- **5 Subagents Pipeline**: `skills/ukrainian-poetry/agents/` (`poetry-imagery-architect`, `poetry-emotional-critic`, `poetry-prosody-phonics`, `poetry-conciseness-editor`, `poetry-form-synthesizer`) + Autonomous QA Auditor (`poetry-qa-bot`).

### Multi-Platform AI Music Generation & Engineering (Meta-Spec v8)
- **Western Genre Anchor**: All sound design must strictly target Western genres (Post-Punk, Darkwave, Synthwave, Trip-Hop, Alt-Pop, Shoegaze, Progressive Metalcore, Melodic Techno, Ambient).
- **6-Step Production Lifecycle**:
  1. *Step 1 — Deep Reference Reverse Engineering*: Genre Hybrid, BPM Range (tempo anchor), Key/Tension, Sonic Aesthetic & Palette, Vocal Triple-Stack (**Character** + **Delivery** + **FX**), Melodic Math hooks.
  2. *Step 2 — AI-Optimized Lyrics Writing*: Syllable symmetry, Spoken Prosody Test, Staccato vs Legato spatial contrast, 5-Second Rule (`[Vocal Intro]`), 50-Second Chorus Rule. Cognitive melody limit $\le 3\text{--}4$.
  3. *Step 3 — Multi-Platform Prompt Engineering*:
     - **Suno AI (v4.5 / v5.5)**: Method 1 (Conversational Paragraph, «First 5 Words» rule) & Method 2 (HookGenius Tag-Based Matrix 5 modules); My Taste, Voices cloning, Custom Models; Failure mode fixes (Lyrics Rushing, Sterile Vocals, Negation Trap). Commercial rights on Pro/Premier.
     - **Udio AI (v4)**: 48 kHz stereo, 10 min continuous track, Context Length (10–15s vs max), Inpainting `*stars*`. Commercial rights on Pro ($30/mo).
     - **Google Flow Music (Lyria 3.5)**: Conversational Agent mode, Spaces, Turntable, Section-level Replace editing, AI Cover, Gemini Omni Flash synchronized video clips, 500 daily credits with commercial rights.
  4. *Step 4 — Step-by-Step Extensions Roadmap*: Seed 30–50s $\to$ Extend $\to$ Vance Powell Verse 2 development (`[Verse 2 - add driving tambourine, shaker, backing vocals]`) $\to$ Breakdown 15–20s & Mega-Chorus $\to$ Outro $\le 20$s.
  5. *Step 5 — Engineering DAW Stem Mixing*: Stem splitting, Kick/Bass phase alignment, dynamic frequency unmasking (Trackspacer/Neutron), Split Bass Compression (<200 Hz brickwall sub vs >200 Hz dynamic saturated), Tchad Blake parallel drum distortion directly to Master Fader (bypassing Drum Bus), dynamic Mid-Side vocal reverb sidechaining.
  6. *Step 6 — Mastering & Algorithmic Streaming Distribution*: Mastering without True Peak trap (-1 dBTP for -6..-8 LUFS with TP limiting OFF, or -14 LUFS for -2 dBTP); flexible genre Skip Rate thresholds (Pop >48%, Hip-hop >44%, Electronic >37%, Indie rock >31%, alarm >45%); abolish Playlist Placement Trap (direct ad spend strictly to singles); Spotify Canvas, Marquee, Discovery Mode.
- **Metatags & Brackets vs Parentheses**:
  - `[Square Brackets]`: Silent structural and arrangement directions (`[Intro]`, `[Vocal Intro]`, `[Verse 1]`, `[Pre-Chorus]`, `[Chorus]`, `[Verse 2 - add driving tambourine, shaker]`, `[Breakdown]`, `[Mega-Chorus]`, `[Outro]`).
  - `(Round Parentheses)`: Sung backing vocals and inline vocal delivery gestures `(whispered)`, `(belted)`, `(falsetto)`, `(screamed)`, `(ad-lib)`, `(building intensity)`, `(key change)`, `(half-time feel)`, `(harmonized)`, `(луна)`.
- **Ukrainian Stress Standard** *(song lyrics for Suno/Udio/Flow Music only — never in poetry)*: Capitalize the stressed vowel only in three hard categories: (A) **Homographs**: `зАмок` vs `замОк`, `дорОга` vs `дорогА`, `мУка` vs `мукА`, `плАчу` vs `плачУ`, `оргАн` vs `Орган`; (B) **Anti-Russian misaccentuation**: `вИпадок`, `чорнОзем`, `одИннадцять`, `листопАд`, `рукОпис`, `довІдник`, `фартУх`, `ненАвисть`, `пізнАння`, `завдАння`, `принестИ`, `вИрок`, `новИй`, `старИй`; (C) **Non-intuitive mobile shifts**: `зЕмлю` (← землЯ), `рУку` (← рукА), `хОдиш` (← ходИти). **Never mark** function words, obvious-stress words (`моя`, `земля`, `прийде`, `заспівай`, `серденько`), or prepositions/pronouns/conjunctions.
- **10 AI Quality Gates**: Full verification across composition, prosody, prompt engineering, DAW mixing, and mastering.

---

## 3. End-to-End Song Creation Pipeline

The **End-to-End Song Creation Pipeline** is the unified master protocol connecting Ukrainian literary poetic creation with production-grade AI music generation across **Suno AI (v4.5/v5.5)**, **Udio AI (v4)**, and **Google Flow Music (Lyria 3.5)**, followed by engineering DAW stem post-production and True Peak streaming distribution.

### 3.1 Unified Architecture Flowchart

```text
               ┌─────────────────────────────────────────────────────────┐
               │              USER CREATIVE BRIEF / THEME                │
               └───────────────────────────┬─────────────────────────────┘
                                           │
                                           ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ STAGE 1: Ukrainian Poetry Generation (skills/ukrainian-poetry)                         │
│ • Subagents Pipeline: Imagery Architect ➔ Emotional Critic ➔ Prosody & Phonics ➔       │
│   Conciseness Editor ➔ Form Synthesizer                                                │
│ • Output: Authentic Ukrainian Poem grounded in 6 Core Poetic Principles                │
└──────────────────────────────────────────┬─────────────────────────────────────────────┘
                                           │ raw_poem
                                           ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ STAGE 2: Autonomous Poetic Quality Audit (poetry-qa-bot)                               │
│ • Forensic scan against 6 Principles + 14-Category Penalty Deduction Matrix            │
│ • Mandatory Quality Gate: Score must be ≥ 90/100 (Master-level) or ≥ 85/100            │
│ • [Loop if < 85/90]: Itemized remediation blueprint routed to specialist subagents     │
└──────────────────────────────────────────┬─────────────────────────────────────────────┘
                                           │ verified_poem (Score ≥ 90)
                                           ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ STAGE 3: Lyrics Adaptation & Spoken Prosody Test (music-lyrics-architect)             │
│ • Structural arrangement: [Intro], [Verse 1], [Pre-Chorus], [Chorus], [Outro]          │
│ • Backing vocals / Delivery gestures strictly in (Round Parentheses)                   │
│ • Syllable symmetry enforcement (8-8-8-8, 10-8-10-8) to prevent vocal rushing          │
│ • Spoken Prosody Test + AI Stress Capitalization (вИпадок, дорОга, моЯ)                 │
│ • Spatial Contrast: Verse Staccato (crisp) vs Chorus Legato (open soaring vowels)      │
│ • 5-Second Rule ([Vocal Intro]) & 50-Second Chorus Rule                                │
└──────────────────────────────────────────┬─────────────────────────────────────────────┘
                                           │ optimized_lyrics + acoustic_dna
                                           ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ STAGE 4: Platform Selection & Prompt Synthesis (music-prompt-synthesizer)              │
│ • Western Genre Anchor (Post-Punk, Darkwave, Trip-Hop, Minimal Alt-Pop, Shoegaze, etc.)│
│ • Multi-Platform Synthesized Prompts:                                                  │
│   - Suno v4.5/v5.5: Method 1 (First 5 Words) & Method 2 (HookGenius 5-Module Matrix)   │
│   - Udio v4: ≤ 250 chars prompt, 48 kHz stereo, inpainting *stars* syntax, Context Len │
│   - Google Flow Music: Conversational Agent mode, Spaces, Section Replace, AI Cover    │
│ • Anti-Local-Pop Exclude Vector & Complete De-identification (zero artist leaks)       │
└──────────────────────────────────────────┬─────────────────────────────────────────────┘
                                           │ audio_prompts + lyrics_box + extensions_roadmap
                                           ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ STAGE 5: The 10 AI Quality Gates Verification                                          │
│ • Gates 1–6 (Pre-Gen / Arrangement): Anti-Skip 5s, 50s Chorus, Spoken Prosody,        │
│   Spatial Contrast, Vance Powell Verse 2 Expansion, Breakdown (15-20s) & Mega-Chorus   │
│ • Gates 7–10 (DAW / Mastering / Ads): Low-End Split Bass, Tchad Blake Distortion to     │
│   Master Fader, True Peak -1 dBTP / -14 LUFS, Single-Only Ad Traffic                   │
└──────────────────────────────────────────┬─────────────────────────────────────────────┘
                                           │ audio_generation + stem_exports
                                           ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ STAGE 6: Professional DAW Stem Engineering & Mastering (music-daw-mastering-critic)    │
│ • Step 5 Stem Mixing: Separation (Moises/RipX/LALAL), Kick/Bass phase alignment,       │
│   surgical frequency unmasking (Trackspacer), Split Bass Compression (<200Hz brickwall │
│   vs >200Hz saturated), Tchad Blake distortion to Master Fader, Mid-Side vocal ducking │
│ • Step 6 Mastering: -1 dBTP with TP Limiting OFF for loud masters (-6..-8 LUFS);       │
│   Genre Skip Rate monitoring (Pop >48%, Electronic >37%, Rock >31%, universal >45%);   │
│   Single-only ad spend (no Playlist Placement Trap), Spotify Canvas / Discovery Mode   │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

### 3.2 Detailed Protocol Across the 6 Stages

#### Stage 1: Thematic Inception to Authentic Ukrainian Verse
- **Tool / Subagent**: `skills/ukrainian-poetry/SKILL.md` (and 5 specialized personas: `poetry-imagery-architect`, `poetry-emotional-critic`, `poetry-prosody-phonics`, `poetry-conciseness-editor`, `poetry-form-synthesizer`).
- **Standard**: Strictly enforce the **6 Core Poetic Principles**:
  1. *Fresh Imagery*: Concrete tactile details across 5 sensory channels; zero dead metaphors (*«кров-любов»*, *«серце палає»*).
  2. *Emotional Sincerity*: Restrained psychological truth; zero theatrical pathos or didactic sermonizing.
  3. *Prosodic Harmony*: Syllabo-tonic, dolnik, or kolomyika cadence; normative literary stresses (*вИпадок*); rich heterogeneous rhymes; balanced euphony (`у/в`, `і/й`, `з/із/зі`).
  4. *Conciseness & Word Weight*: High semantic density; zero filler pronouns (*цей, той, свій*) or padding particles; **zero artificial syntactic inversions for rhyme**.
  5. *Original Perspective*: Novel authorial angle; micro-detail focus; lingering, open, or paradoxical endings.
  6. *Form-Content Unity*: Rhythm and stanza structure organically body forth the psychological state.

#### Stage 2: Autonomous Quality Audit (Poetry QA Bot)
- **Tool / Subagent**: `skills/ukrainian-poetry/agents/poetry-qa-bot.md`.
- **Function**: Autonomous pre-flight audit before any musical resources are expended.
- **Verification Standard**:
  - Scans poem text against the 7 dimensions from `references/rubric.md` (Ceiling: 100 points).
  - Evaluates against the 14-defect penalty deduction matrix:
    - *Metric breakdown (`D01`)*: -5 to -15 pts
    - *Russianized stress (`D02`)*: -5 to -10 pts per case
    - *Homograph confusion (`D03`)*: -5 pts
    - *Verb-verb rhymes (`D04`)*: -3 to -8 pts
    - *Diminutive rhymes (`D05`)*: -4 pts
    - *Blacklist cliché rhymes (`D06`)*: -5 pts
    - *Artificial inversions (`D07`)*: -3 to -6 pts
    - *Filler padding (`D08`)*: -2 to -5 pts
    - *Abstract emotion telling (`D09`)*: -3 to -6 pts
    - *Theatrical pathos (`D10`)*: -5 to -10 pts
    - *Didactic moralizing ending (`D11`)*: -5 pts
    - *Sharovarshchyna / kitsch (`D12`)*: -10 pts
    - *Syntactic calques (`D13`)*: -5 to -15 pts
    - *Monotonic clausulae (`D14`)*: -3 to -5 pts
  - **Passing Gate**: Poem must score **$\ge 90/100$ (Master-level)** or at least **$\ge 85/100$**. If score is below threshold, execute the **Remediation Blueprint** before proceeding to Stage 3.

#### Stage 3: Song Lyrics Adaptation & Prosodic Alignment
- **Tool / Subagent**: `skills/ukrainian-poetry-to-suno/agents/music-lyrics-architect.md`.
- **Arrangement Conventions**:
  - `[Square Brackets]`: Silent structural and arrangement cues for audio models (`[Intro]`, `[Vocal Intro]`, `[Verse 1]`, `[Pre-Chorus]`, `[Chorus]`, `[Verse 2 - add driving tambourine, shaker]`, `[Breakdown]`, `[Mega-Chorus]`, `[Outro]`).
  - `(Round Parentheses)`: Sung vocal delivery cues, backing vocals, and ad-libs `(whispered)`, `(belted)`, `(falsetto)`, `(screamed)`, `(ad-lib)`, `(building intensity)`, `(key change)`, `(half-time feel)`, `(harmonized)`, `(луна)`. **Never place instrumental cues in parentheses.**
- **Syllable Symmetry**: Standardize foot counts (e.g. 8-8-8-8 or 10-8-10-8) to eliminate AI vocal rushing or rhythmic stumbling.
- **Spoken Prosody Test**: Read aloud at speaking cadence; if words stumble, rebalance syllable count.
- **Ukrainian Stress Capitalization**: Mark stressed vowels in non-obvious words and homographs (`вИпадок`, `чорнОзем`, `прИйде`, `заспівАй`, `моЯ`, `землЯ`, `зЕмлю`, `дорОга` vs `дорогА`, `зАмок` vs `замОк`).
- **Spatial Contrast**: Staccato verses (consonant-rich, punchy rhythm) vs Legato chorus (open, soaring vowels `Ooooh, Aaah`).
- **Timing Directives**: First 5 seconds must feature vocal presence or hook (`[Vocal Intro]`); first Chorus must land $\le 50$ seconds. Cognitive melody limit: $\le 3\text{--}4$ melodic themes per track.

#### Stage 4: Platform Selection & Multi-Platform Prompt Synthesis
- **Tool / Subagent**: `skills/ukrainian-poetry-to-suno/agents/music-prompt-synthesizer.md`.
- **Western Genre Anchor**: All prompt design must target contemporary/classic Western genres (Post-Punk, Darkwave, Synthwave, Trip-Hop, Minimalist Alt-Pop, Shoegaze, Progressive Metalcore, Melodic Techno, Ambient).
- **Platform Synthesizers**:
  1. **Suno AI (v4.5 / v5.5)**:
     - *Method 1 (Conversational Paragraph)*: Apply «First 5 Words» rule ($80\%$ model attention on opening descriptors).
     - *Method 2 (HookGenius Tag Matrix)*: 5 modules (Genre, Mood, Vocal Triple-Stack, Instruments, Production/BPM). Style box: 80–180 characters.
     - *Anti-Pattern Fixes*: Lyrics Rushing $\to$ `(half-time feel)` + 4–8 words/line; Sterile Vocals $\to$ Vocal Triple-Stack (**Character** + **Delivery** + **FX**); Negation Trap $\to$ Positive hyper-specificity.
  2. **Udio AI (v4)**:
     - 48 kHz stereo, up to 10 min continuous track, concise prompt $\le 250$ chars.
     - Context Length management (10–15s for abrupt transitions vs max for continuity).
     - Inpainting syntax `*stars*` for surgical line/word replacement.
  3. **Google Flow Music (Lyria 3.5)**:
     - Conversational Agent mode (`[Concept & Style] + [Artist/Vibe Ref] + [Instruments] + [Dynamics/Vocals]`).
     - Spaces, Turntable, Section-level Replace editing, AI Cover, Gemini Omni Flash synced video clips.
- **Exclude Vector**: Enforce universal anti-local-pop tokens (`cheesy regional pop, post-soviet schlager, wedding synth brass, cheap accordion, generic euro-pop, metallic highs, muddy bass`).
- **De-identification**: Zero artist names or copyrighted strings.

#### Stage 5: 10 AI Quality Gates Verification
Every song asset must pass the **10 AI Quality Gates Matrix** before publication:
- **Gate 1 (Anti-Skip First 5s)**: Live human voice or hook present $\le 5$s.
- **Gate 2 (50s Chorus Rule)**: Full chorus arrives $\le 50$s.
- **Gate 3 (Spoken Prosody & Stress)**: Spoken Prosody test passes; capital accents (`вИпадок`, `дорОга`).
- **Gate 4 (Spatial Contrast)**: Verse Staccato vs Chorus Legato.
- **Gate 5 (Verse 2 Development)**: Vance Powell arrangement expansion (tambourine, shaker, backing vocals).
- **Gate 6 (Breakdown & Climax)**: 15–20s energy drop (`[Breakdown]`) followed by `[Mega-Chorus]`.
- **Gate 7 (Low-End Split Bass)**: Sub $<200\text{ Hz}$ brickwall mono vs Mid-High $>200\text{ Hz}$ dynamic saturated; Kick dynamic sidechain unmasking.
- **Gate 8 (Tchad Blake Drum Distortion)**: Parallel crushed drum aux routed **directly to Master Fader** (bypassing Drum Bus).
- **Gate 9 (Mastering True Peak)**: Loud masters ($-6\dots-8\text{ LUFS}$) set to $-1\text{ dBTP}$ with True Peak limiting OFF (or $-14\text{ LUFS}$ if $-2\text{ dBTP}$ is strictly mandatory).
- **Gate 10 (Single-Only Ad Traffic)**: Ad spend directed strictly to target single (Abolishing Playlist Placement Trap).

#### Stage 6: Professional DAW Stem Engineering & Mastering
- **Tool / Subagent**: `skills/ukrainian-poetry-to-suno/agents/music-daw-mastering-critic.md`.
- **Step 5 DAW Stem Engineering**:
  - Stem extraction via Moises Pro, RipX DAW, or LALAL.AI.
  - Mono Kick & Bass phase alignment / polarity inversion check.
  - Surgical frequency unmasking via dynamic sidechain EQ (Trackspacer / Neutron Unmask) ducking bass 2–3 dB during kick hits.
  - Split Bass Compression: Sub-bass $<200\text{ Hz}$ brickwall limited; Mid-High $>200\text{ Hz}$ dynamic saturated.
  - Tchad Blake Parallel Drum Distortion: Routed directly to Master Fader to preserve Drum Bus headroom.
  - Dynamic Mid-Side Vocal Reverb Sidechain: Reverb ducked 3–6 dB during active vocal presence in Mid channel only.
- **Step 6 Mastering & Streaming Viability**:
  - True Peak headroom protection ($-1\text{ dBTP}$).
  - Skip Rate monitoring against Spotify 2026 thresholds (Pop $>48\%$, Hip-hop $>44\%$, Electronic $>37\%$, Indie rock $>31\%$, universal alarm $>45\%$).
  - Target Completion Rate $>55\text{--}60\%$, Save Rate $\ge 20\%$.
  - Single-only smart links, Spotify Canvas (8s visual loops), Marquee, Discovery Mode.

---

### 3.3 End-to-End Pipeline Data Contract

```yaml
# Unified Data Flow across the 6 Stages
pipeline_execution:
  stage_1_poetry:
    input:
      brief: string                      # Creative prompt, theme, emotional atmosphere
      register: enum                    # contemporary-urban | chamber-intimate | neoclassical | folk | etc.
      form: string                      # iamb | dolnik | kolomyika | verlibre | etc.
    output:
      raw_poem: string                  # Publication-grade poem adhering to 6 Principles

  stage_2_audit:
    input:
      poem_text: stage_1.raw_poem
      passing_threshold: 90
    output:
      total_score: float                # Target: ≥ 90/100
      is_passing: boolean
      deductions: list[string]          # Detailed defect list
      remediation_plan: list[string]    # If not passing, step-by-step fix recipes

  stage_3_lyrics:
    input:
      raw_poetry: stage_2.verified_poem
      structure_template: "Verse-Chorus-Verse-Chorus-Bridge-MegaChorus-Outro"
    output:
      optimized_lyrics: string          # Syllable-symmetric lines with [Metatags] and (Gestures)
      stress_capitalized: boolean       # Stressed vowels marked (вИпадок, дорОга)
      spoken_prosody_passed: boolean

  stage_4_prompts:
    input:
      lyrics: stage_3.optimized_lyrics
      western_genre: string             # e.g., 'ukrainian darkwave post-punk'
      target_platforms: ["suno", "udio", "flow_music"]
    output:
      suno_prompt:
        style_box: string               # Method 1 or Method 2 (80-180 chars)
        lyrics_box: string              # Full lyrics with metatags and vocal gestures
        exclude_prompt: string          # Anti-local-pop and anti-artifact tokens
      udio_prompt:
        prompt_text: string             # ≤ 250 chars dense tags
        inpainting_syntax: string       # *stars* markup
      flow_music_prompt:
        agent_command: string           # Natural language prompt for Lyria 3.5

  stage_5_quality_gates:
    input:
      prompts: stage_4.prompts
      lyrics: stage_3.optimized_lyrics
    output:
      gates_1_to_6_status: boolean      # Structural and prosodic pre-flight verification
      gates_7_to_10_status: boolean     # Mixing and mastering pre-flight verification

  stage_6_daw_mastering:
    input:
      generated_audio_stems: list[string]
      target_loudness_lufs: float       # -6 to -8 LUFS (or -14 LUFS if mandatory)
    output:
      stem_mixing_checklist: object     # Low-end split, unmasking, Tchad Blake aux
      mastering_spec: object            # -1 dBTP ceiling, True Peak limiter OFF
      streaming_retention_plan: object  # Canvas, single-only campaigns, skip rate targets
```

---

## 4. Quick Reference

- Master Directives: `AGENTS.md`
- Poetic Guide: `skills/ukrainian-poetry/references/full-guide.md`
- 100-Point Poetic Rubric: `skills/ukrainian-poetry/references/rubric.md`
- Subagents Pipeline: `skills/ukrainian-poetry/agents/` (5 subagents + `poetry-qa-bot`)
- Comprehensive AI Music Engineering Guide: `skills/ukrainian-poetry-to-suno/references/full-guide.md`
- Multi-Platform Prompt Builder: `skills/ukrainian-poetry-to-suno/references/prompt-builder.md`
- Reference & Style Cheatsheet: `skills/ukrainian-poetry-to-suno/references/reference-to-style-cheatsheet.md`
- Mood to Style Map: `skills/ukrainian-poetry-to-suno/references/mood-to-style-map.md`
- Song Structure & Metatag Pack: `skills/ukrainian-poetry-to-suno/references/song-structure-pack.md`
- Lyrics & Multi-Platform Templates: `skills/ukrainian-poetry-to-suno/references/lyrics-to-suno-template.md`
- Anti-Patterns & Failure Modes: `skills/ukrainian-poetry-to-suno/references/suno-prompt-anti-patterns.md`
- 100-Point Suno & Quality Gates Rubric: `skills/ukrainian-poetry-to-suno/references/rubric.md`
- Test Suite: `py -3 tests/run_tests.py --all`


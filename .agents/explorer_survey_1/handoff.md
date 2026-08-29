# Handoff Report: Explorer 1 (Spec & Skills Survey)

## 1. Observation

### 1.1 Direct Source Observations
1. **Authoritative Meta-Spec v8 (`d:\poetry-skill\ai-music-generation-meta-spec-v8.md`, lines 1–307)**:
   - **Architectural Scope**: Establishes a complete 6-step lifecycle from user idea/references to DAW stem mixing and algorithmic streaming distribution:
     - *Step 1 (Lines 70–83)*: Deep Reference Reverse Engineering (Genre complexes, BPM Range, Sonic Aesthetic & Palette, Vocal Triple-Stack [Character + Delivery + FX], Mood & Energy, Harmonic Features & Tension, Melodic Math Hooks [Melodic Previews, Glue Hooks, Nano Hooks], Bracketed Layout).
     - *Step 2 (Lines 85–119)*: AI-Optimized Lyrics Writing (Syllable symmetry, Downbeat alignment, Staccato Verse vs Legato Chorus space contrast, 5-Second Rule for vocal intro, 50-Second Chorus Rule, Melodic Previews, Glue Hooks, cognitive limit $\le 3\text{--}4$ melodies, Spoken Prosody Test).
     - *Step 3 (Lines 121–168)*: Multi-Platform Prompt Engineering across three major platforms:
       - **Suno AI (v4.5 / v5.5)**: 1000 char style limit, 5000 char lyrics limit; Dual prompt methodologies: Method 1 *Conversational Paragraph* with «First 5 Words» rule (80% attention on first 4–5 words) and Method 2 *Tag-Based Matrix* (HookGenius 5 modules: 1. Genre/Subgenre, 2. Mood/Energy, 3. Vocal Triple-Stack, 4. Lead Instruments, 5. Production Aesthetic & BPM; 8–15 tags or $\le 200$ chars); System features (*My Taste*, *Voices* cloning on Pro/Premier, *Custom Models* up to 3); Failure modes (*Lyrics Rushing* $\to$ 4–8 words/line + `(half-time feel)`, *Sterile Vocals* $\to$ Vocal Triple-Stack, *The Negation Trap* $\to$ hyper-specificity e.g. `purely acoustic, solo piano, isolated vocals`); Commercial rights on Pro ($10/mo) & Premier ($30/mo), none on Free tier.
       - **Udio AI (v4)**: 48 kHz stereo, up to 10 min continuous track without drift, Context Length up to 15 min; Prompt formula `[Main Genre], [Sub-Genre], [Year/Era], [Vocal Timbre & Character], [Analog Production Style], [Acoustic Space, BPM]`; Context length management (10–15s for abrupt transitions vs maximum for continuity); Inpainting syntax `*stars*` (e.g. `*static sky*`); Commercial rights strictly on Pro ($30/mo), Standard ($10/mo) has no commercial rights.
       - **Google Flow Music (Lyria 3.5)**: DeepMind Lyria 3.5 engine; 500 daily credits on free tier with full commercial rights (MusicFX closed July 31, 2026); Conversational Agent mode (`[Concept/Style] + [Artist/Vibe Ref] + [Instruments] + [Dynamics/Vocal]`); Browser *Spaces* & *Turntable* DJ deck; Section-level *Replace* editing; *AI Cover* style re-harmonization; *Gemini Omni Flash* synchronized music video generation.
     - *Step 4 (Lines 214–224)*: Step-by-Step Extensions Roadmap / The AI Conductor (Seed 30–50s with Anti-Skip 5s rule $\to$ Extend Verse/Chorus $\to$ Vance Powell Verse 2 development with tambourine/shaker/backing vocals/stereo guitars $\to$ Breakdown 15–20s & Mega-Chorus $\to$ Outro $\le 20$s).
     - *Step 5 (Lines 226–239)*: Engineering DAW Post-Production & Stem Mixing (Stem splitting with Moises/RipX/LALAL.AI; Kick & Bass mono phase alignment / FUSER; Frequency unmasking via Trackspacer / Neutron dynamic sidechain; Split Compression for Bass: Sub-Bass $<200\text{ Hz}$ brickwall limiter vs Mid-High $>200\text{ Hz}$ dynamic saturation/compression; Tchad Blake parallel drum distortion routed directly to Master Fader bypassing Drum Bus; Mid-Side Reverb sidechain ducking vocal reverb 3–6 dB in center only).
     - *Step 6 (Lines 241–264)*: Mastering & Algorithmic Streaming Distribution (True Peak trap elimination: $-1\text{ dBTP}$ ceiling with True Peak limiting disabled for loud $-6\dots-8\text{ LUFS}$ masters, or $-14\text{ LUFS}$ for $-2\text{ dBTP}$; Flexible genre Skip Rate thresholds: Pop $>48\%$, Hip-hop $>44\%$, Electronic $>37\%$, Indie Rock $>31\%$, absolute alarm $>45\%$; Completion Rate $>55\text{--}60\%$, length 2:30–4:00; Save Rate $>20\%$; Abolish *Playlist Placement Trap* by directing ad spend exclusively to target singles; Spotify Canvas 8s loops, Discovery Mode, Spotify Marquee).
     - *Metatags & Inline Gestures (Lines 170–212)*: Structural tags (`[Intro]`, `[Vocal Intro]`, `[Beat Drop]`, `[Verse]`/`[Verse 1]`, `[Pre-Chorus]`, `[Chorus]`, `[Verse 2]`, `[Post-Chorus]`, `[Instrumental Break]`, `[Bridge]`, `[Breakdown]`, `[Mega-Chorus]`, `[Outro]`, `[End]`) and inline vocal parenthetical commands (`(whispered)`, `(whispered, intimate)`, `(belted)`, `(belted, powerful)`, `(falsetto)`, `(screamed)`, `(growl)`, `(ad-lib)`, `(vocal runs)`, `(building intensity)`, `(key change)`, `(half-time feel)`, `(harmonized)`, `(layered harmonies)`).
     - *10 AI Quality Gates (Lines 293–307)*: Complete table defining Gate 1 (Anti-Skip 5s), Gate 2 (50s Chorus Rule), Gate 3 (Spoken Prosody & Naturalness), Gate 4 (Sectional Space Contrast Staccato vs Legato), Gate 5 (Verse 2 Development), Gate 6 (Breakdown & Climax), Gate 7 (Low-End Split Compression & Unmasking), Gate 8 (Tchad Blake Drum Distortion to Master), Gate 9 (Mastering True Peak), Gate 10 (Single-Only Ad Traffic).

2. **Existing Codebase & Skill State Observations**:
   - `skills/ukrainian-poetry-to-suno/SKILL.md` (lines 1–237) and `skills/ukrainian-poetry-to-suno/references/full-guide.md` (lines 1–209):
     - Focus primarily on Suno v3.5/v4 with a single comma-separated style prompt (80–180 chars) and basic section tags.
     - Completely lack the 6-step lifecycle architecture.
     - Lack the dual prompt methodology for Suno v4.5/v5.5 (Method 1 Conversational Paragraph & Method 2 HookGenius Tag Matrix).
     - Lack Udio v4 specifications (48kHz, Context Length, Inpainting `*stars*`, Pro license).
     - Lack Google Flow Music Lyria 3.5 specifications (Spaces, Turntable, Section Replace, AI Cover, Gemini Omni Flash, 500 daily credits).
     - Lack DAW Stem Mixing engineering details (Split Compression, Tchad Blake master routing, Mid-Side Reverb sidechain).
     - Lack Mastering True Peak guidelines and algorithmic streaming distribution rules.
     - Lack the 10 AI Quality Gates table.
   - `skills/poetry-skill/SKILL.md` (lines 1–51), `AGENTS.md` (lines 1–68), `GEMINI.md` (lines 1–9):
     - Outline 6 Poetic Principles and Suno basics, but lack references to the 6-step lifecycle, multi-platform prompt engineering (Suno/Udio/Flow), DAW post-production, True Peak mastering, and the 10 Quality Gates.
   - `tests/validator/metatag_validator.py` (lines 1–207):
     - Contains `STRUCTURAL_PREFIXES` and `INSTRUMENTAL_KEYWORDS_IN_PARENS`.
     - Validates brackets and parentheses, but needs explicit confirmation/support for new tags: `[Vocal Intro]`, `[Beat Drop]`, `[Post-Chorus]`, `[Mega-Chorus]`, `[Breakdown]`, and ensures inline vocal parentheticals like `(whispered)`, `(belted)`, `(key change)`, `(half-time feel)` are recognized without false flags.
   - `tests/run_tests.py`:
     - Test suite runs 63 deterministic tests passing with 100% success rate (Avg Poetry Score: 98.2/100, Avg Suno Score: 99.9/100). All existing tests must remain 100% passing.

---

## 2. Logic Chain

1. **Premise 1: Meta-Spec v8 is the single source of truth for AI music generation.**
   The meta-spec v8 synthesizes all developments across Suno v4.5/v5.5, Udio v4, Google Flow Music (Lyria 3.5), audio engineering post-production, streaming metrics, and quality validation into a unified 6-step lifecycle with 10 AI Quality Gates.

2. **Premise 2: The current repository skills and references represent an earlier v3.5/v4 Suno-only subset.**
   Current files (`skills/ukrainian-poetry-to-suno/SKILL.md`, `references/full-guide.md`, `song-structure-pack.md`, etc.) lack the multi-platform capabilities (Udio v4, Flow Music Lyria 3.5), the 6-step lifecycle, the Vance Powell extension workflow, DAW stem engineering, True Peak mastering, and the 10 Quality Gates.

3. **Premise 3: Existing Ukrainian poetic principles and test suites must be 100% preserved.**
   All 6 Core Poetic Principles, stress capitalization (`вИпадок`, `дорОга`), bracket syntax `[...]` vs parentheses `(...)`, and all 63 existing unit and tier tests must remain intact with zero regressions.

4. **Inference & Strategy: Systematic multi-file update across 4 primary domains:**
   - **Domain A (Core Skill Architecture & Documentation)**: Upgrade `skills/ukrainian-poetry-to-suno/SKILL.md`, `references/full-guide.md`, `skills/poetry-skill/SKILL.md`, `AGENTS.md`, and `GEMINI.md` to incorporate the 6-step lifecycle, multi-platform prompts, DAW mixing, and 10 Quality Gates.
   - **Domain B (Reference Guides & Specialized Packs)**: Upgrade `references/mood-to-style-map.md`, `references/reference-to-style-cheatsheet.md`, `references/prompt-builder.md`, `references/song-structure-pack.md`, `references/lyrics-to-suno-template.md`, `references/suno-prompt-anti-patterns.md`, and `references/rubric.md`.
   - **Domain C (Repository Mirrored Files & Plugin Distribution)**: Synchronize root mirror files (`ukrainian-poetry-to-suno.md`, `song-structure-pack.md`, `lyrics-to-suno-template.md`, `suno-prompt-anti-patterns.md`, etc.), `.agents/skills/`, and the active plugin directory `C:\Users\sm9sh\.gemini\config\plugins\poetry-skill\`.
   - **Domain D (Validation Engine & Test Rigor)**: Update `tests/validator/metatag_validator.py` and `tests/validator/rubric_scorer.py` as needed; verify `tests/run_tests.py` maintains 100% pass rate.

---

## 3. Caveats

- **No Code Modifications in Explorer Turn**: Per Explorer read-only role constraints, no source code or guide files were modified in this turn; all detailed analysis and proposed structures are documented in this report.
- **Platform Licensing Rules**: Udio Pro ($30/mo) is strictly required for commercial rights (Standard $10/mo has none), while Suno Pro ($10/mo) includes commercial rights, and Google Flow Music currently provides 500 daily credits on free tier with commercial rights. These distinct platform policies must be clearly highlighted.
- **External Plugin Sync Dependency**: Updates must be copied to `C:\Users\sm9sh\.gemini\config\plugins\poetry-skill\` to ensure the live environment immediately reflects the v8 architecture.

---

## 4. Conclusion & Actionable File-by-File Implementation Map

### 4.1 File Inventory & Required Changes Matrix

| File Path | Current Status | Required Updates from Meta-Spec v8 |
| :--- | :--- | :--- |
| `skills/ukrainian-poetry-to-suno/SKILL.md` | Suno v3.5/v4 basic style prompts (80-180c) | Complete v8 integration: 6-step lifecycle, Suno v4.5/v5.5 Method 1 & 2, Udio v4 specs, Flow Music Lyria 3.5 specs, Extensions roadmap, DAW stem mixing checklist, Mastering without TP trap, 10 Quality Gates table. |
| `skills/ukrainian-poetry-to-suno/references/full-guide.md` | Basic Suno guide | Exhaustive engineering manual containing all 10 sections of `ai-music-generation-meta-spec-v8.md`. |
| `skills/ukrainian-poetry-to-suno/references/prompt-builder.md` | 6-block Suno builder | Multi-platform builder: Suno Method 1 & 2 (HookGenius 5 modules), Udio v4 formula, Flow Music Lyria 3.5 conversational prompt, plus failure mode remedies. |
| `skills/ukrainian-poetry-to-suno/references/mood-to-style-map.md` | 8 mood clusters | Expand mood mappings to support multi-platform outputs (Suno Conversational / Tag-based, Udio, Flow Music) and tempo/vocal anchors. |
| `skills/ukrainian-poetry-to-suno/references/reference-to-style-cheatsheet.md` | Reference translation table | Add Melodic Math hook deconstruction (Melodic Previews, Glue Hooks) and multi-platform safe prompts. |
| `skills/ukrainian-poetry-to-suno/references/song-structure-pack.md` & root `song-structure-pack.md` | Standard section markers | Add full structural metatags (`[Vocal Intro]`, `[Beat Drop]`, `[Verse 2 - Vance Powell]`, `[Post-Chorus]`, `[Breakdown]`, `[Mega-Chorus]`), inline vocal parentheticals, and Udio Inpainting `*stars*`. |
| `skills/ukrainian-poetry-to-suno/references/lyrics-to-suno-template.md` & root `lyrics-to-suno-template.md` | Single Custom Mode template | Multi-platform templates: Suno Custom Mode (Method 1 & 2), Udio v4 template, Flow Music Conversational Agent template, Seed & Extend roadmap. |
| `skills/ukrainian-poetry-to-suno/references/suno-prompt-anti-patterns.md` & root `suno-prompt-anti-patterns.md` | Top 10 Suno anti-patterns | Add Failure Modes for Suno v4.5/v5.5 (Lyrics Rushing, Sterile Vocals, Negation Trap), Udio Context Length traps, Flow Music limitations, True Peak mastering trap, and Playlist Placement Trap. |
| `skills/ukrainian-poetry-to-suno/references/rubric.md` & root `suno-style-rubric.md` | 100-point Suno rubric | Incorporate 10 AI Quality Gates verification criteria. |
| `skills/poetry-skill/SKILL.md` | Master routing | Update to reflect v8 capabilities (6-step lifecycle, multi-platform Suno/Udio/Flow, DAW engineering, 10 Quality Gates). |
| `AGENTS.md` & `GEMINI.md` | Global directives | Synchronize with v8 directives for multi-platform prompt engineering and 10 Quality Gates. |
| `ukrainian-poetry-to-suno.md` (root) | Outdated v3.5/v4 mirror | Mirror updated `skills/ukrainian-poetry-to-suno/references/full-guide.md`. |
| `tests/validator/metatag_validator.py` | Validates standard brackets | Add new structural prefixes (`vocal intro`, `beat drop`, `mega-chorus`, `megachorus`, `breakdown`) and ensure full compatibility with inline vocal gestures. |
| `.agents/skills/...` | Local workspace mirrors | Mirror all updated skills. |
| `C:\Users\sm9sh\.gemini\config\plugins\poetry-skill\...` | Plugin distribution | Synchronize all updated skills, AGENTS.md, and GEMINI.md. |

---

### 4.2 Detailed Architectural Implementation Guidance for Workers

#### A. 6-Step Lifecycle Breakdown
1. **Step 1: Deep Reference Reverse Engineering**:
   - Genre Complexes: Base + subgenre crossover (e.g. `indie rock, post-punk revival, gritty garage vibe`).
   - BPM Range: Exact tempo anchors (e.g. 120–128 BPM or 75–85 BPM) to prevent genre drift.
   - Sonic Aesthetic & Palette: Concrete instrument timbres and recording textures (`fuzzy analog bass, lo-fi tape hiss, warm console`).
   - Vocal Triple-Stack: Character (`raw passionate male tenor`) + Delivery (`intimate, dry, conversational`) + FX (`sansamp vocal distortion, tape slap`).
   - Melodic Math: Melodic Previews, Glue Hooks, Nano Hooks, suspense chords in intro.
   - Bracketed Layout: Explicit section tags dictating arrangement dynamics.

2. **Step 2: AI-Optimized Lyrics Writing**:
   - Syllable symmetry: Mirror syllable counts (8-8-8-8, 10-8-10-8) forcing downbeat alignment.
   - Spoken Prosody Test: Reading lyrics aloud at conversational speed before generation.
   - Spatial contrast: Verse Staccato (short, punchy words) vs Chorus Legato (open soaring vowels `Ooooh, Aaah`).
   - 5-Second Rule: Vocal intro / acapella hook (`[Vocal Intro]`) to beat the skip rate.
   - 50-Second Rule: First full chorus must appear within the first 50 seconds.
   - Cognitive limit: $\le 3\text{--}4$ unique melodic themes per track.

3. **Step 3: Multi-Platform Prompt Engineering**:
   - **Suno v4.5 / v5.5**:
     - *Method 1 (Conversational Paragraph)*: «First 5 Words» rule ($80\%$ attention). `[Genre & Subgenre] + [Vocal Character] + [Instruments] + [Mood/Energy] + [Aesthetic & BPM]`.
     - *Method 2 (Tag-Based Matrix - HookGenius)*: 5 modules: `[1. Genre/Subgenre], [2. Mood/Energy], [3. Vocal Triple-Stack], [4. Lead Instruments], [5. Production Aesthetic, BPM]` (8–15 tags, $\le 200$ chars).
     - *Failure Modes*: Lyrics Rushing $\to$ 4–8 words/line + `(half-time feel)`; Sterile Vocals $\to$ Vocal Triple-Stack; Negation Trap $\to$ positive hyper-specificity (`purely acoustic, solo piano`).
     - *System Features*: My Taste, Voices cloning (Pro/Premier), Custom Models (up to 3).
     - *Commercial Rights*: Pro ($10/mo) / Premier ($30/mo).
   - **Udio v4**:
     - 48 kHz stereo, 10 min continuous generation, Context Length up to 15 min.
     - Prompt Formula: `[Main Genre], [Sub-Genre], [Year/Era], [Vocal Timbre & Character], [Analog Production Style], [Acoustic Space, BPM]`.
     - Context Length: 10–15s for abrupt transitions/genre shifts; max for continuity.
     - Inpainting: `*stars*` syntax for surgical word/line replacement.
     - Commercial Rights: Strictly on Pro ($30/mo).
   - **Google Flow Music (Lyria 3.5)**:
     - DeepMind Lyria 3.5 engine; 500 daily free credits with commercial rights.
     - Conversational Agent Prompt: `[Concept & Style] + [Artist/Vibe Ref] + [Instruments] + [Dynamics & Vocals]`.
     - Features: Spaces (in-browser apps), Turntable (DJ mixing/scratching), Section Replace, AI Cover, Gemini Omni Flash synchronized video clip generation.

4. **Step 4: Step-by-Step Extensions Roadmap (The AI Conductor)**:
   - Seed (30–50s): Vocal Intro / Hook-first entry $\to$ verify groove.
   - Extend: Add `[Pre-Chorus]` and `[Chorus]`.
   - Verse 2 Development (Vance Powell rules): Add `[Verse 2 - add driving tambourine, syncopated backing vocals, stereo guitar riffs]`.
   - Breakdown & Mega-Chorus: `[Breakdown]` (15–20s bass/vocal strip) $\to$ `[Mega-Chorus - maximum energy, layered harmonies]`.
   - Outro: Short fading outro $\le 20$s.

5. **Step 5: Engineering DAW Post-Production & Stem Mixing**:
   - Stem Splitting: Moises, RipX, LALAL.AI.
   - Phase Alignment: Kick & Bass mono polarity check / FUSER plugin.
   - Frequency Unmasking: Dynamic sidechain EQ (Trackspacer / Neutron Unmask) dipping bass during kick hits.
   - Split Compression for Bass: Sub-Bass $<200\text{ Hz}$ brickwall limiter; Mid-High $>200\text{ Hz}$ dynamic saturated compression.
   - Tchad Blake Parallel Distortion: Distorted drums routed directly to Master Fader (bypassing Drum Bus) to protect headroom.
   - Dynamic Mid-Side Vocal Reverb Sidechain: Sidechain compressor dipping reverb 3–6 dB during active singing in Mid channel only.

6. **Step 6: Mastering & Algorithmic Streaming Distribution**:
   - True Peak Trap Elimination: Loud masters ($-6\dots-8\text{ LUFS}$) must disable True Peak limiting and set ceiling to $-1\text{ dBTP}$ (or $-0.2\text{ dB}$); target $-14\text{ LUFS}$ only if $-2\text{ dBTP}$ is mandatory.
   - Genre Skip Rate Thresholds: Pop $>48\%$, Hip-hop $>44\%$, Electronic $>37\%$, Indie Rock $>31\%$, absolute alarm threshold $>45\%$.
   - Completion Rate: $>55\text{--}60\%$ with track duration 2:30–4:00.
   - Save Rate: $>20\%$.
   - Abolish Playlist Placement Trap: Direct ad traffic solely to individual singles.
   - Spotify Tools: Canvas (8s loops), Discovery Mode, Marquee.

7. **10 AI Quality Gates**:
   - Gate 1: Anti-Skip 5s (Vocal Intro / Hook within 5s).
   - Gate 2: 50s Chorus Rule (Chorus arrives $\le 50$s).
   - Gate 3: Word Naturalness & Spoken Prosody Test.
   - Gate 4: Sectional Space Contrast (Verse Staccato vs Chorus Legato).
   - Gate 5: Verse 2 Development (Vance Powell percussion/backing add).
   - Gate 6: Breakdown & Climax (15-20s energy reset before mega-chorus).
   - Gate 7: Low-End Split Compression (Sub $<200\text{ Hz}$ vs Mid-High $>200\text{ Hz}$ + Kick unmasking).
   - Gate 8: Tchad Blake Drum Distortion Routing (Parallel distortion directly to Master).
   - Gate 9: Mastering True Peak ($-1\text{ dBTP}$ for $-6\dots-8\text{ LUFS}$ or $-14\text{ LUFS}$ for $-2\text{ dBTP}$).
   - Gate 10: Single-Only Ad Campaigns (Eliminating Playlist Placement Trap).

---

## 5. Verification Method

### 5.1 Deterministic Test Suite Execution
Run the full test suite from the repository root:
```bash
py -3 tests/run_tests.py --all
```
**Expected Outcome**: 63+ passed test cases, 0 failures, 100% success rate, Poetic Rubric Score $\ge 95/100$, Suno Score $\ge 95/100$.

### 5.2 Specific File Inspection Points
1. `skills/ukrainian-poetry-to-suno/SKILL.md`: Verify inclusion of the 6-step lifecycle, Suno v4.5/v5.5 Method 1 & 2, Udio v4 specs, Flow Music Lyria 3.5 specs, DAW stem mixing checklist, Mastering without TP trap, and 10 Quality Gates table.
2. `skills/ukrainian-poetry-to-suno/references/full-guide.md`: Verify full synchronization with the 10 sections of `ai-music-generation-meta-spec-v8.md`.
3. `AGENTS.md` & `GEMINI.md`: Verify updated operational directives covering multi-platform prompt generation and quality gates while preserving the 6 Poetic Principles and stress capitalization standards.
4. `tests/validator/metatag_validator.py`: Verify that `[Vocal Intro]`, `[Beat Drop]`, `[Mega-Chorus]`, `[Breakdown]`, and inline parentheticals `(whispered)`, `(belted)`, `(key change)` pass validation cleanly without errors.
5. Plugin sync directory: Verify all changes are copied to `C:\Users\sm9sh\.gemini\config\plugins\poetry-skill\`.

### 5.3 Invalidation Conditions
- Any degradation or syntax error causing `py -3 tests/run_tests.py --all` to fail.
- Any relaxation of the 6 Core Poetic Principles, Ukrainian stress capitalization (`вИпадок`, `дорОга`), or the bracket `[...]` vs parentheses `(...)` rule.
- Any omission of platform specifications (Suno v4.5/v5.5, Udio v4, Flow Music Lyria 3.5) or Quality Gates 1–10.

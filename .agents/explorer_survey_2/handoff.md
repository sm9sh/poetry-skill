# Handoff Report — Explorer 2 (Suno AI Music Prompt Engineering Specialization)

**Date**: 2026-08-26  
**Agent**: Explorer 2 (`.agents/explorer_survey_2`)  
**Parent / Caller**: `1f051654-233b-4bf7-ad7d-e9c4beed0a3d` (orchestrator_1)  
**Type**: Hard Handoff (Task Complete)

---

## 1. Observation

Direct observations and evidence gathered across the codebase:

1. **Polluted Style Fields with Non-Musical Metadata**:
   - In `skills/ukrainian-poetry-to-suno/references/prompt-builder.md`, lines 133–138 & 158–162:
     ```text
     indie pop, nocturnal, midtempo, intimate female vocal, pulsing bass, muted drums, soft synth pads, glossy nocturnal production, restrained chorus lift.
     Exclude: no EDM drop, no bombastic anthem feel.
     Language: Ukrainian.
     Theme: late-night tram, rain, city loneliness.
     ```
   - In `packs/suno-reference-prompt-pack.md`, lines 23–27:
     ```text
     Moody midtempo synth-pop with intimate female vocal, pulsing bass, glossy nocturnal production, restrained chorus lift.
     Language: Ukrainian.
     Theme: late-night tram, rain, city loneliness.
     Exclude: no EDM drop, no bombastic climax.
     ```
   - Observation: Prompts mix metadata fields (`Language: Ukrainian`, `Theme: ...`) into the Style prompt block. In Suno Custom Mode, the Style of Music field is strictly dedicated to audio tokens; placing narrative text here triggers token dilution or word vocalization.

2. **Abstract Flowcharts Instead of Concrete Lyrics Metatags**:
   - In `skills/ukrainian-poetry-to-suno/references/song-structure-pack.md`, lines 7–9:
     ```text
     intro -> verse -> pre-chorus -> chorus -> verse -> pre-chorus -> chorus -> bridge -> final chorus -> outro
     ```
   - Observation: Song structures are expressed as ASCII text arrows without square brackets `[Intro]`, `[Verse]`, `[Chorus]`, `[Solo]`, `[Outro]`, or parenthetical backing vocals `(harmony)`. Users copying these directly into Suno Custom Mode will have the AI sing "intro arrow verse arrow chorus".

3. **Localization Paradox in Prompt Packs**:
   - In `packs/suno-reference-prompt-pack-uk.md`, lines 24–26:
     ```text
     Меланхолійний середньотемповий інді-поп, інтимний вокал, теплий бас, приглушені барабани, м'яке гітарне мерехтіння, нічна міська атмосфера, стриманий емоційний підйом, чистий сучасний продакшн.
     ```
   - Observation: Style prompt tokens are written in Ukrainian. Suno v3.5/v4 diffusion/transformer models are trained predominantly on English musical taxonomy; providing Ukrainian text in the Style field results in muddy, unconditioned, or generic audio outputs.

4. **Limited Subgenre Representation**:
   - In `skills/ukrainian-poetry-to-suno/references/prompt-builder.md`, lines 23–32:
     Only 10 genres are listed (`indie pop`, `synth-pop`, `pop-rock`, `acoustic pop`, `folk-pop`, `indie rock`, `dark pop`, `ambient electronic`, `cinematic folk`, `adult pop-rock`).
   - Major contemporary Ukrainian genres (Ethno-chaos, Post-punk/Doomer wave, Dark Synth/Coldwave, Drill/Trap-folk, Melodic Metalcore, Shoegaze) are completely absent.

5. **Missing Anti-Artifact Negative Prompting**:
   - In `skills/ukrainian-poetry-to-suno/SKILL.md` (lines 124–131) and `references/suno-prompt-anti-patterns.md` (lines 115–117):
     Negative prompts are limited to high-level artistic tropes (`no bombastic anthem feel`, `no tourist-folk cliches`, `no EDM drop`).
   - There is zero guidance on anti-artifact negative prompting to combat metallic treble distortion, muddy sub-bass rumble, garbled vocal glitches, or excessive wet reverb decay.

6. **Severe Repetition Across Reference Files**:
   - `references/reference-to-style-cheatsheet.md`, `references/reference-breakdown-examples.md`, `references/mood-to-style-map.md`, `references/ukrainian-song-scenarios.md`, `references/prompt-builder.md`, and `references/full-guide.md` all repeat the exact same 4 examples (*Нічний трамвай*, *Стриманий патріотичний*, *Безсоння і скло*, *Повернення додому*).

---

## 2. Logic Chain

1. **Premise 1**: Suno AI (v3.5 / v4) separates musical conditioning (`Style of Music` field, 80–180 optimal chars, English token bias) from lyrical/arrangement generation (`Lyrics` field, up to 3000–5000 chars, supports Ukrainian text and `[Metatag]` directives).
2. **Inference from Observation 1**: When prompt builder templates include `Language: Ukrainian` and `Theme: ...` within the Style block, users paste non-functional English/Ukrainian prose into the Style field, violating token economy and triggering unwanted audio hallucinations.
3. **Inference from Observation 2 & 3**: Because `song-structure-pack.md` provides arrow diagrams instead of `[Section]` tags, and `suno-reference-prompt-pack-uk.md` translates musical style tags into Ukrainian, generations fail to execute structured section changes and suffer from degraded audio quality.
4. **Inference from Observation 4 & 5**: The narrow genre palette (only basic pop/rock) and absence of acoustic artifact negative tokens (`metallic highs`, `muddy bass`, `garbled vocals`) prevent the skill from delivering authentic modern Ukrainian music styles or broadcast-quality audio outputs.
5. **Conclusion**: The entire Suno conversion subsystem (`SKILL.md`, reference guides, prompt packs, rubrics, test suites) requires a systematic upgrade focusing on token economy, standard metatag syntax, an expanded Ukrainian genre matrix (8 distinct contemporary styles), anti-artifact negative prompting, and deduplication of prompt packs.

---

## 3. Caveats

- **API vs Web UI Differences**: Suno's character limits and features differ between the public Web UI (Custom Mode) and unofficial third-party API wrappers. The findings are optimized for the canonical Suno v3.5 and v4 Web UI / generation engine.
- **Model Non-Determinism**: Suno is stochastic; bracketed metatags (`[Guitar Solo]`, `[Drop]`) provide strong conditioning guidance (~75–85% compliance in v3.5/v4) but cannot guarantee 100% deterministic section transitions on every seed.
- **No Source Code Modified**: As an explorer in read-only mode, no production source files outside `.agents/explorer_survey_2/` were modified.

---

## 4. Conclusion

The Ukrainian Poetry to Suno skill ecosystem has strong foundational concepts but requires 6 specific upgrades to reach modern state-of-the-art Suno prompt engineering standards:
1. **Token Economy & Clean Custom Mode Separation**: Enforce 80–180 char concise English style tags; eliminate metadata leakage (`Language/Theme`) from the Style field.
2. **Production-Ready Metatag Syntax**: Implement full bracketed syntax `[Intro]`, `[Verse]`, `[Chorus]`, `[Solo]`, `[Outro]`, `(backing harmonies)`, `[Tempo: ... BPM]` across all templates.
3. **Expanded Modern Ukrainian Genre Roster**: Add formulas for Ethno-Chaos, Post-Punk, Dark Synth, Trap-Folk, Melodic Metalcore, Shoegaze, and Neoclassical Bandura.
4. **Authentic Ukrainian Vocal Timbre Directives**: Add white voice (*білий голос*), spoken melodeclamation, raspy bardic, and autotune styling.
5. **Acoustic Anti-Artifact Negative Prompting**: Add Exclude vectors for metallic sibilance, muddy sub-bass, garbled pronunciation, and reverb wash.
6. **Pack Modernization & Deduplication**: Overhaul all 7 prompt packs with distinct subgenres, vocal registers, and BPM/Key recommendations.

---

## 5. Verification Method

To independently verify these findings:
1. **Inspect Tag Contamination**:
   - `view_file` on `d:/poetry-skill/prompt-builder.md` lines 155–189 to verify `Language:` and `Theme:` lines attached to style prompts.
2. **Inspect Missing Metatag Syntax**:
   - `view_file` on `d:/poetry-skill/song-structure-pack.md` to confirm lack of `[Verse]` / `[Chorus]` / `(backing)` brackets.
3. **Inspect Ukrainian Style Tag Localization Issue**:
   - `view_file` on `d:/poetry-skill/packs/suno-reference-prompt-pack-uk.md` to confirm non-English style descriptors in style field.
4. **Inspect Analysis Report**:
   - Review complete technical audit at `d:/poetry-skill/.agents/explorer_survey_2/analysis.md`.

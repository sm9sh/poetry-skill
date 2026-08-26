# Handoff Report — Explorer 3 (Edge Case, Stress-Test & Test Infra Specialization)

**Agent ID**: `188a4db1-21c7-45d2-9c1d-089b0df60a5a` (`explorer_survey_3`)  
**Recipient**: Project Orchestrator (`1f051654-233b-4bf7-ad7d-e9c4beed0a3d`)  
**Working Directory**: `d:/poetry-skill/.agents/explorer_survey_3`  
**Date**: 2026-08-26  

---

## 1. Observation

1. **Repository Layout & Duplication**:
   - Running MD5 hash comparison across the repository identified 22 exact duplicate file pairs between root and `skills/` subdirectories.
   - Example 1: `d:/poetry-skill/packs/dark-pack.md` and `d:/poetry-skill/skills/ukrainian-poetry-to-suno/references/packs/dark-pack.md` both share MD5 `6ADB99E36BAA709323DDA09F9F8327CB`.
   - Example 2: `d:/poetry-skill/ukrainian-poetry-skill-tests.md` and `d:/poetry-skill/skills/ukrainian-poetry/references/tests.md` both share MD5 `A079A2488B966217DE2FCF578EF6CDDC` (178 lines, 6,679 bytes).
   - Example 3: `d:/poetry-skill/suno-prompt-tests.md` and `d:/poetry-skill/skills/ukrainian-poetry-to-suno/references/tests.md` both share MD5 `0558D8E84AD31D1E57BC10BBFBC4A65D` (174 lines, 6,304 bytes).
   - Example 4: `d:/poetry-skill/ukrainian-poetry-skill-stress-pack.md` and `d:/poetry-skill/skills/ukrainian-poetry/references/stress-tests.md` both share MD5 `3B36E7E6EA1DB49FCE3236FD93F853BD` (212 lines, 8,058 bytes).
   - Legacy files in `source/legacy-skills/` (`ukrainian-poetry.md`, `ukrainian-poetry-to-suno.md`) and root (`ukrainian-poetry-skill-uk.md`, `ukrainian-poetry-skill.md`, `ukrainian-poetry-skill-lite.md`, `ukrainian-poetry-to-suno.md`) exhibit divergence in line counts and headers compared to `skills/<name>/SKILL.md` and `skills/<name>/references/full-guide.md`.

2. **Existing Test Suite Coverage**:
   - `skills/ukrainian-poetry/references/tests.md` contains 21 test prompts across 6 sections: Базові тести (1-5), Тести на тон і стиль (6-9), Тести на форму (10-12), Тести на антиштампи (13-15), Тести на редагування (16-18), and Стрес-тести (19-21).
   - `skills/ukrainian-poetry/references/stress-tests.md` contains 15 stress scenarios focused on forbidden words, tone control, and prose-to-poem conversion.
   - `skills/ukrainian-poetry-to-suno/references/tests.md` contains 16 test prompts focused on theme-to-prompt, reference de-identification, and custom split.
   - None of these test suites contain tests for: rare ternary meters (Dactyl, Anapest), accentual verse/dolnik, multilingual/bilingual code-switching lyrics, multi-phase dynamic song structures (acoustic-to-electronic drops, tempo accelerandos), or strict Suno <=120 character Style Box caps.

3. **Current Instruction Constraints & Failure Modes**:
   - In `skills/ukrainian-poetry/SKILL.md:99-100`, meter rules state: *"Prefer iamb for balanced reflection, trochee for song-like drive, amphibrach for soft lyric movement, anapest for lift..."* but provide no structural guidance for stress-tracking or accentual dolnik.
   - In `skills/ukrainian-poetry-to-suno/SKILL.md:58-60`, prompt formula states: *"Build Style of music in this order when possible: genre + mood + tempo/energy + vocal + instrumentation + production + optional structure"* without enforcing character cap limits for Suno's UI style field or preventing token truncation.

---

## 2. Logic Chain

1. **From Layout Duplication (Obs 1) to Maintenance Risk**:
   - Having 22 identical files in the repository root alongside the modular `skills/` directories creates severe desynchronization risk. Any worker editing files in `skills/...` without updating root files leaves the project in an inconsistent state.
   - *Inference*: The project must establish `skills/ukrainian-poetry/` and `skills/ukrainian-poetry-to-suno/` as the single canonical source of truth.

2. **From Test Suite Coverage Analysis (Obs 2) to Real-World Failure Vulnerabilities**:
   - While simple prompts succeed, production song requests require complex verse mechanics (dolnik, ternary meters, bilingual choruses) and dynamic audio engineering cues (`[Tempo Change]`, `[Acoustic Verse -> Electronic Drop]`).
   - *Inference*: The absence of tests for these domains leaves both skills vulnerable to silent failures (hallucinated stresses, metric collapse, audio artifacts).

3. **From Instruction Gaps (Obs 3) to Concrete Failure Modes**:
   - Lack of explicit stress-preservation guardrails causes LLMs to force unnatural word accents (FM-P1: `вікна́`, `роблю́`).
   - Lack of token economy caps in Suno style instructions causes the model to generate >200 char descriptions that Suno truncates (FM-S1).
   - *Inference*: Skill instructions and reference cheatsheets must be hardened with explicit guardrails, and verified through a dedicated 4-tier E2E testing framework.

---

## 3. Caveats

- **Audio Generation Output Testing**: Suno AI audio generation itself requires external API credits and manual listening. The E2E test framework evaluates prompt generation, token economy, syntax compliance, metatag correctness, and linguistic authenticity deterministically and via LLM-as-a-judge rubrics.
- **Root File Cleanup Execution**: In accordance with the read-only exploration constraint, no project source/reference files were modified or deleted in this turn. File reorganization and duplication cleanup are scoped for the upcoming implementation milestones.

---

## 4. Conclusion

1. **Repository Structure**: Root-level duplicated reference files (`packs/`, `*-rubric.md`, `*-tests.md`, `*-template.md`) must be consolidated to the canonical `skills/` reference folders to eliminate synchronization divergence.
2. **Failure Mode Guardrails**: 14 critical failure modes (FM-P1 to FM-P7 for poetry, FM-S1 to FM-S7 for Suno) must be addressed in the updated `SKILL.md` instructions, including stress preservation, non-grammatical rhyming, anti-sharovarshchyna guardrails, <=120 char Style Box caps, and standard structural metatags.
3. **4-Tier E2E Testing Framework**: Both skills require an expanded test suite spanning:
   - **Tier 1**: Feature Coverage (all 9 poetic modes and 5 Suno workflows).
   - **Tier 2**: Boundary & Corner Cases (6-word taboo bans, rare meters, extreme BPM, 120-char style caps).
   - **Tier 3**: Cross-Feature Combinations (full end-to-end brief -> lyrics -> Suno Custom Mode pipeline).
   - **Tier 4**: Real-World Production Scenarios (commercial folk-pop single, cinematic soundtrack, animated children's song, memorial chronicle anthem).
4. **Backward Compatibility**: A baseline acceptance threshold of `>= 85/100` for all 21 existing poetry tests and 100% compliance for existing Suno and stress tests has been defined.

---

## 5. Verification Method

To independently verify all observations, data points, and findings:

1. **Verify File Duplication & MD5 Hashes**:
   ```powershell
   Get-FileHash -Algorithm MD5 (Get-ChildItem -Recurse -File -Exclude .git*).FullName | Format-Table -AutoSize
   ```
   Compare hashes of `packs/*`, `ukrainian-poetry-skill-tests.md`, `suno-prompt-tests.md`, and their counterparts in `skills/.../references/`.

2. **Verify Test Suite Line Counts & Contents**:
   ```powershell
   Get-Content "d:/poetry-skill/skills/ukrainian-poetry/references/tests.md" | Measure-Object -Line
   Get-Content "d:/poetry-skill/skills/ukrainian-poetry-to-suno/references/tests.md" | Measure-Object -Line
   Get-Content "d:/poetry-skill/skills/ukrainian-poetry/references/stress-tests.md" | Measure-Object -Line
   ```

3. **Inspect Complete Analysis Report**:
   Inspect `d:/poetry-skill/.agents/explorer_survey_3/analysis.md` for full taxonomy tables, gap analyses, and E2E test runner specifications.

---

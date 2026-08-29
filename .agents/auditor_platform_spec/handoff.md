# Forensic Audit Report: Prompt & Platform Spec Auditor (Agent 1)

**Work Product**: Platform Prompt Specifications, Custom Mode Payloads, Bracket Grammar, Metatag Validators, and Reference Ecosystem for Suno AI (v4.5/v5.5), Udio AI (v4), and Google Flow Music (Lyria 3.5).
**Profile**: General Project (Integrity Mode: `development`)
**Verdict**: **CLEAN**

---

## 1. Observation

Direct empirical inspection of the codebase, authoritative meta-spec `ai-music-generation-meta-spec-v8.md`, skill documentation, references, root mirrors, and test suites yielded the following verified facts:

### 1.1 Suno AI (v4.5 / v5.5) Specification Integrity
- **Method 1: Conversational Paragraph with «First 5 Words» Rule (80% Attention)**:
  - Formulated in `skills/ukrainian-poetry-to-suno/SKILL.md` (lines 88–90), `references/full-guide.md` (lines 131–133), `references/prompt-builder.md` (lines 24–32), `references/lyrics-to-suno-template.md` (lines 18–20), and mirrored in root files `ukrainian-poetry-to-suno.md`, `prompt-builder.md`, `lyrics-to-suno-template.md`.
  - Formula: `[Genre & Subgenre] + [Vocal Character] + [Instruments] + [Mood/Energy] + [Aesthetic & BPM]` with the opening 4–5 words capturing dominant genre and vocal archetype.
- **Method 2: Tag-Based Matrix (HookGenius 5 Modules)**:
  - Formulated in `SKILL.md` (lines 91–93), `full-guide.md` (lines 134–136), `prompt-builder.md` (lines 34–42), and root mirrors.
  - Formula: `[1. Genre/Subgenre], [2. Mood/Energy], [3. Vocal Triple-Stack], [4. Lead Instruments], [5. Production Aesthetic, BPM]` (8–15 precise tags, 80–180 chars optimal, $\le 200$ chars).
- **Technical Character Limits**:
  - `Style of Music`: Hard cap 1000 chars, optimal range 80–180 chars; `Lyrics`: Hard cap 5000 chars. Confirmed in `SKILL.md` (line 87), `full-guide.md` (line 130), `prompt-builder.md` (line 12), and `tests/validator/suno_validator.py` (`SUNO_MAX_STYLE_CHARS = 1000`, `SUNO_MAX_LYRICS_CHARS = 5000`).
- **System Features**:
  - *My Taste* (personalized genre adaptation), *Voices* (vocal cloning on Pro/Premier), and *Custom Models* (up to 3 custom models) explicitly specified in `SKILL.md` (line 94) and `full-guide.md` (line 137).
- **Failure Modes & Deterministic Remedies**:
  - *Lyrics Rushing*: 4–8 words/line, BPM anchoring, and inline `(half-time feel)` command (`SKILL.md` line 96, `suno-prompt-anti-patterns.md` section 6).
  - *Robotic / Sterile Vocals*: Compulsory Vocal Triple-Stack (**Character** + **Delivery** + **FX**) (`SKILL.md` line 97, `suno-prompt-anti-patterns.md` section 7).
  - *The Negation Trap*: Prohibition of "no drums" / "without guitar" in favor of positive hyper-specificity (`purely acoustic, solo piano, isolated vocals, sparse arrangement`) (`SKILL.md` line 98, `suno-prompt-anti-patterns.md` section 8).
- **Commercial Licensing**:
  - Commercial monetization rights on Pro ($10/mo) and Premier ($30/mo); non-commercial on Free plan (`SKILL.md` line 99, `full-guide.md` line 142).

### 1.2 Udio AI (v4) Specification Integrity
- **Audio Quality & Generation Bounds**:
  - **48 kHz stereo quality**, continuous track generation **up to 10 minutes** without musical drift, total extension length (Context Length) **up to 15 minutes** (`SKILL.md` line 102, `full-guide.md` line 145, `suno_validator.py` line 48).
- **Context Length Management**:
  - 10–15 seconds for sharp genre/language/tempo transitions vs maximum context for timbre continuity (`SKILL.md` line 104, `full-guide.md` line 147, `prompt-builder.md` line 50, `suno_validator.py` line 47).
- **Inpainting Syntax (`*stars*`)**:
  - Inpainting replacement syntax `*static sky*` specified across all guides (`SKILL.md` line 105, `full-guide.md` line 148, `lyrics-to-suno-template.md` line 10) and programmatically validated for asterisk balance in `tests/validator/suno_validator.py` (`validate_udio_prompt` lines 135–139).
- **Prompt Formula**:
  - `[Main Genre], [Sub-Genre], [Year/Era], [Vocal Timbre & Character], [Analog Production Style], [Acoustic Space, BPM]` strictly within 250 characters (`SKILL.md` line 103, `prompt-builder.md` line 48, `suno_validator.py` `UDIO_MAX_PROMPT_CHARS = 250`).
- **Commercial Licensing**:
  - Commercial rights strictly restricted to Pro plan ($30/mo); Standard plan ($10/mo) has no commercial rights (`SKILL.md` line 106, `full-guide.md` line 149).

### 1.3 Google Flow Music (Lyria 3.5) Specification Integrity
- **Engine & Credits**:
  - Powered by Google DeepMind **Lyria 3.5** engine, **500 daily free credits** with full commercial rights, acknowledging the sunset of MusicFX on July 31, 2026 (`SKILL.md` line 109, `full-guide.md` line 152, `suno_validator.py` lines 50–51).
- **Conversational Agent Mode**:
  - Prompt structure: `[Concept & Style Description] + [Atmospheric Reference] + [Instrument Specification] + [Dynamics & Vocal Control]` (`SKILL.md` lines 110–111, `full-guide.md` lines 153–154, `prompt-builder.md` lines 60–66).
- **Platform Features**:
  - *Spaces* (interactive browser music apps/beat-makers), *Turntable* (DJ mixing & live sampling), *Section-Level Replace* (timestamp isolate e.g. 1:12–1:35 and replace words/language/instrumentation without re-recording the full track), *AI Cover* (genre transformations), and *Gemini Omni Flash* (tempo- and mood-synchronized music video generation) (`SKILL.md` lines 112–117, `full-guide.md` lines 155–157).

### 1.4 Metatags in `[...]` vs Inline Vocal Gestures in `(...)`
- **9 Canonical Vocal Gestures in `(...)`**:
  - `(whispered)`, `(belted)`, `(falsetto)`, `(screamed)`, `(ad-lib)`, `(building intensity)`, `(key change)`, `(half-time feel)`, `(harmonized)`, plus backing vocals `(луна)`, `(ніколи знов)` (`SKILL.md` lines 140–150, `full-guide.md` lines 179–190, `song-structure-pack.md` lines 58–73).
  - Explicitly whitelisted in `tests/validator/metatag_validator.py` (`WHITELISTED_VOCAL_GESTURES` lines 56–65).
- **Silent Structural Directives in `[...]`**:
  - `[Intro]`, `[Vocal Intro - dynamic acapella, dry]`, `[Beat Drop]`, `[Verse 1]`, `[Pre-Chorus]`, `[Chorus]`, `[Verse 2 - add driving tambourine, shaker, backing vocals]`, `[Post-Chorus]`, `[Instrumental Break]`, `[Bridge]`, `[Breakdown]`, `[Mega-Chorus]`, `[Outro]`, `[Cold End]`.
- **Exclusion of Instrumental Descriptors from `(...)`**:
  - `tests/validator/metatag_validator.py` defines `INSTRUMENTAL_KEYWORDS_IN_PARENS` (lines 69–76) and intercepts any instrumental term placed inside `(...)` with an explanatory error preventing audio vocalization hallucinations.

### 1.5 Deterministic Verification & Test Execution
- Execution of `py -3 tests/run_tests.py --all`:
  - **63 / 63 test cases PASSED** (0 failures, 100% success rate).
  - Average Poetic Score: **98.2 / 100**.
  - Average Suno Score: **99.9 / 100**.
- Execution of `py -3 -m unittest discover -s tests -p "test_*.py"`:
  - **45 / 45 unit tests PASSED** in 0.443s.
- Execution of `py -3 tests/adversarial_suno_stress_test.py`:
  - **18 / 18 adversarial tests PASSED** (boundary caps, extreme tempos, conflicting constraints, fuzzing injections, and 99 style prompts / 113 exclude prompts / 15 lyrics blocks audited).
- Ecosystem Synchronization:
  - `tests/sync_ecosystem.py` successfully updated all root mirrors, `.agents/skills/`, and the global plugin directory `C:\Users\sm9sh\.gemini\config\plugins\poetry-skill\`.

---

## 2. Logic Chain

1. **Step 1 — Authoritative Baseline Verification**:
   - `ai-music-generation-meta-spec-v8.md` was read as the single source of truth (SSOT) for R4 platform prompt specifications.
2. **Step 2 — Codebase & Documentation Cross-Audit**:
   - Cross-checked `skills/ukrainian-poetry-to-suno/SKILL.md`, `references/full-guide.md`, `references/prompt-builder.md`, `references/song-structure-pack.md`, `references/lyrics-to-suno-template.md`, `references/suno-prompt-anti-patterns.md`, `skills/poetry-skill/SKILL.md`, `AGENTS.md`, and `GEMINI.md`.
   - Verified that every platform feature, limit, failure mode remedy, bracket rule, vocal gesture, and licensing clause is verbatim compliant and accurately explained without contradictions.
3. **Step 3 — Validator Engine Implementation Verification**:
   - Inspected `tests/validator/metatag_validator.py`, `tests/validator/suno_validator.py`, and `tests/validator/style_validator.py`.
   - Verified that validators are genuine algorithmic engines using regex parsers, token bounds, and whitelists, rather than facade implementations or hardcoded results.
4. **Step 4 — Empirical Stress-Testing**:
   - Ran all deterministic suites, unit tests, and adversarial challenger scripts. All tests ran live and passed with 100% success rate.
5. **Step 5 — Verdict Determination**:
   - All Phase 1 forensic checks under Development Mode rules passed with zero integrity violations and zero regressions.

---

## 3. Caveats

- **External Platform Runtime Dependency**: Audio generation is performed by third-party remote inference engines (Suno, Udio, Google Flow Music). The specifications and validators in this repository enforce prompt engineering precision, token economy, syntax cleanliness, and structural alignment to ensure maximum generation quality according to each model's documented behavior.
- **Integrity Mode**: Audited under `development` mode according to `ORIGINAL_REQUEST.md`.

---

## 4. Conclusion

The platform prompt specifications and validator engine for Suno v4.5/v5.5, Udio v4, and Google Flow Music (Lyria 3.5) are fully integrated, consistent across all skill files and root mirrors, compliant with `ai-music-generation-meta-spec-v8.md`, and verified by automated unit and adversarial test suites.

**Verdict**: **CLEAN**

---

## 5. Verification Method

To independently reproduce and verify this audit:

1. **Run full deterministic test suite**:
   ```powershell
   py -3 tests/run_tests.py --all
   ```
   *Expected result*: 63 tests run, 63 passed, 0 failed, avg poetic score $\ge 95/100$, avg suno score $\ge 95/100$.

2. **Run Python standard unit tests**:
   ```powershell
   py -3 -m unittest discover -s tests -p "test_*.py"
   ```
   *Expected result*: 45 tests run, 45 passed, OK.

3. **Run adversarial stress tests**:
   ```powershell
   py -3 tests/adversarial_suno_stress_test.py
   ```
   *Expected result*: 18 adversarial test cases passed.

4. **Verify ecosystem synchronization**:
   ```powershell
   py -3 tests/sync_ecosystem.py
   ```
   *Expected result*: All 16 root mirrors and global plugin files synced.

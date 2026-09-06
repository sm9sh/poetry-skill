# Handoff Report — Challenger 2 (Adversarial Schema, Contracts & Rubric Verifier)

**Agent**: `challenger_2` (Empirical Challenger, Critic / Specialist)  
**Date**: 2026-09-06  
**Working Directory**: `d:\poetry-skill\.agents\challenger_2`  
**Handoff Type**: Hard (Verification & Adversarial Challenge Complete)  
**Verdict**: **REQUEST_CHANGES**

---

## 1. Observation

### 1.1 Master Test Suite & Playground Unit Tests Execution
1. **Adversarial Challenger 2 Test Suite**:
   - Command: `py -3 -m unittest tests/test_adversarial_challenger2.py`
   - Result:
     ```
     .....................
     ----------------------------------------------------------------------
     Ran 21 tests in 0.324s

     OK
     ```
   - Exit code: `0`. All 21 tests passed, including `test_20_subagent_files_and_yaml_frontmatter_schema` which validates all 6 subagents in `skills/ukrainian-poetry/agents/`.

2. **Examples Playground Test Suite**:
   - Command: `py -3 -m unittest tests/test_examples_playground.py`
   - Result:
     ```
     .........
     ----------------------------------------------------------------------
     Ran 9 tests in 0.136s

     OK
     ```
   - Exit code: `0`. All 9 tests passed, verifying file existence, non-emptiness, bracket discipline, Ukrainian stress capitalization, platform constraints (Suno 80-180 chars, Udio <= 250 chars with `*stars*`, Flow Music 65 bpm Spaces), and before/after contrast for all 3 failure guides.

3. **Full System Test Suite**:
   - Command: `py -3 tests/run_tests.py --all`
   - Result: `78 passed, 0 failed, 35 warnings, 100.0% success rate, Avg Poetry: 98.3/100, Avg Suno: 99.7/100`.
   - Exit code: `0`.

4. **Root Cleanliness & Ecosystem Synchronization**:
   - Command: `py -3 tests/sync_ecosystem.py --check`
   - Result: Repository root is 100% clean (0 deprecated root mirror files or `packs/` directory found); `.agents/skills/` and global Gemini plugin directory synced.

---

### 1.2 Verification of `poetry-qa-bot.md` Specification & Edge Cases
- **Locations Verified**: `skills/ukrainian-poetry/agents/poetry-qa-bot.md` and `.agents/skills/ukrainian-poetry/agents/poetry-qa-bot.md` (bit-for-bit identical, verified via `Compare-Object`).
- **YAML Frontmatter**:
  - `name: poetry-qa-bot`
  - `description: ...` (contains `<example>` block and negative constraints `Do NOT use this agent for:`)
  - `model: gemini-2.5-pro`
  - `temperature: 0.2`
  - `max_output_tokens: 4096`
- **Registration**: Registered in `skills/ukrainian-poetry/agents/openai.yaml` and `.agents/skills/ukrainian-poetry/agents/openai.yaml`.
- **Mandatory Sections Present**:
  1. `## 1. Role & Identity`
  2. `## 2. Scope & Boundaries`
  3. `## 3. Input Contract` (YAML schema block with `poem_text`, `target_form`, `target_meter`, `register`, `passing_threshold`, `context_or_intent`)
  4. `## 4. Operational Rules & Heuristics` (6-principle audit matrix, 14-category penalty deduction matrix D01–D14, 7-step scansion protocol, remediation routing engine)
  5. `## 5. Output Contract` (Markdown audit report with 7-dimension scorecard totaling 100 points: 25 + 20 + 15 + 10 + 10 + 10 + 10 = 100)
  6. `## 6. Edge-Case Handling`
- **Edge-Case Handling Audit (Section 6)**:
  - **Free Verse (Верлібр)**: Explicitly instructs not to deduct points for variable line length (`D01`) provided syntagmatic breathing and enjambment weight are preserved; evaluates rhyme section via internal phonics, assonance, and alliteration.
  - **Kolomyika (Коломийка)**: Explicitly enforces strict `(4+4)+6` syllabic structure with mandatory caesura after syllable 8; distinguishes authentic folk speech from tourist kitsch (`шароварщина`).
  - **Historical & Baroque Styles (Історичні та барокові тексти)**: Distinguishes intentional Baroque stylization (Skovoroda, Cossack Baroque: *«всякому городу нрав і права»*) from accidental modern surzhyk or Russian calques.
  - **Song Metatags (Lyrics Handshake)**: Explicitly instructs to ignore structural service tags in square brackets (`[Verse]`, `[Chorus]`) during syllable scansion, but strictly verify accentuation in round parentheses backing vocals `(луна)`.

---

### 1.3 Empirical Bracket vs Parentheses Audit across All Markdown Files
- We executed an automated scanner over all 262 `.md` files in the repository.
- Out of 40 lyrics/song-structure code blocks extracted across the entire codebase:
  - 39 blocks passed `MetatagValidator.validate_lyrics_structure` with 0 errors.
  - **1 block FAILED with 3 errors**.
- **Location of Violation**:
  - `skills/ukrainian-poetry-to-suno/agents/music-lyrics-architect.md` (lines 51–70)
  - `.agents/skills/ukrainian-poetry-to-suno/agents/music-lyrics-architect.md` (lines 51–70)
  - `C:\Users\sm9sh\.gemini\config\plugins\poetry-skill\skills\ukrainian-poetry-to-suno\agents\music-lyrics-architect.md` (lines 51–70)
- **Verbatim Content**:
  ```markdown
  # Output Contract
  ```markdown
  ## 🎼 AI-Optimized Lyrics

  [Intro]
  (ambient build)

  [Verse 1]
  (staccato delivery)
  Line one text hEre
  Line two text hEre

  [Chorus]
  (legato, soaring)
  Line one of chOrus
  Line two of chOrus

  [Outro]
  (fade out)
  ```
- **Verbatim Error Output from `MetatagValidator`**:
  ```json
  [
    "Instrumental descriptor 'staccato delivery' found in parentheses '()'. In Suno AI and Google Flow Music, text in parentheses is read out loud as vocals/ad-libs. Use square brackets '[...]' for musical instructions (e.g. '[Intro - staccato delivery]' or '[staccato delivery]').",
    "Instrumental descriptor 'legato, soaring' found in parentheses '()'. In Suno AI and Google Flow Music, text in parentheses is read out loud as vocals/ad-libs. Use square brackets '[...]' for musical instructions (e.g. '[Intro - legato, soaring]' or '[legato, soaring]').",
    "Instrumental descriptor 'fade out' found in parentheses '()'. In Suno AI and Google Flow Music, text in parentheses is read out loud as vocals/ad-libs. Use square brackets '[...]' for musical instructions (e.g. '[Intro - fade out]' or '[fade out]')."
  ]
  ```

---

## 2. Logic Chain

1. **Directive Contract**: `AGENTS.md` (Section 2, Operational Directives) sets the global standard:
   - `[Square Brackets]`: Used for **ALL structural, instrumentation, and arrangement instructions**. Models parse them as audio directing cues without singing them.
   - `(Round Parentheses)`: Used **EXCLUSIVELY for backing vocals, ad-libs, and vocal delivery gestures** `(whispered)`, `(belted)`, `(falsetto)`, `(screamed)`, `(ad-lib)`, `(building intensity)`, `(key change)`, `(half-time feel)`, `(harmonized)`, `(луна)`, `(ніколи знов)`. Never put instrumental descriptions in parentheses because Google Flow Music and Suno will vocalize/sing them out loud!
2. **Internal Self-Contradiction**: In `skills/ukrainian-poetry-to-suno/agents/music-lyrics-architect.md`:
   - Line 19 states: *"Inserting structure metatags (brackets) and vocal gestures (parentheses)."*
   - Line 49 states: *"Use `[Verse]`, `[Chorus]`, `[Bridge]` for structure. Use `(sigh)`, `(whisper)`, `(breath)`, `(growl)`, `(cry)` for inline vocal gestures."*
   - However, in lines 55–70, its Output Contract template provides an invalid example where:
     - `(ambient build)` puts an instrumental arrangement instruction in round parentheses.
     - `(staccato delivery)` and `(legato, soaring)` put performance directives in round parentheses.
     - `(fade out)` puts a structural ending tag in round parentheses instead of `[Fade Out]` or `[Outro - fade out]`.
3. **Execution Hazard**: If an agent following this contract generates lyrics containing `(ambient build)` or `(fade out)`, audio models (Suno AI v4.5/v5.5 and Google Flow Music Lyria 3.5) will vocalize those words aloud instead of executing them as sound cues.
4. **Dispatch Mandate**: Challenger 2's dispatch instructions explicitly mandate:
   *"4. Verify that brackets vs parentheses rule is 100% adhered to across all markdown templates."*
   *"5. Emit your verdict: APPROVE or REQUEST_CHANGES in d:\poetry-skill\.agents\challenger_2\handoff.md."*
5. **Deduction**: Because `music-lyrics-architect.md` fails `MetatagValidator` and violates the global directives, 100% adherence is not met. Therefore, the honest, empirical verdict is **REQUEST_CHANGES**.

---

## 3. Caveats

- The master test runner `tests/run_tests.py --all` passed 78/78 tests because test suites were testing lyrics in `examples/` and `skills/ukrainian-poetry-to-suno/references/`, but lacked a unit test verifying the subagent output contract inside `skills/ukrainian-poetry-to-suno/agents/music-lyrics-architect.md`.
- All other components (`poetry-qa-bot.md`, `skills/poetry-skill/SKILL.md` End-to-End pipeline, and all 6 files in `examples/`) are 100% compliant and robust.
- The defect is confined to `music-lyrics-architect.md` and requires only a single contiguous block replacement in `skills/ukrainian-poetry-to-suno/agents/music-lyrics-architect.md` and synchronization via `tests/sync_ecosystem.py`.

---

## 4. Conclusion

- **Verdict**: **REQUEST_CHANGES**
- **Actionable Remediation Blueprint**:
  1. In `skills/ukrainian-poetry-to-suno/agents/music-lyrics-architect.md`, replace lines 51–70 with:
     ```markdown
     # Output Contract
     ```markdown
     ## 🎼 AI-Optimized Lyrics

     [Intro - ambient build]

     [Verse 1]
     (whispered)
     Line one text hEre
     Line two text hEre

     [Chorus - soaring legato]
     Line one of chOrus
     Line two of chOrus

     [Outro - fade out]
     ```
     ```
  2. Run `py -3 tests/sync_ecosystem.py` to synchronize `.agents/skills/` and `C:\Users\sm9sh\.gemini\config\plugins\poetry-skill\`.
  3. (Optional but recommended) In `tests/test_adversarial_challenger2.py`, expand `test_20` or add a test to validate that all subagent markdown files in `skills/ukrainian-poetry-to-suno/agents/` pass `MetatagValidator`.

---

## 5. Verification Method

To independently reproduce the finding and verify:

1. **Reproduce the Violation with `MetatagValidator`**:
   ```powershell
   py -3 -c "import sys; sys.path.insert(0, 'd:/poetry-skill'); from tests.validator import MetatagValidator; print(MetatagValidator.validate_lyrics_structure('''[Intro]\n(ambient build)\n\n[Verse 1]\n(staccato delivery)\nLine one text hEre\nLine two text hEre\n\n[Chorus]\n(legato, soaring)\nLine one of chOrus\nLine two of chOrus\n\n[Outro]\n(fade out)''').errors)"
   ```
   Output: 3 errors reported.

2. **Verify Corrected Version Passes**:
   ```powershell
   py -3 -c "import sys; sys.path.insert(0, 'd:/poetry-skill'); from tests.validator import MetatagValidator; res = MetatagValidator.validate_lyrics_structure('''[Intro - ambient build]\n\n[Verse 1]\n(whispered)\nLine one text hEre\nLine two text hEre\n\n[Chorus - soaring legato]\nLine one of chOrus\nLine two of chOrus\n\n[Outro - fade out]'''); print('is_valid:', res.is_valid, 'errors:', res.errors)"
   ```
   Expected output: `is_valid: True errors: []`

3. **Verify All Challenger 2 & Playground Unit Tests**:
   ```powershell
   py -3 -m unittest tests/test_adversarial_challenger2.py
   py -3 -m unittest tests/test_examples_playground.py
   py -3 tests/run_tests.py --all
   ```

4. **Invalidation Conditions**:
   This finding is invalidated if and only if the Output Contract block in `music-lyrics-architect.md` is updated to compliant bracket/parentheses notation, `MetatagValidator` returns 0 errors on the file, and `tests/sync_ecosystem.py` confirms clean synchronization.


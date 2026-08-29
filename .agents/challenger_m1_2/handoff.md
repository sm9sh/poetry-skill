# Handoff Report — Challenger 2 (Milestone 1)

## 1. Observation

### 1.1 Metatags and Bracket Consistency in Skills References
Direct inspection of files in `skills/ukrainian-poetry-to-suno/references/` (`song-structure-pack.md`, `lyrics-to-suno-template.md`, `full-guide.md`, `prompt-builder.md`, `suno-prompt-anti-patterns.md`) and `skills/ukrainian-poetry-to-suno/SKILL.md` showed:
1. **Square Brackets `[...]` for Structure & Arrangement**:
   All 8 genre templates in `song-structure-pack.md` (lines 78–431) and the master template in `lyrics-to-suno-template.md` (lines 16–77) consistently use `[...]` for structural markers and arrangement cues:
   - `[Vocal Intro - dynamic acapella, dry and close]`
   - `[Beat Drop - heavy fuzz bass, punchy driving drums]`
   - `[Verse 1 - rhythmic staccato, deadpan baritone]`
   - `[Pre-Chorus - rising snare roll, building tension]`
   - `[Chorus - explosive, wide chorus guitars, wall of sound]`
   - `[Verse 2 - add driving tambourine, syncopated backing, sharp stereo guitars]`
   - `[Breakdown - vocal and bassline only, intimate, dry]`
   - `[Mega-Chorus - maximum energy, soaring layered harmonies, clashing guitars]`
   - `[Outro - fading out, solo analog synth, tape hiss]`
   - `[End]`, `[Cold End]`
2. **Round Parentheses `(...)` for Vocal Gestures & Ad-libs**:
   All inline gestures and backing vocals consistently use `(...)`:
   - `(whispered)`, `(whispered, intimate)`
   - `(belted)`, `(belted, powerful)`
   - `(falsetto)`
   - `(screamed)`, `(growl)`
   - `(ad-lib)`, `(vocal runs)`
   - `(building intensity)`
   - `(key change)`
   - `(half-time feel)`
   - `(harmonized)`, `(layered harmonies)`
   - Spoken backing text: `(луна)`, `(ніколи знов)`, `(разом у темряві)`.
   Zero instances of instrumental cues were found inside `(...)` in valid template blocks. (The only instance of `(Staccato cutting telecaster...)` occurs in `suno-prompt-anti-patterns.md:46` as an explicit negative anti-pattern demonstration).
3. **Capitalized Vowel Stress Standard**:
   All templates consistently mark non-obvious and mobile accents with capitalized vowels: `вИпадок`, `чорнОзем`, `прИйде`, `заспівАй`, `моЯ`, `землЯ`, `зЕмлю`, `дорОга`, `ліхтарІ`, `унісОн`, `руЇн`, `дібрОвах`.

### 1.2 Platform Limits and Token Constraints
Direct inspection of `skills/ukrainian-poetry-to-suno/SKILL.md`, `references/full-guide.md`, `references/prompt-builder.md`, and `ai-music-generation-meta-spec-v8.md` verified:
- **Suno AI (v4.5 / v5.5)**:
  - Technical limits: Style box 1000 chars hard limit; Lyrics 5000 chars hard limit.
  - Optimal/recommended style range: 80–180 characters (8–15 tags).
  - Method 1 (Conversational Paragraph): Follows "First 5 Words" rule ($80\%$ attention on opening descriptors).
  - Method 2 (Tag-Based Matrix): HookGenius 5-module formula (`[1. Genre/Subgenre], [2. Mood/Energy], [3. Vocal Triple-Stack], [4. Lead Instruments], [5. Production Aesthetic, BPM]`).
  - System features: *My Taste*, *Voices* cloning, *Custom Models* (up to 3).
  - Failure mode fixes: Lyrics Rushing $\to$ 4–8 words/line + `(half-time feel)`; Sterile Vocals $\to$ Vocal Triple-Stack; Negation Trap $\to$ positive hyper-specificity (`purely acoustic, solo piano, isolated vocals`).
  - Commercial licensing: Pro ($10/mo), Premier ($30/mo); Free is strictly non-commercial.
- **Udio AI (v4)**:
  - Audio quality: 48 kHz stereo.
  - Track length: up to 10 min continuous track generation.
  - Context length: up to 15 min (10–15s for abrupt transitions vs maximum for continuity).
  - Prompt length: up to 250 characters.
  - Inpainting syntax: `*stars*` (e.g. `*static sky*`).
  - Commercial licensing: Pro ($30/mo) strictly required for commercial rights; Standard ($10/mo) has no commercial rights.
- **Google Flow Music (Lyria 3.5)**:
  - Engine: DeepMind Lyria 3.5.
  - Credits & Rights: 500 free daily credits with full commercial licenses (MusicFX closed July 31, 2026).
  - Features: Conversational Agent mode, Spaces (browser apps), Turntable (DJ mixing), Section-level Replace (editing timecode sections without re-rolling), AI Cover, Gemini Omni Flash synchronized video generation.

### 1.3 Discrepancies and Failures Observed

#### Discrepancy A: Validator Prefix Gap in `tests/validator/metatag_validator.py`
Executing programmatic validation on the canonical templates from `skills/ukrainian-poetry-to-suno/references/song-structure-pack.md` and `lyrics-to-suno-template.md` via `MetatagValidator.validate_lyrics_structure()` failed with multiple errors:
```text
[ERROR] Invalid metatag '[Vocal Intro - dynamic acapella, dry and close]': Unrecognized metatag syntax: '[Vocal Intro - dynamic acapella, dry and close]'.
[ERROR] Invalid metatag '[Beat Drop - heavy fuzz bass, punchy driving drums]': Unrecognized metatag syntax: '[Beat Drop - heavy fuzz bass, punchy driving drums]'.
[ERROR] Invalid metatag '[Mega-Chorus - maximum energy, layered harmonies, guitars clashing]': Unrecognized metatag syntax: '[Mega-Chorus - maximum energy, layered harmonies, guitars clashing]'.
```
Inspecting `tests/validator/metatag_validator.py` lines 27–44 revealed that `STRUCTURAL_PREFIXES` only contains:
```python
    STRUCTURAL_PREFIXES = [
        "intro", "verse", "pre-chorus", "pre chorus", "chorus", "post-chorus",
        "post chorus", "bridge", "drop", "build-up", "buildup", "build",
        "instrumental", "instrumental break", "instrumental solo", "guitar solo",
        "bandura solo", "sopilka solo", "synth solo", "bass solo", "drum solo",
        "solo", "interlude", "breakdown", "break", "hook", "refrain",
        "spoken word", "spoken", "whisper", "whispering", "chant",
        "polyphonic chant", "outro", "fade out", "fadeout", "fade", "end",
        "ending", "climax", "silence", "pause",
        # Ukrainian equivalents
        "інтро", "куплет", "передприспів", "приспів", "післяприспів",
        "міст", "бридж", "дроп", "програш", "інструментал", "соло",
        "соло гітари", "соло бандури", "соло сопілки", "речитатив",
        "декламація", "шепіт", "аутро", "кінцівка", "фінал", "затихання"
    ]
```
The prefixes `"vocal intro"`, `"beat drop"`, `"mega-chorus"`, `"mega chorus"`, `"cold end"`, and Ukrainian equivalents `"вокальний вступ"`, `"біт дроп"`, `"мега-приспів"`, `"мега приспів"`, `"холодний фінал"`, `"брейкдаун"` are MISSING from `STRUCTURAL_PREFIXES`.
Because `"vocal intro"` does not start with `"intro"`, `"beat drop"` does not start with `"drop"`, and `"mega-chorus"` does not start with `"chorus"`, any compound directive such as `[Vocal Intro - dynamic acapella]` or `[Beat Drop - heavy fuzz bass]` fails `MetatagValidator.is_valid_tag()`.

#### Discrepancy B: Desynchronization of Root Mirror Files
Comparing the root markdown files against `skills/ukrainian-poetry-to-suno/references/` showed:
- `song-structure-pack.md` (root, 7513 bytes) vs `skills/.../song-structure-pack.md` (14112 bytes): Root file references legacy Suno v3.5/v4, lacks Udio v4 and Lyria 3.5, and states `*stars*` should be avoided rather than detailing Udio Inpainting.
- `lyrics-to-suno-template.md` (root, 7001 bytes) vs `skills/.../lyrics-to-suno-template.md` (7709 bytes): Root file lacks the 3-platform master template (Suno Method 1 & 2, Udio, Flow Music) and Vance Powell Verse 2 / Breakdown roadmaps.
- `suno-prompt-anti-patterns.md` (root, 10704 bytes) vs `skills/.../suno-prompt-anti-patterns.md` (8525 bytes): Root file is not synchronized with the v8 anti-pattern taxonomy.
- `prompt-builder.md`, `reference-to-style-cheatsheet.md`, `mood-to-style-map.md`, `ukrainian-poetry-to-suno.md`: Root mirror files contain discrepancies with the v8 specification.

---

## 2. Logic Chain

1. **Premise 1 (Contract Requirement R3)**: `ORIGINAL_REQUEST.md` R3 states:
   > "Оновити валідатори `tests/validator/metatag_validator.py`, `tests/validator/suno_validator.py` та `tests/validator/poetic_validator.py` за потреби для підтримки нових тегів (`[Vocal Intro]`, `[Beat Drop]`, `[Post-Chorus]`, `[Mega-Chorus]`, `[Breakdown]`, інлайн-жестів та лімітів)."
2. **Premise 2 (Contract Requirement R1)**: `ORIGINAL_REQUEST.md` R1 states:
   > "Оновити кореневі симетричні файли: `ukrainian-poetry-to-suno.md`, `ukrainian-poetry-skill.md`, `lyrics-to-suno-template.md`, `song-structure-pack.md`, `suno-prompt-anti-patterns.md`."
3. **Observation Reference**:
   - In `tests/validator/metatag_validator.py`, `STRUCTURAL_PREFIXES` lacks `"vocal intro"`, `"beat drop"`, `"mega-chorus"`, `"mega chorus"`, `"cold end"`, `"вокальний вступ"`, `"біт дроп"`, `"мега-приспів"`, `"мега приспів"`, `"холодний фінал"`, `"брейкдаун"`.
   - Running `MetatagValidator.validate_lyrics_structure()` on canonical templates fails.
   - Root mirror files (`song-structure-pack.md`, `lyrics-to-suno-template.md`, etc.) are outdated legacy versions.
4. **Inference**:
   - The documentation in `skills/ukrainian-poetry-to-suno/` correctly implements the v8 metatags, bracket rules, and platform constraints.
   - However, because `metatag_validator.py` was not updated, automated tests and validator consumers will falsely reject valid v8 prompt packages.
   - Furthermore, because root files were not synchronized, developers and agents accessing root markdown files will receive stale legacy instructions.
5. **Deductive Conclusion**: Changes are strictly required to update `metatag_validator.py` and synchronize root mirror files.

---

## 3. Caveats

1. **Live Audio Generation**: This review verified prompt strings, token counts, regex patterns, bracket grammar, and validator code. Live generation against commercial Suno v5.5, Udio v4, or Google Flow Music APIs was not performed within this offline sandbox.
2. **Existing Test Suite Masking**: The test suite `py -3 tests/run_tests.py --all` currently passes (63/63) because existing tests only exercised older legacy prefixes (`[Intro]`, `[Verse]`, `[Chorus]`, `[Instrumental Break]`) and did not execute `MetatagValidator` on the new v8 compound tags (`[Vocal Intro - ...]`, `[Beat Drop - ...]`, `[Mega-Chorus - ...]`).

---

## 4. Conclusion & Verdict

**Verdict**: **REQUEST_CHANGES**

### Actionable Remediation Checklist for Worker:
1. **Update `tests/validator/metatag_validator.py`**:
   Add the following prefixes to `STRUCTURAL_PREFIXES`:
   ```python
   "vocal intro", "beat drop", "mega-chorus", "mega chorus", "cold end",
   # Ukrainian equivalents
   "вокальний вступ", "біт дроп", "мега-приспів", "мега приспів", "холодний фінал", "брейкдаун"
   ```
2. **Synchronize Root Mirror Markdown Files**:
   Copy/sync updated v8 content from `skills/ukrainian-poetry-to-suno/references/` to corresponding root files:
   - `song-structure-pack.md` $\leftarrow$ `skills/ukrainian-poetry-to-suno/references/song-structure-pack.md`
   - `lyrics-to-suno-template.md` $\leftarrow$ `skills/ukrainian-poetry-to-suno/references/lyrics-to-suno-template.md`
   - `suno-prompt-anti-patterns.md` $\leftarrow$ `skills/ukrainian-poetry-to-suno/references/suno-prompt-anti-patterns.md`
   - `prompt-builder.md` $\leftarrow$ `skills/ukrainian-poetry-to-suno/references/prompt-builder.md`
   - `reference-to-style-cheatsheet.md` $\leftarrow$ `skills/ukrainian-poetry-to-suno/references/reference-to-style-cheatsheet.md`
   - `mood-to-style-map.md` $\leftarrow$ `skills/ukrainian-poetry-to-suno/references/mood-to-style-map.md`
   - `ukrainian-poetry-to-suno.md` $\leftarrow$ `skills/ukrainian-poetry-to-suno/SKILL.md` (or core guide)

---

## 5. Verification Method

To independently verify after changes are made:
1. Run deterministic test suite:
   ```bash
   py -3 tests/run_tests.py --all
   ```
2. Run empirical metatag and template audit harness:
   ```bash
   py -3 tests/audit_challenger2_empirical.py
   ```
   *Expected result*: Exit code 0, zero errors, 100% of templates in `song-structure-pack.md` and `lyrics-to-suno-template.md` pass `MetatagValidator.validate_lyrics_structure()`.
3. Invalidation condition: If `MetatagValidator.is_valid_tag("Vocal Intro - dynamic acapella, dry and close")` returns `False`, the fix is invalid.

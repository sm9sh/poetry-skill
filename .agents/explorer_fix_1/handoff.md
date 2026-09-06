# Handoff Report — Explorer Fix 1 (Bracket & Metatag Remediation Analysis)

**Agent**: `explorer_fix_1` (Teamwork Explorer / Analyst)  
**Date**: 2026-09-06  
**Working Directory**: `d:\poetry-skill\.agents\explorer_fix_1`  
**Handoff Type**: Hard (Investigation & Remediation Analysis Complete)  
**Verdict**: **REMEDIATION_READY**

---

## 1. Observation

### 1.1 Empirical Verification of Challenger 2 Finding in `music-lyrics-architect.md`
We examined `skills/ukrainian-poetry-to-suno/agents/music-lyrics-architect.md` (lines 49–70):

```markdown
49: 5. **Metatags & Gestures**: Use `[Verse]`, `[Chorus]`, `[Bridge]` for structure. Use `(sigh)`, `(whisper)`, `(breath)`, `(growl)`, `(cry)` for inline vocal gestures. Use 9 canonical inline gestures max per section.
50: 
51: # Output Contract
52: ```markdown
53: ## 🎼 AI-Optimized Lyrics
54: 
55: [Intro]
56: (ambient build)
57: 
58: [Verse 1]
59: (staccato delivery)
60: Line one text hEre
61: Line two text hEre
62: 
63: [Chorus]
64: (legato, soaring)
65: Line one of chOrus
66: Line two of chOrus
67: 
68: [Outro]
69: (fade out)
70: ```
```

When evaluated using `MetatagValidator.validate_lyrics_structure()`:
- Command:
  ```powershell
  py -3 -c "import sys; sys.path.insert(0, 'd:/poetry-skill'); from tests.validator import MetatagValidator; block = '''[Intro]\n(ambient build)\n\n[Verse 1]\n(staccato delivery)\nLine one text hEre\nLine two text hEre\n\n[Chorus]\n(legato, soaring)\nLine one of chOrus\nLine two of chOrus\n\n[Outro]\n(fade out)'''; res = MetatagValidator.validate_lyrics_structure(block); print('is_valid:', res.is_valid); print('errors:', res.errors)"
  ```
- Result:
  ```json
  is_valid: False
  errors: [
    "Instrumental descriptor 'staccato delivery' found in parentheses '()'. In Suno AI and Google Flow Music, text in parentheses is read out loud as vocals/ad-libs. Use square brackets '[...]' for musical instructions (e.g. '[Intro - staccato delivery]' or '[staccato delivery]').",
    "Instrumental descriptor 'legato, soaring' found in parentheses '()'. In Suno AI and Google Flow Music, text in parentheses is read out loud as vocals/ad-libs. Use square brackets '[...]' for musical instructions (e.g. '[Intro - legato, soaring]' or '[legato, soaring]').",
    "Instrumental descriptor 'fade out' found in parentheses '()'. In Suno AI and Google Flow Music, text in parentheses is read out loud as vocals/ad-libs. Use square brackets '[...]' for musical instructions (e.g. '[Intro - fade out]' or '[fade out]')."
  ]
  ```
- Additional observation: `(ambient build)` on line 56 places an arrangement directive in round parentheses `(...)`, violating the core rule in `AGENTS.md` ("Never put instrumental descriptions in parentheses because Google Flow Music and Suno will vocalize/sing them out loud!").

### 1.2 Comprehensive Scan of All 4 Subagents in `skills/ukrainian-poetry-to-suno/agents/`
We scanned all 4 specification files located in `skills/ukrainian-poetry-to-suno/agents/`:
1. `music-lyrics-architect.md`:
   - Code Block #1 (lines 28–38): YAML Input Contract (`raw_poetry`, `structure_template`). No lyrics/metatag errors.
   - Code Block #2 (lines 52–70): Markdown Output Contract. **FAILED** with 3 errors from `MetatagValidator`.
2. `music-reference-engineer.md`:
   - Code Block #1 (lines 25–37): YAML Input Contract (`reference_tracks`, `target_vibe`).
   - Code Block #2 (lines 51–73): Markdown Output Contract (Acoustic DNA Report). Uses markdown brackets for document fields (`[Genre]`, `[BPM]`, `[List of instruments/textures]`, `[Description]`, `[Hook Strategy]`). No lyrics blocks or song structure metatags.
   - Result: 0 lyrics blocks, 0 metatag errors.
3. `music-prompt-synthesizer.md`:
   - Code Block #1 (lines 27–37): YAML Input Contract (`reference_dna`, `optimized_lyrics`).
   - Code Block #2 (lines 56–69): Markdown Output Contract (Multi-Platform Prompt Package). Uses markdown brackets for prompt template placeholders (`[Acoustic descriptors, tempo, genre]`, `[Insert optimized lyrics with metatags]`, `[Dense comma-separated tags, high fidelity descriptors]`, `[Natural language request]`).
   - Result: 0 lyrics blocks, 0 metatag errors.
4. `music-daw-mastering-critic.md`:
   - Code Block #1 (lines 27–37): YAML Input Contract (`track_metadata`, `mixing_plan`).
   - Code Block #2 (lines 54–69): Markdown Output Contract (DAW Engineering Audit Report). Uses checklist brackets (`[Pass/Fail]`) and placeholder brackets (`[Suggestions for Trackspacer/Neutron]`, `[Target metrics]`).
   - Result: 0 lyrics blocks, 0 metatag errors.

### 1.3 Full Ecosystem Markdown Scan
We executed an automated scanner over all 45 markdown files across `skills/` and `examples/`:
- Out of all extracted lyrics/song-structure blocks across the entire repository:
  - Exactly **1 block failed**: `skills/ukrainian-poetry-to-suno/agents/music-lyrics-architect.md` (Block #2, lines 52–70).
  - All other 44 files passed with **0 errors**.

---

## 2. Logic Chain

1. **Directive Contract (`AGENTS.md`)**:
   - `[Square Brackets]`: Mandatory for ALL structural markers and arrangement instructions (`[Intro]`, `[Verse 1 - rhythmic staccato]`, `[Chorus - soaring legato]`, `[Outro - fade out]`).
   - `(Round Parentheses)`: Restricted EXCLUSIVELY to sung backing vocals, ad-libs, and 9 canonical inline vocal delivery gestures (`(whispered)`, `(belted)`, `(falsetto)`, `(screamed)`, `(ad-lib)`, `(building intensity)`, `(key change)`, `(half-time feel)`, `(harmonized)`, `(луна)`).
2. **Audio AI Model Behavior**:
   - Suno AI v4.5/v5.5 and Google Flow Music Lyria 3.5 treat round parentheses `(...)` as lyrics to be vocalized by the voice model. If a prompt includes `(staccato delivery)`, `(legato, soaring)`, or `(fade out)`, the singer sings those words aloud.
3. **Internal Inconsistency in `music-lyrics-architect.md`**:
   - Rule 5 on line 49 listed `(sigh)`, `(whisper)`, `(breath)`, `(growl)`, `(cry)` instead of referring to the 9 canonical vocal delivery gestures defined in `AGENTS.md` and `lyrics-to-suno-template.md`.
   - The Output Contract example directly placed instrumental directives (`ambient build`, `staccato delivery`, `legato, soaring`, `fade out`) inside parentheses instead of square brackets or compound bracket metatags.
4. **Scope of Impact**:
   - The issue is completely isolated to `music-lyrics-architect.md` (and its mirrored paths). The remaining 3 music subagents are pure data-transform/audit agents with markdown report schemas, not lyrics generators.
5. **Remediation Feasibility**:
   - The fix requires a single localized update in `skills/ukrainian-poetry-to-suno/agents/music-lyrics-architect.md`, followed by synchronization via `tests/sync_ecosystem.py` and adding a regression test in `tests/test_adversarial_challenger2.py`.

---

## 3. Caveats

- **Placeholder Brackets in Markdown Reports**: `music-reference-engineer.md`, `music-prompt-synthesizer.md`, and `music-daw-mastering-critic.md` contain placeholder tokens such as `[Genre]` and `[Pass/Fail]` inside markdown report templates. These are not lyrics blocks and are not processed by music generators, so they do not violate audio metatag syntax.
- **Ecosystem Mirroring**: Because `skills/` is mirrored to `.agents/skills/` and `C:\Users\sm9sh\.gemini\config\plugins\poetry-skill\`, any fix applied to `skills/` must be synchronized using `py -3 tests/sync_ecosystem.py`.

---

## 4. Conclusion

- **Verdict**: **REMEDIATION_READY**
- **Actionable Remediation Blueprint**:

### 4.1 Changes to `skills/ukrainian-poetry-to-suno/agents/music-lyrics-architect.md`

#### Before:
```markdown
5. **Metatags & Gestures**: Use `[Verse]`, `[Chorus]`, `[Bridge]` for structure. Use `(sigh)`, `(whisper)`, `(breath)`, `(growl)`, `(cry)` for inline vocal gestures. Use 9 canonical inline gestures max per section.

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
```

#### After:
```markdown
5. **Metatags & Gestures**: Use square brackets `[...]` for ALL structural, instrumentation, and arrangement instructions (e.g., `[Intro - ambient build]`, `[Verse 1 - rhythmic staccato]`, `[Chorus - soaring legato]`, `[Outro - fade out]`). Use round parentheses `(...)` EXCLUSIVELY for backing vocals, ad-libs, and vocal delivery gestures (e.g., `(whispered)`, `(belted)`, `(falsetto)`, `(screamed)`, `(ad-lib)`, `(building intensity)`, `(key change)`, `(half-time feel)`, `(harmonized)`, `(луна)`). Never put instrumental or arrangement descriptions in parentheses because Suno AI and Google Flow Music will sing them out loud.

# Output Contract
```markdown
## 🎼 AI-Optimized Lyrics

[Intro - ambient build]

[Verse 1 - rhythmic staccato]
(whispered)
Line one text hEre
Line two text hEre

[Chorus - soaring legato]
(belted)
Line one of chOrus
Line two of chOrus

[Outro - fade out]
```
```

### 4.2 Artifacts Prepared in `d:\poetry-skill\.agents\explorer_fix_1/`
1. `d:\poetry-skill\.agents\explorer_fix_1\remediation.patch` — Unified diff ready for application.
2. `d:\poetry-skill\.agents\explorer_fix_1\proposed_music-lyrics-architect.md` — Complete compliant replacement file.

### 4.3 Ecosystem Synchronization
Run:
```powershell
py -3 tests/sync_ecosystem.py
```
This propagates the fix to:
- `d:\poetry-skill\.agents\skills\ukrainian-poetry-to-suno\agents\music-lyrics-architect.md`
- `C:\Users\sm9sh\.gemini\config\plugins\poetry-skill\skills\ukrainian-poetry-to-suno\agents\music-lyrics-architect.md`

### 4.4 Regression Test Addition in `tests/test_adversarial_challenger2.py`
Add `test_22_music_subagents_and_metatags` to `TestChallenger2Robustness` in `tests/test_adversarial_challenger2.py`:

```python
    def test_22_music_subagents_and_metatags(self):
        """Verify all 4 music subagent markdown files exist, parse valid YAML, and contain valid lyrics metatags."""
        music_agents_dir = PROJECT_ROOT / "skills" / "ukrainian-poetry-to-suno" / "agents"
        self.assertTrue(music_agents_dir.exists(), "music agents directory must exist")

        expected_music_agents = [
            "music-lyrics-architect.md",
            "music-reference-engineer.md",
            "music-prompt-synthesizer.md",
            "music-daw-mastering-critic.md",
        ]

        mandatory_sections = [
            "# Role & Identity",
            "# Scope & Boundaries",
            "# Input Contract",
            "# Operational Rules & Heuristics",
            "# Output Contract",
            "# Edge-Case Handling",
        ]

        for agent_file in expected_music_agents:
            agent_path = music_agents_dir / agent_file
            self.assertTrue(agent_path.exists(), f"Music agent file missing: {agent_file}")

            content = agent_path.read_text(encoding="utf-8")
            self.assertTrue(content.startswith("---"), f"{agent_file} must start with '---'")
            parts = content.split("---", 2)
            self.assertTrue(len(parts) >= 3, f"{agent_file} must have closing '---'")

            body = parts[2]
            for sec in mandatory_sections:
                self.assertIn(sec, body, f"{agent_file} missing section '{sec}'")

            # Validate all code blocks containing lyrics/song-structure metatags
            blocks = re.findall(r"```(?:markdown|text|lyrics)?\s*\n(.*?)```", body, re.DOTALL)
            for block in blocks:
                if any(t in block for t in ["[Verse", "[Chorus", "[Intro", "[Outro", "[Drop", "[Breakdown"]):
                    res = MetatagValidator.validate_lyrics_structure(block)
                    self.assertTrue(
                        res.is_valid,
                        f"Lyrics block in {agent_file} failed MetatagValidator: {res.errors}"
                    )
```

---

## 5. Verification Method

To independently verify the proposed remediation:

1. **Verify Corrected Output Contract Passes `MetatagValidator`**:
   ```powershell
   py -3 -c "import sys; sys.path.insert(0, 'd:/poetry-skill'); from tests.validator import MetatagValidator; text = '''[Intro - ambient build]\n\n[Verse 1 - rhythmic staccato]\n(whispered)\nLine one text hEre\nLine two text hEre\n\n[Chorus - soaring legato]\n(belted)\nLine one of chOrus\nLine two of chOrus\n\n[Outro - fade out]'''; res = MetatagValidator.validate_lyrics_structure(text); print('is_valid:', res.is_valid, 'errors:', res.errors)"
   ```
   **Expected output**: `is_valid: True errors: []`

2. **Verify Proposed Replacement File**:
   ```powershell
   py -3 -c "import sys, re, pathlib; sys.path.insert(0, 'd:/poetry-skill'); from tests.validator import MetatagValidator; p = pathlib.Path(r'd:\poetry-skill\.agents\explorer_fix_1\proposed_music-lyrics-architect.md'); content = p.read_text(encoding='utf-8'); blocks = re.findall(r'```(?:markdown|text|lyrics)?\s*\n(.*?)```', content, re.DOTALL); lyrics_blocks = [b for b in blocks if any(t in b for t in ['[Intro', '[Verse', '[Chorus', '[Outro'])]; print('Found lyrics blocks:', len(lyrics_blocks)); res = MetatagValidator.validate_lyrics_structure(lyrics_blocks[0]); print('is_valid:', res.is_valid, 'errors:', res.errors)"
   ```
   **Expected output**: `Found lyrics blocks: 1`, `is_valid: True errors: []`

3. **Verify Full System Tests and Synchronization After Fix Application**:
   ```powershell
   py -3 tests/sync_ecosystem.py
   py -3 -m unittest tests/test_adversarial_challenger2.py
   py -3 -m unittest tests/test_examples_playground.py
   py -3 tests/run_tests.py --all
   ```
   **Expected output**: All test suites exit with code `0`.

4. **Invalidation Conditions**:
   This remediation is invalidated if and only if the proposed replacement block introduces non-whitelisted parenthetical strings or invalid compound bracket tags.

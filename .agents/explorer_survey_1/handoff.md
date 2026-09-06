# Handoff Report: Explorer 1 — R1 (Root Cleanup & Sync Refactoring)

## Executive Summary
This report delivers an exhaustive architectural survey of repository root cleanup and synchronization refactoring (R1). All 16 root mirror files and the root `packs/` directory were empirically proven to be 100% byte-for-byte redundant duplicates of canonical references under `skills/`. The two standalone Ukrainian poetry guides (`ukrainian-poetry-skill-uk.md` and `ukrainian-poetry-skill-lite.md`) currently reside exclusively at root and should be relocated to `skills/ukrainian-poetry/references/`. In `tests/sync_ecosystem.py`, the `ROOT_MIRRORS` dictionary and `sync_root_mirrors()` function must be purged. Concrete remediation patches are provided for `tests/sync_ecosystem.py`, `INSTALL.md`, and `tests/audit_challenger2_empirical.py`. Deletion of all 16 root files and `packs/` causes zero regression across all 75 E2E and adversarial test suites.

---

## 1. Observation

### 1.1 Complete Inventory of the 16 Redundant Root Mirror Files
Every file at root corresponds 1:1 to a canonical source in `skills/`. Full comparison was conducted via content hashing and character length verification:

| # | Root Mirror File | Canonical Source Path | Disk Size | Char Count | Match Status |
|---|---|---|---|---|---|
| 1 | `ukrainian-poetry-to-suno.md` | `skills/ukrainian-poetry-to-suno/references/full-guide.md` | 31,551 B | 20,506 chars | EXACT MATCH |
| 2 | `ukrainian-poetry-skill.md` | `skills/ukrainian-poetry/references/full-guide.md` | 65,259 B | 38,724 chars | EXACT MATCH |
| 3 | `lyrics-to-suno-template.md` | `skills/ukrainian-poetry-to-suno/references/lyrics-to-suno-template.md` | 11,525 B | 7,709 chars | EXACT MATCH |
| 4 | `song-structure-pack.md` | `skills/ukrainian-poetry-to-suno/references/song-structure-pack.md` | 20,478 B | 14,112 chars | EXACT MATCH |
| 5 | `suno-prompt-anti-patterns.md` | `skills/ukrainian-poetry-to-suno/references/suno-prompt-anti-patterns.md` | 13,065 B | 8,525 chars | EXACT MATCH |
| 6 | `prompt-builder.md` | `skills/ukrainian-poetry-to-suno/references/prompt-builder.md` | 11,344 B | 8,917 chars | EXACT MATCH |
| 7 | `reference-to-style-cheatsheet.md` | `skills/ukrainian-poetry-to-suno/references/reference-to-style-cheatsheet.md` | 13,331 B | 11,331 chars | EXACT MATCH |
| 8 | `mood-to-style-map.md` | `skills/ukrainian-poetry-to-suno/references/mood-to-style-map.md` | 13,203 B | 11,901 chars | EXACT MATCH |
| 9 | `suno-style-rubric.md` | `skills/ukrainian-poetry-to-suno/references/rubric.md` | 9,168 B | 6,042 chars | EXACT MATCH |
| 10 | `reference-breakdown-examples.md` | `skills/ukrainian-poetry-to-suno/references/reference-breakdown-examples.md` | 11,055 B | 7,658 chars | EXACT MATCH |
| 11 | `ukrainian-song-scenarios.md` | `skills/ukrainian-poetry-to-suno/references/ukrainian-song-scenarios.md` | 16,916 B | 13,200 chars | EXACT MATCH |
| 12 | `suno-prompt-tests.md` | `skills/ukrainian-poetry-to-suno/references/tests.md` | 8,543 B | 5,707 chars | EXACT MATCH |
| 13 | `ukrainian-poetry-skill-rubric.md` | `skills/ukrainian-poetry/references/rubric.md` | 18,133 B | 10,711 chars | EXACT MATCH |
| 14 | `ukrainian-poetry-skill-input-template.md` | `skills/ukrainian-poetry/references/input-templates.md` | 8,211 B | 5,349 chars | EXACT MATCH |
| 15 | `ukrainian-poetry-skill-stress-pack.md` | `skills/ukrainian-poetry/references/stress-tests.md` | 15,794 B | 8,957 chars | EXACT MATCH |
| 16 | `ukrainian-poetry-skill-tests.md` | `skills/ukrainian-poetry/references/tests.md` | 12,330 B | 7,085 chars | EXACT MATCH |

Total disk footprint of these 16 redundant files: **281,906 bytes (~282 KB)**.

### 1.2 Inventory & Comparison of Root `packs/` Directory
The root directory `packs/` contains 8 markdown files:
- `README.md` (2,658 B, 1,763 chars)
- `dark-pack.md` (3,425 B, 3,163 chars)
- `female-vocal-pack.md` (3,731 B, 3,354 chars)
- `male-vocal-pack.md` (3,770 B, 3,387 chars)
- `sad-pack.md` (3,476 B, 3,181 chars)
- `suno-reference-prompt-pack-uk.md` (11,862 B, 9,057 chars)
- `suno-reference-prompt-pack.md` (7,110 B, 6,818 chars)
- `uplifting-pack.md` (3,417 B, 3,124 chars)

**Verification**: Comparing `d:\poetry-skill\packs\*` against `d:\poetry-skill\skills\ukrainian-poetry-to-suno\references\packs\*` confirmed that every single file is an **exact 100% byte-for-byte duplicate**. The canonical directory `skills/ukrainian-poetry-to-suno/references/packs/` is already synchronized to `.agents/skills/` and the global plugin `C:\Users\sm9sh\.gemini\config\plugins\poetry-skill\skills\ukrainian-poetry-to-suno\references\packs\`. The root `packs/` directory is completely redundant.

### 1.3 Audit of Root Standalone Ukrainian Guides
Two Ukrainian guides currently exist **only** in the root directory:
1. `ukrainian-poetry-skill-uk.md` (223 lines, 23,034 bytes):
   - Comprehensive Ukrainian-language specification of Ukrainian Poetry v2.
   - Contains: 6 core registers, priority hierarchy, input parameter contracts (`topic`, `form`, `meter`, `rhyme`, `clausula`), meter catalog (iamb, trochee, dactyl, amphibrach, anapest, dolnik, kolomyika, blank verse, verlibre), stress scansion, homographs, euphony (`у/в`, `і/й`), and anti-sharovarshchyna guardrails.
2. `ukrainian-poetry-skill-lite.md` (74 lines, 5,442 bytes):
   - Fast, compact Ukrainian poetry cheat sheet.
   - Contains: Top rule hierarchy, meter overview, mobile stress and homographs list (`зАмок` vs `замОк`, `дорогА` vs `дорОга`), banned Russianisms (`вИпадок`, `чорнОзем`, `одИннадцять`), and heterogeneous rhyming rules.

Neither file is currently copied to `skills/`, `.agents/skills/`, or `docs/`. If deleted without relocation, their specialized Ukrainian-language guidance would be lost from the skill distribution.

### 1.4 Analysis of `tests/sync_ecosystem.py`
Direct observation of `d:\poetry-skill\tests\sync_ecosystem.py`:
- **Lines 18–35**: `ROOT_MIRRORS = { ... }` hardcodes the mapping of 16 canonical reference files to root markdown filenames.
- **Lines 38–48**: `def sync_root_mirrors():` iterates through `ROOT_MIRRORS`, reads from `skills/.../references/` and writes back into `PROJECT_ROOT / dest_name`.
- **Lines 79–81**: In `if __name__ == "__main__":`, `sync_root_mirrors()` is invoked on every run:
  ```python
  if __name__ == "__main__":
      sync_root_mirrors()
      sync_agents_skills()
      sync_global_plugin()
  ```
- **Consequence**: Whenever `sync_ecosystem.py` is run, all 16 deleted root files are automatically regenerated at root. To permanently clean root, `ROOT_MIRRORS` and `sync_root_mirrors()` must be completely removed from `tests/sync_ecosystem.py`.

### 1.5 Cross-Reference Audit Across Documentation and Code
A comprehensive search for references to all 16 files, `packs/`, and the 2 Ukrainian guides was executed:
1. **`INSTALL.md` (Lines 19–21 & 82)**:
   - Line 19: `[`ukrainian-poetry-skill.md`](./ukrainian-poetry-skill.md)` -> points to root mirror file.
   - Line 20: `[`ukrainian-poetry-to-suno.md`](./ukrainian-poetry-to-suno.md)` -> points to root mirror file.
   - Line 21: `[`reference-to-style-cheatsheet.md`](./reference-to-style-cheatsheet.md)` -> points to root mirror file.
   - Line 82: mentions historical `59 тестів` (current count is 75+).
2. **`tests/audit_challenger2_empirical.py` (Lines 89–95 & 209–210)**:
   - Lines 89–95: `root_md_names` lists:
     `"AGENTS.md", "GEMINI.md", "song-structure-pack.md", "lyrics-to-suno-template.md", "suno-prompt-anti-patterns.md", "prompt-builder.md", "reference-to-style-cheatsheet.md", "mood-to-style-map.md", "ukrainian-poetry-to-suno.md", "ukrainian-poetry-skill.md", "ai-music-generation-meta-spec-v8.md"`
     (Note: Line 98 does `if p.exists(): target_files.append(p)`, so missing files don't fail, but stale names should be pruned).
   - Lines 209–210: `templates_to_test` includes `PROJECT_ROOT / "song-structure-pack.md"` and `PROJECT_ROOT / "lyrics-to-suno-template.md"`.
     (Note: Canonical versions `skills/ukrainian-poetry-to-suno/references/song-structure-pack.md` and `lyrics-to-suno-template.md` are already included on lines 204–205).
3. **`PROJECT.md` (Lines 26, 54)**:
   - Mentions historical task: `Synchronize root mirror files`.
4. **`VERSION.md` (Lines 55–56, 115–140)**:
   - Historical changelog entries documenting v1.0.0, v1.1.0, and v2.0.0 releases. (Historical changelogs should be preserved as history).
5. **`README.md` and `README.en.md`**:
   - Clean. No dead references to root mirror files. All links correctly reference `skills/ukrainian-poetry/`, `skills/ukrainian-poetry-to-suno/`, `AGENTS.md`, and `HOWTO.md`.
6. **`HOWTO.md` (Line 5)**:
   - Clean. Already explicitly states: *"Уся робота здійснюється через агенти в каталозі `.agents/skills/` (а не в кореневих файлах-дзеркалах)."*
7. **`AGENTS.md`, `GEMINI.md`, `skills/poetry-skill/SKILL.md`, `skills/ukrainian-poetry-to-suno/SKILL.md`**:
   - Clean. All reference indices already point to canonical paths (`skills/.../references/...` or relative `references/...`).

### 1.6 Existing Test Suite Verification
Executing the master test harness `py -3 tests/run_tests.py --all`:
- Total Test Cases: 75
- Passed: 75 / 75 (100.0% success rate)
- Failed: 0
- Warnings: 32 (non-fatal stylistic advisories)
- Average Poetry Rubric Score: 98.2 / 100
- Average Suno Rubric Score: 99.8 / 100
- Unit & Adversarial Suites: All Passed (Unit tests, Challenger 1, Challenger 2, Challenger Final, MetatagValidator, SunoValidator).
- Direct run of `py -3 tests/audit_challenger2_empirical.py`: 32 files checked, 243 templates verified, 0 errors, 0 violations.

---

## 2. Logic Chain

1. **Observation 1.1 & 1.2** established that all 16 files and the 8 files in `packs/` are byte-for-byte identical to their canonical counterparts in `skills/ukrainian-poetry/references/` and `skills/ukrainian-poetry-to-suno/references/` (and `references/packs/`).
   - *Inference*: Deleting these files from root loses zero documentation or intellectual property.
2. **Observation 1.3** established that `ukrainian-poetry-skill-uk.md` and `ukrainian-poetry-skill-lite.md` are unique assets containing high-value Ukrainian-language versification and anti-kitsch guidance, but currently exist only at root.
   - *Inference*: They must NOT be deleted without relocation. Relocating them to `skills/ukrainian-poetry/references/` integrates them into the canonical skill packaging, meaning `tests/sync_ecosystem.py` will automatically propagate them to `.agents/skills/` and the global Gemini plugin directory.
3. **Observation 1.4** proved that `tests/sync_ecosystem.py` contains active code (`sync_root_mirrors()`) that rewrites the 16 files to root upon every invocation.
   - *Inference*: Any manual deletion of root files without refactoring `tests/sync_ecosystem.py` will be undone the moment sync runs. Removing `ROOT_MIRRORS` and `sync_root_mirrors()` is a mandatory prerequisite.
4. **Observation 1.5** identified stale references in `INSTALL.md` (lines 19–21) and `tests/audit_challenger2_empirical.py` (lines 89–95, 209–210).
   - *Inference*: To guarantee no broken links or missing paths in future audits, `INSTALL.md` must be redirected to `skills/.../references/`, and `audit_challenger2_empirical.py` must remove dead root paths.
5. **Observation 1.6** confirmed that `tests/run_tests.py` and its 4 tiers do not import or validate root mirror files.
   - *Inference*: Root cleanup is completely safe and causes zero regression in test pass rates.

---

## 3. Caveats

1. **Upstream Meta-Spec Relocation**: `ai-music-generation-meta-spec-v8.md` was moved from root to `source/upstream/ai-music-generation-meta-spec-v8.md` in recent worktree changes. `tests/sync_ecosystem.py` line 70 checks `for root_file in ["AGENTS.md", "GEMINI.md", "ai-music-generation-meta-spec-v8.md"]:` using `if src.exists():`. It is recommended to update the script so it looks for `ai-music-generation-meta-spec-v8.md` in `source/upstream/` if not found at root.
2. **Historical Logs in `VERSION.md`**: `VERSION.md` contains historical changelogs for v1.0.0–v2.0.0 mentioning root files. These entries reflect past history and do not need to be rewritten, maintaining git audit integrity.
3. **Root files vs Local Workflows**: Some external tools or IDE bookmarks might expect `ukrainian-poetry-skill.md` at root. Relocating to canonical `skills/` adheres to the Agent Skills Standard (frontmatter + modular references) and avoids root pollution.

---

## 4. Conclusion & Implementation Plan

### 4.1 Step 1: Relocate Standalone Ukrainian Guides
Move the two Ukrainian guides into `skills/ukrainian-poetry/references/`:
```bash
Move-Item "d:\poetry-skill\ukrainian-poetry-skill-uk.md" "d:\poetry-skill\skills\ukrainian-poetry\references\ukrainian-poetry-skill-uk.md"
Move-Item "d:\poetry-skill\ukrainian-poetry-skill-lite.md" "d:\poetry-skill\skills\ukrainian-poetry\references\ukrainian-poetry-skill-lite.md"
```
*(Optional: Also place copies in `docs/` if general documentation browsing requires them).*

Update `skills/ukrainian-poetry/SKILL.md` reference index table:
```markdown
| Ukrainian-Language Reference Guide | `references/ukrainian-poetry-skill-uk.md` |
| Quick-Reference Cheat Sheet | `references/ukrainian-poetry-skill-lite.md` |
```

### 4.2 Step 2: Delete 16 Root Redundant Mirrors and `packs/` Folder
Delete the following 16 files from `d:\poetry-skill\`:
1. `ukrainian-poetry-skill.md`
2. `ukrainian-poetry-to-suno.md`
3. `lyrics-to-suno-template.md`
4. `song-structure-pack.md`
5. `suno-prompt-anti-patterns.md`
6. `prompt-builder.md`
7. `reference-to-style-cheatsheet.md`
8. `mood-to-style-map.md`
9. `suno-style-rubric.md`
10. `reference-breakdown-examples.md`
11. `ukrainian-song-scenarios.md`
12. `suno-prompt-tests.md`
13. `ukrainian-poetry-skill-rubric.md`
14. `ukrainian-poetry-skill-input-template.md`
15. `ukrainian-poetry-skill-stress-pack.md`
16. `ukrainian-poetry-skill-tests.md`

Delete directory:
- `d:\poetry-skill\packs\` (including all 8 internal files).

### 4.3 Step 3: Refactor `tests/sync_ecosystem.py`
Replace the implementation of `tests/sync_ecosystem.py` with:
```python
#!/usr/bin/env python3
"""
Ecosystem Skill & Plugin Synchronization Script.
Synchronizes all canonical skills between skills/, .agents/skills/,
and global plugin directory C:\\Users\\sm9sh\\.gemini\\config\\plugins\\poetry-skill/
No files are copied to the repository root directory.
"""

import os
import shutil
import pathlib

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS_DIR = PROJECT_ROOT / "skills"
AGENTS_SKILLS_DIR = PROJECT_ROOT / ".agents" / "skills"
GLOBAL_PLUGIN_DIR = pathlib.Path(r"C:\Users\sm9sh\.gemini\config\plugins\poetry-skill")


def sync_agents_skills():
    print("=== Syncing .agents/skills/ Directory ===")
    if AGENTS_SKILLS_DIR.exists():
        shutil.rmtree(AGENTS_SKILLS_DIR)
    shutil.copytree(SKILLS_DIR, AGENTS_SKILLS_DIR)
    print(f"  [OK] Copied {SKILLS_DIR} -> {AGENTS_SKILLS_DIR}")


def sync_global_plugin():
    print("\n=== Syncing Global Plugin Directory ===")
    GLOBAL_PLUGIN_DIR.mkdir(parents=True, exist_ok=True)
    
    # 1. Copy all skills
    dest_skills = GLOBAL_PLUGIN_DIR / "skills"
    if dest_skills.exists():
        shutil.rmtree(dest_skills)
    shutil.copytree(SKILLS_DIR, dest_skills)
    print(f"  [OK] Copied skills -> {dest_skills}")
    
    # 2. Copy root config files
    config_files = [
        ("AGENTS.md", PROJECT_ROOT / "AGENTS.md"),
        ("GEMINI.md", PROJECT_ROOT / "GEMINI.md"),
        ("ai-music-generation-meta-spec-v8.md", PROJECT_ROOT / "source" / "upstream" / "ai-music-generation-meta-spec-v8.md"),
    ]
    for filename, src in config_files:
        if not src.exists() and filename == "ai-music-generation-meta-spec-v8.md":
            src = PROJECT_ROOT / filename
        if src.exists():
            dest = GLOBAL_PLUGIN_DIR / filename
            shutil.copy2(src, dest)
            print(f"  [OK] Copied {src.name} -> {dest}")


if __name__ == "__main__":
    sync_agents_skills()
    sync_global_plugin()
    print("\n[OK] Ecosystem Synchronization Complete!")
```

### 4.4 Step 4: Fix References in `INSTALL.md`
In `d:\poetry-skill\INSTALL.md`, lines 18–22:
```markdown
### 1.2. Claude.ai (Веб / Projects)
1. Створіть новий проєкт у Claude.ai (**Projects**).
2. У розділ **Project Knowledge** завантажте:
   - [`skills/ukrainian-poetry/references/full-guide.md`](./skills/ukrainian-poetry/references/full-guide.md) (повна поетична інструкція);
   - [`skills/ukrainian-poetry-to-suno/references/full-guide.md`](./skills/ukrainian-poetry-to-suno/references/full-guide.md) (повна музична інструкція);
   - [`skills/ukrainian-poetry-to-suno/references/reference-to-style-cheatsheet.md`](./skills/ukrainian-poetry-to-suno/references/reference-to-style-cheatsheet.md) (таблиця референсів).
3. У поле **Project Instructions** скопіюйте текст із [`CLAUDE.md`](./CLAUDE.md).
```
And update line 82:
`Всі 75+ тестів мають повернути статус [PASS] зі 100% успішністю.`

### 4.5 Step 5: Clean Up `tests/audit_challenger2_empirical.py`
In `d:\poetry-skill\tests\audit_challenger2_empirical.py`:
- Lines 89–95:
  ```python
  root_md_names = [
      "AGENTS.md", "GEMINI.md"
  ]
  ```
- Lines 203–211:
  Remove the two root entries `PROJECT_ROOT / "song-structure-pack.md"` and `PROJECT_ROOT / "lyrics-to-suno-template.md"` from `templates_to_test`.

---

## 5. Verification Method

### 5.1 Verification Commands
1. **Sync Execution**:
   ```bash
   py -3 tests/sync_ecosystem.py
   ```
   *Expected outcome*: Output shows syncing of `.agents/skills/` and global plugin. **Zero** root mirror files created.
2. **Root Cleanliness Assertion**:
   ```powershell
   # In PowerShell, assert deleted files do not exist at root:
   $mirrors = @(
       'ukrainian-poetry-skill.md', 'ukrainian-poetry-to-suno.md', 'lyrics-to-suno-template.md',
       'song-structure-pack.md', 'suno-prompt-anti-patterns.md', 'prompt-builder.md',
       'reference-to-style-cheatsheet.md', 'mood-to-style-map.md', 'suno-style-rubric.md',
       'reference-breakdown-examples.md', 'ukrainian-song-scenarios.md', 'suno-prompt-tests.md',
       'ukrainian-poetry-skill-rubric.md', 'ukrainian-poetry-skill-input-template.md',
       'ukrainian-poetry-skill-stress-pack.md', 'ukrainian-poetry-skill-tests.md',
       'ukrainian-poetry-skill-uk.md', 'ukrainian-poetry-skill-lite.md'
   )
   $found = $mirrors | Where-Object { Test-Path (Join-Path "d:\poetry-skill" $_) }
   if ($found.Count -eq 0 -and -not (Test-Path "d:\poetry-skill\packs")) { "ROOT IS CLEAN" } else { "LEFTOVERS FOUND: $found" }
   ```
3. **Test Suite Verification**:
   ```bash
   py -3 tests/run_tests.py --all
   ```
   *Expected outcome*: 75+ tests pass with code 0 (100% success rate).
4. **Empirical Audit Verification**:
   ```bash
   py -3 tests/audit_challenger2_empirical.py
   ```
   *Expected outcome*: Exits with code 0, 0 errors, 0 violations.

### 5.2 Invalidation Conditions
- Any invocation of `py -3 tests/sync_ecosystem.py` recreates any of the 16 mirror files or `packs/` at root.
- Any link in `README.md`, `README.en.md`, `HOWTO.md`, or `INSTALL.md` throws a 404 or points to a non-existent file.
- `ukrainian-poetry-skill-uk.md` or `ukrainian-poetry-skill-lite.md` are deleted without being preserved in `skills/ukrainian-poetry/references/`.
- Any regression in `py -3 tests/run_tests.py --all` resulting in test failures.

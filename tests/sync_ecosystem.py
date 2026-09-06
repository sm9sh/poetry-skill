#!/usr/bin/env python3
"""
Ecosystem Skill & Plugin Synchronization Script.
Synchronizes all canonical skills between skills/, .agents/skills/,
and global plugin directory C:\\Users\\sm9sh\\.gemini\\config\\plugins\\poetry-skill/
No files are copied to the repository root directory.
"""

import os
import sys
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


DEPRECATED_ROOT_FILES = [
    "ukrainian-poetry-skill.md",
    "ukrainian-poetry-to-suno.md",
    "lyrics-to-suno-template.md",
    "song-structure-pack.md",
    "suno-prompt-anti-patterns.md",
    "prompt-builder.md",
    "reference-to-style-cheatsheet.md",
    "mood-to-style-map.md",
    "suno-style-rubric.md",
    "reference-breakdown-examples.md",
    "ukrainian-song-scenarios.md",
    "suno-prompt-tests.md",
    "ukrainian-poetry-skill-rubric.md",
    "ukrainian-poetry-skill-input-template.md",
    "ukrainian-poetry-skill-stress-pack.md",
    "ukrainian-poetry-skill-tests.md",
    "ukrainian-poetry-skill-uk.md",
    "ukrainian-poetry-skill-lite.md",
]


def verify_root_cleanliness() -> bool:
    print("\n=== Verifying Repository Root Cleanliness ===")
    violations = []
    for filename in DEPRECATED_ROOT_FILES:
        target = PROJECT_ROOT / filename
        if target.exists():
            violations.append(str(target))
    packs_dir = PROJECT_ROOT / "packs"
    if packs_dir.exists():
        violations.append(str(packs_dir))

    if violations:
        print(f"  [ERROR] Found {len(violations)} deprecated mirror file(s) in repository root:")
        for v in violations:
            print(f"    - {v}")
        return False
    else:
        print("  [OK] Repository root is 100% clean (zero deprecated mirror files or packs/ found).")
        return True


if __name__ == "__main__":
    sync_agents_skills()
    sync_global_plugin()
    clean = verify_root_cleanliness()
    if not clean:
        sys.exit(1)
    print("\n[OK] Ecosystem Synchronization Complete!")


#!/usr/bin/env python3
"""
Ecosystem & Root Markdown Synchronization Script.
Synchronizes all skills, references, root mirrors, .agents/skills/,
and global plugin directory C:\\Users\\sm9sh\\.gemini\\config\\plugins\\poetry-skill/
"""

import os
import shutil
import pathlib

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS_DIR = PROJECT_ROOT / "skills"
AGENTS_SKILLS_DIR = PROJECT_ROOT / ".agents" / "skills"
GLOBAL_PLUGIN_DIR = pathlib.Path(r"C:\Users\sm9sh\.gemini\config\plugins\poetry-skill")

# Root file mirror mapping
ROOT_MIRRORS = {
    "ukrainian-poetry-to-suno.md": SKILLS_DIR / "ukrainian-poetry-to-suno" / "references" / "full-guide.md",
    "ukrainian-poetry-skill.md": SKILLS_DIR / "ukrainian-poetry" / "references" / "full-guide.md",
    "lyrics-to-suno-template.md": SKILLS_DIR / "ukrainian-poetry-to-suno" / "references" / "lyrics-to-suno-template.md",
    "song-structure-pack.md": SKILLS_DIR / "ukrainian-poetry-to-suno" / "references" / "song-structure-pack.md",
    "suno-prompt-anti-patterns.md": SKILLS_DIR / "ukrainian-poetry-to-suno" / "references" / "suno-prompt-anti-patterns.md",
    "prompt-builder.md": SKILLS_DIR / "ukrainian-poetry-to-suno" / "references" / "prompt-builder.md",
    "reference-to-style-cheatsheet.md": SKILLS_DIR / "ukrainian-poetry-to-suno" / "references" / "reference-to-style-cheatsheet.md",
    "mood-to-style-map.md": SKILLS_DIR / "ukrainian-poetry-to-suno" / "references" / "mood-to-style-map.md",
    "suno-style-rubric.md": SKILLS_DIR / "ukrainian-poetry-to-suno" / "references" / "rubric.md",
    "reference-breakdown-examples.md": SKILLS_DIR / "ukrainian-poetry-to-suno" / "references" / "reference-breakdown-examples.md",
    "ukrainian-song-scenarios.md": SKILLS_DIR / "ukrainian-poetry-to-suno" / "references" / "ukrainian-song-scenarios.md",
    "suno-prompt-tests.md": SKILLS_DIR / "ukrainian-poetry-to-suno" / "references" / "tests.md",
    "ukrainian-poetry-skill-rubric.md": SKILLS_DIR / "ukrainian-poetry" / "references" / "rubric.md",
    "ukrainian-poetry-skill-input-template.md": SKILLS_DIR / "ukrainian-poetry" / "references" / "input-templates.md",
    "ukrainian-poetry-skill-stress-pack.md": SKILLS_DIR / "ukrainian-poetry" / "references" / "stress-tests.md",
    "ukrainian-poetry-skill-tests.md": SKILLS_DIR / "ukrainian-poetry" / "references" / "tests.md",
}


def sync_root_mirrors():
    print("=== Syncing Root Markdown Mirror Files ===")
    for dest_name, src_path in ROOT_MIRRORS.items():
        dest_path = PROJECT_ROOT / dest_name
        if src_path.exists():
            content = src_path.read_text(encoding="utf-8")
            dest_path.write_text(content, encoding="utf-8")
            print(f"  [OK] Mirrored: {src_path.relative_to(PROJECT_ROOT)} -> {dest_name}")
        else:
            print(f"  [WARN] Source file not found: {src_path}")


def sync_agents_skills():
    print("\n=== Syncing .agents/skills/ Directory ===")
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
    for root_file in ["AGENTS.md", "GEMINI.md", "ai-music-generation-meta-spec-v8.md"]:
        src = PROJECT_ROOT / root_file
        if src.exists():
            dest = GLOBAL_PLUGIN_DIR / root_file
            shutil.copy2(src, dest)
            print(f"  [OK] Copied {root_file} -> {dest}")


if __name__ == "__main__":
    sync_root_mirrors()
    sync_agents_skills()
    sync_global_plugin()
    print("\n[OK] Ecosystem Synchronization Complete!")

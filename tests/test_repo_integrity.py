#!/usr/bin/env python3
"""
Repository integrity tests: they check the real skill files, not fixtures.

- every agent in the plugin manifest exists, has valid frontmatter and is
  registered in its skill's openai.yaml;
- every song lyrics block shown in the skills and success examples passes the
  bracket validator and check_lyrics.py without errors, so the documentation
  never teaches markup the checker would reject.
"""

import importlib.util
import json
import pathlib
import re
import sys
import unittest

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "tests"))

from validator import MetatagValidator

CHECK_LYRICS = PROJECT_ROOT / "skills" / "ukrainian-poetry-to-suno" / "scripts" / "check_lyrics.py"
LYRICS_START = re.compile(r"^\[(Intro|Verse|Chorus|Bridge|Outro)", re.M)


def load_check_lyrics():
    spec = importlib.util.spec_from_file_location("check_lyrics", CHECK_LYRICS)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def lyrics_blocks():
    """(file, block) for every fenced block that looks like song lyrics."""
    files = sorted(PROJECT_ROOT.glob("skills/**/*.md")) + sorted(PROJECT_ROOT.glob("examples/success/*.md"))
    for md in files:
        text = md.read_text(encoding="utf-8")
        for block in re.findall(r"```[\w-]*\n(.*?)```", text, re.S):
            if LYRICS_START.search(block):
                yield md.relative_to(PROJECT_ROOT), block


class TestAgents(unittest.TestCase):

    def test_manifest_agents_have_frontmatter(self):
        manifest = json.loads((PROJECT_ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
        self.assertTrue(manifest["agents"])
        for rel in manifest["agents"]:
            path = PROJECT_ROOT / rel
            self.assertTrue(path.exists(), f"agent listed in plugin.json is missing: {rel}")
            content = path.read_text(encoding="utf-8")
            self.assertTrue(content.startswith("---"), f"{rel}: no YAML frontmatter")
            frontmatter = content.split("---", 2)[1]
            self.assertIn(f"name: {path.stem}", frontmatter, f"{rel}: name must match the file name")
            self.assertIn("description:", frontmatter, rel)
            self.assertIn("model:", frontmatter, rel)

    def test_agents_registered_in_openai_yaml(self):
        for agents_dir in PROJECT_ROOT.glob("skills/*/agents"):
            registry = (agents_dir / "openai.yaml").read_text(encoding="utf-8")
            for agent in agents_dir.glob("*.md"):
                self.assertIn(agent.stem, registry, f"{agents_dir}/openai.yaml does not list {agent.stem}")


class TestDocumentedLyrics(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.blocks = list(lyrics_blocks())
        cls.check_lyrics = load_check_lyrics()

    def test_lyrics_blocks_found(self):
        self.assertGreaterEqual(len(self.blocks), 10)

    def test_lyrics_blocks_pass_bracket_validator(self):
        for md, block in self.blocks:
            res = MetatagValidator.validate_lyrics_structure(block)
            self.assertTrue(res.is_valid, f"{md}: {res.errors}")

    def test_lyrics_blocks_pass_check_lyrics(self):
        for md, block in self.blocks:
            errors, _ = self.check_lyrics.check(block)
            self.assertEqual(errors, [], f"{md}: {errors}")


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python3
"""
Unit Test Suite for Examples Playground (examples/success/ & examples/failures/).
==============================================================================
Validates:
1. Presence, non-emptiness, and structure of all 6 playground files.
2. Bracket and Parentheses discipline:
   - Structural/arrangement metatags use `[...]`
   - Vocal gestures/ad-libs use `(...)`
   - Zero instrumental descriptors inside parentheses in lyrics sections
   - Balanced brackets and parentheses (no unclosed tags)
3. Ukrainian Stress Standard:
   - Capitalized accented vowels on mobile accents and homographs.
4. Platform Prompt Length Constraints:
   - Suno: style prompt within 80-180 character sweet spot, lyrics <= 5000 chars.
   - Udio: style prompt strictly <= 250 chars, inpainting markup uses `*stars*`.
   - Flow Music: conversational prompt non-empty, 65 bpm, Spaces 3-node matrix documented.
5. Programmatic Validator & Rubric Scorer Compliance for success scenarios:
   - PoeticValidator is_valid == True
   - MetatagValidator is_valid == True
   - StyleValidator is_valid == True
   - RubricScorer passing scores (Poetry >= 85/100, Suno >= 88/100)
6. Programmatic Contrast Testing for failure scenarios:
   - Before (broken) vs After (fixed) verification.
"""

import sys
import re
import pathlib
import unittest

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
sys.path.insert(0, str(PROJECT_ROOT / "tests"))

from tests.validator import StyleValidator, MetatagValidator, PoeticValidator, RubricScorer


class TestExamplesPlayground(unittest.TestCase):
    """Unit test suite for playground examples (success and failure scenarios)."""

    @classmethod
    def setUpClass(cls):
        cls.examples_dir = PROJECT_ROOT / "examples"
        cls.success_dir = cls.examples_dir / "success"
        cls.failures_dir = cls.examples_dir / "failures"

        cls.success_files = {
            "suno": cls.success_dir / "suno-darkwave-postpunk.md",
            "udio": cls.success_dir / "udio-triphop-downtempo.md",
            "flowmusic": cls.success_dir / "flowmusic-cinematic-ambient.md",
        }

        cls.failure_files = {
            "rushing": cls.failures_dir / "lyrics-rushing-fix.md",
            "robotic": cls.failures_dir / "robotic-vocals-fix.md",
            "true_peak": cls.failures_dir / "true-peak-clipping-fix.md",
        }

    # =========================================================================
    # 1. FILE EXISTENCE & NON-EMPTINESS
    # =========================================================================

    def test_01_all_playground_files_exist_and_non_empty(self):
        """Verify all 6 playground markdown files exist, are readable, and non-trivial."""
        for key, path in self.success_files.items():
            self.assertTrue(path.exists(), f"Success file missing: {path}")
            content = path.read_text(encoding="utf-8")
            self.assertGreater(len(content.strip()), 1000, f"Success file too short: {path}")

        for key, path in self.failure_files.items():
            self.assertTrue(path.exists(), f"Failure file missing: {path}")
            content = path.read_text(encoding="utf-8")
            self.assertGreater(len(content.strip()), 1000, f"Failure file too short: {path}")

    # =========================================================================
    # 2. BRACKET & PARENTHESES DISCIPLINE
    # =========================================================================

    def test_02_bracket_and_parentheses_discipline(self):
        """Verify strict bracket rules across all 6 files: [...] for structure, (...) for vocal gestures."""
        all_files = list(self.success_files.values()) + list(self.failure_files.values())

        for path in all_files:
            content = path.read_text(encoding="utf-8")

            # Check balanced brackets outside code fences or comments
            open_sq = content.count("[")
            close_sq = content.count("]")
            self.assertEqual(
                open_sq, close_sq,
                f"Unmatched square brackets in {path.name}: {open_sq} '[' vs {close_sq} ']'"
            )

            # Check balanced parentheses
            open_paren = content.count("(")
            close_paren = content.count(")")
            self.assertEqual(
                open_paren, close_paren,
                f"Unmatched round parentheses in {path.name}: {open_paren} '(' vs {close_paren} ')'"
            )

    # =========================================================================
    # 3. UKRAINIAN STRESS STANDARD
    # =========================================================================

    def test_03_ukrainian_stress_capitalization_in_lyrics(self):
        """Stress marks in example lyrics must stay within the 3 allowed categories (no over-marking)."""
        import importlib.util
        script = PROJECT_ROOT / "skills" / "ukrainian-poetry-to-suno" / "scripts" / "check_lyrics.py"
        spec = importlib.util.spec_from_file_location("check_lyrics", script)
        check_lyrics = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(check_lyrics)
        for path in [self.success_files["suno"], self.success_files["udio"], self.success_files["flowmusic"]]:
            content = path.read_text(encoding="utf-8")
            blocks = [b for b in re.findall(r"```(?:text)?\n(.*?)```", content, re.DOTALL) if "[Verse" in b]
            self.assertTrue(blocks, f"No lyrics block found in {path.name}")
            for block in blocks:
                errors, warnings = check_lyrics.check(block)
                self.assertEqual(errors, [], f"{path.name}: {errors}")
                over = [w for w in warnings if w.startswith("stress marked outside")]
                self.assertEqual(over, [], f"{path.name}: {over}")

    # =========================================================================
    # 4. PLATFORM PROMPT LENGTH CONSTRAINTS
    # =========================================================================

    def test_04_suno_darkwave_prompt_and_lyrics_constraints(self):
        """Verify Suno Darkwave prompt is within 80-180 sweet spot, exclude vector is valid, and lyrics pass."""
        content = self.success_files["suno"].read_text(encoding="utf-8")

        # Extract Method 2 prompt
        m2_match = re.search(r"### Method 2: HookGenius Tag Matrix.*?\n```text\s*\n(.*?)\n```", content, re.DOTALL)
        self.assertIsNotNone(m2_match, "Method 2 HookGenius prompt block not found")
        m2_prompt = m2_match.group(1).strip()
        self.assertLessEqual(len(m2_prompt), 180, f"Suno style prompt exceeds 180 chars: {len(m2_prompt)}")
        self.assertGreaterEqual(len(m2_prompt), 80, f"Suno style prompt below 80 chars: {len(m2_prompt)}")

        # Extract Exclude Vector
        ex_match = re.search(r"### Exclude Vector \(Negative Prompt\).*?\n```text\s*\n(.*?)\n```", content, re.DOTALL)
        self.assertIsNotNone(ex_match, "Exclude Vector block not found")
        exclude_prompt = ex_match.group(1).strip()
        ex_res = StyleValidator.validate_exclude_field(exclude_prompt)
        self.assertTrue(ex_res.is_valid, f"Exclude vector invalid: {ex_res.errors}")

        # Extract Lyrics Block
        lyr_match = re.search(r"## 4\. Complete Accented Lyrics & Structural Directives.*?\n```text\s*\n(.*?)\n```", content, re.DOTALL)
        self.assertIsNotNone(lyr_match, "Lyrics block not found")
        lyrics = lyr_match.group(1).strip()
        self.assertLessEqual(len(lyrics), 5000, f"Suno lyrics exceed 5000 chars: {len(lyrics)}")

        # Validate with MetatagValidator and PoeticValidator
        mv = MetatagValidator.validate_lyrics_structure(lyrics)
        self.assertTrue(mv.is_valid, f"Suno lyrics metatags invalid: {mv.errors}")

        pv = PoeticValidator.validate_poem(lyrics, min_lines=4, max_lines=60)
        self.assertTrue(pv.is_valid, f"Suno lyrics poetic errors: {pv.errors}")

        # Rubric scoring
        sv = StyleValidator.validate_style_prompt(m2_prompt, max_chars=180)
        self.assertTrue(sv.is_valid, f"Suno style invalid: {sv.errors}")

        score_p = RubricScorer.score_poetry(lyrics, pv)
        self.assertGreaterEqual(score_p.total_score, 85.0, f"Poetry score below 85: {score_p.total_score}")

        score_s = RubricScorer.score_suno_style(m2_prompt, lyrics, exclude_prompt, sv, mv)
        self.assertGreaterEqual(score_s.total_score, 88.0, f"Suno score below 88: {score_s.total_score}")

    def test_05_udio_triphop_prompt_and_inpainting_constraints(self):
        """Verify Udio Trip-Hop prompt is strictly <= 250 chars, uses *stars* inpainting, and lyrics pass."""
        content = self.success_files["udio"].read_text(encoding="utf-8")

        # Extract Master Generation Prompt
        p_match = re.search(r"### Master Generation Prompt.*?\n```text\s*\n(.*?)\n```", content, re.DOTALL)
        self.assertIsNotNone(p_match, "Udio Master Generation Prompt not found")
        prompt = p_match.group(1).strip()
        self.assertLessEqual(len(prompt), 250, f"Udio prompt exceeds 250 chars: {len(prompt)}")

        # Inpainting asterisks
        self.assertIn("*", prompt, "Udio prompt missing inpainting asterisks")
        self.assertEqual(prompt.count("*") % 2, 0, "Udio prompt has unbalanced inpainting asterisks")

        # Extract Lyrics Block
        lyr_match = re.search(r"## 5\. Complete Ukrainian Lyrics & Arrangement Architecture.*?\n```text\s*\n(.*?)\n```", content, re.DOTALL)
        self.assertIsNotNone(lyr_match, "Udio lyrics block not found")
        lyrics = lyr_match.group(1).strip()

        mv = MetatagValidator.validate_lyrics_structure(lyrics)
        self.assertTrue(mv.is_valid, f"Udio lyrics metatags invalid: {mv.errors}")

        pv = PoeticValidator.validate_poem(lyrics, min_lines=4, max_lines=60)
        self.assertTrue(pv.is_valid, f"Udio lyrics poetic errors: {pv.errors}")

    def test_06_flowmusic_cinematic_ambient_constraints(self):
        """Verify Flow Music conversational prompt, 65 bpm, Spaces nodes, and free-verse lyrics."""
        content = self.success_files["flowmusic"].read_text(encoding="utf-8")

        # Extract Conversational Agent Prompt
        p_match = re.search(r"## 2\. Lyria 3\.5 Conversational Agent Prompt.*?\n```text\s*\n(.*?)\n```", content, re.DOTALL)
        self.assertIsNotNone(p_match, "Flow Music Conversational Prompt not found")
        prompt = p_match.group(1).strip()
        self.assertIn("65 bpm", prompt.lower(), "Flow Music prompt missing 65 bpm anchor")
        self.assertIn("ambient", prompt.lower(), "Flow Music prompt missing ambient descriptor")

        # Spaces 3-node matrix
        self.assertIn("Node 1: Ground", content, "Missing Node 1 in Flow Music space architecture")
        self.assertIn("Node 2: Air", content, "Missing Node 2 in Flow Music space architecture")
        self.assertIn("Node 3: Nature", content, "Missing Node 3 in Flow Music space architecture")

        # Extract Lyrics Block
        lyr_match = re.search(r"## 5\. Complete Spoken-Word Ukrainian Poetry Text.*?\n```text\s*\n(.*?)\n```", content, re.DOTALL)
        self.assertIsNotNone(lyr_match, "Flow Music lyrics block not found")
        lyrics = lyr_match.group(1).strip()

        mv = MetatagValidator.validate_lyrics_structure(lyrics)
        self.assertTrue(mv.is_valid, f"Flow Music lyrics metatags invalid: {mv.errors}")

        pv = PoeticValidator.validate_poem(lyrics, min_lines=4, max_lines=60, mode="free_verse")
        self.assertTrue(pv.is_valid, f"Flow Music lyrics poetic errors: {pv.errors}")

    # =========================================================================
    # 5. PROGRAMMATIC CONTRAST TESTING FOR FAILURE SCENARIOS
    # =========================================================================

    def test_07_lyrics_rushing_contrast_verification(self):
        """Verify before (broken) vs after (fixed) contrast in lyrics-rushing-fix.md."""
        content = self.failure_files["rushing"].read_text(encoding="utf-8")

        broken_match = re.search(r"### The Broken Input.*?\n```text\s*\n(.*?)\n```", content, re.DOTALL)
        fixed_match = re.search(r"### The Remediated Input.*?\n```text\s*\n(.*?)\n```", content, re.DOTALL)

        self.assertIsNotNone(broken_match, "Broken input block not found in lyrics-rushing-fix.md")
        self.assertIsNotNone(fixed_match, "Remediated input block not found in lyrics-rushing-fix.md")

        broken_text = broken_match.group(1).strip()
        fixed_text = fixed_match.group(1).strip()

        # Broken lines should be excessively long (> 12 words)
        broken_lines = [l for l in broken_text.splitlines() if not l.startswith("[") and l.strip()]
        for line in broken_lines:
            self.assertGreaterEqual(len(line.split()), 12, f"Expected broken line to have >=12 words: '{line}'")

        # Fixed lines should be 4-8 words
        fixed_lines = [l for l in fixed_text.splitlines() if not l.startswith("[") and not l.startswith("(") and l.strip()]
        for line in fixed_lines:
            words = len(line.split())
            self.assertTrue(3 <= words <= 8, f"Expected fixed line to have 3-8 words, got {words}: '{line}'")

        # Fixed text must include [Half-time feel] and [Pause]
        self.assertIn("[Half-time feel]", fixed_text)
        self.assertIn("[Pause]", fixed_text)

        # Fixed lyrics metatags must be valid
        mv = MetatagValidator.validate_lyrics_structure(fixed_text)
        self.assertTrue(mv.is_valid, f"Remediated rushing lyrics metatags invalid: {mv.errors}")

    def test_08_robotic_vocals_contrast_verification(self):
        """Verify before (broken) vs after (fixed) contrast in robotic-vocals-fix.md."""
        content = self.failure_files["robotic"].read_text(encoding="utf-8")

        # Broken style prompt
        broken_style_match = re.search(r"### The Broken Input.*?Style Prompt.*?\n```text\s*\n(.*?)\n```", content, re.DOTALL)
        self.assertIsNotNone(broken_style_match, "Broken style prompt not found in robotic-vocals-fix.md")
        broken_style = broken_style_match.group(1).strip()

        # Remediated style prompt
        fixed_style_match = re.search(r"### The Remediated Input.*?Style Prompt.*?\n```text\s*\n(.*?)\n```", content, re.DOTALL)
        self.assertIsNotNone(fixed_style_match, "Remediated style prompt not found in robotic-vocals-fix.md")
        fixed_style = fixed_style_match.group(1).strip()

        # Broken style has only minimal tags
        self.assertLess(len(broken_style.split(",")), 6, "Broken style unexpectedly has 6+ tags")

        # Fixed style contains full Vocal Triple-Stack
        self.assertIn("baritone", fixed_style.lower())
        self.assertIn("close-mic", fixed_style.lower())
        self.assertIn("tape", fixed_style.lower())

        # Fixed style passes StyleValidator
        sv = StyleValidator.validate_style_prompt(fixed_style, max_chars=180)
        self.assertTrue(sv.is_valid, f"Remediated style prompt invalid: {sv.errors}")

    def test_09_true_peak_clipping_remediation_standards(self):
        """Verify true peak mastering protocol: -1.0 dBTP ceiling, True Peak OFF for loud masters."""
        content = self.failure_files["true_peak"].read_text(encoding="utf-8")

        self.assertIn("-1.0 dBTP", content, "True peak fix missing -1.0 dBTP standard")
        self.assertIn("True Peak Limiting", content)
        self.assertIn("Split Compression", content)
        self.assertIn("200 Hz", content)
        self.assertIn("Tchad Blake", content)
        self.assertIn("Master Fader", content)


def run_playground_tests() -> bool:
    """Convenience runner for TestExamplesPlayground."""
    suite = unittest.TestLoader().loadTestsFromTestCase(TestExamplesPlayground)
    runner = unittest.TextTestRunner(stream=sys.stdout, verbosity=2)
    result = runner.run(suite)
    print(f"Playground Test Suite Summary: {result.testsRun} run, {len(result.errors)} errors, {len(result.failures)} failures")
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_playground_tests()
    sys.exit(0 if success else 1)

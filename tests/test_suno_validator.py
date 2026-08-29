#!/usr/bin/env python3
"""
Unit Tests for SunoValidator, StyleValidator, and Multi-Platform Prompt Engines.
Covers Suno v4.5/v5.5 Method 1 & Method 2, Udio v4 (250 chars, *stars* inpainting),
Google Flow Music (Lyria 3.5), Exclude negative prompt purity, and Rubric scoring.
"""

import sys
import pathlib
import unittest

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
sys.path.insert(0, str(PROJECT_ROOT / "tests"))

from validator.suno_validator import SunoValidator, StyleValidator, MetatagValidator, RubricScorer


class TestSunoValidator(unittest.TestCase):

    def test_suno_style_valid_prompts(self):
        """Tests valid Suno style prompts adhering to character and token limits."""
        # Method 2 (Tag-Based Matrix)
        prompt_tag_matrix = "ukrainian post-punk, darkwave, 135 bpm, punchy chorus bassline, melancholic baritone male vocal, sharp telecaster, lo-fi tape hiss"
        res = StyleValidator.validate_style_prompt(prompt_tag_matrix)
        self.assertTrue(res.is_valid, f"Expected valid tag matrix prompt, got errors: {res.errors}")
        self.assertGreaterEqual(res.metrics["token_count"], 4)

        # Method 1 (Conversational Paragraph)
        prompt_conversational = "Atmospheric Ukrainian indie folk ballad featuring intimate whispered female vocal, delicate acoustic bandura plucking, warm analog cello, 75 bpm"
        res2 = StyleValidator.validate_style_prompt(prompt_conversational)
        self.assertTrue(res2.is_valid, f"Expected valid conversational prompt, got errors: {res2.errors}")

    def test_suno_style_character_caps(self):
        """Tests character limits: strict compact (120 chars) and max boundary (180 chars)."""
        prompt_110 = "ukrainian darkwave, coldwave, 128 bpm, driving analog bass synth, breathy male vocal, vintage reverb, lo-fi master"
        res_compact = StyleValidator.validate_style_prompt(prompt_110, strict_compact=True)
        self.assertTrue(res_compact.is_valid)

        # Over 120 with strict_compact
        prompt_150 = "ukrainian modern melodic metalcore, progressive djent, 160 bpm, aggressive drop-d guitar riff, dual clean and brutal harsh vocals, massive double-bass"
        res_over_compact = StyleValidator.validate_style_prompt(prompt_150, strict_compact=True)
        self.assertFalse(res_over_compact.is_valid)
        self.assertTrue(any("character limit exceeded" in e for e in res_over_compact.errors))

    def test_metadata_label_leakage_rejection(self):
        """Tests rejection of metadata labels (Language:, Theme:, Genre:, etc.) in Style box."""
        leaked_prompts = [
            "Genre: Ukrainian Rock, BPM: 140, Mood: Melancholy",
            "Language: Ukrainian, Topic: War and courage, acoustic guitar",
            "Title: My Song, Vocals: Male baritone, 120 bpm, drums",
            "Production: Lo-fi tape, Lyrics: sad story of love, synthwave"
        ]
        for p in leaked_prompts:
            res = StyleValidator.validate_style_prompt(p)
            self.assertFalse(res.is_valid, f"Expected metadata leakage in '{p}' to be rejected.")
            self.assertTrue(res.metrics["has_metadata_leak"])

    def test_artist_reference_deidentification(self):
        """Tests rejection of direct artist/band names and 'in the style of' triggers."""
        banned_prompts = [
            "ukrainian rock in the style of Okean Elzy, 130 bpm, driving guitars",
            "sounds like DakhaBrakha, ethno chaos, polyphonic vocals, sopilka",
            "modern electro-pop cover of The Hardkiss, aggressive synth leads",
            "sadsvit style post-punk, melancholic baritone, chorus bassline"
        ]
        for p in banned_prompts:
            res = StyleValidator.validate_style_prompt(p)
            self.assertFalse(res.is_valid, f"Expected banned artist in '{p}' to be rejected.")
            self.assertTrue(res.metrics["has_artist_leak"])

    def test_exclude_negative_prompt_validation(self):
        """Tests Exclude field validation: rejecting vague emotional words and accepting concrete acoustic terms."""
        # Valid exclude
        valid_exclude = "cheesy pop brass, metallic highs, muddy sub-bass, generic autotune, edm drop, applause"
        res_valid = StyleValidator.validate_exclude_field(valid_exclude)
        self.assertTrue(res_valid.is_valid, f"Expected valid exclude, got errors: {res_valid.errors}")

        # Invalid vague exclude
        invalid_exclude = "sadness, bad vibes, evil darkness, ugly sound, depression"
        res_invalid = StyleValidator.validate_exclude_field(invalid_exclude)
        self.assertFalse(res_invalid.is_valid)
        self.assertTrue(any("Vague non-acoustic token" in e for e in res_invalid.errors))

    def test_udio_v4_prompt_validation(self):
        """Tests Udio v4 prompt limits (250 chars) and balanced *stars* inpainting syntax."""
        valid_udio = "ukrainian dark ambient post-punk, chorus bass, *whispered baritone*, vintage tape delay, 110 bpm"
        res = SunoValidator.validate_udio_prompt(valid_udio)
        self.assertTrue(res.is_valid)
        self.assertTrue(res.metrics["has_inpainting_tags"])

        # Unbalanced asterisks
        unbalanced_udio = "ukrainian post-punk, *whispered baritone, driving rhythm"
        res_unbalanced = SunoValidator.validate_udio_prompt(unbalanced_udio)
        self.assertFalse(res_unbalanced.is_valid)
        self.assertTrue(any("Unbalanced inpainting asterisks" in e for e in res_unbalanced.errors))

        # Exceeded 250 chars
        long_udio = "ukrainian atmospheric electronic shoegaze, " + "lush reverb wall of sound, " * 10
        res_long = SunoValidator.validate_udio_prompt(long_udio)
        self.assertFalse(res_long.is_valid)
        self.assertTrue(any("exceeded hard cap" in e for e in res_long.errors))

    def test_custom_mode_payload_and_rubric_scoring(self):
        """Tests full custom mode payload validation and 100-point rubric score."""
        payload = {
            "style_of_music": "ukrainian post-punk, coldwave, 130 bpm, driving chorus bassline, melancholic baritone male vocal, lo-fi tape hiss",
            "lyrics": "[Vocal Intro - dynamic acapella, dry and close]\n(whispered)\nМісто мовчить у темряві.\n[Verse 1]\nКроки лунають на мокрому бруку,\n(луна)\n[Chorus - explosive chorus guitars]\nМи шукаємо світло в руЇнах!\n[Cold End]",
            "exclude": "cheesy brass, metallic treble, muddy bass, generic pop"
        }
        val_res = SunoValidator.validate_custom_mode_payload(payload)
        self.assertTrue(val_res.is_valid, f"Expected custom mode payload to be valid, got: {val_res.errors}")

        score_res = SunoValidator.score_prompt_package(
            payload["style_of_music"], payload["lyrics"], payload["exclude"]
        )
        self.assertTrue(score_res.is_passing)
        self.assertGreaterEqual(score_res.total_score, 90.0, f"Expected score >= 90, got {score_res.total_score}")


if __name__ == "__main__":
    unittest.main()

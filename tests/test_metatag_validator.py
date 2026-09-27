#!/usr/bin/env python3
"""
Unit Tests for MetatagValidator Engine.
Covers v8 meta-spec structural metatags, Ukrainian and English prefixes,
inline vocal delivery gestures in parentheses, hyphenated prefixes,
Vance Powell Verse 2 annotations, and anti-hallucination guardrails.
"""

import sys
import pathlib
import unittest

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
sys.path.insert(0, str(PROJECT_ROOT / "tests"))

from validator.metatag_validator import MetatagValidator, MetatagValidationResult


class TestMetatagValidator(unittest.TestCase):

    def test_canonical_structural_tags(self):
        """Tests that all canonical v8 structural prefixes are recognized."""
        canonical_tags = [
            "Intro", "Vocal Intro", "Verse", "Verse 1", "Verse 2",
            "Pre-Chorus", "Pre Chorus", "Chorus", "Mega-Chorus", "Mega Chorus",
            "Post-Chorus", "Post Chorus", "Bridge", "Drop", "Beat Drop",
            "Breakdown", "Instrumental Break", "Guitar Solo", "Bandura Solo",
            "Sopilka Solo", "Outro", "End", "Cold End", "Silence", "Pause",
            # Ukrainian
            "Інтро", "Вокальний вступ", "Вступ", "Куплет", "Куплет 1", "Куплет 2",
            "Передприспів", "Приспів", "Мега-приспів", "Мега приспів",
            "Післяприспів", "Міст", "Бридж", "Дроп", "Біт дроп", "Брейкдаун",
            "Програш", "Інструментал", "Соло", "Соло гітари", "Соло бандури",
            "Аутро", "Фінал", "Холодний фінал", "Затихання"
        ]
        for tag in canonical_tags:
            is_valid, err = MetatagValidator.is_valid_tag(tag)
            self.assertTrue(is_valid, f"Expected canonical tag '[{tag}]' to be valid, but got: {err}")

    def test_compound_sound_design_directives(self):
        """Tests compound sound-design tags with delimiters and hyphenated prefixes."""
        compound_tags = [
            "Vocal Intro - dynamic acapella, dry and close",
            "Beat Drop - heavy fuzz bass, punchy driving drums",
            "Pre-Chorus - rising snare roll, building tension",
            "Chorus - explosive, wide chorus guitars, wall of sound",
            "Mega-Chorus - maximum energy, layered harmonies, guitars clashing",
            "Breakdown - vocal and bassline only, intimate, dry",
            "Verse 2 - Vance Powell: add driving tambourine, syncopated backing",
            "Verse 2 - add driving tambourine, shaker, backing vocals",
            "Outro - fading out, solo analog synth, tape hiss",
            # Ukrainian
            "Вокальний вступ - динамічна акапела, сухий близький звук",
            "Біт дроп - важкий фазз-бас, потужні барабани",
            "Передприспів - наростання темпу, барабанний дріб",
            "Приспів - вибуховий приспів, широкий стереопростір",
            "Мега-приспів - повний вибух, максимальна енергія, стіна гітар",
            "Брейкдаун - тільки бас і вокал, інтимна подача",
            "Холодний фінал - різкий обрив на останньому слові"
        ]
        for tag in compound_tags:
            is_valid, err = MetatagValidator.is_valid_tag(tag)
            self.assertTrue(is_valid, f"Expected compound tag '[{tag}]' to be valid, but got: {err}")

    def test_nine_vocal_delivery_cues_in_brackets(self):
        """Tests that the 9 canonical vocal delivery cues are accepted in [] and backing lyrics in ()."""
        lyrics_with_cues = """[Vocal Intro - dynamic acapella]
[Whispered]
Тихий крок у порожнечі,
[Belted]
Голос розтинає морок!
[Verse 1]
[Falsetto]
Ніч торкається плечей,
[Screamed]
Біль спалює дощенту!
[Pre-Chorus]
[Building intensity]
Наростає гул у серці,
[Key Change]
Світло змінює орбіти.
[Chorus - harmonized, half-time feel]
Ми стоїмо на зламі епох,
[Ad-lib]
[Outro]
[Echo]
(ніколи знов)
[Cold End]"""

        res = MetatagValidator.validate_lyrics_structure(lyrics_with_cues)
        self.assertTrue(res.is_valid, f"Expected lyrics with bracketed vocal cues to pass, but got errors: {res.errors}")
        self.assertEqual(len(res.errors), 0)

    def test_rejection_of_delivery_cues_in_parentheses(self):
        """Delivery cues in () are sung by Suno v6 / Flow Music, so they must be rejected."""
        for cue in ["whispered", "belted, powerful", "key change", "half-time feel", "building intensity", "шепіт"]:
            res = MetatagValidator.validate_lyrics_structure(f"[Verse 1]\n({cue})\nРядок пісні")
            self.assertFalse(res.is_valid, f"Expected '({cue})' to be rejected")
            self.assertTrue(any("square brackets" in err for err in res.errors), res.errors)
        ok = MetatagValidator.validate_lyrics_structure("[Chorus]\nМи ще тут (ще тут)\n(о-о-о)")
        self.assertTrue(ok.is_valid, f"Singable backing vocals in () must pass: {ok.errors}")

    def test_rejection_of_instrumental_descriptors_in_parentheses(self):
        """Tests that instrumental arrangements inside () are rejected with clear errors."""
        bad_lyrics = """[Intro]
(Staccato cutting telecaster riff, driving bassline, punchy drum buildup)
[Verse 1]
Світло гасне у вікні.
(guitar solo)
(heavy 808 sub bass and synth arpeggio)"""

        res = MetatagValidator.validate_lyrics_structure(bad_lyrics)
        self.assertFalse(res.is_valid)
        self.assertGreaterEqual(len(res.errors), 1)
        self.assertTrue(any("found in parentheses" in e for e in res.errors))

    def test_prose_hallucination_detection(self):
        """Tests detection of conversational narrative prose inside brackets."""
        hallucinated_tags = [
            "The song begins with singer weeping softly",
            "Vocalist starts singing about lost memories",
            "Починається розмова двох закоханих",
            "Співак плаче під тиху музику",
            "She sings while guitars enter aggressively"
        ]
        for tag in hallucinated_tags:
            is_valid, err = MetatagValidator.is_valid_tag(tag)
            self.assertFalse(is_valid, f"Expected hallucinated tag '[{tag}]' to be rejected, but it passed.")
            self.assertIn("hallucination", (err or "").lower())

    def test_bracket_length_and_mismatches(self):
        """Tests bracket length limits and unclosed bracket detection."""
        # Over 120 chars
        long_tag = "Verse 1 - " + "very long descriptor " * 10
        is_valid, err = MetatagValidator.is_valid_tag(long_tag)
        self.assertFalse(is_valid)

        # Mismatched brackets
        mismatched_brackets = "[Intro\n[Verse 1]\nРядок тексту"
        res = MetatagValidator.validate_lyrics_structure(mismatched_brackets)
        self.assertFalse(res.is_valid)
        self.assertTrue(any("Mismatched square brackets" in e for e in res.errors))

        # Mismatched parentheses
        mismatched_parens = "[Intro]\n(whispered\n[Verse 1]\nРядок"
        res2 = MetatagValidator.validate_lyrics_structure(mismatched_parens)
        self.assertFalse(res2.is_valid)
        self.assertTrue(any("Mismatched parentheses" in e for e in res2.errors))


if __name__ == "__main__":
    unittest.main()

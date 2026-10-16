#!/usr/bin/env python3
"""
Unit tests for the heuristic validators in tests/validator/ that the tier
suites rely on: inversions, filler words, cliché rhymes, sensory grounding,
taboo words, rubric deductions and stress notation. Each check has a
positive case (the defect is caught) and a negative case (clean text passes).
"""

import sys
import pathlib
import unittest

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "tests"))

from validator import MetatagValidator, PoeticValidator, RubricScorer

CLEAN_STANZA = """Холодний вітер обіймає плечі,
На мокрий гравій опадає тінь,
Ліхтарі запалюють надвечір,
Старий годинник б'є у височінь."""


class TestPoeticValidator(unittest.TestCase):

    def test_inversions_detected(self):
        poem = ("У темну ніч дорогу я шукав,\nКрасиву пісню тихо чув я,\n"
                "Листа у темряві пишу я,\nВона мовчала довго бо,\nІ вірний шлях тоді пізнав він.")
        self.assertGreaterEqual(len(PoeticValidator.check_artificial_inversions(poem, mode="general")), 3)
        self.assertEqual(PoeticValidator.check_artificial_inversions(poem, mode="cossack_baroque"), [])

    def test_natural_word_order_not_flagged(self):
        poem = ("Вечірнє сонце дякує за день,\nНа мокрий гравій опадає тінь,\n"
                "Я чую шепіт стомлених людей,\nІ місто поринає у глибінь.")
        self.assertEqual(PoeticValidator.check_artificial_inversions(poem, mode="general"), [])

    def test_filler_words(self):
        bad = ("І ось я знов іду в цей темний сад,\nНу от і я мій день свій відшукав,\n"
               "Але ж бо той же самий листопад\nВже ось мені мій спокій повернув.")
        res = PoeticValidator.check_filler_words_and_pronouns(bad, mode="general")
        self.assertTrue(res["cluster_count"] >= 2 or res["high_density_stanzas"])

        clean = PoeticValidator.check_filler_words_and_pronouns(CLEAN_STANZA, mode="general")
        self.assertEqual(clean["cluster_count"], 0)
        self.assertEqual(clean["high_density_stanzas"], [])

    def test_cliche_rhymes(self):
        bad = ("У серці знов палає та любов,\nГаряча й чиста, наче свіжа кров.\n"
               "У темну ніч блукає гірка доля,\nДе у степах шумить козацька воля.")
        self.assertGreaterEqual(len(PoeticValidator.check_cliche_rhymes(bad)), 2)
        self.assertEqual(PoeticValidator.check_cliche_rhymes(CLEAN_STANZA), [])

    def test_sensory_grounding(self):
        concrete = ("Шорстке вапно на стінах кам'яниці, іржавий цвях і мідь,\n"
                    "Холодний попіл, м’ятний напій, запах полину і срібний дзвін.")
        res = PoeticValidator.evaluate_sensory_grounding(concrete)
        self.assertEqual(res["grounding_level"], "high")
        self.assertGreaterEqual(res["total_sensory_tokens"], 4)

        abstract = "Душа моя страждає у вічності буття,\nБезмежне почуття надії та нескінченного життя."
        self.assertIn(PoeticValidator.evaluate_sensory_grounding(abstract)["grounding_level"],
                      ("purely_abstract", "low"))

    def test_taboo_words_no_false_positives(self):
        safe = [
            ("У старому задушному вагоні пахло димом.", ["душа"]),
            ("Подолянка танцювала біля річки.", ["доля"]),
            ("Холодний вітер гуде у полі.", ["біль"]),
        ]
        for phrase, banned in safe:
            self.assertEqual(PoeticValidator.check_taboo_words(phrase, banned), [], phrase)

    def test_rubric_penalizes_flawed_poem(self):
        poem = ("І ось я знов любов шукав,\nАле гарячу бачив кров,\n"
                "Душа страждає у вічності без меж,\nІ ти збагнеш, що треба жити.")
        res = PoeticValidator.validate_poem(poem, banned_words=["душа", "кров"])
        score = RubricScorer.score_poetry(poem, res, mode="general")
        self.assertFalse(score.is_passing)
        self.assertLess(score.total_score, 85.0)

    def test_compound_tags_and_stress_notation(self):
        lyrics = ("[Intro - Staccato cutting telecaster riff, driving bassline]\n"
                  "[Verse 1 - Intimate breathy vocal]\nЦей дивний вИпадок і чорнОзем нічний,\n"
                  "(веди, дорОга)\n[Outro - Slow fade out]\n[End]")
        self.assertTrue(MetatagValidator.validate_lyrics_structure(lyrics).is_valid)
        self.assertGreaterEqual(PoeticValidator.check_stress_notation_in_lyrics(lyrics)["stressed_count"], 2)


if __name__ == "__main__":
    unittest.main()

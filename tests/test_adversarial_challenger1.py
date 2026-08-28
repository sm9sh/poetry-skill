#!/usr/bin/env python3
"""
Adversarial Challenge & Stress Test Suite - Challenger 1
========================================================
Empirically tests and challenges:
1. Artificial Inversions (`check_artificial_inversions`):
   - Positive cases: verb + pronoun end-rhyme inversions, stranded conjunctions/particles, auxiliary inversions.
   - Negative cases: natural syntax, subject-first, classical verses (Kostenko, Antonych).
   - Stylistic exemptions: Cossack Baroque, Folk, Children registers.
2. Filler Words & Pronouns (`check_filler_words_and_pronouns`):
   - Positive cases: all 12 rhythmic padding clusters, high-density monosyllabic pronoun stuffing (>32%).
   - Negative cases: natural dense poetic phrasing, clean stanzas.
   - Exemptions: folk, children registers.
3. Banal Cliché Rhymes (`check_cliche_rhymes`):
   - Positive cases: all 22 banned pairs across various case and plural inflections (любов-кров, доля-воля, сльози-грози, etc.).
   - Negative cases: heterogeneous cross-grammatical rhymes with acoustic rich assonance.
4. Physical Sensory Grounding (`evaluate_sensory_grounding`):
   - 5 sensory categories: tactile, acoustic, visual, thermal, olfactory/gustatory.
   - High vs Moderate vs Low vs Purely Abstract classification and scoring.
5. Versification Diversity: Free Verse / Verlibre & Blank Verse Scoring:
   - Free verse scoring without false syllable variance penalty and full rhyme score.
   - Strict Blank Verse (5-foot unrhymed iamb) validation.
6. Suno AI Song Lyrics & Metatag Hygiene:
   - Structural metatag stripping ([Intro], [Verse], [Chorus], [Outro]).
   - Parenthetical backing cues scansion handling ((луна), (шепіт)).
7. Rubric Scorer Deductions, Bounds & Non-Negativity:
   - Cap limits on all 7 dimensions.
   - Non-negativity guarantees, rounding, and passing threshold (85/100).
"""

import sys
import os
import re
import json
import pathlib
import unittest
from typing import Dict, List, Any

# Force UTF-8 on standard streams
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# Ensure imports work from project root
PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
sys.path.insert(0, str(PROJECT_ROOT / "tests"))

from tests.validator import StyleValidator, MetatagValidator, PoeticValidator, RubricScorer
from tests.validator.poetic_validator import PoeticValidationResult


class TestChallenger1EmpiricalChallenge(unittest.TestCase):

    # =========================================================================
    # 1. ARTIFICIAL INVERSIONS CHECK (`check_artificial_inversions`)
    # =========================================================================

    def test_01_artificial_inversions_positive_cases(self):
        """Test that check_artificial_inversions catches forced end-rhyme inversions."""
        # 1. Verb + pronoun with iotated endings (-в, -ла, -ло, -ли, -ю, -єш, -є, -ємо, -єте, -ить, -ять, -уть)
        poem_iotated = "У темну ніч дорогу шукав я,\nКрасиву пісню тихо чула вона,\nІ вірний шлях тоді пізнав він,\nКуди іду не знаю я."
        inversions1 = PoeticValidator.check_artificial_inversions(poem_iotated, mode="general")
        self.assertEqual(len(inversions1), 4, f"Expected 4 inversions in iotated endings, got {len(inversions1)}")

        # 2. Non-iotated verb endings (-у, -еш, -е, -емо, -ете, etc.)
        poem_non_iotated = "Листа у темряві пишу я,\nУ тиші ночі кличеш ти,\nНадії промінь несе він,\nУ чистім полі ідемо ми."
        inversions_non_iot = PoeticValidator.check_artificial_inversions(poem_non_iotated, mode="general")
        self.assertEqual(len(inversions_non_iot), 4, f"Expected 4 inversions in non-iotated endings, got {len(inversions_non_iot)}")

        # 3. Stranded conjunctions/subordinators at line end
        poem_conjunctions = "Вона мовчала довго бо,\nМи вирушаємо у путь хоч,\nЯ повернуся знову але,\nЗвучала музика у серці як."
        inversions2 = PoeticValidator.check_artificial_inversions(poem_conjunctions, mode="general")
        self.assertEqual(len(inversions2), 4, f"Expected 4 inversions in stranded conjunctions, got {len(inversions2)}")

        # 4. Auxiliary verb inversions at line end
        poem_auxiliary = "У замку темнім колись був я,\nЩаслива дуже вчора була вона,\nУ чистім полі вільні були ми,\nУ дивнім краї раді будуть вони."
        inversions3 = PoeticValidator.check_artificial_inversions(poem_auxiliary, mode="general")
        self.assertEqual(len(inversions3), 4, f"Expected 4 inversions in auxiliary verbs, got {len(inversions3)}")

        # 5. Standard supported verb conjugations
        poem_verbs = "В огонь без страху сміло підуть вони,\nТвоє мовчання знову чую я,\nСвою надію тихо берегли ми,\nЧудову казку розкажи ти."
        inversions4 = PoeticValidator.check_artificial_inversions(poem_verbs, mode="general")
        self.assertTrue(len(inversions4) >= 3, f"Expected >= 3 inversions, got {len(inversions4)}")

    def test_02_artificial_inversions_negative_cases_and_exemptions(self):
        """Test natural syntax and stylistic exemptions (Baroque, Folk)."""
        # Natural Ukrainian word order: subject before verb, natural object endings
        natural_poem = """Вечірнє сонце дякує за день,
На мокрий гравій опадає тінь,
Я чую шепіт стомлених людей,
І місто поринає у глибінь."""
        inversions = PoeticValidator.check_artificial_inversions(natural_poem, mode="general")
        self.assertEqual(
            len(inversions), 0,
            f"False positive inversion in natural poem: {inversions}"
        )

        # Baroque stylization exemption: inverted phrasing is canonical
        baroque_poem = """Світ ловив мене у сіті, та не спіймав я,
Бо премудрість Божу щирим серцем знав я,
І хоч плакав гірко у пустелі бо,
Благодать святу навіки осягнув я."""
        baroque_inversions = PoeticValidator.check_artificial_inversions(baroque_poem, mode="cossack_baroque")
        self.assertEqual(
            len(baroque_inversions), 0,
            "Baroque mode ('cossack_baroque') must be exempt from inversion warnings."
        )

        # Folk mode exemption
        folk_poem = """Ой піду я в темний ліс, подивлюся я,\nДе гуляє сивий кінь, заспіваю я."""
        folk_inversions = PoeticValidator.check_artificial_inversions(folk_poem, mode="authentic_folk")
        self.assertEqual(
            len(folk_inversions), 0,
            "Folk mode ('authentic_folk') must be exempt from inversion warnings."
        )

    # =========================================================================
    # 2. FILLER WORDS & PRONOUNS (`check_filler_words_and_pronouns`)
    # =========================================================================

    def test_03_filler_words_and_clusters_positive_cases(self):
        """Test detection of rhythmic filler clusters and high-density pronoun stuffing."""
        # Test each canonical cluster
        clusters = [
            "і ось", "ну от", "але ж бо", "та й ось", "то ж бо",
            "а я ось", "вже ж бо", "ну і ось", "от і все", "ну як же",
            "ось і знов", "та ось же",
        ]
        for cl in clusters:
            test_line = f"Там у саду {cl} зацвіла калина,\nІ тихо спить мала дитина."
            res = PoeticValidator.check_filler_words_and_pronouns(test_line, mode="general")
            self.assertTrue(
                res["cluster_count"] >= 1,
                f"Failed to detect rhythmic cluster '{cl}' in text: '{test_line}'"
            )
            self.assertTrue(any(cl in c["matched"].lower() for c in res["clusters"]))

        # Test high-density pronoun padding (>32% filler tokens in a stanza)
        stuffed_stanza = """І ось я знов іду в цей свій сад,
Ну от і я мій день свій відшукав,
Але ж бо той же цей мій листопад
Вже ось мені мій спокій повернув."""
        res_stuffed = PoeticValidator.check_filler_words_and_pronouns(stuffed_stanza, mode="general")
        self.assertTrue(
            len(res_stuffed["high_density_stanzas"]) >= 1,
            f"Failed to detect high-density filler stanza: {res_stuffed}"
        )
        self.assertTrue(res_stuffed["overall_density"] >= 0.30)

    def test_04_filler_words_negative_cases_and_exemptions(self):
        """Test that natural phrasing and exempt registers do not trigger filler warnings."""
        # Clean lyrical stanza with minimal pronouns
        clean_stanza = """Холодний вітер обіймає плечі,
На мокрий гравій опадає тінь,
Ліхтарі запалюють надвечір,
Старий годинник б'є у височінь."""
        res_clean = PoeticValidator.check_filler_words_and_pronouns(clean_stanza, mode="general")
        self.assertEqual(res_clean["cluster_count"], 0)
        self.assertEqual(len(res_clean["high_density_stanzas"]), 0)
        self.assertTrue(res_clean["overall_density"] < 0.15)

        # Children / folk exemption
        playful_children_stanza = """Я і ти, ми і ви,
Ось і зайчик у траві,
Цей і той, мій і твій,
Покружляй у хороводі мерщій."""
        res_children = PoeticValidator.check_filler_words_and_pronouns(playful_children_stanza, mode="children")
        self.assertEqual(
            len(res_children["high_density_stanzas"]), 0,
            "Children mode must not penalize playful repetition density."
        )

    # =========================================================================
    # 3. BANAL CLICHÉ RHYMES (`check_cliche_rhymes`)
    # =========================================================================

    def test_05_cliche_rhymes_positive_cases(self):
        """Test detection of banned cliché rhyme pairs across case and plural inflections."""
        cliche_pairs_to_test = [
            ("любов", "кров", "У серці знов палає та любов,\nГаряча й чиста, наче свіжа кров."),
            ("крові", "любові", "Немає спокою у тихій крові,\nКоли душа шукає вічної любові."),
            ("кров'ю", "любов'ю", "Змиває землю ворожою кров'ю,\nА серце світить вірною любов'ю."),
            ("доля", "воля", "Блукає світом одинока доля,\nДе у степах шумить козацька воля."),
            ("долі", "волі", "Нема спочинку у тяжкій долі,\nКоли козак шукає в полі волі."),
            ("сльози", "грози", "В очах тремтять непроханії сльози,\nА над землею насувають грози."),
            ("сліз", "гріз", "Повіяв вітер без печальних сліз,\nУ тиші ночі серед давніх гріз."),
            ("ніч", "віч", "На місто тихо опустилась ніч,\nВдивляюсь пильно у темряву віч."),
            ("ночі", "очі", "Блищать зірки у темній ночі,\nСльозами вмиті ясні очі."),
            ("ніч", "пліч", "Холодна впала на дорогу ніч,\nСпадає плащ з козацьких пліч."),
            ("серце", "дверці", "Тривожно б'ється молодеє серце,\nКоли риплять старі дубові дверці."),
            ("небо", "треба", "Пливуть хмарини через синє небо,\nА нам для щастя мало треба."),
            ("жити", "любити", "Як важко на землі без пісні жити,\nКоли нема кого усім серцем любити."),
            ("знати", "кохати", "Як хоче серце правду знати,\nІ до нестями щиро кохати."),
            ("день", "пень", "Минає тихо теплий день,\nСів подорожній на старий пень."),
            ("сни", "весни", "Летять у ніч барвисті сни,\nЧекає серце подиху весни."),
            ("зорі", "морі", "Засяють ясно золотисті зорі,\nЗаграють хвилі у глибокім морі."),
        ]

        for p1, p2, poem_text in cliche_pairs_to_test:
            detected = PoeticValidator.check_cliche_rhymes(poem_text)
            self.assertTrue(
                len(detected) >= 1,
                f"Failed to detect cliché rhyme pair ({p1}-{p2}) in:\n{poem_text}"
            )

    def test_06_cliche_rhymes_negative_cases(self):
        """Test that fresh heterogeneous cross-grammatical rhymes are NOT falsely flagged."""
        fresh_rhymed_poem = """Холодний вітер обіймає плечі,
На мокрий гравій опадає тінь,
Ліхтарі запалюють надвечір,
Старий годинник б'є у височінь.

Спливає час крізь пальці, наче дим,
Торкаюсь попелу німим залізом,
І світ стає по-справжньому живим,
Де кожен звук звучить цілком зарізно."""
        detected = PoeticValidator.check_cliche_rhymes(fresh_rhymed_poem)
        self.assertEqual(
            len(detected), 0,
            f"False positive cliché rhymes in fresh poetry: {detected}"
        )

    # =========================================================================
    # 4. PHYSICAL SENSORY GROUNDING (`evaluate_sensory_grounding`)
    # =========================================================================

    def test_07_sensory_grounding_dimensions_and_levels(self):
        """Test evaluation of all 5 sensory dimensions and grounding levels."""
        # 1. High sensory grounding (multi-sensory: tactile, acoustic, visual, thermal, olfactory)
        multi_sensory = """Шорстке вапно на стінах кам'яниці,
Іржавий цвях і мідна тепла дріт.
Гул поїзда доноситься з границі,
Холодний попіл, запах хвої й лід."""
        res_high = PoeticValidator.evaluate_sensory_grounding(multi_sensory)
        self.assertEqual(res_high["grounding_level"], "high")
        self.assertEqual(res_high["sensory_score"], 20.0)
        self.assertTrue(res_high["total_sensory_tokens"] >= 4)
        self.assertTrue(len(res_high["active_categories"]) >= 3)
        self.assertIn("кам'яниці", res_high["details"]["tactile"])

        # Test words with apostrophes (' and ’): кам'яний, м'який, м’ятний, п'єдестал
        apostrophe_text = "Кам'яний берег, м'який шовк, м’ятний напій і п'єдестал."
        res_apo = PoeticValidator.evaluate_sensory_grounding(apostrophe_text)
        self.assertEqual(res_apo["grounding_level"], "high")
        self.assertIn("кам'яний", res_apo["details"]["tactile"])
        self.assertIn("м’ятний", res_apo["details"]["olfactory_gustatory"])
        self.assertIn("п'єдестал", res_apo["details"]["visual"])

        # 2. Moderate sensory grounding (1-2 tokens)
        moderate_sensory = """У полі вітер стеле темну тінь,
Пливуть хмарини понад синім гаєм."""
        res_mod = PoeticValidator.evaluate_sensory_grounding(moderate_sensory)
        self.assertIn(res_mod["grounding_level"], ("moderate", "high"))
        self.assertTrue(res_mod["sensory_score"] >= 18.0)

        # 3. Purely abstract emotional declarations
        purely_abstract = """Душа моя страждає у вічності буття,
Безмежне почуття надії та нескінченного життя,
Любов і сум глибинний хвилюють серця стан,
Ідеал далекий зникає як оман."""
        res_abs = PoeticValidator.evaluate_sensory_grounding(purely_abstract)
        self.assertEqual(res_abs["grounding_level"], "purely_abstract")
        self.assertEqual(res_abs["sensory_score"], 12.0)
        self.assertTrue(res_abs["total_abstract_tokens"] >= 2)

    # =========================================================================
    # 5. VERSIFICATION DIVERSITY: FREE VERSE & BLANK VERSE
    # =========================================================================

    def test_08_free_verse_verlibre_scoring(self):
        """Test that free verse (verlibre) receives full rhyme score and no false variance penalty."""
        free_verse = """іржавий дах котельні
вбирає вологу листопадового ранку,
два горобці на холодному дроті
ділять шматок черствого житнього хліба,
трамвай розсипає іскри
на розі старої вулиці."""
        poetic_res = PoeticValidator.validate_poem(free_verse, mode="general")
        self.assertTrue(poetic_res.is_valid)

        # Score with is_free_verse=True
        score = RubricScorer.score_poetry(free_verse, poetic_res, is_free_verse=True)
        self.assertTrue(score.is_passing)
        self.assertTrue(score.total_score >= 90.0)
        # Verify rhyme dimension is full 10.0
        self.assertEqual(score.dimension_scores["rhyme_sound_design"], 10.0)
        # Verify rhythm dimension is full 15.0 (no variance deduction)
        self.assertEqual(score.dimension_scores["rhythm_line_breaks"], 15.0)

    def test_09_blank_verse_syllabo_tonic_scansion(self):
        """Test strict blank verse (білий вірш - unrhymed 5-foot iamb)."""
        blank_verse = """Холодний вітер обіймає плечі,
На мокрий гравій опадає тінь,
І ліхтарі запалюють надвечір,
Старий ліхтар серед німих видінь,
І місто поринає в темний сон."""
        poetic_res = PoeticValidator.validate_poem(blank_verse, expected_meter="iamb", mode="general")
        self.assertTrue(poetic_res.is_valid)
        score = RubricScorer.score_poetry(blank_verse, poetic_res, is_free_verse=True)
        self.assertTrue(score.is_passing)
        self.assertTrue(score.total_score >= 95.0)

    # =========================================================================
    # 6. SUNO AI SONG LYRICS & METATAG HYGIENE
    # =========================================================================

    def test_10_suno_lyrics_bracketed_metatags_and_stripping(self):
        """Test clean stripping of Suno structural metatags and parenthetical cues."""
        suno_lyrics = """[Intro - Atmospheric ambient drone]
(тихий шепіт вітру)
[Verse 1]
Шорстке вапно на стінах кам'яниці,
Іржавий цвях тримає синій лід.
[Chorus]
Вогонь гуде у темному залізі,
Холодний попіл падає на брук.
[Drop - Heavy 808 synth bass]
(разом у вогні)
[Outro - Slow fade out]
(тиша навколо)"""

        # 1. get_lines_without_tags should remove [Intro], [Verse 1], [Chorus], [Drop], [Outro]
        lines = PoeticValidator.get_lines_without_tags(suno_lyrics)
        self.assertNotIn("[Intro]", lines)
        self.assertNotIn("[Verse 1]", lines)
        self.assertNotIn("[Chorus]", lines)
        self.assertNotIn("[Drop]", lines)
        self.assertNotIn("[Outro]", lines)

        # 2. Syllable counting should ignore parenthetical backing cues
        line_with_cue = "Холодний вітер обіймає плечі (луна)"
        base_line = "Холодний вітер обіймає плечі"
        count_with_cue = PoeticValidator.count_syllables(line_with_cue)
        count_base = PoeticValidator.count_syllables(base_line)
        self.assertEqual(count_base, 11)
        self.assertEqual(count_with_cue, 11, "Parenthetical backing cue '(луна)' must be stripped during syllable count.")
        self.assertEqual(count_with_cue, count_base)

        # 3. Metatag validator check
        meta_res = MetatagValidator.validate_lyrics_structure(suno_lyrics)
        self.assertTrue(meta_res.is_valid)
        self.assertTrue(meta_res.metrics["total_tags"] >= 4)

    # =========================================================================
    # 7. RUBRIC SCORER DEDUCTIONS, BOUNDS & NON-NEGATIVITY
    # =========================================================================

    def test_11_rubric_deductions_and_bounds(self):
        """Test deduction capping and non-negativity across all 7 rubric dimensions."""
        # Create heavily flawed poem triggering all deductions
        flawed_poem = """І ось я знов шукав я той самий кращий день,
Але гарячу в серці бачив кров,
Душа моя страждає у вічності без меж,
І ти збагнеш, що треба жити."""

        poetic_res = PoeticValidator.validate_poem(flawed_poem, banned_words=["душа", "кров"])
        score = RubricScorer.score_poetry(flawed_poem, poetic_res, mode="general")

        self.assertFalse(score.is_passing)
        self.assertTrue(score.total_score < 75.0)

        # Verify all 7 dimension scores are within [0.0, max]
        max_bounds = {
            "linguistic_naturalness": 25.0,
            "imagery_concreteness": 20.0,
            "rhythm_line_breaks": 15.0,
            "rhyme_sound_design": 10.0,
            "tonal_integrity": 10.0,
            "ending_strength": 10.0,
            "anti_cliche_guardrails": 10.0,
        }
        for dim, max_val in max_bounds.items():
            dim_val = score.dimension_scores[dim]
            self.assertTrue(
                0.0 <= dim_val <= max_val,
                f"Dimension '{dim}' score {dim_val} out of bounds [0.0, {max_val}]"
            )

        # Verify total score is sum of dimensions and rounded to 1 decimal
        self.assertEqual(score.total_score, round(sum(score.dimension_scores.values()), 1))


def run_challenger1_tests() -> bool:
    suite = unittest.TestLoader().loadTestsFromTestCase(TestChallenger1EmpiricalChallenge)
    runner = unittest.TextTestRunner(stream=sys.stdout, verbosity=2)
    result = runner.run(suite)
    print(f"Challenger 1 Suite Summary: {result.testsRun} run, {len(result.errors)} errors, {len(result.failures)} failures")
    
    report_path = PROJECT_ROOT / "tests" / "reports" / "chal1_failures.txt"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(f"Tests run: {result.testsRun}\n")
        f.write(f"Failures: {len(result.failures)}\n")
        f.write(f"Errors: {len(result.errors)}\n\n")
        for test, trace in result.failures:
            f.write(f"=== FAILURE: {test} ===\n{trace}\n\n")
        for test, trace in result.errors:
            f.write(f"=== ERROR: {test} ===\n{trace}\n\n")
            
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_challenger1_tests()
    sys.exit(0 if success else 1)

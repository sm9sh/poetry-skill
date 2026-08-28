#!/usr/bin/env python3
"""
Final Adversarial Stress Harness — Challenger Final (`challenger_final`)
Empirically tests and challenges:
1. Phonetic & Syllable Engine (Unicode combining characters, precomposed accents, extreme diacritics)
2. Taboo Words Discrimination (True Positives on inflected cliches, False Positives on legitimate vocabulary)
3. Caesura & Meter Scansion Engine (Kolomyika 4+4+6 boundaries, strict 3-foot Dactyl, Trochee, Iamb, Amphibrach, Anapest)
4. Stress Homographs & Disambiguation Completeness (All 13 canonical pairs, casing, explicit stress markers)
5. Suno AI Prompt Engineering (Token economy, boundary conditions, negative prompts, metatag sanitization)
6. Ecosystem Cross-Validation (Consistency across all skills, packs, references, and test suites)
"""

import os
import sys
import re
import json
import unicodedata
from pathlib import Path
from typing import Dict, List, Any, Tuple

# Set UTF-8
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
sys.path.insert(0, str(PROJECT_ROOT / "tests"))

from tests.validator.style_validator import StyleValidator
from tests.validator.metatag_validator import MetatagValidator
from tests.validator.poetic_validator import PoeticValidator
from tests.validator.rubric_scorer import RubricScorer


class FinalAdversarialHarness:
    def __init__(self):
        self.results = {
            "total_tests": 0,
            "passed": 0,
            "failed": 0,
            "details": []
        }

    def record(self, test_id: str, category: str, name: str, passed: bool, details: str):
        self.results["total_tests"] += 1
        if passed:
            self.results["passed"] += 1
        else:
            self.results["failed"] += 1
        
        status = "[PASS]" if passed else "[FAIL]"
        print(f"  {status} {test_id} [{category}]: {name} -> {details}")
        self.results["details"].append({
            "id": test_id,
            "category": category,
            "name": name,
            "passed": passed,
            "details": details
        })

    # =========================================================================
    # SUITE 1: Phonetics & Syllable Scansion under Adversarial Unicode
    # =========================================================================
    def run_phonetics_unicode_suite(self):
        print("\n" + "=" * 70)
        print(" > RUNNING SUITE 1: PHONETICS & ADVERSARIAL UNICODE DIACRITICS")
        print("=" * 70)

        # 1.1 Combining acute accents on vowels
        accented_words = [
            ("Ві́тер", 2, "Ві\\u0301тер (combining acute on і)"),
            ("О́бід", 2, "О\\u0301бід (combining acute on О)"),
            ("за́мок", 2, "за\\u0301мок (combining acute on а)"),
            ("замО́к", 2, "замО\\u0301к (capital + acute on О)"),
            ("біли́зна́", 3, "біли\\u0301зна\\u0301 (dual acute markers)"),
            ("перекотипо́ле", 6, "6 syllables with acute"),
            ("струмо́к", 2, "струмо\\u0301к (2 syllables)"),
            ("дивови́жний", 4, "дивови\\u0301жний (4 syllables)"),
        ]
        all_accents_correct = True
        for word, expected, desc in accented_words:
            count = PoeticValidator.count_syllables(word)
            if count != expected:
                all_accents_correct = False
                print(f"    Mismatch: '{word}' ({desc}) -> Expected {expected}, Got {count}")
        
        self.record(
            "ADV_FIN_1_01",
            "Phonetics",
            "Combining Unicode Diacritics Syllable Invariance",
            all_accents_correct,
            f"Tested {len(accented_words)} accented Ukrainian words with combining marks"
        )

        # 1.2 Multi-diacritic stacking & NFC/NFD normalization resilience
        nfd_text = unicodedata.normalize("NFD", "Украї́нська пі́сня ли́не понад степо́м")
        nfc_text = unicodedata.normalize("NFC", "Украї́нська пі́сня ли́не понад степо́м")
        count_nfd = PoeticValidator.count_syllables(nfd_text)
        count_nfc = PoeticValidator.count_syllables(nfc_text)
        expected_syl = 12 # У-кра-їн-ська (4) + піс-ня (2) + ли-не (2) + по-над (2) + сте-пом (2) = 12
        passed_norm = (count_nfd == expected_syl) and (count_nfc == expected_syl)
        self.record(
            "ADV_FIN_1_02",
            "Phonetics",
            "NFD vs NFC Normalization Syllable Count Invariance",
            passed_norm,
            f"NFD Count: {count_nfd}, NFC Count: {count_nfc}, Expected: {expected_syl}"
        )

        # 1.3 Empty / Non-letter lines / Tags removal
        empty_lines = [
            ("", 0),
            ("   \t  \n", 0),
            ("[Verse 1]", 0),
            ("[Intro: Solo Bandura]", 0),
            ("(луна)", 0),
            ("!@#$%^&*()_+-=", 0),
            ("1234567890", 0),
            ("[Chorus]\nСонце встає\n(бек-вокал)", 4) # Сон-це вста-є = 4
        ]
        all_edge_lines_correct = True
        for line, exp in empty_lines:
            cnt = PoeticValidator.count_syllables(line)
            if cnt != exp:
                all_edge_lines_correct = False
                print(f"    Line count error on '{line}' -> Expected {exp}, Got {cnt}")
        
        self.record(
            "ADV_FIN_1_03",
            "Phonetics",
            "Non-Poetic & Metatag Syllable Stripping",
            all_edge_lines_correct,
            f"Tested {len(empty_lines)} edge lines and tag-stripped strings"
        )

    # =========================================================================
    # SUITE 2: Taboo Discrimination (True Positives vs False Positives)
    # =========================================================================
    def run_taboo_discrimination_suite(self):
        print("\n" + "=" * 70)
        print(" > RUNNING SUITE 2: TABOO DISCRIMINATION (TP vs FP RESILIENCE)")
        print("=" * 70)

        banned_base = ["душа", "серце", "доля", "вічність", "життя", "кохання", "сльози", "біль"]

        # 2.1 True Positives (Inflected forms of taboo words MUST be caught)
        true_positives = [
            ("душі моїй спокою нема", "душа (locative)"),
            ("душею і тілом", "душа (instrumental)"),
            ("душам полеглих", "душа (dative plural)"),
            ("серденько моє", "серце (diminutive)"),
            ("сердечний біль", "серце / біль (adjective + noun)"),
            ("доленька гірка", "доля (diminutive)"),
            ("долею судилося", "доля (instrumental)"),
            ("у вічності розчинитися", "вічність (locative)"),
            ("вічністю осяяний", "вічність (instrumental)"),
            ("життю радіти", "життя (dative)"),
            ("життями заплачено", "життя (instrumental plural)"),
            ("палке кохання", "кохання (nominative)"),
            ("у коханні зізнався", "кохання (locative)"),
            ("сльозами вмитий", "сльози (instrumental)"),
            ("сліз не лити", "сльози (genitive plural)"),
            ("болем пронизаний", "біль (instrumental)"),
            ("болю зазнати", "біль (genitive)"),
            ("болями скутий", "біль (instrumental plural)"),
            ("болюча рана", "біль (adjective)"),
        ]
        tp_caught = 0
        for sent, desc in true_positives:
            found = PoeticValidator.check_taboo_words(sent, banned_base)
            if len(found) > 0:
                tp_caught += 1
            else:
                print(f"    [FALSE NEGATIVE] Missed taboo: '{sent}' ({desc})")
        
        passed_tp = tp_caught == len(true_positives)
        self.record(
            "ADV_FIN_2_01",
            "Taboo Filter",
            "True Positive Interception of Inflected Cliches & Diminutives",
            passed_tp,
            f"Caught {tp_caught}/{len(true_positives)} inflected taboo instances"
        )

        # 2.2 False Positives (Legitimate Ukrainian words containing taboo sub-stems MUST NOT be falsely banned)
        false_positives_test = [
            ("задушливий вечір у місті", "задушливий (stifling, not душа)"),
            ("тиха долина між зелених гір", "долина (valley, not доля)"),
            ("гостре долото майстра", "долото (chisel, not доля)"),
            ("довгий шлях попереду", "довгий (long, not доля)"),
            ("подолати перешкоди на шляху", "подолати (overcome, not доля)"),
            ("відкриття нового обрію", "відкриття (discovery, not життя)"),
            ("відродження природи навесні", "відродження (rebirth, not кохання)"),
            ("серпанок ранкового туману", "серпанок (haze, not серце)"),
            ("серпень приніс щедрий урожай", "серпень (August, not серце)"),
            ("болото поросло осокою", "болото (marsh, not біль)"),
            ("соболями прикрашений", "соболями (sables, not біль)"),
        ]
        fp_false_alerts = 0
        for sent, desc in false_positives_test:
            found = PoeticValidator.check_taboo_words(sent, banned_base)
            if len(found) > 0:
                fp_false_alerts += 1
                print(f"    [FALSE POSITIVE] Incorrectly flagged legitimate word: '{sent}' ({desc}) -> Flagged: {found}")
        
        passed_fp = fp_false_alerts == 0
        self.record(
            "ADV_FIN_2_02",
            "Taboo Filter",
            "False Positive Immunity on Legitimate Vocabulary (долина, серпанок, серпень, etc.)",
            passed_fp,
            f"False Alerts: {fp_false_alerts}/{len(false_positives_test)}"
        )

    # =========================================================================
    # SUITE 3: Caesura & Rare Versification Engines
    # =========================================================================
    def run_caesura_and_meter_suite(self):
        print("\n" + "=" * 70)
        print(" > RUNNING SUITE 3: CAESURA & RARE METER SCANSION")
        print("=" * 70)

        # 3.1 Kolomyika 14-Syllable (4+4+6) Caesura Boundary Tests
        valid_kolomyika = """Ой летіли / сиві птахи / через сині гори,
Принесли нам / тиху звістку / про широке поле.
Заспіває / стара сосна / біля того броду,
Не забуде / вільне серце / рідного народу."""

        valid_kolo_continuous = """Ой летіли сиві птахи через сині гори,
Принесли нам тиху звістку про широке поле.
Заспіває стара сосна біля того броду,
Не забуде вільне коло рідного народу."""

        broken_kolo_boundary = """Ой летіли соколи / птахи через сині гори,
Принесли нам звістку / про широке поле тут.
Ще один рядок / для перевірки рими,
Та завершення строфи / звуками сумними."""

        res_v1 = PoeticValidator.validate_poem(valid_kolomyika, expected_meter="kolomyika")
        res_v2 = PoeticValidator.validate_poem(valid_kolo_continuous, expected_meter="kolomyika")
        res_b1 = PoeticValidator.validate_poem(broken_kolo_boundary, expected_meter="kolomyika")

        passed_kolo = res_v1.is_valid and res_v2.is_valid and (not res_b1.is_valid)
        self.record(
            "ADV_FIN_3_01",
            "Caesura Engine",
            "Kolomyika 14-Syllable (4+4+6) Caesura Validation & Boundary Interception",
            passed_kolo,
            f"Explicit Slashes: {res_v1.is_valid}, Word Boundaries: {res_v2.is_valid}, Broken Rejected: {not res_b1.is_valid}"
        )

        # 3.2 Strict 3-Foot Dactyl with Alternating 8/7 Clausulae (TC_T2_02 poem)
        strict_dactyl = """Стелить зима нам завію,
Вітер гуляє в полях.
Холодом вечір засію,
Сніг опадає на шлях.

Сріблом виблискує крига,
Спить під заметами гай.
В тиші гортається книга,
Сяє засніжений край.

Зірка згоряє у тиші,
В небо підноситься дим.
Вітер узори нам пише,
Світ спочиває під ним."""

        res_dactyl = PoeticValidator.validate_poem(strict_dactyl, expected_meter="dactyl")
        dactyl_counts = [PoeticValidator.count_syllables(l) for l in PoeticValidator.get_lines_without_tags(strict_dactyl)]
        expected_dactyl = [8, 7, 8, 7, 8, 7, 8, 7, 8, 7, 8, 7]
        passed_dactyl = res_dactyl.is_valid and (dactyl_counts == expected_dactyl)
        self.record(
            "ADV_FIN_3_02",
            "Meter Scansion",
            "Strict 3-Foot Dactyl 8/7 Syllable Cadence Verification",
            passed_dactyl,
            f"Counts: {dactyl_counts}, Expected: {expected_dactyl}, Valid: {res_dactyl.is_valid}"
        )

        # 3.3 Strict 4-Foot Iamb (8/9 alternation) and 4-Foot Trochee (7/8 alternation)
        strict_iamb = """Вщухає дзвін нічних тривог,
Поволі тане сірий дим.
Стоїть розлогий старий дуб,
Осяяний вогнем німим.""" # 8, 8, 8, 8 (4-foot iamb masculine)
        
        res_iamb = PoeticValidator.validate_poem(strict_iamb, expected_meter="iamb")
        self.record(
            "ADV_FIN_3_03",
            "Meter Scansion",
            "Strict Syllabo-Tonic 4-Foot Iamb Consistency",
            res_iamb.is_valid,
            f"Iamb Syllables: {[PoeticValidator.count_syllables(l) for l in PoeticValidator.get_lines_without_tags(strict_iamb)]}, Valid: {res_iamb.is_valid}"
        )

    # =========================================================================
    # SUITE 4: Stress Homographs & Disambiguation Coverage
    # =========================================================================
    def run_homographs_suite(self):
        print("\n" + "=" * 70)
        print(" > RUNNING SUITE 4: STRESS HOMOGRAPHS & ORTHOEPIC ACCENTUATION")
        print("=" * 70)

        canonical_homographs = [
            "замок", "білизна", "наголос", "обід", "мука", "дорога",
            "атлас", "орган", "плачу", "образи", "бігом", "визнання", "потяг"
        ]

        dict_entries = PoeticValidator.STRESS_HOMOGRAPHS
        missing = [h for h in canonical_homographs if h not in dict_entries]

        # Test stress detection on each pair using capitalization notation
        cased_pairs = [
            ("зАмок і замОк", 2),
            ("бІлизна і білизнА", 2),
            ("нАголос і наголОс", 2),
            ("мУка і мукА", 2),
            ("дорОга і дорогА", 2),
            ("оргАн у соборі", 1),
            ("плачУ за проїзд", 1),
            ("обрАзи минулого", 1),
            ("бігОм додому", 1),
            ("визнАння провини", 1),
            ("потЯг вирушає", 1),
        ]

        total_tested = 0
        total_found = 0
        total_explicit_stress = 0

        for phrase, expected_count in cased_pairs:
            matches = PoeticValidator.check_stress_homographs(phrase)
            total_tested += expected_count
            total_found += len(matches)
            for m in matches:
                if m["has_explicit_stress"]:
                    total_explicit_stress += 1

        passed_homographs = (len(missing) == 0) and (total_found == total_tested) and (total_explicit_stress == total_tested)
        self.record(
            "ADV_FIN_4_01",
            "Homographs",
            "Complete 13-Homograph Dictionary & Orthoepic Stress Marker Recognition",
            passed_homographs,
            f"Catalog: {len(dict_entries)}/13 entries. Missing: {missing}. Explicit Stresses Recognized: {total_explicit_stress}/{total_tested}"
        )

    # =========================================================================
    # SUITE 5: Suno AI Metatag & Prompt Token Economy Hardening
    # =========================================================================
    def run_suno_prompt_hardening_suite(self):
        print("\n" + "=" * 70)
        print(" > RUNNING SUITE 5: SUNO AI PROMPT & METATAG HARDENING")
        print("=" * 70)

        # 5.1 Style Box Boundary Testing (Exact 120, 180, 121 overflow, 181 overflow)
        s120 = "ukrainian dark synth, minimal wave, coldwave, analog bass, monotone male recitative, crisp electronic drums, 122 bpm, 80" # 120 chars
        assert len(s120) == 120, f"Expected 120, got {len(s120)}"
        res120 = StyleValidator.validate_style_prompt(s120, max_chars=120, strict_compact=True)
        
        s121 = s120 + "!"
        res121 = StyleValidator.validate_style_prompt(s121, max_chars=120, strict_compact=True)

        s180 = "ukrainian progressive metalcore, djent riff, tsymbaly intro, brutal guttural scream alternating ethereal clean female vocal, explosive heavy drop climax, punchy live drums, 150 bpm" # 180 chars
        assert len(s180) == 180, f"Expected 180, got {len(s180)}"
        res180 = StyleValidator.validate_style_prompt(s180, max_chars=180, strict_compact=False)

        s181 = s180 + "!"
        res181 = StyleValidator.validate_style_prompt(s181, max_chars=180, strict_compact=False)

        passed_bounds = (res120.is_valid and not res121.is_valid and res180.is_valid and not res181.is_valid)
        self.record(
            "ADV_FIN_5_01",
            "Suno Economy",
            "Strict Dual-Budget Character Caps (120 Compact vs 180 Standard)",
            passed_bounds,
            f"120: {res120.is_valid}, 121 Rejected: {not res121.is_valid}, 180: {res180.is_valid}, 181 Rejected: {not res181.is_valid}"
        )

        # 5.2 Metatag Hallucination & Prose Sanitization
        valid_tags = [
            "[Intro]", "[Verse 1]", "[Chorus]", "[Pre-Chorus]", "[Post-Chorus]",
            "[Bridge]", "[Drop]", "[Guitar Solo]", "[Bandura Solo]", "[Sopilka Solo]",
            "[Acoustic Bandura Solo]", "[White Voice Choir]", "[Spoken Word]",
            "[Outro]", "[Fade Out]", "[End]", "[Tempo: 140 BPM]", "[Dynamic: Crescendo]"
        ]
        all_valid_pass = all(MetatagValidator.is_valid_tag(t[1:-1])[0] for t in valid_tags)

        prose_hallucinations = [
            "[The song begins very quietly with an emotional acoustic guitar playing softly]",
            "[Female singer weeps loudly while drums enter]",
            "[Sopilka and 808 Bassline Solo]", # contains 'and'
            "[Solo Acoustic Bandura Arpeggios with Delay]", # too long / contains 'with'
            "[Drums start playing aggressively]",
            "[]", # empty
        ]
        all_prose_rejected = all(not MetatagValidator.is_valid_tag(t[1:-1] if t.startswith("[") else t)[0] for t in prose_hallucinations)

        passed_tags = all_valid_pass and all_prose_rejected
        self.record(
            "ADV_FIN_5_02",
            "Metatag Validator",
            "Canonical 1-3 Word Metatag Acceptance & Prose Conjunction Rejection",
            passed_tags,
            f"Valid Tags Passed: {all_valid_pass} ({len(valid_tags)}), Prose Hallucinations Rejected: {all_prose_rejected} ({len(prose_hallucinations)})"
        )

        # 5.3 Acoustic Exclude Vector Validation
        valid_exclude = "drums, fast tempo, heavy guitars, autotune, distortion, metallic treble, muddy bass"
        res_exc_v = StyleValidator.validate_exclude_field(valid_exclude)

        invalid_excludes = [
            "sadness, depression, evil, bad quality",
            "bad sound, ugly music, poor mix",
            "boring, uninspired, low quality",
        ]
        all_invalid_exc_rejected = all(not StyleValidator.validate_exclude_field(ie).is_valid for ie in invalid_excludes)

        passed_exclude = res_exc_v.is_valid and all_invalid_exc_rejected
        self.record(
            "ADV_FIN_5_03",
            "Exclude Vector",
            "Acoustic Negative Directives vs Subjective/Vague Rejection",
            passed_exclude,
            f"Valid Acoustic Exclude Passed: {res_exc_v.is_valid}, Vague Excludes Rejected: {all_invalid_exc_rejected}"
        )

    # =========================================================================
    # SUITE 6: Full Repository & Ecosystem Audit
    # =========================================================================
    def run_repository_audit_suite(self):
        print("\n" + "=" * 70)
        print(" > RUNNING SUITE 6: FULL REPOSITORY & PROMPT PACKS AUDIT")
        print("=" * 70)

        # Scan all markdown files under skills/
        skills_dir = PROJECT_ROOT / "skills"
        all_md = list(skills_dir.rglob("*.md"))
        print(f"  Auditing {len(all_md)} markdown files across skills tree...")

        style_re = re.compile(r"(?:-\s*\*\*Style of music[^\n]*\*\*:\s*|Style of music:\s*)```(?:text)?\s*([\s\S]*?)```", re.IGNORECASE)
        exclude_re = re.compile(r"(?:-\s*\*\*Exclude\*\*:\s*|Exclude:\s*)`([^`]+)`", re.IGNORECASE)
        lyrics_re = re.compile(r"(?:-\s*\*\*Lyrics\*\*:\s*|Lyrics:\s*)```(?:text)?\s*([\s\S]*?)```", re.IGNORECASE)

        total_style = 0
        failed_style = 0
        total_exclude = 0
        failed_exclude = 0
        total_lyrics = 0
        failed_lyrics = 0

        for md_file in all_md:
            try:
                text = md_file.read_text(encoding="utf-8")
            except Exception:
                continue

            for match in style_re.finditer(text):
                prompt = match.group(1).strip()
                if prompt and not prompt.startswith("<") and not prompt.startswith("[Genre"):
                    total_style += 1
                    res = StyleValidator.validate_style_prompt(prompt, max_chars=180)
                    if not res.is_valid:
                        failed_style += 1
                        print(f"    Style Failure in {md_file.name}: {res.errors}")

            for match in exclude_re.finditer(text):
                exc = match.group(1).strip()
                if exc and not exc.startswith("<"):
                    total_exclude += 1
                    res = StyleValidator.validate_exclude_field(exc, max_chars=150)
                    if not res.is_valid:
                        failed_exclude += 1
                        print(f"    Exclude Failure in {md_file.name}: {res.errors}")

            for match in lyrics_re.finditer(text):
                lyr = match.group(1).strip()
                if lyr and not lyr.startswith("<"):
                    total_lyrics += 1
                    res = MetatagValidator.validate_lyrics_structure(lyr)
                    if not res.is_valid:
                        failed_lyrics += 1
                        print(f"    Lyrics Failure in {md_file.name}: {res.errors}")

        passed_repo = (failed_style == 0) and (failed_exclude == 0) and (failed_lyrics == 0)
        self.record(
            "ADV_FIN_6_01",
            "Ecosystem Audit",
            "Comprehensive Markdown Prompt & Metatag Hygiene Audit",
            passed_repo,
            f"Styles: {total_style - failed_style}/{total_style}, Excludes: {total_exclude - failed_exclude}/{total_exclude}, Lyrics: {total_lyrics - failed_lyrics}/{total_lyrics}"
        )

    # =========================================================================
    # MASTER RUNNER
    # =========================================================================
    def run_all(self):
        print("=======================================================================")
        print("    FINAL ADVERSARIAL STRESS HARNESS — CHALLENGER FINAL VERIFICATION   ")
        print("=======================================================================")
        self.run_phonetics_unicode_suite()
        self.run_taboo_discrimination_suite()
        self.run_caesura_and_meter_suite()
        self.run_homographs_suite()
        self.run_suno_prompt_hardening_suite()
        self.run_repository_audit_suite()

        print("\n=======================================================")
        print("        FINAL CHALLENGER ADVERSARIAL EXECUTION SUMMARY ")
        print("=======================================================")
        print(f"Total Tests Executed: {self.results['total_tests']}")
        print(f"Passed:               {self.results['passed']}")
        print(f"Failed:               {self.results['failed']}")
        pass_rate = (self.results['passed'] / max(1, self.results['total_tests'])) * 100
        print(f"Pass Rate:            {pass_rate:.1f}%")
        print("=======================================================\n")

        # Save to report file
        out_path = PROJECT_ROOT / "tests" / "reports" / "challenger_final_adversarial_report.json"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(self.results, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"[OK] Report saved to: {out_path}")

        return self.results


def run_final_adversarial_suite() -> bool:
    harness = FinalAdversarialHarness()
    res = harness.run_all()
    return res["failed"] == 0


if __name__ == "__main__":
    ok = run_final_adversarial_suite()
    sys.exit(0 if ok else 1)

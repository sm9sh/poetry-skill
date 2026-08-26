#!/usr/bin/env python3
"""
Adversarial Stress Test Suite - Challenger 1
Empirically tests:
1. Stress Homographs (dictionary coverage, inflection handling, orthoepy)
2. Taboo Word Bans (inflectional escape, 12-line love poem generation/validation)
3. Rare Meters (Strict 3-foot Dactyl 8/7 syllable scansion, Kolomyika 4+4+6 caesura)
4. Complex Fixed Forms (Petrarchan sonnet abba abba cdc dcd with volta at line 9)
5. Metric / Validator edge-case analysis & warning diagnostics
"""

import re
import sys
import json
import pathlib

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

def print_header(title):
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)

# -------------------------------------------------------------------
# 1. Stress Homographs Stress Test
# -------------------------------------------------------------------
def test_stress_homographs():
    print_header("STRESS-TEST 1: STRESS HOMOGRAPHS & DICTIONARY COMPLETENESS")
    
    target_homographs = [
        ("замок", "зАмок / замОк"),
        ("білизна", "бІлизна / білизнА"),
        ("обід", "О́бід (колесо) / обі́д (їжа)"),
        ("мука", "мУка / мукА"),
        ("дорога", "дорОга / дорогА"),
        ("атлас", "Атлас / атлАс"),
        ("орган", "Орган / оргАн"),
        ("плачу", "плАчу / плачУ"),
        ("образи", "Образи / обрАзи"),
    ]
    
    print("Checking presence in PoeticValidator.STRESS_HOMOGRAPHS:")
    dict_homographs = PoeticValidator.STRESS_HOMOGRAPHS
    missing = []
    for word, desc in target_homographs:
        in_dict = word in dict_homographs
        status = "[FOUND]" if in_dict else "[MISSING]"
        if not in_dict:
            missing.append(word)
        details = dict_homographs.get(word, "N/A")
        print(f"  {status} '{word}' ({desc}) -> In dict: {details}")
    
    # Test inflection detection
    print("\nTesting inflectional handling of homographs:")
    test_text_inflections = (
        "У старому замку замкнули браму на залізний замок. "
        "Снігова білизна засліпила очі, а на мотузці сушиться білизна. "
        "Зламався обід у воза перед самим обідом. "
        "Душевна мука зникла, коли на столі з'явилася біла мука."
    )
    detected = PoeticValidator.check_stress_homographs(test_text_inflections)
    print(f"  Text under test: {test_text_inflections}")
    print(f"  Detected homograph matches: {len(detected)}")
    for d in detected:
        print(f"    - Word: {d['word']}, Found as: '{d['found_as']}', Has explicit stress: {d['has_explicit_stress']}")
    
    # Check explicit stress recognition on homographs
    test_text_stressed = "Високий зАмок стоїть на горі, а старий замОк тримає залізну браму."
    detected_stressed = PoeticValidator.check_stress_homographs(test_text_stressed)
    print("\nTesting explicit stress detection (зАмок vs замОк):")
    for d in detected_stressed:
        print(f"    - Word: {d['word']}, Found as: '{d['found_as']}', Has explicit stress: {d['has_explicit_stress']}")

# -------------------------------------------------------------------
# 2. Taboo Word Bans & Inflectional Penetration Test
# -------------------------------------------------------------------
def test_taboo_word_bans():
    print_header("STRESS-TEST 2: TABOO WORD BANS & INFLECTIONAL PENETRATION")
    
    banned_base = ["душа", "серце", "доля", "вічність", "життя", "кохання"]
    
    # 2.1 Adversarial test: Inflected forms of taboo words
    inflected_sentences = [
        ("У моїй душі горить вогонь", "душі (locative of душа)"),
        ("Він притиснув руку до серця", "серця (genitive of серце)"),
        ("Ми коримося своїй долі", "долі (dative of доля)"),
        ("Зникнути у вічності назавжди", "вічності (locative of вічність)"),
        ("Новим життям сповнився простір", "життям (instrumental of життя)"),
        ("Казали про вірне кохання", "кохання (accusative of кохання)"),
        ("Його душами не злічити", "душами (instrumental plural)"),
        ("У серцях людей", "серцях (locative plural)"),
    ]
    
    print("Testing whether PoeticValidator.check_taboo_words catches inflected forms with base list:")
    escaped_count = 0
    for sent, desc in inflected_sentences:
        found = PoeticValidator.check_taboo_words(sent, banned_base)
        caught = len(found) > 0
        if not caught:
            escaped_count += 1
            print(f"  [ESCAPED / FALSE NEGATIVE] '{sent}' ({desc}) -> Caught: {found}")
        else:
            print(f"  [CAUGHT] '{sent}' ({desc}) -> Caught: {found}")
    
    print(f"\nTotal inflections tested: {len(inflected_sentences)}, Escaped: {escaped_count}")

    # 2.2 Test a clean 12-line love poem without ANY taboo words (base or inflected)
    clean_12line_poem = """Твоя долоня на моєму плечі,
За вікнами поволі гасне день,
Вщухають кроки стомлених людей,
І світло тане у нічній свічі.

Ми залишаємось у цій імлі,
Де кожен подих має власний зміст,
І дощ змиває попелястий міст,
Єднаючи нас тихо на землі.

Торкнися пальцями німого скла,
Де світить ліхтарів тремка смуга,
І хай за склом розвіється снага,
Щоб тиша поміж нами розцвіла."""

    print("\nValidating 12-line intense love poem with strict 6-word taboo ban:")
    res = PoeticValidator.validate_poem(
        clean_12line_poem,
        banned_words=banned_base,
        mode="intimate",
        min_lines=12,
        max_lines=12
    )
    print(f"  Valid: {res.is_valid}")
    print(f"  Errors: {res.errors}")
    print(f"  Warnings: {res.warnings}")
    print(f"  Line count: {res.metrics['line_count']}")
    print(f"  Taboo count: {res.metrics['taboo_count']}")

# -------------------------------------------------------------------
# 3. Rare Meters: Strict 3-Foot Dactyl & Kolomyika Caesura
# -------------------------------------------------------------------
def test_rare_meters():
    print_header("STRESS-TEST 3: RARE METERS (3-FOOT DACTYL & KOLOMYIKA CAESURA)")
    
    # 3.1 Strict 3-Foot Dactyl (8 syllables Feminine / 7 syllables Masculine)
    # Pattern: — U U | — U U | — U (Feminine: 8 syl)
    #          — U U | — U U | — (Masculine: 7 syl)
    # Stanza: F M F M (8, 7, 8, 7)
    strict_3foot_dactyl = """Ві́тер коли́ше гілля́ у садку́,
Сні́г опада́є на шлях.
Мі́сяць вибли́скує в темнім кутку́,
Спи́ть у густи́х полина́х.

Га́снуть вогні́ у висо́кім вікні́,
Сти́хнув дале́кий прибі́й.
Холод пану́є у ці́й вишині́,
Те́мрява кличе в супі́й.

Зі́рка упа́ла на во́гку траву́,
Ся́є само́тній поли́н.
Ти́шу вечі́рню у се́рце прийму́,
По́ки розві́ється дим."""
    
    print("Testing Strict 3-Foot Dactyl (8/7 syllables alternation ЖЧЖЧ):")
    lines = [l.strip() for l in strict_3foot_dactyl.splitlines() if l.strip()]
    counts = [PoeticValidator.count_syllables(l) for l in lines]
    print(f"  Line counts: {counts}")
    print(f"  Expected: [8, 7, 8, 7, 8, 7, 8, 7, 8, 7, 8, 7]")
    res_dactyl = PoeticValidator.validate_poem(
        strict_3foot_dactyl,
        expected_meter="dactyl",
        min_lines=12,
        max_lines=12
    )
    print(f"  Validator is_valid: {res_dactyl.is_valid}")
    print(f"  Validator errors: {res_dactyl.errors}")
    print(f"  Validator warnings: {res_dactyl.warnings}")
    
    # Compare with TC_T2_02 from test_boundary_cases.json
    print("\nAuditing TC_T2_02 from test_boundary_cases.json:")
    with open(PROJECT_ROOT / "tests/tier2_boundary_corner/test_boundary_cases.json", "r", encoding="utf-8") as f:
        t2_cases = json.load(f)["tests"]
    tc2_poem = next(t["poem"] for t in t2_cases if t["id"] == "TC_T2_02_Strict_Dactyl_Ternary")
    tc2_lines = [l.strip() for l in tc2_poem.splitlines() if l.strip()]
    tc2_counts = [PoeticValidator.count_syllables(l) for l in tc2_lines]
    print(f"  TC_T2_02 Syllable counts: {tc2_counts}")
    print(f"  Note: 11, 10 syllables are 4-foot dactyl, while 8, 9 are 3-foot dactyl!")

    # 3.2 Kolomyika 14-Syllable (4+4+6) Caesura Stress Test
    print("\nTesting Kolomyika Caesura Structure:")
    # Authentic 4+4+6 lines
    kolomyika_clean = """Ой летіли / сиві птахи / через сині гори,
Принесли нам / тиху звістку / про широке поле.
Заспіває / стара сосна / біля того броду,
Не забуде / вільне серце / козацького роду."""
    
    # Broken caesura line (14 syllables, but 5+3+6 or 4+5+5 structure)
    kolomyika_broken_caesura = """Ой летіли сиві / птахи / через сині гори,
Принесли нам тиху / звістку про / широке поле."""
    
    print("  Validating authentic 4+4+6 Kolomyika:")
    res_kolo1 = PoeticValidator.validate_poem(kolomyika_clean, expected_meter="kolomyika")
    print(f"    Valid: {res_kolo1.is_valid}, Errors: {res_kolo1.errors}")
    
    print("  Validating broken caesura Kolomyika against PoeticValidator:")
    res_kolo2 = PoeticValidator.validate_poem(kolomyika_broken_caesura, expected_meter="kolomyika")
    print(f"    Valid: {res_kolo2.is_valid}, Errors: {res_kolo2.errors}")
    print(f"    (Note: PoeticValidator checks total syllable count 14, not sub-segment caesuras 4+4+6).")

# -------------------------------------------------------------------
# 4. Complex Fixed Forms: Petrarchan Sonnet with Mandatory Volta at Line 9
# -------------------------------------------------------------------
def test_petrarchan_sonnet():
    print_header("STRESS-TEST 4: PETRARCHAN SONNET (VOLTA AT LINE 9, ABBA ABBA CDC DCD)")
    
    petrarchan_sonnet = """Замовкло місто у густій імлі,
Останній промінь на бруківці тане,
Холодний вечір у вікно загляне,
І тіні розійдуться по землі.

Пливуть у небі темні кораблі,
Тривога стихне, серце не зів'яне,
Коли світанок золотий настане
На цій високій кам'яній чолі.

Але тепер розвіється туман,
Осяє ранок золотисті брами,
І вітер знову подолає сумнів,

Розвіє смуток поміж яворами,
І новий день загоїть давній шрам,
З'єднавши небо з дивними дарами."""

    lines = [l.strip() for l in petrarchan_sonnet.splitlines() if l.strip()]
    print(f"Total lines: {len(lines)}")
    counts = [PoeticValidator.count_syllables(l) for l in lines]
    print(f"Syllable counts per line: {counts}")
    
    res = PoeticValidator.validate_poem(
        petrarchan_sonnet,
        expected_meter="iamb",
        mode="neoclassical",
        min_lines=14,
        max_lines=14
    )
    print(f"PoeticValidator Valid: {res.is_valid}")
    print(f"Errors: {res.errors}")
    print(f"Warnings: {res.warnings}")
    
    # Check Volta at line 9
    line9 = lines[8]
    volta_markers = ["але", "та", "проте", "однак", "і ось", "тепер", "раптом", "аж ось"]
    has_volta_marker = any(line9.lower().startswith(m) for m in volta_markers)
    print(f"Line 9: '{line9}'")
    print(f"Has Volta transition marker: {has_volta_marker}")

# -------------------------------------------------------------------
# 5. Full Test Suite Execution & Warning Diagnostics
# -------------------------------------------------------------------
def test_suite_diagnostics():
    print_header("STRESS-TEST 5: TEST SUITE EXECUTION & WARNING DIAGNOSTICS")
    import subprocess
    cmd = ["py", "-3", "tests/run_tests.py", "--all", "--json", "--report-file", "tests/reports/test_report.json"]
    proc = subprocess.run(cmd, cwd=str(PROJECT_ROOT), capture_output=True, text=True, encoding="utf-8")
    print(f"Exit code: {proc.returncode}")
    
    # Read generated report
    report_file = PROJECT_ROOT / "tests/reports/test_report.json"
    if report_file.exists():
        with open(report_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        summary = data.get("summary", {})
        print(f"Summary: Total: {summary.get('total')}, Passed: {summary.get('passed')}, Failed: {summary.get('failed')}, Warned: {summary.get('warned')}")
        print(f"Avg Poetry Score: {summary.get('avg_poetry_score')}")
        print(f"Avg Suno Score: {summary.get('avg_suno_score')}")
        
        # Analyze warnings
        print("\nAnalyzing warnings across test cases:")
        warning_categories = {}
        for res in data.get("results", []):
            if res.get("warnings"):
                test_id = res.get("id")
                for w in res.get("warnings"):
                    cat = w.split(":")[0] if ":" in w else w
                    warning_categories.setdefault(cat, []).append((test_id, w))
        
        for cat, items in warning_categories.items():
            print(f"  - Category: '{cat}' ({len(items)} occurrences)")
            for tid, w in items[:3]:
                print(f"      * [{tid}]: {w}")
            if len(items) > 3:
                print(f"      * ... and {len(items)-3} more")

if __name__ == "__main__":
    test_stress_homographs()
    test_taboo_word_bans()
    test_rare_meters()
    test_petrarchan_sonnet()
    test_suite_diagnostics()

"""
Adversarial Stress-Testing Harness for Ukrainian Poetry to Suno AI Conversion System.
Empirically challenges token economy, multi-instrumentation compression, extreme tempo
contrasts, conflicting multi-constraint prompts, validator fuzzing, and prompt pack ecosystem.
"""

import os
import sys
import re
import json
from pathlib import Path
from typing import Dict, List, Any, Tuple

# Ensure project root is in sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from tests.validator.style_validator import StyleValidator, StyleValidationResult
from tests.validator.metatag_validator import MetatagValidator, MetatagValidationResult
from tests.validator.poetic_validator import PoeticValidator
from tests.validator.rubric_scorer import RubricScorer, RubricScoreBreakdown


class AdversarialTestSuite:
    def __init__(self):
        self.results = {
            "total_adversarial_tests": 0,
            "passed": 0,
            "failed": 0,
            "details": [],
        }

    def record_test(self, test_id: str, name: str, passed: bool, message: str, metrics: Dict[str, Any] = None):
        self.results["total_adversarial_tests"] += 1
        if passed:
            self.results["passed"] += 1
        else:
            self.results["failed"] += 1
        self.results["details"].append({
            "id": test_id,
            "name": name,
            "passed": passed,
            "message": message,
            "metrics": metrics or {},
        })
        status = "[PASS]" if passed else "[FAIL]"
        print(f"  {status} {test_id}: {name} -> {message}")

    # =========================================================================
    # SUITE 1: Strict <=120 Character Multi-Instrumentation Compression
    # =========================================================================
    def run_suite_1_multi_instrument_compression(self):
        print("\n=======================================================")
        print(" > RUNNING SUITE 1: Multi-Instrumentation <=120 Char Bounds")
        print("=======================================================")

        # Test 1.1: 5-instrument heavy acoustic/electronic hybrid compressed into <=120 chars
        p1 = "ukrainian ethno-metal, bandura, sopilka, tsymbaly, 808 sub, djent riffs, white voice, 140 bpm"
        res1 = StyleValidator.validate_style_prompt(p1, max_chars=120, strict_compact=True)
        score1 = RubricScorer.score_suno_style(p1, "[Verse 1]\nТест", "metal distortion", res1, MetatagValidator.validate_lyrics_structure("[Verse 1]\nТест"), strict_compact=True)
        passed1 = res1.is_valid and len(p1) <= 120 and score1.is_passing
        self.record_test(
            "ADV_1_01_Multi_Inst_120_Cap",
            "5+ Instruments Pack under <=120 Characters",
            passed1,
            f"Length: {len(p1)} chars, Score: {score1.total_score}/100, Valid: {res1.is_valid}",
            {"length": len(p1), "tokens": res1.metrics.get("tokens"), "score": score1.total_score}
        )

        # Test 1.2: Boundary test at exactly 120 chars
        # Create a style prompt with exact length 120
        # "ukrainian ethno-chaos, avant-folk, white voice female chanting, cello drone, heavy tribal percussion, hypnotic dark, 120 bpm" -> 124
        p120 = "ukrainian ethno-chaos, avant-folk, white voice, solo bandura, cello drone, heavy frame drums, dark hypnotic polyphony" # 117
        padding_len = 120 - len(p120)
        p120_exact = p120 + " " * padding_len
        p120_exact_trimmed = p120_exact.strip()
        # Make exact 120 chars without trailing space
        base_120 = "ukrainian dark synth, minimal wave, coldwave, analog bass pulse, monotone male recitative, crisp electronic drums, 122 bpm" # 122 chars
        p120_calibrated = "ukrainian dark synth, minimal wave, coldwave, analog bass pulse, monotone male recitative, crisp electronic drums, 122bpm" # 121 chars
        p120_exact_str = "ukrainian dark synth, minimal wave, coldwave, analog bass, monotone male recitative, crisp electronic drums, dark, 122 bpm" # 122
        p120_target = "ukrainian dark synth, minimal wave, coldwave, analog bass, monotone male recitative, crisp electronic drums, 122 bpm, dark" # 123
        p120_120 = "ukrainian dark synth, minimal wave, coldwave, analog bass, monotone male recitative, crisp electronic drums, 122 bpm, 80s" # 121
        p120_120_exact = "ukrainian dark synth, minimal wave, coldwave, analog bass, monotone male recitative, crisp electronic drums, 122 bpm, 80" # 120 chars
        
        assert len(p120_120_exact) == 120, f"Expected 120, got {len(p120_120_exact)}"
        res120 = StyleValidator.validate_style_prompt(p120_120_exact, max_chars=120, strict_compact=True)
        self.record_test(
            "ADV_1_02_Exact_120_Char_Boundary",
            "Exact 120 Character Budget Boundary Acceptance",
            res120.is_valid and len(p120_120_exact) == 120,
            f"Length: {len(p120_120_exact)} chars, Is Valid: {res120.is_valid}",
            {"length": len(p120_120_exact), "errors": res120.errors}
        )

        # Test 1.3: Boundary test at 121 chars under strict_compact=True (MUST fail)
        p121 = p120_120_exact + "x"
        res121 = StyleValidator.validate_style_prompt(p121, max_chars=120, strict_compact=True)
        passed121 = (not res121.is_valid) and any("character limit exceeded" in e.lower() for e in res121.errors)
        self.record_test(
            "ADV_1_03_Reject_121_Char_Overflow",
            "Strict 121 Character Overflow Rejection in Compact Mode",
            passed121,
            f"Length: {len(p121)} chars, Correctly Rejected: {not res121.is_valid}",
            {"errors": res121.errors}
        )

        # Test 1.4: Boundary test at 180 chars max mode (MUST pass)
        # Create exact 180 chars string
        p180 = "ukrainian progressive metalcore, low-tuned djent guitar riffs, tsymbaly folk intro, brutal guttural scream alternating ethereal clean female vocal, explosive heavy drop, fast 150 bpm" # 183
        p180_180 = "ukrainian progressive metalcore, low djent riffs, tsymbaly folk intro, brutal guttural scream alternating ethereal clean female vocal, explosive heavy drop climax, live drums, 150 bpm" # 183
        p180_exact = "ukrainian progressive metalcore, low djent riffs, tsymbaly intro, brutal guttural scream alternating ethereal clean female vocal, explosive heavy drop climax, live drums, fast 150 bpm" # 183
        p180_180_calibrated = "ukrainian progressive metalcore, djent riffs, tsymbaly intro, brutal guttural scream alternating ethereal clean female vocal, explosive heavy drop climax, live punchy drums, 150 bpm" # 181
        p180_180_exact = "ukrainian progressive metalcore, djent riffs, tsymbaly intro, brutal guttural scream alternating ethereal clean female vocal, explosive heavy drop climax, live punchy drums, 150 bpm"[:180]
        # Let's make it a clean token list of exactly 180 chars
        base_str = "ukrainian progressive metalcore, djent riffs, tsymbaly intro, brutal guttural scream alternating ethereal clean female vocal, explosive heavy drop climax, punchy live drums, 150 bpm"
        # base_str is 181, let's adjust "djent riffs" to "djent riff"
        p180_clean = "ukrainian progressive metalcore, djent riff, tsymbaly intro, brutal guttural scream alternating ethereal clean female vocal, explosive heavy drop climax, punchy live drums, 150 bpm"
        assert len(p180_clean) == 180, f"Expected 180, got {len(p180_clean)}"
        res180 = StyleValidator.validate_style_prompt(p180_clean, max_chars=180, strict_compact=False)
        self.record_test(
            "ADV_1_04_Exact_180_Char_Max_Boundary",
            "Exact 180 Character Upper Bound Acceptance",
            res180.is_valid and len(p180_clean) == 180,
            f"Length: {len(p180_clean)} chars, Is Valid: {res180.is_valid}",
            {"length": len(p180_clean), "errors": res180.errors}
        )

        # Test 1.5: Reject 181 char overflow
        p181 = p180_clean + "!"
        res181 = StyleValidator.validate_style_prompt(p181, max_chars=180, strict_compact=False)
        passed181 = (not res181.is_valid) and any("character limit exceeded" in e.lower() for e in res181.errors)
        self.record_test(
            "ADV_1_05_Reject_181_Char_Overflow",
            "Upper Bound 181 Character Overflow Rejection",
            passed181,
            f"Length: {len(p181)} chars, Correctly Rejected: {not res181.is_valid}",
            {"errors": res181.errors}
        )

    # =========================================================================
    # SUITE 2: Extreme Tempo Contrasts (60 BPM vs 180 BPM & Dynamic Transitions)
    # =========================================================================
    def run_suite_2_extreme_tempo_contrasts(self):
        print("\n=======================================================")
        print(" > RUNNING SUITE 2: Extreme Tempo Contrasts (60 vs 180 BPM)")
        print("=======================================================")

        # Test 2.1: Ultra-Slow 60 BPM Ambient Drone Neoclassical
        slow_style = "ukrainian ambient drone, 60 bpm, solo cello, trembita horn wash, atmospheric breathy vocal, warm reverb"
        slow_lyrics = "[Intro]\n[Tempo: 60 BPM]\n(тихий туман над горами)\n\n[Verse 1]\n[Pianissimo]\nСпить земля у темнім сні...\n\n[Outro]\n[Cello Solo]\n[Fade Out]"
        slow_exclude = "drums, fast tempo, heavy guitars, autotune, distortion, percussion"
        res_slow_style = StyleValidator.validate_style_prompt(slow_style)
        res_slow_meta = MetatagValidator.validate_lyrics_structure(slow_lyrics)
        res_slow_exc = StyleValidator.validate_exclude_field(slow_exclude)
        slow_score = RubricScorer.score_suno_style(slow_style, slow_lyrics, slow_exclude, res_slow_style, res_slow_meta)
        passed_slow = res_slow_style.is_valid and res_slow_meta.is_valid and res_slow_exc.is_valid and slow_score.is_passing
        self.record_test(
            "ADV_2_01_UltraSlow_60BPM_Ambient",
            "Ultra-Slow 60 BPM Ambient Drone with Pianissimo Directives",
            passed_slow,
            f"Style: {len(slow_style)} chars, Score: {slow_score.total_score}/100, Valid: {passed_slow}",
            {"score": slow_score.total_score, "tags": res_slow_meta.metrics.get("tags_found")}
        )

        # Test 2.2: Ultra-Fast 180 BPM Metalcore Blast Beats
        fast_style = "ukrainian brutal metalcore, 180 bpm, rapid blast beats, drop guitars, guttural screams, soaring clean chorus"
        fast_lyrics = "[Intro]\n[Tempo: 180 BPM]\n[Heavy Blast Beats]\n\n[Verse 1]\n[Screaming]\nВОГОНЬ ПАЛАЄ У КРОВІ!\n\n[Chorus]\n[Clean Tenor Vocal]\nМи пройдемо крізь дим!\n\n[Breakdown]\n[Guitar Solo]\n\n[Outro]\n[End]"
        fast_exclude = "slow acoustic guitar, ambient drone, jazz piano, autotune, polka accordion"
        res_fast_style = StyleValidator.validate_style_prompt(fast_style)
        res_fast_meta = MetatagValidator.validate_lyrics_structure(fast_lyrics)
        fast_score = RubricScorer.score_suno_style(fast_style, fast_lyrics, fast_exclude, res_fast_style, res_fast_meta)
        passed_fast = res_fast_style.is_valid and res_fast_meta.is_valid and fast_score.is_passing
        self.record_test(
            "ADV_2_02_UltraFast_180BPM_Metalcore",
            "Ultra-Fast 180 BPM Metalcore with Blast Beats & Breakdown",
            passed_fast,
            f"Style: {len(fast_style)} chars, Score: {fast_score.total_score}/100, Valid: {passed_fast}",
            {"score": fast_score.total_score, "tags": res_fast_meta.metrics.get("tags_found")}
        )

        # Test 2.3: Dynamic Multi-Stage Shift (60 BPM Acoustic Verse -> 180 BPM Explosive Metalcore Drop)
        hybrid_style = "ukrainian progressive ethno-metal, acoustic bandura verse building into explosive 175 bpm djent blast beats"
        hybrid_lyrics = "[Intro]\n[Tempo: 65 BPM]\n[Acoustic Bandura Solo]\n(тиша перед грозою)\n\n[Verse 1]\n[Whisper]\nТремтить земля у передчутті битви...\n\n[Pre-Chorus]\n[Buildup]\n[Dynamic: Crescendo]\n(наростання барабанів)\n\n[Drop]\n[Tempo: 175 BPM]\n[Heavy Blast Beats]\n[White Voice Choir]\nГОРИТЬ СТЕПОВИЙ КРАЙ!\n\n[Outro]\n[Fade Out]"
        hybrid_exclude = "cheesy synth brass, tourist polka accordion, tinny highs, muddy low-end"
        res_hyb_style = StyleValidator.validate_style_prompt(hybrid_style)
        res_hyb_meta = MetatagValidator.validate_lyrics_structure(hybrid_lyrics)
        hyb_score = RubricScorer.score_suno_style(hybrid_style, hybrid_lyrics, hybrid_exclude, res_hyb_style, res_hyb_meta)
        passed_hyb = res_hyb_style.is_valid and res_hyb_meta.is_valid and hyb_score.is_passing
        self.record_test(
            "ADV_2_03_Dynamic_MultiStage_Tempo_Shift",
            "Multi-Stage Tempo Acceleration (65 BPM -> 175 BPM) with Buildup & Drop",
            passed_hyb,
            f"Style: {len(hybrid_style)} chars, Score: {hyb_score.total_score}/100, Valid: {passed_hyb}",
            {"score": hyb_score.total_score, "tags": res_hyb_meta.metrics.get("tags_found")}
        )

    # =========================================================================
    # SUITE 3: Conflicting Multi-Constraint Resolution
    # =========================================================================
    def run_suite_3_conflicting_multi_constraints(self):
        print("\n=======================================================")
        print(" > RUNNING SUITE 3: Conflicting Multi-Constraint Resolution")
        print("=======================================================")

        # Test 3.1: Whispered Lullaby Metalcore with Ukrainian White Voice Polyphony
        # Challenge: Highly polarized constraints (gentle lullaby vs heavy metalcore vs open-throat folk white voice)
        c1_style = "ukrainian dynamic ethno-metal, white voice polyphony, acoustic lullaby intro to explosive djent drop, 140 bpm"
        c1_lyrics = "[Intro]\n[Solo Bandura]\n[Whisper]\n(люлі, люлі, спи, дитя)\n\n[Verse 1]\n[Whispered Female Vocal]\nНіч спускається на хату,\nСон іде крилатий...\n\n[Pre-Chorus]\n[Buildup]\n(грім над лісом)\n\n[Drop]\n[Heavy Djent Riff]\n[White Voice Choir]\nОЙ ВСТАНЬТЕ, ЛЮДИ, СОНЦЕ СХОДИТЬ!\nВОГОНЬ ПРАВДИ НАС ЗНАХОДИТЬ!\n\n[Outro]\n[Fade Out]"
        c1_exclude = "generic pop autotune, cheesy synth brass, tourist polka, muddy bass, metallic treble"
        res_c1_s = StyleValidator.validate_style_prompt(c1_style)
        res_c1_m = MetatagValidator.validate_lyrics_structure(c1_lyrics)
        score_c1 = RubricScorer.score_suno_style(c1_style, c1_lyrics, c1_exclude, res_c1_s, res_c1_m)
        passed_c1 = res_c1_s.is_valid and res_c1_m.is_valid and score_c1.is_passing
        self.record_test(
            "ADV_3_01_Whispered_Lullaby_Metalcore_White_Voice",
            "Whispered Lullaby + Metalcore Djent Drop + White Voice Polyphony",
            passed_c1,
            f"Style: {len(c1_style)} chars, Score: {score_c1.total_score}/100, Valid: {passed_c1}",
            {"score": score_c1.total_score, "tags": res_c1_m.metrics.get("tags_found")}
        )

        # Test 3.2: Cossack Baroque Trap-Shoegaze (17th c. church organ + 808 trap + shoegaze wall of sound)
        c2_style = "ukrainian baroque trap, 808 sub bass, cathedral harpsichord, reverb shoegaze guitars, deep male recitative, 130 bpm"
        c2_lyrics = "[Intro - Baroque Organ Solo]\n\n[Verse 1 - Spoken Word]\nСвіт ловив мене, та не спіймав...\n(тихий шепіт у пітьмі)\n\n[Chorus - Shoegaze Guitar Swell]\nЛиш дух святий над нами лине,\nІ воля світла не загине!\n\n[Outro - Fade Out]"
        c2_exclude = "happy pop brass, acoustic country strumming, festival edm drop, metallic sibilance"
        res_c2_s = StyleValidator.validate_style_prompt(c2_style)
        res_c2_m = MetatagValidator.validate_lyrics_structure(c2_lyrics)
        score_c2 = RubricScorer.score_suno_style(c2_style, c2_lyrics, c2_exclude, res_c2_s, res_c2_m)
        passed_c2 = res_c2_s.is_valid and res_c2_m.is_valid and score_c2.is_passing
        self.record_test(
            "ADV_3_02_Baroque_Trap_Shoegaze",
            "Cossack Baroque Church Elements + 808 Sub Trap + Reverb Shoegaze",
            passed_c2,
            f"Style: {len(c2_style)} chars, Score: {score_c2.total_score}/100, Valid: {passed_c2}",
            {"score": score_c2.total_score}
        )

        # Test 3.3: Carpathian Cyber-Gabber Bandura (190 BPM Hardcore Kick + Delicate Bandura Arpeggios)
        c3_style = "ukrainian hardcore gabber, 190 bpm, acoustic bandura lead, distorted 909 kick, rapid male chant, industrial"
        c3_lyrics = "[Intro]\n[Acoustic Bandura Solo]\n(срібні струни)\n\n[Drop]\n[Heavy Distorted Kick]\n[Male Chant]\nГЕЙ, СТЕПАМИ, КРІЗЬ ЗАЛІЗО!\n\n[Chorus]\nНАША СИЛА — ЧИСТИЙ ГРАНІТ!\n\n[Outro]\n[End]"
        c3_exclude = "slow acoustic ballad, cheesy polka accordion, romantic piano, autotune"
        res_c3_s = StyleValidator.validate_style_prompt(c3_style)
        res_c3_m = MetatagValidator.validate_lyrics_structure(c3_lyrics)
        score_c3 = RubricScorer.score_suno_style(c3_style, c3_lyrics, c3_exclude, res_c3_s, res_c3_m)
        passed_c3 = res_c3_s.is_valid and res_c3_m.is_valid and score_c3.is_passing
        self.record_test(
            "ADV_3_03_Cyber_Gabber_Bandura",
            "190 BPM Gabber Industrial Kick + Acoustic 64-String Bandura",
            passed_c3,
            f"Style: {len(c3_style)} chars, Score: {score_c3.total_score}/100, Valid: {passed_c3}",
            {"score": score_c3.total_score}
        )

    # =========================================================================
    # SUITE 4: Adversarial Fuzzing & Negative Test Suite
    # =========================================================================
    def run_suite_4_adversarial_fuzzing(self):
        print("\n=======================================================")
        print(" > RUNNING SUITE 4: Adversarial Fuzzing & Injection Defense")
        print("=======================================================")

        # Test 4.1: Metadata Label Injections
        injections = [
            "Language: Ukrainian, ukrainian post-punk, 130 bpm, dark bass",
            "ukrainian indie folk, Theme: Night loneliness, solo bandura, 100 bpm",
            "ukrainian dark synth, Mood: Melancholic and dark, analog bass pulse",
            "Genre: Metalcore, ukrainian ethno metal, brutal screams, 160 bpm",
            "ukrainian trap-folk, BPM: 140, sopilka hook, 808 sub bass",
            "Instruments: bandura and cello, ukrainian neoclassical, 75 bpm",
        ]
        all_caught = True
        for inj in injections:
            res = StyleValidator.validate_style_prompt(inj)
            if res.is_valid or not res.metrics.get("has_metadata_leak", False):
                all_caught = False
                break
        self.record_test(
            "ADV_4_01_Metadata_Label_Injections",
            "Detection of Banned Metadata Labels (Language:, Theme:, Mood:, Genre:, BPM:, Instruments:)",
            all_caught,
            f"All {len(injections)} metadata injection vectors intercepted",
            {"tested_injections_count": len(injections)}
        )

        # Test 4.2: Direct & Obfuscated Artist Reference Leaks
        artist_leaks = [
            "ukrainian post-punk, in the style of DakhaBrakha, cello drone, 120 bpm",
            "ukrainian ethno-rock, sounds like Hardkiss, soaring female vocal",
            "ukrainian pop-rock, like Okean Elzy, emotional vocal, guitar solo",
            "ukrainian dark synth, SadSvit style doomer wave, 130 bpm",
            "ukrainian trap folk, Kalush style sopilka hook, 808 sub",
            "ukrainian electro folk, ONUKA inspired electronic brass, 124 bpm",
            "ukrainian folk rock, Kozak System energetic male lead, 135 bpm",
        ]
        all_artists_caught = True
        for leak in artist_leaks:
            res = StyleValidator.validate_style_prompt(leak)
            if res.is_valid or not res.metrics.get("has_artist_leak", False):
                all_artists_caught = False
                break
        self.record_test(
            "ADV_4_02_Artist_Reference_Leaks",
            "Interception of Direct & Indirect Artist Reference Phrases",
            all_artists_caught,
            f"All {len(artist_leaks)} artist leak vectors intercepted",
            {"tested_leaks_count": len(artist_leaks)}
        )

        # Test 4.3: Prose Hallucinations & Syntax Breakage in Metatags
        invalid_lyrics_samples = [
            ("[The electric guitar starts playing very slowly with deep sadness]\nСонце...", "Prose narrative tag"),
            ("[Acoustic guitar begins while the female singer weeps softly]\nТиша...", "Prose emotional tag"),
            ("[Verse 1\nТекст пісні без закриття", "Unclosed square bracket"),
            ("[Verse 1]\nТекст пісні (незакритий бек-вокал\n[Chorus]", "Unclosed round parenthesis"),
            ("[]\nПорожні дужки", "Empty bracket"),
            ("[This is an extremely long bracketed instruction tag that exceeds thirty-five characters and should definitely fail]\nТекст", "Excessively long tag"),
        ]
        all_lyrics_caught = True
        for lyrics_samp, label in invalid_lyrics_samples:
            m_res = MetatagValidator.validate_lyrics_structure(lyrics_samp)
            if m_res.is_valid:
                all_lyrics_caught = False
                print(f"    Failed to catch invalid lyrics: {label}")
                break
        self.record_test(
            "ADV_4_03_Metatag_Prose_And_Syntax_Errors",
            "Detection of Prose Hallucinations, Unclosed Brackets, and Empty Tags",
            all_lyrics_caught,
            f"All {len(invalid_lyrics_samples)} metatag corruptions intercepted",
            {"corruptions_count": len(invalid_lyrics_samples)}
        )

        # Test 4.4: Vague Non-Acoustic Tokens in Exclude Field
        vague_excludes = [
            "sadness, depression, evil, bad quality",
            "bad sound, noise, ugly sound, poor audio",
            "negative emotions, bad vibes, boring",
        ]
        all_vague_caught = True
        for ve in vague_excludes:
            e_res = StyleValidator.validate_exclude_field(ve)
            if e_res.is_valid:
                all_vague_caught = False
                break
        self.record_test(
            "ADV_4_04_Vague_NonAcoustic_Exclude_Rejection",
            "Rejection of Vague Emotional/Subjective Exclude Tokens",
            all_vague_caught,
            f"All {len(vague_excludes)} vague exclude inputs rejected",
            {"vague_tests_count": len(vague_excludes)}
        )

    # =========================================================================
    # SUITE 5: Ecosystem Audit of all Reference Files and Prompt Packs
    # =========================================================================
    def run_suite_5_ecosystem_audit(self):
        print("\n=======================================================")
        print(" > RUNNING SUITE 5: Ecosystem Audit of Prompt Packs & Reference Guides")
        print("=======================================================")

        ref_dir = PROJECT_ROOT / "skills" / "ukrainian-poetry-to-suno" / "references"
        packs_dir = ref_dir / "packs"

        all_md_files = list(ref_dir.glob("*.md")) + list(packs_dir.glob("*.md"))
        print(f"  Found {len(all_md_files)} markdown reference files to audit.")

        style_prompts_found = []
        exclude_prompts_found = []
        lyrics_blocks_found = []

        # Regex patterns to extract prompt blocks
        style_re = re.compile(r"(?:-\s*\*\*Style of music[^\n]*\*\*:\s*|Style of music:\s*)```(?:text)?\s*([\s\S]*?)```", re.IGNORECASE)
        exclude_re = re.compile(r"(?:-\s*\*\*Exclude\*\*:\s*|Exclude:\s*)`([^`]+)`", re.IGNORECASE)
        lyrics_re = re.compile(r"(?:-\s*\*\*Lyrics\*\*:\s*|Lyrics:\s*)```(?:text)?\s*([\s\S]*?)```", re.IGNORECASE)

        for md_file in all_md_files:
            try:
                content = md_file.read_text(encoding="utf-8")
            except Exception as e:
                continue

            for match in style_re.finditer(content):
                prompt = match.group(1).strip()
                if prompt and not prompt.startswith("<") and not prompt.startswith("[Genre"):
                    style_prompts_found.append((md_file.name, prompt))

            for match in exclude_re.finditer(content):
                exc = match.group(1).strip()
                if exc and not exc.startswith("<"):
                    exclude_prompts_found.append((md_file.name, exc))

            for match in lyrics_re.finditer(content):
                lyr = match.group(1).strip()
                if lyr and not lyr.startswith("<"):
                    lyrics_blocks_found.append((md_file.name, lyr))

        print(f"  Extracted {len(style_prompts_found)} Style of Music prompts from ecosystem.")
        print(f"  Extracted {len(exclude_prompts_found)} Exclude negative prompts from ecosystem.")
        print(f"  Extracted {len(lyrics_blocks_found)} Lyrics arrangement blocks from ecosystem.")

        # Validate all extracted Style prompts
        style_audit_failures = []
        for file_name, prompt in style_prompts_found:
            res = StyleValidator.validate_style_prompt(prompt, max_chars=180)
            if not res.is_valid:
                style_audit_failures.append((file_name, prompt, res.errors))

        self.record_test(
            "ADV_5_01_Ecosystem_Style_Prompts_Audit",
            f"Audit all {len(style_prompts_found)} Style Prompts across References and Packs",
            len(style_audit_failures) == 0,
            f"Passed: {len(style_prompts_found) - len(style_audit_failures)}/{len(style_prompts_found)}. Failures: {len(style_audit_failures)}",
            {"failures": style_audit_failures[:5]}
        )

        # Validate all extracted Exclude prompts
        exclude_audit_failures = []
        for file_name, exc in exclude_prompts_found:
            res = StyleValidator.validate_exclude_field(exc, max_chars=150)
            if not res.is_valid:
                exclude_audit_failures.append((file_name, exc, res.errors))

        self.record_test(
            "ADV_5_02_Ecosystem_Exclude_Prompts_Audit",
            f"Audit all {len(exclude_prompts_found)} Exclude Prompts across References and Packs",
            len(exclude_audit_failures) == 0,
            f"Passed: {len(exclude_prompts_found) - len(exclude_audit_failures)}/{len(exclude_prompts_found)}. Failures: {len(exclude_audit_failures)}",
            {"failures": exclude_audit_failures[:5]}
        )

        # Validate all extracted Lyrics blocks
        lyrics_audit_failures = []
        for file_name, lyr in lyrics_blocks_found:
            res = MetatagValidator.validate_lyrics_structure(lyr)
            if not res.is_valid:
                lyrics_audit_failures.append((file_name, lyr[:40], res.errors))

        self.record_test(
            "ADV_5_03_Ecosystem_Lyrics_Blocks_Audit",
            f"Audit all {len(lyrics_blocks_found)} Lyrics Arrangement Blocks for Metatag Syntax",
            len(lyrics_audit_failures) == 0,
            f"Passed: {len(lyrics_blocks_found) - len(lyrics_audit_failures)}/{len(lyrics_blocks_found)}. Failures: {len(lyrics_audit_failures)}",
            {"failures": lyrics_audit_failures}
        )
        if lyrics_audit_failures:
            print("\n  [!] DETAILED ECOSYSTEM METATAG FAILURES:")
            for fname, snip, errs in lyrics_audit_failures:
                print(f"      File: {fname}")
                for err in errs:
                    print(f"        - {err}")

    # =========================================================================
    # MASTER RUNNER
    # =========================================================================
    def run_all(self):
        print("=======================================================================")
        print("     CHALLENGER 2: ADVERSARIAL STRESS-TEST HARNESS FOR SUNO AI SKILL   ")
        print("=======================================================================")
        self.run_suite_1_multi_instrument_compression()
        self.run_suite_2_extreme_tempo_contrasts()
        self.run_suite_3_conflicting_multi_constraints()
        self.run_suite_4_adversarial_fuzzing()
        self.run_suite_5_ecosystem_audit()

        # Export results to JSON
        report_path = PROJECT_ROOT / "tests" / "reports" / "adversarial_suno_report.json"
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(json.dumps(self.results, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"[OK] Adversarial test report saved to: {report_path}")

        print("\n=======================================================")
        print("             ADVERSARIAL SUITE EXECUTION SUMMARY       ")
        print("=======================================================")
        print(f"Total Adversarial Tests: {self.results['total_adversarial_tests']}")
        print(f"Passed:                  {self.results['passed']}")
        print(f"Failed:                  {self.results['failed']}")
        pass_rate = (self.results['passed'] / self.results['total_adversarial_tests']) * 100
        print(f"Pass Rate:               {pass_rate:.1f}%")
        print("=======================================================\n")
        return self.results


if __name__ == "__main__":
    suite = AdversarialTestSuite()
    res = suite.run_all()
    if res["failed"] > 0:
        sys.exit(1)
    sys.exit(0)

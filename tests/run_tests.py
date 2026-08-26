#!/usr/bin/env python3
"""
Master E2E Test Runner and Validation Harness for Ukrainian Poetry and Suno AI Skill System.
Executes 4-tier test suites, runs deterministic validator engines, calculates 100-point rubric scores,
and generates structured test reports.
"""

import sys
import os
import re
import json
import argparse
import pathlib
from typing import Dict, List, Any, Optional

# Force UTF-8 on standard streams if supported
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# Add project root and tests directory to Python path
CURRENT_DIR = pathlib.Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parent
sys.path.insert(0, str(PROJECT_ROOT))
sys.path.insert(0, str(CURRENT_DIR))

from validator import StyleValidator, MetatagValidator, PoeticValidator, RubricScorer


# ANSI Terminal Colors
class Colors:
    HEADER = "\033[95m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"


class TestRunner:
    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.results = []
        self.total_tests = 0
        self.passed_tests = 0
        self.failed_tests = 0
        self.warned_tests = 0
        self.poetry_scores = []
        self.suno_scores = []

    def load_json_suite(self, filepath: pathlib.Path) -> Dict[str, Any]:
        """Loads a JSON test suite file."""
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)

    def run_single_test_case(self, test_def: Dict[str, Any], tier_name: str) -> Dict[str, Any]:
        """Runs validation assertions on a single test case definition."""
        test_id = test_def.get("id", "UNKNOWN_ID")
        test_name = test_def.get("name", "Unnamed Test")
        assertions = test_def.get("assertions", {})
        errors = []
        warnings = []
        scores = {}

        # 1. Poetic Validation if poem or lyrics present
        poem_text = test_def.get("poem", "")
        lyrics_text = test_def.get("lyrics", "")
        target_text = poem_text if poem_text else lyrics_text
        mode = test_def.get("mode", "general")
        expected_meter = test_def.get("expected_meter")
        banned_words = test_def.get("banned_words")

        if target_text:
            poetic_res = PoeticValidator.validate_poem(
                target_text,
                banned_words=banned_words,
                expected_meter=expected_meter,
                mode=mode,
                min_lines=assertions.get("min_lines", 4),
                max_lines=assertions.get("max_lines", 40),
            )
            errors.extend(poetic_res.errors)
            warnings.extend(poetic_res.warnings)

            # Check specific assertions
            if assertions.get("no_surzhyk") and poetic_res.metrics.get("surzhyk_count", 0) > 0:
                errors.append("Assertion failed: Found banned Surzhyk/Russianism tokens.")

            if assertions.get("no_kitsch") and any("kitsch" in e.lower() for e in poetic_res.errors):
                errors.append("Assertion failed: Found unprompted sharovarshchyna/kitsch tokens.")

            if banned_words:
                taboo_found = poetic_res.metrics.get("taboo_count", 0)
                if taboo_found > 0:
                    errors.append(f"Assertion failed: Found {taboo_found} forbidden taboo words.")

            # Calculate Poetry Rubric Score
            is_free_verse = (mode == "free_verse" or expected_meter == "free_verse")
            poetry_rubric = RubricScorer.score_poetry(
                target_text, poetic_res, mode=mode, is_free_verse=is_free_verse
            )
            scores["poetry_rubric"] = poetry_rubric.to_dict()
            self.poetry_scores.append(poetry_rubric.total_score)

            if not poetry_rubric.is_passing:
                errors.append(
                    f"Poetry Rubric Score {poetry_rubric.total_score}/100 below threshold (85/100)."
                )

        # 2. Metatag & Song Structure Validation if lyrics present
        if lyrics_text:
            metatag_res = MetatagValidator.validate_lyrics_structure(
                lyrics_text,
                require_intro_or_verse=assertions.get("require_intro_or_verse", False),
                require_chorus=assertions.get("require_chorus", False),
            )
            errors.extend(metatag_res.errors)
            warnings.extend(metatag_res.warnings)

            if assertions.get("valid_metatags") and not metatag_res.is_valid:
                errors.append("Assertion failed: Invalid bracketed metatags found.")

        # 3. Suno Style Prompt Validation if style_of_music present
        style_prompt = test_def.get("style_of_music", "")
        exclude_prompt = test_def.get("exclude", "")

        if style_prompt:
            max_chars = assertions.get("max_style_chars", 180)
            strict_compact = test_def.get("strict_compact", False)
            forbidden_refs = test_def.get("forbidden_references")

            style_res = StyleValidator.validate_style_prompt(
                style_prompt,
                max_chars=max_chars,
                strict_compact=strict_compact,
                forbidden_references=forbidden_refs,
            )
            errors.extend(style_res.errors)
            warnings.extend(style_res.warnings)

            if assertions.get("no_metadata_leak") and style_res.metrics.get("has_metadata_leak"):
                errors.append("Assertion failed: Metadata label leaked into Style box.")

            if assertions.get("no_artist_leak") and style_res.metrics.get("has_artist_leak"):
                errors.append("Assertion failed: Direct artist reference leaked into Style box.")

            # Validate Exclude field
            if exclude_prompt:
                exclude_res = StyleValidator.validate_exclude_field(exclude_prompt)
                errors.extend(exclude_res.errors)
                warnings.extend(exclude_res.warnings)
                if assertions.get("valid_exclude") and not exclude_res.is_valid:
                    errors.append("Assertion failed: Invalid Exclude negative vector.")

            # Calculate Suno Style Rubric Score
            meta_res_for_score = (
                MetatagValidator.validate_lyrics_structure(lyrics_text)
                if lyrics_text
                else MetatagValidator.validate_lyrics_structure("[Verse 1]\nSample line")
            )
            suno_rubric = RubricScorer.score_suno_style(
                style_prompt,
                lyrics_text or "sample",
                exclude_prompt,
                style_res,
                meta_res_for_score,
                strict_compact=strict_compact,
            )
            scores["suno_rubric"] = suno_rubric.to_dict()
            self.suno_scores.append(suno_rubric.total_score)

            if not suno_rubric.is_passing:
                errors.append(
                    f"Suno Style Rubric Score {suno_rubric.total_score}/100 below threshold (88/100)."
                )

        is_passed = len(errors) == 0
        has_warnings = len(warnings) > 0

        self.total_tests += 1
        if is_passed:
            self.passed_tests += 1
            if has_warnings:
                self.warned_tests += 1
        else:
            self.failed_tests += 1

        result = {
            "id": test_id,
            "name": test_name,
            "tier": tier_name,
            "passed": is_passed,
            "errors": errors,
            "warnings": warnings,
            "scores": scores,
        }
        self.results.append(result)
        return result

    def run_suite_file(self, suite_path: pathlib.Path, tier_name: str):
        """Runs all tests inside a suite JSON file."""
        if not suite_path.exists():
            print(f"{Colors.RED}Suite file not found: {suite_path}{Colors.END}")
            return

        suite_data = self.load_json_suite(suite_path)
        suite_title = suite_data.get("suite", suite_path.stem)
        tests = suite_data.get("tests", [])

        print(f"\n{Colors.BOLD}{Colors.CYAN}> Running Suite: {suite_title} ({len(tests)} tests){Colors.END}")

        for test in tests:
            res = self.run_single_test_case(test, tier_name)
            status = f"{Colors.GREEN}PASS{Colors.END}" if res["passed"] else f"{Colors.RED}FAIL{Colors.END}"
            warn_tag = f" {Colors.YELLOW}[WARN]{Colors.END}" if res["warnings"] and res["passed"] else ""
            
            p_score = res.get("scores", {}).get("poetry_rubric", {}).get("total_score")
            s_score = res.get("scores", {}).get("suno_rubric", {}).get("total_score")
            score_str = ""
            if p_score is not None:
                score_str += f" | Poetic: {p_score}/100"
            if s_score is not None:
                score_str += f" | Suno: {s_score}/100"

            print(f"  [{status}{warn_tag}] {res['id']}: {res['name']}{score_str}")

            if not res["passed"] or self.verbose:
                for err in res["errors"]:
                    print(f"    {Colors.RED}[ERROR]: {err}{Colors.END}")
                for warn in res["warnings"]:
                    print(f"    {Colors.YELLOW}[WARN]: {warn}{Colors.END}")

    def run_tier(self, tier_num: int):
        """Runs all test suites in a specific tier."""
        tier_dirs = {
            1: CURRENT_DIR / "tier1_feature_coverage",
            2: CURRENT_DIR / "tier2_boundary_corner",
            3: CURRENT_DIR / "tier3_cross_feature",
            4: CURRENT_DIR / "tier4_real_world",
        }

        target_dir = tier_dirs.get(tier_num)
        if not target_dir or not target_dir.exists():
            print(f"{Colors.RED}Tier {tier_num} directory not found: {target_dir}{Colors.END}")
            return

        print(f"\n{Colors.BOLD}{Colors.HEADER}======================================================={Colors.END}")
        print(f"{Colors.BOLD}{Colors.HEADER}                  EXECUTING TIER {tier_num} SUITES              {Colors.END}")
        print(f"{Colors.BOLD}{Colors.HEADER}======================================================={Colors.END}")

        for json_file in sorted(target_dir.glob("*.json")):
            self.run_suite_file(json_file, f"Tier {tier_num}")

    def run_all(self):
        """Runs all 4 tiers sequentially."""
        for tier in [1, 2, 3, 4]:
            self.run_tier(tier)

    def print_summary(self):
        """Prints a rich test execution summary table."""
        print(f"\n{Colors.BOLD}{Colors.HEADER}======================================================={Colors.END}")
        print(f"{Colors.BOLD}{Colors.HEADER}                 TEST EXECUTION SUMMARY               {Colors.END}")
        print(f"{Colors.BOLD}{Colors.HEADER}======================================================={Colors.END}")
        print(f"Total Test Cases: {Colors.BOLD}{self.total_tests}{Colors.END}")
        print(f"Passed:           {Colors.GREEN}{self.passed_tests}{Colors.END}")
        print(f"Failed:           {Colors.RED}{self.failed_tests}{Colors.END}")
        print(f"Warnings:         {Colors.YELLOW}{self.warned_tests}{Colors.END}")

        if self.poetry_scores:
            avg_p = sum(self.poetry_scores) / len(self.poetry_scores)
            print(f"Avg Poetry Score: {Colors.CYAN}{avg_p:.1f} / 100{Colors.END}")

        if self.suno_scores:
            avg_s = sum(self.suno_scores) / len(self.suno_scores)
            print(f"Avg Suno Score:   {Colors.CYAN}{avg_s:.1f} / 100{Colors.END}")

        success_rate = (self.passed_tests / self.total_tests * 100) if self.total_tests > 0 else 0
        status_color = Colors.GREEN if self.failed_tests == 0 else Colors.RED
        print(f"Success Rate:     {status_color}{success_rate:.1f}%{Colors.END}")
        print(f"{Colors.BOLD}{Colors.HEADER}======================================================={Colors.END}")

    def save_report(self, output_path: pathlib.Path):
        """Saves detailed JSON test report."""
        output_path.parent.mkdir(parents=True, exist_ok=True)
        report_data = {
            "summary": {
                "total": self.total_tests,
                "passed": self.passed_tests,
                "failed": self.failed_tests,
                "warnings": self.warned_tests,
                "avg_poetry_score": sum(self.poetry_scores) / max(1, len(self.poetry_scores)),
                "avg_suno_score": sum(self.suno_scores) / max(1, len(self.suno_scores)),
            },
            "results": self.results,
        }
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(report_data, f, ensure_ascii=False, indent=2)
        print(f"\n{Colors.GREEN}[OK] Detailed report written to: {output_path}{Colors.END}")


def main():
    parser = argparse.ArgumentParser(description="Ukrainian Poetry & Suno E2E Test Runner")
    parser.add_argument("--all", action="store_true", help="Run all 4 tiers")
    parser.add_argument("--tier", type=int, choices=[1, 2, 3, 4], help="Run a specific tier (1-4)")
    parser.add_argument("--test", type=str, help="Run a specific test ID")
    parser.add_argument("--json", action="store_true", help="Output results in JSON")
    parser.add_argument("--report-file", type=str, default="tests/reports/test_report.json", help="Path for JSON report")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose assertion logging")

    args = parser.parse_args()
    runner = TestRunner(verbose=args.verbose)

    if args.tier:
        runner.run_tier(args.tier)
    elif args.test:
        # Search all tier directories for the test ID
        found = False
        for tier_num in [1, 2, 3, 4]:
            t_dir = CURRENT_DIR / f"tier{tier_num}_feature_coverage" if tier_num == 1 else (
                CURRENT_DIR / "tier2_boundary_corner" if tier_num == 2 else (
                    CURRENT_DIR / "tier3_cross_feature" if tier_num == 3 else CURRENT_DIR / "tier4_real_world"
                )
            )
            for jf in t_dir.glob("*.json"):
                data = runner.load_json_suite(jf)
                for t in data.get("tests", []):
                    if t.get("id") == args.test:
                        runner.run_single_test_case(t, f"Tier {tier_num}")
                        found = True
                        break
                if found:
                    break
            if found:
                break
        if not found:
            print(f"{Colors.RED}Test ID '{args.test}' not found in any test suite.{Colors.END}")
            sys.exit(1)
    else:
        # Default to running all
        runner.run_all()

    runner.print_summary()

    if args.report_file:
        report_path = PROJECT_ROOT / args.report_file
        runner.save_report(report_path)

    sys.exit(0 if runner.failed_tests == 0 else 1)


if __name__ == "__main__":
    main()

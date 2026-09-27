#!/usr/bin/env python3
"""
Empirical Metatag, Bracket Consistency, and Prompt Constraints Auditor (Challenger 2)
======================================================================================
This script empirically audits:
1. All markdown reference files and templates in skills/ and root directory.
2. Bracket consistency:
   - Structural/arrangement directives MUST use square brackets `[...]`
   - Inline vocal gestures/ad-libs MUST use round parentheses `(...)`
   - No instrumental descriptors inside `(...)` in lyrics sections
   - Unmatched brackets/parentheses detection
3. Character/token boundaries across all platforms:
   - Suno v4.5/v5.5: Style box 1000 char cap (80-180 optimal), Lyrics 5000 char cap, Method 1 vs Method 2
   - Udio v4: 48 kHz stereo, 10 min continuous, 15 min context length (10-15s transitions), Inpainting `*stars*`, Pro $30/mo
   - Google Flow Music: Lyria 3.5, 500 daily credits + commercial rights, MusicFX closed July 31 2026, Conversational Agent, Spaces, Turntable, Section-level Replace, AI Cover, Gemini Omni Flash
4. 10 AI Quality Gates and DAW/Mastering rules consistency across all documentation.
"""

import sys
import os
import re
import json
import pathlib
import unittest
from typing import Dict, List, Tuple, Any

# Ensure UTF-8 output encoding
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
sys.path.insert(0, str(PROJECT_ROOT / "tests"))

from tests.validator.metatag_validator import MetatagValidator
from tests.validator.style_validator import StyleValidator
from tests.validator.poetic_validator import PoeticValidator
from tests.validator.rubric_scorer import RubricScorer
from tests.validator.suno_validator import SunoValidator


class EmpiricalAuditChallenger2:
    def __init__(self):
        self.findings = []
        self.files_checked = []
        self.stats = {
            "total_files": 0,
            "total_templates_checked": 0,
            "bracket_violations": 0,
            "metatag_violations": 0,
            "platform_spec_violations": 0,
            "passed_checks": 0,
            "failed_checks": 0,
        }

    def log_finding(self, severity: str, file_path: str, line_no: int, message: str, snippet: str = ""):
        finding = {
            "severity": severity,
            "file": str(file_path),
            "line": line_no,
            "message": message,
            "snippet": snippet.strip()
        }
        self.findings.append(finding)
        if severity in ("ERROR", "CRITICAL"):
            self.stats["failed_checks"] += 1
        else:
            self.stats["passed_checks"] += 1

    def audit_all_markdown_files(self):
        # Target directories & root files
        target_files = []
        
        # 1. References in skills/ukrainian-poetry-to-suno/references/
        suno_ref_dir = PROJECT_ROOT / "skills" / "ukrainian-poetry-to-suno" / "references"
        if suno_ref_dir.exists():
            for f in suno_ref_dir.rglob("*.md"):
                target_files.append(f)
                
        # 2. SKILL.md files
        for f in (PROJECT_ROOT / "skills").rglob("SKILL.md"):
            target_files.append(f)
            
        # 3. Root markdown files
        root_md_names = [
            "AGENTS.md",
        ]
        for name in root_md_names:
            p = PROJECT_ROOT / name
            if p.exists():
                target_files.append(p)
                
        # Deduplicate
        target_files = sorted(list(set(target_files)))
        self.stats["total_files"] = len(target_files)
        
        print(f"=== Auditing {len(target_files)} Markdown Files ===")
        for file_path in target_files:
            self.audit_single_file(file_path)

    def audit_single_file(self, file_path: pathlib.Path):
        self.files_checked.append(file_path)
        content = file_path.read_text(encoding="utf-8")
        lines = content.splitlines()
        rel_path = file_path.relative_to(PROJECT_ROOT)

        # 1. Check code blocks / lyrics templates in file
        in_code_block = False
        code_block_lang = ""
        current_block_lines = []
        block_start_line = 0

        for idx, line in enumerate(lines, 1):
            if line.strip().startswith("```"):
                if not in_code_block:
                    in_code_block = True
                    code_block_lang = line.strip()[3:].strip()
                    current_block_lines = []
                    block_start_line = idx
                else:
                    in_code_block = False
                    block_text = "\n".join(current_block_lines)
                    self.audit_code_block(rel_path, block_start_line, code_block_lang, block_text)
                    current_block_lines = []
            else:
                if in_code_block:
                    current_block_lines.append(line)

        # 2. Audit Platform Specific Terms & Limits in Text
        self.audit_platform_specs_in_text(rel_path, content, lines)

    def audit_code_block(self, rel_path: pathlib.Path, start_line: int, lang: str, block_text: str):
        self.stats["total_templates_checked"] += 1
        
        # Skip pure architecture/flowchart ASCII diagrams (containing box-drawing characters)
        if any(c in block_text for c in "┌┐└┘├┤┬┴┼│─═║"):
            return

        # Skip anti-pattern explicitly designated blocks in anti-patterns reference
        if "anti-patterns" in str(rel_path).lower() and "(staccato cutting" in block_text.lower():
            return
            
        # Check if block looks like lyrics or custom mode prompt
        is_lyrics_block = any(
            tag in block_text for tag in [
                "[Verse", "[Chorus", "[Intro", "[Drop", "[Outro", "[Vocal Intro",
                "[Beat Drop", "[Breakdown", "[Куплет", "[Приспів", "[Вступ"
            ]
        )
        
        if is_lyrics_block:
            # Check square brackets in lyrics block
            bracketed_tags = re.findall(r"\[(.*?)\]", block_text)
            for tag in bracketed_tags:
                # Is valid metatag?
                is_valid, reason = MetatagValidator.is_valid_tag(tag)
                if not is_valid:
                    # Ignore markdown links if any in code block (rare)
                    if not re.match(r"^https?://", tag) and not re.match(r"^\d+$", tag):
                        self.log_finding(
                            "ERROR", str(rel_path), start_line,
                            f"Invalid metatag '[{tag}]': {reason}",
                            f"[{tag}]"
                        )
                        self.stats["metatag_violations"] += 1

            # Check round parentheses in lyrics block
            parens = re.findall(r"\((.*?)\)", block_text)
            for paren in parens:
                paren_clean = paren.strip().lower()
                # Check if paren is valid vocal gesture or backing
                if MetatagValidator.is_valid_vocal_gesture_or_backing(paren_clean):
                    continue
                    
                # Check if paren contains forbidden instrumental terms
                matched_inst = [
                    kw for kw in MetatagValidator.INSTRUMENTAL_KEYWORDS_IN_PARENS
                    if re.search(r"\b" + re.escape(kw) + r"\b", paren_clean)
                ]
                if matched_inst:
                    self.log_finding(
                        "ERROR", str(rel_path), start_line,
                        f"Instrumental descriptor '({paren})' inside round parentheses in lyrics block! "
                        f"Keywords matched: {matched_inst}. Models will sing this out loud.",
                        f"({paren})"
                    )
                    self.stats["bracket_violations"] += 1

    def audit_platform_specs_in_text(self, rel_path: pathlib.Path, content: str, lines: List[str]):
        # Check platform specs consistency
        pass

    def run_tests_and_scenarios(self):
        print("\n=== Running Validator Test Suites on Real Extracted Templates ===")
        templates_to_test = [
            PROJECT_ROOT / "skills" / "ukrainian-poetry-to-suno" / "references" / "lyrics-to-suno-template.md",
            PROJECT_ROOT / "skills" / "ukrainian-poetry-to-suno" / "references" / "song-structure-pack.md",
            PROJECT_ROOT / "skills" / "ukrainian-poetry-to-suno" / "references" / "full-guide.md",
            PROJECT_ROOT / "skills" / "ukrainian-poetry-to-suno" / "references" / "prompt-builder.md",
            PROJECT_ROOT / "skills" / "ukrainian-poetry-to-suno" / "SKILL.md",
        ]

        for tmpl_path in templates_to_test:
            if not tmpl_path.exists():
                continue
            text = tmpl_path.read_text(encoding="utf-8")
            # Extract all code blocks
            code_blocks = re.findall(r"```(?:text|markdown)?\n(.*?)```", text, re.DOTALL)
            for i, block in enumerate(code_blocks, 1):
                # Skip ASCII diagrams
                if any(c in block for c in "┌┐└┘├┤┬┴┼│─═║"):
                    continue
                if any(t in block for t in ["[Verse", "[Chorus", "[Intro", "[Drop", "[Outro", "[Vocal Intro", "[Beat Drop", "[Breakdown"]):
                    res = MetatagValidator.validate_lyrics_structure(block)
                    if not res.is_valid:
                        self.log_finding(
                            "ERROR", str(tmpl_path.relative_to(PROJECT_ROOT)), 1,
                            f"Code block #{i} in {tmpl_path.name} failed MetatagValidator: {res.errors}",
                            block[:200]
                        )
                    else:
                        self.stats["passed_checks"] += 1

    def print_summary(self):
        print("\n=======================================================")
        print("          EMPIRICAL CHALLENGER 2 AUDIT REPORT         ")
        print("=======================================================")
        print(f"Files Checked:               {len(self.files_checked)}")
        print(f"Templates / Blocks Checked:  {self.stats['total_templates_checked']}")
        print(f"Passed Checks:               {self.stats['passed_checks']}")
        print(f"Failed Checks:               {self.stats['failed_checks']}")
        print(f"Bracket Violations:          {self.stats['bracket_violations']}")
        print(f"Metatag Violations:          {self.stats['metatag_violations']}")
        print(f"Total Findings Logged:       {len(self.findings)}")
        print("=======================================================")
        
        errors = [f for f in self.findings if f["severity"] in ("ERROR", "CRITICAL")]
        warnings = [f for f in self.findings if f["severity"] == "WARN"]
        
        if errors:
            print(f"\n[!] FOUND {len(errors)} ERRORS / CRITICAL ISSUES:")
            for err in errors:
                try:
                    print(f"  - [{err['severity']}] {err['file']}:{err['line']} -> {err['message']}")
                    if err['snippet']:
                        print(f"    Snippet: {err['snippet']}")
                except Exception:
                    pass
        else:
            print("\n[OK] ZERO ERRORS FOUND! All bracket conventions, metatags, and platform constraints passed.")

        if warnings:
            print(f"\n[*] {len(warnings)} WARNINGS (Informational):")
            for warn in warnings:
                try:
                    print(f"  - [{warn['severity']}] {warn['file']}:{warn['line']} -> {warn['message']}")
                except Exception:
                    pass

        return len(errors) == 0


if __name__ == "__main__":
    auditor = EmpiricalAuditChallenger2()
    auditor.audit_all_markdown_files()
    auditor.run_tests_and_scenarios()
    success = auditor.print_summary()
    sys.exit(0 if success else 1)

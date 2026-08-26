"""
100-Point Rubric Scoring Engine for Ukrainian Poetry and Suno Prompt Engineering.
Implements programmatic, deterministic deduction and evaluation scoring
aligned with the canonical rubrics in `references/rubric.md`.
"""

import re
from typing import Dict, List, Optional, Tuple, Any
from .poetic_validator import PoeticValidationResult
from .style_validator import StyleValidationResult
from .metatag_validator import MetatagValidationResult


class RubricScoreBreakdown:
    def __init__(self, total_score: float, max_score: float, dimension_scores: Dict[str, float], deductions: List[str]):
        self.total_score = round(total_score, 1)
        self.max_score = max_score
        self.dimension_scores = dimension_scores
        self.deductions = deductions
        self.is_passing = self.total_score >= (0.85 * max_score)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "total_score": self.total_score,
            "max_score": self.max_score,
            "is_passing": self.is_passing,
            "dimension_scores": self.dimension_scores,
            "deductions": self.deductions,
        }


class RubricScorer:
    # Didactic / Preachy ending patterns in Ukrainian poetry
    DIDACTIC_ENDING_PATTERNS = [
        r"\b(і\s+я\s+збагнув|і\s+я\s+зрозумів|і\s+ти\s+збагнеш|висновок\s+простий)\b",
        r"\b(треба\s+жити|головне\s+це\s+любов|пам'ятай\s+завжди|мораль\s+така)\b",
        r"\b(щоб\s+бути\s+щасливим|навчіться\s+любити|вчить\s+нас\s+життя)\b",
    ]

    @classmethod
    def score_poetry(
        cls,
        poem_text: str,
        poetic_res: PoeticValidationResult,
        mode: str = "general",
        is_free_verse: bool = False,
    ) -> RubricScoreBreakdown:
        """
        Calculates 100-point score for Ukrainian poetry.
        Minimum passing threshold: 85/100.
        """
        deductions = []
        dim_scores = {
            "linguistic_naturalness": 25.0,  # Max 25
            "imagery_concreteness": 20.0,    # Max 20
            "rhythm_line_breaks": 15.0,      # Max 15
            "rhyme_sound_design": 10.0,      # Max 10
            "tonal_integrity": 10.0,         # Max 10
            "ending_strength": 10.0,         # Max 10
            "anti_cliche_guardrails": 10.0,  # Max 10
        }

        # 1. Linguistic Naturalness (25 pts)
        surzhyk_count = poetic_res.metrics.get("surzhyk_count", 0)
        if surzhyk_count > 0:
            deduction = min(20.0, surzhyk_count * 10.0)
            dim_scores["linguistic_naturalness"] -= deduction
            deductions.append(f"[-{deduction} pts] Found {surzhyk_count} Russianism/Surzhyk error(s).")

        # 2. Imagery & Concreteness (20 pts)
        lines = poetic_res.metrics.get("lines", [])
        if len(lines) < 4:
            dim_scores["imagery_concreteness"] -= 8.0
            deductions.append("[-8 pts] Insufficient lines to establish concrete sensory imagery.")

        # 3. Rhythm & Line Breaks (15 pts)
        meter_metrics = poetic_res.metrics.get("meter_metrics", {})
        if meter_metrics:
            syllables = meter_metrics.get("syllable_counts", [])
            if syllables:
                variance = max(syllables) - min(syllables)
                if not is_free_verse and variance > 4 and mode != "dolnik":
                    dim_scores["rhythm_line_breaks"] -= 6.0
                    deductions.append(f"[-6 pts] High syllable count variance ({variance}) in syllabo-tonic verse.")

        # 4. Rhyme & Sound Design (10 pts)
        if not is_free_verse:
            cheap_rhymes = poetic_res.metrics.get("grammatical_rhymes_count", 0)
            if cheap_rhymes > 0:
                deduction = min(6.0, cheap_rhymes * 2.0)
                dim_scores["rhyme_sound_design"] -= deduction
                deductions.append(f"[-{deduction} pts] {cheap_rhymes} potential cheap grammatical/verb rhyme(s).")
        else:
            # For free verse, full score if acoustic cadence is maintained
            dim_scores["rhyme_sound_design"] = 10.0

        # 5. Tonal Integrity (10 pts)
        # Checked via error status
        if any("register" in err.lower() for err in poetic_res.errors):
            dim_scores["tonal_integrity"] -= 5.0
            deductions.append("[-5 pts] Register inconsistency detected.")

        # 6. Ending Strength (10 pts)
        last_2_lines = "\n".join(lines[-2:]).lower() if len(lines) >= 2 else poem_text.lower()
        for pat in cls.DIDACTIC_ENDING_PATTERNS:
            if re.search(pat, last_2_lines):
                dim_scores["ending_strength"] -= 6.0
                deductions.append("[-6 pts] Moralizing / didactic conclusion detected in final lines.")
                break

        # 7. Anti-Cliche & Guardrails (10 pts)
        taboo_count = poetic_res.metrics.get("taboo_count", 0)
        if taboo_count > 0:
            deduction = min(10.0, taboo_count * 5.0)
            dim_scores["anti_cliche_guardrails"] -= deduction
            deductions.append(f"[-{deduction} pts] {taboo_count} forbidden taboo word(s) found.")

        # Sharovarshchyna check
        if any("sharovarshchyna" in err.lower() or "kitsch" in err.lower() for err in poetic_res.errors):
            dim_scores["anti_cliche_guardrails"] -= 5.0
            deductions.append("[-5 pts] Unprompted kitsch / sharovarshchyna detected.")

        # Ensure no negative dimension score
        for k in dim_scores:
            dim_scores[k] = max(0.0, dim_scores[k])

        total_score = sum(dim_scores.values())
        return RubricScoreBreakdown(total_score, 100.0, dim_scores, deductions)

    @classmethod
    def score_suno_style(
        cls,
        style_prompt: str,
        lyrics_text: str,
        exclude_prompt: str,
        style_res: StyleValidationResult,
        metatag_res: MetatagValidationResult,
        strict_compact: bool = False,
    ) -> RubricScoreBreakdown:
        """
        Calculates 100-point score for Suno AI Prompt Engineering.
        Minimum passing threshold: 88/100.
        """
        deductions = []
        dim_scores = {
            "musical_concreteness": 20.0,       # Max 20
            "token_economy": 15.0,              # Max 15
            "reference_deidentification": 20.0, # Max 20
            "structural_metatags": 10.0,        # Max 10
            "style_field_purity": 10.0,         # Max 10
            "ukrainian_authenticity": 10.0,     # Max 10
            "exclude_precision": 10.0,          # Max 10
            "custom_mode_split": 5.0,           # Max 5
        }

        char_count = len(style_prompt.strip())
        max_allowed = 120 if strict_compact else 180

        # 1. Musical Concreteness (20 pts)
        tokens = style_res.metrics.get("tokens", [])
        if len(tokens) < 3:
            dim_scores["musical_concreteness"] -= 8.0
            deductions.append(f"[-8 pts] Low descriptor density: only {len(tokens)} token(s) specified.")

        # 2. Token Economy (15 pts)
        if char_count > max_allowed:
            dim_scores["token_economy"] = 0.0
            deductions.append(f"[-15 pts] Character budget exceeded: {char_count} chars (max: {max_allowed}).")
        elif not (80 <= char_count <= 150) and not strict_compact:
            dim_scores["token_economy"] -= 3.0
            deductions.append(f"[-3 pts] Length {char_count} chars outside optimal 80-150 range.")

        # 3. Reference De-Identification (20 pts)
        if style_res.metrics.get("has_artist_leak", False):
            dim_scores["reference_deidentification"] = 0.0
            deductions.append("[-20 pts] Banned artist reference or copyright trigger phrase in Style box.")

        # 4. Structural Metatags (10 pts)
        if not metatag_res.is_valid:
            dim_scores["structural_metatags"] -= 6.0
            deductions.append(f"[-6 pts] Invalid metatags or syntax errors: {metatag_res.errors}")
        elif metatag_res.metrics.get("total_tags", 0) == 0:
            dim_scores["structural_metatags"] -= 4.0
            deductions.append("[-4 pts] No bracketed structural metatags found.")

        # 5. Style Field Purity (10 pts)
        if style_res.metrics.get("has_metadata_leak", False):
            dim_scores["style_field_purity"] = 0.0
            deductions.append("[-10 pts] Forbidden metadata label (Language:, Theme:, etc.) in Style box.")

        # 6. Ukrainian Authenticity (10 pts)
        # Check if Ukrainian/Slavic musical markers or instruments are present where relevant
        style_lower = style_prompt.lower()
        has_ukr_marker = any(m in style_lower for m in [
            "ukrainian", "carpathian", "bandura", "sopilka", "white voice",
            "slavic", "folk", "polyphonic", "tsymbaly", "bayan", "trembita"
        ])
        if not has_ukr_marker:
            dim_scores["ukrainian_authenticity"] -= 3.0
            deductions.append("[-3 pts] No distinctive Ukrainian/Slavic sonic or vocal timbre markers specified.")

        # 7. Exclude Precision (10 pts)
        if exclude_prompt:
            for err in style_res.errors:
                if "exclude" in err.lower():
                    dim_scores["exclude_precision"] -= 6.0
                    deductions.append(f"[-6 pts] Exclude field violation: {err}")
        else:
            dim_scores["exclude_precision"] -= 2.0
            deductions.append("[-2 pts] Exclude field was left empty.")

        # 8. Custom Mode Split (5 pts)
        if not (style_prompt and lyrics_text):
            dim_scores["custom_mode_split"] = 0.0
            deductions.append("[-5 pts] Incomplete Custom Mode fields.")

        # Ensure no negative dimension score
        for k in dim_scores:
            dim_scores[k] = max(0.0, dim_scores[k])

        total_score = sum(dim_scores.values())
        return RubricScoreBreakdown(total_score, 100.0, dim_scores, deductions)

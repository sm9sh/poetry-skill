"""
Suno AI, Udio AI & Google Flow Music Unified Prompt Validation Engine.
Provides comprehensive validation for:
- Suno v4.5 / v5.5 Custom Mode payloads (Method 1 Conversational & Method 2 Tag-Based Matrix)
- Udio v4 Prompt syntax (250 char cap, Inpainting *stars*, Context Length)
- Google Flow Music (Lyria 3.5) Conversational Agent blocks
- 10 AI Quality Gates verification
- Re-exports StyleValidator, MetatagValidator, RubricScorer for unified access
"""

import re
from typing import Dict, List, Optional, Tuple, Any

from .style_validator import StyleValidator, StyleValidationResult
from .metatag_validator import MetatagValidator, MetatagValidationResult
from .rubric_scorer import RubricScorer, RubricScoreBreakdown


class SunoValidationResult:
    def __init__(self, is_valid: bool, errors: List[str], warnings: List[str], metrics: Dict[str, Any]):
        self.is_valid = is_valid
        self.errors = errors
        self.warnings = warnings
        self.metrics = metrics

    def to_dict(self) -> Dict[str, Any]:
        return {
            "is_valid": self.is_valid,
            "errors": self.errors,
            "warnings": self.warnings,
            "metrics": self.metrics,
        }


class SunoValidator:
    """
    Unified multi-platform AI music validation engine for Suno, Udio, and Google Flow Music.
    """

    # Multi-platform constants
    SUNO_MAX_STYLE_CHARS = 1000
    SUNO_OPTIMAL_STYLE_MIN = 80
    SUNO_OPTIMAL_STYLE_MAX = 180
    SUNO_MAX_LYRICS_CHARS = 5000

    UDIO_MAX_PROMPT_CHARS = 250
    UDIO_CONTEXT_LENGTH_TRANSITION = "10-15s"
    UDIO_CONTEXT_LENGTH_CONTINUITY = "15m"

    FLOW_MUSIC_DAILY_CREDITS = 500
    FLOW_MUSIC_ENGINE = "Lyria 3.5"

    @classmethod
    def validate_suno_style(
        cls,
        style_prompt: str,
        max_chars: int = 180,
        min_chars: int = 20,
        strict_compact: bool = False,
        forbidden_references: Optional[List[str]] = None,
    ) -> StyleValidationResult:
        """Validates Suno Style of Music box."""
        return StyleValidator.validate_style_prompt(
            style_prompt,
            max_chars=max_chars,
            min_chars=min_chars,
            strict_compact=strict_compact,
            forbidden_references=forbidden_references,
        )

    @classmethod
    def validate_suno_lyrics(
        cls,
        lyrics_text: str,
        require_intro_or_verse: bool = False,
        require_chorus: bool = False,
    ) -> MetatagValidationResult:
        """Validates Suno/Multi-platform Lyrics and Metatags."""
        return MetatagValidator.validate_lyrics_structure(
            lyrics_text,
            require_intro_or_verse=require_intro_or_verse,
            require_chorus=require_chorus,
        )

    @classmethod
    def validate_suno_exclude(
        cls,
        exclude_prompt: str,
        max_chars: int = 150,
    ) -> StyleValidationResult:
        """Validates Suno Exclude / Negative prompt field."""
        return StyleValidator.validate_exclude_field(exclude_prompt, max_chars=max_chars)

    @classmethod
    def validate_custom_mode_payload(
        cls,
        payload: Dict[str, Any],
        max_style_chars: int = 180,
        strict_compact_style: bool = False,
        forbidden_references: Optional[List[str]] = None,
    ) -> StyleValidationResult:
        """Validates full Suno Custom Mode payload."""
        return StyleValidator.validate_custom_mode_payload(
            payload,
            max_style_chars=max_style_chars,
            strict_compact_style=strict_compact_style,
            forbidden_references=forbidden_references,
        )

    @classmethod
    def validate_udio_prompt(
        cls,
        prompt_text: str,
        max_chars: int = 250,
    ) -> SunoValidationResult:
        """
        Validates Udio v4 prompt text (max 250 chars, *stars* inpainting syntax check, de-identification).
        """
        errors = []
        warnings = []
        cleaned = prompt_text.strip()
        char_count = len(cleaned)

        if char_count > max_chars:
            errors.append(f"Udio prompt exceeded hard cap: {char_count} chars (max {max_chars}).")
        elif char_count < 15:
            warnings.append(f"Udio prompt is very short: {char_count} chars.")

        # Check for direct artist references in Udio prompt
        prompt_lower = cleaned.lower()
        for artist in StyleValidator.BANNED_ARTISTS:
            if re.search(r"\b" + re.escape(artist) + r"\b", prompt_lower):
                errors.append(f"Direct artist name detected in Udio prompt: '{artist}'.")

        # Inpainting stars check (if * used, must be balanced in pairs)
        star_count = cleaned.count("*")
        if star_count > 0 and star_count % 2 != 0:
            errors.append(f"Unbalanced inpainting asterisks in Udio prompt: found {star_count} '*' characters.")

        metrics = {
            "char_count": char_count,
            "max_chars": max_chars,
            "has_inpainting_tags": star_count >= 2,
        }

        return SunoValidationResult(len(errors) == 0, errors, warnings, metrics)

    @classmethod
    def validate_flow_music_prompt(
        cls,
        flow_prompt: str,
    ) -> SunoValidationResult:
        """
        Validates Google Flow Music (Lyria 3.5) conversational agent prompt structure.
        """
        errors = []
        warnings = []
        cleaned = flow_prompt.strip()

        if len(cleaned) < 20:
            warnings.append("Google Flow Music prompt is short; include genre hybrid, acoustic timbre, and vocal cues.")

        # Check for bracket isolation (silent arrangement vs sung parentheses)
        meta_res = MetatagValidator.validate_lyrics_structure(cleaned)
        errors.extend(meta_res.errors)
        warnings.extend(meta_res.warnings)

        metrics = {
            "char_count": len(cleaned),
            "engine": cls.FLOW_MUSIC_ENGINE,
            "free_daily_credits": cls.FLOW_MUSIC_DAILY_CREDITS,
        }

        return SunoValidationResult(len(errors) == 0, errors, warnings, metrics)

    @classmethod
    def score_prompt_package(
        cls,
        style_prompt: str,
        lyrics_text: str,
        exclude_prompt: str = "",
        strict_compact: bool = False,
    ) -> RubricScoreBreakdown:
        """
        Calculates 100-point rubric score for full Suno prompt package.
        """
        style_res = cls.validate_suno_style(style_prompt, strict_compact=strict_compact)
        meta_res = cls.validate_suno_lyrics(lyrics_text) if lyrics_text else MetatagValidator.validate_lyrics_structure("[Verse 1]\nSample")
        return RubricScorer.score_suno_style(
            style_prompt,
            lyrics_text,
            exclude_prompt,
            style_res,
            meta_res,
            strict_compact=strict_compact,
        )


__all__ = [
    "SunoValidator",
    "SunoValidationResult",
    "StyleValidator",
    "StyleValidationResult",
    "MetatagValidator",
    "MetatagValidationResult",
    "RubricScorer",
    "RubricScoreBreakdown",
]

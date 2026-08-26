"""
Suno AI Bracketed Metatag and Song Structure Validation Engine.
Validates standard bracketed metatags ([Verse], [Chorus], [Drop], etc.),
detects descriptive prose hallucinations inside brackets, and verifies parenthetical backing notation.
"""

import re
from typing import Dict, List, Optional, Tuple, Any, Set


class MetatagValidationResult:
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


class MetatagValidator:
    # Standard recognized Suno metatag prefixes / names (case-insensitive)
    VALID_TAG_PATTERNS = [
        # English canonical metatags
        r"^intro(\s+[\w\s-]+)?$",
        r"^verse(\s+\d+)?(\s+[\w\s-]+)?$",
        r"^pre-chorus(\s+\d+)?$",
        r"^pre chorus(\s+\d+)?$",
        r"^chorus(\s+\d+)?$",
        r"^post-chorus(\s+\d+)?$",
        r"^post chorus(\s+\d+)?$",
        r"^bridge(\s+\d+)?$",
        r"^drop(\s+[\w\s-]+)?$",
        r"^build-up$",
        r"^buildup$",
        r"^instrumental(\s+break)?$",
        r"^instrumental\s+solo$",
        r"^guitar\s+solo$",
        r"^bandura\s+solo$",
        r"^sopilka\s+solo$",
        r"^synth\s+solo$",
        r"^bass\s+solo$",
        r"^drum\s+solo$",
        r"^solo$",
        r"^interlude$",
        r"^breakdown$",
        r"^hook(\s+\d+)?$",
        r"^refrain$",
        r"^spoken\s+word$",
        r"^spoken$",
        r"^whisper$",
        r"^whispering$",
        r"^chant$",
        r"^polyphonic\s+chant$",
        r"^outro$",
        r"^fade\s+out$",
        r"^fadeout$",
        r"^end$",
        r"^ending$",
        r"^silence$",
        r"^pause$",

        # Ukrainian translated canonical metatags
        r"^інтро$",
        r"^куплет(\s+\d+)?$",
        r"^передприспів(\s+\d+)?$",
        r"^приспів(\s+\d+)?$",
        r"^післяприспів(\s+\d+)?$",
        r"^міст(\s+\d+)?$",
        r"^бридж(\s+\d+)?$",
        r"^дроп$",
        r"^програш$",
        r"^інструментал$",
        r"^соло$",
        r"^соло\s+гітари$",
        r"^соло\s+бандури$",
        r"^соло\s+сопілки$",
        r"^речитатив$",
        r"^декламація$",
        r"^шепіт$",
        r"^аутро$",
        r"^кінцівка$",
        r"^фінал$",
        r"^затихання$",
    ]

    # Patterns indicating prose / instruction hallucinations inside brackets
    PROSE_HALLUCINATION_PATTERNS = [
        r"\b(plays|playing|starts|sing|singing|with|and|that|which|very|slowly|emotional|weeps|cries|loudly|softly)\b",
        r"\b(грає|співає|починає|дуже|тихо|голосно|плаче|емоційно|ніжно|швидко)\b",
        r"\b(she sings|he sings|vocalist starts|acoustic guitar begins|drums enter)\b",
    ]

    @classmethod
    def extract_bracketed_tags(cls, lyrics_text: str) -> List[str]:
        """Extracts all strings inside square brackets from lyrics."""
        return re.findall(r"\[(.*?)\]", lyrics_text)

    @classmethod
    def extract_parentheses(cls, lyrics_text: str) -> List[str]:
        """Extracts all strings inside round parentheses from lyrics."""
        return re.findall(r"\((.*?)\)", lyrics_text)

    @classmethod
    def is_valid_tag(cls, tag_content: str) -> Tuple[bool, Optional[str]]:
        """
        Checks whether a bracketed tag content conforms to standard metatag syntax.
        Returns (is_valid, error_reason).
        """
        cleaned = tag_content.strip().lower()

        # Empty brackets
        if not cleaned:
            return False, "Empty brackets '[]' found in lyrics."

        # Check for length (> 35 chars is almost certainly prose hallucination)
        if len(cleaned) > 35:
            return False, f"Metatag '[{tag_content}]' is too long ({len(cleaned)} chars) and looks like prose."

        # Check against prose hallucination patterns
        for prose_pat in cls.PROSE_HALLUCINATION_PATTERNS:
            if re.search(prose_pat, cleaned) and not any(re.match(p, cleaned) for p in cls.VALID_TAG_PATTERNS):
                return False, f"Prose/narrative hallucination detected inside metatag: '[{tag_content}]'."

        # Check against recognized valid tag patterns
        for pattern in cls.VALID_TAG_PATTERNS:
            if re.match(pattern, cleaned):
                return True, None

        # If it's a short 1-3 word tag that is reasonable (e.g. [Heavy Drop], [Female Vocal Solo])
        words = cleaned.split()
        if len(words) <= 3 and not any(re.search(p, cleaned) for p in cls.PROSE_HALLUCINATION_PATTERNS):
            return True, None

        return False, f"Unrecognized metatag syntax: '[{tag_content}]'."

    @classmethod
    def validate_lyrics_structure(
        cls,
        lyrics_text: str,
        require_intro_or_verse: bool = False,
        require_chorus: bool = False,
    ) -> MetatagValidationResult:
        """
        Validates lyrics structure, checking all bracketed tags and parenthetical notations.
        """
        errors = []
        warnings = []
        tags = cls.extract_bracketed_tags(lyrics_text)
        parentheses = cls.extract_parentheses(lyrics_text)

        if not tags:
            warnings.append("Lyrics text contains no bracketed metatags (e.g. [Verse], [Chorus]).")

        valid_tag_count = 0
        invalid_tags = []

        for tag in tags:
            valid, reason = cls.is_valid_tag(tag)
            if valid:
                valid_tag_count += 1
            else:
                errors.append(reason or f"Invalid metatag: '[{tag}]'")
                invalid_tags.append(tag)

        # Check structural requirements if enabled
        tags_lower = [t.strip().lower() for t in tags]
        has_verse = any("verse" in t or "куплет" in t for t in tags_lower)
        has_chorus = any("chorus" in t or "приспів" in t or "hook" in t for t in tags_lower)
        has_intro = any("intro" in t or "інтро" in t for t in tags_lower)

        if require_intro_or_verse and not (has_intro or has_verse):
            errors.append("Lyrics structure missing an opening [Intro] or [Verse] metatag.")

        if require_chorus and not has_chorus:
            errors.append("Lyrics structure missing a [Chorus] or [Приспів] metatag.")

        # Check for unclosed brackets or mismatched tags
        open_brackets = lyrics_text.count("[")
        close_brackets = lyrics_text.count("]")
        if open_brackets != close_brackets:
            errors.append(
                f"Mismatched square brackets: {open_brackets} '[' vs {close_brackets} ']'."
            )

        open_parens = lyrics_text.count("(")
        close_parens = lyrics_text.count(")")
        if open_parens != close_parens:
            errors.append(
                f"Mismatched parentheses: {open_parens} '(' vs {close_parens} ')'."
            )

        metrics = {
            "total_tags": len(tags),
            "valid_tags": valid_tag_count,
            "invalid_tags": invalid_tags,
            "tags_found": tags,
            "parenthetical_count": len(parentheses),
            "has_verse": has_verse,
            "has_chorus": has_chorus,
            "has_intro": has_intro,
        }

        is_valid = len(errors) == 0
        return MetatagValidationResult(is_valid, errors, warnings, metrics)

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
    # Canonical structural prefixes recognized in Suno / Flow Music
    STRUCTURAL_PREFIXES = [
        "intro", "verse", "pre-chorus", "pre chorus", "chorus", "post-chorus",
        "post chorus", "bridge", "drop", "build-up", "buildup", "build",
        "instrumental", "instrumental break", "instrumental solo", "guitar solo",
        "bandura solo", "sopilka solo", "synth solo", "bass solo", "drum solo",
        "solo", "interlude", "breakdown", "break", "hook", "refrain",
        "spoken word", "spoken", "whisper", "whispering", "chant",
        "polyphonic chant", "outro", "fade out", "fadeout", "fade", "end",
        "ending", "climax", "silence", "pause",
        # Ukrainian equivalents
        "інтро", "куплет", "передприспів", "приспів", "післяприспів",
        "міст", "бридж", "дроп", "програш", "інструментал", "соло",
        "соло гітари", "соло бандури", "соло сопілки", "речитатив",
        "декламація", "шепіт", "аутро", "кінцівка", "фінал", "затихання"
    ]

    # Instrumental and arrangement keywords that MUST NEVER appear inside round parentheses ()
    INSTRUMENTAL_KEYWORDS_IN_PARENS = [
        "riff", "bassline", "telecaster", "guitar", "bandura", "sopilka", "synth",
        "drums", "percussion", "arpeggio", "arpeggios", "staccato", "legato",
        "buildup", "breakdown", "distortion", "reverb", "808", "sub bass",
        "beat", "solo", "tempo", "bpm", "fade out", "drone", "strings", "cello",
        "brass", "piano", "organ", "groove", "drop", "бас", "гітара", "барабани",
        "соло", "дроп", "синтезатор"
    ]
    
    # Narrative conversation prose hallucination patterns (not sound design cues)
    PROSE_HALLUCINATION_PATTERNS = [
        r"\b(the song begins|singer weeps|vocalist starts|starts playing|starts weeping|while \w+ enter|they talk about|conversation starts)\b",
        r"\b(вона співає|він плаче|починається розмова|співак плаче|розповідає історію|пісня починається)\b",
        r"\b(playing softly|playing aggressively)\b",
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
        Validates an individual tag inside square brackets.
        Supports both canonical 1-3 word tags ([Intro], [Guitar Solo]) and compound
        sound-design directives ([Intro - Staccato cutting telecaster riff, driving bassline]).
        """
        cleaned = tag_content.strip().lower()

        # Empty brackets
        if not cleaned:
            return False, "Empty brackets '[]' found in lyrics."

        # Check for extreme length (> 120 chars is excessive for a section tag)
        if len(cleaned) > 120:
            return False, f"Metatag '[{tag_content}]' is too long ({len(cleaned)} chars, max 120)."

        # Check against narrative prose hallucinations
        for prose_pat in cls.PROSE_HALLUCINATION_PATTERNS:
            if re.search(prose_pat, cleaned, re.IGNORECASE):
                return False, f"Narrative prose hallucination detected inside metatag: '[{tag_content}]'."

        # 1. Compound tags with delimiter [Section - Sound description] or [Section: Sound description]
        if ("-" in cleaned or ":" in cleaned or "–" in cleaned or "—" in cleaned):
            parts = re.split(r"[-–—:]", cleaned, 1)
            section = parts[0].strip()
            # check if the left part is a known structural prefix or valid section name
            is_valid_section = any(
                re.match(r"^" + re.escape(prefix) + r"(\s+\d+)?$", section) or section.startswith(prefix)
                for prefix in cls.STRUCTURAL_PREFIXES
            )
            if is_valid_section and len(cleaned) <= 120 and len(cleaned.split()) <= 15:
                return True, None

        # 2. Direct match with structural prefix (with optional number / simple label)
        for prefix in cls.STRUCTURAL_PREFIXES:
            # Matches '[Intro]', '[Verse 1]', '[Chorus 2]', '[Guitar Solo]'
            if re.match(r"^" + re.escape(prefix) + r"(\s+\d+)?$", cleaned):
                return True, None
            # Matches standard combined labels e.g. '[Acoustic Bandura Solo]', '[White Voice Choir]', '[Spoken Word]'
            if cleaned.startswith(prefix) or cleaned.endswith(prefix):
                words = cleaned.split()
                if len(words) <= 4 and not re.search(r"\b(and|with|while)\b", cleaned, re.IGNORECASE):
                    return True, None

        # 3. Short 1-3 word sound design or dynamic tags (e.g. [Pianissimo], [80s Beat])
        words = cleaned.split()
        if len(words) <= 3 and not re.search(r"\b(and|with|while|the|starts|playing)\b", cleaned, re.IGNORECASE):
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
        Ensures instrumental descriptors are inside square brackets `[...]` and NEVER in `(...)`.
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

        # Validate Parentheses: In Suno & Flow Music, () are read as VOCAL lyrics/ad-libs.
        # Instrumental instructions inside () will be sung out loud by the voice engine!
        for paren in parentheses:
            paren_clean = paren.strip().lower()
            # Check if paren contains typical instrumental/arrangement descriptors
            matched_inst = [kw for kw in cls.INSTRUMENTAL_KEYWORDS_IN_PARENS if re.search(r"\b" + re.escape(kw) + r"\b", paren_clean)]
            if matched_inst:
                errors.append(
                    f"Instrumental descriptor '{paren}' found in parentheses '()'. "
                    f"In Suno AI and Google Flow Music, text in parentheses is read out loud as vocals/ad-libs. "
                    f"Use square brackets '[...]' for musical instructions (e.g. '[Intro - {paren}]' or '[{paren}]')."
                )

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

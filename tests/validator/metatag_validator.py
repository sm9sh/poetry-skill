"""
Suno AI & Multi-Platform Audio Metatag and Song Structure Validation Engine.
Validates standard bracketed metatags ([Verse], [Chorus], [Vocal Intro], [Beat Drop], [Mega-Chorus], etc.),
detects descriptive prose hallucinations inside brackets, and verifies that round parentheses hold only
singable backing vocals / echoes. Delivery cues ([Whispered], [Belted], [Key Change], [Half-time feel])
must live in square brackets because Suno and Google Flow Music sing anything inside parentheses.
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
    # Canonical structural prefixes recognized in Suno / Udio / Google Flow Music
    STRUCTURAL_PREFIXES = [
        # English structural markers
        "vocal intro", "intro", "verse", "pre-chorus", "pre chorus", "chorus",
        "mega-chorus", "mega chorus", "final chorus", "last chorus", "post-chorus", "post chorus", "bridge",
        "drop", "beat drop", "build-up", "buildup", "build", "breakdown", "break",
        "instrumental", "instrumental break", "instrumental solo", "short instrumental fill",
        "instrumental fill", "fill", "guitar solo",
        "bandura solo", "sopilka solo", "synth solo", "bass solo", "drum solo",
        "solo", "acoustic solo", "acoustic bandura solo", "interlude", "hook",
        "vocal hook", "vocal solo", "refrain", "spoken word", "spoken", "whisper",
        "whispering", "chant", "polyphonic chant", "white voice choir", "choir",
        "acapella", "outro", "fade out", "fadeout", "fade", "end", "ending",
        "cold end", "climax", "silence", "pause", "pianissimo", "fortissimo",
        "tempo", "dynamic",
        
        # Ukrainian structural markers
        "вокальний вступ", "інтро", "вступ", "куплет", "передприспів", "приспів",
        "мега-приспів", "мега приспів", "післяприспів", "міст", "бридж",
        "дроп", "біт дроп", "брейкдаун", "програш", "короткий програш",
        "інструментал", "інструментальна вставка", "соло",
        "соло гітари", "соло бандури", "соло сопілки", "соло басу", "соло ударних",
        "акустичне соло", "речитатив", "декламація", "шепіт", "хор", "багатоголосся",
        "білий голос", "акапела", "аутро", "кінцівка", "фінал", "холодний фінал",
        "затихання", "кульмінація", "пауза", "тиша", "темп", "динаміка"
    ]

    # Vocal delivery / arrangement cues. Suno (v6 family) and Google Flow Music SING whatever
    # is inside round parentheses, so these cues are only valid inside square brackets:
    # [Whispered], [Belted], [Key Change], [Verse 1 - whispered, half-time feel].
    DELIVERY_CUES_REQUIRE_BRACKETS = [
        "whispered", "belted", "falsetto", "screamed", "ad-lib", "ad lib",
        "building intensity", "key change", "half-time feel", "half time feel",
        "harmonized", "growl", "guttural scream", "vocal runs", "layered harmonies",
        "spoken", "spoken word", "acapella", "whisper", "melisma", "pause",
        "breathy delivery", "soaring vocalise", "stripped back", "fading out",
        # Ukrainian equivalents
        "шепіт", "прошепотіти", "фальцет", "скрім", "гроул", "речитатив", "пауза",
    ]

    # Instrumental and arrangement keywords that MUST NEVER appear alone inside round parentheses ()
    # because Suno & Flow Music vocalize/sing parenthetical text out loud
    INSTRUMENTAL_KEYWORDS_IN_PARENS = [
        "riff", "bassline", "telecaster", "guitar", "bandura", "sopilka", "synth",
        "drums", "percussion", "arpeggio", "arpeggios", "staccato", "legato",
        "buildup", "distortion", "reverb", "808", "sub bass",
        "bpm", "fade out", "drone", "strings", "cello",
        "brass", "piano", "organ", "groove", "бас", "гітара", "барабани",
        "соло", "синтезатор"
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
    def is_delivery_cue(cls, paren_content: str) -> bool:
        """True if the text is a delivery/arrangement cue that belongs in [brackets], not (parentheses)."""
        cleaned = paren_content.strip().lower().rstrip(".!")
        for cue in cls.DELIVERY_CUES_REQUIRE_BRACKETS:
            if cleaned == cue:
                return True
            # English cues may carry modifiers: "(whispered, intimate)", "(belted powerful)".
            # Ukrainian nouns like "шепіт" can be real sung lyrics ("(шепіт дощу)"), so exact match only.
            if cue.isascii() and (cleaned.startswith(cue + ",") or cleaned.startswith(cue + " ")):
                return True
        return False

    @classmethod
    def is_valid_vocal_gesture_or_backing(cls, paren_content: str) -> bool:
        """
        Returns True if parenthetical text is singable backing-vocal / echo lyric text
        (e.g. (ніколи знов), (о-о-о)). Delivery cues and instrument descriptions are rejected,
        because the audio model would sing them out loud.
        """
        cleaned = paren_content.strip().lower()
        if not cleaned:
            return True
        if cls.is_delivery_cue(cleaned):
            return False
        has_inst = any(
            re.search(r"\b" + re.escape(kw) + r"\b", cleaned)
            for kw in cls.INSTRUMENTAL_KEYWORDS_IN_PARENS
        )
        return not has_inst

    @classmethod
    def is_valid_tag(cls, tag_content: str) -> Tuple[bool, Optional[str]]:
        """
        Validates an individual tag inside square brackets.
        Supports:
        - Canonical section tags ([Verse], [Chorus], [Vocal Intro], [Beat Drop], [Mega-Chorus], [Breakdown], [Cold End])
        - Compound sound-design directives ([Vocal Intro - dynamic acapella, dry and close])
        - Section with Vance Powell / extension notes ([Verse 2 - Vance Powell: add driving tambourine, syncopated backing])
        - Ukrainian equivalents ([Вокальний вступ - акапела], [Мега-приспів - максимальна енергія])
        - Rejects prose hallucinations and conjunction-bloated standalone tags without delimiters.
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

        sorted_prefixes = sorted(cls.STRUCTURAL_PREFIXES, key=len, reverse=True)

        # 1. Compound tags with delimiter [Section - Sound description] or [Section: Sound description]
        # Match standard delimiters: " - ", " – ", " — ", ":", or hyphen preceded by space
        delim_match = re.search(r"\s+[-–—:]\s*|:\s*", cleaned)
        if delim_match:
            parts = re.split(r"\s+[-–—:]\s*|:\s*", cleaned, 1)
            section = parts[0].strip()
            desc = parts[1].strip() if len(parts) > 1 else ""

            # Check if section starts with or equals a known structural prefix
            is_valid_section = any(
                re.match(r"^" + re.escape(p) + r"(\s+\d+)?$", section) or section == p
                for p in sorted_prefixes
            )
            if is_valid_section and len(cleaned.split()) <= 20:
                if not re.search(r"\b(the song begins|singer weeps|vocalist starts)\b", desc):
                    return True, None

        # 2. Standalone tags without delimiter
        # Standalone tags must NOT contain narrative prose conjunctions/verbs (e.g. 'and', 'with', 'while', 'starts', 'playing', 'weeps')
        if re.search(r"\b(and|with|while|starts|playing|weeps|weeping|begins|entered|enter|about|loudly|softly)\b", cleaned):
            return False, f"Prose conjunction or action verb detected in standalone metatag: '[{tag_content}]'."

        # Direct exact match or prefix match
        for prefix in sorted_prefixes:
            # Exact match (e.g. '[Intro]', '[Verse 1]', '[Chorus 2]', '[Guitar Solo]', '[Cold End]')
            if re.match(r"^" + re.escape(prefix) + r"(\s+\d+)?$", cleaned):
                return True, None

        # Short 1-4 word sound design or dynamic tags (e.g. [Acoustic Bandura Solo], [White Voice Choir], [Pianissimo])
        words = cleaned.split()
        if len(words) <= 4:
            for prefix in sorted_prefixes:
                if cleaned.startswith(prefix) or cleaned.endswith(prefix):
                    return True, None
            if len(words) <= 3:
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
        Ensures instrumental descriptors and vocal delivery cues are inside square brackets `[...]`
        and NEVER in `(...)`; parentheses may only contain singable backing vocals / echoes.
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
        # Pure instrumental instructions inside () will be sung out loud by the voice engine!
        for paren in parentheses:
            paren_clean = paren.strip().lower()
            
            # If it is a whitelisted vocal delivery gesture or Ukrainian backing text, it is completely valid
            if cls.is_valid_vocal_gesture_or_backing(paren_clean):
                continue
                
            if cls.is_delivery_cue(paren_clean):
                errors.append(
                    f"Delivery cue '({paren})' found in parentheses. Suno and Google Flow Music sing text in '()'. "
                    f"Move it to square brackets: '[{paren.strip().capitalize()}]' or into the section tag "
                    f"('[Verse 1 - {paren.strip()}]')."
                )
                continue

            # Check if paren contains typical forbidden instrumental/arrangement descriptors
            matched_inst = [
                kw for kw in cls.INSTRUMENTAL_KEYWORDS_IN_PARENS
                if re.search(r"\b" + re.escape(kw) + r"\b", paren_clean)
            ]
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
        has_intro = any("intro" in t or "інтро" in t or "вступ" in t for t in tags_lower)

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

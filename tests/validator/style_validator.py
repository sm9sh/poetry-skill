"""
Multi-Platform AI Music Style Prompt and Negative Prompt Validation Engine.
Provides deterministic assertions and checks for Style of Music token economy,
metadata purity, anti-infringement rules, and Exclude field precision.
"""

import re
from typing import Dict, List, Optional, Tuple, Any


class StyleValidationResult:
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


class StyleValidator:
    # Forbidden metadata labels inside the Style of Music field
    FORBIDDEN_METADATA_LABELS = [
        r"language\s*:",
        r"theme\s*:",
        r"topic\s*:",
        r"story\s*:",
        r"bpm\s*:",
        r"title\s*:",
        r"lyrics\s*:",
        r"genre\s*:",
        r"mood\s*:",
        r"instruments?\s*:",
        r"vocals?\s*:",
        r"production\s*:",
    ]

    # Banned artist names and copyright-triggering phrases for reference de-identification
    BANNED_ARTISTS = [
        "okean elzy", "океан ельзи", "dakhabrakha", "дахабраха", "go_a", "go-a", "go a",
        "kalush", "калуш", "the hardkiss", "hardkiss", "хардкісс", "onuka", "онука",
        "antytila", "антитіла", "boombox", "бумбокс", "kazka", "казка",
        "jerry heil", "джеррі хейл", "alyona alyona", "альона альона",
        "kozak system", "козак систем", "vivienne mort", "вів'єн морт",
        "zwyntar", "цвинтар", "motanka", "мотанка", "latexfauna", "латексфауна",
        "karna", "карна", "sadsvit", "mistmorn", "dakh daughters", "даніела заюшкіна",
        "христина соловій", "khrystyna soloviy", "tvorchi", "твіорчі", "воплі відоплясова",
        "вв", "скрябін", "skryabin", "кузьма", "плач єремії", "тарас чубай",
    ]

    BANNED_REFERENCE_PHRASES = [
        "in the style of",
        "sounds like",
        "sound like",
        "cover of",
        "tribute to",
        "similar to",
        "like dakhabrakha",
        "like okean elzy",
        "like hardkiss",
        "like onuka",
        "like go_a",
    ]

    # Vague emotional or non-acoustic tokens forbidden in Exclude
    VAGUE_EXCLUDE_TOKENS = [
        "sadness", "sad vibes", "bad vibes", "darkness", "evil", "depression",
        "boring", "bad quality", "low quality", "bad sound", "noise",
        "negative emotions", "anger", "hate", "ugly sound", "poor audio",
    ]

    # Valid acoustic negative categories expected in Suno Exclude
    CONCRETE_ACOUSTIC_EXCLUDE_SAMPLES = [
        "heavy distortion", "brass", "trap hi-hats", "autotune", "edm drop",
        "acoustic guitar", "synth leads", "screaming", "growling", "choir",
        "saxophone", "metallic treble", "muddy bass", "reverb wash", "harsh frequencies",
        "applause", "spoken dialogue", "crowd noise", "guitar solo", "techno kick",
    ]

    @classmethod
    def validate_style_prompt(
        cls,
        style_prompt: str,
        max_chars: int = 180,
        min_chars: int = 20,
        strict_compact: bool = False,
        forbidden_references: Optional[List[str]] = None,
    ) -> StyleValidationResult:
        """
        Validates a Suno AI Style of Music prompt against character limits,
        metadata purity, and reference de-identification.
        """
        errors = []
        warnings = []
        cleaned_prompt = style_prompt.strip()
        char_count = len(cleaned_prompt)

        # 1. Character budget check
        effective_max = 120 if strict_compact else max_chars
        if char_count > effective_max:
            errors.append(
                f"Style field character limit exceeded: {char_count} chars (max allowed: {effective_max})."
            )
        elif char_count < min_chars:
            warnings.append(
                f"Style field is very short: {char_count} chars (minimum recommended: {min_chars})."
            )

        if not (80 <= char_count <= 150) and not strict_compact and char_count <= max_chars:
            warnings.append(
                f"Style field length ({char_count} chars) outside optimal range (80-150 chars)."
            )

        # 2. Metadata leakage check
        prompt_lower = cleaned_prompt.lower()
        for label_regex in cls.FORBIDDEN_METADATA_LABELS:
            match = re.search(label_regex, prompt_lower)
            if match:
                errors.append(
                    f"Metadata label leakage detected in Style box: '{match.group(0)}'. "
                    "Style box must contain only comma-separated musical descriptors."
                )

        # Check for full narrative sentence leakage (e.g. "This song is about...")
        if re.search(r"\b(this song is about|a song about|lyrics about|story of)\b", prompt_lower):
            errors.append(
                "Narrative story/lyric description leaked into Style box. Story details belong in Lyrics/Brief."
            )

        # 3. Reference de-identification check
        for phrase in cls.BANNED_REFERENCE_PHRASES:
            if phrase in prompt_lower:
                errors.append(
                    f"Copyright-triggering reference phrase found: '{phrase}'. "
                    "Deconstruct reference into pure acoustic traits."
                )

        # Check for specific banned artist names
        all_banned_artists = list(cls.BANNED_ARTISTS)
        if forbidden_references:
            all_banned_artists.extend([ref.lower() for ref in forbidden_references])

        for artist in all_banned_artists:
            # Word boundary search to avoid accidental substring matches
            pattern = r"\b" + re.escape(artist) + r"\b"
            if re.search(pattern, prompt_lower):
                errors.append(
                    f"Artist/band name detected in Style box: '{artist}'. "
                    "Direct artist references are strictly forbidden."
                )

        # 4. Token format and separator check
        tokens = [t.strip() for t in cleaned_prompt.split(",") if t.strip()]
        if len(tokens) < 2 and char_count >= 30:
            warnings.append("Style prompt does not appear to use comma-separated descriptors.")

        metrics = {
            "char_count": char_count,
            "token_count": len(tokens),
            "tokens": tokens,
            "has_metadata_leak": any("leakage" in e.lower() for e in errors),
            "has_artist_leak": any("artist" in e.lower() or "reference" in e.lower() for e in errors),
        }

        is_valid = len(errors) == 0
        return StyleValidationResult(is_valid, errors, warnings, metrics)

    @classmethod
    def validate_exclude_field(
        cls,
        exclude_prompt: str,
        max_chars: int = 150,
    ) -> StyleValidationResult:
        """
        Validates the Exclude / Negative prompt field for concreteness and absence of vague emotional tokens.
        """
        errors = []
        warnings = []
        cleaned_exclude = exclude_prompt.strip()
        char_count = len(cleaned_exclude)

        if not cleaned_exclude:
            warnings.append("Exclude field is empty.")
            return StyleValidationResult(True, errors, warnings, {"char_count": 0, "tokens": []})

        if char_count > max_chars:
            errors.append(f"Exclude field exceeded limit: {char_count} chars (max {max_chars}).")

        exclude_lower = cleaned_exclude.lower()
        for vague in cls.VAGUE_EXCLUDE_TOKENS:
            pattern = r"\b" + re.escape(vague) + r"\b"
            if re.search(pattern, exclude_lower):
                errors.append(
                    f"Vague non-acoustic token in Exclude field: '{vague}'. "
                    "Exclude must contain concrete musical instruments or production artifacts."
                )

        tokens = [t.strip() for t in cleaned_exclude.split(",") if t.strip()]
        metrics = {
            "char_count": char_count,
            "token_count": len(tokens),
            "tokens": tokens,
        }

        is_valid = len(errors) == 0
        return StyleValidationResult(is_valid, errors, warnings, metrics)

    @classmethod
    def validate_custom_mode_payload(
        cls,
        payload: Dict[str, Any],
        max_style_chars: int = 180,
        strict_compact_style: bool = False,
        forbidden_references: Optional[List[str]] = None,
    ) -> StyleValidationResult:
        """
        Validates a full Suno Custom Mode payload containing 'style_of_music', 'lyrics', and optional 'exclude'.
        """
        errors = []
        warnings = []
        metrics = {}

        # Check for required fields
        style = payload.get("style_of_music", payload.get("style", ""))
        lyrics = payload.get("lyrics", payload.get("lyrics_box", ""))
        exclude = payload.get("exclude", payload.get("negative_prompt", ""))

        if not style:
            errors.append("Custom Mode payload missing required 'style_of_music' field.")
        else:
            style_res = cls.validate_style_prompt(
                style,
                max_chars=max_style_chars,
                strict_compact=strict_compact_style,
                forbidden_references=forbidden_references,
            )
            errors.extend(style_res.errors)
            warnings.extend(style_res.warnings)
            metrics["style"] = style_res.metrics

        if not lyrics:
            errors.append("Custom Mode payload missing required 'lyrics' field.")

        if exclude:
            exclude_res = cls.validate_exclude_field(exclude)
            errors.extend(exclude_res.errors)
            warnings.extend(exclude_res.warnings)
            metrics["exclude"] = exclude_res.metrics

        is_valid = len(errors) == 0
        return StyleValidationResult(is_valid, errors, warnings, metrics)

    @classmethod
    def validate_udio_prompt(
        cls,
        prompt: str,
        max_chars: int = 250,
        min_chars: int = 30,
        forbidden_references: Optional[List[str]] = None,
    ) -> StyleValidationResult:
        """
        Validates a Udio v4 prompt.
        Max 250 chars, min 30 chars, comma-separated descriptors.
        No structural metatags (like [Verse]) allowed.
        """
        errors = []
        warnings = []
        cleaned_prompt = prompt.strip()
        char_count = len(cleaned_prompt)

        if char_count > max_chars:
            errors.append(f"Udio prompt exceeded limit: {char_count} chars (max {max_chars}).")
        elif char_count < min_chars:
            warnings.append(f"Udio prompt is very short: {char_count} chars (minimum {min_chars}).")

        prompt_lower = cleaned_prompt.lower()
        
        # Metadata labels check
        for label_regex in cls.FORBIDDEN_METADATA_LABELS:
            if re.search(label_regex, prompt_lower):
                errors.append(
                    f"Metadata label leakage detected in Udio prompt. "
                    "Prompt must contain only comma-separated musical descriptors."
                )

        # Suno specific metatags leak
        if re.search(r"\[.*?\]", cleaned_prompt):
            errors.append("Structural metatags (like [Verse]) are not allowed in Udio prompt.")

        # Reference check
        for phrase in cls.BANNED_REFERENCE_PHRASES:
            if phrase in prompt_lower:
                errors.append(f"Copyright-triggering reference phrase found: '{phrase}'.")

        all_banned_artists = list(cls.BANNED_ARTISTS)
        if forbidden_references:
            all_banned_artists.extend([ref.lower() for ref in forbidden_references])

        for artist in all_banned_artists:
            pattern = r"\b" + re.escape(artist) + r"\b"
            if re.search(pattern, prompt_lower):
                errors.append(f"Artist/band name detected in Udio prompt: '{artist}'.")

        tokens = [t.strip() for t in cleaned_prompt.split(",") if t.strip()]
        if len(tokens) < 2 and char_count >= 30:
            warnings.append("Udio prompt does not appear to use comma-separated descriptors.")

        metrics = {
            "char_count": char_count,
            "token_count": len(tokens),
            "tokens": tokens,
        }

        is_valid = len(errors) == 0
        return StyleValidationResult(is_valid, errors, warnings, metrics)

    @classmethod
    def validate_udio_inpainting(
        cls,
        inpainting_text: str,
    ) -> StyleValidationResult:
        """
        Validates Udio inpainting replacement syntax.
        Words to replace must be wrapped in *asterisks*.
        """
        errors = []
        warnings = []
        cleaned = inpainting_text.strip()
        
        matches = re.findall(r"\*(.*?)\*", cleaned)
        if not matches:
            errors.append("No asterisks found. Udio inpainting requires words to be wrapped in *asterisks*.")
            
        for match in matches:
            if not match.strip():
                errors.append("Empty asterisks found in inpainting text.")
            if re.search(r"\[.*?\]", match):
                errors.append(f"Structural metatags are not allowed inside inpainting marks: '*{match}*'")

        metrics = {
            "inpainting_segments_count": len(matches),
            "segments": matches
        }

        is_valid = len(errors) == 0
        return StyleValidationResult(is_valid, errors, warnings, metrics)

    @classmethod
    def validate_flow_music_prompt(
        cls,
        prompt: str,
        forbidden_references: Optional[List[str]] = None,
    ) -> StyleValidationResult:
        """
        Validates Google Flow Music Lyria 3.5 conversational agent mode prompt.
        """
        errors = []
        warnings = []
        cleaned_prompt = prompt.strip()
        char_count = len(cleaned_prompt)

        if char_count < 50:
            errors.append(f"Flow Music prompt too short: {char_count} chars (minimum 50).")
        if char_count > 1000:
            errors.append(f"Flow Music prompt exceeded limit: {char_count} chars (max 1000).")

        prompt_lower = cleaned_prompt.lower()
        
        if re.search(r"\[.*?\]", cleaned_prompt):
            errors.append("Suno-specific metatags (like [Verse]) are not allowed in Flow Music prompt.")
        if re.search(r"\(.*?\)", cleaned_prompt):
            errors.append("Suno-specific inline gestures (like (whispered)) are not allowed in Flow Music prompt text.")
            
        tokens = [t.strip() for t in cleaned_prompt.split(",") if t.strip()]
        if len(tokens) > 5 and not re.search(r"\b(create|make|generate|song|track|with|featuring|inspired)\b", prompt_lower):
            warnings.append("Flow Music prompt should be natural language, not just comma-separated tags.")

        # Key elements check
        if not re.search(r"(genre|style|rock|pop|jazz|metal|synth|techno|ambient|indie)", prompt_lower):
            warnings.append("Flow Music prompt should contain genre/style description.")
        if not re.search(r"(instrument|guitar|piano|synth|bass|drum|beat)", prompt_lower):
            warnings.append("Flow Music prompt should contain instrument description.")
        if not re.search(r"(vocal|voice|singer|singing|choir|whisper|belt)", prompt_lower):
            warnings.append("Flow Music prompt should contain vocal description.")

        # Reference check
        for phrase in cls.BANNED_REFERENCE_PHRASES:
            if phrase in prompt_lower:
                errors.append(f"Copyright-triggering reference phrase found: '{phrase}'.")

        all_banned_artists = list(cls.BANNED_ARTISTS)
        if forbidden_references:
            all_banned_artists.extend([ref.lower() for ref in forbidden_references])

        for artist in all_banned_artists:
            pattern = r"\b" + re.escape(artist) + r"\b"
            if re.search(pattern, prompt_lower):
                errors.append(f"Artist/band name detected in Flow Music prompt: '{artist}'.")

        metrics = {
            "char_count": char_count,
        }

        is_valid = len(errors) == 0
        return StyleValidationResult(is_valid, errors, warnings, metrics)

    @classmethod
    def validate_multi_platform_payload(
        cls,
        payload: Dict[str, Any],
        forbidden_references: Optional[List[str]] = None,
    ) -> StyleValidationResult:
        """
        Validates a full multi-platform payload containing 'platform'.
        Routes to the correct validator based on platform ('suno', 'udio', 'flow_music').
        """
        platform = payload.get("platform", "").lower()
        
        if platform == "suno":
            return cls.validate_custom_mode_payload(payload, forbidden_references=forbidden_references)
        elif platform == "udio":
            prompt = payload.get("prompt", "")
            res = cls.validate_udio_prompt(prompt, forbidden_references=forbidden_references)
            
            context_length = payload.get("context_length")
            if context_length is not None and not isinstance(context_length, (int, str)):
                res.errors.append("Invalid context_length format.")
                res.is_valid = False
                
            inpainting = payload.get("inpainting_text")
            if inpainting:
                inpaint_res = cls.validate_udio_inpainting(inpainting)
                res.errors.extend(inpaint_res.errors)
                res.warnings.extend(inpaint_res.warnings)
                res.is_valid = res.is_valid and inpaint_res.is_valid
                
            return res
        elif platform == "flow_music":
            prompt = payload.get("prompt", "")
            return cls.validate_flow_music_prompt(prompt, forbidden_references=forbidden_references)
        else:
            return StyleValidationResult(
                False, 
                [f"Unsupported platform: '{platform}'. Must be 'suno', 'udio', or 'flow_music'."], 
                [], 
                {}
            )

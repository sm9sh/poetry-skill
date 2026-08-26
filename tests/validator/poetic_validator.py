"""
Ukrainian Poetic and Linguistic Validation Engine.
Provides deterministic scansion, syllable counting, clausula analysis,
Russianism / Surzhyk filtering, anti-sharovarshchyna detection, taboo word checks,
stress homograph validation, and heterogeneous rhyme classification.
"""

import re
from typing import Dict, List, Optional, Tuple, Any, Set


class PoeticValidationResult:
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


class PoeticValidator:
    # Ukrainian vowels (strictly base vowels, combining accents handled separately)
    UKR_VOWELS = set("аеєиіїоуюяАЕЄИІЇОУЮЯ")
    
    # Common Surzhyk and Russianism phrases with recommended Ukrainian corrections
    SURZHYK_DICTIONARY = {
        r"\bсамий\s+кращий\b": "найкращий",
        r"\bсамий\s+більший\b": "найбільший",
        r"\bсамий\s+перший\b": "найперший",
        r"\bсамий\s+головний\b": "найголовніший",
        r"\bсамий\s+[а-яіїєґ]+ий\b": "най- + прикметник",
        r"\bбільше\s+чим\b": "більше ніж / більше за",
        r"\bменше\s+чим\b": "менше ніж / менше за",
        r"\bв\s+кінці\s+кінців\b": "зрештою / кінець кінцем",
        r"\bприймати\s+участь\b": "брати участь",
        r"\bприйняти\s+участь\b": "взяти участь",
        r"\bполучається\b": "виходить",
        r"\bполучати\b": "отримувати / здобувати",
        r"\bслідуючий\b": "наступний",
        r"\bслідуюча\b": "наступна",
        r"\bслідуюче\b": "наступне",
        r"\bслідуючі\b": "наступні",
        r"\bявляється\b": "є / виступає",
        r"\bна\s+протязі\s+\d+\b": "протягом",
        r"\bна\s+протязі\s+(часу|дня|ночі|року|життя|місяця|тижня)\b": "протягом",
        r"\bвірніше\b": "точніше / вірніше кажучи -> точніше",
        r"\bкстати\b": "до речі",
        r"\bв\s+першу\s+чергу\b": "насамперед / передусім",
        r"\bв\s+залежності\s+від\b": "залежно від",
        r"\bпо\s+крайній\s+мірі\b": "принаймні",
        r"\bбувший\b": "колишній",
        r"\bвідноситися\s+до\b": "ставитися до / належати до",
        r"\bзаключається\b": "полягає",
        r"\bспівпадає\b": "збігається",
        r"\bдав\s+добро\b": "дав згоду / дозволив",
    }

    # Kitsch / Sharovarshchyna tokens that should not appear in non-folk modern poetry
    SHAROVARSHCHYNA_TOKENS = [
        "шаровари", "шароварщина", "сало", "горілка", "кунтуш", "чуприна",
    ]

    # Homographs with mobile stress and distinct meanings
    STRESS_HOMOGRAPHS = {
        "замок": ("зАмок (твердиня, фортеця)", "замОк (пристрій для замикання)"),
        "білизна": ("бІлизна (білість, відблиск)", "білизнА (тканина, одяг)"),
        "наголос": ("нАголос (знак наголосу)", "наголОс (акцент, підкреслення)"),
        "обід": ("О́бід (обіддя, обід колеса)", "обі́д (прийом їжі)"),
        "мука": ("мУка (страждання, терпіння)", "мукА (борошно)"),
        "дорога": ("дорОга (шлях)", "дорогА (коштовна, люба)"),
        "атлас": ("Атлас (збірник карт)", "атлАс (тканина)"),
        "орган": ("Орган (частина тіла / установа)", "оргАн (музичний інструмент)"),
        "плачу": ("плАчу (лити сльози)", "плачУ (віддавати гроші)"),
        "образи": ("Образи (ікони, художні зображення)", "обрАзи (кривди, зневаги)"),
        "бігом": ("бІгом (бігом, способом руху)", "бігОм (поспіхом, прислівник)"),
        "визнання": ("вИзнання (авторитет, пошана)", "визнАння (зізнання у чомусь)"),
        "потяг": ("пОтяг (схильність, прагнення)", "потЯг (поїзд)"),
    }

    # Common verb infinitive and inflected suffixes for grammatical rhyme detection
    VERB_SUFFIXES = (
        "ти", "тись", "тися", "ть", "ться",
        "ати", "яти", "іти", "ити", "ути",
        "ає", "яє", "ить", "їть", "уть", "ють", "ать", "ять",
        "не", "нуть", "лось", "лась", "лося", "лися",
        "ав", "яв", "ив", "ів", "ила", "іла", "ала", "али", "или", "іли",
    )

    # Common noun/adjective grammatical inflection suffixes for cheap rhyme detection
    GRAMMATICAL_SUFFIXES = (
        "ами", "ями", "ості", "остей", "істю", "ного", "ному", "ними", "тими",
    )

    # Stem and inflection mapping for standard taboo words
    TABOO_STEM_MAP = {
        "душа": r"\b(душ[а-яіїєґ]*)\b",
        "серце": r"\b(серц[а-яіїєґ]*|сердечн[а-яіїєґ]*|серд[а-яіїєґ]+)\b",
        "доля": r"\b(дол[іеяюью]|доле[ю]?|доленьк[а-яіїєґ]*|доль[а-яіїєґ]*)\b",
        "вічність": r"\b(вічн[а-яіїєґ]*)\b",
        "життя": r"\b(житт[а-яіїєґ]*)\b",
        "кохання": r"\b(кохан[а-яіїєґ]*)\b",
        "сльози": r"\b(сльоз[а-яіїєґ]*|сліз[а-яіїєґ]*)\b",
        "біль": r"\b(бол[іеяюью][а-яіїєґ]*|болюч[а-яіїєґ]*|біль|болю|болем|болями)\b",
    }

    @classmethod
    def count_syllables(cls, line: str) -> int:
        """Counts the number of syllables in a line of Ukrainian text."""
        cleaned = re.sub(r"\[.*?\]|\(.*?\)", "", line)
        cleaned = re.sub(r"[\u0300-\u036f]", "", cleaned)
        return sum(1 for char in cleaned if char in cls.UKR_VOWELS)

    @classmethod
    def get_lines_without_tags(cls, poem_text: str) -> List[str]:
        """Extracts text lines excluding bracketed metatags and empty lines."""
        lines = []
        for line in poem_text.splitlines():
            stripped = line.strip()
            # Skip empty lines and structural headers
            if not stripped or (stripped.startswith("[") and stripped.endswith("]")):
                continue
            lines.append(stripped)
        return lines

    @classmethod
    def check_surzhyk_and_russianisms(cls, text: str) -> List[Tuple[str, str]]:
        """
        Scans text for Surzhyk and Russianism phrases.
        Returns a list of (found_phrase, suggested_correction).
        """
        violations = []
        text_lower = text.lower()
        for pattern, correction in cls.SURZHYK_DICTIONARY.items():
            match = re.search(pattern, text_lower)
            if match:
                violations.append((match.group(0), correction))
        return violations

    @classmethod
    def check_taboo_words(cls, text: str, banned_words: List[str]) -> List[str]:
        """
        Checks if any explicitly banned taboo words appear in the text,
        including their inflected forms and derivatives.
        """
        found = []
        text_lower = text.lower()
        for word in banned_words:
            w_clean = word.lower().strip()
            if w_clean in cls.TABOO_STEM_MAP:
                pattern = cls.TABOO_STEM_MAP[w_clean]
            else:
                # Morphological stem matching for general Ukrainian words
                if w_clean.endswith("ість") and len(w_clean) > 4:
                    stem = w_clean[:-4]
                    pattern = r"\b" + re.escape(stem) + r"[а-яіїєґ]*\b"
                elif (w_clean.endswith("ння") or w_clean.endswith("ття")) and len(w_clean) > 3:
                    stem = w_clean[:-2]
                    pattern = r"\b" + re.escape(stem) + r"[а-яіїєґ]*\b"
                elif w_clean.endswith(("а", "е", "є", "и", "і", "о", "у", "ю", "я", "ь")) and len(w_clean) > 3:
                    stem = w_clean[:-1]
                    pattern = r"\b" + re.escape(stem) + r"[а-яіїєґ]*\b"
                else:
                    pattern = r"(?<![а-яіїєґА-ЯІЇЄҐ])" + re.escape(w_clean) + r"(?![а-яіїєґА-ЯІЇЄҐ])"
            
            if re.search(pattern, text_lower):
                found.append(word)
        return found

    @classmethod
    def check_sharovarshchyna(cls, text: str, mode: str = "general") -> List[str]:
        """
        Checks for unprompted sharovarshchyna / kitsch tokens in non-folk contexts.
        """
        found = []
        if mode in ("folk", "historical_folk", "authentic_folk"):
            return found

        text_lower = text.lower()
        for token in cls.SHAROVARSHCHYNA_TOKENS:
            pattern = r"(?<![а-яіїєґА-ЯІЇЄҐ])" + re.escape(token.lower()) + r"(?![а-яіїєґА-ЯІЇЄҐ])"
            if re.search(pattern, text_lower):
                found.append(token)
        return found

    @classmethod
    def check_stress_homographs(cls, text: str) -> List[Dict[str, Any]]:
        """
        Detects occurrences of stress-sensitive homographs.
        Checks if explicit stress accents or capitalization (e.g. зАмок / замОк) are present.
        """
        reports = []
        text_lower = text.lower()
        for homograph, meanings in cls.STRESS_HOMOGRAPHS.items():
            pattern = r"(?<![а-яіїєґА-ЯІЇЄҐ])" + re.escape(homograph) + r"(?![а-яіїєґА-ЯІЇЄҐ])"
            matches = list(re.finditer(pattern, text_lower))
            if matches:
                # Check if original text has explicit stress notation (acute accent \u0301 or mixed case)
                for m in matches:
                    orig_word = text[m.start():m.end()]
                    has_explicit_stress = ("\u0301" in orig_word) or any(c.isupper() for c in orig_word[1:])
                    reports.append({
                        "word": homograph,
                        "found_as": orig_word,
                        "has_explicit_stress": has_explicit_stress,
                        "meanings": meanings,
                    })
        return reports

    @classmethod
    def classify_clausula(cls, line: str) -> str:
        """
        Determines the clausula (cadence ending) of a line.
        Returns 'M' (masculine), 'F' (feminine), 'D' (dactylic), or 'U' (unknown).
        """
        cleaned = re.sub(r"[^\w\sа-яіїєґА-ЯІЇЄҐ\u0301]", "", line).strip()
        words = cleaned.split()
        if not words:
            return "U"
        
        last_word = words[-1].lower()
        vowels = [c for c in last_word if c in cls.UKR_VOWELS]
        vowel_count = len(vowels)

        if vowel_count == 0:
            return "U"
        if vowel_count == 1:
            return "M"
        
        # Check for explicit acute accent or stress
        if "\u0301" in last_word:
            # Find vowel before accent
            parts = last_word.split("\u0301")
            # If stress is on last vowel -> M, penultimate -> F, etc.
            # Simplified heuristic based on common endings
            pass

        # Ukrainian typical accentuation rules by word endings
        if last_word.endswith(("а", "е", "я", "є", "о", "и", "і", "ю", "у", "ти", "ла", "ли", "ло")):
            if vowel_count == 2:
                return "F"
            if vowel_count >= 3 and last_word.endswith(("ого", "ому", "ими", "ості")):
                return "F"
            return "F"
        
        # Consonant endings often masculine in single/two-syllables with final stress
        if last_word.endswith(("в", "й", "к", "л", "м", "н", "р", "с", "т", "х")):
            if vowel_count == 2 and last_word.endswith(("ок", "як", "ун", "яр")):
                return "M"
            return "M" if vowel_count <= 2 else "F"

        return "F"

    @classmethod
    def check_meter_consistency(
        cls,
        poem_text: str,
        expected_meter: str = "iamb",
        expected_feet: Optional[int] = None,
    ) -> Tuple[bool, List[str], Dict[str, Any]]:
        """
        Checks syllabic and rhythm consistency for a specified meter.
        Supported meters: 'iamb', 'trochee', 'dactyl', 'amphibrach', 'anapest', 'dolnik', 'kolomyika'.
        """
        lines = cls.get_lines_without_tags(poem_text)
        errors = []
        syllable_counts = [cls.count_syllables(line) for line in lines]

        if not lines:
            return False, ["No poetic lines found in text."], {"line_count": 0}

        meter_lower = expected_meter.lower()

        if meter_lower == "kolomyika":
            # Kolomyika: either 14-syllable lines (4+4+6 with caesura) or alternating 8 and 6 syllables
            valid_kolomyika = True
            for i, line in enumerate(lines):
                count = syllable_counts[i]
                if count != 14 and count not in (8, 6):
                    errors.append(
                        f"Line {i+1} has {count} syllables (Kolomyika requires 14 syllables or 8/6 alternation): '{lines[i]}'"
                    )
                    valid_kolomyika = False
                elif count == 14:
                    # Check 4+4+6 caesura
                    if "/" in line:
                        parts = [p.strip() for p in line.split("/") if p.strip()]
                        if len(parts) == 3:
                            p_counts = [cls.count_syllables(p) for p in parts]
                            if p_counts != [4, 4, 6]:
                                errors.append(
                                    f"Line {i+1} has broken Kolomyika caesura segment counts {p_counts} (expected [4, 4, 6]): '{lines[i]}'"
                                )
                                valid_kolomyika = False
                        else:
                            errors.append(
                                f"Line {i+1} Kolomyika has {len(parts)} caesura segments (expected 3 segments [4+4+6]): '{lines[i]}'"
                            )
                            valid_kolomyika = False
                    else:
                        # Check word boundaries for 4+4+6 caesura
                        words = re.findall(r"[а-яіїєґА-ЯІЇЄҐ\u0300-\u036f]+", line)
                        cum = 0
                        boundaries = set()
                        for w in words:
                            cum += cls.count_syllables(w)
                            boundaries.add(cum)
                        if 4 not in boundaries or 8 not in boundaries:
                            errors.append(
                                f"Line {i+1} breaks Kolomyika 4+4+6 caesura structure (word boundaries must fall at syllables 4 and 8): '{lines[i]}'"
                            )
                            valid_kolomyika = False
                elif count == 8:
                    # For 8-syllable line in 8/6 pair, verify 4+4 sub-caesura
                    words = re.findall(r"[а-яіїєґА-ЯІЇЄҐ\u0300-\u036f]+", line)
                    cum = 0
                    boundaries = set()
                    for w in words:
                        cum += cls.count_syllables(w)
                        boundaries.add(cum)
                    if 4 not in boundaries:
                        errors.append(
                            f"Line {i+1} (8-syllable Kolomyika hemistich) breaks 4+4 caesura: '{lines[i]}'"
                        )
                        valid_kolomyika = False

            return valid_kolomyika, errors, {"syllable_counts": syllable_counts}

        elif meter_lower in ("dolnik", "taktovik", "accentual"):
            # Dolnik/Taktovik allows variable syllable counts across stresses (typically 6-26 syllables)
            is_consistent = all(6 <= count <= 26 for count in syllable_counts)
            if not is_consistent:
                errors.append(f"Dolnik syllable counts vary outside expected limits: {syllable_counts}")
            return len(errors) == 0, errors, {"syllable_counts": syllable_counts}

        elif meter_lower in ("iamb", "trochee"):
            # Binary meters: 2 syllables per foot
            # Check syllable count consistency across lines (typically variance <= 1 due to F/M clausulae)
            if syllable_counts:
                avg_syllables = sum(syllable_counts) / len(syllable_counts)
                for i, count in enumerate(syllable_counts):
                    if abs(count - avg_syllables) > 1.5:
                        errors.append(
                            f"Line {i+1} ({count} syllables) breaks syllabo-tonic regular length (expected ~{round(avg_syllables)}): '{lines[i]}'"
                        )

        elif meter_lower in ("dactyl", "amphibrach", "anapest"):
            # Ternary meters: 3 syllables per foot
            if syllable_counts:
                avg_syllables = sum(syllable_counts) / len(syllable_counts)
                for i, count in enumerate(syllable_counts):
                    if abs(count - avg_syllables) > 2.0:
                        errors.append(
                            f"Line {i+1} ({count} syllables) deviates from ternary foot count: '{lines[i]}'"
                        )

        metrics = {
            "line_count": len(lines),
            "syllable_counts": syllable_counts,
            "avg_syllables": sum(syllable_counts) / max(1, len(syllable_counts)),
        }
        return len(errors) == 0, errors, metrics

    @classmethod
    def check_clausula_alternation(cls, poem_text: str) -> Tuple[bool, List[str], List[str]]:
        """
        Checks if clausula cadence alternates cleanly (e.g. FMFM or MFMF).
        """
        lines = cls.get_lines_without_tags(poem_text)
        clausulae = [cls.classify_clausula(line) for line in lines]
        errors = []

        if len(clausulae) >= 4:
            # Check 4-line stanzas for alternation
            for stanza_idx in range(0, len(clausulae) - 3, 4):
                pattern = "".join(clausulae[stanza_idx:stanza_idx+4])
                # Common valid patterns: FMFM, MFMF, FFMM, MMFF, FMMF, MFFM
                valid_patterns = {"FMFM", "MFMF", "FFMM", "MMFF", "FMMF", "MFFM", "FFFF", "MMMM"}
                if pattern not in valid_patterns:
                    errors.append(
                        f"Stanza starting line {stanza_idx+1} has irregular clausula cadence: '{pattern}'"
                    )

        return len(errors) == 0, errors, clausulae

    @classmethod
    def check_grammatical_rhymes(cls, poem_text: str) -> List[Tuple[str, str]]:
        """
        Detects cheap grammatical / verb-verb or suffix-suffix rhyming pairs.
        """
        lines = cls.get_lines_without_tags(poem_text)
        cheap_rhymes = []

        last_words = []
        for line in lines:
            cleaned = re.sub(r"[^\wа-яіїєґА-ЯІЇЄҐ\u0300-\u036f]", "", line.split()[-1] if line.split() else "").lower()
            cleaned = re.sub(r"[\u0300-\u036f]", "", cleaned)
            if cleaned:
                last_words.append(cleaned)

        # Check adjacent or alternate rhyme pairs (AABB or ABAB)
        all_suffixes = cls.VERB_SUFFIXES + cls.GRAMMATICAL_SUFFIXES
        for i in range(len(last_words)):
            for j in (i + 1, i + 2):
                if j < len(last_words):
                    w1, w2 = last_words[i], last_words[j]
                    if len(w1) >= 4 and len(w2) >= 4 and w1 != w2:
                        for sfx in all_suffixes:
                            if w1.endswith(sfx) and w2.endswith(sfx) and len(sfx) >= 2:
                                # Both end in same grammatical suffix -> potential cheap grammatical rhyme
                                cheap_rhymes.append((w1, w2))
                                break

        return cheap_rhymes

    @classmethod
    def validate_poem(
        cls,
        poem_text: str,
        banned_words: Optional[List[str]] = None,
        expected_meter: Optional[str] = None,
        mode: str = "general",
        min_lines: int = 4,
        max_lines: int = 40,
    ) -> PoeticValidationResult:
        """
        Performs full comprehensive validation of a poem.
        """
        errors = []
        warnings = []
        lines = cls.get_lines_without_tags(poem_text)
        line_count = len(lines)

        # 1. Line count check
        if line_count < min_lines:
            errors.append(f"Poem is too short: {line_count} lines (minimum required: {min_lines}).")
        elif line_count > max_lines:
            warnings.append(f"Poem is long: {line_count} lines (max expected: {max_lines}).")

        # 2. Surzhyk and Russianism check
        surzhyk_matches = cls.check_surzhyk_and_russianisms(poem_text)
        for found, repl in surzhyk_matches:
            errors.append(f"Banned Russianism/Surzhyk detected: '{found}'. Suggested Ukrainian: '{repl}'.")

        # 3. Taboo words check
        if banned_words:
            taboo_matches = cls.check_taboo_words(poem_text, banned_words)
            for taboo in taboo_matches:
                errors.append(f"Forbidden taboo word found: '{taboo}'.")

        # 4. Sharovarshchyna check
        kitsch_matches = cls.check_sharovarshchyna(poem_text, mode=mode)
        for kitsch in kitsch_matches:
            errors.append(f"Unprompted kitsch / sharovarshchyna token detected in non-folk poem: '{kitsch}'.")

        # 5. Stress homograph check
        homographs = cls.check_stress_homographs(poem_text)

        # 6. Meter consistency check if specified
        meter_metrics = {}
        if expected_meter:
            meter_valid, meter_errors, meter_metrics = cls.check_meter_consistency(
                poem_text, expected_meter=expected_meter
            )
            errors.extend(meter_errors)

        # 7. Clausula alternation check
        clausula_valid, clausula_errors, clausulae = cls.check_clausula_alternation(poem_text)
        warnings.extend(clausula_errors)

        # 8. Grammatical rhyme check
        grammatical_rhymes = cls.check_grammatical_rhymes(poem_text)
        if grammatical_rhymes:
            for w1, w2 in grammatical_rhymes:
                warnings.append(f"Potential cheap grammatical/verb rhyme detected: '{w1}' - '{w2}'.")

        metrics = {
            "line_count": line_count,
            "lines": lines,
            "surzhyk_count": len(surzhyk_matches),
            "taboo_count": len(cls.check_taboo_words(poem_text, banned_words or [])),
            "clausulae": clausulae,
            "grammatical_rhymes_count": len(grammatical_rhymes),
            "homographs_found": homographs,
            "meter_metrics": meter_metrics,
        }

        is_valid = len(errors) == 0
        return PoeticValidationResult(is_valid, errors, warnings, metrics)

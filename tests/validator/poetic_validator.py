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

    # Patterns for artificial / forced end-rhyme syntactic inversions
    ARTIFICIAL_INVERSION_PATTERNS = [
        # 1. Verb + Postpositive Personal Pronoun at line end
        (
            r"\b([а-яіїєґА-ЯІЇЄҐ]+(?:в|ла|ло|ли|у|ю|еш|єш|е|є|емо|ємо|ете|єте|ить|їть|ать|ять|уть|ють|иш|їш|имо|їмо|ите|їте|нув|нула|нуло|нули|тиме|тиму|тимеш|тимемо|тимете|тимуть|всь|вся|лась|лося|лися))\s+(я|ти|він|вона|воно|ми|ви|вони)\s*[\.,!?;:—\-]*$",
            "Штучна інверсія 'дієслово + особовий займенник' у кінці рядка заради рими",
        ),
        # 2. Conjunction / subordinator / particle stranded at line end
        (
            r"\b([а-яіїєґА-ЯІЇЄҐ]+)\s+(що|щоб|як|мов|немов|ніби|бо|але|хоч|хоча)\s*[\.,!?;:—\-]*$",
            "Синтаксичний розрив сполучника / частки в кінці рядка",
        ),
        # 3. Unnatural auxiliary inversion at line end
        (
            r"\b(був|була|було|були|буде|будуть)\s+(я|ти|він|вона|воно|ми|ви|вони)\s*[\.,!?;:—\-]*$",
            "Штучна інверсія допоміжного дієслова із займенником у кінці рядка",
        ),
    ]

    # Rhythmic filler / padding clusters used solely for meter stuffing
    FILLER_RHYTHMIC_CLUSTERS = [
        r"\b(і\s+ось)\b",
        r"\b(ну\s+от)\b",
        r"\b(але\s+ж\s+бо)\b",
        r"\b(та\s+й\s+ось)\b",
        r"\b(то\s+ж\s+бо)\b",
        r"\b(а\s+я\s+ось)\b",
        r"\b(вже\s+ж\s+бо)\b",
        r"\b(ну\s+і\s+ось)\b",
        r"\b(от\s+і\s+все)\b",
        r"\b(ну\s+як\s+же)\b",
        r"\b(ось\s+і\s+знов)\b",
        r"\b(та\s+ось\s+же)\b",
    ]

    # High-density monosyllabic padding pronouns and particles
    FILLER_PRONOUNS_AND_PARTICLES = {
        "я", "ти", "він", "вона", "воно", "ми", "ви", "вони",
        "мій", "моє", "моя", "мої", "твій", "твоє", "твоя", "твої",
        "свій", "своє", "своя", "свої", "цей", "ця", "це", "ці",
        "той", "та", "те", "ті", "ось", "от", "вже",
    }

    # Banal / hackneyed cliché rhyme pairs
    BANAL_RHYME_PAIRS = [
        ("любов", "кров"),
        ("серце", "перце"),
        ("серце", "дверці"),
        ("доля", "воля"),
        ("сльози", "грози"),
        ("сльози", "морози"),
        ("грози", "морози"),
        ("сліз", "гріз"),
        ("ніч", "віч"),
        ("ніч", "пліч"),
        ("віч", "пліч"),
        ("ночі", "очі"),
        ("зорі", "морі"),
        ("зоря", "моря"),
        ("небо", "треба"),
        ("туга", "розлука"),
        ("туга", "друга"),
        ("день", "пень"),
        ("рано", "кохано"),
        ("жити", "любити"),
        ("знати", "кохати"),
        ("сон", "дзвін"),
        ("сни", "весни"),
    ]

    # Sensory grounding lexicon categorized by physical perception
    SENSORY_LEXICON = {
        "tactile": [
            "ірж", "мід", "вапн", "гравій", "шовк", "шорстк", "глин", "шкір", "граніт",
            "пісок", "піск", "пил", "скл", "заліз", "сталь", "дерев", "тканин", "колюч",
            "гостр", "шерст", "камін", "кам'ян", "бетон", "бруд", "волог", "сух", "мокр",
            "крапл", "долон", "пальц", "дотик", "кора", "голк", "струн", "склян", "мармур",
        ],
        "acoustic": [
            "рип", "шелест", "скрегіт", "свист", "гул", "дзеньк", "тріск", "лун", "дзвін",
            "гомін", "хруск", "шепіт", "стогін", "плюск", "брязк", "шум", "стук", "грім",
            "крик", "цокіт", "клацан", "тиш", "дзвен", "мовчан", "голос", "музик", "спів",
            "бриніт", "бринить",
        ],
        "visual": [
            "попіл", "морок", "бурштин", "слюд", "полин", "чад", "відблиск", "дим", "смол",
            "тінь", "туман", "іскр", "світл", "темр", "відтін", "багрян", "смарагд", "золот",
            "сріб", "куряв", "сяйв", "хмар", "зоря", "промін", "блиск", "шибк", "плям",
            "віддзеркал", "колір", "барв", "ліхтар", "п'єдестал", "колон", "рудий", "жовт",
            "синій", "червон", "чорн", "біл", "зелен",
        ],
        "thermal": [
            "холод", "тепл", "жар", "мороз", "криг", "крижан", "лід", "льод", "палюч",
            "студен", "прохолод", "пекуч", "вогн", "плам", "полум", "стиг", "охолон",
        ],
        "olfactory_gustatory": [
            "полин", "м'ят", "смол", "хвой", "гірк", "солод", "кисл", "терпк", "дим",
            "запах", "аромат", "пріл", "солон", "сиріст", "деревій", "кав", "хліб",
            "смак", "пахощ", "чайник", "мед",
        ],
    }

    # Abstract emotional noise lexicon
    ABSTRACT_LEXICON = [
        "душ", "серц", "дол", "вічн", "житт", "кохан", "почутт", "мрій", "наді",
        "сут", "бутт", "нескінчен", "ідеал", "абстракц", "духовн", "глибин", "стражд",
    ]

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
    def check_artificial_inversions(cls, poem_text: str, mode: str = "general") -> List[Dict[str, Any]]:
        """
        Detects artificial, forced end-rhyme syntactic inversions.
        Exempts authentic folk, baroque, and cossack baroque registers where
        traditional inverted phrasing is historically and stylistically canonical.
        """
        if mode in ("folk", "historical_folk", "authentic_folk", "baroque", "cossack_baroque", "baroque_cossack"):
            return []

        lines = cls.get_lines_without_tags(poem_text)
        inversions = []

        for i, line in enumerate(lines):
            line_clean = line.strip()
            for pattern, desc in cls.ARTIFICIAL_INVERSION_PATTERNS:
                m = re.search(pattern, line_clean, re.IGNORECASE)
                if m:
                    inversions.append({
                        "line_num": i + 1,
                        "line": line_clean,
                        "matched": m.group(0).strip(),
                        "description": desc,
                    })
                    break

        return inversions

    @classmethod
    def check_filler_words_and_pronouns(cls, poem_text: str, mode: str = "general") -> Dict[str, Any]:
        """
        Detects excessive monosyllabic filler clusters and padding pronouns
        used merely for meter stuffing.
        """
        lines = cls.get_lines_without_tags(poem_text)
        found_clusters = []

        # 1. Cluster check
        for i, line in enumerate(lines):
            line_clean = line.strip()
            for pat in cls.FILLER_RHYTHMIC_CLUSTERS:
                m = re.search(pat, line_clean, re.IGNORECASE)
                if m:
                    found_clusters.append({
                        "line_num": i + 1,
                        "line": line_clean,
                        "matched": m.group(0).strip(),
                    })

        # 2. Stanza-level pronoun and particle density check
        high_density_stanzas = []
        total_filler_count = 0
        total_word_count = 0

        stanza_size = 4
        for stanza_idx in range(0, len(lines), stanza_size):
            stanza_lines = lines[stanza_idx:stanza_idx + stanza_size]
            stanza_text = " ".join(stanza_lines)
            words = re.findall(r"[а-яіїєґА-ЯІЇЄҐ]+", stanza_text.lower())
            total_word_count += len(words)

            filler_tokens = [w for w in words if w in cls.FILLER_PRONOUNS_AND_PARTICLES]
            total_filler_count += len(filler_tokens)

            if len(words) >= 10 and mode not in ("folk", "children"):
                density = len(filler_tokens) / len(words)
                if len(filler_tokens) >= 5 or density >= 0.32:
                    high_density_stanzas.append({
                        "stanza_index": (stanza_idx // stanza_size) + 1,
                        "start_line": stanza_idx + 1,
                        "filler_count": len(filler_tokens),
                        "total_words": len(words),
                        "density": density,
                        "tokens": filler_tokens,
                    })

        overall_density = (total_filler_count / max(1, total_word_count)) if total_word_count > 0 else 0.0

        return {
            "clusters": found_clusters,
            "cluster_count": len(found_clusters),
            "high_density_stanzas": high_density_stanzas,
            "total_filler_count": total_filler_count,
            "overall_density": overall_density,
        }

    @classmethod
    def check_cliche_rhymes(cls, poem_text: str) -> List[Dict[str, Any]]:
        """
        Detects banned, worn-out cliché rhyming pairs (e.g. кров-любов, доля-воля, сльози-грози).
        """
        lines = cls.get_lines_without_tags(poem_text)
        cliche_rhymes = []

        last_words = []
        for i, line in enumerate(lines):
            cleaned = re.sub(r"[^\wа-яіїєґА-ЯІЇЄҐ\u0300-\u036f]", "", line.split()[-1] if line.split() else "").lower()
            cleaned = re.sub(r"[\u0300-\u036f]", "", cleaned)
            if cleaned:
                last_words.append((i + 1, cleaned, line))

        def _word_matches_stem(w: str, stem: str) -> bool:
            if w == stem:
                return True
            if stem in ("любов", "кров"):
                return w.startswith("любов") if stem == "любов" else w.startswith("кров")
            if stem in ("доля", "воля"):
                return (w.startswith("дол") or w.startswith("діл")) if stem == "доля" else (w.startswith("вол") or w.startswith("віл"))
            if stem in ("сльози", "сліз"):
                return w.startswith("сльоз") or w.startswith("сліз")
            if stem in ("грози", "гріз"):
                return w.startswith("гроз") or w.startswith("гріз")
            if stem == "морози":
                return w.startswith("мороз")
            if stem == "серце":
                return w.startswith("серц") or w.startswith("серд")
            if stem == "перце":
                return w.startswith("перц")
            if stem == "дверці":
                return w.startswith("дверц") or w.startswith("двер")
            if stem == "ніч":
                return w in ("ніч", "ночі", "ніччю", "ночах", "ночей")
            if stem == "віч":
                return w.startswith("віч")
            if stem == "пліч":
                return w.startswith("пліч")
            if stem in ("очі", "ночі"):
                return w.startswith("оч") if stem == "очі" else w.startswith("ноч")
            if stem in ("зорі", "зоря"):
                return w.startswith("зор") or w.startswith("зір")
            if stem in ("морі", "моря"):
                return w.startswith("мор")
            if stem == "небо":
                return w.startswith("неб")
            if stem == "треба":
                return w.startswith("треб")
            if stem == "туга":
                return w.startswith("туг")
            if stem == "розлука":
                return w.startswith("розлук")
            if stem == "друга":
                return w.startswith("друг")
            if stem == "день":
                return w in ("день", "дня", "днем", "дні")
            if stem == "пень":
                return w in ("пень", "пня", "пнем", "пні")
            if stem == "рано":
                return w.startswith("ран")
            if stem == "кохано":
                return w.startswith("кохан")
            if stem == "жити":
                return w.startswith("жит") or w.startswith("жив")
            if stem == "любити":
                return w.startswith("люб")
            if stem == "знати":
                return w.startswith("зна")
            if stem == "кохати":
                return w.startswith("коха")
            if stem in ("сон", "сни"):
                return w.startswith("сон") or w.startswith("сн")
            if stem == "дзвін":
                return w.startswith("дзвін") or w.startswith("дзвон")
            if stem == "весни":
                return w.startswith("весн")
            return w.startswith(stem[:-1]) if len(stem) > 3 else (w == stem)

        for i in range(len(last_words)):
            for j in (i + 1, i + 2, i + 3):
                if j < len(last_words):
                    l_num1, w1, line1 = last_words[i]
                    l_num2, w2, line2 = last_words[j]
                    if w1 != w2:
                        for p1, p2 in cls.BANAL_RHYME_PAIRS:
                            if (_word_matches_stem(w1, p1) and _word_matches_stem(w2, p2)) or \
                               (_word_matches_stem(w1, p2) and _word_matches_stem(w2, p1)):
                                cliche_rhymes.append({
                                    "line_num1": l_num1,
                                    "line_num2": l_num2,
                                    "word1": w1,
                                    "word2": w2,
                                    "pair": f"{p1}-{p2}",
                                    "line1": line1,
                                    "line2": line2,
                                })
                                break

        return cliche_rhymes

    @classmethod
    def evaluate_sensory_grounding(cls, poem_text: str) -> Dict[str, Any]:
        """
        Evaluates physical sensory grounding (tactile, acoustic, visual, thermal, olfactory)
        versus abstract emotional declarations.
        """
        words = re.findall(r"[а-яіїєґА-ЯІЇЄҐ'’]+", poem_text.lower())
        found_sensory: Dict[str, List[str]] = {cat: [] for cat in cls.SENSORY_LEXICON}
        found_abstract: List[str] = []

        for word in words:
            word_norm = word.replace("’", "'").replace("ʼ", "'")
            # Check sensory categories
            matched_sensory = False
            for cat, stems in cls.SENSORY_LEXICON.items():
                for stem in stems:
                    if word_norm.startswith(stem):
                        found_sensory[cat].append(word)
                        matched_sensory = True
                        break
                if matched_sensory:
                    break

            # Check abstract stems
            for stem in cls.ABSTRACT_LEXICON:
                if word_norm.startswith(stem):
                    found_abstract.append(word)
                    break

        total_sensory = sum(len(v) for v in found_sensory.values())
        active_categories = [cat for cat, toks in found_sensory.items() if len(toks) > 0]
        total_abstract = len(found_abstract)

        if total_sensory >= 3 and len(active_categories) >= 2:
            grounding_level = "high"
            sensory_score = 20.0
        elif total_sensory >= 1:
            grounding_level = "moderate"
            sensory_score = 18.0
        elif total_sensory == 0 and total_abstract >= 2:
            grounding_level = "purely_abstract"
            sensory_score = 12.0
        else:
            grounding_level = "low"
            sensory_score = 15.0

        return {
            "grounding_level": grounding_level,
            "sensory_score": sensory_score,
            "total_sensory_tokens": total_sensory,
            "active_categories": active_categories,
            "total_abstract_tokens": total_abstract,
            "details": {cat: toks for cat, toks in found_sensory.items() if toks},
            "abstract_tokens": found_abstract,
        }

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

        # 9. Artificial Inversions check
        inversions = cls.check_artificial_inversions(poem_text, mode=mode)
        if inversions:
            for inv in inversions:
                warnings.append(
                    f"Line {inv['line_num']}: Potential artificial syntactic inversion detected: '{inv['matched']}' ({inv['description']})."
                )

        # 10. Filler words and pronouns check
        filler_metrics = cls.check_filler_words_and_pronouns(poem_text, mode=mode)
        if filler_metrics["cluster_count"] > 0:
            for cl in filler_metrics["clusters"]:
                warnings.append(
                    f"Line {cl['line_num']}: Pleonastic rhythmic filler padding detected: '{cl['matched']}'."
                )
        if filler_metrics["high_density_stanzas"]:
            for s in filler_metrics["high_density_stanzas"]:
                warnings.append(
                    f"Stanza {s['stanza_index']}: Excessive filler pronoun/particle density ({s['filler_count']} tokens, {s['density']:.1%})."
                )

        # 11. Cliché rhymes check
        cliche_rhymes = cls.check_cliche_rhymes(poem_text)
        if cliche_rhymes:
            for cr in cliche_rhymes:
                warnings.append(
                    f"Lines {cr['line_num1']} & {cr['line_num2']}: Worn-out cliché rhyme pair detected: '{cr['word1']}' - '{cr['word2']}'."
                )

        # 12. Sensory Grounding evaluation
        sensory_metrics = cls.evaluate_sensory_grounding(poem_text)
        if sensory_metrics["grounding_level"] == "purely_abstract":
            warnings.append(
                "Text is purely abstract and lacks concrete sensory imagery (tactile, acoustic, visual, thermal, olfactory)."
            )

        metrics = {
            "line_count": line_count,
            "lines": lines,
            "surzhyk_count": len(surzhyk_matches),
            "taboo_count": len(cls.check_taboo_words(poem_text, banned_words or [])),
            "clausulae": clausulae,
            "grammatical_rhymes_count": len(grammatical_rhymes),
            "homographs_found": homographs,
            "meter_metrics": meter_metrics,
            "inversions": inversions,
            "inversion_count": len(inversions),
            "filler_metrics": filler_metrics,
            "filler_count": filler_metrics["cluster_count"] + len(filler_metrics["high_density_stanzas"]),
            "cliche_rhymes": cliche_rhymes,
            "cliche_rhyme_count": len(cliche_rhymes),
            "sensory_grounding": sensory_metrics,
        }

        is_valid = len(errors) == 0
        return PoeticValidationResult(is_valid, errors, warnings, metrics)

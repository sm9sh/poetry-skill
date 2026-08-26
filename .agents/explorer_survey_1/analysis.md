# Comprehensive Audit & Feature Exploration: Ukrainian Poetry Generation Skill

**Auditor**: Explorer 1 (Ukrainian Poetic & Linguistic Specialization)  
**Date**: 2026-08-26  
**Working Directory**: `d:/poetry-skill/.agents/explorer_survey_1`  
**Target Materials**: 
- `skills/ukrainian-poetry/SKILL.md`
- `skills/ukrainian-poetry/references/full-guide.md`
- `skills/ukrainian-poetry/references/input-templates.md`
- `skills/ukrainian-poetry/references/rubric.md`
- `skills/ukrainian-poetry/references/stress-tests.md`
- `skills/ukrainian-poetry/references/tests.md`
- Root mirrors: `ukrainian-poetry-skill.md`, `ukrainian-poetry-skill-uk.md`, `ukrainian-poetry-skill-lite.md`, `ukrainian-poetry-skill-rubric.md`, `ukrainian-poetry-skill-input-template.md`, `ukrainian-poetry-skill-stress-pack.md`, `ukrainian-poetry-skill-tests.md`
- Legacy sources: `source/legacy-skills/ukrainian-poetry.md`

---

## 1. Executive Summary & Problem Statement

The Ukrainian Poetry generation skill represents a thoughtful and stylistically tasteful framework. Its core ethos — **"Natural Ukrainian phrasing first; weaken form before weakening language"** — provides a vital defense against awkward, machine-translated verses.

However, an exhaustive linguistic, prosodic, and systemic audit reveals significant technical gaps in **versification mechanics**, **accentuation rigor**, **rhyme typology**, **non-standard registers**, and **evaluation rubrics**. While the instructions effectively steer models away from shallow sentimentality (e.g. banning overuse of *душа*, *доля*, *серце*), they lack the explicit, rule-based prosodic constraints necessary for an LLM to reliably generate complex metric forms, avoid subtle Russian stress interference, or construct authentic historical and contemporary poetic textures.

### Key Audit Findings at a Glance
1. **Versification Gaps**: Omission of **dactyl** from primary meter guidance; lack of operational definitions for **dolnik (дольник)**, **taktovik (тактовик)**, and **accentual verse (акцентний вірш)**; total absence of the foundational Ukrainian **kolomyika meter (коломийковий вірш: 4+4+6)**; failure to differentiate **blank verse (білий вірш)** from **free verse (верлібр)**; lack of fixed-form specifications (sonnet, rondo, triolet, terza rima).
2. **Stress & Accentuation Vulnerabilities**: Zero guidance on Ukrainian **mobile stress (рухомий наголос)**, double literary accents (*зАвжди / завждИ*), or stress homographs (*зАмок / замОк*, *нАголос / наголОс*). No guardrails against frequent LLM cross-linguistic stress transfers from Russian (*вИпадок* vs *випАдок*, *чорнОзем* vs *чорнозЕм*, *новИй* vs *нОвий*).
3. **Rhyme Typology Deficits**: The guidance lumps rhymes into vague "exact vs approximate" without explaining **grammatically heterogeneous rhymes (різнорідні рими)**, **rich pre-tonic rhymes (багаті опорні рими)**, or warning against pervasive suffixal diminutive clichés (*-очка/-ечка*, *-енька/-онька*).
4. **Register & Kitsch Incompleteness**: While *patriotic* and *folk* modes exist, they lack granular rules to prevent **sharovarshchyna (шароварщина)** and pseudo-folk kitsch (*соловейко-калина-гопак*), nor do they codify authentic **Baroque/Cossack**, **Urban Slang**, or **Hermetic/Neoclassical** registers.
5. **Rubric & Template Gaps**: Input templates omit `form`, `clausula`, `stanza_type`, and `subgenre`. The 100-point rubric lacks penalization categories for metric breakage, Russianisms, or stress deformation.

---

## 2. Deep Audit: Versification Systems & Poetic Forms

### 2.1 Syllabo-Tonic Meters (Силабо-тонічна система)

#### Observations in Current Codebase
- In `skills/ukrainian-poetry/SKILL.md:100`: *"Prefer iamb for balanced reflection, trochee for song-like drive, amphibrach for soft lyric movement, anapest for lift, and free verse when voice and image matter more than pattern."*
  - **Noticeable omission**: **Dactyl (дактиль — `— U U`)** is missing from the descriptive guidance sentence in `SKILL.md:100`, despite being listed in `references/input-templates.md:15`.
- In `references/full-guide.md:237-247`, meter descriptions are purely impressionistic without technical schemes or scansion notation.

#### Linguistic & Prosodic Reality in Ukrainian
1. **The Role of Pyrrhics (Пірихій — `U U`) & Spondees (Спондей — `— —`)**:
   - Ukrainian words average 2.8 to 3.2 syllables. A strict two-syllable foot meter (iamb `U —` or trochee `— U`) without pyrrhic substitutions would force poets to use only monosyllabic and disyllabic words, resulting in artificial, choppy phrasing.
   - The skill instructions do not explain that **pyrrhic substitution (пропуск метричного наголосу)** on polysyllabic words is standard and necessary in Ukrainian iambic/trochaic lines.
2. **Ternary Meters (Трьохскладні розміри: Дактиль, Амфібрахій, Анапест)**:
   - Ternary meters have fewer pyrrhic variations and demand stricter syllable-count consistency in Ukrainian.
   - **Dactyl (`— U U`)**: Foundational for solemn, elegiac, or narrative Ukrainian verse (e.g. Franko's *«Каменярі»*, Shevchenko's dactylic variations).
   - **Amphibrach (`U — U`)**: Widely used in romance, balladry, and 19th–20th c. intimate lyrics.
   - **Anapest (`U U —`)**: Conveys rising dynamic momentum and energetic declamation (e.g. Lesya Ukrainka, Bazhan).

### 2.2 Clausulae & Line Endings (Клаузули та їх чергування)

#### Current State
- Completely unaddressed in `SKILL.md` and `references/full-guide.md`.
- LLMs generating quatrains frequently output monotonous 4-line blocks of exclusively feminine (`ЖЖЖЖ`) or exclusively masculine (`ЧЧЧЧ`) rhymes, causing acoustic fatigue.

#### Required Rules for Clausulae
| Clausula Type | Ukrainian Term | Stress Position | Example | Acoustic Effect |
| :--- | :--- | :--- | :--- | :--- |
| **Masculine** | Чоловіча (Ч) | Final syllable (`—`) | *вого́нь, полі́т, земля́* | Crisp, abrupt, resolute |
| **Feminine** | Жіноча (Ж) | Penultimate syllable (`— U`) | *весна́ми, си́ла, но́чі* | Melodic, smooth, flowing |
| **Dactylic** | Дактилічна (Д) | 3rd from end (`— U U`) | *ві́трами, па́морозь, го́лосно* | Soft, undulating, folk-like |
| **Hyperdactylic** | Гіпердактилічна (Г) | 4th+ from end (`— U U U`) | *пе́рекотипо́лями* | Rare, experimental, playful |

**Standard Alternation Patterns (Чергування)**:
- `ЖЧЖЧ` (Feminine-Masculine-Feminine-Masculine): The default classical Ukrainian stanza cadence (e.g. Shevchenko, Franko, Rylsky, Kostenko).
- `ЧЖЧЖ` (Masculine-Feminine-Masculine-Feminine): Dynamic, assertive opening with soft suspension.
- `ЖЖЧЖ` or `ЧЧЖЧ`: Specialized folk and strophic variants.

### 2.3 Tonic, Accentual & Folk Versification (Тонічний, дольник, тактовик, народний вірш)

#### Current State
- `references/full-guide.md:229` merely states: *"Українська поезія може бути силабічною, тонічною, силабо-тонічною, фольклорною або верлібровою. Не підганяй усі тексти під одну схему."*
- There are **no actionable instructions** on how to write dolnik, taktovik, or authentic folk meters.

#### Prosodic System Breakdown
1. **Dolnik (Дольник)**:
   - Lines have an equal (or intentionally balanced) number of primary ictuses (3 or 4 stresses), but the interval of unstressed syllables between ictuses varies strictly between **1 and 2 syllables**.
   - Essential for early 20th-century Ukrainian modernism (Pavlo Tychyna's *«Сонячні кларнети»*, Bohdan-Ihor Antonych), as well as modern Ukrainian post-punk/rock songwriting.
2. **Taktovik (Тактовик)**:
   - Inter-ictic intervals vary more widely (**1 to 3 syllables**).
3. **Pure Accentual Verse (Чисто тонічний / акцентний вірш)**:
   - Regulated solely by the number of strong phrasal stresses per line (e.g. 3 or 4 stresses), with arbitrary unstressed syllables.
4. **Kolomyika Meter (Коломийковий вірш)**:
   - **Crucial Ukrainian national meter**: 14 syllables per couplet/line, broken strictly into `(4 + 4) + 6` (or two lines of `8 + 6` syllables: `4+4 // 4+2` with mandatory caesura after the 8th syllable).
   - Stress typically falls on the 3rd, 7th, 11th, and 13th syllables (trochaic baseline).
   - This is the engine of Ukrainian songs, Hutsul kolomyikas, and Shevchenko's ballad forms (e.g. *«Реве та стогне Дніпр широкий»* — modified 4+4//6).
5. **Cossack Duma Verse (Думний вірш / нерівноскладний речитатив)**:
   - Astrophic, uneven line lengths (from 4 to 16+ syllables), united by monorhyme or syntactic parallelism, resting on recitative cadence with extended dactylic or hyperdactylic feminine endings.

### 2.4 Free Verse (Верлібр) vs Blank Verse (Білий вірш)

#### Ambiguity in Current Codebase
- The prompt templates and guides treat `free-verse` as the sole unrhymed option.
- **Blank Verse (Білий вірш)** — unrhymed syllabo-tonic verse (e.g. unrhymed 5-foot iamb / *білий п'ятистопний ямб*) — is completely absent as a distinct mode or meter option, despite being the premier vehicle for Ukrainian poetic drama (Lesya Ukrainka, Kostomarov) and neoclassical monologue.

#### Distinction Matrix
| Form | Meter | Rhyme | Structural Principle | Primary Ukrainian Reference |
| :--- | :--- | :--- | :--- | :--- |
| **Free Verse (Верлібр)** | Non-metric | None (or irregular) | Syntagmatic cadence, enjambment, breath, image movement | Vasyl Holoborodko, Ihor Kalynets, Serhiy Zhadan |
| **Blank Verse (Білий вірш)** | Strict syllabo-tonic (e.g. Iamb 5-foot) | None (`rhyme: none`) | Meter constancy, enjambment, line-ending pause | Lesya Ukrainka (*«Кассандра»*, *«Одержима»*) |
| **Prose Poem (Поезія в прозі)** | Astrophic prose | None | Rhythmic prose, metaphoric density, soundplay | Ivan Franko, Olha Kobylianska, Mykhailo Kotsiubynsky |

### 2.5 Complex & Fixed Poetic Forms (Тверді поетичні форми)

The skill currently lacks explicit templates and formal rules for classical fixed forms:
1. **Sonnet (Сонет)**:
   - 14 lines: 2 quatrains (octave) + 2 tercets (sestet) `[4+4+3+3]` or 3 quatrains + couplet `[4+4+4+2]`.
   - Rhyme schemes: Italian/Petrarchan (`abba abba cdc dcd` or `abba abba cde cde`), French (`abba abba ccd eed`), English/Shakespearean (`abab cdcd efef gg`).
   - Internal logic: *Thesis* (1st quatrain) -> *Development* (2nd quatrain) -> *Volta / Turning Point* (line 9) -> *Synthesis/Antithesis* (tercets) -> *Sonnet Key / Epigrammatic punchline* (final line).
   - Ukrainian master tradition: Mykola Zerov, Maksym Rylsky, Yuriy Klen, Dmytro Pavlychko.
2. **Rondo / Rondel (Рондо / Рондель)**:
   - Rondo: 13-15 lines on 2 rhymes with refrain (AABBA AAB R AABBA R).
   - Rondel: 13 lines with refrain repeats on lines 1-2, 7-8, 13.
3. **Triolet (Тріолет)**:
   - 8-line stanza on 2 rhymes: `ABaAabAB` (lines 1, 4, 7 identical; lines 2, 8 identical).
4. **Terza Rima (Терцини)**:
   - 3-line stanzas with interlocking chain rhyme: `aba bcb cdc ... yzy z`. (e.g. Franko's *«Мойсей»* prologue).
5. **Rubaiyat (Рубаї)**:
   - 4-line stanzas with `aaba` (or `aaaa`) scheme, philosophical closure (Dmytro Pavlychko's Ukrainian rubai tradition).

---

## 3. Deep Audit: Stress, Accentuation & Phonetic Euphony

### 3.1 Ukrainian Mobile Stress Mechanics (Рухомий і розрізнювальний наголос)

Ukrainian has free, mobile, and distinctive dynamic stress. When paradigms inflect, stress shifts systematically. LLMs routinely stumble here because their tokenizers segment Ukrainian words into sub-word tokens without phonological stress tracking.

#### Major Paradigmatic Stress Shifts in Ukrainian
- **Nouns**:
  * *рукА* (nom. sg.) -> *рУку* (acc. sg.) -> *рУки* (nom. pl.) -> *рукАми* (inst. pl.)
  * *вікнО* -> *вІкна* (nom. pl.) -> *вІкон* (gen. pl.)
  * *землЯ* -> *зЕмлю* -> *зЕмлі* -> *землЯх*
  * *головА* -> *гОлову* -> *гОлови* -> *головАм*
- **Verbs**:
  * *ходИти* -> *ходжУ* -> *хОдиш* -> *хОдять*
  * *вестИ* -> *ведУ* -> *ведЕш* -> *велИ* -> *велА*
  * *берегтИ* -> *бережУ* -> *бережЕш* -> *берЕгти* (archaic)
- **Adjectives & Participles**:
  * *новИй*, *старИй*, *легкИй*, *тяжкИй*, *яснИй*, *малИй*, *босИй* (stress on ending in nominative masculine!).
  * *жадАний*, *нездолАнний*, *несказАнний*, *невпізнАнний* (stressed on penultimate suffix `-Анн-`).

### 3.2 Catalog of Frequent LLM Stress Hallucinations (Russianisms & Misaccentuations)

When generating Ukrainian syllabo-tonic verse, models frequently misplace accents to fit meters, transferring Russian stress patterns. 

| Word | Correct Ukrainian Stress | Incorrect LLM Stress (Hallucination/Calque) | Grammatical Category |
| :--- | :--- | :--- | :--- |
| **випадок** | **вИпадок** | *випАдок* (calque from RU *слу́чай/вы́падок*) | Noun |
| **чорнозем** | **чорнОзем** | *чорнозЕм* (calque from RU *чернозём*) | Noun |
| **одинадцять** | **одИннадцять** | *одиннАдцять* | Numeral |
| **чотирнадцять** | **чотирнАдцять** | *чотирнадцЯть* | Numeral |
| **листопад** | **листопАд** | *листОпад* | Noun |
| **рукопис** | **рукОпис** | *рукопИс* | Noun |
| **довідник** | **довІдник** | *довіднИк* | Noun |
| **фартУх** | **фартУх** | *фАртух* | Noun |
| **ненависть** | **ненАвисть** | *ненавИсть* | Noun |
| **ненавидіти** | **ненАвидіти** | *ненавидІти* | Verb |
| **новий** | **новИй** | *нОвий* | Adjective |
| **старий** | **старИй** | *стАрий* | Adjective |
| **босий** | **бОсий** | *босИй* | Adjective |
| **пізнання** | **пізнАння** | *пізнаннЯ* | Verbal Noun |
| **читання** | **читАння** | *читаннЯ* | Verbal Noun |
| **завдання** | **завдАння** | *завданнЯ* | Verbal Noun |
| **нести / везти** | **нестИ, везтИ** | *нЕсти, вЕзти* | Infinitive |
| **принести** | **принестИ** | *принЕсти* | Infinitive |
| **перепис** | **перЕпис** | *перепИс* | Noun |
| **вирок** | **вИрок** | *вирОк* | Noun |

### 3.3 Dual/Double Accents in Ukrainian Literary Norm (Подвійний наголос)

Ukrainian orthoepy permits double accents for specific words. Models can legitimately leverage these for metric flexibility:
- *зАвжди́* (*зАвжди* and *завждИ*)
- *пОми́лка* (*пОмилка* and *помИлка*)
- *правдИ́вий* (*прАвдивий* and *правдИвий*)
- *веснЯ́ни́й* (*веснЯний* and *веснянИй*)
- *первІ́сний* (*пЕрвісний* and *первІсний*)
- *тА́ко́ж* / *тА́кже́*
- *мА́бУ́ть*
- *прО́сти́й*
- *свІ́та́нок* (colloquial/poetic)

### 3.4 Homographs and Distinctive Stress (Омографи / Розрізнювальний наголос)

Words spelled identically whose meaning and syntactic function depend entirely on stress:
- **зАмок** (palace/fortress) vs **замОк** (door lock / mechanism)
- **нАголос** (phonetic stress mark) vs **наголОс** (emphatic priority)
- **бІлизна** (whiteness, snow-like glare) vs **білизнА** (clothing, underwear, linens)
- **атлАс** (silk fabric) vs **Атлас** (geographical book)
- **оргАн** (musical pipe instrument) vs **Орган** (biological organ / administrative body)
- **плАчу** (1st pers. pres. of *плакати* — I weep) vs **плачУ** (1st pers. pres. of *платити* — I pay)
- **дорОга** (noun: path, street) vs **дорогА** (fem. adj.: expensive, precious)
- **мУка** (torment, suffering) vs **мукА** (ground grain/flour)
- **обрАзи** (nom. pl. of *образа* — insults, offenses) vs **Образи** (nom. pl. of *образ* — holy icons, artistic images)
- **кОлос** (individual ear of wheat) vs **колОс** (giant colossus)
- **потягтИся** (stretch) vs **пОтЯг** (train)

### 3.5 Phonetic Euphony & Syllabic Scansion (Закони милозвучності)

In Ukrainian poetry, phonetic alternation rules (**милозвучність**) directly govern syllable counts, rhythm, and acoustic flow:
1. **Alternation of `У` / `В`**:
   - Between consonants: *«шумів у лісі»* (adds syllable `у`) vs *«вітер в лісі»* (metric synizesis/elision if `в` is non-syllabic).
   - After vowels before consonants: *«жила в селі»* (1 syllable less than *«жила у селі»*).
   - Avoiding hiatus (зяяння — adjacent vowels): *«прийшла ввечері»* vs *«прийшла у вечері»*.
2. **Alternation of `І` / `Й`**:
   - `І` is a full syllable; `Й` is a non-syllabic glide (`[j]`).
   - *«сонце і місяць»* (+1 syllable) vs *«сонце й місяць»* (retains meter).
3. **Prepositional Alternations (`З` / `ІЗ` / `ЗІ` / `ЗО`)**:
   - *«зі скелі»*, *«із шовку»*, *«зо два дні»*.
4. **Jotated Vowels and Apostrophe Scansion**:
   - Soft sign (`ь`) and apostrophe (`'`) never create a syllable (*мідь* = 1 syl, *в'юн* = 1 syl).
   - Jotated vowels (`я, ю, є, ї`) represent **2 phonemes** (`[j] + vowel`) after vowels, apostrophes, or word-initially, creating rich sonic resonance, but only **1 phoneme** (`softening + vowel`) after paired consonants.

---

## 4. Deep Audit: Rhyme Typology, Quality & Anti-Banal Guardrails

### 4.1 Exhaustive Rhyme Classification for Ukrainian Poetry

Current skill files (`SKILL.md:93-100`, `references/full-guide.md:201-226`) state that rhymes should be "sound plus meaning" and divide them simply into `exact` vs `approximate`. This lacks the necessary granularity to guide model generation.

```
                         UKRAINIAN RHYME TAXONOMY
                                    │
    ┌───────────────────────────────┼──────────────────────────────┐
    ▼                               ▼                              ▼
By Stress Position          By Sonic Precision             By Morphological Structure
- Masculine (Чоловіча)      - Exact (Точна)                - Homogeneous / Grammatical
- Feminine (Жіноча)         - Approximate (Неточна):         (Однорідна / Граматична)
- Dactylic (Дактилічна)       * Assonance (Асонансна)        * Verb-Verb (Дієслівна)
- Hyperdactylic               * Dissonance (Дисонансна)      * Adj-Adj (Прикметникова)
  (Гіпердактилічна)           * Truncated (Усічена)          * Suffixal Diminutive
                              * Jotated (Йотована)             (Зменшувальна)
                                                           - Heterogeneous / Cross-Grammar
                                                             (Різнорідна / Неоднорідна)
                                                             * Verb + Noun
                                                             * Noun + Adverb
                                                             * Adj + Pronoun
```

#### Detailed Breakdown of Sonic Precision (За точністю співзвуччя)
1. **Exact Rhymes (Точні рими)**:
   - Full identity of stressed vowel and all subsequent consonants/vowels: *крило́ — село́*, *ти́ша — колиш* (approximate), *дзвін — він*.
2. **Assonance Rhymes (Асонансні рими)**:
   - Stressed vowels match exactly; consonants differ but share acoustic affinity (sonorants, labials):
   - *води́ — сади́* (exact), *но́чі — о́чі* (exact), *те́плий — ве́лет* (assonance), *рука́ — вода́* (assonance), *хма́ра — кана́ва* (assonance).
   - Widely celebrated in Ukrainian modernism (Antonych, Rylsky, Kostenko).
3. **Dissonance / Consonance Rhymes (Дисонансні / Консонансні рими)**:
   - Consonant framework matches; vowels differ:
   - *дзво́ни — ди́вно*, *кві́тка — клі́тка*, *бу́ти — би́ти*.
4. **Truncated Rhymes (Усічені рими)**:
   - One rhyme word has a final consonant omitted in the partner:
   - *ти́ша — ди́шеш*, *сло́во — умо́в*.
5. **Jotated / Sonorant Approximations (Йотовані / Сонорні співзвуччя)**:
   - *земля́ — зоря́*, *ві́тер — сві́тить*, *ве́чір — пле́чі*.

### 4.2 Morphological Structure: Grammatical vs Heterogeneous Rhymes

#### The Flaw of Grammatical Rhymes (Граматичні / Однорідні рими)
LLMs default heavily to grammatical rhyming because matching morphological suffixes are high-probability completions. In Ukrainian, these create a cheap, sing-song, amateurish acoustic:
- **Verb + Verb**: *зна́ти — коха́ти*, *прийшла́ — розцвіла́*, *летя́ть — горя́ть*, *зрозумі́в — зумів*.
- **Noun + Noun in identical case**: *карти́на — стежи́на*, *життя́ — буття́*, *доли́ні — хвили́ні*, *ноча́ми — сльоза́ми*.
- **Adjective + Adjective**: *ясни́й — рясни́й*, *золота́ — молода́*, *холо́дні — голо́дні*.
- **Diminutive + Diminutive**: *кві́точка — зі́рочка*, *стежи́ночка — крапли́ночка*, *серде́нько — миле́нько*.

#### The Quality Standard: Heterogeneous Rhymes (Різнорідні рими)
Skill instructions should explicitly mandate **heterogeneous (різнорідні)** rhyming where words belong to different parts of speech or have different root structures:
- **Verb + Noun**: *сві́тить — ві́тер*, *зна́ю — кра́ю*, *мовча́ти — но́чі*, *гори́ть — мить*.
- **Noun + Adverb**: *мо́ву — зно́ву*, *стіна́ — сповна́*, *рука́ — здалека́*.
- **Adjective + Noun/Pronoun**: *те́мно — даре́мно*, *про́стий — го́сті*, *живи́й — ти*.
- **Compound Rhymes (Складені рими)**: *де́ ти — пое́ти*, *до ра́нку — на ґа́нку*, *сто лі́т — столі́ть*.

### 4.3 Rhyme Lexical Richness & Cliché Blacklist

#### Rich Rhymes (Багаті рими) with Pre-Tonic Supporting Consonants (Опорні приголосні)
- The consonant *preceding* the stressed vowel matches, elevating acoustic fullness:
- *т**р**ава́ — т**р**ива́*, *к**р**и́ло — вк**р**и́ло*, *п**л**о́мінь — п**р**о́мінь*, *д**з**ві́н — на**з**дігі́н*.

#### Comprehensive Banal Rhyme Blacklist (Тавтологічні та банальні пари)
The skill must explicitly ban these predictable, worn-out pairs:
```text
любов — кров            доля — воля             серце — перце
день — пень             ніч — очі / віч-на-віч  зорі — морі
жаль — печаль           квіти — діти            вік — чоловік
молодий — золотий       жити — любити           чути — бути
сльози — морози         очі — дівочі            вітер — квіти
хмара — пара            осінь — просинь         тиша — колише
```

---

## 5. Deep Audit: Linguistic Registers, Anti-Cliche & Anti-Sharovarshchyna

### 5.1 Authentic Register Taxonomy for Ukrainian Poetry

Current files support generic labels: `розмовний`, `нейтральний`, `піднесений`, `народнопісенний`, `церемоніальний`. This is insufficient to capture the historical and modern range of Ukrainian poetry.

```
                           UKRAINIAN POETIC REGISTERS
                                        │
    ┌────────────────┬──────────────────┼─────────────────┬────────────────┐
    ▼                ▼                  ▼                 ▼                ▼
Contemporary     Chamber &          Philosophical &    Baroque &       Authentic Folk
Urban            Intimate Lyric     Neoclassical       Old Cossack     (Anti-Kitsch)
(Сучасний        (Камерно-інтимний, (Медитативний,     (Бароковий,     (Автентичний
 урбаністичний)   тиха лірика)       неокласичний)      старокозацький) фольклорний)
```

1. **`contemporary-urban` (Сучасний урбаністичний)**:
   - Diction: Living Ukrainian spoken in contemporary cities (Kyiv, Lviv, Kharkiv, Odesa, Dnipro). Natural syntax, anglicisms where organic, post-industrial imagery (concrete, asphalt, railway tracks, balconies, telegram channels, night air sirens).
   - Traditions: Serhiy Zhadan, Yuriy Andrukhovych, Yuri Izdryk, Kateryna Kalytko, Halyna Kruk.
2. **`chamber-intimate` (Камерно-інтимний / Тиха лірика)**:
   - Diction: Minimalist, domestic, sensory, whispered. Psychological nuance without theatrical pathos.
   - Traditions: Maksym Rylsky, Mykola Vinhranovsky, Leonid Kyselov, Vasyl Holoborodko, Iryna Zhylenko.
3. **`philosophical-neoclassical` (Медитативно-філософський / Неокласичний)**:
   - Diction: High intellectual density, rich antique/mythological subtext, impeccable metric discipline, sculptural imagery.
   - Traditions: Mykola Zerov, Maksym Rylsky (*«Київські неокласики»*), Vasyl Stus, Volodymyr Svidzinsky, Mykola Bazhan.
4. **`baroque-cossack` (Бароковий / Старокозацький / Герметичний)**:
   - Diction: Authentic Early Modern Ukrainian (16th–18th c.). Dignified archaic vocabulary used purposefully (*днесь, воістину, суєта, глас, перст, ректи, посполиті, корогва, клейноди, сагайдак, звитяга, ратище*).
   - Traditions: Hryhoriy Skovoroda, Ivan Mazepa, Taras Shevchenko (historical poems), Bohdan-Ihor Antonych (*«Ротації»*), Valeriy Shevchuk.
5. **`folk-authentic` (Автентичний фольклорний / Обрядовий)**:
   - Diction: Archaic ritual depth (колядки, щедрівки, купальські, веснянки, голосіння, замовляння, балади). Mythological animism (ліс, вода, земля, жито, роса).
   - Strict avoidance of stage-kitsch.
6. **`children-playful` (Дитячий ігровий)**:
   - Diction: Alliterative tongue-twisters (скоромовки), joyful onomatopoeia, clear rhythmic bouncing, humorous absurdity without condescension.
   - Traditions: Hryhoriy Falkovych, Ivan Malkovych, Roman Skiba, Sashko Dermansky.

### 5.2 The Anti-Sharovarshchyna Guardrail (Антишароварщина)

**Sharovarshchyna (Шароварщина)** is the reduction of complex Ukrainian culture to primitive, Soviet-era folkloric caricature: plastic flowers, exaggerated satin trousers (*шаровари*), mechanical consumption of *сало* and *горілка*, mindless repetition of *«гопак»*, *«калина-малина»*, *«соловейко в лузі»*, *«струнка тополя»*, *«козак гуляє»*.

#### Mandatory Guardrail Directives
- **Direct Ban**: Forbid using folkloric markers as decorative stickers without ontological or dramatic purpose.
- **Rooted Authenticity**: If botanical or folk symbols appear (*калина*, *верба*, *полин*, *чорнобривці*), they must be rooted in tactile reality, seasonal biology, grief, ritual, or personal memory, rather than automated pastoral wallpaper.
- **De-idealization**: Avoid portraying Cossack or rural life as a cartoonish festival. Ground historical motifs in fatigue, cold, horse sweat, iron, soil, and historical tragedy.

### 5.3 Russianisms, Surzhyk & Calques Detection Catalog (Антисуржик і кальки)

LLMs trained on bilingual corpora often produce calqued syntactic constructs and false friends.

```
┌──────────────────────────────────────┬──────────────────────────────────────────┐
│ ❌ Calqued / Russianized Formulation │ ✅ Authentic Ukrainian Poetic Equivalent  │
├──────────────────────────────────────┼──────────────────────────────────────────┤
│ по вечорах                          │ вечорами / щовечора                      │
│ на протязі (часу)                   │ протягом / упродовж                      │
│ у кінці кінців                      │ зрештою / кінець кінцем                  │
│ приймати участь                     │ брати участь                             │
│ по крайній мірі                     │ принаймні                                │
│ влучний вистріл                     │ влучний постріл                          │
│ під відкритим небом                 │ просто неба                              │
│ закрити очі                         │ заплющити очі                            │
│ відкрити вікно                      │ відчинити вікно                          │
│ відкрити книгу                      │ розгорнути книгу                         │
│ потерпіти поразку                   │ зазнати поразки                          │
│ являється (в значенні "є")          │ є / постає                               │
│ кидатися в очі                      │ впадати в очі / упадати в око            │
│ в обнімку                           │ обійнявшись / в обіймах                  │
│ нанести удар                        │ завдати удару                            │
│ роковий                             │ фатальний / доленосний                   │
│ луна (в значенні "місяць")          │ місяць (укр. "луна" = echo!)             │
│ міроприємство                       │ захід / подія                            │
│ любий (в значенні "будь-який")      │ будь-який / кожен (укр. "любий" = dear)  │
└──────────────────────────────────────┴──────────────────────────────────────────┘
```

#### Authentic Idiomatic Lexicon Enrichment
Encourage the model to draw upon vivid, native Ukrainian adverbial and sensory constructions:
* *горілиць* (face up), *долілиць* (face down), *наосліп* (blindly), *потайки* (secretly), *мигцем* (in a flash), *навпочіпки* (squatting), *знетяма* (frenzy/oblivion), *навзнак* (on one's back), *сторч* (upright/headlong), *вочевидь* (evidently), *подекуди* (here and there), *чимдуж* (as fast as possible).

---

## 6. Deep Audit: Input Templates, Parameter Taxonomy & Evaluation Rubrics

### 6.1 Parameter Taxonomy Deficiencies in `input-templates.md`

`input-templates.md` currently provides:
```text
topic, mood, mode, length, rhyme, meter, register, image_density, ending_strength, additional constraints
```

#### Missing Essential Parameters
1. **`form`**:
   - Values: `free | sonnet | blank-verse | rondo | triolet | terza-rima | rubai | kolomyika | haiku | limerick | astrophic`
   - *Why*: A user wanting a Sonnet currently has to cram it into `additional constraints`, with no guarantee the model applies correct 14-line octave/sestet turning point rules.
2. **`clausula`**:
   - Values: `alternating-fm (ЖЧЖЧ) | masculine (ЧЧ) | feminine (ЖЖ) | dactylic (Д) | free`
   - *Why*: Essential for musical/strophic control.
3. **`stanza_type`**:
   - Values: `couplets (дистих) | tercets (терцет) | quatrains (катрен) | cinquains (п'ятивірш) | sestets (секстина) | octaves (октава) | astrophic (суцільний)`
4. **`subgenre`**:
   - Values: `lyric-poem | elegy (елегія) | ballad (балада) | ode (ода) | epigram (епіграма) | idyll (ідилія) | duma (дума) | romance-lyrics (романс) | spoken-word`

### 6.2 Rubric Gaps in `references/rubric.md`

The existing 100-point rubric allocates points as follows:
- 1. Природність української мови — 25
- 2. Образність і конкретика — 20
- 3. Ритм і рядкоподіл — 15
- 4. Рима і звукова організація — 10
- 5. Цілісність тону і режиму — 10
- 6. Сила фіналу — 10
- 7. Антиштампи — 10

#### Analytical Critique & Critical Gaps
1. **No Explicit Penalty for Metric Failure**: If a user requests an Iambic Pentameter and the model produces lines with 9, 12, 8, and 11 syllables with broken stress, it only loses a few points in the 15-point "Ритм" bucket. There is no hard disqualification or deduction for broken meter under strict formal requests.
2. **Conflation of Language & Accentuation**: Stress distortions (*випАдок*, *чорнозЕм*) are lost inside the 25-point language score rather than being flagged as prosodic flaws.
3. **Lack of Anti-Sharovarshchyna Scoring**: Pseudo-folk kitsch is vaguely judged under "Антиштампи" (10 pts), allowing kitsch poems to score 85+ if their syntax is technically clean.
4. **No Scansion Verification Guidance**: The rubric does not provide human evaluators or automated evaluators with a scansion checklist (counting stresses, checking clausulae, scanning ictuses).

### 6.3 Test Suites Analysis (`tests.md` and `stress-tests.md`)

#### Coverage Matrix
| Test Domain | Existing Coverage (`tests.md` + `stress-tests.md`) | Missing Critical Test Scenarios |
| :--- | :--- | :--- |
| **Syllabo-tonic Meters** | Iamb, Amphibrach (Tests 10, 11) | **Dactyl**, **Anapest**, strict **Blank Verse** pentameter |
| **Non-classical Verse** | Free-verse (Tests 2, 4, 10) | **Dolnik**, **Taktovik**, **Kolomyika**, **Accentual recitative** |
| **Fixed Forms** | None | **Sonnet** (with volta), **Triolet**, **Terza rima** |
| **Accentuation & Homographs** | None | Stress homographs (*зАмок/замОк*, *нАголос/наголОс*), high-risk accentuation (*вИпадок*, *листопАд*) |
| **Registers** | Children, Patriotic, Ironic, Folk-tint | **Contemporary Urban Slang**, **Baroque 17th c.**, **Philosophical Neoclassical**, **High Elegy** |
| **Anti-Kitsch** | General cliché bans (words: душа, серце) | Explicit **Anti-Sharovarshchyna stress test** (ban on *калина/гопак/шаровари* kitsch) |
| **Phonetic Euphony** | General calque test | Strict **Euphony stress test** (dense consonant clusters, strict U/V, I/Y alternating rules) |

---

## 7. Architectural & File Synchronization Audit

### 7.1 Multi-File Redundancy & Desynchronization Risks

The repository currently maintains multiple near-duplicate copies of poetry skills:
1. Canonical modular folder: `skills/ukrainian-poetry/` (contains `SKILL.md`, `references/full-guide.md`, `references/input-templates.md`, `references/rubric.md`, `references/stress-tests.md`, `references/tests.md`).
2. Root mirror files:
   - `ukrainian-poetry-skill.md` (Full English single-file version, 433 lines)
   - `ukrainian-poetry-skill-uk.md` (Full Ukrainian single-file version, 433 lines)
   - `ukrainian-poetry-skill-lite.md` (Compact Ukrainian version, 83 lines)
   - `ukrainian-poetry-skill-input-template.md`, `ukrainian-poetry-skill-rubric.md`, `ukrainian-poetry-skill-stress-pack.md`, `ukrainian-poetry-skill-tests.md` (Identical mirrors of `skills/ukrainian-poetry/references/*`)
3. Legacy archive: `source/legacy-skills/ukrainian-poetry.md` (514 lines).

#### Risk Assessment
- `skills/ukrainian-poetry/SKILL.md` is the canonical entry point for AI agents (frontmatter format).
- Any upgrade made to `skills/ukrainian-poetry/` must be synchronized to the root-level source docs and lite versions to prevent drift.

---

## 8. Prioritized Roadmap & Actionable Enhancement Specs

To elevate the Ukrainian Poetry skill to professional literary quality, the following upgrades are recommended for implementation:

### Priority 1: Core SKILL.md and Full Guide Upgrades
1. **Expand Prosodic Taxonomy**:
   - Add Dactyl to ternary meter rules.
   - Introduce operational rules for **Dolnik (дольник)**, **Taktovik (тактовик)**, and **Kolomyika meter (коломийковий вірш: 4+4+6)**.
   - Codify **Blank Verse (білий вірш)** alongside Free Verse.
2. **Integrate Clausula Disciplines**:
   - Mandate conscious alternation of feminine and masculine clausulae (`ЖЧЖЧ`, `ЧЖЧЖ`).
3. **Embed Accentuation & Homograph Guardrails**:
   - Include a dedicated phonetic section with high-risk Ukrainian accent patterns, double accents, and stress homographs.
   - Provide an internal self-check protocol using capitalized vowels (e.g. `вИпадок`, `новИй`) or acute marks during draft scansion.
4. **Codify Heterogeneous Rhymes & Ban Banal Clichés**:
   - Explicitly instruct the model to prefer **cross-grammatical rhymes (різнорідні)** and **rich pre-tonic rhymes (багаті опорні)** over same-part-of-speech suffix matching.
   - Formalize the banal rhyme blacklist (*любов-кров*, *день-пень*, *-очка/-ечка*).
5. **Add Anti-Sharovarshchyna & Anti-Calque Guardrails**:
   - Add explicit prohibitions against rustic pseudo-folk kitsch.
   - Embed the Ukrainian calque correction table into reference materials.

### Priority 2: Reference & Template Expansions
1. **Update `input-templates.md`**:
   - Add `form` (sonnet, blank-verse, kolomyika, rondo, etc.), `clausula`, `stanza_type`, and `subgenre`.
2. **Refine `rubric.md`**:
   - Add explicit metric penalty points for rhythmic stumbles and stress hallucinations.
   - Add a dedicated Anti-Sharovarshchyna / Authentic Register score.
   - Provide a scansion verification protocol for evaluators.
3. **Expand `tests.md` and `stress-tests.md`**:
   - Add Test 22: *Neoclassical Sonnet with strict volta and Petrarchan rhyme scheme*.
   - Add Test 23: *Dolnik / Rock lyric with 3-stress lines*.
   - Add Test 24: *Authentic Kolomyika folk meter (14-syllable 4+4+6)*.
   - Add Test 25: *Blank Verse dramatic monologue (unrhymed iambic pentameter)*.
   - Add Test 26: *Homograph and High-Risk Accentuation Stress Test*.
   - Add Test 27: *Anti-Sharovarshchyna Baroque/Cossack Historical Register Test*.

---

*Report compiled by Explorer 1 (Ukrainian Poetic & Linguistic Specialization).*

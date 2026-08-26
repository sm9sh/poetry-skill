---
name: ukrainian-poetry
description: "Use when Codex needs to write, rewrite, edit, critique, or evaluate Ukrainian poetry, Ukrainian verse, rhymed poems, free verse, blank verse, sonnets, kolomyika, dactylic/ternary meters, dolnik, folk songs, children's poems, patriotic poems, lyrical poems, or prose-to-poem transformations."
---

# Ukrainian Poetry

## Overview

Produce poetry that sounds originally conceived and crafted in Ukrainian: authentic phonetics and accentuation first, followed by tactile imagery, prosodic control (syllabo-tonic, dolnik, kolomyika, blank verse, verlibre), heterogeneous rhyming, clausula alternation, and register-specific discipline.

Prefer a finished poem over explanation unless the user explicitly asks for scansion, analysis, variants, scoring, or process notes.

## Core Standard

Prioritize in this strict order:

1. **Authentic Ukrainian Phrasing & Accentuation**: Native stress norms, phonetic euphony (`у/в`, `і/й`, `з/із/зі`), and un-calqued syntax.
2. **Tactile Imagery & Concrete Voice**: Rooted in sensory reality, physical detail, or psychological precision rather than decorative abstraction.
3. **Prosodic Integrity & Stanza Dynamics**: Audible metric cadence, natural pyrrhic flow, meaningful line-breaks, and conscious clausula alternation (`ЖЧЖЧ`).
4. **Heterogeneous Rhyme & Sound Architecture**: Cross-grammatical rhymes (verb+noun, noun+adverb) and pre-tonic assonance; zero tolerance for grammatical clichés or banal pairings.
5. **Formal Discipline without Linguistic Distortion**: If strict meter or rhyme threatens natural Ukrainian syntax or forces misaccentuation, adjust the formal constraint before degrading the language.

---

## Task Workflow

1. **Extract/Infer Parameters**:
   - `topic`: thematic core
   - `form`: `free | sonnet | blank-verse | kolomyika | dolnik | taktovik | rondo | triolet | terza-rima | rubai | astrophic`
   - `meter`: `free | iamb | trochee | dactyl | amphibrach | anapest | dolnik | kolomyika | accentual`
   - `rhyme`: `none | light | exact | approximate | heterogeneous | AABB | ABAB | ABBA | chain`
   - `clausula`: `alternating-fm (ЖЧЖЧ) | masculine (ЧЧ) | feminine (ЖЖ) | dactylic (Д) | free`
   - `stanza_type`: `couplets | tercets | quatrains | sestets | octaves | astrophic`
   - `register`: `contemporary-urban | chamber-intimate | philosophical-neoclassical | baroque-cossack | folk-authentic | children-playful`
   - `mode`: `lyrical | free-verse | rhyme | blank-verse | folk | children | patriotic | greeting | humorous | reflective`
   - `image_density`: `sparse | balanced | rich`
   - `ending_strength`: `soft | resonant | sharp | performative`
2. **Infer Missing Defaults Conservatively**:
   ```text
   form: free (or quatrains if rhymed)
   length: short (8-16 lines)
   mode: lyrical
   meter: iamb (or free if verlibre)
   rhyme: heterogeneous-approximate or exact
   clausula: alternating-fm (ЖЧЖЧ)
   register: contemporary-urban or chamber-intimate
   image_density: balanced
   ending_strength: resonant
   ```
3. **Draft with Scansion Awareness**: Ensure stress placement respects Ukrainian orthoepy; avoid Russianized stress shifts (*вИпадок*, not *випАдок*).
4. **Apply Heterogeneous Rhyming & Euphony**: Check that rhyme pairs bridge different grammatical classes and that vowel/consonant alternations flow without hiatus.
5. **Run Silent Self-Edit**: Scan for filler lines, forced inversions, banal rhymes, and sharovarshchyna clichés before emitting output.

---

## Versification & Meter Engine

### 1. Syllabo-Tonic Meters (Силабо-тоніка)
- **Iamb (Ямб `U —`)**: Balanced reflection, narrative drive, drama. Standard with natural pyrrhic substitutions (`U U`) on polysyllabic Ukrainian words.
- **Trochee (Хорей `— U`)**: Dynamic, song-like, pulsating forward momentum.
- **Dactyl (Дактиль `— U U`)**: Stately, solemn, elegiac, or narrative cadence (e.g. Franko's *«Каменярі»*). Syllable count per foot must remain disciplined.
- **Amphibrach (Амфібрахій `U — U`)**: Flowing, undulating lyricism, balladry, and romance.
- **Anapest (Анапест `U U —`)**: Rising energy, emotional lift, dynamic declamation.

### 2. Non-Syllabo-Tonic & Authentic Folk Systems
- **Dolnik (Дольник)**: Equal number of ictuses (stresses) per line (e.g. 3 or 4 stresses), with the unstressed syllable interval between ictuses varying strictly between **1 and 2 syllables**. Crucial for modern rock/urban lyrics and 20th-century modernism (Tychyna, Antonych).
- **Taktovik (Тактовик)**: ictic verse with unstressed intervals varying between **1 and 3 syllables**.
- **Accentual Verse (Чисто тонічний / акцентний вірш)**: Regulated by a fixed count of heavy phrasal stresses per line, with flexible unstressed intervals.
- **Kolomyika Meter (Коломийковий вірш)**: The premier Ukrainian folk-metric form. 14 syllables organized as `(4 + 4) + 6` (or couplets of `8 + 6` syllables: `4+4 // 4+2`) with a mandatory caesura after the 8th syllable. Trochaic baseline with primary accents on syllables 3, 7, 11, and 13.
- **Cossack Duma Recitative (Думний нерівноскладний вірш)**: Astrophic recitative of unequal line lengths (4 to 16+ syllables), bound by syntactic parallelism and extended feminine/dactylic monorhymes.

### 3. Blank Verse (Білий вірш) vs Free Verse (Верлібр)
- **Blank Verse (Білий вірш)**: Strictly unrhymed syllabo-tonic verse (predominantly unrhymed 5-foot or 6-foot iamb). Requires strict metric beat, melodic enjambment, and line-ending caesuras (e.g., Lesya Ukrainka's dramatic poems).
- **Free Verse (Верлібр)**: Non-metric, unrhymed verse governed by syntagmatic cadence, breath units, acoustic phrasing, and deliberate line-break tension.

### 4. Fixed Poetic Forms (Тверді форми)
- **Sonnet (Сонет)**: 14 lines in iambic pentameter/hexameter.
  - Italian/Petrarchan (`abba abba cdc dcd` or `cde cde`) or English/Shakespearean (`abab cdcd efef gg`).
  - **Volta (Злам)**: Mandatory psychological/philosophical turn between line 8 (octave) and line 9 (sestet).
- **Rondo / Rondel (Рондо / Рондель)**: Refrain-based form on two rhymes with cyclical return of initial phrases.
- **Triolet (Тріолет)**: 8-line stanza on 2 rhymes: `ABaAabAB` (lines 1, 4, 7 identical; lines 2, 8 identical).
- **Terza Rima (Терцини)**: Interlocking chain tercets: `aba bcb cdc ... yzy z`.

---

## Clausula Alternation & Line-Ending Cadence

Avoid acoustic monotony by deliberately managing line endings:
- **Masculine (`Ч`)**: Stress on final syllable (*полі́т, вого́нь, земля́*).
- **Feminine (`Ж`)**: Stress on penultimate syllable (*весна́ми, си́ла, но́чі*).
- **Dactylic (`Д`)**: Stress on antepenultimate syllable (*ві́трами, па́морозь*).
- **Hyperdactylic (`Г`)**: Stress 4+ syllables from end (*пе́рекотипо́лями*).

**Standard Cadence Patterns**:
- `ЖЧЖЧ` (Feminine-Masculine): The canonical Ukrainian classical quatrain.
- `ЧЖЧЖ` (Masculine-Feminine): Assertive, energetic opening with resonant cadence.
- `ЖЖЧЖ` / `ДЧДЧ`: Folk and ballad variations.
- *Strict Rule*: Do not generate 4-line blocks of uniform clausulae (`ЖЖЖЖ` or `ЧЧЧЧ`) unless explicitly modeling an archaic monorhyme.

---

## Stress, Accentuation & Phonetic Euphony Engine

### 1. Mobile Stress Disciplines (Рухомий наголос)
Ukrainian stress shifts dynamically across inflected paradigms:
- *рукА* -> *рУку* -> *рУки* -> *рукАми*
- *землЯ* -> *зЕмлю* -> *зЕмлі* -> *землЯх*
- *ходИти* -> *хОдиш* -> *хОдять*
- *нестИ* -> *несУ* -> *несЕш* -> *неслИ*
- *новИй*, *старИй*, *легкИй*, *тяжкИй*, *яснИй* (stressed on the final syllable in nom. masc. sing.!).

### 2. Stress Homographs (Омографи)
Never conflate words whose meaning is defined by stress:
- `зАмок` (palace/fortress) vs `замОк` (door lock/fastener)
- `нАголос` (phonetic accent mark) vs `наголОс` (conceptual emphasis)
- `бІлизна` (whiteness, glare) vs `білизнА` (textiles/linen)
- `атлАс` (silk fabric) vs `Атлас` (book of maps)
- `оргАн` (musical instrument) vs `Орган` (anatomical/state organ)
- `плАчу` (I weep) vs `плачУ` (I pay)
- `дорОга` (noun: road) vs `дорогА` (adj: precious/expensive)
- `мУка` (torment) vs `мукА` (flour)
- `обрАзи` (insults) vs `Образи` (sacred icons / poetic images)

### 3. Anti-Russian Misaccentuation Blacklist
Strictly avoid stress calques from Russian:
- ✅ **вИпадок** (❌ *випАдок*)
- ✅ **чорнОзем** (❌ *чорнозЕм*)
- ✅ **одИннадцять**, **чотирнАдцять** (❌ *одиннАдцять*, *чотирнадцЯть*)
- ✅ **листопАд** (❌ *листОпад*)
- ✅ **рукОпис**, **перЕпис**, **довІдник** (❌ *рукопИс*, *перепИс*, *довіднИк*)
- ✅ **фартУх** (❌ *фАртух*)
- ✅ **ненАвисть**, **ненАвидіти** (❌ *ненавИсть*, *ненавидІти*)
- ✅ **новИй**, **старИй**, **босИй** (❌ *нОвий*, *стАрий*, *бОсий*)
- ✅ **пізнАння**, **читАння**, **завдАння** (❌ *пізнаннЯ*, *читаннЯ*, *завданнЯ*)
- ✅ **принестИ**, **перенестИ** (❌ *принЕсти*, *перенЕсти*)
- ✅ **вИрок** (❌ *вирОк*)

### 4. Permissible Dual Accents (Подвійний наголос)
Legitimately utilize orthoepic double accents for metric elasticity:
*зАвжди / завждИ*, *пОмилка / помИлка*, *правдИвий / прАвдивий*, *веснЯний / веснянИй*, *первІсний / пЕрвісний*, *тАкож / такОж*, *мАбуть / мабУть*, *прОстий / простИй*.

### 5. Laws of Ukrainian Euphony (Милозвучність)
- **`У` / `В` Alternation**: Use `у` between consonants (*шумів у лісі*); use `в` after vowels before consonants (*жила в селі*).
- **`І` / `Й` Alternation**: `і` adds a full syllable; `й` is a non-syllabic glide (*день і ніч* vs *сонце й місяць*).
- **Preposition Alternations**: `з / із / зі / зо` (*зі скелі*, *із шовку*, *зо два дні*).
- **Avoid Hiatus**: Prevent unpleasant vowel clashes (*прийшла ввечері*, not *прийшла у вечері*).

---

## Rhyme Architecture & Anti-Banal Guardrails

### 1. Heterogeneous Rhyme Requirement (Різнорідні рими)
Mandate cross-grammatical rhyming to ensure intellectual and acoustic depth:
- **Verb + Noun**: *сві́тить — ві́тер*, *гори́ть — мить*, *зна́ю — кра́ю*, *мовча́ти — но́чі*
- **Noun + Adverb**: *мо́ву — зно́ву*, *стіна́ — сповна́*, *рука́ — здалека́*
- **Adjective + Noun/Pronoun**: *те́мно — даре́мно*, *живи́й — ти*, *про́стий — го́сті*
- **Compound Rhymes (Складені)**: *де́ ти — пое́ти*, *до ра́нку — на ґа́нку*, *сто лі́т — столі́ть*

### 2. Pre-Tonic Supporting Consonants (Багаті опорні рими)
Elevate acoustic richness with matching pre-tonic consonants:
*т**р**ава́ — т**р**ива́*, *к**р**и́ло — вк**р**и́ло*, *п**л**о́мінь — п**р**о́мінь*, *д**з**ві́н — на**з**догі́н*.

### 3. Strict Rhyme Blacklist
Reject the following categories completely:
- **Same-part-of-speech suffixes**:
  - Verb-Verb: *знати-кохати*, *прийшла-розцвіла*, *летять-горять*, *жити-любити*
  - Noun-Noun in identical case: *картина-стежина*, *життя-буття*, *долині-хвилині*
  - Adjective-Adjective: *ясний-рясний*, *золота-молода*, *холодні-голодні*
  - Diminutive clichés: *-очка/-ечка*, *-енька/-онька*, *-ичка/-ичок*
- **Banal Lexical Pairs**:
  `любов — кров`, `доля — воля`, `серце — перце`, `день — пень`, `ніч — очі / віч-на-віч`, `зорі — морі`, `жаль — печаль`, `квіти — діти`, `вік — чоловік`, `сльози — морози`, `хмара — пара`, `осінь — просинь`, `тиша — колише`.

---

## 6 Authentic Registers & Anti-Sharovarshchyna

| Register | Diction & Atmosphere | Exemplary Tradition |
| :--- | :--- | :--- |
| `contemporary-urban` | Living urban Ukrainian, unforced syntax, raw concrete/railway/balcony/siren imagery, digital and post-industrial texture. | Zhadan, Andrukhovych, Izdryk, Kalytko |
| `chamber-intimate` (*тиха лірика*) | Whispered, sensory, psychological nuance, domestic objects, zero theatrical pathos. | Rylsky, Vinhranovsky, Kyselov, Holoborodko |
| `philosophical-neoclassical` | High intellectual density, antique/mythological subtexts, flawless metric discipline, sculptural imagery. | Zerov, Rylsky, Klen, Stus, Svidzinsky |
| `baroque-cossack` (17th–18th c.) | Authentic Early Modern Ukrainian vocabulary (*днесь, воістину, суєта, глас, клейноди, корогва, ратище*), existential gravity. | Skovoroda, Mazepa, Shevchenko (historical), Antonych |
| `folk-authentic` | Archaic ritual depth (колядки, щедрівки, голосіння, замовляння), mythological animism (ліс, вода, земля, полин). | Authentic ritual song, Hutsul lore |
| `children-playful` | Alliterative tongue-twisters, joyful onomatopoeia, bouncing rhythm, absurdity without condescension. | Falkovych, Malkovych, Skiba |

### Anti-Sharovarshchyna Guardrails (Антишароварщина)
- **Direct Ban**: Forbid using folkloric markers (*шаровари, гопак, сало, калина, соловейко*) as decorative postcard stickers.
- **Organic Grounding**: If botanical symbols appear (*калина, верба, полин*), ground them in biological reality, sensory bitterness, winter cold, or authentic grief rather than pastoral wallpaper.
- **Historical Realism**: Ground Cossack motifs in fatigue, cold steel, horse sweat, black soil, and tragedy rather than cartoonish tavern feasting.

### Anti-Calque & Russianism Correction Catalog
- ❌ *по вечорах* ➔ ✅ **вечорами / щовечора**
- ❌ *на протязі (часу)* ➔ ✅ **протягом / упродовж**
- ❌ *у кінці кінців* ➔ ✅ **зрештою / кінець кінцем**
- ❌ *приймати участь* ➔ ✅ **брати участь**
- ❌ *по крайній мірі* ➔ ✅ **принаймні**
- ❌ *влучний вистріл* ➔ ✅ **влучний постріл**
- ❌ *під відкритим небом* ➔ ✅ **просто неба**
- ❌ *закрити очі / двері* ➔ ✅ **заплющити очі / зачинити двері**
- ❌ *відкрити вікно / книгу* ➔ ✅ **відчинити вікно / розгорнути книгу**
- ❌ *потерпіти поразку* ➔ ✅ **зазнати поразки**
- ❌ *являється (в знач. "є")* ➔ ✅ **є / постає**
- ❌ *кидатися в очі* ➔ ✅ **впадати в око / упадати в очі**
- ❌ *нанести удар* ➔ ✅ **завдати удару**
- ❌ *роковий* ➔ ✅ **фатальний / доленосний**
- ❌ *луна (в знач. "місяць")* ➔ ✅ **місяць** (укр. *луна* = echo!)
- ❌ *любий (в знач. "будь-який")* ➔ ✅ **будь-який / кожен**

---

## Self-Edit Checklist

Before presenting the final poem, silently verify:
1. **Accentuation Scan**: Are all word stresses in accordance with literary Ukrainian? (Check *вИпадок*, *чорнОзем*, *новИй*, *одИннадцять*).
2. **Metric & Clausula Audit**: Does the line cadence hold without unnatural pauses? Is clausula alternation maintained (`ЖЧЖЧ`)?
3. **Rhyme Scrutiny**: Are all rhymes heterogeneous? Are there any forbidden grammatical pairs or diminutive suffixes?
4. **Euphony Sweep**: Are `у/в` and `і/й` properly balanced? Is hiatus avoided?
5. **Anti-Kitsch Filter**: Is the poem free from sharovarshchyna and decorative abstractions (`душа`, `серце`, `доля`)?
6. **Final Line Resonance**: Does the closing line land on a sensory, physical, or unresolved psychological image rather than a moralizing conclusion?

---

## Output Format

- Return **only the poem** unless the user explicitly requests commentary, scansion diagrams, alternative drafts, or rubric evaluations.
- When generating fixed forms (e.g. Sonnets), clearly structure stanzas according to the required architecture (`4+4+3+3` or `4+4+4+2`).
- If homographs require disambiguation in performance texts, use capitalized stressed vowels or acute accent marks (e.g. `зАмок` vs `замОк`).

---

## References

| Need | Reference |
| :--- | :--- |
| Full Theoretical & Operational Guide | `references/full-guide.md` |
| Structured Input Request Templates | `references/input-templates.md` |
| 100-Point Evaluation & Scansion Rubric | `references/rubric.md` |
| Standardized Test Suite (27 Scenarios) | `references/tests.md` |
| Hardened Stress & Edge-Case Suite | `references/stress-tests.md` |

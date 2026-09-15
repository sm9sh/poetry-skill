---
name: ukrainian-poetry
description: "Use when Codex needs to write, rewrite, edit, critique, or evaluate Ukrainian poetry, Ukrainian verse, rhymed poems, free verse, blank verse, sonnets, kolomyika, dactylic/ternary meters, dolnik, folk songs, children's poems, patriotic poems, lyrical poems, or prose-to-poem transformations."
---

# Ukrainian Poetry

## Overview

Produce poetry that sounds originally conceived and crafted in Ukrainian: authentic phonetics and accentuation first, followed by tactile imagery, prosodic control (syllabo-tonic, dolnik, kolomyika, blank verse, verlibre), heterogeneous rhyming, clausula alternation, and register-specific discipline.

Prefer a finished poem over explanation unless the user explicitly asks for scansion, analysis, variants, scoring, or process notes.

## 6 Core Poetic Principles (Фундаментальні принципи майстерності)

Prioritize these 6 inviolable quality standards across all generations and audits:

1. **Свіжа образність та метафоричність (Fresh Imagery & Metaphoricity)**:
   - *Rule*: "Show, don't tell". Anchor emotions in tangible sensory details (tactile, visual, acoustic, olfactory, temperature), physical actions, and unexpected authorial metaphors.
   - *Anti-patterns*: Clichéd tropes (*«кров — любов»*, *«серце палає»*, *«душа плаче»*, *«море сліз»*, *«крила надії»*), declarative abstract statements without physical embodiment.
   - *Example*: ❌ *«Моє серце розривається від болю в холодній самотності.»* ➔ ✅ *«Холодна застібка куртки торкається підборіддя. На дні кишені — квиток на потяг, якого більше немає в розкладі.»*

2. **Емоційна глибина та щирість (Emotional Depth & Sincerity)**:
   - *Rule*: Authentic psychological truth, empathy, and restraint. Build emotional resonance through domestic gestures, unspoken tension, and quiet psychological truth.
   - *Anti-patterns*: Theatrical pathos, melodramatic hysteria, preachy moralizing (*«пам'ятай завжди»*, *«і я збагнув, що треба жити»*, *«любіть природу»* as cheap slogans).
   - *Example*: ❌ *«О люди, любіть свій рідний край і знайте, що в єдності наше щастя!»* ➔ ✅ *«Батько мовчки обкопує яблуню до перших заморозків. Земля під лопатою ще пахне серпневим дощем.»*

3. **Ритмічна та звукова гармонія (Rhythmic & Phonic Harmony)**:
   - *Rule*: Breathing prosody and organic cadence. In syllabo-tonic verse — natural pyrrhics; in dolnik/taktovik — disciplined ictic intervals; in verlibre — syntagmatic breath units. Elevate acoustics with heterogeneous rhymes (verb+noun, noun+adverb), pre-tonic supporting consonants (*трава́ — трива́*), conscious phonics (alliteration, assonance, soundscapes), and flawless euphony (`у/в`, `і/й`, `з/із/зі`, no hiatus).
   - *Anti-patterns*: Banal grammatical rhymes (verb-verb *знати-кохати*, noun-noun in identical case), suffixal rhyming (*-очка/-енька*), hiatus, dissonant consonant clusters.
   - *Example*: ❌ *«Я іду у поле і шукаю волю, щоб знайти у ньому свою кращу долю.»* ➔ ✅ *«Колючий вітер вистудив траву́, / І перша паморозь лягла без зву́ку. / Я цим осіннім вечором живу́, / В кишеню заховавши змерзлу ру́ку.»*

4. **Лаконічність і вага слова (Conciseness & Word Weight)**:
   - *Rule*: High semantic compression («словам тісно, думкам просторо»). Every noun, verb, and epithet must carry irreplaceable weight.
   - *Anti-patterns*: Rhythmic padding ("водичка"), filler pronouns (*я, мій, твій, цей, той, свій, вже, ось, то, ж*) used merely to pad syllable counts; **artificial syntactic inversions** (*«сонце ясне зійшло»*, *«погляд свій сумний підвів»*, *«іду я в ніч темну»*) forced for rhyme. Natural Ukrainian word order is mandatory.
   - *Example*: ❌ *«І от уже цей мій сумний і темний вечір прийшов до мене у моє вікно знов.»* ➔ ✅ *«Сутінки осідають на підвіконня. Ліхтарі вмикаються за секунду до темряви.»*

5. **Оригінальність ракурсу (Originality of Perspective)**:
   - *Rule*: Unconventional authorial angle on eternal themes (love, war, memory, loneliness). Shift focus from macro-abstractions to revealing micro-details. Close with paradoxical, lingering, or open endings that avoid didactic conclusions.
   - *Anti-patterns*: Predictable storylines, cliché perspectives (generic battlefield, generic broken heart), banal moralizing final lines.
   - *Example*: ❌ *«І так ми прожили життя щасливо, бо головне — це вірити в добро.»* ➔ ✅ *«Годинник на вокзалі поспішає на три хвилини — рівно на стільки, щоб встигнути передумати й залишитися.»*

6. **Органічна єдність форми та змісту (Organic Unity of Form & Content)**:
   - *Rule*: External architecture (meter, stanza structure, speed, line breaks, caesuras, enjambments) must intrinsically embody the psychological state and theme.
   - *Anti-patterns*: Mismatched form and tone (e.g. expressing tragic grief via a cheerful, bouncy 4-foot trochee with diminutive suffixes).
   - *Example*: An urban panic or anxiety expressed through an abrupt, irregular dolnik or syncopated verlibre rather than an ornate, rigid classical stanza.

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
3. **Draft with Scansion & Principle Awareness**:
   - Align meter and stanza architecture with emotional dynamics (**Principle 6: Form & Content**).
   - Ground themes in tactile sensory anchors, avoiding declarative statements and cliches (**Principle 1: Imagery** & **Principle 2: Sincerity**).
   - Ensure stress placement respects Ukrainian orthoepy; avoid Russianized stress shifts (*вИпадок*, not *випАдок*).
4. **Apply Heterogeneous Rhyming, Phonics & Natural Syntax**:
   - Mandate cross-grammatical rhymes with pre-tonic supporting consonants (**Principle 3: Phonics & Rhyme**).
   - Enforce natural Ukrainian word order: strictly prohibit artificial inversions created to force end-rhymes (**Principle 4: Conciseness & Syntax**).
   - Cleanse any filler pronouns (*цей, той, свій*) or rhythmic padding words.
5. **Run Silent Self-Edit**: Scan for filler lines, forced inversions, banal rhymes, declarative emotions, and sharovarshchyna clichés before emitting output.

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

### 4a. Attested Poetic / Folk / Surzhyk Stress Variants (Атестовані варіанти)
A stress shift that deviates from the standard orthoepic norm is **permitted** when there exists documented precedent in Ukrainian literary poetry, folk song, or organic surzhyk usage (e.g., Shevchenko, Franko, Lesya Ukrainka, Antonych, Zhadan, Ukrainian folk songs, Hutsul dialects). Such variants give the poet metric flexibility while remaining within the living Ukrainian phonetic tradition.

**Rule — Hard Cap: ≤ 2 attested stress variants per poem or song.**
- Exceeding 2 destabilizes the listener's prosodic trust and signals metric incompetence rather than artistic license.
- When using an attested variant, the word must land in a metrically natural position — the shifted stress must reinforce the ictus, not fight it.
- In lyrics destined for AI audio (Suno/Udio/Flow Music), mark the used variant with a capitalized stressed vowel so the audio model respects the intended shift.

**Examples of attested variants:**
| Standard | Attested Variant | Source tradition |
| :--- | :--- | :--- |
| `дорОга` | `дорогА` | folk songs, oral tradition |
| `кОлись` | `колИсь` | Shevchenko, folk |
| `рікА` | `рЕка` (surzhyk metric) | avoided — surzhyk variants require extra care |
| `зелЕний` | `зелЕний` / `зЕлений` | folk dumy, older poetry |
| `нікОли` | `нікОли` / `ніколИ` | dual norm, both attested |
| `свЯтий` | `святИй` | folk carol tradition |
| `прАвда` | `правдА` | some folk variants |

**How to apply:**
1. Identify that the shifted stress is metrically required (the foot demands it).
2. Verify the variant exists in at least one canonical source (poetry collection, folk song corpus, dialect dictionary).
3. Use it — but count it against the 2-per-poem budget.
4. Do **not** compound more than 2; if 3+ shifts are needed, rework the line to find a better word choice.


### 5. Laws of Ukrainian Euphony (Милозвучність)
- **`У` / `В` Alternation**: Use `у` between consonants (*шумів у лісі*); use `в` after vowels before consonants (*жила в селі*).
- **`І` / `Й` Alternation**: `і` adds a full syllable; `й` is a non-syllabic glide (*день і ніч* vs *сонце й місяць*).
- **Preposition Alternations**: `з / із / зі / зо` (*зі скелі*, *із шовку*, *зо два дні*).
- **Avoid Hiatus**: Prevent unpleasant vowel clashes (*прийшла ввечері*, not *прийшла у вечері*).

### 6. AI Audio Model Phonetic Stress Standard (Suno AI & Google Flow Music)

> **Context gate**: This notation is **exclusively for song lyrics** destined for Suno/Udio/Flow Music. In pure poetry output, use Unicode acute accent `́` marks or leave words unmarked. Never apply uppercase-vowel notation to regular poetic text.

Neural audio engines (Suno v3.5/v4/v5.5, Udio v4, Google Flow Music Lyria 3.5) can strip Unicode diacritics during tokenization. To guarantee correct pronunciation, capitalize the stressed vowel — but **only** in words belonging to one of three hard categories:

**Category A — Homographs** (stress determines meaning):
- `зАмок` (castle/fortress) vs `замОк` (door lock)
- `дорОга` (noun: road) vs `дорогА` (adj: precious)
- `мУка` (torment) vs `мукА` (flour)
- `плАчу` (I weep) vs `плачУ` (I pay)
- `бІлизна` (whiteness/glare) vs `білизнА` (linen/textiles)
- `нАголос` (accent mark) vs `наголОс` (conceptual emphasis)
- `оргАн` (musical instrument) vs `Орган` (anatomical/state organ)
- `Атлас` (map book) vs `атлАс` (silk fabric)
- `обрАзи` (insults) vs `Образи` (sacred icons / poetic images)

**Category B — Anti-Russian Misaccentuation** (words AI models habitually mispronounce using Russian stress):
`вИпадок`, `чорнОзем`, `одИннадцять`, `чотирнАдцять`, `листопАд`, `рукОпис`, `перЕпис`, `довІдник`, `фартУх`, `ненАвисть`, `пізнАння`, `читАння`, `завдАння`, `принестИ`, `вИрок`, `новИй`, `старИй`, `босИй`.

**Category C — Non-Intuitive Mobile Accent Shifts** (inflected form stress differs noticeably from citation form):
- `зЕмлю`, `зЕмлі` (citation form: `землЯ`)
- `рУку`, `рУки` (citation form: `рукА`)
- `хОдиш`, `хОдять` (citation form: `ходИти`)
- `несУ`, `несЕш` (citation form: `нестИ`)

**Never mark** — these must remain lowercase, as their stress is phonetically obvious or they are function words:
- All prepositions, conjunctions, particles: `і`, `й`, `та`, `що`, `але`, `або`, `як`, `за`, `на`, `до`, `від`, `при`, `без`, `під`, `над`, `між`, `через`, `перед`, `після`, `під`, `про`.
- Common pronouns and adverbs with obvious stress: `він`, `вона`, `вони`, `воно`, `ми`, `ви`, `вже`, `ще`, `тут`, `там`, `лише`, `навіть`, `завжди`, `тоді`, `коли`.
- Words where the capitalized-vowel form appeared in older examples but stress is obvious to native speakers: `моя`, `земля`, `прийде`, `заспівай`, `серденько`, `моє`, `твоє`, `своє`.

- **Syllable Hyphenation for Fast Tempos**: Use hyphens (`за-спі-вай`, `не-по-втор-ний`) in rapid delivery (e.g. trap-folk recitative) to prevent slurred pronunciation.

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

### 4. Natural Syntax & Anti-Inversion Prohibition (Заборона штучних інверсій)
- **Natural Word Order**: Ukrainian syntax is flexible, but poetic phrasing must remain natural and organic. Never invert word order artificially merely to force a rhyme word to the end of a line (*«сонце ясне зійшло»*, *«погляд свій сумний підвів»*, *«іду я в ніч»*).
- **Rule**: If maintaining a strict rhyme requires breaking natural syntax or inserting filler pronouns (*цей, той, свій*), **rephrase the entire line or change the rhyme scheme**. Linguistic naturalness takes precedence over mechanical form.

### 5. Phonics, Soundscapes & Euphony (Фоніка та звукопис)
- **Acoustic Orchestration**: Deliberately employ alliteration and assonance to enhance atmosphere (soft sibilants and fricatives for silence, snow, or whispering; sonorous liquids `/l/, /r/, /m/, /n/` for vastness and bell-like resonance).
- **Potebnja's Inner Form**: Leverage the acoustic root memory of Ukrainian words for multilayered poetic resonance.

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

Before presenting the final poem, silently verify all 6 Poetic Principles:
1. **Imagery & Sensory Anchor (Принцип 1)**: Is the poem grounded in concrete physical details and fresh metaphors ("show, don't tell")? Are abstract clichés (*душа, серце, доля, крила надії*) eliminated?
2. **Sincerity & Zero Pathos (Принцип 2)**: Is the tone psychologically genuine? Is the text free from theatrical pathos, loud declarations, and moralizing conclusions?
3. **Prosody, Phonics & Euphony (Принцип 3)**: Does the rhythm breathe naturally with correct pyrrhics? Are stresses strictly literary (*вИпадок*, *чорнОзем*, *новИй*)? Are `у/в`, `і/й`, `з/із/зі` balanced? Is assonance/alliteration harmonized?
4. **Conciseness, Natural Syntax & Anti-Inversion (Принцип 4)**: Is the poem compressed without filler pronouns (*цей, той, свій*) or rhythmic padding? Is the word order 100% natural without artificial inversions for rhyme?
5. **Perspective & Paradoxical Ending (Принцип 5)**: Does the poem offer an unexpected angle on the topic? Does the final line leave a lingering sensory or philosophical resonance without preaching?
6. **Form & Content Unity (Принцип 6)**: Does the metric structure, stanza pace, and line breaks organically match the emotional weight of the theme?

---

## Output Format

- Return **only the poem** unless the user explicitly requests commentary, scansion diagrams, alternative drafts, or rubric evaluations.
- When generating fixed forms (e.g. Sonnets), clearly structure stanzas according to the required architecture (`4+4+3+3` or `4+4+4+2`).
- If homographs require disambiguation in performance texts, use capitalized stressed vowels or acute accent marks (e.g. `зАмок` vs `замОк`).

---

## Pipeline Orchestration (5 Subagents Sequential Flow)

When performing a multi-agent deep refinement (e.g., the user requests a "refined" or "production-grade" poem, or the orchestrator deems the draft requires full pipeline treatment), execute the 5 subagents in sequence:

```text
User Input (topic, draft, or brief)
         │
         ▼
┌──────────────────────────────────────┐
│ 1. poetry-imagery-architect          │
│    (Образотворець)                   │
│    → Sensory grounding, anti-cliché  │
│    → Output: Enhanced draft +        │
│      Sensory Map + Imagery Score     │
└─────────────┬────────────────────────┘
              │ draft + sensory_map
              ▼
┌──────────────────────────────────────┐
│ 2. poetry-emotional-critic           │
│    (Критик щирості)                  │
│    → Sincerity audit, anti-pathos    │
│    → Output: Emotional Audit Report  │
│      + Revised draft                 │
└─────────────┬────────────────────────┘
              │ draft + emotional_audit
              ▼
┌──────────────────────────────────────┐
│ 3. poetry-prosody-phonics            │
│    (Майстер фоніки та просодії)      │
│    → Meter scansion, stress check,   │
│      euphony, rhyme heterogeneity    │
│    → Output: Scansion Diagram +      │
│      Phonics Report + Revised draft  │
└─────────────┬────────────────────────┘
              │ draft + scansion + phonics
              ▼
┌──────────────────────────────────────┐
│ 4. poetry-conciseness-editor         │
│    (Редактор лаконічності)           │
│    → Filler purge, anti-inversion    │
│    → Output: Compression Report +    │
│      Lean draft                      │
└─────────────┬────────────────────────┘
              │ lean_draft + all_reports
              ▼
┌──────────────────────────────────────┐
│ 5. poetry-form-synthesizer           │
│    (Архітектор форми та ракурсу)      │
│    → Form-content harmony, voltas,   │
│      conflict arbitration, 100-pt    │
│      rubric scoring                  │
│    → Output: FINAL POEM + Scorecard  │
└──────────────────────────────────────┘
```

### Data Flow Contract

Each agent receives:
```yaml
draft_text: string       # Current draft (output from previous agent)
register: enum           # Passed through from user request
mode: enum               # Passed through from user request
previous_reports: list    # Accumulated reports from prior agents
```

Each agent outputs:
```yaml
revised_draft: string    # Updated draft text
report: object           # Agent-specific audit report
score_impact: object     # Estimated rubric dimension scores
```

### When to Use Full Pipeline vs Single Agent

- **Full pipeline**: New poem from scratch, "production quality" request, 100-point rubric evaluation
- **Single agent**: Targeted editing ("fix the rhymes", "remove clichés", "check meter"), where only the relevant specialist is invoked
- **Partial pipeline**: Skip agents whose domain the draft already satisfies (e.g., skip imagery-architect if the draft is already sensory-rich)

---

## References

| Need | Reference |
| :--- | :--- |
| Full Theoretical & Operational Guide | `references/full-guide.md` |
| Ukrainian-Language Reference Guide | `references/ukrainian-poetry-skill-uk.md` |
| Quick-Reference Cheat Sheet | `references/ukrainian-poetry-skill-lite.md` |
| Structured Input Request Templates | `references/input-templates.md` |
| 100-Point Evaluation & Scansion Rubric | `references/rubric.md` |
| 5 Specialized Subagents Pipeline | `agents/` (`agents/openai.yaml`) |
| Standardized Test Suite (27 Scenarios) | `references/tests.md` |
| Hardened Stress & Edge-Case Suite | `references/stress-tests.md` |


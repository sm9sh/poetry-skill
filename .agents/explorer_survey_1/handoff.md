# 5-Component Handoff Report: Ukrainian Poetic & Linguistic Audit

**Agent**: Explorer 1 (Ukrainian Poetic & Linguistic Specialization)  
**Working Directory**: `d:/poetry-skill/.agents/explorer_survey_1`  
**Date**: 2026-08-26  
**Recipient**: Parent Orchestrator (`1f051654-233b-4bf7-ad7d-e9c4beed0a3d`)

---

## 1. Observation

Direct observations and citations from the audited repository files:

1. **Omission of Dactyl in Core Meter Guidance**:
   - `skills/ukrainian-poetry/SKILL.md:100` states verbatim:
     > *"Prefer iamb for balanced reflection, trochee for song-like drive, amphibrach for soft lyric movement, anapest for lift, and free verse when voice and image matter more than pattern."*
   - Dactyl (`дактиль` — `— U U`) is omitted from this sentence, creating an asymmetry with `references/input-templates.md:15` where `meter: <free | iamb | trochee | amphibrach | anapest | approximate only>` also omits dactyl from the template string.
2. **Lack of Operational Definitions for Non-Syllabo-Tonic Verse**:
   - In `skills/ukrainian-poetry/references/full-guide.md:229`:
     > *"Українська поезія може бути силабічною, тонічною, силабо-тонічною, фольклорною або верлібровою. Не підганяй усі тексти під одну схему."*
   - No subsequent rules, intervals, or templates exist in `full-guide.md` or `SKILL.md` for **Dolnik (дольник)**, **Taktovik (тактовик)**, **Accentual verse (акцентний вірш)**, or the national Ukrainian **Kolomyika meter (коломийковий вірш: 4+4+6)**.
3. **Absence of Blank Verse Codification**:
   - In `skills/ukrainian-poetry/SKILL.md:40-41` and `full-guide.md:48-49`, `rhyme: none` defaults to `mode: free-verse`. There is no instruction or mode for **Blank Verse (білий вірш — unrhymed syllabo-tonic verse, e.g. iambic pentameter)**, conflating unrhymed meter with non-metric free verse.
4. **No Clausula Control or Stanza Alternation Rules**:
   - In `skills/ukrainian-poetry/SKILL.md:97` and `full-guide.md:212-216`, rhyme schemes are listed as `AABB`, `ABAB`, `ABBA`, but there is zero instruction regarding masculine (`Ч`), feminine (`Ж`), dactylic (`Д`), or alternating (`ЖЧЖЧ`) clausulae.
5. **No Stress Mechanics, Homographs, or Anti-Calque Accents**:
   - Neither `SKILL.md` nor `full-guide.md` contains guidance on Ukrainian mobile stress (`рухомий наголос`), stress homographs (`зАмок / замОк`, `нАголос / наголОс`, `бІлизна / білизнА`), or common LLM stress hallucinations calqued from Russian (`вИпадок` vs `випАдок`, `чорнОзем` vs `чорнозЕм`, `новИй` vs `нОвий`, `листопАд` vs `листОпад`).
6. **Vague Rhyme Typology & Absence of Heterogeneous Rhyme Directive**:
   - In `skills/ukrainian-poetry/SKILL.md:98`:
     > *"Reject rhymes that are grammatically lazy, semantically empty, predictable, or dependent on unnatural syntax."*
   - The files do not operationally define **heterogeneous rhymes (різнорідні рими: verb+noun, noun+adverb)**, **rich pre-tonic rhymes (багаті опорні рими)**, **assonance vs dissonance rhymes**, nor do they blacklist specific suffixal diminutive clichés (`-очка/-ечка`, `-енька/-онька`).
7. **Absence of Anti-Sharovarshchyna and Granular Register Definitions**:
   - In `skills/ukrainian-poetry/SKILL.md:54`: `folk` mode is only defined as *"Use parallelism and cadence lightly; avoid fake archaism."*
   - There are no explicit definitions or guardrails against **sharovarshchyna (шароварщина)**, nor are there register specifications for **Contemporary Urban**, **Philosophical/Neoclassical**, **Baroque/Cossack (17th c.)**, or **Chamber-Intimate (Тиха лірика)**.
8. **Evaluation Rubric Gaps**:
   - In `skills/ukrainian-poetry/references/rubric.md:7-129`, the 100-point rubric lacks explicit deductions for broken meter under strict formal prompts, stress distortions, or pseudo-folk kitsch.

---

## 2. Logic Chain

1. **From Observation 1 & 2 to Prosodic Incompleteness**:
   - Because `SKILL.md` and `full-guide.md` omit dactyl, dolnik, taktovik, and kolomyika meter, an LLM receiving requests for traditional Ukrainian folk forms, 20th-century modernist lyrics (Tychyna, Antonych), or Ukrainian rock song meters has no operational rules to generate proper inter-ictic intervals or 14-syllable 4+4+6 structures.
2. **From Observation 3 to Formal Confusion**:
   - Because blank verse is not distinguished from free verse, requests for unrhymed dramatic iambics (e.g. Lesya Ukrainka style) default to non-metric free verse, resulting in failure to satisfy classical unrhymed formal requests.
3. **From Observation 4 to Acoustic Monotony**:
   - Without clausula alternation rules (`ЖЧЖЧ`), LLMs default to all-feminine (`ЖЖЖЖ`) or all-masculine (`ЧЧЧЧ`) line endings, which degrades the musical balance and natural cadence of Ukrainian verse.
4. **From Observation 5 to Metric Disruption & Language Calques**:
   - Ukrainian stress is mobile and distinct from Russian stress. Because LLMs lack explicit stress checks and homograph awareness, they frequently distort stress positions (*випАдок*, *чорнозЕм*, *нОвий*) to force an iamb or trochee, violating the core rule that "good Ukrainian comes first."
5. **From Observation 6 to Rhyme Degeneration**:
   - Without positive guidance toward **heterogeneous rhymes** (verb + noun, noun + adverb) and specific prohibitions against suffixal diminutive rhymes (`-очка/-ечка`), LLMs default to low-effort grammatical rhyming (verb-verb, adjective-adjective in identical case).
6. **From Observation 7 to Stylistic Kitsch Risk**:
   - Without a strict anti-sharovarshchyna guardrail and authentic historical register guidelines, the model will produce stereotypical postcard verses (*соловейко, калина, козак*) when asked for folk or patriotic poetry.
7. **From Observation 8 to Ineffective Quality Benchmarking**:
   - The rubric cannot detect or penalize metric breakage or stress hallucination rigorously if points are only deducted under a generalized 15-point rhythm score.

---

## 3. Caveats

- **Scope boundary**: This audit specifically focuses on the Ukrainian linguistic, poetic, prosodic, and rubric components (`skills/ukrainian-poetry/` and related mirrors/legacy files). Suno AI music prompting and audio metatag architecture are audited in parallel by Explorer 2.
- **Model behavior**: LLMs have inherent sub-word tokenization constraints that make purely internal phonetic counting challenging without explicit prompting techniques (such as scansion checking, capitalized stress vowels, or combining acute diacritics).
- No source code outside `.agents/explorer_survey_1` has been modified during this read-only investigation phase.

---

## 4. Conclusion & Actionable Recommendations

The Ukrainian Poetry skill has an excellent philosophical foundation ("natural Ukrainian diction over forced form"), but requires significant structural, prosodic, and linguistic enhancements to reach professional literary standard.

### Concrete Enhancement Specifications:
1. **Core SKILL.md & full-guide.md Updates**:
   - Add **Dactyl** to meter definitions.
   - Codify **Dolnik**, **Taktovik**, **Kolomyika meter (4+4+6)**, and **Blank verse (білий вірш)**.
   - Introduce **Clausula alternation principles (`ЖЧЖЧ`)**.
   - Add the **Phonetic & Stress Guardrail**: stress homographs catalog, mobile stress rules, dual accents, and anti-Russian misaccentuation blacklist.
   - Add the **Heterogeneous Rhyme Requirement** and **Anti-Grammatical/Banal Rhyme Blacklist**.
   - Codify **6 Authentic Registers** (`contemporary-urban`, `chamber-intimate`, `philosophical-neoclassical`, `baroque-cossack`, `folk-authentic`, `children-playful`).
   - Implement the **Anti-Sharovarshchyna Guardrail**.
2. **Template & Rubric Refinements**:
   - Update `input-templates.md` with `form`, `clausula`, `stanza_type`, and `subgenre`.
   - Update `rubric.md` with explicit metric violation deductions, anti-sharovarshchyna scoring, and evaluator scansion checklists.
3. **Test Suite Expansions**:
   - Expand `tests.md` and `stress-tests.md` with 6 new advanced test cases: Sonnet with volta, Dolnik rock lyric, Kolomyika 14-syllable, Blank verse monologue, Homograph stress test, and Baroque Cossack register test.
4. **Mirror Synchronization**:
   - Synchronize updates across `skills/ukrainian-poetry/`, `ukrainian-poetry-skill.md`, `ukrainian-poetry-skill-uk.md`, and `ukrainian-poetry-skill-lite.md`.

---

## 5. Verification Method

To independently verify the findings in this report:

1. **Inspect Code Locations**:
   - Verify dactyl omission: `view_file` on `skills/ukrainian-poetry/SKILL.md:100` and `references/input-templates.md:15`.
   - Verify absence of Dolnik/Kolomyika/Blank verse: `grep_search` for `дольник`, `тактовик`, `коломий`, `білий вірш` in `skills/ukrainian-poetry/`.
   - Verify absence of stress homographs: `grep_search` for `омограф`, `зАмок`, `наголос` across `skills/ukrainian-poetry/`.
2. **Run Prosodic Scansion Test on LLM Output**:
   - Execute test prompt: *"Напиши сонет українською мовою п'ятистопним ямбом за схемою ABBA ABBA CDC DCD з чергуванням жіночих і чоловічих рим."*
   - Evaluate whether existing instructions prevent stress hallucinations on words like *вИпадок* or *чорнОзем*.
3. **Audit Report Reference**:
   - Read the complete 8-chapter deep analysis in `d:/poetry-skill/.agents/explorer_survey_1/analysis.md`.

---
*End of Handoff Report.*

# AGENTS.md — Global Agent Directives for Ukrainian Poetry & Suno Prompting

This repository is an AI Skills ecosystem for authentic Ukrainian poetry generation and production-grade Suno AI / Flow Music prompt engineering.

## Operational Directives

### 1. Ukrainian Poetry Directives (`ukrainian-poetry`)
All models and agents generating, editing, or evaluating Ukrainian poetry MUST strictly enforce the **6 Core Poetic Principles (Фундаментальні принципи поетичної майстерності)** as foundational quality standards:

1. **Свіжа образність та метафоричність (Fresh Imagery & Metaphoricity)**:
   - "Show, don't tell" through concrete physical detail, sensory anchors (sight, sound, touch, smell, temperature), and action rather than abstract declarations of emotion.
   - Categorical rejection of worn-out cliches and sentimental tropes (*«кров — любов»*, *«троянди — сльози»*, *«серце палає»*, *«душа плаче»*).
2. **Емоційна глибина та щирість (Emotional Depth & Sincerity)**:
   - Rooted in psychological truth, restraint, and genuine human empathy.
   - Zero theatrical pathos, plastic sentimentality, or preachy moralizing (*«і я збагнув, що треба жити»*).
3. **Ритмічна та звукова гармонія (Rhythmic & Phonic Harmony)**:
   - Audible, breathing prosodic flow (syllabo-tonic, dolnik, taktovik, 14-syllable kolomyika, blank verse, or verlibre).
   - Rich heterogeneous cross-grammatical rhymes (verb+noun, noun+adverb) with pre-tonic supporting consonants; zero grammatical verb-verb or diminutive rhymes.
   - Conscious phonics & soundscapes (alliteration, assonance, Potebnja's inner form of words) and strict adherence to Ukrainian euphony (`у/в`, `і/й`, `з/із/зі`, no hiatus).
4. **Лаконічність і вага слова (Conciseness & Word Weight)**:
   - Maximum semantic density («словам тісно, думкам просторо»).
   - Zero rhythmic padding or filler pronouns (*цей, той, свій, я, вже, ось*) inserted merely to fill foot counts.
   - Strict prohibition against artificial syntactic inversions (*«сонце ясне зійшло»*, *«погляд свій сумний підвів»*) used to force end-rhymes; natural Ukrainian word order is inviolable.
5. **Оригінальність ракурсу (Originality of Perspective)**:
   - Unconventional authorial angle on universal themes; shifting focus from macro-abstractions to revealing micro-details.
   - Paradoxical, lingering, or open endings that avoid trivial closures or moral conclusions.
6. **Органічна єдність форми та змісту (Organic Unity of Form & Content)**:
   - External form (meter, stanza structure, tempo, caesuras, enjambment, line raggedness or smoothness) must intrinsically embody the emotional state and theme.
   - Form is never arbitrary decoration — it is the living body of the poem.

### 2. Suno AI & Google Flow Music Generation Directives (`ukrainian-poetry-to-suno`)
- **Western Genre Anchor**: Musically target Western contemporary and classic genres (UK/US Post-Punk, Darkwave, Synthwave, Trip-Hop, Minimalist Alt-Pop, Shoegaze, Progressive Metalcore, Melodic Techno, Ambient). Music must sound like a top-tier global release, not regional/provincial pop.
- **Token Economy**: `Style of Music` must be strictly **80–180 characters** (optimal 80–150).
- **Field Separation & Metatag Syntax**:
  - `Style of Music`: English Western genre descriptors, BPM, vocal timbre, instruments, production feel.
  - `Lyrics`: Ukrainian text with **bracketed structure & arrangement tags** `[Intro - Staccato cutting telecaster riff, driving bassline]`, `[Verse 1 - Intimate vocal]`, `[Chorus]`, `[Instrumental Break - Bandura solo]`, `[Drop - Heavy 808]`, `[Outro - Slow fade out]`.
  - **Strict Parentheses vs Brackets Rule**:
    - `[Square Brackets]`: Used for ALL structural, instrumentation, and arrangement instructions. Models parse them as audio directing cues without singing them.
    - `(Round Parentheses)`: Used **EXCLUSIVELY for backing vocals, ad-libs, and vocal echoes** `(луна)`, `(ніколи знов)`. Never put instrumental descriptions in parentheses because Google Flow Music and Suno will vocalize/sing them out loud!
  - **Ukrainian Stress Standard for Audio AI Models**:
    - To prevent TTS/vocal engines from mispronouncing Ukrainian words or shifting stresses, capitalize the stressed vowel on non-obvious words, homographs, and mobile accents: `вИпадок`, `чорнОзем`, `прИйде`, `заспівАй`, `моЯ`, `землЯ`, `зЕмлю`, `дорОга` vs `дорогА`, `зАмок` vs `замОк`, `плАчу` vs `плачУ`, `сердЕнько`, `одИннадцять`, `листопАд`.
  - `Exclude`: Anti-local-pop and anti-artifact suppression tokens (`cheesy regional pop, post-soviet schlager, wedding synth brass, cheap accordion, generic euro-pop, metallic highs, muddy bass`).
- **De-identification**: Never output direct artist names or copyright phrases (`in the style of...`).

## Specialized Subagents Pipeline (`skills/ukrainian-poetry/agents/`)
For multi-stage poetic refinement, the ecosystem utilizes 5 specialized personas:
1. `poetry-imagery-architect` (**Образотворець**): Tactile imagery, sensory anchors, fresh metaphors, anti-cliche guardrails.
2. `poetry-emotional-critic` (**Критик щирості**): Sincerity audit, zero pathos, anti-moralizing, psychological nuance.
3. `poetry-prosody-phonics` (**Майстер фоніки та просодії**): Metric scansion, stress accuracy, acoustic euphony (`у/в`, `і/й`), heterogeneous rhymes, phonics.
4. `poetry-conciseness-editor` (**Редактор лаконічності**): Semantic compression, removal of filler words/pronouns, elimination of artificial inversions.
5. `poetry-form-synthesizer` (**Архітектор форми та ракурсу**): Form-content harmony, paradoxical perspective, final assembly.

## Reference Index & Skill Files
- Poetry Skill: `skills/ukrainian-poetry/SKILL.md`
- Subagents Pipeline: `skills/ukrainian-poetry/agents/`
- Full Poetic Guide: `skills/ukrainian-poetry/references/full-guide.md`
- 100-Point Poetic Rubric: `skills/ukrainian-poetry/references/rubric.md`
- Suno Conversion Skill: `skills/ukrainian-poetry-to-suno/SKILL.md`
- Reference & Style Cheatsheet: `skills/ukrainian-poetry-to-suno/references/reference-to-style-cheatsheet.md`
- Mood to Style Map: `skills/ukrainian-poetry-to-suno/references/mood-to-style-map.md`
- Prompt Builder: `skills/ukrainian-poetry-to-suno/references/prompt-builder.md`

## Verification & Testing
Run deterministic test suites (Python 3 standard library):
```bash
py -3 tests/run_tests.py --all
```

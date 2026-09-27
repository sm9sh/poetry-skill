# Iteration 1 — with_skill — process notes

Skills read in full: `skills/ukrainian-poetry/SKILL.md`, `skills/ukrainian-poetry-to-suno/SKILL.md`, `docs/PIPELINE.md`, plus `poem-to-song-adaptation.md`, `world-class-song-criteria.md`, `platforms.md`, `quality-criteria.md`, parts of `mood-to-style-map.md`, `suno-prompt-anti-patterns.md`, and the kolomyika examples in `full-guide.md` / `stress-tests.md`. `check_lyrics.py` was run on every song (evals 5–8). I wrote everything myself and did not use the specialist agents, because no prompt asked for a "production-grade" or scored poem.

## Cross-cutting issues (read first)

1. **AGENTS.md contradicts the skills on parentheses, and this is exactly the bug in eval 8.** AGENTS.md (loaded as project instructions that "OVERRIDE any default behavior") says `(Round Parentheses)` are "EXCLUSIVELY for backing vocals, ad-libs, and vocal delivery gestures `(whispered)`, `(belted)`, `(half-time feel)`, `(key change)`…". Both SKILL files, `platforms.md`, the anti-patterns file and `check_lyrics.py` say the opposite: delivery cues go in `[...]` because v6/Flow sing anything in `(...)`. A model that follows AGENTS.md literally will produce the eval-8 failure. AGENTS.md needs to be brought in line with the skills; right now it is the highest-priority source, and it is wrong.
2. **AGENTS.md is out of date on platforms.** It targets Suno v4.5/v5.5, calls Udio v4 a live target with commercial rights, and lists Flow "Spaces / Turntable / AI Cover / Gemini Omni Flash" as features. `platforms.md` (checked 2026-09-27) says v4–v5.5 were retired on 2026-09-09, Udio is a closed garden, and those Flow features are unverified. AGENTS.md also has a second gate system (10 AI Quality Gates plus a 6-step lifecycle with DAW and ads) next to PIPELINE's P/S/M gates. I followed the skills and PIPELINE, but a reader has to work out on their own which source wins.
3. `mood-to-style-map.md` still gives "Method 1 / Method 2 / Udio v4" prompts, and the anti-patterns file's "good" Style example starts with `ukrainian indie pop`. That contradicts SKILL.md, which says to put the Western genre first and drop "ukrainian" as the lead tag.
4. CLAUDE.md's test command is `py -3 …`, which is Windows-only. I did not run `tests/` because no code changed.
5. **Syllable counting and stress placement were the slowest part by far**, all done by hand for every line. `check_lyrics.py` could cheaply (a) print a vowel count per sung line and (b) compare V1 and V2 line by line (criterion 8 / Gate 3: "рівні рядки у відповідних секціях"). Right now the script checks nothing about the most important singability rule.
6. `check_lyrics.py` has no Flow mode and no snippet mode. Passing a Flow prompt as `--style` gives a false "547 chars" warning. Checking a single verse (Pipeline D) gives false "no [Chorus]" and "no line repeats 3+" warnings. Suggested fixes: `--platform flow` (checks prompt sentences, not length) and `--section` (skips song-level checks).

## Eval 1 — father-fence-chamber (Pipeline A)
- Steps: parameters → concept (angle: the father is heard about by phone, not seen; central images are the boards, the nails in his mouth, the old paint; turn: the gate he didn't touch; ending: open) → draft → checklist 1–16.
- Form: verlibre, because restraint and silence suit short, uneven lines. Item 15 (line breaks) is mandatory for verlibre, so I checked each break: "щоб не стирчала вище." / "тому й мовчить." are deliberate.
- The checklist caught: "вибив" (imprecise) → "повиривав". "приміряє до старої" was unclear → "прикладає до сусідньої, щоб не стирчала вище". An explicit ending line ("каже, руки не дійшли") would have named the subtext, so I dropped it and ended on the gate that "не зачиняється до кінця".
- No title: every candidate either repeated the first line or gave away the ending (item 16).
- Unclear: nothing major. The "no filler pronouns (мій)" rule made me pause over "за моїм велосипедом". I kept it because the pronoun carries meaning (my absence). The rule could say "filler = pronoun that carries no meaning".

## Eval 2 — fix-draft-rhymes (Pipeline C)
- Steps: scope ("покращ" = more than rhymes, but keep theme and voice) → diagnosis with the checklist (blacklisted pair воля/доля; verb-verb віє/гріє/пломеніє; cliché "надія в серці пломеніє"; filler "свою", "тихо"; hiatus "іду у") → minimal rewrite in the author's own meter (trochaic 6+6) → Gate P → poem + short note.
- Rhymes now: дороги/вологий (noun + adjective), сліди/куди (noun + adverb). Clausulae changed from ЖЖЖЖ to ЖЖЧЧ.
- Judgment calls: "від ріки вологий" is a post-positioned adjunct. I judged it natural speech (like «від дощу мокрий»), not a rhyme-forced inversion, but the skill has no test for telling the two apart. I also dropped the author's "сонце" and "надія". Pipeline C says keep "ключові образи автора", but the priority list in PIPELINE §0 doesn't rank the author's images against removing clichés. Worth one sentence in the skill.
- "звідки ти й куди": chose й for euphony after a vowel.

## Eval 3 — sonnet-volta (Pipeline A, fixed form)
- Italian sonnet abba abba cde cde, iambic pentameter (a = masculine 10 syllables, b = feminine 11). Scansion done line by line, all ictuses on even syllables with allowed pyrrhics.
- Concept: no war words at all. Octave: silent departure, the father on the dark platform clicking a lighter so they can see his hand, one light suitcase, mint picked "yesterday". Volta at line 9: 3 a.m., the train stops in an unnamed field. Sestet: dawn shows a poplar, haystack and water tower, and the daughter asks "Мамо, ми вже вдома?" (a paradoxical open ending).
- Rhymes are heterogeneous: гудка/рука/легка/здалека (noun gen., noun nom., adjective, adverb); тато/багато; полі/поволі; знак/так; солома/вдома.
- The checklist caught: "так положено" (Russianism) removed. "з тьми" (bookish) → "з темряви". A double "пахне" in octave and sestet → the octave now says "нарвала вчора біля хати" (more subtext: the flight was sudden). "як в нас" (euphony violation) → dropped that ending.
- Unclear: the skill doesn't say how exact the four-fold octave rhyme must be. Mine is approximate on b (тато/багато/м'ята/хати: -ато/-ята/-ати). That is fine by the "heterogeneous-approximate" default, but a strict sonnet reader might object.

## Eval 4 — kolomyika-humor (Pipeline A, folk form)
- 4 kolomyika quatrains, each half-line 8 + 6 syllables with the caesura after 8. The 8-syllable halves mostly stress 3 and 7. Every 6-syllable half ends feminine, and the 6-syllable lines rhyme in pairs.
- Anti-sharovarshchyna: humour from domestic detail (basket, kerchief, "шусть по вуха", "дременув під ґанок", "розговівся"). No калина, гопак or сало stickers.
- Rhymes: поклала/мало, бачить/ледачий, ґанок/зранку, люди/буде. All heterogeneous and approximate, which suits a folk voice. I avoided the tempting verb-verb pair розговівся/вмівся.
- **Unclear/contradictory:** SKILL.md says kolomyika accents fall on "3, 7, 11 and 13", but the skill's own example in `full-guide.md` ("край битого шляху") stresses 10 and 13. The folk tradition varies too. The rule reads stricter than the evidence behind it. The skill also doesn't say whether folk forms relax the heterogeneous-rhyme rule, since traditional kolomyiky often use grammatical rhymes.

## Eval 5 — poem-to-darkwave-suno (Pipeline B, adapt mode)
- Mode: "адаптувати" (verlibre → song), per `poem-to-song-adaptation.md`.
- Concept: a fast clock gives you time to not take the train. Hook-title: "Три хвилини наперед" (7 syllables). Sound DNA: darkwave/cold post-punk, deadpan baritone, 124 bpm.
- Form: Intro (hook in the first seconds) → V1 → Pre → C → V2 → Pre → C → Bridge → Final C (last line varied to "ще без нас") → Outro. Trochaic; verses are 7-7-8-7 syllables and match between V1 and V2. The hook appears 7 times. 5–7 sung lines before the first chorus.
- V2 adds new information (doors hiss, the conductor asks «Ну? Ідеш?», "і поїзд — теж") and a new arrangement layer (chorus guitar, tambourine). The bridge is the turn ("Хай не лагодять ніколи. / Хай спішить. Я постою." — the "ти" is revealed as the speaker's self-address).
- check_lyrics.py: OK, no warnings. Style is 167 characters, darkwave first, no negations or artist names. No stress marks were needed.
- **Eval contamination:** the eval prompt is almost verbatim the worked example in `poem-to-song-adaptation.md` (same poem, and "три хвилини" is suggested as the hook). A model can copy the example's lyrics. I deliberately changed the hook phrase, meter, genre and all lines, but the eval can't really measure adaptation skill while the answer sits in a reference. Change either the eval poem or the example.
- The output-format rule ("1–3 рядки після блоків") was tight. My note runs to two short paragraphs because it has to cover what changed, why, and what to tweak.

## Eval 6 — brief-to-song-flow (Pipeline B, no poem, Flow)
- Concept: the sold orchard doesn't care whose it is, but the knowledge that went with it is lost. Hook-title: "Сад не знає, чий" (5 syllables). Final-chorus variation: "Я не знаю, чия" (criteria 10 and 12).
- Compact Flow structure: Intro (hook sung) → V1 → C → V2 → C → Bridge → Final C. V1 and V2 are both 7-8-7-8 syllables.
- V2 adds new information (grandma's jam jars on a city balcony, handwritten labels «вишня», «аґрус», «двадцять п'ять»). The bridge turn is about Antonivka apples that strangers will call sour, not knowing they need to lie until winter.
- Stress marks: only `замОк` (homograph). No parentheses at all, which suits Flow.
- The checklist caught: "її рукою" in V2 had no antecedent (literal clarity, item 10) → V1 now says "хтось підрізав бабі грушу".
- check_lyrics.py: OK on the lyrics. With the Flow prompt passed as `--style`, it gives a false length warning (see cross-cutting item 6).
- Unclear: the skill doesn't say which language the Flow prompt should be in. I used English, following `mood-to-style-map.md`. Criterion 3 (voice within 5 s) is "softened" for ambient, but trip-hop/ambient hybrids aren't mentioned. I put the hook in the intro anyway. It's also unverified whether Flow reads section-tag descriptors ("voice enters at once") the way Suno does.

## Eval 7 — keep-text-mode (Pipeline B, keep mode)
- Words unchanged: I only added tags and repeated or reordered existing lines (keep mode explicitly allows this).
- To satisfy Gate S criterion 5 without writing new words, I split the text: V1 = lines 1–2, V2 = lines 3–4 (different lines, so the verses don't repeat), chorus = the ring line ×2–3 with a sung echo `(без ключів)` built from the user's own words. The breakdown plays the full text once, in the original order.
- check_lyrics.py: OK. Style is 170 characters, post-punk first. No stress marks needed.
- **Unclear:** SKILL.md says Gate S applies to every song "без винятків", but in keep mode with a 5-line text, criteria 5 (V2 development) and 3 can conflict with "слова не міняй". PIPELINE §0 priority 1 (the user's explicit request) settles it, but the song skill should say so directly, e.g. "у режимі «зберегти» критерії 5/6 виконуй лише перестановкою; якщо неможливо — скажи користувачу й запропонуй нові рядки".

## Eval 8 — fix-generation-problems (Pipeline D)
- Diagnosis, from the Pipeline D table: cues in `()` get sung → move them into the section tag `[Verse 1 - whispered, half-time feel]`. Over-marking `моЯ` → lowercase. `вИпадок` stays (Russian-stress trap). `дорОга` stays (homograph with дорогА).
- Next steps: regenerate only that section with Suno section editing, and set Variety = Off.
- check_lyrics.py on the user's original: 2 ERRORs (both parenthesised cues) and a WARNING for `моЯ`, i.e. all three problems caught. On the fixed snippet there are no errors, only the false snippet warnings (no chorus, no repeat).
- **Gap:** the user says the model still sings "випАдок" although it's marked. Neither the skill nor PIPELINE covers "marked correctly, still mispronounced". I improvised: remove the surrounding noise (over-marks, sung cues) first, and if it persists, the melody's strong beat is landing on the 2nd syllable, so restructure the line so "вИ" falls on the downbeat, with the user's permission. This belongs in the Pipeline D table.

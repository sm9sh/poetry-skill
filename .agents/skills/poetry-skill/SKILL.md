---
name: poetry-skill
description: "Use when creating, analyzing, editing, or evaluating Ukrainian poetry, versification, rhymed poems, lyrics, or converting Ukrainian poetic material into production-grade Suno AI / Flow Music audio prompts with Western sound standards."
---

# Ukrainian Poetry & Suno Music Skill Suite (poetry-skill)

Unified entry point and master routing for Ukrainian poetry versification and Suno AI music prompt engineering.

## 1. Sub-Skill Routing

Depending on the task, invoke the specialized sub-workflow:

| Task Type | Trigger / Intent | Sub-Skill to Load |
|---|---|---|
| **Poetry & Versification** | Writing poems, sonnets, dolnik, kolomyika, editing rhymes, stress scansion, Ukrainian lyrical texts | `skills/ukrainian-poetry/SKILL.md` |
| **Suno AI Music Prompts** | Converting poems/briefs to Suno Custom Mode, style prompts, Western genre arrangement, metatags | `skills/ukrainian-poetry-to-suno/SKILL.md` |
| **End-to-End Songwriting** | Generating Ukrainian lyrics + creating matching Western Suno AI prompts in one flow | Execute **Poetry Workflow** first, then **Suno Conversion Workflow** |

---

## 2. Core Directives Summary

### Ukrainian Poetry (6 Poetic Standards & 5 Subagents)
1. **Свіжа образність та метафоричність**: Показ через дію й тактильну деталь замість декларацій; нуль затертих штампів (*«кров-любов»*, *«серце палає»*).
2. **Емоційна глибина та щирість**: Справжній психологізм, відсутність фальшивого пафосу, театральщини та моралізаторства.
3. **Ритмічна та звукова гармонія**: Живе дихання розміру (силабо-тоніка, дольник, верлібр), багаті різнорідні рими, фоніка (асонанси, алітерації, звукопис) та закони евфонії (`у/в`, `і/й`, `з/із/зі`).
4. **Лаконічність і вага слова**: Максимальна смислова компресія; нуль "води" та займенників-заповнювачів; сувора заборона штучних синтаксичних інверсій заради рими.
5. **Оригінальність ракурсу**: Нетривіальний авторський погляд на вічні теми, мікро-фокус, парадоксальні або відкриті фінали.
6. **Органічна єдність форми та змісту**: Метр, строфіка та динаміка пауз є природним відбитком теми та внутрішнього стану.
- **5 Subagents Pipeline**: `skills/ukrainian-poetry/agents/` (`poetry-imagery-architect`, `poetry-emotional-critic`, `poetry-prosody-phonics`, `poetry-conciseness-editor`, `poetry-form-synthesizer`).

### Suno AI & Google Flow Music Prompting
- **Western Genre Anchor**: All sound design must strictly target Western genres (Post-Punk, Darkwave, Synthwave, Trip-Hop, Alt-Pop, Shoegaze, Progressive Metalcore, Melodic Techno, Ambient).
- **Token Economy**: `Style of Music` strictly **80–180 characters** (optimal 80–150), comma-delimited, English only, zero metadata labels (`Language:` forbidden).
- **Structure & Arrangement Metatags**: Use square brackets for ALL structural and sound design cues: `[Intro - Staccato cutting telecaster riff, driving bassline]`, `[Verse 1 - Intimate vocal]`, `[Chorus]`, `[Instrumental Break - Bandura solo]`, `[Drop - Heavy 808]`, `[Outro - Slow fade out]`.
- **Parentheses Rule**: Round parentheses `(...)` are used **EXCLUSIVELY for sung backing vocals / echoes** `(луна)`, `(ніколи знов)`. Never put instrumental descriptors in parentheses (Google Flow Music and Suno will vocalize/sing them out loud!).
- **Ukrainian Stress Standard**: Capitalize the stressed vowel in words with non-obvious stress, homographs, and mobile accents (`вИпадок`, `чорнОзем`, `прИйде`, `заспівАй`, `моЯ`, `землЯ`, `зЕмлю`, `дорОга` vs `дорогА`, `зАмок` vs `замОк`, `плАчу` vs `плачУ`, `сердЕнько`).
- **Anti-Local-Pop Exclude**: `cheesy regional pop, post-soviet schlager, wedding synth brass, cheap accordion, generic euro-pop, metallic highs, muddy bass`.

---

## 3. Quick Reference

- Master Rules: `AGENTS.md`
- Poetic Guide: `skills/ukrainian-poetry/references/full-guide.md`
- Evaluation Rubric: `skills/ukrainian-poetry/references/rubric.md`
- Subagents Pipeline: `skills/ukrainian-poetry/agents/`
- Reference Cheatsheet: `skills/ukrainian-poetry-to-suno/references/reference-to-style-cheatsheet.md`
- Tests: `py -3 tests/run_tests.py --all`

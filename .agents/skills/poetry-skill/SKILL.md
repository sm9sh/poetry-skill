---
name: poetry-skill
description: "Use when creating, analyzing, editing, or evaluating Ukrainian poetry, versification, rhymed poems, lyrics, or converting Ukrainian poetic material into production-grade Suno AI (v4.5/v5.5), Udio AI (v4), or Google Flow Music (Lyria 3.5) audio prompts with Western sound standards, DAW stem mixing, and streaming distribution."
---

# Ukrainian Poetry & AI Music Generation Skill Suite (poetry-skill)

Unified entry point and master routing for authentic Ukrainian poetry versification and production-grade AI music generation across **Suno AI (v4.5 / v5.5)**, **Udio AI (v4)**, and **Google Flow Music (Lyria 3.5)**, incorporating engineering DAW post-production, algorithmic streaming mastering, and the **10 AI Quality Gates**.

## 1. Sub-Skill Routing

Depending on the task, invoke the specialized sub-workflow:

| Task Type | Trigger / Intent | Sub-Skill to Load |
|---|---|---|
| **Poetry & Versification** | Writing poems, sonnets, dolnik, taktovik, kolomyika, editing rhymes, stress scansion, Ukrainian lyrical texts | `skills/ukrainian-poetry/SKILL.md` |
| **Multi-Platform AI Music Prompts** | Converting poems/briefs to Suno Custom Mode, Udio v4, Flow Music Lyria 3.5, style prompts, Western genre arrangements, metatags | `skills/ukrainian-poetry-to-suno/SKILL.md` |
| **End-to-End Songwriting & Production** | Generating Ukrainian lyrics + creating matching multi-platform prompts + DAW stem engineering roadmap | Execute **Poetry Workflow** first, then **Multi-Platform Music Conversion Workflow** |

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

### Multi-Platform AI Music Generation & Engineering (Meta-Spec v8)
- **Western Genre Anchor**: All sound design must strictly target Western genres (Post-Punk, Darkwave, Synthwave, Trip-Hop, Alt-Pop, Shoegaze, Progressive Metalcore, Melodic Techno, Ambient).
- **6-Step Production Lifecycle**:
  1. *Step 1 — Deep Reference Reverse Engineering*: Genre Hybrid, BPM Range (tempo anchor), Key/Tension, Sonic Aesthetic & Palette, Vocal Triple-Stack (**Character** + **Delivery** + **FX**), Melodic Math hooks.
  2. *Step 2 — AI-Optimized Lyrics Writing*: Syllable symmetry, Spoken Prosody Test, Staccato vs Legato spatial contrast, 5-Second Rule (`[Vocal Intro]`), 50-Second Chorus Rule. Cognitive melody limit $\le 3\text{--}4$.
  3. *Step 3 — Multi-Platform Prompt Engineering*:
     - **Suno AI (v4.5 / v5.5)**: Method 1 (Conversational Paragraph, «First 5 Words» rule) & Method 2 (HookGenius Tag-Based Matrix 5 modules); My Taste, Voices cloning, Custom Models; Failure mode fixes (Lyrics Rushing, Sterile Vocals, Negation Trap). Commercial rights on Pro/Premier.
     - **Udio AI (v4)**: 48 kHz stereo, 10 min continuous track, Context Length (10–15s vs max), Inpainting `*stars*`. Commercial rights on Pro ($30/mo).
     - **Google Flow Music (Lyria 3.5)**: Conversational Agent mode, Spaces, Turntable, Section-level Replace editing, AI Cover, Gemini Omni Flash synchronized video clips, 500 daily credits with commercial rights.
  4. *Step 4 — Step-by-Step Extensions Roadmap*: Seed 30–50s $\to$ Extend $\to$ Vance Powell Verse 2 development (`[Verse 2 - add driving tambourine, shaker, backing vocals]`) $\to$ Breakdown 15–20s & Mega-Chorus $\to$ Outro $\le 20$s.
  5. *Step 5 — Engineering DAW Stem Mixing*: Stem splitting, Kick/Bass phase alignment, dynamic frequency unmasking (Trackspacer/Neutron), Split Bass Compression (<200 Hz brickwall sub vs >200 Hz dynamic saturated), Tchad Blake parallel drum distortion directly to Master Fader (bypassing Drum Bus), dynamic Mid-Side vocal reverb sidechaining.
  6. *Step 6 — Mastering & Algorithmic Streaming Distribution*: Mastering without True Peak trap (-1 dBTP for -6..-8 LUFS with TP limiting OFF, or -14 LUFS for -2 dBTP); flexible genre Skip Rate thresholds (Pop >48%, Hip-hop >44%, Electronic >37%, Indie rock >31%, alarm >45%); abolish Playlist Placement Trap (direct ad spend strictly to singles); Spotify Canvas, Marquee, Discovery Mode.
- **Metatags & Brackets vs Parentheses**:
  - `[Square Brackets]`: Silent structural and arrangement directions (`[Intro]`, `[Vocal Intro]`, `[Verse 1]`, `[Pre-Chorus]`, `[Chorus]`, `[Verse 2 - add driving tambourine, shaker]`, `[Breakdown]`, `[Mega-Chorus]`, `[Outro]`).
  - `(Round Parentheses)`: Sung backing vocals and inline vocal delivery gestures `(whispered)`, `(belted)`, `(falsetto)`, `(screamed)`, `(ad-lib)`, `(building intensity)`, `(key change)`, `(half-time feel)`, `(harmonized)`, `(луна)`.
- **Ukrainian Stress Standard**: Capitalize the stressed vowel in words with non-obvious stress, homographs, and mobile accents (`вИпадок`, `чорнОзем`, `прИйде`, `заспівАй`, `моЯ`, `землЯ`, `зЕмлю`, `дорОга` vs `дорогА`, `зАмок` vs `замОк`, `плАчу` vs `плачУ`, `сердЕнько`).
- **10 AI Quality Gates**: Full verification across composition, prosody, prompt engineering, DAW mixing, and mastering.

---

## 3. Quick Reference

- Master Directives: `AGENTS.md`
- Poetic Guide: `skills/ukrainian-poetry/references/full-guide.md`
- 100-Point Poetic Rubric: `skills/ukrainian-poetry/references/rubric.md`
- Subagents Pipeline: `skills/ukrainian-poetry/agents/`
- Comprehensive AI Music Engineering Guide: `skills/ukrainian-poetry-to-suno/references/full-guide.md`
- Multi-Platform Prompt Builder: `skills/ukrainian-poetry-to-suno/references/prompt-builder.md`
- Reference & Style Cheatsheet: `skills/ukrainian-poetry-to-suno/references/reference-to-style-cheatsheet.md`
- Mood to Style Map: `skills/ukrainian-poetry-to-suno/references/mood-to-style-map.md`
- Song Structure & Metatag Pack: `skills/ukrainian-poetry-to-suno/references/song-structure-pack.md`
- Lyrics & Multi-Platform Templates: `skills/ukrainian-poetry-to-suno/references/lyrics-to-suno-template.md`
- Anti-Patterns & Failure Modes: `skills/ukrainian-poetry-to-suno/references/suno-prompt-anti-patterns.md`
- 100-Point Suno & Quality Gates Rubric: `skills/ukrainian-poetry-to-suno/references/rubric.md`
- Test Suite: `py -3 tests/run_tests.py --all`

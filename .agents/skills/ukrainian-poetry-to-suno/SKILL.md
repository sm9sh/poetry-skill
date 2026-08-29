---
name: ukrainian-poetry-to-suno
description: "Use when Codex needs to turn Ukrainian song ideas, poems, lyrics, moods, artist or song references, or rough briefs into multi-platform audio prompts (Suno v4.5/v5.5, Udio v4, Google Flow Music Lyria 3.5), custom mode blocks, reference breakdowns, DAW stem engineering checklists, mastering guidelines, or 10 AI Quality Gates verification."
---

# Multi-Platform AI Music Generation & Prompt Engineering (`ukrainian-poetry-to-suno`)

## Overview

Transform Ukrainian poetic material and song briefs into production-grade AI music prompts adhering to modern generative audio model mechanics across **Suno AI (v4.5 / v5.5)**, **Udio AI (v4)**, and **Google Flow Music (Lyria 3.5)**, complete with DAW stem engineering and algorithmic streaming distribution standards.

**Core Musical Rule — Western Genre Orientation**:
All musical sound design, genres, production standards, and reference frameworks must be strictly oriented toward **Western contemporary and classic music genres** (US/UK/Nordic/European indie, synthwave, darkwave, post-punk, trip-hop, alternative rock, shoegaze, progressive metalcore, melodic techno, cinematic ambient, neo-soul, modern electro-pop). The resulting track must sound like a top-tier Western release with authentic Ukrainian lyrics, strictly preventing regional cheesy pop, post-Soviet schlager, or tourist-folk kitsch (*шароварщина*).

Maintain strict separation between poetic text generation and music prompt engineering. If the user requires lyrics first, invoke the Ukrainian poetry versification workflow before generating multi-platform configuration blocks.

---

## The 6-Step Production Lifecycle Architecture

```text
[ВХІД: Ідея користувача + Референси (трек / артист)]
                    │
                    ▼
 ┌─────────────────────────────────────────────────────────┐
 │ Крок 1: Глибока деконструкція референсів (Track/Artist) │
 │ ─ Жанровий гібрид, темп (BPM), тональність і напруга    │
 │ ─ Звуковий ландшафт, тембри, текстура аналогового запису│
 │ ─ Вокальний Triple-Stack (Персонаж + Подача + Ефект)    │
 │ ─ Melodic Math: Melodic Previews, Glue Hooks, Nano Hooks│
 └─────────────────────┬───────────────────────────────────┘
                       │
                       ▼
 ┌─────────────────────────────────────────────────────────┐
 │ Крок 2: AI-Оптимізоване написання лірики (Lyrics Sheet) │
 │ ─ Складова симетрія (8-8-8-8 / 10-8-10-8) + Downbeats   │
 │ ─ Тест розмовним ритмом (Spoken Prosody Test)           │
 │ ─ Секційний контраст: Verse Staccato vs Chorus Legato   │
 │ ─ 5-Second Rule ([Vocal Intro]) та «Правило 50 секунд»  │
 │ ─ Когнітивний ліміт мелодій (<= 3-4 на весь трек)       │
 └─────────────────────┬───────────────────────────────────┘
                       │
                       ▼
 ┌─────────────────────────────────────────────────────────┐
 │ Крок 3: Інжиніринг промптів та метатегів стилю          │
 │ ─ Suno v4.5/v5.5: Method 1 Conversational & Method 2 Tag│
 │ ─ Udio v4: 48kHz, Context Length (10-15s vs max), *stars*│
 │ ─ Flow Music (Lyria 3.5): Conversational Agent, Spaces  │
 │ ─ Бібліотека метатегів [] та інлайн-жестів у ()         │
 └─────────────────────┬───────────────────────────────────┘
                       │
                       ▼
 ┌─────────────────────────────────────────────────────────┐
 │ Крок 4: Дорожня карта покрокової генерації (Extensions) │
 │ ─ Seed (30-50s): Hook-first вступ (Anti-skip 5s)        │
 │ ─ Verse 2 development за Венсом Пауеллом (Tambourine+)  │
 │ ─ Breakdown (15-20s) та фінальний Mega-Chorus           │
 │ ─ Лаконічне Outro (<= 20s) для глибини дослуховування   │
 └─────────────────────┬───────────────────────────────────┘
                       │
                       ▼
 ┌─────────────────────────────────────────────────────────┐
 │ Крок 5: Інженерна DAW-обробка та зведення AI-стемів     │
 │ ─ Stem splitting (Moises, RipX, LALAL.AI)               │
 │ ─ Фазова оптимізація Kick & Bass (Mono check / FUSER)   │
 │ ─ Частотне розмаскування (Dynamic Sidechain Trackspacer)│
 │ ─ Split Bass Compression (<200Hz sub vs >200Hz dynamic) │
 │ ─ Тчад Блейк паралельний дисторшн барабанів на Master   │
 │ ─ Динамічний вокальний Mid-Side Reverb sidechaining     │
 └─────────────────────┬───────────────────────────────────┘
                       │
                       ▼
 ┌─────────────────────────────────────────────────────────┐
 │ Крок 6: Мастеринг та Алгоритмічна Дистрибуція          │
 │ ─ Мастеринг: усунення TP-пастки (-1 dBTP для -6..-8LUFS)│
 │ ─ Жанрові пороги Skip Rate (Pop>48%, Hip-hop>44%, ...)  │
 │ ─ Ліквідація Playlist Placement Trap (Single-only ads)  │
 │ ─ Промо-інструменти Spotify: Canvas, Marquee, Discovery │
 └─────────────────────────────────────────────────────────┘
```

---

## Multi-Platform Prompt Engineering Matrices

### 1. Suno AI (v4.5 / v5.5)
- **Технічні ліміти**: `Style of Music` — до 1000 символів (оптимально **80–180 символів** або 8–15 точних тегів); `Lyrics` — до 5000 символів.
- **Метод 1: «Conversational Paragraph»**: Цілісний опис стилю англійським абзацом за правилом **«First 5 Words»** (80% уваги нейромережі на перших 4–5 словах):
  - *Формула*: `[Genre & Subgenre] + [Vocal Character] + [Instruments] + [Mood/Energy] + [Aesthetic & BPM]`
  - *Приклад*: `Alternative rock, passionate dry male tenor vocals, gritty garage guitars, warm analog bass, tape saturation, dark melancholic mood, 115 BPM.`
- **Метод 2: «Tag-Based Matrix» (Формула HookGenius)**:
  - *Формула 5 модулів*: `[1. Genre/Subgenre], [2. Mood/Energy], [3. Vocal Triple-Stack], [4. Lead Instruments], [5. Production Aesthetic, BPM]`
  - *Приклад*: `indie rock, melancholic, raspy male vocals, intimate close-up delivery, dry mic, clean electric guitar, driving melodic bass, live drum kit, lo-fi tape hiss, 115 BPM` (168 chars)
- **Системні функції v5.5**: *My Taste* (персональний стиль), *Voices* (вокальне клонування на Pro/Premier), *Custom Models* (до 3 кастомних моделей).
- **Усунення Failure Modes**:
  - *Lyrics Rushing*: рядки по 4–8 слів, помірний BPM, інлайн-команда `(half-time feel)`.
  - *Sterile Vocals*: обов'язковий вокальний Triple-Stack (**характер** + **подача** + **ефекти**).
  - *The Negation Trap*: жодних заперечень ("no drums"); використовувати позитивну гіперспецифічність: `purely acoustic, solo piano, isolated vocals, sparse`.
- **Комерційні права**: Доступні на тарифах **Pro ($10/міс)** та **Premier ($30/міс)**.

### 2. Udio AI (v4)
- **Технічні параметри**: Якість аудіо **48 кГц стерео**, генерація безперервного треку **до 10 хвилин**, глибина розширення (Context Length) **до 15 хвилин**.
- **Формула промпту**: `[Main Genre], [Sub-Genre], [Year/Era], [Vocal Timbre & Character], [Analog Production Style], [Acoustic Space, BPM]` (до 250 символів).
- **Керування Context Length**: 10–15 секунд для різких жанрових/мовних переходів; максимальний контекст для безшовної спадковості.
- **Inpainting вокалу**: Виділення фрагмента на хвильовій формі та взяття слів для заміни в зірочки `*static sky*` у полі лірики.
- **Комерційні права**: Тільки на тарифі **Pro ($30/міс)** (Standard $10/міс не надає комерційних прав).

### 3. Google Flow Music (Модель DeepMind Lyria 3.5)
- **Технічний статус**: Працює на базі моделі **Lyria 3.5** від Google DeepMind. Безкоштовний тариф надає **500 кредитів щодня** з повними комерційними ліцензіями (сервіси MusicFX закрито 31 липня 2026).
- **Формула промпту (Conversational Agent Mode)**:
  `[Опис концепту і стилю] + [Референс атмосфери] + [Специфікація інструментів] + [Керування динамікою і вокалом]`
- **Унікальні можливості**:
  - *Spaces*: Створення інтерактивних музичних браузерних додатків та біт-мейкерів.
  - *Turntable*: DJ-мікшування, зміна бітів на льоту, live-семплування.
  - *Section-Level Replace*: Виділення будь-якого таймкоду (наприклад, 1:12–1:35) і заміна вокалу, мови чи інструменту без перезапису всього треку.
  - *AI Cover*: Повне переаранжування мелодії в новий жанровий стиль.
  - *Gemini Omni Flash Video Sync*: Автоматична генерація та синхронізація музичного кліпу з монтажними склейками за темпом та емоцією треку.

---

## Metatag Grammar & Inline Vocal Gestures Library

```text
┌─────────────────────────┬──────────────────────────────────────────┬────────────────────────────────────────────────────────┐
│ Синтаксис               │ Як інтерпретує аудіо-модель              │ Приклад правильного використання                       │
├─────────────────────────┼──────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ [Квадратні дужки]       │ Неспіваний метатег / звукова вказівка    │ [Vocal Intro - dynamic acapella, dry and close],       │
│                         │ (структура, інструменти, динаміка)       │ [Beat Drop - heavy fuzz bass], [Verse 2], [Mega-Chorus]│
├─────────────────────────┼──────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ (Круглі дужки)          │ Співаний бек-вокал / вокальні жести      │ (whispered), (belted), (falsetto), (screamed),         │
│                         │ УВАГА: Flow Music та Suno співають ()!   │ (ad-lib), (building intensity), (key change),          │
│                         │                                          │ (half-time feel), (harmonized), (луна), (ніколи знов)  │
├─────────────────────────┼──────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ ВЕЛИКІ ЛІТЕРИ ГОЛОСНИХ  │ Фіксація точного наголосу для ШІ-вокалу  │ вИпадок, чорнОзем, прИйде, заспівАй, моЯ, дорОга       │
├─────────────────────────┼──────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ *Зірочки*               │ Udio Inpainting синтаксис заміни слів    │ *static sky* (виключно в Udio; уникати в Suno/Flow)    │
└─────────────────────────┴──────────────────────────────────────────┴────────────────────────────────────────────────────────┘
```

### 9 Канонічних інлайн вокальних жестів у `(...)`
1. `(whispered)` / `(whispered, intimate)` — Інтимний шепіт біля мікрофона (Verse 1, Breakdown).
2. `(belted)` / `(belted, powerful)` — Потужний відкритий грудний вокал на емоційному піку (Chorus).
3. `(falsetto)` — Перехід на фальцет для створення емоційної крихкості.
4. `(screamed)` / `(growl)` — Агресивна вокальна експресія (Metalcore, Post-Punk).
5. `(ad-lib)` / `(vocal runs)` — Вокальні мелізми та фонова імпровізація.
6. `(building intensity)` — Поступове наростання гучності та вокального тиску.
7. `(key change)` — Тональна модуляція для фінального вибуху приспіву.
8. `(half-time feel)` — Уповільнення ритму фразування вокалу вдвічі (усуває вокальну скоромовку).
9. `(harmonized)` / `(layered harmonies)` — Багатоголосся на ключовому слові хука.

---

## 8-Жанрова таксономія західного продакшну

| # | Жанр & Західні орієнтири | Style Prompt Formula (80–180 Chars) | Anti-Local-Pop Exclude Vector |
|---|--------------------------|-------------------------------------|--------------------------------|
| **1** | **Post-Punk / Darkwave / Coldwave**<br>*(Joy Division, The Cure, Boy Harsher)* | `british post-punk, darkwave, chorus electric guitar, 80s drum machine, driving bassline, melancholic baritone male vocal, lo-fi nocturnal, 128 bpm` | `cheesy regional pop, wedding synth brass, cheerful accordion, schlager, autotune pop` |
| **2** | **Dark Synthwave / EBM / Cyberpunk**<br>*(Depeche Mode, Carpenter Brut, Perturbator)* | `dark synthwave, analog moog bass pulse, gated 80s snare, crisp electronic arpeggios, monotone male vocal, cyberpunk nocturnal, 120 bpm` | `acoustic folk, post-soviet pop, live accordion, polka, cheesy brass` |
| **3** | **Trip-Hop / Downtempo / Bristol Sound**<br>*(Massive Attack, Portishead, Morcheeba)* | `trip-hop, downtempo, dusty vinyl breakbeat, warm rhodes piano, deep 808 sub bass, breathy female vocal, cinematic tape warmth, 85 bpm` | `cheesy euro-pop, fast edm drop, aggressive screaming, generic midi drums` |
| **4** | **Modern Alt-Pop / Dark Electro-Pop**<br>*(Billie Eilish, Lorde, Banks, FINNEAS)* | `minimalist alt-pop, heavy 808 sub bass, crisp close-mic breathy female vocal, organic foley percussions, dark spatial production, 100 bpm` | `tourist folk cliches, cheesy polka accordion, 90s eurodance, brass fanfare` |
| **5** | **Progressive Metalcore / Modern Djent**<br>*(Bring Me The Horizon, Architects, Spiritbox)*| `modern progressive metalcore, drop-tuned djent guitar riffs, punchy aggressive drums, brutal screaming alternating ethereal clean vocal, 150 bpm`| `mumble vocal, cheap pop synth brass, acoustic ukulele, dance club beat` |
| **6** | **Shoegaze / Dream Pop / Indie Rock**<br>*(Slowdive, Beach House, Arctic Monkeys)*| `shoegaze, dream pop, wall of sound reverb guitars, jangly indie groove, whispered breathy vocal, lush vintage chorus, atmospheric slow groove, 90 bpm` | `harsh digital clipping, aggressive rap, dry close mix, stadium shouting` |
| **7** | **Melodic Techno / Ambient Electronica**<br>*(Bicep, Moderat, Jon Hopkins)* | `melodic techno, electronica, hypnotic analog arpeggios, atmospheric vocal chops, deep rolling sub bass, four-on-the-floor groove, 124 bpm` | `cheap midi brass, wedding accordion, tourist folk, acoustic strumming` |
| **8** | **Cinematic Ambient / Neoclassical**<br>*(Hans Zimmer, Max Richter, Ólafur Arnalds)* | `contemporary cinematic ambient, felt upright piano, emotive soaring cello, warm tape saturation, intimate whispered vocal, 70 bpm` | `electronic drums, distorted guitars, aggressive shouting, festival drop, local pop` |

---

## Vocal Triple-Stack Formula

Завжди комбінуйте три складові опису вокалу:
- **Характер (Character)**: `raw passionate male tenor`, `fragile breathy female soprano`, `deep melancholic baritone`, `authentic white voice`.
- **Подача (Delivery)**: `intimate, dry, conversational close-mic`, `deadpan monotone recitative`, `soaring anthemic belting`.
- **Ефекти та Простір (FX & Space)**: `sansamp vocal saturation, tape slap delay, dry upfront mix, subtle room plate`.

---

## Step 4: Дорожня карта генерації (The AI Conductor)

1. **Seed (30–50s)**: Вокальний вступ (`[Vocal Intro - dynamic acapella, dry]`) для виконання правила 5 секунд та захисту від skip-rate. Перевірка темпу та груву.
2. **Extend 1 (Verse & Pre-Chorus)**: Розгін до першого приспіву; обов'язкова поява приспіву до 50-ї секунди треку.
3. **Extend 2 (Verse 2 Development за Венсом Пауеллом)**: Оновлення промпту метатегом:
   `[Verse 2 - add driving tambourine, syncopated backing vocals, stereo guitar riffs]`.
4. **Extend 3 (Breakdown & Mega-Chorus)**: 15–20 секунд спаду енергії `[Breakdown - vocal and sub-bass only]` перед фінальним вибухом `[Mega-Chorus - maximum energy, layered harmonies, guitars clashing]`.
5. **Extend 4 (Outro)**: Лаконічне аутро $\le 20$s (`[Outro - dynamic fading vocal]`, `[End]`).

---

## Step 5: Чек-лист для інженерного DAW-зведення стемів

1. **Stem Splitting**: Розбиття треку на Vocals, Bass, Drums, Other через Moises Pro, RipX або LALAL.AI.
2. **Phase Alignment**: Зведення бочки та басу в моно, перевірка інверсії полярності ($180^\circ$) або застосування *Sound Radix Auto-Align / FUSER* для максимального панчу.
3. **Dynamic Unmasking**: Динамічний сайдчейн-еквалайзер (*Trackspacer* на 10–25% або *Neutron Unmask*) на басі, керований від Kick.
4. **Bass Split Compression**:
   - *Sub-Bass (<200 Hz)*: Brickwall limiting з 3–6 dB пригнічення для кам'яної стабільності низу.
   - *Mid-High Bass (>200 Hz)*: Аналогова сатурація (*Decapitator / Saturn 2*) та динамічна компресія (*1176* 4:1) для виразності атаки струн.
5. **Tchad Blake Parallel Drum Distortion**: Сильно сатуровані барабани (*SansAmp / Devil-Loc*) направляються **безпосередньо на Master Fader**, оминаючи Drum Bus для збереження headroom.
6. **Dynamic Mid-Side Reverb Sidechaining**: Сайдчейн-компресор на вокальній реверберації, керований від Lead Vocal (пригнічення 3–6 dB), у режимі **Mid-Side** (пригнічується тільки центр, стерео-боки залишаються широкими).

---

## Step 6: Мастеринг та Алгоритмічна Дистрибуція

1. **Мастеринг без True Peak пастки**:
   - Для гучних сучасних майстрів ($-6\dots-8\text{ LUFS}$): **вимкнути True Peak лімітування** та встановити стелю лімітера на **-1 dBTP** (або -0.2 dB).
   - Якщо платформа суворо вимагає -2 dBTP: цільова гучність має бути знижена до **-14 LUFS** (або -8 LUFS).
2. **Spotify 2026 Skip Rate пороги**:
   - Поп: критично $> 48\%$
   - Хіп-хоп: критично $> 44\%$
   - Електроніка: критично $> 37\%$
   - Інді-рок: критично $> 31\%$
   - **Універсальний поріг тривоги**: $> 45\%$ повністю закриває алгоритмічні плейлисти (*Discover Weekly*, *Radio*).
3. **Метрики утримання**: Completion Rate $> 55\text{--}60\%$ (довжина треку 2:30–4:00 хв), Save Rate $\ge 20\%$.
4. **Ліквідація Playlist Placement Trap**: Рекламний трафік (Meta/TikTok Ads) спрямовується **виключно на цільовий сингл**, а не на плейлист артиста.
5. **Промо-інструменти**: Spotify Canvas (8с відео, +5% завершення), Marquee (15% конверсія наміру), Discovery Mode.

---

## The 10 AI Quality Gates Matrix

| № | Назва гейту | Метод контролю / Стандарт якості | Усунення помилки |
| :--- | :--- | :--- | :--- |
| **Gate 1** | **Анти-Skip (Перші 5с)** | Живий голос або хук у перші 5 секунд. | Перегенерувати Seed з `[Vocal Intro - dynamic acapella]`. |
| **Gate 2** | **«Правило 50 секунд»** | Головний приспів звучить $\le 50$ секунд. | Скоротити Verse 1, прибрати зайві рядки. |
| **Gate 3** | **Просодія та наголоси** | Тест розмовним ритмом; великі літери на наголосах (`вИпадок`, `дорОга`). | Збалансувати склади; Udio Inpainting `*words*` / Flow Replace. |
| **Gate 4** | **Контраст простору** | Verse Staccato (гостро) vs Chorus Legato (широко `Ooooh, Aaah`). | Додати відкриті голосні; тег `[Chorus - explosive open wide space]`. |
| **Gate 5** | **Розвиток 2-го куплету** | Verse 2 додає нові інструменти (перкусія, бек-вокал, гітари). | Extend після 1-го приспіву з `[Verse 2 - add driving tambourine, shaker, backing vocals]`. |
| **Gate 6** | **Breakdown & Mega-Chorus** | 15–20с спад енергії перед вибуховим кульмінаційним приспівом. | Перегенерувати фінал: `[Breakdown]` $\to$ `[Mega-Chorus - maximum energy]`. |
| **Gate 7** | **Low-End Split Bass (DAW)** | Бас розділено на Sub (<200Hz) та Mid-High (>200Hz); сайдчейн від Kick. | Split Compression + Trackspacer по сайдчейну від бочки. |
| **Gate 8** | **Тчад Блейк дисторшн (DAW)** | Паралельний дисторшн барабанів йде на Master Fader (повз Drum Bus). | Перенаправити аукс дисторшну барабанів на Master Fader. |
| **Gate 9** | **Мастеринг True Peak** | -1 dBTP для -6..-8 LUFS з вимкненим TP лімітуванням (або -14 LUFS для -2 dBTP). | Вимкнути TP лімітування; ceiling на -1 dBTP або знизити майстер до -14 LUFS. |
| **Gate 10**| **Рекламний трафік** | Реклама спрямовується виключно на цільовий сингл (без плейлист-пастки). | Перенаправити рекламу на смарт-посилання окремого треку. |

---

## Output Modes

### 1. Suno Custom Mode Output (Method 1 & Method 2)
```text
Style of music (Method 1 - Conversational):
<Genre & Subgenre>, <Vocal Triple-Stack>, <Key Instruments>, <Mood/Energy>, <Aesthetic & BPM> (80-180 chars)

Style of music (Method 2 - HookGenius Tag Matrix):
<1. Genre/Subgenre>, <2. Mood/Energy>, <3. Vocal Triple-Stack>, <4. Lead Instruments>, <5. Aesthetic & BPM> (80-180 chars)

Lyrics:
[Vocal Intro - dynamic acapella, dry and close]
(Почуй цей шУм у вен... ах)
[Beat Drop - heavy fuzz bass, punchy driving drums]

[Verse 1 - rhythmic staccato, intimate delivery]
<Українські рядки з наголосами: вИпадок, дорОга, моЯ>
(whispered) <інтимний шепіт>
(луна у тИші)

[Pre-Chorus - building intensity, rising snare]
<Рядки передприспіву>
(building intensity)

[Chorus - explosive open wide space, soaring vocal]
<Широкі відкриті голосні legato: Оооо, Аааа>
(belted) <потужний відкритий вокал>
(layered harmonies)

[Verse 2 - add driving tambourine, shaker, backing vocals]
<Розвиток аранжування другого куплету за Венсом Пауеллом>

[Chorus]
<Приспів>

[Breakdown - vocal and sub-bass only, intimate, dry]
(whispered) <15-20 секунд спаду енергії>

[Mega-Chorus - maximum energy, layered harmonies, guitars clashing]
(key change) <Кульмінаційний вибух>
(belted, powerful)

[Outro - dynamic fading vocal, tape hiss]
[End]

Exclude:
cheesy regional pop, post-soviet schlager, wedding synth brass, cheap accordion, metallic highs, harsh sibilance, muddy bass
```

### 2. Udio v4 Mode Output
```text
Prompt (Udio v4):
<Main Genre>, <Sub-Genre>, <Year/Era>, <Vocal Timbre & Character>, <Analog Production Style>, <Acoustic Space, BPM>

Context Length:
10-15 seconds for transitions / Max for continuity

Inpainting Replacement:
*words to replace*
```

### 3. Google Flow Music Conversational Agent Output
```text
Flow Music Prompt (Lyria 3.5):
Create a modern <Western Genre> song with <Vocal Triple-Stack> inspired by the atmospheric tension of <Western Benchmark>. Instrumentation features <Analog Instruments>. The track opens with an intimate vocal acapella hook, explodes into a punchy beat drop, builds into a wide soaring chorus within 45 seconds, drops into an intimate breakdown, and finishes with an epic mega-chorus.
```

---

## Pre-Generation Quality Checklist

Перед фіналізацією перевірте:
- [ ] Виконано **6-етапний життєвий цикл** та враховано **10 AI Quality Gates**.
- [ ] `Style of music` строго **80–180 символів** (англійські токени, без метаданих).
- [ ] Жанровий фундамент — **західний продакшн** (Post-Punk, Darkwave, Trip-Hop, Alt-Pop, Metalcore тощо).
- [ ] Текст містить **великі літери на наголошених голосних** (`вИпадок`, `дорОга`, `моЯ`).
- [ ] Всі аранжувальні вказівки у **квадратних дужках `[...]`**, а бек-вокали та жести у **круглих дужках `(...)`**.
- [ ] Відсутній витік імен реальних артистів у стильові поля.

---

## Reference Ecosystem Index

| Призначення | Канонічний документ |
|---|---|
| Повний вичерпний посібник (10 розділів) | `references/full-guide.md` |
| Модульний конструктор промптів (Suno / Udio / Flow) | `references/prompt-builder.md` |
| Матриця відповідності емоцій та стилів | `references/mood-to-style-map.md` |
| Шпаргалка референсів та деперсоналізації | `references/reference-to-style-cheatsheet.md` |
| Каталог структур пісень та метатегів | `references/song-structure-pack.md` |
| Готові шаблони лірики та Custom Mode | `references/lyrics-to-suno-template.md` |
| Посібник з антипатернів та помилок генерації | `references/suno-prompt-anti-patterns.md` |
| 100-бальна рубрика та валідація Quality Gates | `references/rubric.md` |
| 24+ автентичні українські пісенні сценарії | `references/ukrainian-song-scenarios.md` |
| Спеціалізовані промпт-паки (7 паків) | `references/packs/README.md` |
| Тестовий набір | `references/tests.md` |

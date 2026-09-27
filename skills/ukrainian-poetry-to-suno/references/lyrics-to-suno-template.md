# Lyrics To Suno, Udio & Google Flow Music Custom Mode Templates (v8)

Універсальні шаблони для перетворення українських віршів, пісенних текстів, референсів та творчих брифів у готові конфігурації для **Suno AI (v6-mini)**, **Udio AI (v4)** та **Google Flow Music (Lyria 3.5)**.

> [!IMPORTANT]
> **Золоте правило синтаксису дужок та наголосів**:
> - **Квадратні дужки `[ ... ]`**: призначені виключно для метатегів, структури, звукових ефектів та інструментальних вказівок (`[Vocal Intro - dynamic acapella, dry]`, `[Beat Drop]`, `[Verse 2 - add driving tambourine, shaker]`, `[Breakdown]`, `[Mega-Chorus]`, `[Outro]`). Аудіомоделі обробляють їх як німі музичні команди!
> - **Круглі дужки `( ... )`**: тільки те, що має **прозвучати голосом** — бек-вокал та ехо слів (`(ніколи знов)`, `(о-о-о)`). Suno та Flow Music співають усе, що в круглих дужках, тому вказівки подачі (`[Whispered]`, `[Belted]`, `[Falsetto]`, `[Key Change]`, `[Half-time feel]`) і будь-які інструменти пишуться лише в квадратних дужках.
> - **Наголоси у тексті (`вИпадок`, `дорОга`)**: щоб запобігти зсуву наголосу моделлю при генерації вокалу, виділяйте наголошену голосну **великою літерою** лише у трьох категоріях: омографи (`дорОга` vs `дорогА`, `зАмок` vs `замОк`, `плАчу` vs `плачУ`), слова, які модель вимовляє по-російськи (`вИпадок`, `чорнОзем`, `листопАд`), та неочевидні зсуви у відмінках (`зЕмлю`, `рУку`). Службові й очевидні слова (`моя`, `земля`, `прийде`, `заспівай`) не позначайте.
> - **Udio Inpainting `*stars*`**: для точкової заміни слів у Udio v4 використовуйте зірочки (`*static sky*`).

---

## 1. Головний мультиплатформний шаблон (Master Copy-Paste Template)

```text
======================= SUNO AI (v6-mini) =======================
Style of music (Method 1 - Conversational):
<Genre & Subgenre>, <Vocal Triple-Stack>, <Key Instruments>, <Mood/Energy>, <Aesthetic & BPM> (80-180 chars)

Style of music (Method 2 - HookGenius Tag Matrix):
<1. Genre/Subgenre>, <2. Mood/Energy>, <3. Vocal Triple-Stack>, <4. Lead Instruments>, <5. Production Aesthetic, BPM> (80-180 chars)

Lyrics:
[Vocal Intro - dynamic acapella, dry and close]
(Почуй цей шум у наших венах...)
[Beat Drop - heavy fuzz bass, punchy driving drums]

[Verse 1 - rhythmic staccato, intimate delivery]
<Рядки першого куплету; великі літери лише в омографах / пастках / зсувах: вИпадок, дорОга, зЕмлю>
[Whispered] <інтимний шепіт>
(у тиші)

[Pre-Chorus - building intensity, rising snare roll]
<Передприспів: наростання напруги>
[Building intensity]

[Chorus - explosive open wide space, soaring vocal]
<Широкі відкриті голосні legato: Оооо, Аааа>
[Belted] <потужний відкритий вокал>
[Layered harmonies]

[Verse 2 - add driving tambourine, syncopated backing, sharp guitars]
<Розвиток аранжування другого куплету за Венсом Пауеллом>
[Half-time feel]

[Chorus]
<Приспів>

[Breakdown - vocal and sub-bass only, intimate, dry]
[Whispered] <15-20 секунд спаду енергії>

[Mega-Chorus - maximum energy, layered harmonies, guitars clashing]
[Key Change] <Кульмінаційний вибух>
[Belted, powerful]
[Layered harmonies]

[Outro - dynamic fading vocal, tape hiss]
[End]

Exclude:
cheesy regional pop, post-soviet schlager, wedding synth brass, cheap accordion, metallic highs, harsh sibilance, muddy bass

========================== UDIO AI (v4) ==========================
Prompt:
<Main Genre>, <Sub-Genre>, <Year/Era>, <Vocal Timbre & Character>, <Analog Production Style>, <Acoustic Space, BPM>

Context Length:
10-15 seconds for transitions / Max for continuity

Inpainting Syntax:
*words to replace*

================== GOOGLE FLOW MUSIC (LYRIA 3.5) ==================
Prompt (Conversational Agent):
Create a modern <Western Genre> song with <Vocal Triple-Stack> inspired by <Western Benchmark>. Instrumentation features <Analog Instruments>. The track opens with an intimate vocal acapella hook, explodes into a punchy beat drop, builds into a wide soaring chorus within 45 seconds, drops into an intimate breakdown, and finishes with an epic mega-chorus.
```

---

## 2. Дорожня карта покрокової генерації (The AI Conductor Roadmap)

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ Крок 1: The Seed (0:00 - 0:40)                                                         │
│ ─ Генерація вступу з вокальним хуком [Vocal Intro] (The 5-Second Rule).                │
│ ─ Перевірка темпу, ритму та відсутності скіп-тригерів.                                 │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Крок 2: Extend 1 — Verse & Chorus (0:40 - 1:20)                                        │
│ ─ Перший приспів обов'язково звучить до 50-ї секунди треку («Правило 50 секунд»).      │
│ ─ Контраст Staccato у куплетах та широкого Legato у приспіві.                         │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Крок 3: Extend 2 — Verse 2 Development (1:20 - 2:10)                                   │
│ ─ Оновлення метатегу: [Verse 2 - add driving tambourine, shaker, backing vocals].      │
│ ─ Запобігання монотонності та слухової втоми за правилами Венса Пауелла.               │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Крок 4: Extend 3 — Breakdown & Mega-Chorus (2:10 - 3:15)                               │
│ ─ Скидання інструментальної енергії на 15–20 секунд: [Breakdown - vocal and bass only].│
│ ─ Вибух у кульмінаційний [Mega-Chorus] з модуляцією [Key Change] та багатоголоссям.    │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Крок 5: Extend 4 — Лаконічне Outro (3:15 - 3:35)                                       │
│ ─ Коротка кода [Outro] тривалістю <= 20 секунд для збереження глибини дослуховування.  │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Шаблони за типами вхідних даних

### Шаблон А: З готового українського вірша
```text
Перетвори цей український вірш у мультиплатформенний пакет (Suno v6-mini, Udio v4, Flow Music Lyria 3.5).

Параметри:
- Бажаний західний жанр: <Post-Punk | Dark Synthwave | Trip-Hop | Alt-Pop | Metalcore | Shoegaze | Techno | Ambient>
- Темп / BPM: <наприклад, 125 bpm>
- Vocal Triple-Stack: <Характер + Подача + Ефект>
- Уникати: <шароварщина, пафос, металевий бруд, гудіння басу>

Текст вірша:
<встав текст>
```

---

### Шаблон Б: З теми та настрою (без готового тексту)
```text
Створи повну пісенну структуру та мультиплатформенні промпти для українського треку за 6-етапним життєвим циклом v8.

- Тема: <тема треку>
- Настрій / Емоційне ядро: <емоція>
- Західний музичний орієнтир: <жанр / піджанр>
- Вокальний архетип: <Vocal Triple-Stack>
- Анти-стиль: <чого не повинно бути>

Поверни:
1. Деконструкцію референсу (BPM, тональність, хуки).
2. Suno v6-mini Prompts (Method 1 Conversational & Method 2 HookGenius Tag Matrix).
3. Udio v4 Prompt (з Context Length & Inpainting).
4. Google Flow Music Prompt (Lyria 3.5).
5. Lyrics Sheet з розміткою [] та інлайн-жестами ().
6. Дорожню карту Extend.
7. Чек-лист DAW-зведення стемів.
```

---

### Шаблон В: З музичного референса (артист / трек)
```text
У мене є музичний референс, але в фінальному prompt'і заборонено згадувати імена артистів або назви треків.

Референс:
- Артист: <artist>
- Трек: <track>

Потрібно:
1. Провести деконструкцію звукового ДНК (BPM, тональність, тембри, вокальний Triple-Stack, анатомія хуків).
2. Скласти деперсоналізований Safe Style Prompt для Suno, Udio та Flow Music.
3. Написати український текст із дотриманням 6 принципів поезії, складової симетрії, наголосів великими літерами та розмітки [].
4. Додати дорожню карту розширень та інженерний чек-лист DAW-зведення.
```

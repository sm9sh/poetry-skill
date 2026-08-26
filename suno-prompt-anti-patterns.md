# Suno AI Prompt Anti-Patterns & Audio Artifact Guide

Повний посібник із типових помилок промптингу в `Suno AI` (v3.5 / v4) та інструкції з їх виправлення.

---

## 1. Топ-10 анти-патернів у Suno Prompting

### 1. Переповнення токенів та розсіювання уваги (Token Overflow & Dilution)
- **Помилка**: Написання довгих есе та прикметникових ланцюгів на 300–600 символів у полі `Style of music`.
- **Чому це ламає генерацію**: Модель має обмежене вікно крос-уваги (*cross-attention*). Перенасичення тегами призводить до "усереднення" стилю (*style averaging*) у безликий поп-рок або втрати контролю над інструментами.
- **Погано (310 символів)**:
  ```text
  A very beautiful deeply emotional epic atmospheric dark nocturnal melodic cinematic indie pop song with huge wide guitars, warm gentle piano accents, deep bass, punchy live drums, soft airy vocal, wonderful reverb, and dramatic buildup into an unbelievable stadium chorus with lots of synth layers and nice feeling.
  ```
- **Добре (135 символів)**:
  ```text
  ukrainian indie pop, dark nocturnal atmosphere, 110 bpm, intimate airy female vocal, pulsing bass, muted drum machine, soft analog synths
  ```

---

### 2. Витік метаданих у поле стилю (Metadata Leakage)
- **Помилка**: Розміщення службових полів (`Language: Ukrainian`, `Theme: night tram`, `Mood: sad`, `BPM: 120`) всередині поля `Style of music`.
- **Чому це ламає генерацію**: Модель сприймає службові слова як музичні теги або галюцинує їх у вокальний текст, забираючи корисні токени стилю.
- **Погано**:
  ```text
  ukrainian indie pop. Language: Ukrainian. Theme: night city, rain, loneliness. Mood: melancholic.
  ```
- **Добре**:
  ```text
  ukrainian indie pop, melancholic nocturnal atmosphere, 115 bpm, intimate female vocal, warm bass, muted drums, rainy street mood
  ```
  *(А сам український текст розміщується суто в полі `Lyrics`).*

---

### 3. Парадокс локалізації стилю (The Localization Paradox)
- **Помилка**: Написання музичних тегів у полі `Style of music` українською мовою (*"Меланхолійний середньотемповий інді-поп, теплий бас..."*).
- **Чому це ламає генерацію**: Музичний енкодер Suno натренований переважно на англомовних тегах. Український текст у полі стилю викликає деградацію аудіо, поганий підбір інструментів або випадковий синтезаторний шум.
- **Правило**: Текст пісні в `Lyrics` — українською мовою. Дескриптори в `Style of music` — англійською (із збереженням автентичних назв інструментів: `bandura`, `sopilka`, `tsymbaly`, `duda`).

---

### 4. Неструктуровані ASCII-стрілки замість метатегів
- **Помилка**: Використання схем виду `intro -> verse -> chorus -> outro` у тексті пісні або стилі.
- **Чому це ламає генерацію**: Парсер Suno не розпізнає стрілочки `->`. Співак спробує проспівати слова "інтро верс приспів" або проігнорує переходи.
- **Добре**: Використовувати офіційні квадратні дужки: `[Intro]`, `[Verse 1]`, `[Pre-Chorus]`, `[Chorus]`, `[Bridge]`, `[Outro]`, `[End]`, та круглі дужки для бек-вокалу: `(луна у тиші)`.

---

### 5. Конфліктний стильовий стек (Contradictory Style Stack)
- **Помилка**: Змішування взаємовиключних жанрів та енергій.
- **Погано**:
  ```text
  minimal acoustic dark pop aggressive EDM folk metal stadium anthem
  ```
- **Добре**: Обрати 1 головний жанр і максимум 1 суміжний гібридний вектор:
  ```text
  ukrainian ethno-chaos, avant-folk, white voice chanting, acoustic cello drone, tribal percussion, 120 bpm
  ```

---

### 6. Прямий неймінг та копіювання артистів (Copyright Risk)
- **Помилка**: Вживання прямих імен артистів або назв треків (`in the style of DakhaBrakha`, `sound like Jinjer`).
- **Чому це ламає генерацію**: Suno блокує або спотворює прямі імена артистів через вбудовані фільтри безпеки.
- **Добре**: Використовувати деперсоналізований звуковий ДНК (див. `reference-to-style-cheatsheet.md`).

---

### 7. Відсутність негативного промптингу для акустичних артефактів
- **Помилка**: Залишати поле `Exclude` порожнім, сподіваючись, що модель сама згенерує ідеальні високі частоти й бас без гудіння.
- **Добре**: Обов'язково додавати таргетовані токени проти артефактів:
  ```text
  Exclude: metallic highs, harsh sibilance, muddy bass, boomy low-end, garbled vocals, excessive reverb
  ```

---

### 8. Шароварщина та псевдофольклорні кліше
- **Помилка**: Простий тег `ukrainian folk`, що провокує генерацію карикатурного "весільного" синтезатора та ярмаркової польки.
- **Добре**: Вказувати конкретні модальні жанри та автентичні інструменти:
  ```text
  ukrainian ethno-rock, authentic duda bagpipe hook, live distorted guitars, punchy drums, 135 bpm
  Exclude: cheesy synth brass, cheap midi instruments, 90s schlager synthesizer, carnival polka accordion
  ```

---

### 9. Неконкретний вокальний запит
- **Помилка**: `good vocals`, `nice singing`, `beautiful voice`.
- **Добре**: Вказувати точний фізіологічний та стилістичний тип вокалу:
  - `white voice female chanting, authentic slavic polyphony`
  - `melancholic baritone male vocal, deadpan delivery`
  - `intimate breathy female vocal, close-mic whisper`
  - `spoken word male recitative, rhythmic cadence`
  - `brutal guttural growl alternating soaring clean female belting`

---

### 10. Поетичний опис замість звукового інжинірингу
- **Помилка**: *"Срібний туман, що розчиняється в серці розбитих надій..."* у полі стилю.
- **Чому це ламає генерацію**: Ліричні метафори не дають моделі інформації про інструменти, бас, барабани чи просторове зведення.
- **Добре**: Метафори залишати у `Lyrics`, а у `Style of music` писати чіткі фізичні параметри звуку.

---

## 2. Матриця акустичних збоїв та точних рішень

```text
┌──────────────────────────────┬────────────────────────────────────────────┬────────────────────────────────────────────────────────┐
│ Акустичний симптом           │ Першопричина в генерації                   │ Точний Exclude-вектор для усунення                     │
├──────────────────────────────┼────────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ Металевий пісок на верхах    │ Фазова інверсія на тарілках і сибілянтах   │ metallic highs, harsh sibilance, piercing treble,      │
│ (Harsh digital treble)       │                                            │ tinny high-end, digital clipping, harsh cymbals        │
├──────────────────────────────┼────────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ Бубніння і каша на низах     │ Неконтрольований суб-бас 30–60 Гц          │ muddy bass, boomy low-end, distorted sub-bass,         │
│ (Low-end rumble)             │                                            │ muffled low frequencies, bass rumble                   │
├──────────────────────────────┼────────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ Проковтування слів і глітчі  │ Забагато складів у рядку без пауз          │ garbled vocals, mumbled words, slurred pronunciation,  │
│ (Garbled diction)            │                                            │ double-vocal glitch, robotic vocal artifacts           │
├──────────────────────────────┼────────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ Кавернозне відлуння і гул    │ Модель заливає трек 100% соборним холлом   │ excessive reverb, cavernous reverb, muddy hall decay,  │
│ (Reverb drowning)            │                                            │ wash of echo, drowning delay, swampy mix               │
├──────────────────────────────┼────────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ Дешеві міді-дудки і попса    │ Загальний тег folk викликав schlager sound │ cheesy synth brass, cheap midi instruments,            │
│ (Cheesy MIDI / Schlager)     │                                            │ 90s schlager synthesizer, carnival polka accordion     │
├──────────────────────────────┼────────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ Недоречний стадіонний вибух  │ Стандартна крива поп-року зламала баладу   │ bombastic anthem climax, festival EDM drop,            │
│ (Unwanted stadium drop)      │                                            │ heavy metal blast beats, melodramatic screaming        │
└──────────────────────────────┴────────────────────────────────────────────┴────────────────────────────────────────────────────────┘
```

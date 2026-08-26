# Ukrainian Poetry To Suno AI — Comprehensive Engineering Guide

Повний посібник із перетворення української поезії, пісенної лірики, музичних референсів та творчих концептів у високоточні запити для сучасних аудіомоделей `Suno AI` (v3.5 / v4 / сучасні гібридні дифюзійно-трансформерні рушії).

---

## 1. Архітектура та механіка сучасних моделей Suno AI

### 1.1 Три окремі вхідні вектори Suno Custom Mode

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ 1. Поле "Style of Music" (Стиль музики)                                                │
│    - Призначення: Формування жанрової матриці, темпоритму, інструментів, продакшну.    │
│    - Мова: Суворо англійські музичні терміни + автентичні українські інструменти.      │
│    - Економіка токенів: 80–180 символів (оптимально 80–150 символів, ~15–30 токенів). │
│    - Правило: Повна відсутність метаданих (Language, Theme, Mood).                     │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 2. Поле "Lyrics" (Текст пісні та аранжувальні метатеги)                                │
│    - Призначення: Співаний текст, розподіл куплетів/приспівів, динаміка та бек-вокал.  │
│    - Синтаксис: Квадратні дужки [Intro], [Verse], [Chorus] для структурних команд;    │
│                 Круглі дужки (луна), (бек-вокал) для бек-вокалу та гармоній.           │
│    - Мова: Автентична українська літературна мова або діалекти.                       │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 3. Поле "Exclude Styles" (Негативний промпт)                                           │
│    - Призначення: Віднімання небажаних звукових векторів із латентного простору.       │
│    - Наповнення: Акустичні анти-артефакти (металевий бруд, гудіння басу, глітчі)      │
│                  та стилістичні анти-кліше (шароварщина, дешевий MIDI, EDM-дроп).      │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Економіка токенів та ліво-право позиційне зважування

### 2.1 Проблема розсіювання уваги (Cross-Attention Dispersion)
При перевищенні 180–200 символів у полі стилю вага кожного окремого дескриптора падає. Модель потрапляє у стан *style averaging* (усереднення стилю), перетворюючи специфічний пост-панк чи етно-хаос на стандартний середньотемповий поп-рок.

### 2.2 Формула ліво-правого позиціонування
Suno зчитує токени зліва направо з найвищим пріоритетом перших трьох позицій:
1. **Позиція 1–2 (Фундамент)**: Головний жанр і субжанр (`ukrainian post-punk, doomer wave`).
2. **Позиція 3 (Ритм і пульс)**: Темпоритм, драм-машина або барабанний профіль (`130 bpm, driving bassline, 80s drum machine`).
3. **Позиція 4 (Вокальний тембр)**: Фізіологічний тип вокалу (`melancholic baritone male vocal`).
4. **Позиція 5 (Ключовий інструмент)**: Головний тембральний хук (`chorus-drenched electric guitar`).
5. **Позиція 6 (Продакшн і простір)**: Характер зведення (`lo-fi nocturnal production`).

---

## 3. 8-Жанрова таксономія сучасної української музики

| # | Жанровий кластер & Архетипи | Точний Style Prompt (80–180 chars) | Рекомендований Exclude Vector |
|---|-----------------------------|------------------------------------|-------------------------------|
| **1** | **Ethno-Chaos / Avant-Folk**<br>*(DakhaBrakha, Dakh Daughters)* | `ukrainian ethno-chaos, avant-folk, white voice female chanting, acoustic cello drone, heavy tribal percussion, hypnotic dark polyphony, 120 bpm` (138 chars) | `cheesy synth brass, 90s schlager, edm drop, generic pop, metallic highs` |
| **2** | **Post-Punk / Doomer Wave**<br>*(SadSvit, Mistmorn, Renie Cares)* | `ukrainian post-punk, doomer wave, 130 bpm, driving bassline, melancholic baritone male vocal, chorus electric guitar, lo-fi night production` (135 chars) | `bright acoustic strumming, polished autotune pop, cheerful brass, harsh sibilance` |
| **3** | **Dark Synth / Coldwave / EBM**<br>*(Kurs Valüt)* | `ukrainian dark synth, minimal wave, coldwave, analog bass pulse, monotone male recitative, crisp electronic drums, nocturnal, 122 bpm` (134 chars) | `acoustic guitar, joyful schlager, live orchestra, heavy metal distortion, reverb mud` |
| **4** | **Trap-Folk / Modern Drill**<br>*(Kalush, SKOFKA, alyona alyona)* | `ukrainian trap-folk, drill beat, 140 bpm, 808 sub bass, rapid hi-hats, authentic sopilka hook, rhythmic male recitative, energetic chorus` (136 chars) | `tourist folk cliches, cheesy polka accordion, slow acoustic ballad, distorted sub-bass` |
| **5** | **Progressive Metalcore / Ethno-Metal**<br>*(Jinjer, Motanka, Space of Variations)* | `ukrainian progressive metalcore, djent riffs, tsymbaly folk intro, brutal guttural scream alternating ethereal clean female vocal, heavy drop, 150 bpm` (146 chars) | `mumble vocal, pop synth brass, acoustic ukulele, dance club beat, tinny cymbals` |
| **6** | **Shoegaze / Dream Pop**<br>*(Latexfauna, Vivienne Mort)* | `ukrainian shoegaze, dream pop, wall of sound reverb guitars, whispered breathy female vocal, lush chorus, sensual slow groove, 90 bpm` (138 chars) | `harsh distortion, aggressive rap, dry close mix, stadium shouting, metallic sibilance` |
| **7** | **Authentic Modern Ethno-Rock**<br>*(Kozak System, Tin Sontsya, Haydamaky)* | `ukrainian ethno-rock, live heavy guitars, authentic duda bagpipe hook, punchy live drums, energetic male lead, anthemic driving folk, 135 bpm` (137 chars) | `cheap midi instruments, synthpop arpeggios, tourist polka, trap 808, digital clipping` |
| **8** | **Neoclassical Bandura / Ambient**<br>*(KRUTЬ, chamber acoustic)* | `contemporary ukrainian neoclassical, solo bandura arpeggios, emotive cello, warm ambient synth, intimate breathy female vocal, 75 bpm` (138 chars) | `electronic drums, distorted guitars, aggressive shouting, festival drop, boomy low-end` |

---

## 4. Автентичні тембри українського вокалу

Щоб отримати живе звучання замість роботизованого синтезу, вказуй точні вокальні дескриптори:

- **Білий голос (*White Voice*)**: `white voice female chanting, authentic slavic village polyphony, open-throat vocal, throat resonance`.
- **Пост-панк баритон**: `melancholic baritone male vocal, deadpan monotone delivery, cold low register`.
- **Мелодекламація / Речитатив**: `spoken word male recitative, deadpan rhythmic cadence, poetic speech delivery`.
- **Інтимний шепіт**: `intimate breathy female vocal, close-mic whisper, fragile emotional delivery, ASMR vocal texture`.
- **Хрипкий бардичний тембр**: `raspy male vocal, raw textured gravelly timbre, smoked vocal edge, strained emotional delivery`.
- **Потужний белтинг**: `powerful soaring female vocal, resonant chest voice belting, high-energy emotional release`.
- **Металкор гроул / скрім**: `brutal guttural growl, harsh screaming alternating ethereal clean melodic vocal`.
- **Сучасний автотюн**: `modern autotune vocal, formant-shifted vocal chops, futuristic pitch correction`.

---

## 5. Повний синтаксис метатегів аранжування

### 5.1 Секційні метатеги `[Square Brackets]`
- **Секції пісні**: `[Intro]`, `[Verse 1]`, `[Verse 2]`, `[Pre-Chorus]`, `[Chorus]`, `[Post-Chorus]`, `[Bridge]`, `[Outro]`, `[End]`.
- **Інструментальні пасажі**: `[Instrumental Interlude]`, `[Guitar Solo]`, `[Bandura Solo]`, `[Sopilka Solo]`, `[Cello Solo]`, `[Bass Drop]`, `[Beat Drop]`, `[Drum Fill]`.
- **Динаміка і темп**: `[Tempo: 125 BPM]`, `[Dynamic: Crescendo]`, `[Dynamic: Pianissimo]`, `[Beat Cut]`, `[Silence]`, `[Acapella]`, `[Stripped Back]`.
- **Вокальний розподіл**: `[Male Lead Vocal]`, `[Female Lead Vocal]`, `[Duet]`, `[White Voice Choir]`.

### 5.2 Бек-вокал та ехо `(Parentheses)`
Текст у круглих дужках розпізнається нейромережею як бек-вокальна партія, стерео-відлуння або адліб:
```text
[Verse 1]
У темнім склі тремтить моє безсонне відбиття,
(у темнім склі)
І чайник знову перший заговорив у тиші.
(тиша навколо)
```

---

## 6. Акустичний негативний промптинг (Exclude Vectors)

```text
┌──────────────────────────────┬────────────────────────────────────────────────────────┐
│ Проблема у згенерованому треку│ Ефективний набір Exclude-токенів                      │
├──────────────────────────────┼────────────────────────────────────────────────────────┤
│ Металевий пісок на верхах    │ metallic highs, harsh sibilance, piercing treble,      │
│                              │ tinny high-end, digital clipping, harsh cymbals        │
├──────────────────────────────┼────────────────────────────────────────────────────────┤
│ Бубніння і гул на суб-басі   │ muddy bass, boomy low-end, distorted sub-bass,         │
│                              │ muffled low frequencies, bass rumble                   │
├──────────────────────────────┼────────────────────────────────────────────────────────┤
│ Проковтування слів / глітчі  │ garbled vocals, mumbled words, slurred pronunciation,  │
│                              │ double-vocal glitch, robotic vocal artifacts           │
├──────────────────────────────┼────────────────────────────────────────────────────────┤
│ Кавернозне відлуння холу     │ excessive reverb, cavernous reverb, muddy hall decay,  │
│                              │ wash of echo, drowning delay, swampy mix               │
├──────────────────────────────┼────────────────────────────────────────────────────────┤
│ Шароварщина і дешевий MIDI   │ cheesy synth brass, cheap midi instruments,            │
│                              │ 90s schlager synthesizer, carnival polka accordion     │
├──────────────────────────────┼────────────────────────────────────────────────────────┤
│ Недоречний стадіонний пафос  │ bombastic anthem climax, festival EDM drop,            │
│                              │ heavy metal blast beats, melodramatic screaming        │
└──────────────────────────────┴────────────────────────────────────────────────────────┘
```

---

## 7. Робота з музичними референсами (Safe Reference Extraction)

### Алгоритм деперсоналізації:
1. Отримати назву артиста чи пісні від користувача.
2. Проаналізувати ритм, BPM, бас, гітарний тембр, вокальну манеру та атмосферу.
3. Повністю видалити імена, бренди та прямі фрази `in the style of`.
4. Скласти легальний `Safe Style Prompt` у межах 80–180 символів.

### Приклад:
- **Запит**: "Зроби трек як Latexfauna - Lime"
- **Аналіз**: Дрім-поп, лінивий фанковий бас, пошепки вокал, реверберовані гітари, літній вайб.
- **Safe Style Prompt (138 символів)**:
  ```text
  ukrainian shoegaze, dream pop, wall of sound reverb guitars, whispered breathy female vocal, lush chorus, sensual slow groove, 90 bpm
  ```
- **Exclude**: `harsh distortion, aggressive rap, dry close mix, stadium shouting, metallic sibilance`

---

## 8. Покроковий Custom Mode Workflow

```text
Вхідний вірш / ідея ──> Вибір 1 із 8 жанрів ──> Складання Style Prompt (80-180 chars)
                                              ├──> Розмітка Lyrics ([Verse], [Chorus], (ехо))
                                              └──> Підбір Exclude векторів
```

### Фінальний приклад генерації:

**Style of music (135 символів)**:
```text
ukrainian post-punk, doomer wave, 130 bpm, driving bassline, melancholic baritone male vocal, chorus electric guitar, lo-fi night production
```

**Lyrics**:
```text
[Intro]
[80s Beat]
[Guitar Riff]

[Verse 1]
[Baritone Male Vocal]
Порожній проспект ковтає ліхтарі,
Холодний дощ стікає по вікні.
Ми знову чужі у цьому дворі,
(у цьому дворі)
Де пам'ять згорає на самому дні.

[Chorus]
[Driving Bassline]
Нічний трамвай іржавим колесом,
Везе мій сум за темний горизонт.
Лишився тільки мокрий автохтон,
І вікна, що світять в унісон.

[Guitar Solo]
[Pedal Lead Solo]

[Outro]
[Cold End]
```

**Exclude**:
```text
bright acoustic strumming, polished autotune pop, cheerful brass, harsh sibilance, stadium shouting, metallic highs, muddy bass
```

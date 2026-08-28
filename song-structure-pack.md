# Suno AI & Google Flow Music Song Structure & Metatag Pack

Повний каталог структурних шаблонів і стандартного синтаксису метатегів для `Suno AI Custom Mode` (v3.5 / v4) та `Google Flow Music`.

---

## 1. Синтаксична граматика парсера Suno та Flow Music

```text
┌─────────────────────────┬──────────────────────────────────────────┬────────────────────────────────────────────────────────┐
│ Символи синтаксису      │ Як інтерпретує парсер Suno / Flow Music  │ Приклад правильного використання                       │
├─────────────────────────┼──────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ [Квадратні дужки]       │ Неспіваний метатег / звукова вказівка    │ [Intro - Staccato telecaster riff, driving bassline],  │
│                         │ (структура, соло, темп, аранжування)     │ [Verse 1 - Intimate vocal], [Guitar Solo], [Outro]     │
├─────────────────────────┼──────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ (Круглі дужки)          │ Співаний бек-вокал, ехо, гармонія, адліб │ (луна в імлі), (ніколи знов), (голос у тиші)           │
│                         │ УВАГА: Flow Music читає () вголос!       │ ЖОДНИХ інструментів у () — лише співані слова!         │
├─────────────────────────┼──────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ ВЕЛИКІ ЛІТЕРИ ГОЛОСНИХ  │ Точна фіксація наголосу для ШІ-вокалу    │ вИпадок, чорнОзем, прИйде, заспівАй, моЯ, дорОга       │
├─────────────────────────┼──────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ Дефіси у словах         │ Складовий поділ для швидких темпів       │ за-спі-вай, не-по-втор-ний (запобігає ковтанню слів)   │
├─────────────────────────┼──────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ *Зірочки*               │ Нестандартний синтаксис (ризик збоїв)    │ Уникати. Модель може вимовляти зірочки вголос          │
├─────────────────────────┼──────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ "Лапки"                 │ Непередбачувана ритміка фрази            │ Уникати в полі Lyrics; розбивай рядки переносом        │
└─────────────────────────┴──────────────────────────────────────────┴────────────────────────────────────────────────────────┘
```

---

## 2. Повний довідник стандартних метатегів

### 1. Секційні маркери
- `[Intro]` / `[Acoustic Bandura Intro]` / `[Atmospheric Synth Intro]`
- `[Verse 1]`, `[Verse 2]`, `[Verse 3]`
- `[Pre-Chorus]` / `[Rising Pre-Chorus]`
- `[Chorus]` / `[Anthemic Chorus]` / `[Soft Melodic Chorus]`
- `[Post-Chorus]` / `[Vocal Hook Post-Chorus]`
- `[Bridge]` / `[Dynamic Bridge]` / `[Quiet Spoken Bridge]`
- `[Outro]` / `[Acoustic Outro]` / `[Fade Out]` / `[Cold End]` / `[Abrupt Cut]` / `[End]`

### 2. Інструментальні інтерлюдії та соло
- `[Instrumental Break]` / `[Instrumental Interlude]`
- `[Guitar Solo]` / `[Bandura Solo]` / `[Sopilka Solo]` / `[Cello Solo]`
- `[Drum Fill]` / `[Bass Drop]` / `[Beat Drop]` / `[Riff]`

### 3. Динамічні та темпові вказівки
- `[Tempo: 120 BPM]`, `[Tempo: Half-Time]`, `[Tempo: Double-Time]`
- `[Key: D Minor]`, `[Key: A Minor]`
- `[Dynamic: Crescendo]`, `[Dynamic: Pianissimo]`, `[Dynamic: Fortissimo]`
- `[Silence]`, `[Beat Cut]`, `[Acapella]`, `[Stripped Back]`

### 4. Розподіл вокальних партій
- `[Male Lead Vocal]`, `[Female Lead Vocal]`, `[Duet]`, `[Call-Response]`
- `[White Voice Choir]`, `[Spoken Word Recitative]`, `[Whispered Vocals]`
- `[Brutal Guttural Growl]`, `[Soaring Clean Belting]`

---

## 3. Готові структурні шаблони за жанрами

### Шаблон 1: Classic Pop / Rock Structure
```text
[Intro]
[Instrumental Hook]

[Verse 1]
<Куплет 1>
(бек-вокал)

[Pre-Chorus]
<Передприспів: наростання динаміки>

[Chorus]
<Потужний відкритий приспів>

[Verse 2]
<Куплет 2>

[Pre-Chorus]
<Передприспів>

[Chorus]
<Приспів>

[Bridge]
<Емоційний контрастний міст>

[Guitar Solo]
[Melodic Solo]

[Chorus]
[Explosive Final Chorus]
(бек-вокал гармонія)

[Outro]
[Fade Out]
[End]
```

---

### Шаблон 2: Ethno-Chaos Build & Trance Drop (DakhaBrakha style)
```text
[Intro]
[Acoustic Cello Drone]
[Minimal Shaker]
(автентичний заспів)

[Verse 1]
[White Voice Choir]
<Куплет 1>

[Tribal Percussion Build-up]
[Dynamic: Crescendo]

[Chorus]
[Polyphonic Folk Harmony]
<Приспів: ритуальне багатоголосся>
(луна понад кручами)

[Instrumental Break]
[Djembe Solo]
[Accordion Riff]

[Verse 2]
[Accelerando]
<Куплет 2: швидший темп>

[Tribal Drop]
[Tribal Drums]

[Climax Chorus]
[Fortissimo]
<Фінальний шалений приспів>

[Outro]
[Cello Drone]
[Fade Out]
[End]
```

---

### Шаблон 3: Post-Punk / Doomer Wave Direct Motion (SadSvit style)
```text
[Intro]
[80s Beat]
[Guitar Riff]

[Verse 1]
[Baritone Male Vocal]
<Куплет 1: монотонна нічна лірика>
(у цьому дворі)

[Chorus]
[Driving Bassline]
<Приспів: швидкий мелодійний хук>

[Verse 2]
<Куплет 2>

[Chorus]
<Приспів>

[Guitar Solo]
[Pedal Lead Solo]

[Chorus]
[Final Driving Chorus]

[Outro]
[Bassline Solo]
[Cold End]
```

---

### Шаблон 4: Dark Synth / Coldwave EBM Loop (Kurs Valüt style)
```text
[Intro]
[Analog Bass Pulse]
[Crisp Electronic Drums]

[Verse 1]
[Monotone Male Recitative]
<Куплет 1: розмовна суха декламація>
(сигнал прийнято)

[Chorus]
[Synthwave Hook]
<Приспів: мінімалістичний електронний рефрен>

[Instrumental Drop]
[Modular Synth Loop]

[Verse 2]
[Monotone Recitative]
<Куплет 2>

[Chorus]
<Приспів>

[Outro]
[Analog Bassline Decay]
[Abrupt Cut]
```

---

### Шаблон 5: Progressive Metalcore Dynamic Dual (Jinjer style)
```text
[Intro]
[Solo Tsymbaly Dulcimer]
[Heavy Bass Drop]

[Verse 1]
[Brutal Guttural Growl]
<Куплет 1: екстремальний вокал, бластбіти>
(лють не згасне!)

[Pre-Chorus]
[Clean Female Vocal]
[Dynamic: Crescendo]
<Передприспів: чистий перехід>

[Chorus]
[Soaring Clean Belting]
<Приспів: потужний мелодійний бельтинг>

[Verse 2]
[Harsh Screaming]
<Куплет 2>

[Breakdown]
[Polyrhythmic Djent Riff]
[Heavy Drop]

[Chorus]
[Epic Final Chorus]
(поліфонічний бек-вокал)

[Outro]
[Acoustic Tsymbaly Outro]
[End]
```

---

### Шаблон 6: Trap-Folk & Drill Hook-First (Kalush style)
```text
[Hook Intro]
[Sopilka Solo]
(гей-гей, ой летіла зоря)

[Chorus]
[Melodic Folk Chorus]
<Приспів-хук на початку треку>

[Verse 1]
[Rapid Male Recitative]
[808 Bass]
[Drill Hi-Hats]
<Куплет 1: швидка речитативна читка>

[Pre-Chorus]
[Sopilka Hook]

[Chorus]
<Приспів>

[Verse 2]
[Syncopated Drill Flow]
<Куплет 2>

[Instrumental Drop]
[Sopilka Solo]

[Chorus]
[Energetic Final Chorus]

[Outro]
[Sopilka Flute Solo]
[Fade Out]
```

---

### Шаблон 7: Neoclassical Bandura Chamber Arc (KRUTЬ style)
```text
[Intro]
[Acoustic Bandura Solo]

[Verse 1]
[Intimate Female Vocal]
<Куплет 1: ніжний напівпошепки спів>
(пахне садом)

[Chorus]
[Emotive Cello Layer]
<Приспів: камерне тепле розкриття>

[Verse 2]
<Куплет 2>

[Chorus]
<Приспів>

[Bandura Solo]
[Delicate Chromatic Flourish]

[Outro]
[Bandura Cello Duet]
[Pianissimo]
[Fade Out]
[End]
```

---

### Шаблон 8: Shoegaze / Dream Pop Wall of Sound (Latexfauna style)
```text
[Ambient Intro]
[Shimmering Synth Pads]
[Reverb Guitar Swell]

[Verse 1]
[Whispered Female Vocal]
<Куплет 1: чуттєвий повільний вокал>

[Chorus]
[Reverb Swell]
<Приспів: гітарне марення>
(ah-ah-ah)

[Verse 2]
<Куплет 2>

[Chorus]
<Приспів>

[Instrumental Interlude]
[Fuzz Guitar Solo]

[Chorus]
[Ethereal Climax]

[Outro]
[Ambient Synth Wash]
[Fade Out]
```

# Lyrics To Suno Custom Mode Templates

Універсальні шаблони для перетворення українських віршів, пісенних текстів, референсів та творчих брифів у готові блоки для `Suno AI Custom Mode` (v3.5 / v4).

---

## 1. Головний шаблон Custom Mode (Copy-Paste)

```text
Style of music:
<genre, subgenre, tempo/bpm, vocal timbre, key instruments, production feel — 80-180 chars>

Lyrics:
[Intro]
<інструментальний вступ або ехо-заспів>

[Verse 1]
<Рядки першого куплету>
(бек-вокал або ехо)

[Pre-Chorus]
<Передприспів: наростання напруги>

[Chorus]
<Головний приспів>
(поліфонічна підтримка)

[Verse 2]
<Рядки другого куплету>

[Chorus]
<Приспів>

[Bridge]
<Міст: емоційний поворот>

[Guitar Solo]
[Instrumental Break]

[Chorus]
[Climax]
<Фінальний потужний приспів>

[Outro]
[Fade Out]
[End]

Exclude:
<акустичні анти-артефакти, небажані стильові елементи>
```

---

## 2. Шаблони за типами вхідних даних

### Шаблон А: З готового українського вірша
```text
Перетвори цей український вірш у Suno Custom Mode конфігурацію.

Параметри:
- Бажаний жанр: <один із 8 сучасних українських жанрів або гібрид>
- Темп / BPM: <наприклад, 125 bpm>
- Вокальний тембр: <білий голос | речитатив | баритон | белтинг | шепіт | гроул>
- Уникати: <шароварщина, пафос, металевий бруд тощо>

Текст вірша:
<встав текст>
```

---

### Шаблон Б: З теми та настрою (без готового тексту)
```text
Створи повну Suno Custom Mode конфігурацію для українського треку.

- Тема: <тема треку>
- Настрій: <емоційне ядро>
- Музичний орієнтир: <жанр / піджанр>
- Вокал: <тип вокалу>
- Анти-стиль: <чого не повинно бути>

Поверни:
1. Style of music (суворо 80–180 символів, англійські токени)
2. Lyrics (структурований український текст із тегами [Intro], [Verse], [Chorus], [Outro] та (бек-вокалом))
3. Exclude (анти-артефакти та анти-кліше)
```

---

### Шаблон В: З музичного референса (артист / трек)
```text
У мене є музичний референс, але в фінальному prompt заборонено згадувати імена артистів або назви треків.

Референс:
- Артист: <artist>
- Трек: <track>

Потрібно:
1. Reference breakdown (жанр, BPM, вокальний тембр, інструменти, продакшн)
2. Safe style prompt (80–180 символів)
3. Lyrics (розмічений текст під цю структуру)
4. Exclude (список анти-артефактів)

Мій український текст / тема:
<встав текст або тему>
```

---

## 3. Готові зразки за 4-ма сценаріями

### Зразок 1: Пост-панк / Doomer Wave (SadSvit style)
- **Style of music (135 символів)**:
  ```text
  ukrainian post-punk, doomer wave, 130 bpm, driving bassline, melancholic baritone male vocal, chorus electric guitar, lo-fi night production
  ```
- **Lyrics**:
  ```text
  [Intro]
  [80s Beat]
  [Chorus Guitar Riff]

  [Verse 1]
  Порожній проспект ковтає ліхтарі,
  Холодний дощ стікає по вікні.
  Ми знову чужі у цьому дворі,
  (у цьому дворі)
  Де пам'ять згорає на самому дні.

  [Chorus]
  [Melancholic Baritone Vocal]
  Нічний трамвай іржавим колесом,
  Везе мій сум за темний горизонт.
  Лишився тільки мокрий автохтон,
  І вікна, що світять в унісон.

  [Guitar Solo]
  [Chorus Pedal Lead]

  [Outro]
  [Cold End]
  ```
- **Exclude**: `bright acoustic strumming, polished autotune pop, cheerful brass, harsh sibilance, stadium shouting`

---

### Зразок 2: Етно-хаос / Avant-Folk (DakhaBrakha style)
- **Style of music (138 символів)**:
  ```text
  ukrainian ethno-chaos, avant-folk, white voice female chanting, acoustic cello drone, heavy tribal percussion, hypnotic dark polyphony, 120 bpm
  ```
- **Lyrics**:
  ```text
  [Intro]
  [Acoustic Cello Drone]
  (гей-я, ой на морі)

  [Verse 1]
  [White Voice Chanting]
  Ой на горі вогонь горить,
  Там зоря з зорею говорить.
  (зоря говорить)
  Стиха вода камінь точить,
  Ніч глибока правду свідчить.

  [Chorus]
  [White Voice Harmony]
  Ой лети, вітре, понад кручами,
  Розжени тугу із криницями!
  (розжени тугу!)

  [Instrumental Break]
  [Tribal Percussion Drop]

  [Outro]
  [Fade Out]
  [End]
  ```
- **Exclude**: `cheesy synth brass, 90s schlager, edm drop, generic pop, metallic highs, muddy bass`

---

### Зразок 3: Неокласична бандура (KRUTЬ style)
- **Style of music (138 символів)**:
  ```text
  contemporary ukrainian neoclassical, solo bandura arpeggios, emotive cello, warm ambient synth, intimate breathy female vocal, 75 bpm
  ```
- **Lyrics**:
  ```text
  [Intro]
  [Acoustic Bandura Solo]

  [Verse 1]
  [Intimate Female Vocal]
  Тихий вечір сідає на плечі,
  Старе яблуко пахне садом.
  (пахне садом)
  Срібні струни моєї предтечі
  Озиваються ніжним ладом.

  [Chorus]
  [Warm Cello Layer]
  Пам'ятай мене сонцем крізь вікна,
  Пам'ятай мене стежкою в житі.
  Поки пісня у серці не стихне,
  Доти будемо в світі зігріті.

  [Bandura Solo]
  [Delicate Chromatic Flourish]

  [Outro]
  [Pianissimo]
  [Fade Out]
  [End]
  ```
- **Exclude**: `electronic drums, distorted guitars, aggressive shouting, festival drop, boomy low-end, harsh sibilance`

---

### Зразок 4: Треп-фолк / Дрилл (Kalush style)
- **Style of music (136 символів)**:
  ```text
  ukrainian trap-folk, drill beat, 140 bpm, 808 sub bass, rapid hi-hats, authentic sopilka hook, rhythmic male recitative, energetic chorus
  ```
- **Lyrics**:
  ```text
  [Hook Intro]
  [Sopilka Solo]
  (гей-гей, ой летіла зоря)

  [Chorus]
  [Melodic Folk Hook]
  Ой летіла зоря понад темним гаєм,
  Де ми рідний край у піснях плекаєм!

  [Verse 1]
  [Rapid Male Recitative]
  [808 Bass]
  Вулиця дихає в такт моїх кроків,
  Скільки пройшли ми незвіданих років.
  (незвіданих років)
  Правда не спить у бетонних кварталах,
  Слово горить у відкритих фіналах!

  [Instrumental Drop]
  [Sopilka Solo]

  [Chorus]
  [Energetic Final Chorus]

  [Outro]
  [Sopilka Flute Solo]
  [Fade Out]
  ```
- **Exclude**: `tourist folk cliches, cheesy polka accordion, slow acoustic ballad, distorted sub-bass, tinny treble`

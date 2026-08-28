# Modular Suno Prompt Builder

Швидкий конструктор високоточних `Suno` prompt'ів (v3.5 / v4 / сучасні моделі).

---

## 1. Архітектурні принципи та економіка токенів

1. **Ліво-право пріоритет (Positional Priority)**: Перші 3 дескриптори формують західний акустичний фундамент, темпоритм та загальну структуру спектру. Усі наступні токени уточнюють тембр вокалу, інструменти та продакшн.
2. **Орієнтація на західні жанри**: Щоб уникнути шароварщини та дешевої локальної попси, музична основа завжди обирається із західних жанрів (Post-Punk, Darkwave, Synthwave, Trip-Hop, Alt-Pop, Shoegaze, Metalcore, Melodic Techno, Cinematic Ambient).
3. **Бюджет символів**: Суворо **80–180 символів** (оптимально **80–150 символів**, ~15–30 токенів). Перевищення 200 символів призводить до розсіювання уваги моделі (*cross-attention dispersion*) та усереднення треку до шаблонного поп-звучання.
4. **Чистота полів (Zero Metadata Leakage)**: У полі `Style of music` суворо заборонено писати метадані (`Language: Ukrainian`, `Theme: ...`, `Mood: ...`, `BPM: 120`). Мова задається текстом у полі `Lyrics`, темп — токеном `120 bpm`.
5. **Англомовні токени стилю**: Поле стилю заповнюється англійськими музичними термінами.

---

## 2. Базова 6-блокова формула стилю

```text
[Western Genre / Subgenre] + [Tempo / Groove] + [Vocal Timbre] + [Key Instruments] + [Production / Space] + [Dynamic Arc]
```

### Приклад збірки (136 символів):
```text
british post-punk, darkwave, 130 bpm, driving bassline, melancholic baritone male vocal, chorus electric guitar, lo-fi night production
```

---

## 3. Модульні будівельні блоки

### Block 1: Western Genre & Subgenre (Позиція 1–2)
*Обери 1 домінуючий західний жанр або 2 гармонійні суміжні жанри:*

- `british post-punk, darkwave, coldwave`
- `dark synthwave, cyberpunk ebm, minimal wave`
- `bristol trip-hop, downtempo, lo-fi hip-hop`
- `minimalist alt-pop, dark electro-pop`
- `modern progressive metalcore, djent riffs`
- `shoegaze, dream pop, indie rock`
- `melodic techno, ambient electronica, modular`
- `contemporary cinematic ambient, neoclassical`
- `indie folk, singer-songwriter, chamber acoustic`
- `post-rock, atmospheric ambient rock`

---

### Block 2: Tempo, Rhythm & Energy (Позиція 3)
*Задай точний пульс або відчуття руху:*

- `75 bpm, slow-burning pulse`
- `95 bpm, hypnotic groove`
- `110 bpm, steady midtempo`
- `125 bpm, driving rhythm`
- `140 bpm, fast energetic tempo`
- `160 bpm, rapid double-time`
- `808 sub bass glides, syncopated hi-hats`
- `punchy live drum kit, driving groove`
- `muted electronic drum machine`
- `tribal frame drum percussion`

---

### Block 3: Authentic Vocal Timbre Directives (Позиція 4)
*Обери конкретний тип та характер вокалу:*

- `white voice female chanting, authentic slavic polyphony` (*білий голос*)
- `melancholic baritone male vocal, deadpan delivery` (*пост-панк баритон*)
- `spoken word male recitative, rhythmic cadence` (*мелодекламація*)
- `intimate breathy female vocal, close-mic whisper` (*інтимний напівпошепки*)
- `raspy male vocal, raw textured gravelly timbre` (*хрипкий бардичний*)
- `powerful soaring female vocal, resonant chest belting` (*потужний белтинг*)
- `brutal guttural growl alternating ethereal clean female vocal` (*металкор дуальність*)
- `modern autotune vocal, formant-shifted vocal chops` (*сучасний автотюн / треп*)
- `village polyphonic choir, call and response` (*хоровий автентичний фолк*)

---

### Block 4: Key Instruments & Cultural Anchors (Позиція 5)
*Обери 2–3 ключові інструментальні маркери:*

- **Автентичні українські інструменти**: `solo acoustic bandura arpeggios`, `authentic sopilka flute hook`, `telenka overtone melody`, `acoustic tsymbaly dulcimer`, `duda bagpipe riff`, `trembita horn drone`, `drymba jaw harp`.
- **Електроніка та бас**: `analog synth pads`, `cold modular bass pulse`, `deep 808 sub bass`, `glassy synth arpeggios`, `warm analog bassline`.
- **Гітари та акустика**: `chorus-drenched electric guitar`, `wall of sound fuzz guitars`, `low-tuned djent guitar riffs`, `fingerstyle acoustic guitar`, `emotive cello drone`, `warm string quartet`.

---

### Block 5: Production & Space (Позиція 6)
*Вкажи просторовий характер та зведення:*

- `clean modern production, wide stereo image`
- `lo-fi nocturnal production, raw tape saturation`
- `sleek cold production, clinical dystopian space`
- `lush reverb-rich production, ethereal ambient wash`
- `crisp radio-ready mix, punchy dynamic master`
- `organic room acoustic, intimate dry close-mic`

---

### Block 6: Dynamic Arc & Arrangement Hint (Опціонально)
*Короткий натяк на динаміку (якщо дозволяє ліміт символів):*

- `restrained chorus lift`
- `explosive dynamic drop`
- `gradual crescendo to climax`
- `minimal sparse verses, wide melodic chorus`
- `hypnotic static loop`

---

## 4. Acoustic Anti-Artifact Exclude Vectors

У полі `Exclude` (Negative Prompt) обов'язково комбінуй **акустичні анти-артефакти** та **жанрові обмеження**:

```text
┌──────────────────────────────┬────────────────────────────────────────────────────────┐
│ Категорія небажаного звуку   │ Точні токени для поля Exclude                          │
├──────────────────────────────┼────────────────────────────────────────────────────────┤
│ Металевий пісок і сибілянти  │ metallic highs, harsh sibilance, piercing treble,      │
│ (Treble artifacts)           │ tinny high-end, digital clipping, harsh cymbals        │
├──────────────────────────────┼────────────────────────────────────────────────────────┤
│ Гудіння і брудний суб-бас    │ muddy bass, boomy low-end, distorted sub-bass,         │
│ (Low-end mud)                │ muffled low frequencies, bass rumble                   │
├──────────────────────────────┼────────────────────────────────────────────────────────┤
│ Нерозбірливий вокал і глітчі │ garbled vocals, mumbled words, slurred pronunciation,  │
│ (Vocal hallucinations)       │ double-vocal glitch, robotic vocal artifacts           │
├──────────────────────────────┼────────────────────────────────────────────────────────┤
│ Тонучий ревербераційний гул  │ excessive reverb, cavernous reverb, muddy hall decay,  │
│ (Reverb wash)                │ drowning echo wash, swampy mix                         │
├──────────────────────────────┼────────────────────────────────────────────────────────┤
│ Локальна попса та шароварщина │ cheesy regional pop, post-soviet schlager, wedding    │
│ (Anti-Kitsch Suppression)    │ synth brass, cheap accordion, generic euro-pop,       │
│                              │ amateur midi production, tourist folk cliches, polka   │
├──────────────────────────────┼────────────────────────────────────────────────────────┤
│ Недоречний фестивальний крик │ bombastic anthem climax, festival EDM drop,            │
│ (Unwanted stadium bombast)   │ generic stadium trance, melodramatic belting           │
└──────────────────────────────┴────────────────────────────────────────────────────────┘
```

---

## 5. Готові зразки західних жанрів для українських пісень

### 1. British Post-Punk / Darkwave (136 символів)
- **Style of music**:
  ```text
  british post-punk, darkwave, 130 bpm, driving bassline, melancholic baritone male vocal, chorus electric guitar, lo-fi night production
  ```
- **Exclude**: `cheesy regional pop, post-soviet schlager, cheerful accordion, bright pop autotune`

### 2. Dark Synthwave / Cyberpunk EBM (137 символів)
- **Style of music**:
  ```text
  dark synthwave, analog moog bass pulse, gated 80s snare, crisp electronic arpeggios, monotone male vocal, cyberpunk nocturnal, 120 bpm
  ```
- **Exclude**: `cheesy regional pop, wedding synth brass, cheap accordion, acoustic strumming`

### 3. Bristol Trip-Hop / Downtempo (139 символів)
- **Style of music**:
  ```text
  trip-hop, downtempo, dusty vinyl breakbeat, warm rhodes piano, deep 808 sub bass, breathy female vocal, cinematic tape warmth, 85 bpm
  ```
- **Exclude**: `cheesy euro-pop, fast edm drop, wedding synth brass, aggressive shouting`

### 4. Minimalist Dark Alt-Pop (137 символів)
- **Style of music**:
  ```text
  minimalist alt-pop, heavy 808 sub bass, crisp close-mic breathy female vocal, organic foley percussions, dark spatial production, 100 bpm
  ```
- **Exclude**: `tourist folk cliches, cheesy polka accordion, 90s eurodance, brass fanfare, metallic sibilance`

### 5. Progressive Metalcore / Modern Djent (142 символи)
- **Style of music**:
  ```text
  modern progressive metalcore, drop-tuned djent guitar riffs, punchy aggressive drums, brutal screaming alternating ethereal clean vocal, 150 bpm
  ```
- **Exclude**: `cheap midi brass, mumble vocal, acoustic ukulele, dance club beat, tinny cymbals`

### 6. Shoegaze / Dream Pop (139 символів)
- **Style of music**:
  ```text
  shoegaze, dream pop, wall of sound reverb guitars, jangly indie groove, whispered breathy vocal, lush vintage chorus, atmospheric slow groove
  ```
- **Exclude**: `harsh digital clipping, aggressive rap, dry close mix, stadium shouting, cheesy pop brass`

### 7. Melodic Techno / Ambient Electronica (138 символів)
- **Style of music**:
  ```text
  melodic techno, electronica, hypnotic analog arpeggios, atmospheric vocal chops, deep rolling sub bass, four-on-the-floor groove, 124 bpm
  ```
- **Exclude**: `cheap midi brass, wedding accordion, tourist folk, acoustic strumming, generic pop drop`

### 8. Contemporary Cinematic Ambient (137 символів)
- **Style of music**:
  ```text
  contemporary cinematic ambient, felt upright piano, emotive soaring cello, warm tape saturation, intimate whispered vocal, 70 bpm
  ```
- **Exclude**: `electronic dance drums, distorted guitars, aggressive shouting, festival drop, cheesy regional pop`

---

## 6. Контрольний алгоритм перевірки якості

Перед надсиланням у генератор переконайся:
1. `Style of music` містить від **80 до 180 символів**.
2. Відсутні слова `Language:`, `Theme:`, `Mood:`, `Prompt:`.
3. Перші 3 слова чітко визначають жанровий фундамент і темпоритм.
4. Вокал описаний конкретним тембральним маркером (білий голос, речитатив, баритон тощо).
5. Поле `Exclude` містить як мінімум 2 акустичні анти-артефакти та 2 жанрові анти-штампи.

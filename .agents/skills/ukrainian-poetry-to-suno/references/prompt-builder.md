# Multi-Platform AI Music Prompt Builder (Suno v4.5/v5.5, Udio v4, Flow Music Lyria 3.5)

Швидкий конструктор високоточних запитів для сучасних аудіомоделей **Suno AI (v4.5 / v5.5)**, **Udio AI (v4)** та **Google Flow Music (Lyria 3.5)**.

---

## 1. Архітектурні принципи та економіка токенів

1. **Ліво-право пріоритет (Positional Priority & «First 5 Words» Rule)**: Перші 4–5 слів забирають 80% уваги нейромережі. Домінантний західний жанр, темпоритм та вокальний тембр завжди розміщуються на початку.
2. **Орієнтація на західні жанри**: Базовий стиль формується із західних жанрів (Post-Punk, Darkwave, Synthwave, Trip-Hop, Alt-Pop, Shoegaze, Metalcore, Melodic Techno, Cinematic Ambient) для уникнення провінційної попси та шароварщини.
3. **Бюджет символів**:
   - **Suno v4.5/v5.5**: Суворо **80–180 символів** (оптимально 80–150 символів або 8–15 точкових тегів; максимальний технічний ліміт поля — 1000 символів).
   - **Udio v4**: До **250 символів** (оптимально 100–200 символів).
   - **Flow Music (Lyria 3.5)**: Розмовний абзац на 150–300 слів для AI-агента.
4. **Чистота полів (Zero Metadata Leakage)**: У полі `Style of music` суворо заборонено писати службові мітки (`Language: Ukrainian`, `Theme: ...`, `Mood: ...`, `BPM: 120`). Мова задається текстом у `Lyrics`, темп — токеном `120 bpm`.
5. **Англомовні токени стилю**: Поле стилю заповнюється англійськими музичними термінами.

---

## 2. Формули створення промптів за платформами

### 2.1 Suno AI (v4.5 / v5.5)

#### Метод 1: «Conversational Paragraph» (Правило «First 5 Words»)
Цілісний опис стилю англійським абзацом, де перші 4–5 слів визначають жанр та вокал:
```text
[Genre & Subgenre] + [Vocal Triple-Stack] + [Key Instruments] + [Mood/Energy] + [Aesthetic & BPM]
```
*Приклад (138 символів)*:
```text
Alternative rock, passionate dry male tenor vocals, gritty garage guitars, warm analog bass, tape saturation, dark melancholic mood, 115 BPM.
```

#### Метод 2: «Tag-Based Matrix» (Формула HookGenius — 5 Модулів)
Складання стилю із 8–15 точних дескрипторів через кому:
```text
[1. Genre/Subgenre], [2. Mood/Energy], [3. Vocal Triple-Stack], [4. Lead Instruments], [5. Production Aesthetic, BPM]
```
*Приклад (168 символів)*:
```text
indie rock, melancholic, raspy male vocals, intimate close-up delivery, dry mic, clean electric guitar, driving melodic bass, live drum kit, lo-fi tape hiss, 115 BPM
```

---

### 2.2 Udio AI (v4)
```text
[Main Genre], [Sub-Genre], [Year/Era], [Vocal Timbre & Character], [Analog Production Style], [Acoustic Space, BPM]
```
- **Context Length**: Регулювання від 10–15 секунд (для переходів, зміни мови/стилю) до максимуму (для збереження тембру).
- **Inpainting вокалу**: Виділення фрагмента на волноводі й взяття слів для заміни в зірочки: `*static sky*`.
*Приклад (172 символи)*:
```text
British Post-Punk, Darkwave, 1980s analog recording, melancholic baritone male vocal, chorus electric guitar, tight drum machine, driving bassline, lo-fi tape saturation, 128 BPM
```

---

### 2.3 Google Flow Music (Lyria 3.5 — Conversational Agent)
```text
[Опис концепту і стилю] + [Референс атмосфери/виконавця] + [Специфікація інструментів] + [Керування динамікою і вокалом]
```
*Приклад*:
```text
Create a contemporary dark synthwave track with deep analog Moog bass pulse and tight gated 80s drums, inspired by the cinematic nocturnal mood of modern cyberpunk. The vocal is an intimate monotone male recitative with dry close-up delivery. The song begins with an acapella vocal hook, drops into a driving synth groove, and explodes into an anthemic chorus with layered harmonies.
```

---

## 3. Модульні будівельні блоки

### Модуль 1: Western Genre & Subgenre (Позиція 1–2)
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

### Модуль 2: Tempo, Rhythm & Energy (Позиція 3)
- `75 bpm, slow-burning vinyl pulse`
- `85 bpm, dusty trip-hop breakbeat`
- `100 bpm, syncopated minimalist groove`
- `115 bpm, steady driving indie tempo`
- `120 bpm, motorik four-on-the-floor pulse`
- `128 bpm, high-energy post-punk drive`
- `140 bpm, aggressive drill beat, rapid hi-hats`
- `150 bpm, double-bass metalcore drive`
- `808 sub bass glides, tight acoustic snare`
- `punchy live drum kit, compressed room tone`

---

### Модуль 3: Vocal Triple-Stack (Позиція 4)
Завжди поєднуй **Характер** + **Подачу** + **Ефект/Простір**:
- `raw passionate male tenor, intimate conversational delivery, dry close-mic`
- `fragile breathy female vocal, close-mic whisper, ASMR vocal texture`
- `melancholic baritone male vocal, deadpan monotone delivery, cold plate reverb`
- `authentic slavic white voice, open-throat resonance, natural room acoustics`
- `raspy male vocal, textured gravelly delivery, tape saturation`
- `soaring female lead vocal, chest voice belting, wide stereo harmonies`
- `brutal guttural scream alternating ethereal clean melodic vocal`
- `modern autotune vocal, formant-shifted melodic chops`
- `spoken word male recitative, rhythmic poetic cadence`

---

### Модуль 4: Key Instruments & Cultural Anchors (Позиція 5)
- **Автентичні українські інструменти**: `solo acoustic bandura arpeggios`, `authentic sopilka flute hook`, `telenka overtone melody`, `acoustic tsymbaly dulcimer`, `duda bagpipe riff`, `trembita horn drone`, `drymba jaw harp`.
- **Синтезатори та бас**: `analog moog bass pulse`, `cold modular bassline`, `deep 808 sub bass`, `glassy synth arpeggios`, `warm rhodes piano chords`.
- **Гітари та акустика**: `chorus-drenched electric guitar`, `wall of sound fuzz guitars`, `low-tuned djent guitar riffs`, `fingerpicked acoustic guitar`, `emotive cello drone`, `warm string quartet`.

---

### Модуль 5: Production Aesthetic & Space (Позиція 6)
- `clean modern production, wide stereo image, upfront dry vocals`
- `lo-fi nocturnal production, raw tape saturation, warm analog console`
- `sleek cold production, clinical dystopian space, tight punchy drums`
- `lush reverb-rich production, ethereal ambient wash, wide spatial mix`
- `crisp radio-ready mix, punchy dynamic master, transparent transients`
- `organic room acoustic, intimate dry close-mic texture`

---

## 4. Усунення критичних помилок (Failure Modes)

1. **Lyrics Rushing (вокальна скоромовка)**:
   - *Причина*: Занадто довгі рядки або перенасичений текст при швидкому темпі.
   - *Виправлення*: Розбивати текст на рядки по 4–8 слів, знизити BPM на 10–15 пунктів, додати інлайн-команду `(half-time feel)`.
2. **Robotic / Sterile Vocals (бездушний вокал)**:
   - *Причина*: Однослівний опис вокалу ("male vocal").
   - *Виправлення*: Застосувати повний Vocal Triple-Stack: `raw passionate male tenor, intimate dry conversational delivery, subtle tape warmth`.
3. **The Negation Trap (пастка заперечень)**:
   - *Причина*: Використання "no drums", "without guitar" у полі стилю (моделі ігнорують частку "no" і додають барабани).
   - *Виправлення*: Використовувати позитивну гіперспецифічність: `purely acoustic, solo piano, isolated vocals, sparse arrangement, unaccompanied`.
4. **Instrumental Parentheses Hallucination (співання інструментів)**:
   - *Причина*: Написання `(guitar solo)` у круглих дужках у полі лірики.
   - *Виправлення*: Перенести в квадратні дужки `[Guitar Solo]`. Круглі дужки `(...)` залишити виключно для бек-вокалу `(луна)` та вокальних жестів `(whispered)`, `(belted)`.

---

## 5. Acoustic Anti-Artifact Exclude Vectors

У полі `Exclude` (Negative Prompt) обов'язково комбінуй **акустичні анти-артефакти** та **жанрові анти-кліше**:

```text
cheesy regional pop, post-soviet schlager, wedding synth brass, cheap accordion, generic euro-pop, amateur midi production, tourist folk cliches, polka, metallic highs, harsh sibilance, piercing treble, tinny high-end, digital clipping, muddy bass, boomy low-end, distorted sub-bass, garbled vocals, mumbled words, double-vocal glitch, robotic vocal artifacts, excessive reverb, cavernous reverb, drowning echo wash, bombastic anthem climax, festival EDM drop
```

---

## 6. Чек-лист верифікації перед генерацією

- [ ] `Style of music` містить від **80 до 180 символів** (оптимально 80–150).
- [ ] Відсутні службові мітки `Language:`, `Theme:`, `Mood:`, `BPM:`.
- [ ] Перші 4–5 слів чітко визначають домінантний західний жанр, темп та вокал.
- [ ] Вокал задано за формулою **Vocal Triple-Stack** (Характер + Подача + Ефект).
- [ ] Поле `Exclude` містить як мінімум 2 акустичні анти-артефакти та 2 жанрові анти-штампи.
- [ ] Текст пісні розмічено за **правилом дужок `[...]` vs `(...)`** та містить **великі літери на наголосах** (`вИпадок`, `дорОга`).

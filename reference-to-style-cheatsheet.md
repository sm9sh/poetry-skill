# Western & Ukrainian Reference-to-Style Cheatsheet (v8)

Шпаргалка для безпечного перетворення референсів у легальні `safe style prompts` для **Suno AI (v4.5 / v5.5)**, **Udio AI (v4)** та **Google Flow Music (Lyria 3.5)** з **пріоритетом західних музичних жанрів, вокального Triple-Stack та стандартів продакшну**, що гарантує фірмове західне звучання треку без шароварщини та дешевої локальної попси.

---

## 1. Головне правило: Орієнтація на західні жанри та саунд-дизайн

1. **Західний звуковий еталон**: Музична складова завжди спирається на західні жанрові конвенції (UK/US/Nordic/European Post-Punk, Darkwave, Synthwave, Trip-Hop, Alt-Pop, Shoegaze, Progressive Metalcore, Melodic Techno, Cinematic Ambient).
2. **Український вокал без шароварщини**: Текст і вокальні партії подаються чистою, глибокою українською мовою, але в аранжуванні використовується фірмовий західний продакшн (не провінційне диско, не весільний синтезатор і не шароварний псевдофольк).
3. **Сувора деперсоналізація**: Жодних імен артистів, гуртів, альбомів чи назв треків у фінальному prompt'і.
4. **Бюджет символів**: 80–180 символів для Suno (оптимально 80–150 символів); до 250 символів для Udio.
5. **Обов'язковий Exclude проти локальної попси**: У полі `Exclude` завжди пригнічуються маркери локальної естради: `cheesy regional pop, post-soviet schlager, wedding synth brass, cheap accordion, generic euro-pop, tourist folk cliches`.

---

## 2. Мапа західних еталонів та безпечних стилів (Western Benchmarks)

### 1. Depeche Mode / Boy Harsher / Carpenter Brut Archetype (Dark Synthwave / EBM)
- **Звуковий ДНК**: Аналоговий бас Moog, гейтований 80s малий барабан, арпеджіатори, нічний кіберпанк-драйв.
- **Vocal Triple-Stack**: `monotone male recitative, deadpan spoken cadence, coldwave vocal, dry close-mic`.
- **Melodic Math**: Старт із субдомінанти у вступі, сполучний хук у приспіві, контраст Staccato куплету та широкого Legato приспіву.
- **Suno Safe Style (Method 1 - 138 симв.)**:
  ```text
  Dark synthwave, monotone male vocal, analog moog bass pulse, gated 80s snare, crisp electronic arpeggios, cyberpunk nocturnal mood, 120 BPM.
  ```
- **Suno Safe Style (Method 2 - 167 симв.)**:
  ```text
  dark synthwave, cyberpunk ebm, nocturnal, monotone male vocal, dry close-mic, analog moog bass pulse, gated 80s snare, electronic arpeggios, sleek cold mix, 120 bpm
  ```
- **Udio v4 Safe Prompt**:
  `Dark Synthwave, EBM, 1980s electronic, monotone male vocal, analog moog bassline, gated snare, crisp arpeggios, clinical dystopian production, 120 BPM`
- **Exclude**: `cheesy regional pop, wedding synth brass, cheap accordion, acoustic strumming, metallic highs`

---

### 2. Joy Division / The Cure / Molchat Doma Archetype (Post-Punk / Darkwave)
- **Звуковий ДНК**: Хорус на гітарі, пульсуючий високий бас, сухий вінтажний драм-машинний біт, меланхолійний баритон.
- **Vocal Triple-Stack**: `melancholic baritone male vocal, deadpan monotone delivery, cold plate reverb`.
- **Melodic Math**: Акапельний вступ `[Vocal Intro]`, мелодичний анонс на 4-му рядку куплету, приспів до 45-ї секунди.
- **Suno Safe Style (Method 1 - 143 симв.)**:
  ```text
  British post-punk, melancholic baritone male vocal, driving bassline, chorus electric guitar, 80s drum machine, lo-fi nocturnal mood, 128 BPM.
  ```
- **Suno Safe Style (Method 2 - 158 симв.)**:
  ```text
  british post-punk, darkwave, melancholic, baritone male vocal, deadpan delivery, dry mic, chorus electric guitar, driving bassline, 80s drum machine, 128 bpm
  ```
- **Udio v4 Safe Prompt**:
  `British Post-Punk, Darkwave, 1980s analog recording, melancholic baritone male vocal, chorus electric guitar, tight drum machine, driving bassline, lo-fi tape saturation, 128 BPM`
- **Exclude**: `cheesy regional pop, post-soviet schlager, cheerful accordion, bright pop autotune`

---

### 3. Massive Attack / Portishead / Morcheeba Archetype (Trip-Hop / Bristol Sound)
- **Звуковий ДНК**: Вініловий даунтемпо-брейкбіт, теплий Rhodes, глибокий саб-бас 808, димчастий жіночий напівшепіт, плівкове насичення.
- **Vocal Triple-Stack**: `breathy smoky female vocal, intimate whispered delivery, subtle tape warmth`.
- **Melodic Math**: 5-секундний вокальний шепіт `(whispered)`, мінімалістичний 808 біт-дроп `[Beat Drop]`, 3 когнітивні мелодії.
- **Suno Safe Style (Method 1 - 145 симв.)**:
  ```text
  Bristol trip-hop, breathy smoky female vocal, dusty vinyl breakbeat, warm rhodes piano, deep 808 sub bass, dark melancholic tape warmth, 85 BPM.
  ```
- **Suno Safe Style (Method 2 - 170 симв.)**:
  ```text
  trip-hop, downtempo, melancholic, breathy smoky female vocal, intimate delivery, dry mic, dusty vinyl breakbeat, warm rhodes piano, deep 808 sub bass, tape hiss, 85 bpm
  ```
- **Udio v4 Safe Prompt**:
  `Bristol Trip-Hop, Downtempo, 1990s vinyl production, smoky female vocal, warm rhodes chords, deep 808 sub bass, dusty acoustic breakbeat, tape saturation, 85 BPM`
- **Exclude**: `cheesy euro-pop, fast edm drop, wedding synth brass, aggressive shouting`

---

### 4. Billie Eilish / Lorde / Banks Archetype (Minimalist Dark Alt-Pop)
- **Звуковий ДНК**: Мінімалістичний 808 саб, інтимний ASMR-вокал (близький мікрофон), органічний перкусійний фолі-шум, просторовий мікс.
- **Vocal Triple-Stack**: `close-mic breathy female vocal, ASMR vocal texture, fragile whisper, dry upfront mix`.
- **Melodic Math**: Інлайн-жести `(whispered)` у куплетах, вибуховий `(belted)` приспів із розширенням `[Chorus - explosive open wide space]`.
- **Suno Safe Style (Method 1 - 131 симв.)**:
  ```text
  Minimalist alt-pop, intimate breathy female vocal, heavy 808 sub bass, organic foley percussions, dark spatial production, 100 BPM.
  ```
- **Suno Safe Style (Method 2 - 160 симв.)**:
  ```text
  minimalist alt-pop, dark pop, intimate, breathy female vocal, ASMR close-mic, dry delivery, heavy 808 sub bass, organic foley percussions, spatial mix, 100 bpm
  ```
- **Udio v4 Safe Prompt**:
  `Minimalist Alt-Pop, Dark Pop, modern intimate production, ASMR breathy female vocal, heavy 808 sub bass, organic percussions, upfront dry mix, 100 BPM`
- **Exclude**: `tourist folk cliches, cheesy polka accordion, 90s eurodance, brass fanfare, metallic sibilance`

---

### 5. Bring Me The Horizon / Spiritbox / Architects Archetype (Modern Metalcore / Djent)
- **Звуковий ДНК**: Дроп-тюнінг, низькі джент-рифи, щільні панчеві барабани, контраст брутального гроулу та епічного чистого приспіву.
- **Vocal Triple-Stack**: `brutal guttural scream alternating soaring ethereal clean melodic vocal`.
- **Melodic Math**: Вибуховий `[Mega-Chorus]` після 15-секундного `[Breakdown]`, модульований фінал `(key change)`.
- **Suno Safe Style (Method 1 - 143 симв.)**:
  ```text
  Progressive metalcore, brutal screaming alternating soaring clean vocal, drop-tuned djent riffs, punchy drums, aggressive dark mood, 150 BPM.
  ```
- **Suno Safe Style (Method 2 - 168 симв.)**:
  ```text
  progressive metalcore, djent, aggressive, brutal screaming, clean melodic chorus, drop-tuned guitars, heavy double-bass drums, massive sub drop, wall of sound, 150 bpm
  ```
- **Udio v4 Safe Prompt**:
  `Progressive Metalcore, Modern Djent, heavy drop tuning, dual vocals with brutal scream and soaring clean melodic chorus, aggressive punchy drums, 150 BPM`
- **Exclude**: `cheap midi brass, mumble vocal, acoustic ukulele, dance club beat, tinny cymbals`

---

### 6. Slowdive / Beach House / Arctic Monkeys Archetype (Shoegaze / Dream Pop / Indie)
- **Звуковий ДНК**: Стіна реверберованих гітар, вінтажний хорус, теплий аналоговий грув, повітряний вокал у просторі.
- **Vocal Triple-Stack**: `whispered breathy vocal, delicate airy high register, lush vintage chorus`.
- **Melodic Math**: Повільне наростання напруги `(building intensity)` у пре-приспіві, гітарний сольний хук `[Instrumental Break]`.
- **Suno Safe Style (Method 1 - 143 симв.)**:
  ```text
  Shoegaze dream pop, whispered breathy vocal, wall of sound reverb guitars, jangly indie groove, lush vintage chorus, atmospheric mood, 90 BPM.
  ```
- **Suno Safe Style (Method 2 - 158 симв.)**:
  ```text
  shoegaze, dream pop, ethereal, whispered breathy vocal, delicate delivery, lush chorus, wall of sound reverb guitars, warm bassline, vintage tape mix, 90 bpm
  ```
- **Udio v4 Safe Prompt**:
  `Shoegaze, Dream Pop, 1990s vintage reverb guitars, whispered breathy vocal, shimmering synth pads, warm analog bass, ethereal spatial production, 90 BPM`
- **Exclude**: `harsh digital clipping, aggressive rap, dry close mix, stadium shouting, cheesy pop brass`

---

## 3. Мапа перекладу українських артистів у західний саунд-дизайн

| Український виконавець | Західний звуковий еталон | Ключовий Vocal Triple-Stack | Safe Style Prompt (Suno / Udio / Flow) |
|---|---|---|---|
| **SadSvit / Mistmorn** | UK Post-Punk / Coldwave (*Joy Division, The Cure*) | `melancholic baritone male vocal, deadpan delivery, tape slap delay` | `british post-punk, darkwave, driving bassline, chorus electric guitar, 80s drum machine, baritone male vocal, lo-fi nocturnal, 128 bpm` |
| **Latexfauna** | Indie Dream-Pop / Yacht Rock (*Men I Trust, Mac DeMarco*) | `sensual breathy male vocal, close-mic whisper, subtle chorus` | `indie dream pop, lush analog synth pads, funky muted bass, sensual breathy male vocal, jangly chorus guitar, slow groove, 92 bpm` |
| **Kurs Valüt** | Dark Synthwave / Minimal EBM (*Boy Harsher, DAF*) | `monotone male recitative, deadpan cadence, dry upfront` | `dark synthwave, minimal wave, coldwave, analog moog bass pulse, monotone male recitative, crisp electronic drums, nocturnal, 122 bpm` |
| **DakhaBrakha / Dakh Daughters** | Avant-Folk / Dark Polyphony (*Dead Can Dance, Heilung*) | `authentic slavic white voice, open-throat polyphony, throat resonance` | `ukrainian ethno-chaos, avant-folk, white voice female chanting, acoustic cello drone, heavy tribal percussion, dark polyphony, 120 bpm` |
| **Kalush / SKOFKA** | Trap-Folk / UK Drill (*Central Cee, Stormzy*) | `rapid rhythmic male recitative, syncopated cadence, modern autotune` | `ukrainian trap-folk, drill beat, 808 sub bass, rapid hi-hats, authentic sopilka hook, rhythmic male recitative, energetic chorus, 140 bpm` |
| **Vivienne Mort** | Chamber Dark Pop / Baroque Pop (*Tori Amos, Agnes Obel*) | `emotive soaring soprano, intimate fragile whisper, room plate` | `chamber dark pop, intimate acoustic piano, soaring expressive female soprano, emotive cello, subtle tape saturation, dramatic arc, 80 bpm` |
| **Jinjer / Motanka** | Progressive Metalcore / Djent (*Spiritbox, Meshuggah*) | `brutal guttural growl alternating soaring clean belting` | `progressive metalcore, djent riffs, tsymbaly folk intro, brutal guttural scream alternating ethereal clean female vocal, heavy drop, 150 bpm` |
| **KRUTЬ** | Neoclassical Chamber Ambient (*Ólafur Arnalds, Nils Frahm*) | `fragile breathy female vocal, intimate close-mic, subtle reverb` | `contemporary neoclassical, solo bandura arpeggios, emotive cello drone, warm ambient synth, intimate breathy female vocal, 75 bpm` |
| **Kozak System / Haydamaky** | Celtic Folk-Punk / Ethno-Rock (*Dropkick Murphys, Gogol Bordello*)| `raw passionate male lead, energetic anthemic belting` | `ethno-rock, live heavy guitars, authentic duda bagpipe hook, punchy live drums, energetic male lead, anthemic driving folk, 135 bpm` |

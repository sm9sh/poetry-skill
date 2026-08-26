# Western & Ukrainian Reference-to-Style Cheatsheet

Шпаргалка для безпечного перетворення референсів у легальні `safe style prompts` для `Suno AI / Flow Music` з **пріоритетом західних музичних жанрів і стандартів продакшну**, що гарантує фірмове західне звучання треку без шароварщини та дешевої локальної попси.

---

## 1. Головне правило: Орієнтація на західні жанри та саунд-дизайн

1. **Західний звуковий еталон**: Музична складова завжди спирається на західні жанрові конвенції (UK/US/Nordic/European Post-Punk, Darkwave, Synthwave, Trip-Hop, Alt-Pop, Shoegaze, Progressive Metalcore, Melodic Techno, Cinematic Ambient).
2. **Український вокал без шароварщини**: Текст і вокальні партії подаються чистою, глибокою українською мовою, але в аранжуванні використовується фірмовий західний продакшн (не провінційне диско, не весільний синтезатор і не шароварний псевдофольк).
3. **Сувора деперсоналізація**: Жодних імен артистів, гуртів, альбомів чи назв треків у фінальному prompt'і.
4. **Бюджет символів**: 80–180 символів (оптимально 80–150 символів).
5. **Обов'язковий Exclude проти локальної попси**: У полі `Exclude` завжди пригнічуються маркери локальної естради: `cheesy regional pop, post-soviet schlager, wedding synth brass, cheap accordion, generic euro-pop, tourist folk cliches`.

---

## 2. Мапа західних еталонів та безпечних стилів (Western Benchmarks)

### 1. Depeche Mode / Boy Harsher / Carpenter Brut Archetype (Dark Synthwave / EBM)
- **Звуковий ДНК**: Аналоговий бас Moog, гейтований 80s малий барабан, арпеджіатори, нічний кіберпанк-драйв, монотонний вокал.
- **Safe Style Prompt (137 символів)**:
  ```text
  dark synthwave, analog moog bass pulse, gated 80s snare, crisp electronic arpeggios, monotone male vocal, cyberpunk nocturnal, 120 bpm
  ```
- **Exclude**: `cheesy regional pop, wedding synth brass, cheap accordion, acoustic strumming, metallic highs`

---

### 2. Joy Division / The Cure / Molchat Doma Archetype (Post-Punk / Darkwave)
- **Звуковий ДНК**: Хорус на гітарі, пульсуючий високий бас, сухий вінтажний драм-машинний біт, меланхолійний баритон.
- **Safe Style Prompt (136 символів)**:
  ```text
  british post-punk, darkwave, chorus electric guitar, 80s drum machine, driving bassline, melancholic baritone male vocal, lo-fi nocturnal
  ```
- **Exclude**: `cheesy regional pop, post-soviet schlager, cheerful accordion, bright pop autotune`

---

### 3. Massive Attack / Portishead / Morcheeba Archetype (Trip-Hop / Bristol Sound)
- **Звуковий ДНК**: Вініловий даунтемпо-брейкбіт, теплий Rhodes, глибокий саб-бас 808, димчастий жіночий напівшепіт, плівкове насичення.
- **Safe Style Prompt (139 символів)**:
  ```text
  trip-hop, downtempo, dusty vinyl breakbeat, warm rhodes piano, deep 808 sub bass, breathy female vocal, cinematic tape warmth, 85 bpm
  ```
- **Exclude**: `cheesy euro-pop, fast edm drop, wedding synth brass, aggressive shouting`

---

### 4. Billie Eilish / Lorde / Banks Archetype (Minimalist Dark Alt-Pop)
- **Звуковий ДНК**: Мінімалістичний 808 саб, інтимний ASMR-вокал (близький мікрофон), органічний перкусійний фолі-шум, просторовий мікс.
- **Safe Style Prompt (137 символів)**:
  ```text
  minimalist alt-pop, heavy 808 sub bass, crisp close-mic breathy female vocal, organic foley percussions, dark spatial production, 100 bpm
  ```
- **Exclude**: `tourist folk cliches, cheesy polka accordion, 90s eurodance, brass fanfare, metallic sibilance`

---

### 5. Bring Me The Horizon / Spiritbox / Architects Archetype (Modern Metalcore / Djent)
- **Звуковий ДНК**: Дроп-тюнінг, низькі джент-рифи, щільні панчеві барабани, контраст брутального гроулу та епічного чистого приспіву.
- **Safe Style Prompt (142 символи)**:
  ```text
  modern progressive metalcore, drop-tuned djent guitar riffs, punchy aggressive drums, brutal screaming alternating ethereal clean vocal, 150 bpm
  ```
- **Exclude**: `cheap midi brass, mumble vocal, acoustic ukulele, dance club beat, tinny cymbals`

---

### 6. Slowdive / Beach House / Arctic Monkeys Archetype (Shoegaze / Dream Pop / Indie)
- **Звуковий ДНК**: Стіна реверберованих гітар, вінтажний хорус, теплий аналоговий грув, повітряний вокал у просторі.
- **Safe Style Prompt (139 символів)**:
  ```text
  shoegaze, dream pop, wall of sound reverb guitars, jangly indie groove, whispered breathy vocal, lush vintage chorus, atmospheric slow groove
  ```
- **Exclude**: `harsh digital clipping, aggressive rap, dry close mix, stadium shouting, cheesy pop brass`

---

### 7. Bicep / Moderat / Jon Hopkins Archetype (Melodic Techno / Electronica)
- **Звуковий ДНК**: Гіпнотичні аналогові модулярні патерни, атмосферні вокальні чопи, глибокий чотиридольний біт, емоційне електронне розгортання.
- **Safe Style Prompt (138 символів)**:
  ```text
  melodic techno, electronica, hypnotic analog arpeggios, atmospheric vocal chops, deep rolling sub bass, four-on-the-floor groove, 124 bpm
  ```
- **Exclude**: `cheap midi brass, wedding accordion, tourist folk, acoustic strumming, generic pop drop`

---

### 8. Hans Zimmer / Max Richter Archetype (Cinematic Ambient / Neoclassical)
- **Звуковий ДНК**: Акустичне фортепіано з фетровим демпфером, струнний ансамбль, теплий ембієнтний саб-бас, кінематографічний простір.
- **Safe Style Prompt (137 символів)**:
  ```text
  contemporary cinematic ambient, felt upright piano, emotive soaring cello, warm tape saturation, intimate whispered vocal, 70 bpm
  ```
- **Exclude**: `electronic dance drums, distorted guitars, aggressive shouting, festival drop, cheesy regional pop`

---

## 3. Мапа перекладу українських артистів у західний саунд-дизайн

| Український артист-орієнтир | Західний звуковий еквівалент | Формула Style Prompt (80–180 Chars) |
|---|---|---|
| **SadSvit / Mistmorn** | Joy Division / Molchat Doma (Post-Punk) | `british post-punk, darkwave, 130 bpm, driving bassline, melancholic baritone male vocal, chorus electric guitar, lo-fi night production` |
| **Kurs Valüt** | Boy Harsher / Depeche Mode (Dark Synth) | `dark synthwave, minimal wave, coldwave, analog bass pulse, monotone male recitative, crisp electronic drums, nocturnal, 122 bpm` |
| **Latexfauna** | Men I Trust / Mac DeMarco (Dream Pop/Indie) | `dream pop, indie funk, wall of sound reverb guitars, whispered breathy vocal, lush chorus, sensual slow groove, 90 bpm` |
| **Jinjer / Motanka** | Spiritbox / Meshuggah (Modern Metalcore) | `modern progressive metalcore, djent riffs, punchy drums, brutal guttural scream alternating ethereal clean female vocal, 150 bpm` |
| **KRUTЬ** | Ólafur Arnalds / Agnes Obel (Neoclassical) | `contemporary neoclassical, acoustic plucked strings, emotive cello, warm ambient synth, intimate breathy female vocal, 75 bpm` |
| **DakhaBrakha** | Dead Can Dance / Wardruna (Avant-Dark-Folk) | `dark avant-folk, tribal percussion, cello drone, hypnotic dark polyphony, atmospheric cinematic acoustic, 115 bpm` |

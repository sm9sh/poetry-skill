# Mood To Style Mapping Guide (Western Sound Standards & Multi-Platform v8)

Матриця перетворення емоційного ядра та настрою української поезії у високоточні параметри стилю для **Suno AI (v4.5 / v5.5)**, **Udio AI (v4)** та **Google Flow Music (Lyria 3.5)** з **пріоритетом західних музичних жанрів, вокального Triple-Stack та саунд-дизайну**.

---

## 1. Архітектурний місток

```text
Емоція / Поетичний настрій ──> Західний жанровий кластер ──> BPM / Пульс ──> Vocal Triple-Stack ──> Інструменти ──> Продакшн ──> Exclude (Анти-попса)
```

---

## 2. Матриця 8 емоційних кластерів та мультиплатформних промптів

### 1. Нічна урбаністична меланхолія, екзистенційна самотність (Post-Punk / Darkwave)
- **Західний жанр**: British Post-Punk / Darkwave (*Joy Division, The Cure, Molchat Doma*)
- **BPM / Енергія**: 125–132 BPM, швидкий монотонний біг баса
- **Vocal Triple-Stack**: `melancholic baritone male vocal, deadpan monotone delivery, cold plate reverb`
- **Інструменти**: `chorus electric guitar, punchy 80s drum machine, driving bassline`
- **Продакшн**: `lo-fi nocturnal production, raw tape saturation, muted high-end`
- **Suno Method 1 (Conversational)**:
  `British post-punk, melancholic baritone male vocal, driving bassline, chorus electric guitar, 80s drum machine, lo-fi nocturnal mood, 128 BPM.` (143 chars)
- **Suno Method 2 (Tag Matrix)**:
  `british post-punk, darkwave, melancholic, baritone male vocal, deadpan delivery, dry mic, chorus electric guitar, driving bassline, 80s drum machine, 128 bpm` (158 chars)
- **Udio v4 Prompt**:
  `British Post-Punk, Darkwave, 1980s analog recording, melancholic baritone male vocal, chorus electric guitar, tight drum machine, driving bassline, lo-fi tape saturation, 128 BPM`
- **Flow Music (Lyria 3.5)**:
  `Create a moody British post-punk song with melancholic baritone male vocal, driving bassline, and chorus guitars, capturing the lonely atmosphere of a rainy night city at 128 BPM.`
- **Exclude**: `cheesy regional pop, post-soviet schlager, cheerful accordion, bright pop autotune, metallic highs`

---

### 2. Кіберпанк-морок, техногенний холод, безсоння (Dark Synthwave / EBM)
- **Західний жанр**: Dark Synthwave / EBM / Cyberpunk (*Depeche Mode, Carpenter Brut, Boy Harsher*)
- **BPM / Енергія**: 120–126 BPM, холодний механічний грув
- **Vocal Triple-Stack**: `monotone male recitative, deadpan spoken cadence, coldwave vocal`
- **Інструменти**: `analog moog bass pulse, gated 80s snare, crisp electronic arpeggios`
- **Продакшн**: `sleek cold production, clinical dystopian space, tight dry transients`
- **Suno Method 1 (Conversational)**:
  `Dark synthwave, monotone male vocal, analog moog bass pulse, gated 80s snare, crisp electronic arpeggios, cyberpunk nocturnal mood, 120 BPM.` (138 chars)
- **Suno Method 2 (Tag Matrix)**:
  `dark synthwave, cyberpunk ebm, nocturnal, monotone male vocal, dry close-mic, analog moog bass pulse, gated 80s snare, electronic arpeggios, sleek cold mix, 120 bpm` (167 chars)
- **Udio v4 Prompt**:
  `Dark Synthwave, EBM, 1980s electronic, monotone male vocal, analog moog bassline, gated snare, crisp arpeggios, clinical dystopian production, 120 BPM`
- **Flow Music (Lyria 3.5)**:
  `Generate a cold cyberpunk dark synthwave track with deep analog Moog bass pulse, crisp electronic arpeggios, and dry monotone male recitative at 120 BPM.`
- **Exclude**: `cheesy regional pop, wedding synth brass, cheap accordion, acoustic strumming, boomy low-end`

---

### 3. Глибока печаль, димний спокій, вечірній дощ (Trip-Hop / Downtempo)
- **Західний жанр**: Bristol Trip-Hop / Downtempo (*Massive Attack, Portishead, Morcheeba*)
- **BPM / Енергія**: 80–90 BPM, вініловий повільний брейкбіт
- **Vocal Triple-Stack**: `breathy smoky female vocal, intimate whispered delivery, subtle tape warmth`
- **Інструменти**: `dusty vinyl breakbeat, warm rhodes piano, deep 808 sub bass`
- **Продакшн**: `cinematic tape warmth, smoky reverb decay, analog saturation`
- **Suno Method 1 (Conversational)**:
  `Bristol trip-hop, breathy smoky female vocal, dusty vinyl breakbeat, warm rhodes piano, deep 808 sub bass, dark melancholic tape warmth, 85 BPM.` (145 chars)
- **Suno Method 2 (Tag Matrix)**:
  `trip-hop, downtempo, melancholic, breathy smoky female vocal, intimate delivery, dry mic, dusty vinyl breakbeat, warm rhodes piano, deep 808 sub bass, tape hiss, 85 bpm` (170 chars)
- **Udio v4 Prompt**:
  `Bristol Trip-Hop, Downtempo, 1990s vinyl production, smoky female vocal, warm rhodes chords, deep 808 sub bass, dusty acoustic breakbeat, tape saturation, 85 BPM`
- **Flow Music (Lyria 3.5)**:
  `Produce an intimate Bristol trip-hop track with breathy smoky female vocal, dusty vinyl breakbeat, warm Rhodes piano chords, and deep sub-bass at 85 BPM.`
- **Exclude**: `cheesy euro-pop, fast edm drop, wedding synth brass, aggressive shouting, digital clipping`

---

### 4. Інтимна сповідь, нічна тиша, тендітність (Minimalist Alt-Pop / Dark Pop)
- **Західний жанр**: Minimalist Dark Alt-Pop (*Billie Eilish, Lorde, Banks*)
- **BPM / Енергія**: 95–105 BPM, мінімалістичний грув
- **Vocal Triple-Stack**: `close-mic breathy female vocal, ASMR vocal texture, fragile whisper, dry upfront mix`
- **Інструменти**: `heavy 808 sub bass, organic foley percussion, muted acoustic guitar`
- **Продакшн**: `dark spatial mix, wide stereo imaging, upfront dry vocals`
- **Suno Method 1 (Conversational)**:
  `Minimalist alt-pop, intimate breathy female vocal, heavy 808 sub bass, organic foley percussions, dark spatial production, 100 BPM.` (131 chars)
- **Suno Method 2 (Tag Matrix)**:
  `minimalist alt-pop, dark pop, intimate, breathy female vocal, ASMR close-mic, dry delivery, heavy 808 sub bass, organic foley percussions, spatial mix, 100 bpm` (160 chars)
- **Udio v4 Prompt**:
  `Minimalist Alt-Pop, Dark Pop, modern intimate production, ASMR breathy female vocal, heavy 808 sub bass, organic percussions, upfront dry mix, 100 BPM`
- **Flow Music (Lyria 3.5)**:
  `Create a minimalist dark alt-pop ballad with intimate ASMR breathy female vocal, heavy 808 sub bass, and organic percussion in a wide spatial mix at 100 BPM.`
- **Exclude**: `tourist folk cliches, cheesy polka accordion, 90s eurodance, brass fanfare, metallic sibilance`

---

### 5. Люта боротьба, екзистенційний крик, спротив (Modern Metalcore / Djent)
- **Західний жанр**: Progressive Metalcore / Modern Djent (*Bring Me The Horizon, Spiritbox, Architects*)
- **BPM / Енергія**: 145–160 BPM, екстремальна динаміка з контрастними спадами
- **Vocal Triple-Stack**: `brutal guttural scream alternating soaring ethereal clean vocal`
- **Інструменти**: `drop-tuned djent guitar riffs, punchy aggressive drums, heavy sub drop`
- **Продакшн**: `wall of sound metal production, modern punchy drum transients`
- **Suno Method 1 (Conversational)**:
  `Progressive metalcore, brutal screaming alternating soaring clean vocal, drop-tuned djent riffs, punchy drums, aggressive dark mood, 150 BPM.` (143 chars)
- **Suno Method 2 (Tag Matrix)**:
  `progressive metalcore, djent, aggressive, brutal screaming, clean melodic chorus, drop-tuned guitars, heavy double-bass drums, massive sub drop, wall of sound, 150 bpm` (168 chars)
- **Udio v4 Prompt**:
  `Progressive Metalcore, Modern Djent, heavy drop tuning, dual vocals with brutal scream and soaring clean melodic chorus, aggressive punchy drums, 150 BPM`
- **Flow Music (Lyria 3.5)**:
  `Generate a heavy progressive metalcore track featuring brutal screams in verses alternating with a soaring clean melodic chorus, drop-tuned djent riffs at 150 BPM.`
- **Exclude**: `cheap midi brass, mumble vocal, acoustic ukulele, dance club beat, tinny cymbals, schlager`

---

### 6. Чуттєва мрійливість, нічне марення (Shoegaze / Dream Pop)
- **Західний жанр**: Shoegaze / Dream Pop / Indie (*Slowdive, Beach House, Arctic Monkeys*)
- **BPM / Енергія**: 85–95 BPM, плавний повільний грув
- **Vocal Triple-Stack**: `whispered breathy vocal, delicate airy high register, lush vintage chorus`
- **Інструменти**: `wall of sound reverb guitars, shimmering synth pads, warm rounded bassline`
- **Продакшн**: `lush vintage spatial reverb, tape saturated guitars, wide stereo field`
- **Suno Method 1 (Conversational)**:
  `Shoegaze dream pop, whispered breathy vocal, wall of sound reverb guitars, jangly indie groove, lush vintage chorus, atmospheric mood, 90 BPM.` (143 chars)
- **Suno Method 2 (Tag Matrix)**:
  `shoegaze, dream pop, ethereal, whispered breathy vocal, delicate delivery, lush chorus, wall of sound reverb guitars, warm bassline, vintage tape mix, 90 bpm` (158 chars)
- **Udio v4 Prompt**:
  `Shoegaze, Dream Pop, 1990s vintage reverb guitars, whispered breathy vocal, shimmering synth pads, warm analog bass, ethereal spatial production, 90 BPM`
- **Flow Music (Lyria 3.5)**:
  `Produce an ethereal shoegaze dream-pop track with wall of sound reverb guitars, shimmering synths, and whispered breathy vocals in a lush spatial mix at 90 BPM.`
- **Exclude**: `harsh digital clipping, aggressive rap, dry close mix, stadium shouting, cheesy pop brass`

---

### 7. Електронна ейфорія, клубний гіпноз, рух (Melodic Techno / Electronica)
- **Західний жанр**: Melodic Techno / Electronica (*Bicep, Moderat, Jon Hopkins*)
- **BPM / Енергія**: 122–126 BPM, гіпнотичний пульс чотири-на-чотири
- **Vocal Triple-Stack**: `atmospheric vocal chops, ethereal whispered female vocal, subtle tape delay`
- **Інструменти**: `hypnotic analog arpeggios, deep rolling sub bass, four-on-the-floor groove`
- **Продакшн**: `clean modern production, wide stereo club mix, transparent dynamic master`
- **Suno Method 1 (Conversational)**:
  `Melodic techno, atmospheric vocal chops, hypnotic analog arpeggios, deep rolling sub bass, four-on-the-floor groove, euphoric mood, 124 BPM.` (141 chars)
- **Suno Method 2 (Tag Matrix)**:
  `melodic techno, electronica, hypnotic, atmospheric vocal chops, ethereal delivery, analog modular arpeggios, rolling sub bass, four-on-the-floor, 124 bpm` (155 chars)
- **Udio v4 Prompt**:
  `Melodic Techno, Electronica, modular synthesizer arpeggios, atmospheric vocal chops, rolling sub bass, four-on-the-floor kick, transparent club master, 124 BPM`
- **Flow Music (Lyria 3.5)**:
  `Create a hypnotic melodic techno track with rolling sub-bass, modular analog synth arpeggios, and ethereal atmospheric vocal chops at 124 BPM.`
- **Exclude**: `cheap midi brass, wedding accordion, tourist folk, acoustic strumming, generic pop drop`

---

### 8. Кінематографічна велич, пам'ять, споглядання (Cinematic Ambient / Neoclassical)
- **Західний жанр**: Contemporary Cinematic Ambient / Neoclassical (*Hans Zimmer, Max Richter, Ólafur Arnalds*)
- **BPM / Енергія**: 65–75 BPM, повільне величне розгортання
- **Vocal Triple-Stack**: `intimate whispered vocal, emotive breathy soprano, subtle room plate`
- **Інструменти**: `felt upright piano, emotive soaring cello, warm ambient synth drone, bandura accents`
- **Продакшн**: `warm tape saturation, cinematic hall reverb, pristine dynamic range`
- **Suno Method 1 (Conversational)**:
  `Cinematic ambient, intimate whispered vocal, felt upright piano, emotive soaring cello, warm tape saturation, reflective solemn mood, 70 BPM.` (143 chars)
- **Suno Method 2 (Tag Matrix)**:
  `cinematic ambient, neoclassical, solemn, intimate whispered vocal, dry close-mic, felt upright piano, emotive cello, warm synth drone, tape warmth, 70 bpm` (156 chars)
- **Udio v4 Prompt**:
  `Cinematic Ambient, Contemporary Neoclassical, felt piano, emotive soaring cello, warm analog drone, intimate whispered vocal, pristine dynamic acoustic space, 70 BPM`
- **Flow Music (Lyria 3.5)**:
  `Generate a solemn cinematic ambient neoclassical soundtrack featuring felt upright piano, emotive cello drone, and intimate whispered vocal at 70 BPM.`
- **Exclude**: `electronic dance drums, distorted guitars, aggressive shouting, festival drop, cheesy regional pop`

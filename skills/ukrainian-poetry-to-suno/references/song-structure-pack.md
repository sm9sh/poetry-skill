# Suno v6-mini & Lyria 3.5 Song Structure & Metatag Pack

Повний каталог структурних шаблонів, стандартного синтаксису метатегів та інлайн вокальних жестів для **Suno AI (v6-mini)** та **Lyria 3.5**.

---

## 1. Синтаксична граматика парсерів ШІ-аудіомоделей

```text
┌─────────────────────────┬──────────────────────────────────────────┬────────────────────────────────────────────────────────┐
│ Символи синтаксису      │ Як інтерпретує аудіо-модель              │ Приклад правильного використання                       │
├─────────────────────────┼──────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ [Квадратні дужки]       │ Неспіваний метатег / звукова вказівка    │ [Vocal Intro - dynamic acapella, dry and close],       │
│                         │ (структура, інструменти, динаміка, темп) │ [Beat Drop - heavy fuzz bass], [Verse 2], [Mega-Chorus]│
├─────────────────────────┼──────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ (Круглі дужки)          │ Співаний бек-вокал / вокальні жести      │ [Whispered], [Belted], [Falsetto], [Screamed],         │
│                         │ УВАГА: Lyria 3.5 та Suno співають ()!   │ [Ad-lib], [Building intensity], [Key Change],          │
│                         │                                          │ [Half-time feel], [Harmonized], (луна), (ніколи знов)  │
├─────────────────────────┼──────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ ВЕЛИКІ ЛІТЕРИ ГОЛОСНИХ  │ Фіксація точного наголосу для ШІ-вокалу  │ вИпадок, чорнОзем, листопАд, зЕмлю, дорОга/дорогА      │
├─────────────────────────┼──────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ Дефіси у словах         │ Складовий поділ для швидких темпів       │ за-спі-вай, не-по-втор-ний (запобігає ковтанню слів)   │
└─────────────────────────┴──────────────────────────────────────────┴────────────────────────────────────────────────────────┘
```

---

## 2. Повний довідник стандартних метатегів `[Square Brackets]`

### 2.1 Секційні маркери структури
- `[Intro]` / `[Atmospheric Synth Intro]`
- `[Vocal Intro - dynamic acapella, dry and close]` (The 5-Second Rule)
- `[Beat Drop - heavy fuzz bass, punchy driving drums]`
- `[Verse 1]` / `[Verse 1 - rhythmic, dry vocals, clean muted guitar]`
- `[Pre-Chorus]` / `[Pre-Chorus - building intensity, rising snare roll]`
- `[Chorus]` / `[Chorus - explosive, epic harmonies, wide stereo]`
- `[Verse 2 - add driving tambourine, shaker, backing vocals]` (другий куплет додає новий шар аранжування)
- `[Post-Chorus - rhythmic vocal chops, synth arpeggio]`
- `[Instrumental Break - gritty fuzz slide guitar solo]`
- `[Guitar Solo]` / `[Bandura Solo]` / `[Sopilka Solo]` / `[Cello Solo]`
- `[Bridge - acoustic, stripped-back, warm Rhodes chords]`
- `[Breakdown - vocal and sub-bass only, intimate, dry]` (15–20с спад енергії)
- `[Mega-Chorus - maximum energy, layered harmonies, guitars clashing]`
- `[Outro - fading out, solo analog synth, tape hiss]` (Лаконічне завершення $\le 20$с)
- `[End]` / `[Cold End]` / `[Abrupt Cut]`

### 2.2 Динамічні та темпові вказівки
- `[Tempo: 120 BPM]`, `[Tempo: Half-Time]`, `[Tempo: Double-Time]`
- `[Key: D Minor]`, `[Key: A Minor]`
- `[Dynamic: Crescendo]`, `[Dynamic: Pianissimo]`, `[Dynamic: Fortissimo]`
- `[Silence]`, `[Beat Cut]`, `[Acapella]`, `[Stripped Back]`

---

## 3. Повний довідник вокальних вказівок `[Square Brackets]`

Вказівки подачі ставляться в **квадратних дужках** окремим рядком перед фразою (або в тезі секції: `[Verse 1 - whispered]`). У круглих дужках модель їх заспіває, тому `( )` лишаються тільки для співаного бек-вокалу та ехо (`(ніколи знов)`, `(о-о-о)`).

| Інлайн вокальний жест | Характер впливу на вокал ШІ | Рекомендована позиція у треку |
|---|---|---|
| **`[Whispered]`** / **`[Whispered, intimate]`** | Перехід на інтимний шепіт або близький ASMR-вокал | `[Verse 1]`, `[Breakdown]` |
| **`[Belted]`** / **`[Belted, powerful]`** | Вимога потужного, відкритого грудного вокалу на високій ноті | `[Chorus]`, `[Mega-Chorus]` |
| **`[Falsetto]`** | Перехід на фальцет для створення емоційної крихкості | `[Pre-Chorus]`, `[Bridge]` |
| **`[Screamed]`** / **`[Growl]`** | Перехід на агресивний вокал у рок- чи метал-генераціях | `[Verse 2]`, `[Bridge]` |
| **`[Ad-lib]`** / **`[Vocal runs]`** | Вокальні мелізми та фонова імпровізація | `[Post-Chorus]`, `[Outro]` |
| **`[Building intensity]`** | Плавне підвищення гучності та агресії вокалу | `[Pre-Chorus]` |
| **`[Key Change]`** | Провокація ШІ на тональну модуляцію | Перед `[Mega-Chorus]` |
| **`[Half-time feel]`** | Уповільнення ритмічного відчуття вокалу вдвічі (лікує скоромовку) | Швидкі куплети |
| **`[Harmonized]`** / **`[Layered harmonies]`** | Вимога увімкнути багатоголосся на ключовому слові хука | Кульмінаційні фрази приспіву |

---

## 4. 8 Готових структурних шаблонів за жанрами (з розвитком другого куплету та Breakdown)

### Шаблон 1: British Post-Punk / Darkwave
```text
[Vocal Intro - dynamic baritone acapella, dry]
(Порожній проспект ковтає ліхтарі...)
[Beat Drop - driving chorus bassline, 80s drum machine]

[Verse 1 - rhythmic staccato, deadpan baritone]
Холодний дощ стікає по вікні,
Ми знову чужі у цьому дворі,
(у цьому дворі)
Де пам'ять згорає на самому дні.

[Pre-Chorus - rising snare roll, building tension]
[Building intensity]
І кроки відлунюють в темну імлу...

[Chorus - explosive, wide chorus guitars, wall of sound]
[Belted]
Нічний трамвай іржавим колесом,
[Layered harmonies]
Везе мій сум за темний горизонт!

[Verse 2 - add driving tambourine, syncopated backing, sharp stereo guitars]
Сліди на асфальті змиває вода,
(луна стін)
І ніч непомітно повз нас проплива.

[Chorus - wide stereo, high energy]
Нічний трамвай іржавим колесом,
Везе мій сум за темний горизонт!

[Breakdown - vocal and bassline only, intimate, dry]
[Whispered]
Лиш вікна, що світять в унісон...

[Mega-Chorus - maximum energy, soaring layered harmonies, clashing guitars]
[Key Change]
[Belted, powerful]
Нічний трамвай іржавим колесом,
[Layered harmonies]
Везе мій сум за темний горизонт!

[Outro - fading out, solo analog synth, tape hiss]
[End]
```

---

### Шаблон 2: Dark Synthwave / Cyberpunk EBM
```text
[Intro - atmospheric analog moog swell, vinyl crackle]
[Beat Drop - aggressive moog bass pulse, gated 80s snare]

[Verse 1 - monotone male recitative, dry close-mic]
Екрани пульсують неоновим склом,
(холодний неон)
Місто засинає під мертвим крилом.

[Pre-Chorus - rising electronic arpeggios]
[Building intensity]
Сигнали зникають у морі датчиків...

[Chorus - explosive analog synth lead, wide stereo]
[Belted]
Кібер-ніч розчиняє мою тінь,
[Layered harmonies]
Крізь дроти у безкінечну глибинь!

[Verse 2 - add driving electronic percussion, syncopated vocal chops]
Комп'ютерний шум заспокоює біль,
(нуль і один)
І пам'ять стирає останню з подій.

[Chorus - full synthesizer energy]
Кібер-ніч розчиняє мою тінь,
Крізь дроти у безкінечну глибинь!

[Breakdown - monotone vocal and sub-bass pulse only]
[Whispered]
Тільки струм у змерзлих пальцях...

[Mega-Chorus - maximum synth wall of sound, heavy gated drums]
[Layered harmonies]
[Belted, powerful]
Кібер-ніч розчиняє мою тінь,
Крізь дроти у безкінечну глибинь!

[Outro - pulsing synth decay, fast cutoff filter fade]
[End]
```

---

### Шаблон 3: Bristol Trip-Hop / Downtempo
```text
[Vocal Intro - breathy smoky female acapella, dry]
(Дим опускається на мокрий брук...)
[Beat Drop - dusty vinyl breakbeat, warm rhodes, deep 808 sub]

[Verse 1 - intimate close-mic whisper, slow groove]
[Whispered]
У шафі холодній сховався мій жаль,
(тихий жаль)
За склом пропливає розмита печаль.

[Chorus - soaring melodic vocal, smoky room reverb]
[Falsetto]
Ооооой, не клич мене в темряву знову,
[Echo]
Залиш мені тільки розмову...

[Verse 2 - add organic shaker, vinyl crackle, subtle muted trumpet]
Краплі води відбивають ліхтар,
І ніч розгортає безмерний товар.

[Chorus]
Ооооой, не клич мене в темряву знову,
Залиш мені тільки розмову...

[Breakdown - vocal and warm rhodes only]
[Whispered, intimate]
Лиш тиша між нами...

[Mega-Chorus - full vinyl warmth, layered vocal harmonies]
[Layered harmonies]
Ооооой, не клич мене в темряву знову,
Залиш мені тільки розмову!

[Outro - slow fading breakbeat, vinyl runout groove]
[End]
```

---

### Шаблон 4: Minimalist Dark Alt-Pop
```text
[Vocal Intro - solo close-mic ASMR breathy vocal]
(Чуєш, як б'ється пульс...)
[Beat Drop - heavy 808 sub bass, organic foley snaps]

[Verse 1 - staccato whispers, intimate dry mix]
[Whispered]
Тіні на стінах танцюють без слів,
(без слів)
Холод кімнати розрізав мій гнів.

[Pre-Chorus - rising foley clicks]
[Building intensity]
Я рахую до трьох...

[Chorus - explosive wide open space, deep 808 glide]
[Belted]
Оооох, ми згораємо в цьому вогні,
[Layered harmonies]
Лиш попіл лишився мені!

[Verse 2 - add syncopated acoustic foley, vocal chops, stereo shaker]
Пальці торкаються мерзлого скла,
(холод скла)
Втрачена ніжність навік утекла.

[Chorus]
Оооох, ми згораємо в цьому вогні,
Лиш попіл лишився мені!

[Breakdown - isolated breathy vocal and sub-bass swell only]
[Whispered]
Нічого не бійся...

[Mega-Chorus - maximum 808 power, multi-layered soaring vocal stack]
[Key Change]
[Belted, powerful]
Оооох, ми згораємо в цьому вогні,
[Layered harmonies]
Лиш попіл лишився мені!

[Outro - intimate whispered fade out]
[End]
```

---

### Шаблон 5: Progressive Metalcore / Modern Djent
```text
[Vocal Intro - brutal guttural scream hook]
(ПРОКИНЬСЯ!)
[Beat Drop - low-tuned djent riff, double-bass drum barrage, sub drop]

[Verse 1 - aggressive rhythmic growl, heavy palm-muted groove]
[Screamed]
Земля розкололась під нашим тяжким кроком!
(тяжким кроком)
Стіна піднімається перед сліпим Оком!

[Pre-Chorus - rising clean vocal, building tempo]
[Building intensity]
[Falsetto]
І крізь темряву я бачу світло...

[Chorus - epic soaring clean vocal, massive wall of sound]
[Belted]
Ми піднімемось знову з руїн і золи,
[Layered harmonies]
Хоч би як нас вітри не гнули!

[Verse 2 - add syncopated double-kick patterns, harsh scream backing]
[Screamed]
Кров на камінні застигла сталлю,
(сталлю!)
Ми не заплачемо перед печаллю!

[Chorus]
Ми піднімемось знову з руїн і золи,
Хоч би як нас вітри не гнули!

[Breakdown - massive half-time djent breakdown, brutal guttural screams, sub drop]
[Screamed]
ЛАМАЙ! ЗНИЩУЙ КОРДОНИ!

[Mega-Chorus - ultimate climax, soaring clean vocal layered with harsh scream]
[Key Change]
[Belted, powerful]
[Layered harmonies]
Ми піднімемось знову з руїн і золи,
Хоч би як нас вітри не гнули!

[Outro - heavy fading djent guitar feedback, final abrupt snare cut]
[Cold End]
```

---

### Шаблон 6: Shoegaze / Dream Pop
```text
[Intro - shimmering reverb guitar swell, lush vintage chorus]
[Verse 1 - whispered breathy vocal, floating guitar textures]
[Whispered]
Хмари пливуть над сріблястим ліском,
(над ліском)
Вітер торкається хвиль язиком.

[Chorus - wall of sound guitars, soaring ethereal vocal]
[Falsetto]
Ооооо-ааааа, засинає ріка у тумані,
[Layered harmonies]
Всі тривоги лишились в остогоні...

[Verse 2 - add jangly rhythm guitar, soft tambourine, stereo arpeggios]
Зорі випали на мокру траву,
(на траву)
Я уві сні цим повітрям живу.

[Chorus]
Ооооо-ааааа, засинає ріка у тумані,
Всі тривоги лишились в остогоні...

[Breakdown - delicate whispered vocal and solo chorus guitar only]
[Whispered, intimate]
Тільки спокій...

[Mega-Chorus - maximum reverb saturation, epic soaring harmonies]
[Belted]
[Layered harmonies]
Ооооо-ааааа, засинає ріка у тумані,
Всі тривоги лишились в остогоні!

[Outro - slow ambient guitar decay, tape hiss fade]
[End]
```

---

### Шаблон 7: Melodic Techno / Electronica
```text
[Intro - hypnotic analog synth arpeggio, ambient filter swell]
[Beat Drop - four-on-the-floor kick, rolling sub-bass]

[Verse 1 - rhythmic spoken recitative, dry upfront]
Ритм у вісках відраховує крок,
(один-два)
Ніч розливає густий свій ковток.

[Pre-Chorus - rising snare roll, opening filter]
[Building intensity]
Час зупинився...

[Chorus - euphoric melodic drop, wide vocal chops]
[Layered harmonies]
Світло неону у наших очах,
(у очах)
Розчиняється темний наш страх!

[Verse 2 - add syncopated hi-hats, modular acid synth lead]
Шум автомагістралі звучить як струна,
(як струна)
Нас огортає нічна глибина.

[Chorus]
Світло неону у наших очах,
Розчиняється темний наш страх!

[Breakdown - kick mute, atmospheric pad and vocal chops only]
[Whispered]
Відчуй цей пульс...

[Mega-Chorus - full drop with rolling sub-bass and layered anthemic lead]
[Ad-lib]
[Layered harmonies]
Світло неону у наших очах,
Розчиняється темний наш страх!

[Outro - filtered synth arpeggio decay, four-bar kick fade]
[End]
```

---

### Шаблон 8: Contemporary Cinematic Ambient / Neoclassical
```text
[Intro - felt upright piano arpeggios, emotive cello drone]
[Verse 1 - intimate whispered female soprano, close-mic]
[Whispered]
Сніг опадає на старі дахи,
(на дахи)
Сплять у дібровах знеможені птахи.

[Chorus - soaring emotive cello, rich hall space]
[Falsetto]
Ооооой, збережи цю мовчанку святу,
[Echo]
Крізь негоду й нічну самоту...

[Verse 2 - add solo acoustic bandura plucking, warm string quartet]
Пам'ять торкається білих сторінок,
(білих сторінок)
Сонце малює на склі візерунок.

[Chorus]
Ооооой, збережи цю мовчанку святу,
Крізь негоду й нічну самоту...

[Breakdown - solo bandura and whispered vocal only]
[Whispered, intimate]
Лиш тиша і світло...

[Mega-Chorus - full symphonic string swell, soaring expressive belting]
[Belted, powerful]
[Layered harmonies]
Ооооой, збережи цю мовчанку святу,
Крізь негоду й нічну самоту!

[Outro - solo felt piano chord decay, ambient silence]
[Cold End]
```

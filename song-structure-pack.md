# Suno AI, Udio & Google Flow Music Song Structure & Metatag Pack (v8)

Повний каталог структурних шаблонів, стандартного синтаксису метатегів та інлайн вокальних жестів для **Suno AI (v4.5 / v5.5)**, **Udio AI (v4)** та **Google Flow Music (Lyria 3.5)**.

---

## 1. Синтаксична граматика парсерів ШІ-аудіомоделей

```text
┌─────────────────────────┬──────────────────────────────────────────┬────────────────────────────────────────────────────────┐
│ Символи синтаксису      │ Як інтерпретує аудіо-модель              │ Приклад правильного використання                       │
├─────────────────────────┼──────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ [Квадратні дужки]       │ Неспіваний метатег / звукова вказівка    │ [Vocal Intro - dynamic acapella, dry and close],       │
│                         │ (структура, інструменти, динаміка, темп) │ [Beat Drop - heavy fuzz bass], [Verse 2], [Mega-Chorus]│
├─────────────────────────┼──────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ (Круглі дужки)          │ Співаний бек-вокал / вокальні жести      │ (whispered), (belted), (falsetto), (screamed),         │
│                         │ УВАГА: Flow Music та Suno співають ()!   │ (ad-lib), (building intensity), (key change),          │
│                         │                                          │ (half-time feel), (harmonized), (луна), (ніколи знов)  │
├─────────────────────────┼──────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ ВЕЛИКІ ЛІТЕРИ ГОЛОСНИХ  │ Фіксація точного наголосу для ШІ-вокалу  │ вИпадок, чорнОзем, прИйде, заспівАй, моЯ, дорОга       │
├─────────────────────────┼──────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ *Зірочки*               │ Udio Inpainting синтаксис заміни слів    │ *static sky* (офіційний синтаксис Udio v4 Inpainting;  │
│                         │                                          │ уникати в текстах для Suno та Flow Music)              │
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
- `[Verse 2 - add driving tambourine, shaker, backing vocals]` (Розвиток за Венсом Пауеллом)
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

## 3. Повний довідник інлайн вокальних жестів `(Round Parentheses)`

Ці команди впроваджуються **всередині** ліричних рядків, безпосередньо перед або після потрібного слова, щоб керувати емоціями та динамікою вокаліста ШІ:

| Інлайн вокальний жест | Характер впливу на вокал ШІ | Рекомендована позиція у треку |
|---|---|---|
| **`(whispered)`** / **`(whispered, intimate)`** | Перехід на інтимний шепіт або близький ASMR-вокал | `[Verse 1]`, `[Breakdown]` |
| **`(belted)`** / **`(belted, powerful)`** | Вимога потужного, відкритого грудного вокалу на високій ноті | `[Chorus]`, `[Mega-Chorus]` |
| **`(falsetto)`** | Перехід на фальцет для створення емоційної крихкості | `[Pre-Chorus]`, `[Bridge]` |
| **`(screamed)`** / **`(growl)`** | Перехід на агресивний вокал у рок- чи метал-генераціях | `[Verse 2]`, `[Bridge]` |
| **`(ad-lib)`** / **`(vocal runs)`** | Вокальні мелізми та фонова імпровізація | `[Post-Chorus]`, `[Outro]` |
| **`(building intensity)`** | Плавне підвищення гучності та агресії вокалу | `[Pre-Chorus]` |
| **`(key change)`** | Провокація ШІ на тональну модуляцію (за Венсом Пауеллом) | Перед `[Mega-Chorus]` |
| **`(half-time feel)`** | Уповільнення ритмічного відчуття вокалу вдвічі (лікує скоромовку) | Швидкі куплети |
| **`(harmonized)`** / **`(layered harmonies)`** | Вимога увімкнути багатоголосся на ключовому слові хука | Кульмінаційні фрази приспіву |

---

## 4. 8 Готових структурних шаблонів за жанрами (з розвитком за Пауеллом та Breakdown)

### Шаблон 1: British Post-Punk / Darkwave
```text
[Vocal Intro - dynamic baritone acapella, dry]
(Порожній проспект ковтає ліхтарІ...)
[Beat Drop - driving chorus bassline, 80s drum machine]

[Verse 1 - rhythmic staccato, deadpan baritone]
Холодний дощ стікає по вікнІ,
Ми знОву чужІ у цьому дворІ,
(у цьому дворІ)
Де пам'ять згорАє на самому днІ.

[Pre-Chorus - rising snare roll, building tension]
(building intensity)
І крОки відлунюють в темну імлУ...

[Chorus - explosive, wide chorus guitars, wall of sound]
(belted)
Нічний трамвай іржАвим колесОм,
(layered harmonies)
ВезЕ мій сум за тЕмний горизОнт!

[Verse 2 - add driving tambourine, syncopated backing, sharp stereo guitars]
Сліди на асфАльті змивАє водА,
(луна стін)
І нІч непомІтно повз нАс пропливА.

[Chorus - wide stereo, high energy]
Нічний трамвай іржАвим колесОм,
ВезЕ мій сум за тЕмний горизОнт!

[Breakdown - vocal and bassline only, intimate, dry]
(whispered)
Лиш вікна, що світять в унісОн...

[Mega-Chorus - maximum energy, soaring layered harmonies, clashing guitars]
(key change)
(belted, powerful)
Нічний трамвай іржАвим колесОм,
(layered harmonies)
ВезЕ мій сум за тЕмний горизОнт!

[Outro - fading out, solo analog synth, tape hiss]
[End]
```

---

### Шаблон 2: Dark Synthwave / Cyberpunk EBM
```text
[Intro - atmospheric analog moog swell, vinyl crackle]
[Beat Drop - aggressive moog bass pulse, gated 80s snare]

[Verse 1 - monotone male recitative, dry close-mic]
ЕкрАни пульсують неОновим склом,
(холодний неОн)
МістО засинає під мЕртвим крилОм.

[Pre-Chorus - rising electronic arpeggios]
(building intensity)
СигнАли зникАють у мОрі датчИків...

[Chorus - explosive analog synth lead, wide stereo]
(belted)
Кібер-ніч розчинЯє моЮ тінь,
(layered harmonies)
Крізь дроти у безкІнечну глибИнь!

[Verse 2 - add driving electronic percussion, syncopated vocal chops]
Комп'ютерний шум заспокОює бІль,
(нуль і одИн)
І пам'ять стирАє останню з подІй.

[Chorus - full synthesizer energy]
Кібер-ніч розчинЯє моЮ тінь,
Крізь дроти у безкІнечну глибИнь!

[Breakdown - monotone vocal and sub-bass pulse only]
(whispered)
Тільки струм у змерзлих пальцях...

[Mega-Chorus - maximum synth wall of sound, heavy gated drums]
(layered harmonies)
(belted, powerful)
Кібер-ніч розчинЯє моЮ тінь,
Крізь дроти у безкІнечну глибИнь!

[Outro - pulsing synth decay, fast cutoff filter fade]
[End]
```

---

### Шаблон 3: Bristol Trip-Hop / Downtempo
```text
[Vocal Intro - breathy smoky female acapella, dry]
(Дим опускАється на мокрий брук...)
[Beat Drop - dusty vinyl breakbeat, warm rhodes, deep 808 sub]

[Verse 1 - intimate close-mic whisper, slow groove]
(whispered)
У шАфі холОдній сховАвся мій жАль,
(тихий жАль)
За склом пропливАє розмИта печАль.

[Chorus - soaring melodic vocal, smoky room reverb]
(falsetto)
Ооооой, не клич мене в темряву знОву,
(луна)
Залиш мені тІльки розмОву...

[Verse 2 - add organic shaker, vinyl crackle, subtle muted trumpet]
КраплІ водИ відбивають ліхтар,
І нІч розгортАє безмЕрний товАр.

[Chorus]
Ооооой, не клич мене в темряву знОву,
Залиш мені тІльки розмОву...

[Breakdown - vocal and warm rhodes only]
(whispered, intimate)
Лиш тИша між нами...

[Mega-Chorus - full vinyl warmth, layered vocal harmonies]
(layered harmonies)
Ооооой, не клич мене в темряву знОву,
Залиш мені тІльки розмОву!

[Outro - slow fading breakbeat, vinyl runout groove]
[End]
```

---

### Шаблон 4: Minimalist Dark Alt-Pop
```text
[Vocal Intro - solo close-mic ASMR breathy vocal]
(ЧУєш, як б'ється пульс...)
[Beat Drop - heavy 808 sub bass, organic foley snaps]

[Verse 1 - staccato whispers, intimate dry mix]
(whispered)
Тіні на стінах танцюють без слІв,
(без слів)
ХОлод кімнати розрІзав мій гнів.

[Pre-Chorus - rising foley clicks]
(building intensity)
Я рахую до трьох...

[Chorus - explosive wide open space, deep 808 glide]
(belted)
Оооох, ми згорАємо в цьОму вогнІ,
(layered harmonies)
Лиш попіл лишився мені!

[Verse 2 - add syncopated acoustic foley, vocal chops, stereo shaker]
Пальці торкАються мерзлого скла,
(холод скла)
Втрачена ніжність навік утеклА.

[Chorus]
Оооох, ми згорАємо в цьОму вогнІ,
Лиш попіл лишився мені!

[Breakdown - isolated breathy vocal and sub-bass swell only]
(whispered)
Нічого не бІйся...

[Mega-Chorus - maximum 808 power, multi-layered soaring vocal stack]
(key change)
(belted, powerful)
Оооох, ми згорАємо в цьОму вогнІ,
(layered harmonies)
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
(screamed)
ЗемлЯ розколОлась під нАшим тяжкИм крОком!
(тяжкИм крОком)
СтінА піднімАється перед сліпИм Оком!

[Pre-Chorus - rising clean vocal, building tempo]
(building intensity)
(falsetto)
І крізь темряву я бАчу світло...

[Chorus - epic soaring clean vocal, massive wall of sound]
(belted)
Ми піднІмемось знОву з руЇн і золИ,
(layered harmonies)
Хоч би як нас вітрИ не гнулИ!

[Verse 2 - add syncopated double-kick patterns, harsh scream backing]
(screamed)
Кров на камінні застИгла сталлю,
(сталлю!)
Ми не заплачемо перед печаллю!

[Chorus]
Ми піднІмемось знОву з руЇн і золИ,
Хоч би як нас вітрИ не гнулИ!

[Breakdown - massive half-time djent breakdown, brutal guttural screams, sub drop]
(screamed)
ЛАМАЙ! ЗНИЩУЙ КОРДОНИ!

[Mega-Chorus - ultimate climax, soaring clean vocal layered with harsh scream]
(key change)
(belted, powerful)
(layered harmonies)
Ми піднІмемось знОву з руЇн і золИ,
Хоч би як нас вітрИ не гнулИ!

[Outro - heavy fading djent guitar feedback, final abrupt snare cut]
[Cold End]
```

---

### Шаблон 6: Shoegaze / Dream Pop
```text
[Intro - shimmering reverb guitar swell, lush vintage chorus]
[Verse 1 - whispered breathy vocal, floating guitar textures]
(whispered)
ХмАри пливУть над сріблЯстим ліскОм,
(над ліскОм)
Вітер торкАється хвИль язикОм.

[Chorus - wall of sound guitars, soaring ethereal vocal]
(falsetto)
Ооооо-ааааа, засинає ріка у тумАні,
(layered harmonies)
Всі тривОги лишились в остогОні...

[Verse 2 - add jangly rhythm guitar, soft tambourine, stereo arpeggios]
ЗОрі випАли на мокру травУ,
(на травУ)
Я уві сні цим повітрям живУ.

[Chorus]
Ооооо-ааааа, засинає ріка у тумАні,
Всі тривОги лишились в остогОні...

[Breakdown - delicate whispered vocal and solo chorus guitar only]
(whispered, intimate)
Тільки спокій...

[Mega-Chorus - maximum reverb saturation, epic soaring harmonies]
(belted)
(layered harmonies)
Ооооо-ааааа, засинає ріка у тумАні,
Всі тривОги лишились в остогОні!

[Outro - slow ambient guitar decay, tape hiss fade]
[End]
```

---

### Шаблон 7: Melodic Techno / Electronica
```text
[Intro - hypnotic analog synth arpeggio, ambient filter swell]
[Beat Drop - four-on-the-floor kick, rolling sub-bass]

[Verse 1 - rhythmic spoken recitative, dry upfront]
Ритм у віскАх відрахОвує крОк,
(один-два)
Ніч розливАє густИй свій ковтОк.

[Pre-Chorus - rising snare roll, opening filter]
(building intensity)
Час зупинився...

[Chorus - euphoric melodic drop, wide vocal chops]
(layered harmonies)
Світло неОну у наших очах,
(у очах)
РозчинЯється темний наш страх!

[Verse 2 - add syncopated hi-hats, modular acid synth lead]
Шум автомагістралі звучить як струнА,
(як струнА)
Нас огортАє нічнА глибинА.

[Chorus]
Світло неОну у наших очах,
РозчинЯється темний наш страх!

[Breakdown - kick mute, atmospheric pad and vocal chops only]
(whispered)
Відчуй цей пульс...

[Mega-Chorus - full drop with rolling sub-bass and layered anthemic lead]
(ad-lib)
(layered harmonies)
Світло неОну у наших очах,
РозчинЯється темний наш страх!

[Outro - filtered synth arpeggio decay, four-bar kick fade]
[End]
```

---

### Шаблон 8: Contemporary Cinematic Ambient / Neoclassical
```text
[Intro - felt upright piano arpeggios, emotive cello drone]
[Verse 1 - intimate whispered female soprano, close-mic]
(whispered)
Сніг опадАє на стАрі дахИ,
(на дахИ)
Сплять у дібрОвах знеможені птахИ.

[Chorus - soaring emotive cello, rich hall space]
(falsetto)
Ооооой, збережи цю мовчАнку святу,
(луна)
Крізь негодУ й нічну самотУ...

[Verse 2 - add solo acoustic bandura plucking, warm string quartet]
Пам'ять торкАється білих сторІнок,
(білих сторІнок)
Сонце малює на склі візерунок.

[Chorus]
Ооооой, збережи цю мовчАнку святу,
Крізь негодУ й нічну самотУ...

[Breakdown - solo bandura and whispered vocal only]
(whispered, intimate)
Лиш тиша і світло...

[Mega-Chorus - full symphonic string swell, soaring expressive belting]
(belted, powerful)
(layered harmonies)
Ооооой, збережи цю мовчАнку святу,
Крізь негодУ й нічну самотУ!

[Outro - solo felt piano chord decay, ambient silence]
[Cold End]
```

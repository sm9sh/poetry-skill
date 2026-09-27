---
name: ukrainian-poetry-to-suno
description: "Turns Ukrainian poems, lyrics, song ideas, moods or references into ready-to-paste songs for Suno v6-mini (also v6 / v6-wild) and Google Flow Music (Lyria 3.5): adapts a poem into singable song form, marks tricky stresses, writes the Style / Exclude prompt and the tagged lyrics sheet. Use it whenever the user wants a song, track, Suno or Flow Music prompt, or says things like «зроби з цього вірша пісню», «пісня для суно», «текст пісні», «стиль для suno», «промпт для flow music», «хочу трек у стилі darkwave», even if they don't name the platform. Also covers fixing a generation (wrong stress, rushed vocals, sung instructions) and, on request, stem mixing, mastering and release."
---

# Ukrainian Poetry → Song (Suno v6-mini & Google Flow Music)

Цей скіл перетворює український вірш або ідею на пісню, яку можна одразу вставити в Suno чи Flow Music: лірику з розміткою, Style та Exclude. Основна ціль — **Suno v6-mini**. Для **Flow Music (Lyria 3.5)** вихід інший, див. нижче.

**Звучання — західний сучасний продакшн** (post-punk, darkwave, synthwave, trip-hop, alt-pop, shoegaze, indie rock, metalcore, melodic techno, cinematic ambient). Українська лірика звучить найсильніше, коли музика — рівня світового релізу, а не регіональної попси, шансону чи туристичного фольку (шароварщини). Модель тягне в цей бік, щойно бачить «українське», тож жанр, інструменти й Exclude мають її від цього відводити.

Якість тексту важить більше за промпт: слабку лірику не врятує жоден стиль. Якщо тексту ще немає, напиши його за скілом `ukrainian-poetry` — одразу в пісенній формі.

## Робочий процес

1. **Зрозумій запит.** Визнач:
   - платформу (за замовчуванням Suno v6-mini);
   - жанр і настрій, референс (опиши звук, без імен артистів);
   - чи є готовий вірш і чи можна його змінювати.
   Питай лише те, без чого не обійтися. Інше обери сам і коротко назви вибір.
2. **Лірика.**
   - **Є вірш** → адаптуй за `references/poem-to-song-adaptation.md`: режим «зберегти» чи «адаптувати», хук, пісенна форма, рівні рядки, співучі голосні. Це головний крок скіла; не пропускай його, навіть коли вірш гарний.
   - **Немає вірша** → напиши лірику за принципами `ukrainian-poetry`, одразу з куплетами, приспівом і хуком.
   - **Лексика — жива й зрозуміла на слух.** Без архаїзмів, діалектизмів, рідковживаних і вигаданих слів, якщо користувач прямо про них не просить. У пісні це ще важливіше, ніж у вірші: слухач не може перечитати рядок, а модель погано вимовляє незнайомі слова.
3. **Розмітка.** Секції та всі вказівки — у `[...]`, співаний бек-вокал — у `(...)` (див. нижче).
4. **Наголоси** — останнім проходом, лише три категорії.
5. **Промпт.** Для Suno — Style (англ. теги) + Exclude. Для Flow Music — промпт природною мовою.
6. **Обов'язкова перевірка перед видачею** — для кожної пісні, без винятків:
   1. Лірика проходить **Quality Checklist** зі скілу `ukrainian-poetry`: образність, щирість, ритм і звук, лаконічність, ракурс, форма, жива лексика, граматика, відповідність запиту. Пісенний виняток один: повтор хука й приспіву — прийом, а не «вода».
   2. Скрипт — виправ усі ERROR:
      ```bash
      python scripts/check_lyrics.py lyrics.txt --style "<style>" --exclude "<exclude>"
      ```
   3. Прочитай текст уголос у темпі пісні: рядок, який важко вимовити, модель теж зіпсує.
   Якщо будь-який пункт не пройдено — виправ і перевір знову. Користувач бачить лише результат, що пройшов перевірку.
7. **Видай результат** у форматі з розділу «Формат відповіді».

## Дужки: що співається, а що ні

Suno v6 і Flow Music **співають усе, що в круглих дужках**. Це найчастіша причина, чому у треку раптом звучить «half-time feel» чи «guitar solo».

| Синтаксис | Що робить модель | Приклади |
|---|---|---|
| `[Квадратні]` окремим рядком | Не співає: структура, інструменти, динаміка, **подача вокалу** | `[Verse 1 - intimate, dry close-mic]`, `[Chorus - open, soaring]`, `[Whispered]`, `[Belted]`, `[Falsetto]`, `[Key Change]`, `[Half-time feel]`, `[Breakdown - vocal and sub-bass only]`, `[End]` |
| `(Круглі)` | **Співає** як бек-вокал | `(ніколи знов)`, `(о-о-о)`, ехо останніх слів рядка |

Подачу можна вказати й у тезі секції: `[Verse 1 - whispered, half-time feel]`. Такий запис чистіший, ніж окремі рядки-теги.

## Наголоси для аудіомоделі

Велика літера на наголошеній голосній — **тільки в ліриці для Suno/Flow** (у звичайних віршах — знак наголосу ́ або нічого) і **тільки в трьох категоріях**:

1. **Омографи**: `зАмок / замОк`, `дорОга / дорогА`, `мУка / мукА`, `плАчу / плачУ`, `Орган / оргАн`.
2. **«Російські пастки»** — модель вимовляє по-російськи: `вИпадок`, `чорнОзем`, `листопАд`, `одИннадцять`, `фартУх`, `ненАвисть`, `новИй`, `вИрок`, `завдАння`.
3. **Неочевидні зсуви у формах**: `зЕмлю` (землЯ), `рУку` (рукА), `хОдиш` (ходИти), `несУ` (нестИ).

Решту слів не позначай — ні службових (*і, що, вже*), ні очевидних (*моя, земля, прийде, заспівай*). Надмаркування робить вокал ходульним і знецінює справжні позначки. У типовій пісні таких слів 0–5.

Поетичні / фольклорні варіанти наголосу — не більше двох на пісню, лише з названим джерелом і великою літерою (деталі — в `ukrainian-poetry`).

## Style для Suno v6-mini

- **80–200 символів, англійською, найважливіше — першим.** v6 найсильніше зважає на перші теги, тож порядок такий: жанр → настрій → вокал → 2–3 інструменти → продакшн → BPM.
- **Вокал описуй трьома шарами:** характер (`raspy male baritone`), подача (`intimate close-mic`), простір/обробка (`dry upfront, tape slap delay`). Без цього v6-mini дає «стерильний» усереднений голос.
- **Жодних заперечень у Style** (`no drums` модель читає як «drums»). Пиши позитивну конкретику (`solo piano, sparse`), а небажане — в **Exclude**.
- **Жодних імен артистів і назв пісень** — описуй звук.
- **Variety = Off**, якщо промпт вивірений. На інших рівнях Suno сам переписує Style. Для пошуку ідей радь Normal або High.
- Базовий Exclude проти «регіональної попси»: `cheesy regional pop, schlager, wedding brass, accordion, generic euro-pop, heavy autotune`. Додай специфічне для жанру.

Готові жанрові формули: `references/mood-to-style-map.md` і `references/reference-to-style-cheatsheet.md`. Короткий орієнтир:

| Жанр | Стартова формула Style |
|---|---|
| Post-punk / darkwave | `british post-punk, darkwave, melancholic baritone male vocal, chorus electric guitar, driving bassline, 80s drum machine, lo-fi, 128 bpm` |
| Dark synthwave | `dark synthwave, monotone male vocal, analog moog bass pulse, gated snare, crisp arpeggios, nocturnal, 120 bpm` |
| Trip-hop | `trip-hop, downtempo, breathy female vocal, dusty vinyl breakbeat, warm rhodes, deep sub bass, cinematic, 85 bpm` |
| Minimalist alt-pop | `minimalist alt-pop, dark, close-mic breathy female vocal, heavy 808 sub, organic foley percussion, 100 bpm` |
| Shoegaze / dream pop | `shoegaze, dream pop, whispered breathy vocal, wall of reverb guitars, lush chorus, slow groove, 90 bpm` |
| Metalcore | `modern progressive metalcore, screamed and clean male vocals, drop-tuned djent riffs, punchy drums, 150 bpm` |
| Melodic techno | `melodic techno, hypnotic, airy vocal chops, analog arpeggios, rolling sub bass, four-on-the-floor, 124 bpm` |
| Cinematic ambient | `cinematic ambient, neoclassical, intimate whispered vocal, felt piano, soaring cello, tape warmth, 70 bpm` |

## Flow Music (Lyria 3.5)

- **Промпт — природною мовою**, 2–4 речення: концепт і жанр → атмосфера (без імен артистів) → інструменти → динаміка й вокал, плюс тривалість.
- **Треки до ~3 хв.** Структура компактніша, ніж для Suno: V1 → C → V2 → C → Bridge → C.
- Лірику з тими ж `[секціями]` вставляй у поле тексту. Правило круглих дужок те саме.
- Проблемну секцію виправляй через Replace, а не перегенеруй весь трек.

Деталі й ліміти обох платформ (а також статус Udio) — у `references/platforms.md`, перевіряй там, перш ніж щось обіцяти.

## Контроль якості пісні (Gates 1–6)

| Gate | Що перевірити | Як виправити |
|---|---|---|
| 1. Перші 5 секунд | Голос або впізнаваний хук одразу, без довгого інструментального вступу | `[Intro]` коротким або почати з `[Vocal Intro - dry acapella]` |
| 2. Приспів до ~50 с | До першого приспіву не більше 8–12 співаних рядків | Скоротити V1, прибрати Pre-Chorus |
| 3. Просодія й наголоси | Рядки однакової довжини, текст читається вголос природно, наголоси позначено за трьома категоріями | Вирівняти склади; виправити секцію редагуванням у Suno / Replace у Flow |
| 4. Контраст | Куплет — стакато й близько, приспів — легато й широко | `[Chorus - open, soaring]`, відкриті голосні на довгих нотах |
| 5. Розвиток V2 | Другий куплет додає новий шар аранжування | `[Verse 2 - add brushed drums, backing vocals]` |
| 6. Кульмінація | Спад енергії (бридж / брейкдаун) перед фінальним приспівом | `[Bridge - stripped back]` → `[Final Chorus - full band, layered harmonies]` |

Gates 7–10 (зведення, мастеринг, реклама) — у `references/post-production.md`. Відкривай його лише на прохання користувача.

## Типові проблеми після генерації

| Симптом | Причина | Що робити |
|---|---|---|
| Вокал тараторить | Довгі рядки, забагато тексту (>3000 символів), швидкий BPM | Рядки по 4–8 слів, `[Half-time feel]` у тезі секції, повільніший BPM |
| Модель проспівала вказівку | Вказівка в `( )` | Перенести в `[ ]` |
| Неправильний наголос | Слово з трьох категорій без позначки, або надмаркування навколо | Позначити лише це слово й перегенерувати секцію (редагування секції / Replace) |
| Звучить як регіональна попса | Слабкий жанровий якір, немає Exclude, «ukrainian» першим тегом | Західний жанр першим; Exclude; прибрати «ukrainian folk», якщо фольк не потрібен |
| Style «поплив» від генерації до генерації | Variety вище Off | Variety = Off |
| Приспів не повторюється як треба | Приспів у тексті різний або немає тегу `[Chorus]` | Повторити приспів дослівно з тим самим тегом |

## Формат відповіді

Давай блоки, які можна скопіювати й вставити. Не пропонуй два Style на вибір — обери один.

**Suno v6-mini:**

````markdown
**Style** (Variety: Off)
```
<80–200 символів англійських тегів>
```

**Exclude**
```
<небажане>
```

**Lyrics**
```
[Intro - ...]

[Verse 1 - ...]
...

[Chorus - ...]
...
```
````

**Flow Music:** блок **Prompt** (2–4 речення природною мовою) + блок **Lyrics**.

Після блоків додай 1–3 рядки: що змінено у вірші й чому (якщо адаптував) і що підкрутити, якщо перша генерація не влучить. Без довгих лекцій про теорію — лише якщо користувач просить.

## Довідники

| Коли | Файл |
|---|---|
| Адаптуєш вірш під пісню (завжди, коли є вихідний вірш) | `references/poem-to-song-adaptation.md` |
| Потрібні ліміти, функції, статус платформ | `references/platforms.md` |
| Підбір жанру під настрій | `references/mood-to-style-map.md` |
| Користувач назвав артиста чи трек як референс | `references/reference-to-style-cheatsheet.md`, `references/reference-breakdown-examples.md` |
| Структури пісень і каталог метатегів | `references/song-structure-pack.md` |
| Шаблони лірики | `references/lyrics-to-suno-template.md` |
| Готові промпт-паки за настроєм / вокалом | `references/packs/README.md` |
| Українські пісенні сценарії (весілля, колискова, гімн, військова тощо) | `references/ukrainian-song-scenarios.md` |
| Типові помилки й антипатерни | `references/suno-prompt-anti-patterns.md` |
| Оцінювання (100-бальна рубрика) | `references/rubric.md` |
| Зведення, мастеринг, реліз — лише на запит | `references/post-production.md` |
| Розширена теорія (шестикроковий цикл, Melodic Math) | `references/full-guide.md` |
| Механічна перевірка лірики та Style | `scripts/check_lyrics.py` |

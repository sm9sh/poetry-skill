# Original User Request

## 2026-08-28T11:38:57Z

<USER_REQUEST>
# Teamwork Project Prompt

Створити та інтегрувати 5 спеціалізованих сабагентів та 6 фундаментальних принципів поетичної майстерності у систему навичок (skills), посібники, валідатори та тести репозиторію `poetry-skill`.

Working directory: `d:\poetry-skill`
Integrity mode: development

## Requirements

### R1. Інтеграція 6 поетичних прийомів у навички проекту (Skill Integration)
- Оновити `skills/ukrainian-poetry/SKILL.md`, `skills/ukrainian-poetry/references/full-guide.md`, `skills/ukrainian-poetry/references/rubric.md`, `skills/poetry-skill/SKILL.md` та `AGENTS.md`.
- Зафіксувати 6 принципів як обов'язкові стандарти якості:
  1. **Свіжа образність та метафоричність**: відмова від затертих штампів ("кров-любов", "троянди-сльози"), авторські несподівані порівняння, "показ через дію/деталь" замість декларування почуттів.
  2. **Емоційна глибина та щирість**: нуль штучного пафосу, театральності й менторського моралізаторства; тонка емпатія через побутові та психологічні деталі.
  3. **Ритмічна та звукова гармонія**: дихання вірша (як у силабо-тоніці, так і у верлібрі), багата нетривіальна рима, фоніка (асонанси, алітерації, звукопис).
  4. **Лаконічність і вага слова**: максимальне смислове стиснення, відсутність зайвих займенників/"води" заради розміру, заборона штучних синтаксичних інверсій заради рими.
  5. **Оригінальність ракурсу**: унікальний авторський кут зору на вічні теми, парадоксальні фінали, перенесення фокусу з макроявищ на мікродеталі.
  6. **Органічна єдність форми та змісту**: зовнішня форма (ритм, строфіка, паузи, рваність чи плавність) бездоганно відповідає емоційному стану та темі.

### R2. Створення 5 спеціалізованих сабагентів (5 Subagent Personas)
Створити системні промпти, конфігурації та специфікації для 5 сабагентів (у `skills/ukrainian-poetry/agents/` та реєстрах системи):
1. `poetry-imagery-architect` (**Образотворець**): спеціалізується на свіжій образності, сенсорній тактильності, виявленні та усуненні кліше і штампів.
2. `poetry-emotional-critic` (**Критик щирості**): аудит емоційної глибини, відсікання фальшивого пафосу, моралізаторства і театральщини.
3. `poetry-prosody-phonics` (**Майстер фоніки та просодії**): контроль метрики, наголосів (усунення русизмів/помилок), милозвучності (у/в, і/й), алітерацій, асонансів та різнорідних рим.
4. `poetry-conciseness-editor` (**Редактор лаконічності**): очищення тексту від "води", зайвих службових слів, виправлення штучних інверсій та збереження природного синтаксису.
5. `poetry-form-synthesizer` (**Архітектор форми та ракурсу**): контроль органічної єдності форми/змісту, створення нетривіального ракурсу і парадоксальних фіналів, фінальна збірка твору.

### R3. Інтеграція в систему тестування та валідатор (Validation & Rubric)
- Оновити 100-бальну шкалу оцінювання `rubric.md` та логіку в `tests/validator/poetic_validator.py` / `tests/validator/rubric_scorer.py`, щоб враховувати нові критерії (штучні інверсії, сенсорні деталі, зайві займенники-заповнювачі).
- Додати нові тестові сценарії або оновити існуючі тест-кейси для перевірки роботи нових критеріїв.
- Зберегти 100% сумісність з існуючим модулем `ukrainian-poetry-to-suno`.

## Acceptance Criteria

### Документація та навички
- [ ] Усі 6 принципів детально розписані з практичними правилами, прикладами та антипатернами в `skills/ukrainian-poetry/SKILL.md` та `references/full-guide.md`.
- [ ] Оновлено `AGENTS.md` та `skills/poetry-skill/SKILL.md` з новими директивами.

### Сабагенти
- [ ] Створено 5 файлів конфігурацій/промптів сабагентів у `skills/ukrainian-poetry/agents/` з чіткими контрактами (роль, задачі, правила валідації, формат входу/виходу).
- [ ] Зареєстровано сабагентів у системі та описано їхню спільну конвеєрну взаємодію (Pipeline).

### Тести та валідація
- [ ] Тестовий набір `py -3 tests/run_tests.py --all` виконується успішно (59+ тестів, 0 помилок).
- [ ] Середній бал поетичної рубрики залишається >= 95/100.

</USER_REQUEST>

## 2026-08-29T19:16:28Z

<USER_REQUEST>
# Teamwork Project Prompt

Інтегрувати повномасштабну специфікацію «AI Music Alchemy & Prompt Engineer (Suno / Udio / Flow Music)» v8 (файл `d:\poetry-skill\ai-music-generation-meta-spec-v8.md`) у навички, референси, архітектуру промптів, валідатори та тести екосистеми `poetry-skill`, забезпечивши безшовну взаємодію з модулем української поезії, підтримку Suno v4.5/v5.5, Udio v4 та Google Flow Music (Lyria 3.5), інженерне DAW-зведення, мастеринг без True Peak пастки та 10 AI Quality Gates. Після виконання завдання створити 3 незалежних агентів-аудиторів для суворої перевірки на відсутність помилок, суперечностей або регресій.

Working directory: `d:\poetry-skill`
Integrity mode: development

## Requirements

### R1. Оновлення та розширення навичок екосистеми (Skill Architecture & Guides)
- Оновити `skills/ukrainian-poetry-to-suno/SKILL.md`, `skills/ukrainian-poetry-to-suno/references/full-guide.md`, `skills/poetry-skill/SKILL.md`, `AGENTS.md` та `GEMINI.md`.
- Оновити кореневі симетричні файли: `ukrainian-poetry-to-suno.md`, `ukrainian-poetry-skill.md`, `lyrics-to-suno-template.md`, `song-structure-pack.md`, `suno-prompt-anti-patterns.md`.
- Інтегрувати 6-етапний повний цикл:
  1. Step 1: Deep Reference Reverse Engineering (Genre hybrid, BPM, Key, Sonic aesthetic/timbre, Vocal Triple-Stack [Character+Delivery+FX], Melodic Math hooks, Bracketed layout).
  2. Step 2: AI-Optimized Lyrics Writing (Syllable symmetry, Spoken Prosody Test, Staccato vs Legato spatial contrast, 5-Second Rule, 50-Second Chorus Rule, Melodic Previews, Glue Hooks, Cognitive melody limits <=3-4).
  3. Step 3: Multi-Platform Prompt Engineering:
     - **Suno v4.5 / v5.5**: Метод 1 (Conversational Paragraph із правилом «First 5 Words») та Метод 2 (Tag-Based Matrix за формулою HookGenius 5 модулів), нові системні фічі (My Taste, Voices cloning, Custom Models), усунення Failure Modes (Lyrics Rushing, Sterile Vocals, The Negation Trap), комерційні ліцензії (Pro/Premier).
     - **Udio v4**: 48 кГц якість, керування Context Length (10-15с для переходів vs максимум для спадковості), Inpainting синтаксис `*stars*`, комерційні права на Pro.
     - **Google Flow Music (Lyria 3.5)**: Conversational Agent Mode, Spaces, Turntable, Section-level replace editing, AI Cover, синхронізація Gemini Omni Flash для музичних кліпів, 500 кредитів щодня + комерційні ліцензії (MusicFX закрито 31 липня 2026).
  4. Step 4: Step-by-Step Extensions Roadmap (The AI Conductor: Seed 30-50s, Extend, Vance Powell Verse 2 development з додаванням tambourine/shaker/backing vocals, Breakdown & Mega-Chorus, лаконічне Outro <=20s).
  5. Step 5: Engineering DAW Post-Production & Stem Mixing (Stem splitting [Moises, RipX, LALAL.AI], фазова оптимізація бочки/басу, хірургічне частотне розмаскування через динамічний сайдчейн, Split Compression басу [<200Hz brickwall sub vs >200Hz dynamic saturated], паралельна сатурація Тчада Блейка безпосередньо на Master Fader [минаючи Drum Bus для збереження headroom], динамічний Mid-Side Reverb sidechaining вокалу).
  6. Step 6: Mastering & Algorithmic Streaming Distribution (Мастеринг без True Peak пастки: -1 dBTP для гучних майстрів -6...-8 LUFS з вимкненням TP-лімітування, або -14 LUFS для -2 dBTP; гнучкі жанрові пороги Skip Rate [Поп >48%, Хіп-хоп >44%, Електроніка >37%, Інді-рок >31%, тривога >45%]; ліквідація пастки Playlist Placement Trap [спрямування реклами виключно на цільовий сингл, а не на плейлист артиста]; Spotify Canvas, Marquee, Discovery Mode).

### R2. Розширення бібліотеки метатегів, правил просодії та 10 AI Quality Gates
- Оновити `song-structure-pack.md`, `lyrics-to-suno-template.md`, `suno-prompt-anti-patterns.md`.
- Додати інлайн вокальні жести в круглих дужках: `(whispered)`, `(belted)`, `(falsetto)`, `(screamed)`, `(ad-lib)`, `(building intensity)`, `(key change)`, `(half-time feel)`, `(harmonized)`.
- Додати повну таблицю 10 гейтів контролю якості (Gate 1: Anti-Skip 5s, Gate 2: 50s Rule, Gate 3: Spoken Prosody, Gate 4: Staccato vs Legato, Gate 5: Verse 2 development за Пауеллом, Gate 6: Breakdown & Mega-Chorus, Gate 7: Low end Split Compression, Gate 8: Tchad Blake drum distortion routing to Master, Gate 9: Mastering True Peak, Gate 10: Single-only Ads).

### R3. Синхронізація валідаторів, тестів та збереження сумісності
- Оновити валідатори `tests/validator/metatag_validator.py`, `tests/validator/suno_validator.py` та `tests/validator/poetic_validator.py` за потреби для підтримки нових тегів (`[Vocal Intro]`, `[Beat Drop]`, `[Post-Chorus]`, `[Mega-Chorus]`, `[Breakdown]`, інлайн-жестів та лімітів).
- Зберегти 100% сумісність з 6 принципами української поезії, правилом великих літер у наголосах (`вИпадок`, `дорОга`), правилом квадратних дужок `[...]` для аранжувань та ізоляцією круглих дужок `(...)` під вокальні партії/бек-вокал.
- Забезпечити повне проходження тестів `py -3 tests/run_tests.py --all` (100% успішних тестів, 0 помилок).
- Синхронізувати оновлені файли в `.agents/skills/` та глобальний каталог `C:\Users\sm9sh\.gemini\config\plugins\poetry-skill\`.

### R4. Верифікаційний аудит трьома спеціалізованими агентами (Post-Implementation 3-Agent Audit)
Після завершення інтеграції та виконання тестів виконати аудит трьома спеціалізованими ролями:
1. **Agent 1: Prompt & Platform Spec Auditor (Аудитор платформних промптів)** — перевірити повноту правил Suno v4.5/v5.5 (Conversational & Tag-Based), Udio v4 (Context Length, Inpainting), Google Flow Music (Lyria 3.5, Spaces, Turntable, Omni Flash), лімітів символів, токенів та цілісності метатегів.
2. **Agent 2: Audio Engineering & Distribution Auditor (Аудитор аудіоінженерії та мастерингу)** — перевірити коректність DAW-стем зведення (Split Compression, фазова оптимізація, паралельний дисторшн Тчада Блейка на майстер, Mid-Side сайдчейн), усунення True Peak пастки, жанрових порогів Skip Rate та відсутності суперечностей у Quality Gates.
3. **Agent 3: Ukrainian Poetry & Cross-System Integrity Auditor (Аудитор поетичної та системної інтеграції)** — перевірити збереження 6 принципів поетичної майстерності, коректності наголосів великими літерами, правила дужок `[...]` vs `(...)`, відсутності суперечностей або регресій в існуючих модулях та автотестах.

## Acceptance Criteria
- [ ] Повний цикл з 6 кроків, 10 AI Quality Gates та специфікації Suno v4.5/v5.5, Udio v4, Flow Music Lyria 3.5 інтегровані в `SKILL.md` та `references/full-guide.md`.
- [ ] Оновлено `AGENTS.md`, `GEMINI.md`, шаблони `lyrics-to-suno-template.md`, `song-structure-pack.md`, `suno-prompt-anti-patterns.md`.
- [ ] `py -3 tests/run_tests.py --all` виконується з кодом 0 (100% успішних тестів, 0 помилок).
- [ ] Зміни синхронізовано в `C:\Users\sm9sh\.gemini\config\plugins\poetry-skill\`.
- [ ] Звіт 3 аудиторів підтверджує повну відсутність конфліктів, помилок і суперечностей.

</USER_REQUEST>

## 2026-09-06T09:42:47Z

<USER_REQUEST>
Завершити реалізацію залишкових завдань екосистеми poetry-skill: очистити корінь репозиторію від файлів-дзеркал з оновленням скрипта синхронізації, створити субагента Poetry QA Bot, додати наскрізний пайплайн (End-to-End Song Bridge) у головний оркестратор та створити бібліотеку прикладів (Playground) із кейсами успіху та розбором типових помилок.

Working directory: d:\poetry-skill
Integrity mode: development

## Requirements

### R1. Очищення кореня та оновлення синхронізації (Root Cleanup & Sync Refactoring)
- Видалити 16 надлишкових файлів-дзеркал із кореневої директорії репозиторію (`ukrainian-poetry-skill.md`, `ukrainian-poetry-to-suno.md`, `lyrics-to-suno-template.md`, `song-structure-pack.md`, `suno-prompt-anti-patterns.md`, `prompt-builder.md`, `reference-to-style-cheatsheet.md`, `mood-to-style-map.md`, `suno-style-rubric.md`, `reference-breakdown-examples.md`, `ukrainian-song-scenarios.md`, `suno-prompt-tests.md`, `ukrainian-poetry-skill-rubric.md`, `ukrainian-poetry-skill-input-template.md`, `ukrainian-poetry-skill-stress-pack.md`, `ukrainian-poetry-skill-tests.md` та кореневу папку `packs/`).
- Оновити `tests/sync_ecosystem.py`: видалити логіку копіювання файлів у корінь; скрипт повинен синхронізувати виключно канонічні скіли між `skills/`, `.agents/skills/` та глобальним плагіном Gemini.
- Перемістити або синхронізувати `ukrainian-poetry-skill-uk.md` та `ukrainian-poetry-skill-lite.md` у відповідні папки `docs/` або `references/`, щоб у корені не залишалося неконтрольованих розрізнених гайдів.
- Перевірити всі посилання у `README.md`, `README.en.md`, `HOWTO.md` та документації — вони повинні вказувати на шляхи всередині `.agents/skills/` або `skills/`, без посилань на видалені кореневі дзеркала.

### R2. Агент контролю якості Poetry QA Bot
- Створити файл специфікації субагента `poetry-qa-bot.md` у `skills/ukrainian-poetry/agents/` та `.agents/skills/ukrainian-poetry/agents/`.
- Зареєструвати агента у `skills/ukrainian-poetry/agents/openai.yaml` та `.agents/skills/ukrainian-poetry/agents/openai.yaml`.
- Агент повинен діяти як автономний аудитор: приймати віршований текст, сканувати його на відповідність 6 принципам майстерності, застосовувати 100-бальну матрицю штрафів з `rubric.md` та повертати деталізований скоринг-звіт із балами по кожному критерію і конкретними покроковими рекомендаціями щодо покращення.

### R3. Наскрізний пайплайн створення пісні (End-to-End Song Creation Bridge)
- Оновити головний оркестратор `skills/poetry-skill/SKILL.md` та `.agents/skills/poetry-skill/SKILL.md`, додавши розділ `## End-to-End Song Creation Pipeline`.
- Задокументувати повний єдиний протокол: «Ідея / тема → генерація вірша (ukrainian-poetry) → аудит якості (poetry-qa-bot) → адаптація лірики та Spoken Prosody Test (music-lyrics-architect) → вибір платформи та синтез промптів (music-prompt-synthesizer: Suno / Udio / Flow Music) → перевірка 10 AI Quality Gates → рекомендації DAW-зведення (music-daw-mastering-critic)».

### R4. Бібліотека прикладів та розбору помилок (Prompt Playground)
- Створити каталог `examples/` із підкаталогами `examples/success/` та `examples/failures/`.
- `examples/success/` має містити щонайменше 3 готові наскрізні сценарії для різних платформ:
  1. Darkwave / Post-Punk трек для Suno v4.5/v5.5 (вірш з акцентуацією + промпт + ексклюди).
  2. Trip-Hop трек для Udio v4 (текст + промпт 250 симв. + розмітка Inpainting `*stars*` + Context Length).
  3. Cinematic Ambient трек для Google Flow Music Lyria 3.5 (діалоговий промпт агента + опис простору).
- `examples/failures/` має містити розбір типових помилок та інструкції з виправлення:
  1. `lyrics-rushing-fix.md`: проблема вокальної скоромовки та її вирішення через `(half-time feel)` і ліміти 4–8 слів/рядок.
  2. `robotic-vocals-fix.md`: усунення пластикового вокалу через вокальний Triple-Stack.
  3. `true-peak-clipping-fix.md`: запобігання міжсемпловому спотворенню на стрімінгах.

## Acceptance Criteria

### Цілісність кодової бази та тести
- [ ] Виконання `py -3 tests/run_tests.py --all` завершується кодом 0, 100% тестів пройдено (75+ тестів), відсутні помилки імпорту чи відсутніх файлів.
- [ ] Виконання `py -3 tests/sync_ecosystem.py` не створює нових файлів-дзеркал у кореневій директорії репозиторію.
- [ ] У корені репозиторію відсутні старі 16 файлів-дублікатів та папка `packs/`.

### Нові компоненти та функціонал
- [ ] Створено та зареєстровано `poetry-qa-bot.md` з повною структурою специфікації (Role, Boundaries, Contracts, Heuristics, Output, Edge cases).
- [ ] У `poetry-skill/SKILL.md` повністю розписано протокол `End-to-End Song Creation Pipeline`.
- [ ] У каталозі `examples/` створено щонайменше 3 робочі кейси в `success/` та 3 інструкції з діагностики в `failures/`.
- [ ] Усі внутрішні посилання в оновленій документації ведуть на дійсні файли без 404/dead links.
</USER_REQUEST>

# HOWTO: Практичний посібник з використання екосистеми

Цей посібник описує повні робочі процеси для написання поезії, перетворення її на музичні промпти для **Suno AI**, оцінювання за 100-бальною рубрикою та запуску автоматизованих E2E-тестів.

---

## 1. Робочий процес 1: Написання автентичного вірша

### Крок 1. Вибір скіла
- **Канонічний варіант для агентів**: `skills/ukrainian-poetry/`
- **Автономний посібник**: `ukrainian-poetry-skill.md` (або `ukrainian-poetry-skill-uk.md` українською, чи `ukrainian-poetry-skill-lite.md` для швидких запусків)

### Крок 2. Формування запиту
Використовуй параметри з `ukrainian-poetry-skill-input-template.md`:
```text
topic: Нічне місто під час тривоги, світло у вікнах
form: sonnet
meter: iamb
rhyme: heterogeneous
clausula: alternating-fm (ЖЧЖЧ)
register: contemporary-urban
```

### Крок 3. Перевірка якості
1. **Наголос**: Перевір слова на відповідність літературній нормі (*вИпадок*, *чорнОзем*, *новИй*, *одИннадцять*).
2. **Рима**: Переконайся у відсутності дієслівних пар (*знати-любити*) та штампів (*любов-кров*).
3. **Антишароварщина**: Переконайся у відсутності бутафорських штампів (*шаровари, гопак*).

---

## 2. Робочий процес 2: Створення музичного промпту для Suno AI

### Крок 1. Вибір скіла
- **Канонічний варіант**: `skills/ukrainian-poetry-to-suno/`
- **Швидкий конструктор**: `prompt-builder.md`

### Крок 2. Побудова поля Style of Music (80–180 символів)
Застосовуй формулу з 6 блоків англійською мовою з українськими культурними якорями:
`[Жанр] + [Темп/BPM] + [Вокал] + [Інструменти] + [Продакшн] + [Динаміка]`

*Приклад*:
`ukrainian post-punk, coldwave, 130 bpm, monotone male baritone, melodic chorus bass, jangly reverb guitar, analog drum machine` (127 символів)

### Крок 3. Оформлення тексту з метатегами
Розміщуй український текст пісні у полі `Lyrics`, використовуючи квадратні дужки для структури та круглі для бек-вокалу:
```text
[Intro]
[Instrumental: melodic bassline]

[Verse 1]
У темнім склі тремтить моє безсонне відбиття...
(тиша навколо)

[Chorus]
Горить вогонь, і ніч стискає коло...

[Outro]
[Fade Out]
[End]
```

### Крок 4. Заповнення поля Exclude (Negative Prompt)
Додай антиартефактні вектори з `suno-prompt-anti-patterns.md`:
```text
metallic highs, harsh sibilance, piercing treble, muddy bass, boomy low-end, garbled vocals, excessive reverb wash, cheesy synth brass
```

---

## 3. Робочий процес 3: Робота з музичними референсами

Якщо користувач дає ім'я виконавця чи назву треку:
1. Відкрий `reference-to-style-cheatsheet.md` та `reference-breakdown-examples.md`.
2. Вилучи згадки імен, назв та брендів.
3. Переклади звучання на мову 8 українських жанрів (наприклад, SadSvit -> *ukrainian post-punk, doomer coldwave*, DakhaBrakha -> *ukrainian ethno-chaos, avant-folk*).

---

## 4. Робочий процес 4: 100-бальне оцінювання (Рубрики)

- **Для поезії**: Використовуй `ukrainian-poetry-skill-rubric.md` (7 критеріїв: наголос і милозвучність, ритміка і метр, рима і строфіка, образна тканина, регістр, антишароварщина, форма).
- **Для Suno**: Використовуй `suno-style-rubric.md` (8 критеріїв: токен-економіка 80–180 симв., чистота полів без витоку метаданих, англійська термінологія, акустичні якорі, метатеги, Exclude-вектор, жанровий баланс, відсутність прямих імен).

---

## 5. Робочий процес 5: Запуск автоматизованого тестування

Запусти майстер-раннер тестів для перевірки всіх компонентів:
```powershell
# Повний запуск усіх 59 тестів (Tiers 1–4)
py -3 tests/run_tests.py --all

# Запуск окремого рівня
py -3 tests/run_tests.py --tier 1
py -3 tests/run_tests.py --tier 2
py -3 tests/run_tests.py --tier 3
py -3 tests/run_tests.py --tier 4

# Генерація звіту у форматі JSON
py -3 tests/run_tests.py --all --json --report-file tests/reports/test_report.json
```

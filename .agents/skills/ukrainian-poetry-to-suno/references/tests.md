# Suno AI Prompt Engineering Test Suite

Комплексний набір тестових сценаріїв для валідації модуля `ukrainian-poetry-to-suno`.

---

## Частина 1: Стандартні функціональні тести

### 1. Перетворення теми в Custom Mode
```text
Згенеруй повну Suno Custom Mode конфігурацію для сучасної української пісні.
Тема: нічний трамвай і дощовий асфальт у Києві.
Настрій: меланхолійний, теплий, спокійний.
```
*Критерій проходження*:
- `Style of music` містить 80–180 символів, англійські токени (`indie pop, nocturnal city atmosphere, 110 bpm...`) — жанр першим, без «ukrainian» як першого тегу.
- Відсутні службові поля `Language:` та `Theme:` у полі стилю.
- `Lyrics` містить українські рядки з метатегами `[Intro]`, `[Verse]`, `[Chorus]`, `[Outro]`.
- `Exclude` містить анти-артефакти та анти-кліше.

---

### 2. Перетворення готового українського вірша
```text
На основі цього вірша створи блоки Custom Mode для стилю Post-Punk / Doomer Wave:

Порожній проспект ковтає ліхтарі,
Холодний дощ стікає по вікні.
Ми знову чужі у цьому дворі,
Де пам'ять згорає на самому дні.
```
*Критерій проходження*:
- `Style of music` відповідає архетипу SadSvit (`ukrainian post-punk, doomer wave, 130 bpm...`).
- Вірш розмічено квадратними дужками секцій та круглими дужками бек-вокалу `(у цьому дворі)`.

---

### 3. Стриманий патріотичний трек без шароварщини та пафосу
```text
Створи Suno prompt для пісні про пам'ять полеглих воїнів та землю.
Суворо без лозунгів, без плакатного пафосу, без весільного акордеона.
```
*Критерій проходження*:
- Стиль: `contemporary ukrainian neoclassical` або `restrained acoustic folk`.
- `Exclude` містить: `cheesy synth brass, tourist polka accordion, bombastic anthem climax, propaganda slogans`.

---

### 4. Деперсоналізація музичного референса
```text
У мене є референс: DakhaBrakha - "Шо з-під дуба".
Потрібно повернути:
1. Reference breakdown
2. Safe style prompt (без імен та назв треків)
3. Custom Mode Lyrics setup
4. Exclude vector
```
*Критерій проходження*:
- У фінальному `Style of music` повністю відсутні слова "DakhaBrakha", "Dakh Daughters", "in the style of".
- Виділено стиль: `ukrainian ethno-chaos, avant-folk, white voice female chanting, cello drone...`.

---

## Частина 2: Стрес-тести та граничні випадки (Edge Cases)

### 5. Тест екстремального темпу (160+ BPM Ska-Punk / Fast Drill)
```text
Створи Suno prompt для високошвидкісного бойового треку з живою духовою секцією та хрипким речитативом у темпі 160 BPM.
```
*Критерій перевірки*:
- Наявність чіткого темпового маркера `160 bpm` на початку або середині промпта.
- Жанрові дескриптори: `ukrainian ska-punk, fast energetic brass section, driving live drums, raspy male vocal`.
- Структура містить швидкі переходи `[Intro]`, `[Verse]`, `[Trumpet Solo]`, `[Outro]`.

---

### 6. Тест надповільного темпу (65–75 BPM Neoclassical Lament)
```text
Створи Suno prompt для жалобного похоронного голосіння або інтимної неокласики під соло бандури у темпі 70 BPM.
```
*Критерій перевірки*:
- Темповий маркер: `70 bpm` або `75 bpm`.
- Вокал: `solo sorrowful female white voice` або `intimate breathy female vocal`.
- `Exclude` пригнічує гудіння низьких частот: `boomy low-end, distorted sub-bass, metallic highs`.

---

### 7. Тест гібридного схрещування непоєднуваних жанрів
```text
Згенеруй стиль для незвичного гібриду: український прогресивний джент-металкор з автентичними етно-цимбалами та чергуванням жіночого гроулу й чистого сопрано.
```
*Критерій перевірки*:
- Стиль: `ukrainian progressive metalcore, djent riffs, tsymbaly folk intro, brutal guttural scream alternating ethereal clean female vocal, heavy drop, 150 bpm`.
- Довжина стилю суворо в межах 80–180 символів.
- Розмітка тексту містить `[Brutal Guttural Growl]` у куплетах і `[Clean Female Vocal]` у приспіві.

---

### 8. Тест динамічного дропу та контрастних секцій
```text
Створи аранжування з різким контрастом: тихий акустичний вступ на віолончелі -> повільне наростання білого голосу -> вибуховий брейкдаун з важкими барабанами.
```
*Критерій перевірки*:
- Текст містить метатеги `[Cello Drone Intro]`, `[White Voice Choir]`, `[Dynamic: Crescendo]`, `[Tribal Percussion Drop]`, `[Climax Chorus]`.
- Відсутність старих ASCII-стрілок `->`.

---

### 9. Валідація ліміту символів (Strict Character Budget Audit)
```text
Перевір, що кожен із згенерованих Style of music промптів для 8-ми базових українських жанрів вміщується у діапазон від 80 до 180 символів:
1. Ethno-Chaos
2. Post-Punk
3. Dark Synth
4. Trap-Folk
5. Metalcore
6. Shoegaze
7. Ethno-Rock
8. Neoclassical Bandura
```
*Критерій перевірки*:
- Довжина кожного рядка `len(style_prompt)` строго: `80 <= len <= 180`.

---

### 10. Аудит чистоти полів (Zero Metadata Leakage Check)
```text
Перевір згенеровані конфігурації на наявність витоку метаданих у полі стилю.
```
*Критерій перевірки*:
- Поле `Style of music` НЕ містить підрядків:
  - `Language:`
  - `Theme:`
  - `Mood:`
  - `Prompt:`
  - `Style:`
  - `Artist:`

---

### 11. Валідація парадоксу локалізації (Localization Paradox Audit)
```text
Перевір, що поле Style of music не містить кириличних речень опису стилю, а Lyrics не містить англійського тексту пісні (якщо це український трек).
```
*Критерій перевірки*:
- `Style of music`: виключно латинські літери (окрім автентичних термінів на кшталт `bandura`, `sopilka`, `tsymbaly`, `duda`).
- `Lyrics`: український текст із коректною розміткою.

---

### 12. Аудит акустичного негативного промптингу (Exclude Vector Check)
```text
Перевір, що поле Exclude містить як мінімум 2 токени пригнічення фізичних артефактів аудіо (metallic highs, muddy bass, garbled vocals, excessive reverb) та 2 токени стилістичних анти-кліше.
```
*Критерій перевірки*:
- Наявність фізичних анти-артефактів у кожному тестовому виході.

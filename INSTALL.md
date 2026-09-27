# Інструкція зі встановлення (Antigravity / Claude / Codex / Cursor)

Цей репозиторій розроблено за відкритим стандартом **Agent Skills Specification** (YAML frontmatter + Markdown + модульні посилання), що дозволяє використовувати його у будь-якому сучасному ШІ-агенті або LLM-середовищі.

---

## 1. 🟣 Встановлення для Anthropic Claude

### 1.1. Claude Code (CLI)
Claude Code автоматично знаходить скіли у робочій директорії:
1. Клонуйте або скопіюйте папку `skills/` у корінь вашого проєкту (або вкажіть шлях до `D:\poetry-skill\skills`).
2. Скіли активуються автоматично за їхніми описами (description у `SKILL.md`):
   - `skills/ukrainian-poetry/SKILL.md` — для поезії;
   - `skills/ukrainian-poetry-to-suno/SKILL.md` — для пісень (Suno v6-mini, Flow Music).
   Спільні правила — у [`AGENTS.md`](./AGENTS.md).

### 1.2. Claude.ai (Веб / Projects)
1. Створіть новий проєкт у Claude.ai (**Projects**).
2. У розділ **Project Knowledge** завантажте:
   - [`skills/ukrainian-poetry/references/full-guide.md`](./skills/ukrainian-poetry/references/full-guide.md) (повна поетична інструкція);
   - [`skills/ukrainian-poetry-to-suno/references/full-guide.md`](./skills/ukrainian-poetry-to-suno/references/full-guide.md) (повна музична інструкція);
   - [`skills/ukrainian-poetry-to-suno/references/reference-to-style-cheatsheet.md`](./skills/ukrainian-poetry-to-suno/references/reference-to-style-cheatsheet.md) (таблиця референсів).
3. У поле **Project Instructions** скопіюйте текст із [`AGENTS.md`](./AGENTS.md).

---

## 2. 🟢 Встановлення для OpenAI / Codex / Custom GPTs

### 2.1. OpenAI Custom GPTs / Assistants API
1. Відкрийте редактор **GPT Builder** або **OpenAI Assistants**.
2. У поле **Instructions** вставте текст із [`skills/ukrainian-poetry/SKILL.md`](./skills/ukrainian-poetry/SKILL.md) або [`skills/ukrainian-poetry-to-suno/SKILL.md`](./skills/ukrainian-poetry-to-suno/SKILL.md) (або [`AGENTS.md`](./AGENTS.md)).
3. У розділ **Knowledge** (Retrieval) завантажте файли з папки `references/` (довідники настроїв, анти-патерни, паки стилів).
4. У папках скілів вже присутні готові маніфести [`agents/openai.yaml`](./skills/ukrainian-poetry/agents/openai.yaml).

### 2.2. Codex CLI / Автономні агенти
Вкажіть шлях до директорії `skills/` або використовуйте глобальні інструкції з [`AGENTS.md`](./AGENTS.md).

---

## 3. 🔵 Встановлення для Google Antigravity / Gemini CLI

### 3.1. Глобальний плагін (Рекомендовано)
Плагін встановлюється у глобальну конфігурацію користувача:
```text
~/.gemini/config/plugins/poetry-skill/
├── plugin.json
└── skills/
    ├── ukrainian-poetry/
    └── ukrainian-poetry-to-suno/
```
Увімкнення в `~/.gemini/config/config.json`:
```json
{
  "plugins": {
    "poetry-skill": {
      "enabled": true
    }
  }
}
```

### 3.2. Локальний проєкт
Antigravity автоматично підтягує скіли з поточної робочої директорії через `AGENTS.md` та `skills/`.

---

## 4. 💻 Встановлення для Cursor IDE / Windsurf / VS Code

1. У проєкті вже налаштовано файли:
   - [`.cursorrules`](./.cursorrules)
   - [`.cursor/rules/ukrainian-poetry.mdc`](./.cursor/rules/ukrainian-poetry.mdc)
   - [`AGENTS.md`](./AGENTS.md)
2. Cursor автоматично застосовує правила версифікації та генерації промптів при відкритті відповідних файлів або зверненні до чату.

---

## 5. Перевірка коректності роботи

Запустіть автономний тестовий раннер:
```bash
py -3 tests/run_tests.py --all
```
Всі 75+ тестів мають повернути статус `[PASS]` зі 100% успішністю.

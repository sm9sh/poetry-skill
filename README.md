# Ukrainian Poetry & AI Songs (v4.0.0)

Два скіли для AI-агентів (Claude Code, Gemini / Antigravity, Cursor, Codex):

| Скіл | Що робить |
|---|---|
| `skills/ukrainian-poetry/` | Пише, редагує й оцінює українські вірші: свіжа образність, щирість, правильні наголоси та евфонія, різнорідні рими, природний порядок слів, форма відповідно до змісту. |
| `skills/ukrainian-poetry-to-suno/` | Перетворює вірш або ідею на пісню для **Suno v6-mini** (основна ціль) і **Google Flow Music (Lyria 3.5)**: пісенна форма й хук, розмітка `[...]` / `(...)`, наголоси, Style та Exclude. |

Спільні правила — у `AGENTS.md`.

## Як це працює

```text
тема / чернетка / вірш
        │
        ▼
ukrainian-poetry ──► вірш (6 принципів, наголоси, рими)
        │
        ▼  якщо потрібна пісня
ukrainian-poetry-to-suno
   1. адаптація вірша під пісню (хук, форма, рівні рядки)
   2. розмітка: [секції й вказівки], (лише співаний бек-вокал)
   3. наголоси великими літерами — лише 3 категорії
   4. Style + Exclude (Suno) або промпт природною мовою (Flow)
   5. scripts/check_lyrics.py
        │
        ▼
готові блоки для вставки в Suno / Flow Music
```

## Швидкий старт

- «Напиши вірш про …» → поетичний скіл.
- «Зроби з цього вірша пісню для суно в стилі darkwave» → вірш адаптується, ви отримуєте Style / Exclude / Lyrics.
- Перевірити лірику вручну:
  ```bash
  python skills/ukrainian-poetry-to-suno/scripts/check_lyrics.py lyrics.txt --style "darkwave, ..." --exclude "cheesy pop, ..."
  ```

## Структура

- `skills/` — джерело правди. `.agents/skills/` — дзеркало для рантайму (`python tests/sync_ecosystem.py`).
- `skills/ukrainian-poetry-to-suno/references/platforms.md` — актуальні ліміти й функції платформ (з датою перевірки).
- `examples/` — приклади треків і розбори типових помилок.
- `tests/` — валідатори та фікстури: `python tests/run_tests.py --all`.
- `evals/` — реальні запити для оцінки якості виходу «зі скілом / без скіла».

Детальніше — `HOWTO.md`.

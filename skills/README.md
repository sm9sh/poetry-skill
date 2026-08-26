# Skills

Готова папка для підключення локальних Codex / agentskills skills.

## Вміст

- `ukrainian-poetry/` - готовий skill для написання, редагування й оцінювання української поезії
- `ukrainian-poetry-to-suno/` - готовий skill для перетворення українських ідей, віршів, лірики й референсів у Suno prompts

Кожен skill має стандартну структуру:

```text
skill-name/
  SKILL.md
  agents/openai.yaml
  references/
```

## Як підключати

1. Вкажи цю папку як директорію skills:

```text
D:\poetry-skill\skills
```

2. Перезапусти сесію агента або раннер.
3. Перевір, що з'явилися skills:
   - `ukrainian-poetry`
   - `ukrainian-poetry-to-suno`

## Нотатка

Файли `SKILL.md` навмисно компактні. Великі матеріали, тести, рубрики й prompt packs лежать у `references/` всередині відповідного skill і мають читатися лише за потреби.

Старі однофайлові entrypoints збережені в `../source/legacy-skills/`.

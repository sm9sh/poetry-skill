Це пісня для **Lyria 3.5** (Google Flow Music): блок Prompt і блок Lyrics.

Скрипт `check_lyrics.py` я не запускав, бо в цій сесії немає доступу до папки скіла. Перевірку зробив вручну за чеклістом: дужки, повтор хука, форма, довжина рядків.

**Prompt**
```
Dreamy trip-hop and ambient with a slow, hypnotic downtempo groove at about 70 BPM. Intimate, breathy female vocal, close and dry with soft reverb tails, over warm sub-bass, a muted brushed drum loop, vinyl crackle and wide evolving synth pads. Sparse and calm, with a quiet piano motif; the final chorus opens up with layered harmonies, then fades out. About 2.5 minutes.
```

**Lyrics**
```
[Intro - sparse ambient pad, soft vinyl crackle]

[Verse 1 - whispered, intimate, half-time feel]
Хвіртка тепер зелена.
Ключ ще лежить у кишені.
Яблуня тягне гілку
До чужого вікна.

[Chorus - open, airy, layered harmonies]
Сад уже не наш,
Сад уже не наш.
Яблука падають тихо,
Так само, як при тобі.
Сад уже не наш.
(не наш)

[Verse 2 - low, breathy, sub-bass enters]
Мальви зрізали під корінь.
Поставили сітку й паркан.
Я збираю в долоню
Три яблука з її трави.

[Chorus - open, airy, layered harmonies]
Сад уже не наш,
Сад уже не наш.
Яблука падають тихо,
Так само, як при тобі.
Сад уже не наш.
(не наш)

[Bridge - almost spoken, only pad and sub-bass]
Я відламала гілочку смородини.
Загорну її в хустинку.
Хай росте на підвіконні
У місті, де немає саду.

[Final Chorus - widest, soft harmonies, fading pad]
Сад уже не там,
Сад тепер у мені.
Яблука падають тихо,
Так само, як при тобі.
Сад уже не наш.
(не наш)

[End]
```

**Примітки**
- Ви написали «тексту немає», тож слова я написав сам. Співає онука, яка прийшла до проданого саду. Хук-назва: «Сад уже не наш».
- V2 додає нові деталі: зрізані мальви й новий паркан. Бридж дає поворот: гілочка смородини, яку вона забирає в місто. У фінальному приспіві хук змінюється на «Сад тепер у мені».
- Наголосів не позначав: у тексті немає омографів і «російських пасток».
- Якщо вокал тараторить, у Prompt напишіть `slower, about 65 BPM`. Якщо хочете більше ambient і менше ритму, замініть `muted brushed drum loop` на `barely-there soft pulse`.
- Якщо вдалася не вся пісня, а лише одна секція (наприклад, бридж), виправляйте її через Replace, не перегенеровуйте трек.

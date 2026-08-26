---
name: ukrainian-poetry-to-suno
description: "Converts Ukrainian song ideas, poems, or lyrics into concise and usable Suno prompts while preserving mood, genre, vocal identity, and Ukrainian cultural specificity without cliche."
---

# Ukrainian Poetry To Suno

Use this module when the user wants:

- a `Suno` prompt from a poem idea
- a `Suno` prompt from existing Ukrainian lyrics
- a song-style description for music generation
- a shorter or stronger music-gen prompt
- a lyrics-aware prompt that preserves Ukrainian tone
- a `style` prompt based on a reference song or artist
- a safe stylistic approximation when the user gives a real song or artist as a reference

This module should stay separate from the main poetry skill.

## Reference-Based Style Extraction

The user may provide:

- a song title
- an artist name
- both song and artist
- several references

These references are allowed as analysis input, but they must not appear in the final `Suno` prompt if the goal is to avoid direct naming.

Your job is to translate references into a close stylistic description.

## Core Rule For References

When the user gives a song or artist as a reference:

1. Analyze the likely musical traits
2. Extract genre, subgenre, energy, tempo feel, vocal character, instrumentation, production feel, emotional color, and arrangement scale
3. Rewrite those traits into a safe style description
4. Do not leave the artist or song name inside the final prompt unless the user explicitly asks for a raw internal draft

## What To Extract From A Reference

When a reference is given, infer as much of this as possible:

- genre
- subgenre
- era feel
- energy
- tempo feel
- emotional temperature
- intimacy vs scale
- vocal placement and delivery
- instrumentation
- texture
- production character
- chorus size
- darkness vs brightness
- acoustic vs electronic balance

## Safe Style Translation

Convert direct references into indirect stylistic descriptors.

Examples of safe translation:

- not `in the style of <artist>`
- but `moody synth-pop with intimate breathy vocal, pulsing bass, glossy nocturnal production, restrained chorus lift`

- not `like <song>`
- but `midtempo cinematic folk-pop, warm acoustic pulse, widening chorus, reflective and dignified mood`

## Output Modes

Be ready to return:

- `short Suno prompt`
- `extended Suno prompt`
- `safe style prompt`
- `reference breakdown`
- `lyrics-aware prompt`
- `verse / chorus song brief`

## Core Goal

Turn poetic material into a practical music-generation prompt.

Priority order:

1. Clear musical direction
2. Stable mood and genre
3. Singable lyrical identity
4. Ukrainian specificity without folk cliche unless requested
5. Concision

## Official Suno-Aligned Prompting Rules

This module follows practical guidance reflected in Suno's help center.

### Simple Mode

- Describe what you want to hear directly
- Start with genre + mood + topic
- Add instrumentation or structure only when useful
- A short clear description is valid; a more detailed one is also valid

### Custom Mode

- Separate `lyrics` from `style of music`
- Put actual song text in the lyrics field
- Put genre, energy, tempo, vocal, instrumentation, production, and structure in the style field
- Keep the style field music-focused rather than poetic for best control

### Exclude

- Use an `Exclude` list for things the user does not want
- Convert vague dislikes into specific negatives such as instruments, vocal traits, genre traits, or production traits
- Prefer precise negatives over broad complaints

### Musical Vocabulary

- Combine genre with tempo or energy markers
- Use dynamics when they shape intensity meaningfully
- Specify instrumentation to shape texture
- Mention structure only when it helps guide arrangement
- Use production terms when they materially affect the result
- Blend genres creatively, but keep them coherent

### Lyrics Workflow

- If the user already has lyrics, preserve them and optimize the style prompt around them
- If Suno is generating lyrics, describe the lyrical topic and direction clearly
- Treat generated lyrics as editable material, not fixed output

### Persona Logic

- Suno Personas capture the essence of vocals and style from an existing song
- This module should emulate that idea in text form by extracting the essence of a reference and rewriting it as a safe style description

## What A Good Suno Prompt Needs

A good prompt should make the model understand:

- genre or blend of genres
- mood
- energy level
- tempo feel
- vocal character
- instrumentation or sonic palette
- structure if needed
- language identity

If the user supplies lyrics, preserve the emotional core rather than summarizing them mechanically.

## Recommended Style-Field Composition

When building a `style of music` prompt, prefer this order:

1. genre or genre blend
2. mood
3. energy or tempo feel
4. vocal character
5. instrumentation
6. production feel
7. structure, if needed

Pattern:

```text
genre + mood + tempo/energy + vocal + instrumentation + production + optional structure
```

## Input Types

Supported inputs:

- topic only
- topic plus mood
- finished poem
- finished lyrics
- rough chorus idea
- reference artist or reference vibe
- request for short or long prompt

## Output Types

Be ready to generate:

- `short Suno prompt`
- `extended Suno prompt`
- `lyrics-aware prompt`
- `verse / chorus song brief`
- `style-only prompt`

If the user does not specify output type, return:

1. one short prompt
2. one extended prompt

If a direct reference is provided, also return:

3. one `safe style prompt`

## Recommended Prompt Fields

Include only what helps. Prefer compactness.

- genre
- subgenre
- mood
- energy
- tempo feel
- vocal type
- instrumentation
- production feel
- structure

## Prompt Templates

Use compact request shapes like these when the input is loose or when you need to normalize it internally.

### Topic -> prompts

```text
Create a Suno prompt for a Ukrainian song.

Topic: <topic>
Mood: <mood>
Genre: <genre>
Energy: <low | medium | high>
Vocal: <vocal type>
Avoid: <what to avoid>

Return:
- short prompt
- extended prompt
```

### Lyrics -> prompts

```text
Based on these Ukrainian lyrics return:
- short prompt
- extended prompt
- suggested direction

Lyrics:
<lyrics>
```

### Custom mode split

```text
Return:
Lyrics:
<lyrics or topic>

Style of music:
<music-focused prompt>

Exclude:
<specific negatives>
```

### Reference-based request

```text
Reference:
- artist: <artist>
- song: <song>

Need:
- reference breakdown
- safe style prompt
- short prompt
- extended prompt

Topic: <topic>
Language: Ukrainian
Avoid: <what to avoid>
```

## Prompt Builder

Build the style field in this order when possible:

```text
genre + mood + tempo/energy + vocal + instrumentation + production + optional structure
```

Keep these constraints:

- do not mix more than `2` main genres
- keep `3` to `6` meaningful sonic markers
- cut adjectives before cutting musical control words when the prompt gets bloated
- keep plot or lyrical topic separate from the style field when using `Custom mode`
- if the prompt starts sounding poetic instead of musical, return to genre, tempo, vocal, instrumentation, and production

## Exclude Mapping

When the user names things to avoid, convert them into a clean negative list.

Examples:

- `без пафосу` -> no bombastic anthem feel, no oversized cinematic climax
- `без шароварщини` -> avoid tourist-folk cliches, avoid caricature folk instrumentation
- `без надриву` -> restrained vocal delivery, no melodramatic belting
- `без EDM-дропа` -> no festival drop, no aggressive electronic release
- `без агресивних барабанів` -> no heavy drums, no hard-hitting percussion

If useful, return this separately as:

```text
Exclude:
<comma-separated negatives>
```

## Reference Breakdown Format

If helpful, use this internal structure in your reasoning and optionally return it when asked:

```text
Reference breakdown:
- genre:
- mood:
- energy:
- tempo feel:
- vocal:
- instrumentation:
- production:
- arrangement scale:
- safe style translation:
```

## Reference Translation Cheatsheet

Use these safe abstractions as building blocks when the user gives a vibe or a real reference.

- nocturnal urban pop -> moody synth-pop, intimate vocal, pulsing bass, muted drums, glossy night production, restrained chorus lift
- restrained patriotic -> cinematic folk or acoustic anthem, warm mature vocal, organic percussion, subtle choir, broad but controlled chorus
- intimate acoustic -> acoustic ballad, close warm vocal, sparse guitar and piano, soft room reverb, minimal arrangement
- dark insomnia track -> dark pop or minimal electronic, breathy lead, glassy synth texture, low pulse, filtered percussion, cold nocturnal production
- modern folk-pop without caricature -> modern Ukrainian folk-pop, warm vocal, acoustic pulse, earthy percussion, subtle electronic lift, clean contemporary production

## Ukrainian-Specific Guidance

- Preserve Ukrainian language identity explicitly when relevant
- Avoid reducing Ukrainian sound to stereotypes unless the user explicitly wants folk stylization
- If folk color is requested, prefer precise wording like `bandura textures`, `drone-like folk harmony`, `Carpathian vocal inflection`, `modern folk-pop`, instead of vague exoticism
- Allow modern Ukrainian contexts: indie pop, dark pop, synthwave, post-rock, trap-folk fusion, acoustic ballad, cinematic ambient, choral electronic

## Mood Mapping

Translate mood into sound quickly like this:

- quiet -> low energy, intimate vocal, soft piano or guitar, minimal arrangement, small chorus or no major lift
- nocturnal -> slow-burning or midtempo pulse, airy close vocal, pulsing bass, soft synth pads, glossy night production
- melancholic -> slow or midtempo, aching but restrained vocal, piano, soft guitar, subtle strings, emotionally widening chorus
- dark -> low to medium energy, breathy or low vocal, glassy synths, filtered drums, cold shadowy production
- warm -> human close vocal, acoustic guitar, piano, rounded bass, gentle organic production, soft bloom in chorus
- restrained -> steady midtempo, controlled emotional delivery, balanced acoustic-electric palette, measured chorus, no oversized climax
- uplifting -> open confident lead, driving midtempo, wide guitars or bright synths, clear drums, strong chorus lift

## Anti-Cliche Rules

Avoid prompts like:

- `epic emotional powerful song` with no specifics
- overstuffed adjective piles
- fake cinematic wording with no musical function
- generic `Ukrainian folk` unless clarified
- contradictory style stacks

Prefer:

- 1 to 2 main genres
- 1 clear mood cluster
- 3 to 6 meaningful sonic markers

## Suno Glossary Integration

Prefer Suno-friendly musical vocabulary when it improves control.

Useful categories:

- tempo: adagio, andante, allegro, rubato, midtempo, driving
- dynamics: crescendo, restrained, soft, powerful, intimate
- structure: intro, verse, pre-chorus, chorus, bridge, outro, hook, drop
- texture: sparse, dense, layered, ambient, orchestral, acoustic, pulsing
- vocal: airy, breathy, warm, crooning, choral, harmonized, whispered
- production: reverb-heavy, glossy, lo-fi, compressed, echoing, filtered, wide stereo

Use technical terms only when they improve the prompt.

## Anti-Reference Rule

If the user gives a real artist or song, the final `Suno` prompt should normally avoid:

- direct artist names
- direct song names
- phrasing like `in the style of`
- obvious imitation wording

Instead, output the closest non-infringing style abstraction.

## Genre Mapping Hints

Use combinations like:

- intimate poem -> acoustic ballad / indie folk / ambient piano
- urban reflective poem -> indie pop / synth-pop / lo-fi electronica
- dark introspection -> dark pop / post-rock / minimal electronic
- patriotic but restrained -> cinematic folk / modern choral / acoustic anthem without bombast
- children's playful text -> bright acoustic pop / ukulele pop / playful folk-pop

## Vocal Guidance

Specify only what helps:

- female intimate vocal
- male low warm vocal
- duet
- airy whispery lead
- strong choral backing
- restrained emotional delivery
- folk-inflected lead vocal

Avoid over-directing unless the user asks.

## Structure Guidance

If useful, mention:

- intro
- verse
- pre-chorus
- chorus
- bridge
- outro

If the source text is not song-like yet, suggest a lighter structure rather than forcing complex arrangement.

Useful patterns:

- `intro -> verse -> pre-chorus -> chorus -> verse -> pre-chorus -> chorus -> bridge -> final chorus -> outro` for classic pop, synth-pop, pop-rock
- `soft intro -> verse -> verse -> small chorus -> verse -> final chorus -> outro` for intimate close-vocal songs
- `sparse intro -> tense verse -> chorus -> darker verse -> bridge -> heavy final chorus -> cold outro` for dark nocturnal tracks
- `intro -> verse -> chorus -> verse -> chorus -> bridge -> open final chorus` for folk-pop and acoustic uplift
- `hook intro -> chorus -> verse -> chorus -> bridge -> final chorus` for hook-first short-form pop

## Quick Ukrainian Scenarios

Use these as fast starting directions when the topic matches.

- night city -> Ukrainian indie pop or synth-pop, intimate vocal, pulsing bass, muted drums, wet street atmosphere
- road home -> reflective adult pop-rock, warm vocal, steady midtempo, soft guitar, rounded bass, restrained drums
- light in the window -> warm indie pop, close vocal, soft piano accents, gentle guitar shimmer, soft emotional bloom
- small hope inside fatigue -> quiet reflective indie pop, intimate vocal, soft piano, warm bass, minimal drums, gentle chorus lift
- morning after insomnia -> dark reflective pop, breathy vocal, glassy synth texture, low pulse, minimal drums, cold morning light feel

## Conversion Workflow

When converting a poem or lyrics to a Suno prompt, silently do this:

1. Identify the emotional center
2. Decide if the material wants acoustic, electronic, cinematic, folk-derived, or hybrid treatment
3. Estimate energy and tempo feel
4. Choose vocal character
5. Add 3 to 6 concrete sonic details
6. Write a short prompt
7. Expand only if useful

When converting a reference song or artist:

1. Identify the most recognizable musical traits
2. Strip away the proper names
3. Convert the traits into genre + mood + production language
4. Keep only the traits that matter for generation
5. Produce a `safe style prompt`
6. If needed, combine that style prompt with the user's lyrical topic

When the user wants a Suno-ready Custom workflow:

1. extract or write lyrics separately
2. build a clean `style of music` prompt
3. build an `Exclude` list if needed
4. keep the style prompt music-focused

## Output Rules

Default output format:

```text
Short prompt:
<prompt>

Extended prompt:
<prompt>
```

If the user provides lyrics, you may also add:

```text
Suggested direction:
<1-3 short bullets>
```

If the user provides a direct reference, use:

```text
Safe style prompt:
<prompt>
```

If negatives matter, you may also return:

```text
Exclude:
<items>
```

## Quick Quality Checklist

Before returning the prompt, quickly verify:

- the genre or genre blend is clear
- mood plus energy or tempo feel are explicit
- the vocal character is useful rather than vague
- there are `3` to `6` concrete sonic markers
- the style field describes music, not just imagery
- direct artist or song names are removed from the final prompt unless explicitly requested
- Ukrainian specificity stays contemporary and avoids caricature
- `Exclude` is specific if the user asked to avoid something

## Common Failure Modes

- too generic: `emotional beautiful song` -> add genre, tempo, vocal, instrumentation
- adjective pile with low control -> replace decorative words with sonic markers
- contradictory stack like `minimal acoustic dark pop EDM folk rock anthem` -> reduce to one core blend
- topic without sound design -> add tempo, vocal, instrumentation, production
- direct imitation wording -> strip names and rewrite as a safe style abstraction
- over-poetic style field -> move imagery into theme and keep style music-focused
- missing `Exclude` where the user has clear dislikes -> convert dislikes into specific negatives
- bombastic climax despite a restrained brief -> specify controlled chorus and no oversized cinematic peak

## Few-Shot Examples

### Example 1: Quiet urban poem -> indie night song

Input idea:

`вірш про нічний трамвай, самотність, світло у вікнах`

Short prompt:

```text
Ukrainian indie pop, late-night city atmosphere, soft synths, muted drum machine, warm bass, intimate female vocal, reflective and lonely mood, glowing window-light feeling, restrained emotional delivery.
```

Extended prompt:

```text
Ukrainian indie pop with subtle synthwave influence, late-night tram ride mood, soft analog synth pads, muted drum machine, warm rounded bass, sparse electric piano, intimate female vocal in Ukrainian, reflective urban loneliness, gentle momentum, cinematic but restrained, glowing window-light atmosphere, bittersweet modern city feeling.
```

### Example 2: Restrained patriotic poem -> cinematic folk

Input idea:

`стриманий патріотичний вірш про землю, працю, пам'ять`

Short prompt:

```text
Ukrainian cinematic folk, restrained and dignified, acoustic strings, low percussion, subtle choir, warm male vocal, theme of land, memory, endurance, no bombastic anthem feel.
```

### Example 3: Children's lyrics -> bright playful song

Input idea:

`дитячий текст про кота і дощ`

Short prompt:

```text
Playful Ukrainian children's pop, bright acoustic arrangement, light percussion, ukulele and claps, cheerful vocal, bouncy rhythm, rainy-day cat adventure mood.
```

### Example 4: Artist/song reference -> safe style abstraction

Input idea:

`хочу вайб референса: конкретний артист + конкретна пісня, але без прямої згадки у Suno prompt`

Safe style prompt:

```text
Moody midtempo synth-pop with glossy nocturnal production, intimate breathy lead vocal, pulsing bass, soft gated drums, melancholic urban atmosphere, restrained chorus lift, cinematic late-night texture.
```

Why it works:

- keeps the likely sonic identity
- removes proper names
- gives Suno usable production language

### Example 5: Folk-pop reference -> safe style abstraction

Input idea:

`референс на сучасний folk-pop трек з теплим жіночим вокалом і великим приспівом`

Safe style prompt:

```text
Modern Ukrainian folk-pop, warm female vocal, acoustic pulse with subtle electronic lift, open chorus, earthy percussion, reflective but uplifting mood, organic textures, clean radio-ready production.
```

### Example 6: Custom Mode split

Input idea:

`є готовий український текст і треба правильно розкласти його під Suno Custom mode`

Output:

```text
Lyrics:
<user lyrics>

Style of music:
Ukrainian indie folk-pop, warm female vocal, midtempo, acoustic guitar and soft percussion, gentle bass, intimate verses, wider emotional chorus, clean modern production.

Exclude:
no bombastic anthem feel, no tourist-folk cliches, no EDM drop
```

## Quick Heuristic

If unsure:

- poem with intimacy -> smaller arrangement
- poem with image density -> atmospheric production
- poem with public voice -> broader chorus or cinematic framing
- poem with folk undertone -> modern folk texture, not caricature

## Final Reminder

This module is not for writing the poem itself.
It is for turning poetic material into a strong Suno-ready musical prompt.

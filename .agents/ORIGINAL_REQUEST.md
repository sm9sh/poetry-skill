# Original User Request

## 2026-08-26T09:37:56Z

Perform a comprehensive multi-agent audit and upgrade of the Ukrainian Poetry and Suno AI skills in this repository (ukrainian-poetry and ukrainian-poetry-to-suno), identifying weak points, failure modes, and ambiguities across linguistic authenticity, poetic mechanics, and AI music generation prompt engineering, and implementing concrete improvements.

Working directory: d:/poetry-skill
Integrity mode: development

## Requirements

### R1. Ukrainian Poetic & Linguistic Audit
Analyze the poetry generation skill (ukrainian-poetry/SKILL.md and related reference docs) for accuracy, depth, and practical guidance on Ukrainian versification (syllabo-tonic, tonic/dolnik, verlibre), stress/accentuation rules, rhyme quality (avoiding banal/grammatical rhymes without forcing awkward syntax), diction registers, emotional resonance, and preventing cliches, pseudo-folk tropes (sharovarshchyna), or translation calques.

### R2. Suno AI Music Prompting & Structure Audit
Analyze the Suno conversion skill (ukrainian-poetry-to-suno/SKILL.md and related reference docs) for compatibility with modern Suno AI models, tag token economy, style/genre blending rules, vocal timbre directives, metatag placement ([Verse], [Chorus], [Drop], etc.), Exclude field behavior, and Ukrainian cultural/contemporary musical style mapping.

### R3. Edge Case & Stress-Test Gap Analysis
Evaluate the existing test suites (	ests.md, stress-tests.md, ukrainian-poetry-skill-tests.md, suno-prompt-tests.md) against challenging real-world requests (e.g., complex meters, mixed languages, subtle subgenres, conflicting constraints). Identify missing edge cases and potential failure modes where the current instructions lead to degraded outputs.

### R4. Actionable Improvements & File Upgrades
Produce a structured audit report detailing identified weaknesses, trade-offs, and prioritized solutions, and apply high-value enhancements directly to the skill instructions, reference guides, rubrics, and test suites across the repository.

## Acceptance Criteria

### Audit & Analysis Deliverables
- [ ] A structured evaluation report cataloging weaknesses, ambiguities, and failure modes for both ukrainian-poetry and ukrainian-poetry-to-suno
- [ ] Specific analysis of Ukrainian linguistic/poetic constraints (meter fidelity, rhyme classification, stress management, anti-cliche guardrails)
- [ ] Specific analysis of Suno AI generation constraints (token efficiency, tag weighting, metatag syntax, audio artifact reduction)

### Upgraded Artifacts & Skill Files
- [ ] Improved SKILL.md files for both skills with clearer instructions, sharper constraints, and refined default parameters
- [ ] Enhanced reference files and cheatsheets addressing identified gaps (e.g., modern Ukrainian music genres, dolnik/accentual verse, stress dictionaries, meta-tag best practices)
- [ ] Expanded test suites with new stress-test scenarios covering discovered edge cases
- [ ] Backward compatibility verified: existing standard test cases pass without regressions

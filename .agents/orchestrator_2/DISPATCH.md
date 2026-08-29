# Dispatch Log

## 2026-08-29T19:17:04Z

You are the Project Orchestrator for the poetry-skill AI Music Alchemy v8 integration project.

Working directory: d:\poetry-skill\.agents\orchestrator_2
Original user request is authoritative at: d:\poetry-skill\.agents\ORIGINAL_REQUEST.md
Source specification: d:\poetry-skill\ai-music-generation-meta-spec-v8.md

Your mission:
Integrate the full-scale specification «AI Music Alchemy & Prompt Engineer (Suno / Udio / Flow Music)» v8 into skills, references, prompt architecture, validators, and tests of the poetry-skill ecosystem.

Key requirements to orchestrate:
1. R1: Skill Architecture & Guides Update:
   - Update skills/ukrainian-poetry-to-suno/SKILL.md, skills/ukrainian-poetry-to-suno/references/full-guide.md, skills/poetry-skill/SKILL.md, AGENTS.md, and GEMINI.md.
   - Update root symmetrical files: ukrainian-poetry-to-suno.md, ukrainian-poetry-skill.md, lyrics-to-suno-template.md, song-structure-pack.md, suno-prompt-anti-patterns.md.
   - Integrate the complete 6-step lifecycle:
     - Step 1: Deep Reference Reverse Engineering (Genre hybrid, BPM, Key, Sonic aesthetic/timbre, Vocal Triple-Stack [Character+Delivery+FX], Melodic Math hooks, Bracketed layout).
     - Step 2: AI-Optimized Lyrics Writing (Syllable symmetry, Spoken Prosody Test, Staccato vs Legato spatial contrast, 5-Second Rule, 50-Second Chorus Rule, Melodic Previews, Glue Hooks, Cognitive melody limits <=3-4).
     - Step 3: Multi-Platform Prompt Engineering (Suno v4.5/v5.5 Method 1 First 5 Words & Method 2 Tag Matrix 5 modules, My Taste, Voices cloning, Custom Models, Failure modes; Udio v4 48kHz, Context Length, Inpainting *stars*, Pro rights; Google Flow Music Lyria 3.5 Conversational Agent, Spaces, Turntable, Section replace, AI Cover, Gemini Omni Flash sync, 500 daily credits).
     - Step 4: Step-by-Step Extensions Roadmap (The AI Conductor: Seed 30-50s, Extend, Vance Powell Verse 2 development, Breakdown & Mega-Chorus, Outro <=20s).
     - Step 5: Engineering DAW Post-Production & Stem Mixing (Stem splitting [Moises, RipX, LALAL.AI], phase optimization kick/bass, dynamic sidechain unmasking, Split Compression bass [<200Hz brickwall sub vs >200Hz dynamic saturated], Tchad Blake parallel distortion directly on Master Fader bypassing Drum Bus, dynamic Mid-Side Reverb sidechaining for vocals).
     - Step 6: Mastering & Algorithmic Streaming Distribution (Mastering without True Peak trap: -1 dBTP for -6..-8 LUFS with TP limiting disabled, or -14 LUFS for -2 dBTP; genre skip rate thresholds [Pop >48%, Hip-hop >44%, Electronic >37%, Indie rock >31%, alert >45%]; elimination of Playlist Placement Trap - direct ads to single only; Spotify Canvas, Marquee, Discovery Mode).

2. R2: Metatags, Prosody Rules & 10 AI Quality Gates:
   - Update song-structure-pack.md, lyrics-to-suno-template.md, suno-prompt-anti-patterns.md.
   - Add inline vocal gestures in parentheses: (whispered), (belted), (falsetto), (screamed), (ad-lib), (building intensity), (key change), (half-time feel), (harmonized).
   - Add the full table of 10 AI Quality Gates (Gate 1: Anti-Skip 5s, Gate 2: 50s Rule, Gate 3: Spoken Prosody, Gate 4: Staccato vs Legato, Gate 5: Verse 2 development by Powell, Gate 6: Breakdown & Mega-Chorus, Gate 7: Low end Split Compression, Gate 8: Tchad Blake drum distortion routing to Master, Gate 9: Mastering True Peak, Gate 10: Single-only Ads).

3. R3: Validators, Tests Synchronization & Backward Compatibility:
   - Update validators (tests/validator/metatag_validator.py, tests/validator/suno_validator.py, tests/validator/poetic_validator.py, etc.) to support new tags, inline gestures, and rules.
   - Preserve 100% compliance with 6 Ukrainian poetry principles, uppercase vowel stresses (вИпадок, дорОга), square brackets [...] for arrangements, round parentheses (...) exclusively for vocals/ad-libs.
   - Run tests `py -3 tests/run_tests.py --all` and achieve 100% passing tests (0 errors).
   - Sync updated files to .agents/skills/ and global directory C:\Users\sm9sh\.gemini\config\plugins\poetry-skill\.

4. R4: Post-Implementation 3-Agent Audit:
   - After integration and tests pass, dispatch 3 specialized auditor agents:
     - Agent 1: Prompt & Platform Spec Auditor (Suno v4.5/v5.5, Udio v4, Flow Music Lyria 3.5, tokens, chars, metatags)
     - Agent 2: Audio Engineering & Distribution Auditor (DAW split compression, phase optimization, Tchad Blake distortion to Master, Mid-Side reverb sidechaining, True Peak trap elimination, Skip Rate thresholds, Quality Gates)
     - Agent 3: Ukrainian Poetry & Cross-System Integrity Auditor (6 poetic principles, capitalized vowel stresses, brackets rule [...] vs (...), zero regression in existing modules and tests)
   - Ensure all 3 auditors approve with zero findings.

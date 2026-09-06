# Ukrainian Poetry & Multi-Platform AI Music Generation Ecosystem (v3.0.0)

A comprehensive AI skill ecosystem for generating, auditing, verifying, and transforming authentic Ukrainian poetry into production-grade prompts for **Suno AI v4.5/v5.5**, **Udio AI v4**, and **Google Flow Music Lyria 3.5**.

The Single Source of Truth for system architecture is `AGENTS.md`.

---

## 1. System Architecture (6-Step Production Lifecycle)

The architecture is built on a 6-Step Production Lifecycle connecting specialized AI skills with a shared reference foundation:

```text
                  [User Input / Creative Brief]
                                │
                                ▼
               ┌─────────────────────────────────┐
               │     ukrainian-poetry Skill      │
               │  - Syllabo-Tonic & Dolnik       │
               │  - Mobile Stress & Homographs   │
               │  - 5 poetry subagents           │
               └────────────────┬────────────────┘
                                │ (Structured Lyrics + Prosodic Metatags)
                                ▼
               ┌─────────────────────────────────┐
               │   Music Prompting Engine        │
               │  - 4 music subagents            │
               │  - 8-Genre Western Anchor       │
               │  - Vocal Triple-Stack           │
               └────┬───────────┬───────────┬────┘
                    │           │           │
                    ▼           ▼           ▼
             [Suno AI]      [Udio AI]  [Flow Music]
```

---

## 2. Repository Structure

### 2.1 Canonical Skills (Runtime-Ready in `.agents/skills/`)
Core agents and prompts are located in `.agents/skills/`.
- **5 poetry subagents** for text generation and auditing.
- **4 new music production subagents** for Suno, Udio, and Flow Music.

### 2.2 Automated E2E Test Infrastructure
- Master test runner covers Tiers 1-4.
- **Udio + Flow Music validators** to ensure output quality.
- Metric, style, and metatag validation.

---

## 3. Key Features & 10 AI Quality Gates

The system implements a matrix of **10 AI Quality Gates** for end-to-end quality control.

### 3.1 Music Production & AI Conductor
- **Western Genre Anchor**: Updated 8-genre taxonomy.
- **Vocal Triple-Stack**: Formula for complex vocal arrangements.
- **AI Conductor extensions roadmap**: Generation sequence (Seed → Extend → Breakdown → Mega-Chorus → Outro).
- **Metatag Grammar**: Strict rules for brackets `[]` vs parentheses `()`, and 9 canonical inline vocal gestures.

### 3.2 Post-Production and Distribution
- **DAW stem mixing checklist**: Split Bass, Tchad Blake distortion, Mid-Side reverb sidechain.
- **Mastering**: Avoiding the True Peak trap (-1 dBTP for -6..-8 LUFS).
- **Streaming distribution**: Skip Rate thresholds, Playlist Placement Trap elimination.

---

## 4. Quick Start

### Poetry Generation & Multi-Platform Prompting
1. Generate authentic Ukrainian lyrics using `skills/ukrainian-poetry/`.
2. Use **Method 1 (Conversational)** or **Method 2 (HookGenius Tag Matrix)** for Suno, or specific formulas for Udio and Flow Music.
3. Obtain production-ready prompts for your target platform.

See `HOWTO.md` for more details.

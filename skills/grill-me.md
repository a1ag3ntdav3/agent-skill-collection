---
id: grill-me
title: Grill Me
category: Planning & Alignment
created_at: 2026-05-24
updated_at: 2026-05-24
difficulty: Intermediate
tags:
  - alignment
  - planning
  - requirements
  - interactive
---

# Grill Me

## Overview
The "Grill Me" skill (often triggered via `/grill-me`) is a structured alignment methodology designed to prevent "vibe coding." Instead of executing on vague or ambiguous prompts, the AI agent is instructed to act as a rigorous, Socratic interviewer, stress-testing requirements, architectural decisions, and edge cases before a single line of code is written.

## Prerequisites
- [Prompt Engineering](prompt-engineering.md) (Intermediate) - Understanding how system instructions govern agent persona and formatting.

## Core Concepts
- **Socratic Interviewing**: Asking deep, targeted questions about constraints, design choices, and dependencies rather than accepting initial user assumptions.
- **Decision Trees**: Exploring implementation paths branch-by-branch to surface hidden trade-offs.
- **Alignment Lock**: Ensuring the user and the agent share an identical mental model of the feature's architecture and behavioral requirements before beginning implementation.

## In-Depth Guide
The typical `/grill-me` workflow proceeds as follows:

1. **Activation**: The user invokes the command or indicates they want to plan a new feature (e.g., "Let's grill-me on building a database cache").
2. **Analysis**: The agent scans the existing codebase to understand the context and identify constraints.
3. **Interrogation**: The agent presents a structured set of questions covering:
   - Functional requirements (What must it do?)
   - Architectural constraints (How does it fit into the existing system?)
   - Edge cases and failure modes (What happens under load or network partitions?)
   - Developer preferences (Which tools, styles, or libraries should be used?)
4. **Iterative Refinement**: The user answers the questions, and the agent synthesizes this feedback, raising follow-up questions if new branches of decisions appear.
5. **Output Synthesis**: Once all branches are resolved, the agent compiles a clear specification (such as a PRD or a set of technical tasks) that details the agreed-upon design.

### Example Prompt/Instruction for Grill Me
```markdown
When the user invokes "/grill-me", do NOT write any code. Instead:
1. Identify the core user goal.
2. Ask 3-5 highly specific, critical questions that reveal hidden architectural decisions or edge cases in their plan.
3. Keep your questions brief and structured.
4. Wait for the user's response, and iterate if necessary. Only proceed to coding when the user explicitly signs off.
```

## Verification
To verify this skill:
1. Invoke `/grill-me` with a vague prompt like "I want to add OAuth authentication."
2. Confirm that the agent refuses to write code and instead replies with a list of clarifying questions regarding the OAuth providers, token storage, and session duration.
3. Verify that the agent maintains this interviewing persona until all queries are resolved and alignment is reached.

---
id: llm-wiki
title: LLM Wiki
category: Knowledge & Memory
created_at: 2026-05-24
updated_at: 2026-05-24
difficulty: Intermediate
tags:
  - documentation
  - knowledge-base
  - memory
  - context
---

# LLM Wiki

## Overview
An LLM Wiki is a persistent, structured knowledge base composed of markdown files in a repository. Popularized by builders like Andrej Karpathy, this pattern serves as the agent's external memory. By reading from and writing to a dedicated `/skills` or `/wiki` folder, the agent maintains long-term context, architectural decisions, and domain-specific knowledge across sessions without relying on complex, external RAG pipelines.

## Prerequisites
- [Git Basics](git-basics.md) (Beginner) - To version control the wiki.
- [Prompt Engineering](prompt-engineering.md) (Intermediate) - To direct the agent on how to update and link wiki files.

## Core Concepts
- **Persistent Context**: Unlike ephemeral chat logs, wiki pages stay in the codebase and are referenced by the agent dynamically.
- **Bi-directional Linking**: Markdown links (e.g., `[[git-basics|Git Basics]]` or `[Git Basics](git-basics.md)`) that form a web of knowledge, allowing agents to navigate related concepts.
- **Ingestion / Update Loop**: The process where compiler agents automatically update index pages and metrics as new files are added.

## In-Depth Guide
### Structure of an LLM Wiki
A standard LLM Wiki directory structure includes:
```
wiki/
├── index.md            # Entry point, metrics, and categorization list
├── git-basics.md       # Knowledge page on version control
└── prompt-engineering.md # Knowledge page on prompt techniques
```

### Writing Style for LLM Ingestion
When designing wiki pages for LLM ingestion:
1. **Be Concise**: Keep explanations direct and avoid conversational padding.
2. **Use Semantic Structure**: Utilize markdown headers (`#`, `##`, `###`) to outline concepts.
3. **Embed Verification Steps**: Every wiki entry should contain a verification section to check if the skill has been correctly applied.
4. **Link Generously**: Link to other relevant files inside the wiki to guide the agent's reasoning path.

### Automating the Wiki
To ensure the integrity of the wiki, configure a validation script (e.g., `validate_wiki.py`) to run as a git hook or CI pipeline. The script should verify:
- Frontmatter schema completeness.
- Broken links.
- Index file synchronicity.

## Verification
To verify this skill:
1. Create a new skill file under the wiki directory.
2. Update the wiki index file to link the new skill and increment the total count.
3. Run the validation script (e.g., `python3 scripts/validate_wiki.py`) to ensure no formatting errors or broken links exist.

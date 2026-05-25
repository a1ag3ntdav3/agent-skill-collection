---
name: llm-wiki
description: Maintaining persistent, structured codebase-level knowledge bases.
---

# LLM Wiki

Use this skill when reading from or writing to the persistent codebase-level documentation and wiki directory.

## Instructions
1. When learning project structure, read the central `wiki/index.md` file first.
2. When creating new files, write metadata in YAML frontmatter and save in `wiki/{id}.md`.
3. Add double-bracket relative links (e.g. `[[git-basics|Git Basics]]`) to cross-link files.
4. Ensure the total count and categorization are updated in `wiki/index.md`.
5. Run the validation script `python3 scripts/validate_wiki.py` to maintain database integrity.

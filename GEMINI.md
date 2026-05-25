# Gemini Developer Guide

This file outlines instructions, commands, and rules for Google Gemini-based coding agents working in this repository.

## Commands

### Run Wiki Validation
Always run the validation script after modifying any files in the `wiki/` or `skills/` directories, or adding new files. This checks for frontmatter correctness, missing skills, duplicate declarations, and broken links:
```bash
python3 scripts/validate_wiki.py
```

## Ingestion Workflows
When you are tasked with processing raw inputs from the community:
1. Scan `raw_inputs/` for new files (e.g. `.json`, `.md`, `.txt`).
2. Read the existing files in `wiki/` to check for overlapping content or duplicates.
3. If the skill is brand new:
   - **Create the Metadata Wiki Page**: Create a file `wiki/{new-skill-id}.md`. Ensure you write the mandatory frontmatter:
     ```yaml
     id: new-skill-id
     title: Human Readable Title
     category: Category Name
     created_at: YYYY-MM-DD
     updated_at: YYYY-MM-DD
     difficulty: Beginner | Intermediate | Advanced
     tags:
       - tag1
       - tag2
     ```
     Draft the content covering Overview, Prerequisites, Core Concepts, In-Depth Guide, and Verification.
   - **Create the Executable Agent Skill**: Create a directory `skills/{new-skill-id}/` and a file `skills/{new-skill-id}/SKILL.md`. Ensure you write the minimal standard frontmatter:
     ```yaml
     ---
     name: new-skill-id
     description: Brief agent-focused trigger description (<200 characters).
     ---
     ```
     Draft the concise prompt/instructions that the AI agent should execute.
   - **Update Catalog**: Update `wiki/index.md` (increment the total count, add to the categorization list, and link the new skill page).
4. If it augments an existing skill:
   - Edit the relevant wiki page in `wiki/`.
   - Update the `updated_at` date in its frontmatter.
   - If prompt/instructions changed, edit the corresponding `skills/{skill-id}/SKILL.md` file.
5. Delete or move the processed file from `raw_inputs/` to avoid double-processing.
6. Run `python3 scripts/validate_wiki.py` to ensure everything compiles cleanly.

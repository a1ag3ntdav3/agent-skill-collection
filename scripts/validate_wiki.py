#!/usr/bin/env python3
import json
import os
import re
import sys

def extract_description(body):
    # Find ## Overview and get the paragraph following it (up to double newline or next heading)
    match = re.search(r'##\s+Overview\r?\n+(.*?)(?:\r?\n\r?\n|\r?\n+##|\r?\n+$)', body, re.DOTALL)
    if match:
        desc = match.group(1).strip()
        # Replace markdown links [Label](url) with Label
        desc = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', desc)
        # Replace Obsidian links [[url|Label]] or [[url]]
        desc = re.sub(r'\[\[([^\|\]]+)(?:\|([^\]]+))?\]\]', lambda m: m.group(2) if m.group(2) else m.group(1), desc)
        # Collapse multiple spaces and strip newlines
        desc = re.sub(r'\s+', ' ', desc)
        return desc
    return ""

# Color output helpers
def print_green(text):
    print(f"\033[92m{text}\033[0m")

def print_red(text):
    print(f"\033[91m{text}\033[0m")

def print_yellow(text):
    print(f"\033[93m{text}\033[0m")

def parse_frontmatter(content):
    # Match frontmatter block: starts with --- and ends with ---
    match = re.match(r'^---\r?\n(.*?)\r?\n---\r?\n(.*)', content, re.DOTALL)
    if not match:
        return None, content
    
    frontmatter_text = match.group(1)
    body = match.group(2)
    
    data = {}
    lines = frontmatter_text.splitlines()
    current_key = None
    
    for line in lines:
        if not line.strip():
            continue
        # Check if it is a list item
        list_match = re.match(r'^\s*-\s*(.*)', line)
        if list_match and current_key is not None:
            if not isinstance(data[current_key], list):
                data[current_key] = []
            val = list_match.group(1).strip()
            # Remove optional wrapping quotes
            if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
                val = val[1:-1]
            data[current_key].append(val)
        else:
            kv_match = re.match(r'^([^:]+):\s*(.*)', line)
            if kv_match:
                key = kv_match.group(1).strip()
                val = kv_match.group(2).strip()
                if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
                    val = val[1:-1]
                data[key] = val
                current_key = key
            else:
                pass
                
    return data, body

def validate_wiki(workspace_dir):
    skills_dir = os.path.join(workspace_dir, "skills")
    if not os.path.exists(skills_dir):
        print_red(f"Error: 'skills' directory not found at {skills_dir}")
        return False

    index_path = os.path.join(skills_dir, "index.md")
    if not os.path.exists(index_path):
        print_red(f"Error: index.md not found at {index_path}")
        return False

    # Get list of skill files (exclude index.md)
    skill_files = [f for f in os.listdir(skills_dir) if f.endswith(".md") and f != "index.md"]
    skill_ids = set()
    errors = 0
    manifest_data = []

    required_fields = {"id", "title", "category", "created_at", "updated_at", "difficulty", "tags"}

    print(f"Scanning {len(skill_files)} skill pages...")

    # First pass: parse frontmatter and check filenames
    parsed_skills = {}
    for filename in sorted(skill_files):
        filepath = os.path.join(skills_dir, filename)
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            print_red(f"Error reading {filename}: {e}")
            errors += 1
            continue

        frontmatter, body = parse_frontmatter(content)
        if not frontmatter:
            print_red(f"Error in {filename}: Missing or malformed YAML frontmatter. Must start and end with '---'")
            errors += 1
            continue

        # Check required fields
        missing_fields = required_fields - set(frontmatter.keys())
        if missing_fields:
            print_red(f"Error in {filename}: Missing required frontmatter fields: {', '.join(missing_fields)}")
            errors += 1
            continue

        skill_id = frontmatter["id"]
        
        # Verify file name matches ID
        expected_filename = f"{skill_id}.md"
        if filename != expected_filename:
            print_red(f"Error in {filename}: File name must match ID '{skill_id}'. Expected '{expected_filename}' but found '{filename}'")
            errors += 1
            continue

        # Check tags is a list
        if "tags" in frontmatter and not isinstance(frontmatter["tags"], list):
            print_red(f"Error in {filename}: 'tags' must be a YAML list (sequence).")
            errors += 1

        skill_ids.add(skill_id)
        parsed_skills[skill_id] = (filepath, frontmatter, body)

        description = extract_description(body)
        manifest_data.append({
            "id": skill_id,
            "title": frontmatter.get("title", ""),
            "description": description,
            "category": frontmatter.get("category", ""),
            "difficulty": frontmatter.get("difficulty", ""),
            "tags": frontmatter.get("tags", []),
            "filePath": f"skills/{filename}"
        })

    # Second pass: Check links inside skill pages
    print("Checking inter-skill links...")
    for skill_id, (filepath, frontmatter, body) in parsed_skills.items():
        filename = f"{skill_id}.md"
        
        # Match standard Markdown links targetting a local .md file, e.g. [Git Basics](git-basics.md)
        # Allows optional leading dot-slash ./ or file name, and optional #anchor link
        md_links = re.findall(r'\[[^\]]+\]\(\s*\.?/?([^)#\s]+\.md)(?:#[^)]*)?\s*\)', body)
        
        # Match Obsidian style links, e.g. [[git-basics]] or [[git-basics|Git Basics]]
        obsidian_links = re.findall(r'\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]', body)

        all_linked_targets = md_links + obsidian_links

        for target in all_linked_targets:
            # Normalize target to target_id (removing .md extension if present)
            target_id = target[:-3] if target.endswith(".md") else target
            target_id = target_id.strip()

            if target_id not in skill_ids:
                print_red(f"Error in {filename}: Broken link to target '{target}' (resolved to ID '{target_id}'). File does not exist.")
                errors += 1

    # Validate index.md
    print("Validating skills/index.md...")
    try:
        with open(index_path, "r", encoding="utf-8") as f:
            index_content = f.read()
    except Exception as e:
        print_red(f"Error reading index.md: {e}")
        return False

    # Check if index lists the skills
    for skill_id in skill_ids:
        # Check standard markdown link to skill_id.md
        md_pattern = rf'\[[^\]]+\]\(\s*\.?/?{skill_id}\.md(?:#[^)]*)?\s*\)'
        # Check Obsidian link
        obsidian_pattern = rf'\[\[\s*{skill_id}(?:#[^\]|]*)?(?:\|[^\]]*)?\s*\]\]'
        
        if not (re.search(md_pattern, index_content) or re.search(obsidian_pattern, index_content)):
            print_yellow(f"Warning in index.md: Skill '{skill_id}' is not linked. Adding links is highly recommended.")

    # Check total count indicator in index.md
    # Look for "Total Skills: X" or similar pattern (case insensitive)
    count_match = re.search(r'total\s+skills\s*:\s*(\d+)', index_content, re.IGNORECASE)
    if count_match:
        declared_count = int(count_match.group(1))
        actual_count = len(skill_ids)
        if declared_count != actual_count:
            print_red(f"Error in index.md: Declared 'Total Skills: {declared_count}' but found {actual_count} skill files in the database.")
            errors += 1
    else:
        print_yellow("Warning: No 'Total Skills: <number>' statistic found in index.md. Adding this is recommended for tracking.")

    # Report results
    if errors == 0:
        manifest_path = os.path.join(skills_dir, "manifest.json")
        try:
            with open(manifest_path, "w", encoding="utf-8") as f:
                json.dump({"skills": manifest_data}, f, indent=2)
            print_green(f"Manifest successfully updated at {manifest_path}")
        except Exception as e:
            print_red(f"Error writing manifest.json: {e}")
            errors += 1

    if errors == 0:
        print_green(f"\nSuccess! All {len(skill_ids)} skills validated successfully. No errors found.")
        return True
    else:
        print_red(f"\nValidation failed with {errors} errors.")
        return False

if __name__ == "__main__":
    # Determine workspace root (parent of scripts directory)
    script_dir = os.path.dirname(os.path.realpath(__file__))
    workspace_root = os.path.dirname(script_dir)
    
    success = validate_wiki(workspace_root)
    sys.exit(0 if success else 1)

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
    wiki_dir = os.path.join(workspace_dir, "wiki")
    skills_dir = os.path.join(workspace_dir, "skills")
    
    if not os.path.exists(wiki_dir):
        print_red(f"Error: 'wiki' directory not found at {wiki_dir}")
        return False
        
    if not os.path.exists(skills_dir):
        print_red(f"Error: 'skills' directory not found at {skills_dir}")
        return False

    index_path = os.path.join(wiki_dir, "index.md")
    if not os.path.exists(index_path):
        print_red(f"Error: index.md not found at {index_path}")
        return False

    # Get list of wiki pages (exclude index.md)
    wiki_files = [f for f in os.listdir(wiki_dir) if f.endswith(".md") and f != "index.md"]
    skill_ids = set()
    errors = 0
    manifest_data = []

    required_wiki_fields = {"id", "title", "category", "created_at", "updated_at", "difficulty", "tags"}

    print(f"Scanning {len(wiki_files)} wiki pages...")

    # First pass: parse wiki frontmatter, verify executable skill directories & SKILL.md files
    parsed_wikis = {}
    for filename in sorted(wiki_files):
        filepath = os.path.join(wiki_dir, filename)
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            print_red(f"Error reading wiki file {filename}: {e}")
            errors += 1
            continue

        frontmatter, body = parse_frontmatter(content)
        if not frontmatter:
            print_red(f"Error in wiki file {filename}: Missing or malformed YAML frontmatter. Must start and end with '---'")
            errors += 1
            continue

        # Check required wiki fields
        missing_fields = required_wiki_fields - set(frontmatter.keys())
        if missing_fields:
            print_red(f"Error in wiki file {filename}: Missing required frontmatter fields: {', '.join(missing_fields)}")
            errors += 1
            continue

        skill_id = frontmatter["id"]
        
        # Verify file name matches ID
        expected_filename = f"{skill_id}.md"
        if filename != expected_filename:
            print_red(f"Error in wiki file {filename}: File name must match ID '{skill_id}'. Expected '{expected_filename}' but found '{filename}'")
            errors += 1
            continue

        # Check tags is a list
        if "tags" in frontmatter and not isinstance(frontmatter["tags"], list):
            print_red(f"Error in wiki file {filename}: 'tags' must be a YAML list (sequence).")
            errors += 1

        skill_ids.add(skill_id)
        parsed_wikis[skill_id] = (filepath, frontmatter, body)

        # NOW, check matching executable skill folder skills/{skill_id}/SKILL.md
        exec_skill_dir = os.path.join(skills_dir, skill_id)
        if not os.path.exists(exec_skill_dir):
            print_red(f"Error for skill '{skill_id}': Executable directory '{exec_skill_dir}' not found.")
            errors += 1
            continue

        skill_md_path = os.path.join(exec_skill_dir, "SKILL.md")
        if not os.path.exists(skill_md_path):
            print_red(f"Error for skill '{skill_id}': 'SKILL.md' file not found at '{skill_md_path}'.")
            errors += 1
            continue

        # Validate executable SKILL.md
        try:
            with open(skill_md_path, "r", encoding="utf-8") as sf:
                skill_content = sf.read()
        except Exception as e:
            print_red(f"Error reading '{skill_md_path}': {e}")
            errors += 1
            continue

        skill_fm, skill_body = parse_frontmatter(skill_content)
        if not skill_fm:
            print_red(f"Error in executable '{skill_md_path}': Missing or malformed YAML frontmatter.")
            errors += 1
            continue

        # Check name and description in SKILL.md
        if "name" not in skill_fm:
            print_red(f"Error in executable '{skill_md_path}': Missing required field 'name' in frontmatter.")
            errors += 1
        elif skill_fm["name"] != skill_id:
            print_red(f"Error in executable '{skill_md_path}': 'name' in frontmatter must match skill ID '{skill_id}', found '{skill_fm['name']}'.")
            errors += 1

        exec_desc = ""
        if "description" not in skill_fm:
            print_red(f"Error in executable '{skill_md_path}': Missing required field 'description' in frontmatter.")
            errors += 1
        else:
            exec_desc = skill_fm["description"]
            if len(exec_desc) > 200:
                print_red(f"Error in executable '{skill_md_path}': 'description' length exceeds 200 characters (found {len(exec_desc)}).")
                errors += 1

        manifest_data.append({
            "id": skill_id,
            "title": frontmatter.get("title", ""),
            "description": exec_desc if exec_desc else extract_description(body),
            "category": frontmatter.get("category", ""),
            "difficulty": frontmatter.get("difficulty", ""),
            "tags": frontmatter.get("tags", []),
            "wikiPath": f"wiki/{filename}",
            "filePath": f"skills/{skill_id}/SKILL.md"
        })

    # Second pass: Check links inside wiki pages
    print("Checking inter-wiki links...")
    for skill_id, (filepath, frontmatter, body) in parsed_wikis.items():
        filename = f"{skill_id}.md"
        
        # Match standard Markdown links targetting a local .md file, e.g. [Git Basics](git-basics.md)
        md_links = re.findall(r'\[[^\]]+\]\(\s*\.?/?([^)#\s]+\.md)(?:#[^)]*)?\s*\)', body)
        
        # Match Obsidian style links, e.g. [[git-basics]] or [[git-basics|Git Basics]]
        obsidian_links = re.findall(r'\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]', body)

        all_linked_targets = md_links + obsidian_links

        for target in all_linked_targets:
            # Normalize target to target_id (removing .md extension if present)
            target_id = target[:-3] if target.endswith(".md") else target
            target_id = target_id.strip()

            if target_id not in skill_ids:
                print_red(f"Error in wiki file {filename}: Broken link to target '{target}' (resolved to ID '{target_id}'). File does not exist.")
                errors += 1

    # Validate index.md
    print("Validating wiki/index.md...")
    try:
        with open(index_path, "r", encoding="utf-8") as f:
            index_content = f.read()
    except Exception as e:
        print_red(f"Error reading index.md: {e}")
        return False

    # Check if index lists the skills
    for skill_id in skill_ids:
        md_pattern = rf'\[[^\]]+\]\(\s*\.?/?{skill_id}\.md(?:#[^)]*)?\s*\)'
        obsidian_pattern = rf'\[\[\s*{skill_id}(?:#[^\]|]*)?(?:\|[^\]]*)?\s*\]\]'
        
        if not (re.search(md_pattern, index_content) or re.search(obsidian_pattern, index_content)):
            print_yellow(f"Warning in index.md: Wiki page '{skill_id}' is not linked. Adding links is highly recommended.")

    # Check total count indicator in index.md
    count_match = re.search(r'total\s+skills\s*:\s*(\d+)', index_content, re.IGNORECASE)
    if count_match:
        declared_count = int(count_match.group(1))
        actual_count = len(skill_ids)
        if declared_count != actual_count:
            print_red(f"Error in index.md: Declared 'Total Skills: {declared_count}' but found {actual_count} wiki pages in the database.")
            errors += 1
    else:
        print_yellow("Warning: No 'Total Skills: <number>' statistic found in index.md.")

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

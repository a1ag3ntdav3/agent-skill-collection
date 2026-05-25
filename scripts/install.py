#!/usr/bin/env python3
import argparse
import json
import os
import urllib.request
import urllib.error
import sys

DEFAULT_REPO_RAW_URL = "https://raw.githubusercontent.com/georg/intelligent-planck/main/"

def load_manifest(local_path, remote_url):
    # Try local first
    if os.path.exists(local_path):
        try:
            with open(local_path, 'r', encoding='utf-8') as f:
                return json.load(f), False
        except Exception as e:
            print(f"Error reading local manifest: {e}")
            sys.exit(1)
            
    # Try remote
    url = remote_url.rstrip('/') + "/skills/manifest.json"
    print(f"Local manifest not found. Fetching from remote: {url}")
    try:
        with urllib.request.urlopen(url) as response:
            return json.loads(response.read().decode('utf-8')), True
    except urllib.error.URLError as e:
        print(f"Error fetching remote manifest: {e}")
        print("Please check your internet connection or repository URL.")
        sys.exit(1)

def install_skill(skill, dest_dir, local_repo_dir, remote_url, is_remote):
    os.makedirs(dest_dir, exist_ok=True)
    filename = os.path.basename(skill['filePath'])
    dest_path = os.path.join(dest_dir, filename)
    
    if is_remote:
        src_url = remote_url.rstrip('/') + "/" + skill['filePath']
        print(f"Downloading {skill['title']} from {src_url}...")
        try:
            with urllib.request.urlopen(src_url) as response:
                content = response.read()
            with open(dest_path, 'wb') as f:
                f.write(content)
            print(f"Successfully installed to {dest_path}")
        except urllib.error.URLError as e:
            print(f"Error downloading skill: {e}")
            sys.exit(1)
    else:
        src_path = os.path.join(local_repo_dir, skill['filePath'])
        print(f"Copying {skill['title']} from {src_path}...")
        try:
            with open(src_path, 'rb') as src, open(dest_path, 'wb') as dest:
                dest.write(src.read())
            print(f"Successfully installed to {dest_path}")
        except Exception as e:
            print(f"Error copying skill: {e}")
            sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="AI Agent Skill Installer CLI")
    parser.add_argument('--list', action='store_true', help="List all available skills")
    parser.add_argument('--search', type=str, help="Search skills by title, tags, category, or description")
    parser.add_argument('--install', type=str, help="Install specific skill by ID")
    parser.add_argument('--dest', type=str, help="Destination directory for installed skill (e.g. .claude/skills/)")
    parser.add_argument('--repo', type=str, default=DEFAULT_REPO_RAW_URL, help="Base URL of GitHub raw repository content")
    
    args = parser.parse_args()
    
    # Paths
    script_dir = os.path.dirname(os.path.realpath(__file__))
    workspace_root = os.path.dirname(script_dir)
    local_manifest = os.path.join(workspace_root, "skills", "manifest.json")
    
    # Load manifest
    manifest, is_remote = load_manifest(local_manifest, args.repo)
    skills = manifest.get("skills", [])
    
    if args.list:
        print(f"\nAvailable Skills ({len(skills)}):")
        print("=" * 60)
        for s in skills:
            print(f"ID:         {s['id']}")
            print(f"Title:      {s['title']}")
            print(f"Category:   {s['category']}")
            print(f"Difficulty: {s['difficulty']}")
            print(f"Tags:       {', '.join(s['tags'])}")
            print(f"Description:{s['description']}")
            print("-" * 60)
        return

    if args.search:
        query = args.search.lower()
        results = []
        for s in skills:
            if (query in s['id'].lower() or 
                query in s['title'].lower() or 
                query in s['category'].lower() or 
                query in s['description'].lower() or 
                any(query in t.lower() for t in s['tags'])):
                results.append(s)
        
        print(f"\nSearch Results for '{args.search}' ({len(results)} found):")
        print("=" * 60)
        for s in results:
            print(f"ID:         {s['id']}")
            print(f"Title:      {s['title']}")
            print(f"Category:   {s['category']}")
            print(f"Difficulty: {s['difficulty']}")
            print(f"Tags:       {', '.join(s['tags'])}")
            print(f"Description:{s['description']}")
            print("-" * 60)
        return

    if args.install:
        skill_id = args.install
        target_skill = None
        for s in skills:
            if s['id'] == skill_id:
                target_skill = s
                break
                
        if not target_skill:
            print(f"Error: Skill ID '{skill_id}' not found in manifest.")
            sys.exit(1)
            
        dest = args.dest
        if not dest:
            # Try to auto-detect target directory (e.g. .claude/skills in current working directory)
            dest = os.path.join(os.getcwd(), ".claude", "skills")
            print(f"Destination --dest not specified. Defaulting to: {dest}")
            
        install_skill(target_skill, dest, workspace_root, args.repo, is_remote)
        return
        
    parser.print_help()

if __name__ == "__main__":
    main()

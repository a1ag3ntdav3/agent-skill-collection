---
id: git-basics
title: Git Basics
category: Version Control
created_at: 2026-05-24
updated_at: 2026-05-24
difficulty: Beginner
tags:
  - git
  - vcs
  - collaboration
---

# Git Basics

## Overview
Git is a distributed version control system designed to handle everything from small to very large projects with speed and efficiency. This skill covers the fundamental workflow required to initialize a repository, track changes, stage modifications, and commit revisions.

## Prerequisites
No prior software skills are required, though familiarity with using a terminal/command-line interface is highly recommended.

## Core Concepts
- **Working Directory**: The local directory where you are editing your project files.
- **Staging Area (Index)**: A file maintained by Git that contains information about what files and changes will go into your next commit.
- **Local Repository**: The `.git` directory containing all committed snapshots of your project.
- **Commit**: A cryptographic snapshot of your project's state. Each commit is identified by a SHA-1 hash and records the author, date, and commit message.

## In-Depth Guide
### Initializing a Repository
To start tracking a project, navigate to the folder in your terminal and run:
```bash
git init
```
This creates a hidden `.git` directory in your workspace.

### Checking Status
To see which files Git is tracking and which have modifications:
```bash
git status
```

### Staging Changes
Add files to the staging area to prepare them for a commit:
```bash
# Stage a specific file
git add filename.txt

# Stage all changes in the current directory
git add .
```

### Committing Changes
Commit the staged snapshot to the local repository history:
```bash
git commit -m "Your descriptive commit message"
```

## Verification
To verify that you have successfully set up and used Git in your repository:
1. Run `git status` and verify it reports "nothing to commit, working tree clean".
2. Run `git log --oneline` to confirm that your commits are recorded in the repository history.

---
id: prompt-engineering
title: Prompt Engineering
category: LLM Interactions
created_at: 2026-05-24
updated_at: 2026-05-24
difficulty: Intermediate
tags:
  - prompt
  - llm
  - instruction-following
---

# Prompt Engineering

## Overview
Prompt Engineering is the practice of structuring text inputs to large language models (LLMs) to ensure they produce the desired output. High-quality prompts combine context, instructions, input data, and formatting constraints to minimize hallucinations and maximize accuracy.

## Prerequisites
- Basic understanding of how LLMs generate text.
- [Git Basics](git-basics.md) (highly recommended for tracking prompt iterations and versioning prompts).

## Core Concepts
- **System Instructions**: Pre-conditioning the model's behavior, style, and constraints.
- **Few-Shot Prompting**: Providing a few high-quality input-output examples inside the prompt to guide the model's output format.
- **Chain of Thought (CoT)**: Directing the LLM to think step-by-step before answering, which greatly improves reasoning accuracy.
- **Role Prompting**: Assigning a specific persona to the LLM (e.g., "You are an expert systems engineer").

## In-Depth Guide

### Structural Anatomy of a Prompt
A robust prompt typically contains four main parts:
1. **Instruction**: A clear statement of the task the model should perform.
2. **Context**: Background information or constraints.
3. **Input Data**: The text, codebase, or content to process.
4. **Output Indicator**: A specification of the format of the output (e.g., JSON, Markdown tables).

### Example: Chain of Thought + Few-Shot JSON Extraction
```
You are a code compliance agent. Parse the following git diff and extract any potential security flaws.

First, explain your thinking step-by-step.
Finally, output a JSON array of issues found, following this schema:
[{"file": "filename", "line": 12, "flaw": "description"}]

---
Input Diff:
...
```

### Versioning Prompts
For professional LLM applications, it is vital to track prompt changes over time. Always store your prompts in a version-controlled repository using [[git-basics|Git Basics]]. This allows you to revert to older, working prompt variations if updates cause regressions.

## Verification
To verify this skill:
1. Write a prompt using Chain of Thought and evaluate if the model outputs its reasoning steps prior to the answer.
2. Verify that formatting instructions (e.g., JSON or Markdown) are strictly adhered to by the model across multiple test queries.

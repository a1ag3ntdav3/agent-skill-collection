---
name: prompt-chaining
description: Decompose complex tasks into a sequential pipeline of LLM calls, with optional programmatic validation between steps.
---

# Prompt Chaining

Use this skill to implement the Prompt Chaining pattern, breaking a complex prompt down into discrete, sequential LLM calls where the output of each step feeds the next.

## Instructions
1. **Decompose**: Split a complex, multi-step task into simpler sub-tasks.
2. **Chain**: Design the sequence of LLM calls, mapping the output of step `N` as part of the context/input for step `N+1`.
3. **Validate**: Insert programmatic checks (validation, filtering, schema checks) between steps to intercept and correct errors early.
4. **Prune**: Keep the context passed to subsequent steps clean and concise.

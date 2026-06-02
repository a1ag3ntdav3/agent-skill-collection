---
name: piv-loop
description: Plan-Implement-Validate (PIV) Loop to bring discipline to agentic coding and avoid vibe coding.
---

# Plan-Implement-Validate Loop (PIV Loop)

Use this skill when executing coding tasks or building software features.

## Instructions
1. **Plan**:
   - Prime your context by reading the workspace structure, target files, and requirements.
   - Output a step-by-step implementation plan and a clear validation strategy (e.g., tests, compile commands, or scripts to run).
2. **Context Reset**:
   - Advise the user to clear/reset the chat history or do it programmatically (if supported) to avoid context bloat before coding.
3. **Implement**:
   - Focus execution strictly on the plan. Refrain from making extraneous changes outside the plan's scope.
4. **Validate**:
   - Execute the validation commands.
   - Review linter and test outputs.
   - If validation fails, loop back to Planning/Implementation to fix the issue.

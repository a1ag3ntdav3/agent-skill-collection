---
name: human-in-the-loop
description: Orchestration pattern requiring explicit human verification or modification for critical actions.
---

# Human-in-the-Loop

Use this skill when executing operations with high impact or risk, ensuring the user has direct control and sign-off.

## Instructions
1. **Identify**: Monitor actions for high-risk flags (e.g. command execution, file deletion, data modification).
2. **Halt**: Pause execution immediately; do not proceed automatically.
3. **Present**: Render the proposed action, parameters, and rationale clearly.
4. **Iterate**: Listen for approval, rejection, or instructions for changes, applying modifications before execution.

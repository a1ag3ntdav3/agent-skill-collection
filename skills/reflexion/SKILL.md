---
name: reflexion
description: Execute the Reflexion loop to iteratively refine agent outputs using self-critique and persistent failure memory.
---

# Reflexion

Use this skill when you need to solve complex problems where early attempts may fail, and you must track your errors, reflect on them, and correct them iteratively.

## Instructions
1. **Attempt**: Generate a solution (code, plan, or analysis) for the given task.
2. **Test**: Run verification tests, compile the code, or review the output against instructions.
3. **Reflect**: If errors or discrepancies occur, write a brief self-reflection in your prompt state:
   - Identify the exact line or logic that failed.
   - Explain why it failed.
   - Propose a concrete corrective action for the next run.
4. **Retry**: In the next attempt, explicitly list your past reflections and modify the solution accordingly.
5. **Stop**: Halt execution once the solution compiles/passes tests successfully, or after 3 unsuccessful trials to request user guidance.

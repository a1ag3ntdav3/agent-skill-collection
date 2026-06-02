---
name: tool-maker
description: Autonomously create, debug, test, and register custom code tools to solve specific recurring tasks and reuse them to save token costs and improve accuracy.
---

# Tool Maker

Use this skill to implement the Tool Maker (LATM) pattern, creating specialized, tested code functions to handle complex or repetitive operations rather than relying on raw LLM text generation.

## Instructions
1. **Identify**: Determine if a sub-task requires a custom procedural calculation, parsing, or API call that is best solved with a code tool.
2. **Create**: Write a clean, reusable Python function (or script) to perform the task.
3. **Verify**: Run tests or execute the code with sample inputs to ensure it works correctly and handles edge cases.
4. **Register**: Store the validated function in the local tool repository or registry.
5. **Use**: Call the registered tool to execute the task.

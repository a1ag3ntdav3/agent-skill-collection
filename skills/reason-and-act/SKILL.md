---
name: reason-and-act
description: Reusable execution loop alternating between reasoning (Thought) and tool execution (Action / Observation).
---

# Reason and Act

Use this skill to implement the ReAct pattern, allowing agents to systematically reason before selecting and executing tools in an iterative loop.

## Instructions
1. **Thought**: Analyze the current task state, user intent, and available context.
2. **Action**: Choose the appropriate tool and call it with precise, well-formed arguments.
3. **Observation**: Read and parse the tool's response to update the internal state.
4. **Iterate**: Repeat the Thought-Action-Observation cycle until the task is complete.

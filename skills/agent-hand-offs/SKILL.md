---
name: agent-hand-offs
description: Lightweight multi-agent coordination pattern where agents transfer execution control dynamically.
---

# Agent Hand-offs

Use this skill when you need to coordinate multi-agent teams without a central orchestrator, passing execution context dynamically between specialized agents.

## Instructions
1. **Agent Definition**: Set up specialized agents with clear, narrow instructions and custom system prompts.
2. **Handoff Implementation**: Expose routing tools that allow an agent to transition execution to another agent.
3. **Context Transfer**: Ensure all conversation history and active state variables are bundled and sent with the hand-off.
4. **Triage**: Implement an entry-point agent to classify the task and hand off execution immediately.

---
name: swarm-orchestration
description: Orchestrate decentralized teams of micro-agents that dynamically hand off control and coordinate task execution through fluid, peer-to-peer routing.
---

# Swarm Orchestration

Use this skill when designing or executing multi-agent workflows that require flexible, peer-to-peer coordination and dynamic role switching.

## Instructions
1. **Define micro-agents**: Identify specialized, single-purpose roles required for the task.
2. **Setup shared context**: Establish a unified context structure to carry the execution state.
3. **Execute peer transitions**: Have agents perform their tasks and return handoff directions to target peers.
4. **Enforce loop detection**: Monitor transitions to prevent cyclic routing loops.
5. **Collect outputs**: Terminate swarm execution when an agent returns a final completed result.

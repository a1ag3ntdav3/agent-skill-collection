---
name: flow-engineering
description: Construct deterministic agent control flows and state machines for predictable execution paths.
---

# Flow Engineering

Use this skill when designing multi-step agent pipelines requiring strict compliance, loop retries, input/output validation checks, or custom execution paths.

## Instructions
1. **Define State**: Construct a centralized state schema detailing the data variables shared across nodes.
2. **Implement Nodes**: Code separate node functions for each discrete processing step (e.g. prompt, check, validation). Node execution must only read from and write to the shared state.
3. **Set Up Routing**: Implement conditional routing logic to navigate between nodes based on state values.
4. **Compile Graph**: Register nodes and routing edges into a directed acyclic or cyclic graph structure.
5. **Execute Workflow**: Start execution from the designated entry point, passing state through the graph until an end node is reached.

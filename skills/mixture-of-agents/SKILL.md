---
name: mixture-of-agents
description: Layered multi-agent pattern that runs multiple LLM calls in parallel and aggregates their outputs across sequential steps to improve response quality.
---

# Mixture of Agents

Use this skill when dealing with highly complex, creative, or reasoning-intensive tasks that benefit from combining multiple perspectives or model outputs.

## Instructions
1. **Parallel Execution**: Spawn multiple proposer LLM instances (or different models) to generate initial draft responses for the user query.
2. **Collect Drafts**: Gather all generated responses and format them clearly as input for the next layer.
3. **Aggregate & Refine**: Pass the gathered responses along with the original query to an aggregator LLM.
4. **Synthesize**: Instruct the aggregator to identify commonalities, resolve contradictions, and synthesize a single superior final response.

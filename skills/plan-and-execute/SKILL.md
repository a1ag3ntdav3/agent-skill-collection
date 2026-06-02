---
name: plan-and-execute
description: Decouple planning from execution by generating a step-by-step plan first, executing each step sequentially, and dynamically re-planning if errors occur.
---

# Plan-and-Execute

Use this skill to implement the Plan-and-Execute pattern, decomposing a complex objective into sequential tasks, executing them with specialized sub-agents or tools, and adjusting the plan dynamically based on execution outcomes.

## Instructions
1. **Plan**: Analyze the main objective and decompose it into a structured sequence of sub-tasks.
2. **Execute**: Execute the sub-tasks one by one. Use specialized tools or sub-agents for each execution step.
3. **Monitor & Re-plan**: After each step's execution, observe the output. If a step fails or new information changes the requirements, update the remaining plan.
4. **Finalize**: Deliver the combined result once all plan items are successfully completed.

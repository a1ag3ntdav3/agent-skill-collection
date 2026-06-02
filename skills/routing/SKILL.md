---
name: routing
description: Classification-based redirection of tasks to specialized prompts, models, or sub-agents.
---

# Routing

Use this skill to implement the Routing pattern, acting as a traffic controller that dynamically classifies input queries to send them to the most appropriate downstream handler or sub-agent.

## Instructions
1. **Classify**: Analyze the incoming user input's intent, complexity, and domain.
2. **Map**: Select the specialized downstream handler, prompt, or model best suited for the classified intent.
3. **Redirect**: Pass the input and accumulated context to the selected downstream handler.
4. **Fallback**: Ensure a default fallback route exists for ambiguous, out-of-domain, or failed classifications.

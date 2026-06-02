---
name: model-context-protocol
description: Standardized client-server framework for LLMs to securely query resources, prompts, and tools.
---

# Model Context Protocol

Use this skill to integrate and coordinate with external MCP servers, discovering and invoking standardized tools and resources.

## Instructions
1. **Discovery**: Read the available tools, prompts, and resources exposed by the MCP servers.
2. **Matching**: Analyze the task requirements and match them against the active tool schemas.
3. **Execution**: Invoke MCP tools using JSON-RPC 2.0 parameters. Do not exceed the required argument types.
4. **Context Loading**: Retrieve files, logs, or APIs through standard MCP resource URIs.

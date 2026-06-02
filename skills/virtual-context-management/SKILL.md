---
name: virtual-context-management
description: Manage LLM context window constraints using virtual memory paging, core memory edits, and episodic/archival data retrievals.
---

# Virtual Context Management

Use this skill when managing long-running agent execution tasks, multi-session chat histories, or very large document retrieval sets that exceed native LLM context window limits.

## Instructions
1. **Load Core Memory**: Initialize the active system prompt context with critical user profiles, agent persona, and current task focus.
2. **Monitor Context Size**: Keep track of the token usage in the active message history.
3. **Page Out (Evict)**: When context limits are approached, compress the oldest dialog threads, write them to Episodic Memory storage, and delete them from active context.
4. **Page In (Retrieve)**: When details from past conversations or archival documents are required, use vector search or SQL queries to retrieve them from Episodic or Archival storage into the active core memory block.
5. **Update Core Memory**: Dynamically edit core memory sections when persistent facts or user preferences change.

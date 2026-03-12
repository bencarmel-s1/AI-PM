# MCP Configuration

## What is MCP?

MCP (Model Context Protocol) is an open standard that lets AI assistants like Windsurf connect to external tools and data sources. Instead of copy-pasting content into a chat, MCP gives the AI a live connection — it can read, search, and act on real data directly.

For a PM, this means you can ask your AI assistant things like "what are my open Jira tickets this sprint?" or "summarize the Confluence page on our Q3 roadmap" without leaving your editor.

MCP servers are configured in Windsurf's settings. Each server connects to one external system and exposes a set of actions the AI can use.

---

## Available configurations

| Folder | What it connects to |
|---|---|
| [jira-mcp-integration-for-windsurf](./jira-mcp-integration-for-windsurf/) | Jira and Confluence (Atlassian) |

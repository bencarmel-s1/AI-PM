# Template: Plugin Packaging Guide

## Before you start

**What you need:** A working set of Claude Code skills, agents, or commands in a `.claude/` folder that you want to distribute as a single installable package.

**What this covers:** Claude Code's plugin system lets you bundle skills, agents, hooks, and MCP servers into a shareable, versioned package. This guide explains the system and walks through how to convert this repo's assets into a plugin.

**Why this matters:** Instead of asking every PM to clone a git repo and manage updates manually, a plugin gives you one-command installation, versioned updates, and the option to publish to the Claude Code marketplace.

---

## How to use

```
Help me package the skills and agents in this repo as a Claude Code plugin using @plugin-packaging.md as a guide.
```

---

## What is a Claude Code Plugin?

A plugin is a bundled collection of Claude Code assets — skills, agents, commands, hooks, and MCP server configurations — packaged with a manifest file (`plugin.json`) that describes what's included, how to install it, and what version it is.

Think of it like an npm package for Claude Code: instead of copying files manually, users install a plugin and get everything wired up automatically.

### What a plugin can contain

| Asset Type | Description | Example from this repo |
|---|---|---|
| Skills | Single-purpose knowledge frameworks | `customer-feedback-synthesis`, `backlog-prioritization` |
| Agents | Specialist sub-agents with personas | `engineer`, `executive`, `user-researcher` |
| Commands | Multi-step slash command workflows | `/prd-creation`, `/launch-pack` |
| Hooks | Automated triggers for quality gates | (not yet in this repo — see `hooks-for-pms.md`) |
| MCP Servers | External tool connections | Jira MCP integration |

---

## Plugin Manifest Structure

The manifest file (`plugin.json`) lives at the root of your plugin and describes everything inside. Here's what one would look like for this repo:

```json
{
  "name": "ai-pm-toolkit",
  "version": "1.0.0",
  "description": "Product management skills, agents, and workflows for Claude Code",
  "author": "SentinelOne PM Team",
  "license": "MIT",
  "claude_code_version": ">=1.0.0",
  "assets": {
    "skills": [
      "skills/customer-feedback-synthesis",
      "skills/customer-call-questionnaire",
      "skills/strategic-decision-validation",
      "skills/backlog-prioritization",
      "skills/todo-prioritization",
      "skills/multi-agent-review",
      "skills/stakeholder-communication"
    ],
    "agents": [
      "agents/engineer",
      "agents/executive",
      "agents/user-researcher"
    ],
    "commands": [
      "commands/prd-creation",
      "commands/feature-request-discovery",
      "commands/data-analysis",
      "commands/launch-pack",
      "commands/product-strategy"
    ]
  },
  "dependencies": {},
  "keywords": ["product-management", "pm", "prd", "strategy", "research"]
}
```

> **Note:** Do not create this file yet — the manifest format may evolve. This example documents the current structure so you understand the mapping.

---

## Converting This Repo to a Plugin

If the team decides to publish, here's how the repo's `.claude/` assets map to plugin components:

### Step 1: Audit your assets

List everything in `.claude/`:

```
Show me all skills, agents, and commands in .claude/ with their descriptions.
```

### Step 2: Create the manifest

Write a `plugin.json` at the repo root that references each asset by its relative path within `.claude/`.

### Step 3: Add metadata

Include version, description, author, and minimum Claude Code version. Follow semantic versioning — bump the minor version when you add new skills, bump the patch version for fixes.

### Step 4: Test locally

Before publishing, verify the plugin installs correctly:

```
claude plugin install ./path-to-your-repo
```

### Step 5: Choose a distribution method

| Method | How | Best For |
|---|---|---|
| **Git install** | `claude plugin install github:org/repo` | Internal teams with private repos |
| **Marketplace** | Submit via Claude Code marketplace | Public distribution to the broader community |
| **Direct path** | `claude plugin install ./local-path` | Local testing and development |

---

## When to Use Plugins vs Git Clone

| Scenario | Recommendation |
|---|---|
| Internal team, frequent updates, everyone has repo access | **Git clone** — simpler, direct file access, easy to contribute back |
| Sharing with teams outside your org | **Plugin** — cleaner install, no repo access needed |
| Publishing to the broader PM community | **Plugin + marketplace** — discoverable, versioned, one-command install |
| Experimenting with your own skills locally | **Neither** — just use `.claude/` directly in your project |

---

## Tips

- **Start with git clone, graduate to plugin.** This repo currently distributes via git clone, which is fine for an internal team. Convert to a plugin when you want to share beyond the team or need versioned releases.
- **Version your skills.** When you change a skill's behavior, bump the version in the manifest. This lets users pin to a known-good version while you iterate.
- **Keep the human-readable guides.** Plugins distribute the `.claude/` runnable versions. The `skills/` and `workflows/` human-readable guides are for onboarding and learning — they complement the plugin, they don't replace it.
- **Test before publishing.** Install the plugin in a clean project to verify everything resolves correctly. Missing file references are the most common issue.

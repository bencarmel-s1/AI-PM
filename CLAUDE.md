# AI-PM — Claude Code Context

This is the SentinelOne AI-PM repository: a living knowledge base for Product Managers to accelerate their work with Claude Code. You are helping a SentinelOne PM work through product management tasks.

## Company Context

Load this at the start of any PRD, strategy, or discovery session:

```
@workflows/company-context/company-context-sentinelone.md
```

> The file has placeholders for your product area and team. Fill those in once and save your own copy.

---

## Available Agents

These agents are pre-installed — no setup required. Invoke them with `use agent:X` or reference them directly in prompts.

| Agent | When to invoke |
|-------|----------------|
| `engineer` | Before handing off any spec to engineering — finds technical gaps, risks, and missing edge cases |
| `executive` | Before leadership syncs, writing a business case, or reframing a setback for stakeholders |
| `user-researcher` | After a research sprint — synthesizes interviews, support tickets, or survey data into themes and opportunities |

---

## Available Slash Commands

Type `/command-name` to run a full multi-step workflow. Each command asks you questions before doing anything.

| Command | What it does |
|---------|--------------|
| `/prd-creation` | Full PRD workflow: Socratic sharpening → 3 strategic versions → agent reviews → final doc |
| `/feature-request-discovery` | Pull and analyze Jira feature requests by product line, OKR alignment, and revenue signal |
| `/data-analysis` | Funnel/problem analysis, ROI impact estimation, or A/B test readout |
| `/launch-pack` | Generate all launch artifacts: release notes, sales brief, CS brief, exec announcement |
| `/product-strategy` | 3-phase strategy: competitive research → 5 strategic choices → Rumelt Kernel doc + exec slides |

---

## Available Skills

Skills are single-purpose knowledge frameworks. Invoke when you have relevant content to process.

| Skill | Invoke when... |
|-------|----------------|
| `customer-feedback-synthesis` | You have 3+ feedback sources (calls, tickets, surveys) to turn into themes and opportunities |
| `customer-call-questionnaire` | You have an interview guide draft and want to stress-test it before running calls |
| `strategic-decision-validation` | You have a proposed direction and want structured pressure-testing before committing |
| `backlog-prioritization` | You have a list of backlog items and need to align and frame them for prioritization |
| `todo-prioritization` | You have a task list and need to decide what to work on next by strategic leverage |
| `multi-agent-review` | You have a spec or PRD ready for parallel review from engineer, executive, and user-researcher perspectives |
| `stakeholder-communication` | You need to draft an executive update, bad-news message, cross-functional announcement, or board prep |

---

## Key Workflow Guidance

- **Writing a PRD?** → `/prd-creation`
- **Analyzing feature requests from Jira?** → `/feature-request-discovery` (requires Jira MCP)
- **Got data to analyze?** → `/data-analysis`
- **Shipping a feature?** → `/launch-pack`
- **Setting product strategy?** → `/product-strategy`
- **Got customer call notes?** → `customer-feedback-synthesis` skill
- **Reviewing a spec before engineering handoff?** → `engineer` agent
- **Preparing a leadership update?** → `executive` agent

---

## Repo Structure

```
workflows/advanced-workflow/   # Source workflows (read these to understand command internals)
skills/reviewer-guides/        # Human-readable agent guides
skills/customer-research/      # Human-readable skill guides
skills/strategic-planning/     # Human-readable skill guides
skills/productivity/           # Human-readable skill guides
prompts/                       # Standalone reusable prompts
case-studies/                  # Real PM examples
```

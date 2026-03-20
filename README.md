# 🤖 AI Product Management with Claude Code

> A collaborative space for Product Managers to explore, experiment, and share how Claude Code can accelerate and enhance the way we work.

---

## 📌 Purpose

This repository serves as a **living knowledge base** for our PM team to:

- Validate how **Claude Code** can support product management workflows
- Share **learnings, experiments, and outcomes** from real usage
- Build a library of **reusable prompts, templates, and workflows**
- Foster a culture of **AI-augmented product thinking**

---

## 🆕 What's New

> See the full [CHANGELOG](./CHANGELOG.md) for a complete history of additions and changes, including what each item does and when to use it.

**2026-03-20 — Trend Scout Update: 6 New Additions**
Added multi-agent review workflow and skill, plugin packaging guide, hooks & automation guide, stakeholder communication skill, 5 new prompt templates (seeding all 4 prompt categories + research study analysis), and the first AI PM Trend Scout report. See the [full CHANGELOG](./CHANGELOG.md) for details.

**2026-03-17 — New Skills: Customer Research, Strategic Planning, Productivity**
Added 5 new skill guides across 3 new categories in `skills/`: customer feedback synthesis, customer call questionnaire improvement, strategic decision validation, backlog prioritization, and to-do prioritization.

**2026-03-13 — Initial Release**
The repo launched with a full set of onboarding guides, 7 basic workflow templates, 4 advanced multi-step workflows (PRD creation, data analysis, feature request discovery, launch pack generation), the end-to-end PM lifecycle framework, specialist agent templates, and the SentinelOne company context file.

---

## ⚡ Claude Code Infrastructure

This repo ships with a pre-configured `.claude/` folder — agents, commands, and skills are ready to use the moment you open this project in Claude Code. No manual setup or file copying required.

### Slash Commands

Type `/command-name` in Claude Code to run a full multi-step workflow:

| Command | What it does |
|---------|--------------|
| `/prd-creation` | Full PRD workflow: Socratic sharpening → 3 strategic versions → agent reviews → final doc |
| `/feature-request-discovery` | Pull and analyze Jira feature requests by product line, OKR alignment, and revenue signal |
| `/data-analysis` | Funnel/problem analysis, ROI impact estimation, or A/B test readout |
| `/launch-pack` | Generate all launch artifacts: release notes, sales brief, CS brief, exec announcement |
| `/product-strategy` | 3-phase strategy: competitive research → 5 strategic choices → Rumelt Kernel doc + exec slides |

### Agents

Pre-installed specialist agents (invoke with `use agent:X` or reference in any prompt):

| Agent | When to invoke |
|-------|----------------|
| `engineer` | Before handing off any spec to engineering — finds technical gaps, risks, missing edge cases |
| `executive` | Before leadership syncs, writing a business case, or reframing a setback |
| `user-researcher` | After a research sprint — synthesizes qualitative data into themes and opportunities |

### Skills

Single-purpose knowledge frameworks (invoke when you have content to process):

| Skill | Invoke when... |
|-------|----------------|
| `customer-feedback-synthesis` | You have 3+ feedback sources to turn into themes and opportunities |
| `customer-call-questionnaire` | You have an interview guide draft to stress-test before running calls |
| `strategic-decision-validation` | You have a proposed direction to pressure-test before committing |
| `backlog-prioritization` | You have backlog items to normalize, align, and frame for prioritization |
| `todo-prioritization` | You have a task list and need to decide what to work on next |
| `multi-agent-review` | You have a spec or PRD ready for parallel review from 3 specialist perspectives |
| `stakeholder-communication` | You need to draft (not just review) an executive update, bad-news message, or cross-functional announcement |

> **Note:** The `skills/` folder contains human-readable guides for learning and onboarding. The `.claude/skills/` folder contains the runnable Claude Code versions of those same skills.

---

## 🗂️ Repository Structure

```
├── getting-started/      # Setup guides for both Claude tools
│   ├── claude-code/            # Terminal-based setup (Claude Code CLI)
│   │   ├── README.md           # Claude Code overview + when to use vs Desktop
│   │   ├── installing-claude.md    # Install on Mac/Windows, Zscaler setup, auth
│   │   ├── claude-md-setup.md      # Set up persistent context for your product/team
│   │   └── faq.md                  # Common setup issues and troubleshooting
│   ├── claude-desktop/         # No-terminal alternative using Claude Desktop + Cowork
│   │   ├── README.md           # Desktop vs CLI: when to use which
│   │   └── getting-started-cowork.md  # Install Claude Desktop and run your first task
│   └── mcp-configuration/      # Connect AI tools to external systems via MCP
│       ├── README.md           # What is MCP and what configs are available
│       └── jira-mcp-integration-for-windsurf/   # Connect Windsurf to Jira and Confluence
│           ├── README.md           # Step-by-step setup guide
│           └── jira-mcp-integration-config.md  # Config file to copy into Windsurf
│
├── prompts/              # Reusable prompt templates by PM use case
│   ├── discovery/        # User research, problem framing, hypothesis generation
│   ├── strategy/         # Roadmapping, prioritization, competitive analysis
│   ├── execution/        # PRD writing, spec generation, ticket creation
│   └── analytics/        # Data interpretation, metric definitions, OKR framing
│
├── workflows/            # Step-by-step Claude Code workflows for common PM tasks
│   ├── basic-workflows/  # 6 ready-to-use templates + quickstart guide
│   ├── advanced-workflow/          # Multi-step workflows for complex PM tasks
│   │   ├── prd-creation/           # Full PRD creation workflow with agent reviews
│   │   ├── data-analysis/          # Funnel analysis, ROI modeling, A/B test readouts
│   │   ├── product-strategy/       # 3-phase strategy workflow with Rumelt's Kernel
│   │   └── multi-agent-review/     # Parallel 3-agent spec review with unified synthesis
│   └── company-context/  # SentinelOne context templates for Claude sessions
│
├── case-studies/         # Real examples of Claude Code used in our PM work
│
├── skills/               # Guides on Claude Code capabilities relevant to PMs
│   ├── context-management.md   # How context windows work and how to manage long sessions
│   ├── reviewer-guides/  # Pullable agent templates for specialized PM tasks
│   │   ├── user-researcher.md  # Synthesize interviews, tickets, and qualitative feedback
│   │   ├── executive.md        # Reframe updates and decisions for leadership
│   │   └── engineer.md         # Review specs for technical gaps and feasibility
│   ├── customer-research/      # Skills for synthesizing feedback and improving discovery
│   │   ├── customer-feedback-synthesis.md   # Turn raw notes into themes and decision signals
│   │   └── customer-call-questionnaire.md   # Audit and improve your interview questions
│   ├── strategic-planning/     # Skills for decisions and backlog work
│   │   ├── strategic-decision-validation.md # Pressure-test a direction before committing
│   │   └── backlog-prioritization.md        # Normalize, align, and frame your backlog
│   ├── productivity/           # Skills for managing your own focus
│   │   ├── todo-prioritization.md           # Prioritize your to-do list by strategic leverage
│   │   └── multi-agent-patterns.md          # When to use subagents vs agent teams
│   └── communication/          # Skills for drafting stakeholder communications
│       └── stakeholder-communication.md     # Draft exec updates, bad-news framing, announcements
│
├── learning/             # Shared courses, certifications, and learning resources
│
└── resources/            # External links, papers, and reference material
```

---

## 🚀 Getting Started

**New to Claude Code?** Follow these steps in order:

> **Prefer not to use the terminal?** Skip straight to [`getting-started/claude-desktop/`](./getting-started/claude-desktop/) to set up Claude Desktop and Cowork — no terminal required.

1. **Install Claude Code** — [`getting-started/claude-code/`](./getting-started/claude-code/) covers Mac and Windows installation, Zscaler setup, authentication, and why you're using the terminal instead of the website.
2. **Complete the level-set course** — Work through [Claude Code for Product Managers](./learning/claude-code-for-pms.md) by Carl Vellotti (~10–12 hours, self-paced, free with Claude Pro). This is the shared baseline for the whole team — do this before anything else.
3. **Get yourself familiar with the Product Management Lifecycle with the use of Claude Code** - Work through [Product Management Lifecycle](./product-management-lifecycle/) which showcases the end-to-end PM workflow.
3. **Run your first workflow** — [`workflows/basic-workflows/quickstart.md`](./workflows/basic-workflows/quickstart.md) walks you through a complete end-to-end example in under 15 minutes. Start here before exploring other templates.
4. **Connect to Jira (optional)** — [`getting-started/mcp-configuration/`](./getting-started/mcp-configuration/) shows you how to connect Windsurf to Jira and Confluence via MCP, so you can query tickets and pages directly from the chat.
5. **Personalize your CLAUDE.md** — A `CLAUDE.md` is already included at the repo root with shared SentinelOne context and a full index of available agents, commands, and skills. Open [`workflows/company-context/company-context-sentinelone.md`](./workflows/company-context/company-context-sentinelone.md) and fill in your product area and team details — then you're fully set up. See [`getting-started/claude-code/claude-md-setup.md`](./getting-started/claude-code/claude-md-setup.md) for more guidance.
6. **Explore the templates** — Browse [`workflows/basic-workflows/`](./workflows/basic-workflows/) for 6 ready-to-use PM templates, or jump straight into an advanced workflow with `/prd-creation`, `/data-analysis`, or `/product-strategy`.
7. **Contribute back** — Share what worked (and what didn't).

---

## 🤝 How to Contribute

We grow this repo together. Here's how you can add value:

1. **Add a prompt** — Drop a tested prompt into the right `prompts/` subfolder with a short description of what it does and when to use it.
2. **Document a workflow** — Write a short step-by-step guide in `workflows/` for a task you've automated or improved with Claude Code.
3. **Share a case study** — Capture a real example in `case-studies/` using the template below.
4. **Share a learning resource** — Add a course or tutorial to [`learning/`](./learning/) using the template in that folder's README.
5. **Raise a question or idea** — Open an issue to spark discussion with the team.

### Case Study Template

```markdown
## [Task Name]
**PM:** [Your name]  
**Date:** [YYYY-MM-DD]  
**Time Saved:** [Estimate]

### The Challenge
What problem were you trying to solve?

### How Claude Code Helped
What did you ask it to do? What prompt/workflow did you use?

### Outcome
What was the result? What would you do differently?

### Prompt Used
[Paste the prompt here]
```

---

## 📐 Prompt Writing Guidelines

To keep our prompt library high quality and reusable:

- **Be specific about role and context** — e.g., *"You are a senior PM at a B2B SaaS company..."*
- **Define the output format** — e.g., *"Return a table with columns: Feature, User Value, Effort, Risk"*
- **Include constraints** — e.g., *"Limit to 5 items. Avoid technical jargon."*
- **Test before committing** — only share prompts you've validated yourself
- **Add a usage note** — one line explaining when this prompt is most useful

---

## 📚 Learning Resources

Head to the [`learning/`](./learning/) folder for shared courses, certifications, and tutorials — including the first entry, [Claude Code for Product Managers](./learning/claude-code-for-pms.md) by Carl Vellotti.

Quick links:
- [Anthropic Prompt Engineering Guide](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)
- [Claude Code Documentation](https://docs.claude.ai)
- [Zscaler Certificate Documentation](https://connect.sentinelone.com/site/b00a4fac-a250-505d-abfd-079c9f50f972/page/64426c1d-c34b-433c-a5f2-db32495d0dc3)

---

## 🧭 Guiding Principles

- **AI augments, it doesn't replace** — We use Claude Code to go faster and think better, not to skip thinking.
- **Share openly** — A prompt that saves you 30 minutes might save the whole team hours.
- **Validate and iterate** — Always review Claude's output critically. Document what works and what doesn't.
- **Keep the human in the loop** — Especially for decisions that affect users, customers, or strategy.

---

## 📬 Maintainers

| Name | Role | Contact |
|---|---|---|
| Ben Carmel | Repo Owner | ben.carmel@sentinelone.com |
| Ingemar Dvorsky | Contributor | ingemar.dvorsky@sentinelone.com |

> Want to become a maintainer? Reach out or open a PR!

---

*Last updated: March 2026*
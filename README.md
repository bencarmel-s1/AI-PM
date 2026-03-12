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

## 🗂️ Repository Structure

```
├── getting-started/      # Setup guides for both Claude tools
│   ├── claude-code/            # Terminal-based setup (Claude Code CLI)
│   │   ├── README.md           # Claude Code overview + when to use vs Desktop
│   │   ├── installing-claude.md    # Install on Mac/Windows, Zscaler setup, auth
│   │   ├── claude-md-setup.md      # Set up persistent context for your product/team
│   │   └── faq.md                  # Common setup issues and troubleshooting
│   └── claude-desktop/         # No-terminal alternative using Claude Desktop + Cowork
│       ├── README.md           # Desktop vs CLI: when to use which
│       └── getting-started-cowork.md  # Install Claude Desktop and run your first task
│
├── prompts/              # Reusable prompt templates by PM use case
│   ├── discovery/        # User research, problem framing, hypothesis generation
│   ├── strategy/         # Roadmapping, prioritization, competitive analysis
│   ├── execution/        # PRD writing, spec generation, ticket creation
│   └── analytics/        # Data interpretation, metric definitions, OKR framing
│
├── workflows/            # Step-by-step Claude Code workflows for common PM tasks
│   ├── basic-workflows/  # 6 ready-to-use templates + quickstart guide
│   ├── advanced-workflow/prd-creation/      # Full PRD creation workflow with agent reviews
│   ├── advanced-workflow/data-analysis/     # Funnel analysis, ROI modeling, A/B test readouts
│   ├── advanced-workflow/product-strategy/  # 3-phase strategy workflow with Rumelt's Kernel
│   └── company-context/  # SentinelOne context templates for Claude sessions
│
├── case-studies/         # Real examples of Claude Code used in our PM work
│
├── skills/               # Guides on Claude Code capabilities relevant to PMs
│   ├── context-management.md   # How context windows work and how to manage long sessions
│   └── agents/           # Pullable agent templates for specialized PM tasks
│       ├── user-researcher.md  # Synthesize interviews, tickets, and qualitative feedback
│       ├── executive.md        # Reframe updates and decisions for leadership
│       └── engineer.md         # Review specs for technical gaps and feasibility
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
3. **Run your first workflow** — [`workflows/basic Workflows/quickstart.md`](./workflows/basic%20Workflows/quickstart.md) walks you through a complete end-to-end example in under 15 minutes. Start here before exploring other templates.
4. **Set up your CLAUDE.md** — [`getting-started/claude-code/claude-md-setup.md`](./getting-started/claude-code/claude-md-setup.md) shows you how to give Claude persistent context about your product and team. Do this once and save time every session. Use [`workflows/company-context/company-context-sentinelone.md`](./workflows/company-context/company-context-sentinelone.md) as your starting point — SentinelOne context is pre-filled.
5. **Explore the templates** — Browse [`workflows/basic Workflows/`](./workflows/basic%20Workflows/) for 6 ready-to-use PM templates.
6. **Contribute back** — Share what worked (and what didn't).

---

## 💡 PM Use Cases We're Exploring

> **Legend:** 🟢 Done · 🟡 In Progress · 🔵 Planned

**Setup & Onboarding**
| Use Case | Status | Where |
|---|---|---|
| Install & configure Claude Code | 🟢 Done | `getting-started/claude-code/installing-claude.md` |
| Set up CLAUDE.md for your product | 🟢 Done | `getting-started/claude-code/claude-md-setup.md` |
| Run your first workflow | 🟢 Done | `workflows/Basic Workflows/quickstart.md` |
| Use Claude without a terminal (Desktop + Cowork) | 🟢 Done | `getting-started/claude-desktop/` |

**Research & Discovery**
| Use Case | Status | Where |
|---|---|---|
| User interview synthesis | 🟢 Done | `workflows/Basic Workflows/` |
| Competitive research synthesis | 🟢 Done | `workflows/Basic Workflows/` |
| Synthesize research with a specialist agent | 🟢 Done | `skills/reviewer-guides/user-researcher.md` |

**Planning & Execution**
| Use Case | Status | Where |
|---|---|---|
| User story & ticket generation | 🟢 Done | `workflows/Basic Workflows/` |
| Writing & refining PRDs | 🟡 In Progress | `prompts/execution/` |
| Spec review for technical gaps | 🟢 Done | `skills/reviewer-guides/engineer.md` |
| Roadmap scenario planning | 🔵 Planned | `prompts/strategy/` |

**Communication & Reporting**
| Use Case | Status | Where |
|---|---|---|
| Meeting notes → action items | 🟢 Done | `workflows/Basic Workflows/` |
| Weekly status updates | 🟢 Done | `workflows/Basic Workflows/` |
| Sprint retrospectives | 🟢 Done | `workflows/Basic Workflows/` |
| Leadership-ready updates and briefs | 🟢 Done | `skills/reviewer-guides/executive.md` |

**Strategy & Analytics**
| Use Case | Status | Where |
|---|---|---|
| Product strategy development | 🟢 Done | `workflows/advanced-workflow/product-strategy/` |
| OKR & metric definition | 🔵 Planned | `prompts/analytics/` |

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
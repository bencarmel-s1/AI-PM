# AI Product Management with Claude Code

A resource for SentinelOne Product Managers to adopt, run, and improve a Claude Code-powered PM Operating System.

---

## The PM Operating System

The `S1-PM-OS/` folder contains a **complete, opinionated PM Operating System** — the setup we recommend every PM adopt as their primary working environment with Claude Code.

It includes:
- **Folder structure** (`1-Tasks/` through `6-Data/`) — a canonical way to organize tasks, projects, meetings, knowledge, workflows, and data
- **22 Claude skills** — pre-built for daily PM work: standup, meeting prep, PRD writing, research synthesis, stakeholder updates, and more
- **Hooks** — `skill-activator.py` auto-suggests the right skill for each prompt; `model-advisor.py` recommends the right Claude model by complexity
- **CLAUDE.md + GOALS.md** — session-to-session context so Claude always knows your role, OKRs, and stakeholders
- **Sample data** — a fully filled-in example OS (Jamie Chen at Acme Analytics) so you can see what it looks like in real use

**Start here:** [`S1-PM-OS/README.md`](./S1-PM-OS/README.md)

To adopt the OS for yourself:
1. Copy `S1-PM-OS/` to your own working directory
2. Replace `GOALS.md` with your own role, OKRs, and stakeholders
3. Update `CLAUDE.md` with your product area and team details
4. Clear out the sample data (`1-Tasks/`, `2-Projects/`, `3-Meetings/`, `5-Knowledge/People/`) and start fresh

---

## Getting Started

New to Claude Code? [`getting-started/`](./getting-started/) covers installation, setup, authentication, and how to connect to Jira/Confluence via MCP. Work through this before adopting the OS.

---

## Knowledgebase

[`Knowledgebase/`](./Knowledgebase/) contains **patterns, templates, and experiments** that are either precursors to OS workflows or things we're still figuring out. Browse, try things, share what works.

| Folder | What's there |
|--------|-------------|
| `basic-workflows/` | 6 simple templates for common PM tasks (meeting notes → actions, sprint retro, user story, etc.) |
| `advanced-workflow/` | Multi-step workflows for PRD creation, data analysis, product strategy, feature discovery, launch |
| `company-context/` | SentinelOne context templates for seeding Claude sessions |
| `prompts/` | Standalone reusable prompts by use case (discovery, strategy, execution, analytics) |
| `skills/` | Human-readable guides for skills already in the OS |
| `learning/` | Courses, tutorials, and educational resources |
| `case-studies/` | Real PM examples — please contribute when you have a good one |
| `resources/` | External links, papers, and reference material |
| `product-management-lifecycle/` | End-to-end PM lifecycle documentation (in progress) |

---

## Claude Code Infrastructure

The repo root `.claude/` is pre-configured with agents, commands, and skills ready to use from this project. These are the **team-level** tools, separate from the full OS:

**Slash Commands** — multi-step workflows:

| Command | What it does |
|---------|--------------|
| `/prd-creation` | Full PRD workflow: Socratic sharpening → 3 strategic versions → agent reviews → final doc |
| `/feature-request-discovery` | Pull and analyze Jira feature requests by product line, OKR alignment, and revenue signal |
| `/data-analysis` | Funnel/problem analysis, ROI impact estimation, or A/B test readout |
| `/launch-pack` | Generate all launch artifacts: release notes, sales brief, CS brief, exec announcement |
| `/product-strategy` | 3-phase strategy: competitive research → 5 strategic choices → Rumelt Kernel doc + exec slides |

**Agents:**

| Agent | When to invoke |
|-------|----------------|
| `engineer` | Before handing off any spec to engineering — finds technical gaps, risks, missing edge cases |
| `executive` | Before leadership syncs, writing a business case, or reframing a setback |
| `user-researcher` | After a research sprint — synthesizes qualitative data into themes and opportunities |

**Skills** (7 core, team-shared):

| Skill | Invoke when... |
|-------|----------------|
| `customer-feedback-synthesis` | You have 3+ feedback sources to turn into themes and opportunities |
| `customer-call-questionnaire` | You have an interview guide draft to stress-test before running calls |
| `strategic-decision-validation` | You have a proposed direction to pressure-test before committing |
| `backlog-prioritization` | You have backlog items to normalize, align, and frame for prioritization |
| `todo-prioritization` | You have a task list and need to decide what to work on next |
| `multi-agent-review` | You have a spec or PRD ready for parallel review from 3 specialist perspectives |
| `stakeholder-communication` | You need to draft an executive update, bad-news message, or cross-functional announcement |

> The OS (`S1-PM-OS/.claude/skills/`) includes 22 skills — a superset of these 7. Once you adopt the OS, use those instead.

---

## How to Contribute

- **Add a prompt** — Drop a tested prompt into `ideas/prompts/` with a short description
- **Document a workflow** — Write a step-by-step guide in `ideas/basic-workflows/` or `ideas/advanced-workflow/`
- **Share a case study** — Capture a real example in `ideas/case-studies/`
- **Improve the OS** — If you find a better pattern, improve a skill in `os/.claude/skills/` and open a PR

---

## Maintainers

| Name | Role | Contact |
|---|---|---|
| Ben Carmel | Repo Owner | ben.carmel@sentinelone.com |
| Ingemar Dvorsky | Contributor | ingemar.dvorsky@sentinelone.com |

*Last updated: April 2026*

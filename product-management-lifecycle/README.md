# 🔄 Product Management Lifecycle

> A structured framework for how PMs work with Claude Code — from first signal to shipped feature.

---

## 📌 What This Folder Is

This folder defines the **product management lifecycle** as it exists when Claude Code is a first-class collaborator.

It's a north star, not a finished product. The content here will grow as the team validates and documents each stage with real workflows, prompts, and examples. If you're reading this early, you're seeing it take shape.

The goal: make the PM process from raw discovery to delivered feature faster, more consistent, and more thoughtful — with Claude handling the synthesis and scaffolding while PMs stay in control of the decisions.

---

## 🗺️ The Lifecycle at a Glance

| Stage | What Happens | Claude's Role | Status |
|---|---|---|---|
| 1. Discovery | Gather signals — research, feedback, tickets, competitive data | Synthesize, theme, and surface insights | 🟢 Supported |
| 2. Problem Framing | Define the opportunity, validate assumptions, prioritize | Structure hypotheses, identify gaps | 🟡 In Progress |
| 3. Requirements | Collect and organize requirements from stakeholders | Draft, organize, and format requirements docs | 🟡 In Progress |
| 4. PRD | Write the product requirements document | Draft full PRD, refine sections, flag missing states | 🟡 In Progress |
| 5. Prototyping | Build interactive mockups to validate ideas before engineering | Generate prototype scaffolding, review designs, suggest interactions | 🟡 In Progress |
| 6. Jira | Push specs into tickets for the engineering team | Generate epics, stories, acceptance criteria, push to Jira | 🔵 Planned |
| 7. Delivery Tracking | Monitor progress, surface blockers, keep stakeholders updated | Summarize sprint updates, draft comms | 🟢 Supported |
| 8. Retrospective | Capture what worked, what didn't, what to carry forward | Synthesize retro notes into structured action items | 🟢 Supported |

> **Legend:** 🟢 Supported by existing workflows/prompts · 🟡 In Progress · 🔵 Planned

---

## 🔍 Stage Details

### Stage 1 — Discovery

**What you're doing:** Pulling in raw signals — user interviews, support tickets, NPS verbatims, competitive research — and making sense of them before you've committed to anything.

**Claude's role:** Synthesize. Theme. Surface patterns you'd miss by reading linearly.

**Tools available today:**
- [`skills/agents/user-researcher.md`](../skills/agents/user-researcher.md) — synthesize interviews, tickets, and qualitative feedback
- [`workflows/basic Workflows/user-research-synthesis.md`](../workflows/basic%20Workflows/user-research-synthesis.md) — step-by-step workflow
- [`workflows/basic Workflows/competitive-analysis.md`](../workflows/basic%20Workflows/competitive-analysis.md) — competitive research synthesis
- [`prompts/discovery/`](../prompts/discovery/) — targeted discovery prompts *(coming soon)*

---

### Stage 2 — Problem Framing

**What you're doing:** Turning raw insight into a crisp opportunity statement. Mapping assumptions. Writing hypotheses you can validate.

**Claude's role:** Help structure the problem space. Generate "how might we" framings. Challenge assumptions you haven't questioned.

**Tools available today:**
- [`prompts/discovery/`](../prompts/discovery/) *(coming soon)*

---

### Stage 3 — Requirements

**What you're doing:** Collecting and organizing what the product needs to do — from stakeholder input, technical constraints, user research, and your own judgment.

**Claude's role:** Draft structured requirements from messy inputs. Identify gaps and conflicts. Format for stakeholder review.

**Tools available today:**
- [`prompts/execution/`](../prompts/execution/) *(coming soon)*
- This lifecycle folder will contain a dedicated `requirements/` workflow *(planned)*

---

### Stage 4 — PRD

**What you're doing:** Writing the document that aligns engineering, design, and leadership on what you're building, why, and for whom.

**Claude's role:** Draft sections, suggest structure, flag missing edge cases and error states, and run an engineer review before you share.

**Tools available today:**
- [`skills/agents/engineer.md`](../skills/agents/engineer.md) — review your PRD for technical gaps before sending to eng
- [`prompts/execution/`](../prompts/execution/) — PRD drafting prompts *(in progress)*

---

### Stage 5 — Prototyping

**What you're doing:** Building interactive mockups or lightweight prototypes to validate your ideas with users, stakeholders, or engineering before anything gets built for real.

**Claude's role:** Generate prototype scaffolding (HTML/React), suggest UI interactions, review Figma designs for UX gaps, and help you iterate quickly without waiting on a full engineering cycle.

**Tools available today:**
- Claude Code can scaffold interactive prototypes from a PRD or wireframe description — see [`Prototyping/`](../../Prototyping/) for examples of real prototypes built this way
- Figma MCP integration — share a Figma URL and Claude can read your designs and generate code directly from them
- [`skills/agents/engineer.md`](../skills/agents/engineer.md) — sanity-check prototype assumptions before showing to engineering

**What's coming:**
- A `prototyping/` workflow in this folder: from PRD → working prototype in one session
- Prompt templates for common prototype patterns (data tables, dashboards, forms, navigation)

---

### Stage 6 — Jira

**What you're doing:** Translating the PRD into the actual tickets your engineering team will pick up in sprint planning.

**Claude's role:** Generate well-formed epics, user stories, and acceptance criteria directly from your PRD. Push to Jira via the Atlassian MCP integration.

**What's coming:**
- A workflow for PRD → Jira: one command to go from a spec to a full set of structured tickets
- Jira prompt templates for story formatting, epic structure, and acceptance criteria
- Integration guide for the Atlassian MCP connection

> This is the highest-leverage stage in the lifecycle. A good PRD can become a Jira backlog in minutes. This workflow is a top priority for this folder.

---

### Stage 7 — Delivery Tracking

**What you're doing:** Monitoring sprint progress, communicating status, and keeping stakeholders aligned while the team builds.

**Claude's role:** Summarize sprint notes. Draft status updates for leadership. Identify blockers that need attention.

**Tools available today:**
- [`workflows/basic Workflows/weekly-status-update.md`](../workflows/basic%20Workflows/weekly-status-update.md)
- [`workflows/basic Workflows/sprint-retrospective.md`](../workflows/basic%20Workflows/sprint-retrospective.md)
- [`skills/agents/executive.md`](../skills/agents/executive.md) — turn sprint notes into leadership-ready updates

---

### Stage 8 — Retrospective

**What you're doing:** Closing the loop. What shipped, what didn't, what you'd do differently, and what the team learned.

**Claude's role:** Synthesize retro notes into structured outputs. Surface patterns across multiple retros over time.

**Tools available today:**
- [`workflows/basic Workflows/sprint-retrospective.md`](../workflows/basic%20Workflows/sprint-retrospective.md)
- [`workflows/basic Workflows/meeting-notes-to-action-items.md`](../workflows/basic%20Workflows/meeting-notes-to-action-items.md)

---

## 🔗 How This Connects to the Rest of the Repo

This lifecycle is a frame — a way to see how all the other content in the repo fits together.

| If you're at this stage... | Start here |
|---|---|
| Discovery | `skills/agents/user-researcher.md` · `workflows/basic Workflows/` |
| PRD writing | `prompts/execution/` · `skills/agents/engineer.md` |
| Prototyping | `Prototyping/` · Figma MCP integration · `skills/agents/engineer.md` |
| Jira / ticket creation | `prompts/execution/` · *(lifecycle workflows, coming soon)* |
| Stakeholder communication | `skills/agents/executive.md` · `workflows/basic Workflows/weekly-status-update.md` |
| Retrospectives | `workflows/basic Workflows/sprint-retrospective.md` |

---

## 🧭 Guiding Principles for This Lifecycle

- **PM owns the decisions. Claude owns the scaffolding.** Claude drafts, synthesizes, and organizes. You decide what goes in the PRD, what gets into Jira, and what ships.
- **Every stage has a handoff.** Each lifecycle stage produces a real artifact — a synthesis doc, a requirements list, a PRD, a set of Jira tickets. Claude helps you get there faster.
- **Garbage in, garbage out.** Claude is only as good as the inputs you give it. Messy requirements produce messy PRDs. Context is your most important asset.
- **This is a loop, not a line.** Discovery doesn't end when you start writing a PRD. You'll cycle back. Claude can hold context across that iteration — use it.

---

## 📁 What Will Live in This Folder

As the lifecycle matures, this folder will contain:

```
product-management-lifecycle/
├── README.md                        ← You are here
├── requirements/
│   ├── requirements-workflow.md     # How to go from stakeholder inputs to a structured requirements doc
│   └── requirements-prompt.md       # Claude prompt for requirements gathering and formatting
├── prd/
│   ├── prd-workflow.md              # End-to-end PRD writing workflow with Claude
│   ├── prd-template.md              # PRD structure and format for our team
│   └── prd-to-jira-workflow.md      # How to go from a finished PRD to Jira tickets
├── prototyping/
│   ├── prototyping-workflow.md      # How to go from a PRD to a working prototype with Claude Code
│   ├── figma-to-code-workflow.md    # How to use the Figma MCP to generate code from designs
│   └── prototype-prompt-templates.md # Prompts for common UI patterns (tables, dashboards, forms)
├── jira/
│   ├── jira-integration-setup.md    # How to connect Claude Code to Jira via Atlassian MCP
│   ├── story-generation-prompt.md   # Prompt for generating user stories from specs
│   └── epic-structure-prompt.md     # Prompt for structuring epics and hierarchies
└── delivery/
    └── sprint-review-workflow.md    # How to run a delivery review with Claude
```

---

## 🤝 How to Contribute

This is an early-stage folder and every stage needs content. The repository will be updated by Contributors.

Use the [case study template](../README.md) to capture real examples as you go.

---

*Last updated: March 2026 · This folder is actively being built — check back often.*

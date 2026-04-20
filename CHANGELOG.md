# Changelog

> What's been added, changed, or removed — and why it matters to you as a PM.
>
> Entries are in reverse-chronological order. Each item explains what it is, what problem it solves, and when you'd use it.

---

## 2026-04-20 — Repo Restructure: S1-PM-OS + Knowledgebase

**What's new:** The repo is reorganized around a clear two-part structure. `S1-PM-OS/` is the complete, production PM Operating System — what we recommend every PM adopt. `Knowledgebase/` contains all the patterns, templates, and experiments from the previous repo structure, kept as a living reference and exchange space.

### Changed

- **Repo structure** — The root now has three folders: `S1-PM-OS/` (the OS), `Knowledgebase/` (patterns and experiments), and `getting-started/` (onboarding). Previous top-level folders (`workflows/`, `prompts/`, `skills/`, `learning/`, `case-studies/`, `resources/`, `product-management-lifecycle/`) have moved into `Knowledgebase/`.
- **README.md** — Rewritten to lead with the OS as the primary recommendation, with Knowledgebase clearly positioned as supplemental.
- **CLAUDE.md** — Updated repo structure map to reflect the new layout.

### Added

- **[S1-PM-OS](./S1-PM-OS/)** — A complete, opinionated PM Operating System. Includes the 1–6 folder structure (Tasks, Projects, Meetings, Workflows, Knowledge, Data), 22 Claude skills for daily PM work, two hooks (skill-activator and model-advisor), CLAUDE.md + GOALS.md templates, and fully filled-in sample data so you can see what a real OS looks like. Copy this to your own working directory, replace the personal context, and start using it.
- **[Knowledgebase](./Knowledgebase/)** — All prior workflow guides, prompt templates, skill guides, learning resources, and case studies. Use for reference, exploration, and contributing new patterns back to the team.

---

## 2026-03-20 — Stakeholder Communication Skill

**What's new:** Added a skill for drafting stakeholder communications — exec updates, bad-news framing, cross-functional announcements, and board prep. Pairs with the executive agent for a complete draft → review workflow.

### Added

- **[Stakeholder Communication Skill](./skills/communication/stakeholder-communication.md)** — Draft leadership-facing communications with structured frameworks for different scenarios. Use when you need to write (not just review) exec updates, deliver difficult news, or prepare board materials. Pair with the `executive` agent for review.

---

## 2026-03-20 — Hooks & Automation Guide

**What's new:** Added a guide with 4 PM-specific hook recipes for automating spec reviews, enforcing template compliance, and building quality gates into your Claude Code workflows.

### Added

- **[Hooks for PMs](./workflows/basic-workflows/hooks-for-pms.md)** — Guide to Claude Code hooks with PM-specific recipes: auto-run agent reviews on spec edits, enforce PRD template sections, auto-format markdown, and validate required content before completion. Use when you want to automate quality checks in your PM workflows.

---

## 2026-03-20 — Research Study Analysis Prompt

**What's new:** Added a discovery prompt for analyzing published research studies (like Anthropic's 81K-person AI usage study) and extracting product implications, user segments, and opportunity areas.

### Added

- **[Research Study Analysis](./prompts/discovery/research-study-analysis.md)** — Turn published research findings into product insights and opportunity areas. Use when a major study drops and you want to connect it to your product strategy.

---

## 2026-03-20 — Prompt Library: First 4 Prompts

**What's new:** Seeded all 4 prompt categories with exemplar prompts. Each includes purpose, when to use, the prompt itself, and a usage example — setting the standard for future contributions.

### Added

- **[Interview Synthesis](./prompts/discovery/interview-synthesis.md)** — Synthesize raw interview notes into structured themes, pain points, and opportunities. Use after customer calls or research sprints.
- **[PRD Draft](./prompts/execution/prd-draft.md)** — Draft a PRD section from a brief or research input. Use for lightweight PRD drafting without the full advanced workflow.
- **[OKR Writing](./prompts/analytics/okr-writing.md)** — Write or refine OKRs from strategic context. Use during quarterly planning or goal-setting.
- **[Competitive Positioning](./prompts/strategy/competitive-positioning.md)** — Generate a competitive positioning statement. Use when preparing for strategy reviews or market analysis.

---

## 2026-03-20 — Plugin Packaging Guide

**What's new:** Added a guide for packaging Claude Code skills, agents, and commands as a distributable plugin. Covers the plugin manifest format, conversion steps, and distribution options.

### Added

- **[Plugin Packaging Guide](./workflows/basic-workflows/plugin-packaging.md)** — Step-by-step guide for turning a collection of skills, agents, and commands into a Claude Code plugin. Use when you want to share your PM toolkit beyond a git clone — covers manifest structure, local testing, and marketplace publishing.

---

## 2026-03-20 — Multi-Agent Review & Repo Health Fixes

**What's new:** Added a multi-agent review system that runs the engineer, executive, and user-researcher agents in parallel on any spec or PRD, then synthesizes their feedback into a unified review. Also fixed repo health issues (missing CHANGELOG entry, broken README links).

### Added

**Multi-Agent Review**
- **[Multi-Agent Review Workflow](./workflows/advanced-workflow/multi-agent-review/)** — Runs all 3 specialist agents in parallel on a spec, then synthesizes their feedback into a unified, priority-ordered review document. Use before any major spec handoff or leadership review.
- **[Multi-Agent Review Skill](./skills/productivity/multi-agent-patterns.md)** — Human-readable guide on when to use subagents vs agent teams, how to compose the repo's 3 agents for comprehensive reviews, and PM-specific multi-agent patterns (parallel competitive research, draft → review pipelines).

### Fixed

- Added missing CHANGELOG entry for the March 17 skills release (see below)
- Fixed broken `workflows/basic Workflows/` links in README Getting Started section (now correctly points to `workflows/basic-workflows/`)

---

## 2026-03-17 — New Skills: Customer Research, Strategic Planning, Productivity

**What's new:** Added 5 skill guides across 3 new categories, each with a runnable Claude Code version in `.claude/skills/` and a human-readable guide in `skills/`. These cover customer feedback synthesis, interview questionnaire improvement, strategic decision validation, backlog prioritization, and to-do prioritization.

### Added

**Customer Research**
- **[Customer Feedback Synthesis](./skills/customer-research/customer-feedback-synthesis.md)** — Turn raw feedback from calls, tickets, and surveys into structured themes, pain points, and product opportunities. Use after any research sprint or before a planning session.
- **[Customer Call Questionnaire](./skills/customer-research/customer-call-questionnaire.md)** — Audit and stress-test your interview guide before running customer calls. Use when preparing for a research sprint.

**Strategic Planning**
- **[Strategic Decision Validation](./skills/strategic-planning/strategic-decision-validation.md)** — Pressure-test a proposed direction against your strategy before committing. Use before leadership reviews or major roadmap decisions.
- **[Backlog Prioritization](./skills/strategic-planning/backlog-prioritization.md)** — Normalize, align, and frame backlog items for prioritization conversations. Use before sprint planning or quarterly reviews.

**Productivity**
- **[To-Do Prioritization](./skills/productivity/todo-prioritization.md)** — Prioritize your personal task list by strategic leverage. Use at the start of your week when deciding what to work on.

---

## 2026-03-13 — Initial Release

**What's new:** The AI-PM repo launched with a complete foundation: onboarding guides for all skill levels, 7 ready-to-use basic workflow templates, 4 advanced multi-step workflows, a product strategy module with 3 frameworks, the end-to-end PM lifecycle framework, specialist reviewer agents, and a Salesforce automation. Everything below is available now.

### Added

**Getting Started**
- **[Claude Code Setup Guide](./getting-started/claude-code/)** — Install guide for Mac and Windows including Zscaler cert setup and authentication. Use this if you're new to Claude Code and want the full terminal-based experience.
- **[Claude Desktop Guide](./getting-started/claude-desktop/)** — No-terminal alternative using Claude Desktop + Cowork. Start here if you want results fast without touching the command line.
- **[Jira MCP Integration](./getting-started/mcp-configuration/jira-mcp-integration-for-windsurf/)** — Step-by-step guide + config file to connect Windsurf directly to your Jira and Confluence instance. Unlocks the ability to query tickets, read pages, and push updates without leaving the AI chat.

**Basic Workflows** — 7 ready-to-run templates, each a self-contained prompt + guide
- **[Quickstart](./workflows/basic-workflows/quickstart.md)** — A 15-minute end-to-end example covering a complete PM task. Start here before exploring anything else.
- **[User Research Synthesis](./workflows/basic-workflows/user-research-synthesis.md)** — Takes raw interview notes and surfaces themes, pain points, and opportunity areas. Replaces hours of manual affinity mapping.
- **[Competitive Analysis](./workflows/basic-workflows/competitive-analysis.md)** — Structures competitor notes into a comparison matrix. Useful for strategy prep or stakeholder readouts.
- **[Meeting Notes to Action Items](./workflows/basic-workflows/meeting-notes-to-action-items.md)** — Converts messy meeting notes into clean action items with owners and due dates.
- **[Sprint Retrospective](./workflows/basic-workflows/sprint-retrospective.md)** — Structures retro feedback into went-well / didn't-go-well / to-improve buckets with suggested actions.
- **[Weekly Status Update](./workflows/basic-workflows/weekly-status-update.md)** — Drafts a stakeholder-ready status update from your notes or bullet points.
- **[User Story](./workflows/basic-workflows/user-story.md)** — Generates well-formed user stories with acceptance criteria from a brief feature description.

**Advanced Workflows** — Multi-step workflows for complex PM tasks, each with a workflow guide, templates, and worked examples
- **[PRD Creation](./workflows/advanced-workflow/prd-creation/)** — Full 5-phase PRD workflow. Includes a Socratic questioning phase to sharpen your thinking before writing, sub-agent review setup, Carl's and Lenny's PRD templates, and a complete example output. Use this for any significant feature or initiative.
- **[Data Analysis](./workflows/advanced-workflow/data-analysis/)** — Covers problem analysis, impact estimation, and experiment readouts. Each comes with a template and a worked example. Use this when you have raw data and need to build a narrative or recommendation around it.
- **[Feature Request Discovery](./workflows/advanced-workflow/feature-request-discovery/)** — Queries Jira live to pull and theme feature requests, then maps them to OKRs. Includes a workflow guide, discovery template, OKR template, and a worked example. Replaces manual ticket triage.
- **[Launch Pack Generation](./workflows/advanced-workflow/launch/)** — Generates a full launch pack (sales enablement, CS brief, exec summary, customer announcement, internal FAQ, and social copy) from a single feature description. Includes a worked example. Cuts cross-functional launch prep from days to hours.
- **[Product Strategy](./workflows/advanced-workflow/product-strategy/)** — 3-phase strategy workflow that outputs a written strategy document and executive slides. Includes 3 plug-and-play frameworks:
  - **[Rumelt's Strategy Kernel](./workflows/advanced-workflow/product-strategy/frameworks/rumelt-strategy-kernel.md)** — Diagnosis → Guiding Policy → Coherent Actions. Best for defining a focused, opinionated strategy.
  - **[Gibson Biddle's DHM](./workflows/advanced-workflow/product-strategy/frameworks/gibson-biddle-dhm.md)** — Delight, Hard to Copy, Margin. Best for product strategy grounded in defensibility.
  - **[SWOT Analysis](./workflows/advanced-workflow/product-strategy/frameworks/swot-analysis.md)** — Structured strengths / weaknesses / opportunities / threats. Best for situation assessment before choosing a direction.

**Product Management Lifecycle**
- **[PM Lifecycle Framework](./product-management-lifecycle/)** — End-to-end map of the PM workflow (Discovery → Problem Framing → Requirements → PRD → Prototyping → Jira → Delivery → Launch → Retrospective) with Claude's role at each stage, status indicators, and links to relevant workflows. Use this to understand where AI can help at each phase of your work.

**Company Context**
- **[SentinelOne Context Template](./workflows/company-context/company-context-sentinelone.md)** — Pre-filled CLAUDE.md context with SentinelOne product, market, and team context. Paste into your CLAUDE.md once so Claude always understands your company context without re-explaining every session.
- **[Blank Company Context Template](./workflows/company-context/company-context-template.md)** — Generic version for teams outside SentinelOne or for creating a personal context file.

**Skills**
- **[Context Management](./skills/context-management.md)** — Explains how Claude's context window works and how to manage long sessions without losing quality. Read this if you've noticed Claude's responses degrading mid-conversation.
- **[User Researcher Agent](./skills/reviewer-guides/user-researcher.md)** — Specialist sub-agent for synthesizing interviews, support tickets, and qualitative feedback. Pull this in when you need a dedicated research analysis pass on a big data set.
- **[Executive Agent](./skills/reviewer-guides/executive.md)** — Sub-agent that reframes technical updates and decisions for a leadership audience. Useful for preparing board updates, exec syncs, or investor materials.
- **[Engineer Agent](./skills/reviewer-guides/engineer.md)** — Sub-agent that reviews specs for technical gaps, feasibility concerns, and missing edge cases. Run this before sharing a PRD with engineering.
- **[Weekly Salesforce Pipeline Digest](./skills/scheduled-tasks/weekly-salesforce-pipeline-digest/)** — Automated recurring task that queries Salesforce and delivers a pipeline summary to your inbox. Use this as a starting point for any scheduled AI-driven report.

**Learning**
- **[Claude Code for PMs](./learning/claude-code-for-pms.md)** — Curated course by Carl Vellotti. ~10–12 hours, self-paced, free with Claude Pro. The team's shared baseline — recommended before exploring any workflows.

---

## How to Add an Entry

When you add or change something meaningful in the repo, add an entry at the top of this file following the format above. Include:

1. **The date** — `YYYY-MM-DD`
2. **A short title** — describe what changed in plain language
3. **What's new** — 1–2 sentence summary
4. **Each item** — link, what it does, when to use it

The goal: any PM reading this should understand what's available and why it exists — not just that a file was added.

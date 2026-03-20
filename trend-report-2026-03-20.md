# AI PM Trend Scout Report — 2026-03-20

## Executive Summary

The AI-PM repo contains 5 skills, 12 workflows (7 basic + 5 advanced), 5 commands, 3 agents, and 1 scheduled task. All 4 prompt category folders remain empty. External scanning was partially successful: Anthropic's newsroom, engineering blog, and Claude Code documentation were reachable, providing strong signals on platform evolution. GitHub, Hacker News, Substack newsletters (Lenny's, Pragmatic Engineer), and competitor sites (Cursor, Aider) were blocked by network egress restrictions. From the sources scanned, **3 trends qualified** (scored 7+/12) with concrete repo improvement proposals, alongside 3 internal gap proposals from the repo audit.

## Current Repo Baseline

| Category | Count | Items |
|----------|-------|-------|
| **Skills** | 5 | customer-feedback-synthesis, customer-call-questionnaire, strategic-decision-validation, backlog-prioritization, todo-prioritization |
| **Basic Workflows** | 7 | quickstart, user-research-synthesis, competitive-analysis, meeting-notes-to-action-items, sprint-retrospective, weekly-status-update, user-story |
| **Advanced Workflows** | 5 | prd-creation, data-analysis, feature-request-discovery, launch, product-strategy |
| **Commands** | 5 | /prd-creation, /feature-request-discovery, /data-analysis, /launch-pack, /product-strategy |
| **Agents** | 3 | executive, user-researcher, engineer |
| **Scheduled Tasks** | 1 | weekly-salesforce-pipeline-digest |
| **Prompt Categories** | 4 | discovery (empty), execution (empty), analytics (empty), strategy (empty) |

### Coverage Gaps Identified

- **All 4 prompt folders are empty** — scaffolding exists, zero prompts contributed after 7 days
- **No multi-agent or agent team patterns** — the repo has 3 isolated agents but no guidance on composing them or using Claude Code's agent teams feature
- **No plugin architecture awareness** — Claude Code now has a full plugin system with marketplaces, but the repo has no skill or guide covering plugin creation or distribution
- **No stakeholder communication skill** — executive agent reviews but nothing drafts comms
- **No OKR/metric skill** — analytics prompt folder lists these as intended content but nothing exists
- **No sprint planning workflow** — retro exists but no planning counterpart
- **No design/UX review agent** — specs go through PRD pipeline with no UX scrutiny
- **No hooks or automation patterns** — Claude Code hooks enable powerful automation but the repo doesn't cover them

---

## Top Trends & Proposals

### 1. Claude Code Agent Teams & Multi-Agent Orchestration — Score: 10/12

**Signal:** Claude Code now supports agent teams (experimental) — multiple Claude instances working together with shared task lists, inter-agent messaging, and coordinated work. This is a major platform capability that enables parallel code review, competing-hypothesis debugging, and cross-layer feature work. The engineering blog post on building a C compiler with parallel Claudes (Feb 2026) demonstrates production-grade multi-agent patterns. The repo's 3 agents (engineer, executive, user-researcher) currently work in isolation with no guidance on composing them.

**Sources:**
- https://code.claude.com/docs/en/agent-teams (agent teams documentation)
- https://www.anthropic.com/engineering (parallel Claudes blog post, Feb 5, 2026)
- https://code.claude.com/docs/en/sub-agents (subagent documentation)

**Scores:** Relevance 3 | Validation 3 | Actionability 3 | Timeliness 1

**Repo Gap:** The repo has 3 agents but no documentation on how to compose them for multi-perspective reviews, no awareness of agent teams, and no patterns for parallel work. The PRD creation workflow uses sub-agent reviews sequentially, but there's no guide on running engineer + executive + user-researcher in parallel, or using agent teams for complex PM workflows like competitive research sprints.

**Proposed Change:**
- **Type:** New workflow + new skill
- **Target:** `workflows/advanced-workflow/multi-agent-review/` + `.claude/skills/multi-agent-review/SKILL.md` + `skills/productivity/multi-agent-patterns.md`
- **Change:** Create a multi-agent review workflow that runs all 3 existing agents in parallel on a spec or PRD using agent teams or parallel subagents. Include a human-readable guide covering: when to use subagents vs agent teams, how to compose the existing 3 agents for comprehensive spec review, and patterns for PM-specific multi-agent workflows (parallel competitive research, multi-perspective risk assessment).
- **Rationale:** The repo already has the agents — it just needs the orchestration layer. Agent teams are the most significant Claude Code capability addition relevant to PM workflows, and the repo has zero coverage. This turns 3 isolated agents into a force-multiplied review team.

---

### 2. Claude Code Plugin System for PM Tool Distribution — Score: 9/12

**Signal:** Claude Code now has a mature plugin system: plugins package skills, agents, hooks, and MCP servers into shareable, versioned bundles with marketplace distribution. This directly impacts the AI-PM repo's mission — the entire repo is essentially a collection of skills, agents, and commands that could be distributed as a plugin. The official docs include a full plugin creation guide, manifest schema, and marketplace submission process.

**Sources:**
- https://code.claude.com/docs/en/plugins (plugin creation guide)
- https://code.claude.com/docs/en/skills (skills documentation showing plugin integration)

**Scores:** Relevance 3 | Validation 3 | Actionability 3 | Timeliness 0

**Repo Gap:** The repo distributes its skills and agents via a git clone. There's no mention of plugins anywhere. PMs on the team must clone the entire repo and manually manage updates. Converting the repo's assets into a Claude Code plugin would enable one-command installation, versioned updates, and marketplace distribution to the broader PM community.

**Proposed Change:**
- **Type:** New workflow + enhancement
- **Target:** `workflows/basic-workflows/plugin-packaging.md` + new `.claude-plugin/plugin.json` at repo root
- **Change:** Create a guide for packaging the repo's skills, agents, and commands as a Claude Code plugin. Include a plugin manifest, migration steps for converting `.claude/` assets to plugin format, and instructions for distributing via a marketplace. Optionally, create a `plugin.json` manifest that turns the entire repo into an installable plugin.
- **Rationale:** The plugin system solves the repo's distribution problem. Instead of every PM cloning the repo and managing updates, they install a plugin. This also opens the door to sharing the PM toolkit with the broader Claude Code community via marketplace.

---

### 3. Anthropic's 81K-Person AI Usage Study — Score: 8/12

**Signal:** On March 18, 2026 (2 days ago), Anthropic published findings from a study of 81,000 Claude users — described as the largest multilingual qualitative AI usage study. This research represents a massive dataset on how people actually use AI, what they want from it, and where gaps exist. For a PM toolkit focused on AI-augmented product work, the study's findings are directly actionable for customer research frameworks, persona development, and product strategy.

**Sources:**
- https://www.anthropic.com/news (March 18, 2026 — "What 81,000 people want from AI")

**Scores:** Relevance 2 | Validation 3 | Actionability 2 | Timeliness 3

**Repo Gap:** The customer-feedback-synthesis skill handles interview/ticket synthesis, but there's no workflow for incorporating large-scale public research findings into product strategy. The repo has no prompt or workflow for analyzing published research studies and extracting product implications.

**Proposed Change:**
- **Type:** New prompt + enhancement
- **Target:** `prompts/discovery/research-study-analysis.md` + enhancement to `skills/customer-research/customer-feedback-synthesis.md`
- **Change:** Create a discovery prompt for analyzing published research studies (like Anthropic's 81K study) and extracting product implications, user segments, and opportunity areas. Enhance the customer-feedback-synthesis skill to handle structured research reports as an input source alongside interviews and tickets. Reference the 81K study as an example use case in the prompt.
- **Rationale:** This seeds the empty discovery prompt folder with a high-value prompt while also connecting to a timely, credible external signal. It gives PMs a framework for turning published research into actionable product insights — a common need that's currently uncovered.

---

### 4. Empty Prompt Library (Internal Gap) — Score: 9/12

**Signal:** All 4 prompt category folders (discovery, execution, analytics, strategy) have been empty since the March 13 launch. READMEs describe intended content but after 7 days, zero prompts have been contributed.

**Sources:** Internal repo audit — `prompts/*/README.md`

**Scores:** Relevance 3 | Validation 3 | Actionability 3 | Timeliness 0

**Repo Gap:** An empty library signals the contribution barrier is too high. The READMEs list what should exist but nobody has seeded the first examples.

**Proposed Change:**
- **Type:** New prompts (4 files)
- **Target:** `prompts/discovery/interview-synthesis.md`, `prompts/execution/prd-draft.md`, `prompts/analytics/okr-writing.md`, `prompts/strategy/competitive-positioning.md`
- **Change:** Seed each category with one exemplar prompt following the repo's prompt writing guidelines. Each prompt should include: purpose, when to use, the prompt itself, and a usage example.
- **Rationale:** Seeding with 4 prompts sets the standard and lowers the contribution barrier from "start from scratch" to "add to something that exists."

---

### 5. Missing Hooks & Automation Guide (Internal Gap) — Score: 8/12

**Signal:** Claude Code hooks enable powerful automation: pre/post tool-use validation, session lifecycle management, permission automation, and quality gates. The repo has no awareness of this system. For PMs, hooks could automate spec validation, enforce review checklists, or auto-format outputs.

**Sources:**
- https://code.claude.com/docs/en/hooks (hooks documentation)
- Internal repo audit — no hooks mentioned anywhere

**Scores:** Relevance 3 | Validation 2 | Actionability 3 | Timeliness 0

**Repo Gap:** The repo teaches PMs how to use skills, agents, and commands, but completely skips hooks — one of Claude Code's most powerful customization features. For PM workflows, hooks could enforce that every PRD gets agent review before completion, or that spec outputs follow a template.

**Proposed Change:**
- **Type:** New workflow
- **Target:** `workflows/basic-workflows/hooks-for-pms.md`
- **Change:** Create a guide covering: what hooks are, how they work, and 3-4 PM-specific hook recipes (auto-run engineer agent review on every spec edit, enforce PRD template compliance, auto-format markdown outputs, validate that required sections exist before marking a PRD complete).
- **Rationale:** Hooks turn manual review steps into automated quality gates. This is the missing "automate your PM workflows" piece that connects the existing skills and agents into reliable pipelines.

---

### 6. Missing Stakeholder Communication Skill (Internal Gap) — Score: 8/12

**Signal:** The repo has an executive agent for reviewing content and a weekly-status-update basic workflow, but no structured skill for drafting stakeholder communications.

**Sources:** Internal repo audit — gap between `skills/reviewer-guides/executive.md` (review-only) and drafting needs

**Scores:** Relevance 3 | Validation 2 | Actionability 3 | Timeliness 0

**Repo Gap:** The executive agent reviews but doesn't create. PMs write stakeholder comms daily with no tool support.

**Proposed Change:**
- **Type:** New skill
- **Target:** `.claude/skills/stakeholder-communication/SKILL.md` + `skills/communication/stakeholder-communication.md`
- **Change:** Skill covering exec update drafting, bad-news framing, cross-functional announcements, and board prep. Pairs with the existing executive agent as a draft→review pipeline.
- **Rationale:** Fills the creation gap. Draft with the skill, review with the executive agent — a complete communication workflow.

---

## GitHub Activity Summary

| Repo | Status |
|------|--------|
| getcursor/cursor | EGRESS_BLOCKED |
| continuedev/continue | EGRESS_BLOCKED |
| sourcegraph/cody | EGRESS_BLOCKED |
| aider-ai/aider | EGRESS_BLOCKED |
| langchain-ai/langchain | EGRESS_BLOCKED |
| microsoft/autogen | EGRESS_BLOCKED |
| crewAI-Inc/crewAI | EGRESS_BLOCKED |
| anthropics/anthropic-cookbook | EGRESS_BLOCKED |
| anthropics/courses | EGRESS_BLOCKED |

> GitHub remains blocked by the network egress proxy. This section will be populated once access is restored.

## Anthropic Ecosystem Activity (Accessible Sources)

| Source | Notable Activity |
|--------|-----------------|
| **Anthropic Newsroom** | Mar 18: "What 81,000 people want from AI" — largest multilingual qualitative AI study. Mar 12: $100M Claude Partner Network investment. Mar 11: Anthropic Institute launched. |
| **Anthropic Engineering** | Mar 6: Eval awareness in Claude Opus 4.6's BrowseComp. Feb 5: Building a C compiler with parallel Claudes — key multi-agent patterns. |
| **Claude Code Docs** | Agent teams (experimental), plugin system with marketplaces, hooks system, scheduled tasks, LSP plugins, `/batch` and `/simplify` bundled skills, agent memory. |

## Newsletter Sources (Blocked)

| Source | Domain | Status |
|--------|--------|--------|
| Lenny's Newsletter | lennysnewsletter.com | EGRESS_BLOCKED |
| The Pragmatic Engineer | newsletter.pragmaticengineer.com | EGRESS_BLOCKED |
| Every.to | every.to | EGRESS_BLOCKED |
| One Useful Thing (Ethan Mollick) | oneusefulthing.org | EGRESS_BLOCKED |
| Simon Willison's Blog | simonwillison.net | EGRESS_BLOCKED |
| Substack Search | substack.com | EGRESS_BLOCKED |

> These should be added to the approved egress list for future runs.

## Trending Repos Discovered

GitHub trending was inaccessible. No repos could be discovered.

## Low-Scoring Signals (Watch List)

| Signal | Score | Why Watch |
|--------|-------|-----------|
| Claude Partner Network ($100M, Mar 12) | 5/12 | Enterprise adoption acceleration could shift what PM tools partners need; not directly actionable for the repo yet |
| Anthropic Institute (Mar 11) | 4/12 | AI safety/governance focus — could eventually warrant a "responsible AI product decisions" skill, but too early |
| Eval awareness in BrowseComp (Mar 6) | 4/12 | Model evaluation integrity is interesting but not PM-workflow-relevant |
| Claude Code LSP plugin support | 5/12 | Code intelligence for Claude Code — relevant for engineering-heavy PMs but not core PM workflows |
| Claude Code `/batch` skill | 6/12 | Parallel codebase changes at scale — powerful but primarily an engineering tool, not PM-specific |

## Repo Health Notes

1. **All 4 prompt folders are empty** — Most visible gap. 7 days post-launch with zero contributions. Seeding is the highest-priority improvement.

2. **CHANGELOG.md missing March 17 update** — The README references "2026-03-17 — New Skills" but the CHANGELOG only has the 2026-03-13 initial release. The 5 new skills are undocumented in the change log.

3. **Inconsistent folder naming** — `workflows/basic-workflows/` uses hyphens in the directory, but README Getting Started links to `workflows/basic Workflows/` (with a space). This breaks on case-sensitive file systems.

4. **No case studies yet** — Template exists but no actual case studies. Like the prompt folders, needs seeding.

5. **No awareness of Claude Code platform capabilities** — The repo teaches skills, agents, and commands but has no content on: hooks (automation), plugins (distribution), agent teams (multi-agent), scheduled tasks (beyond the Salesforce digest), or the `/batch` and `/simplify` bundled skills. This is a significant gap given how fast the platform is evolving.

6. **Network egress blocking most sources** — GitHub, Hacker News, all Substack newsletters, TechCrunch, VentureBeat, competitor blogs, and OpenAI's blog are all blocked. Only Anthropic's own sites (anthropic.com, code.claude.com) are accessible. The scheduled task source list should be updated to prioritize Anthropic ecosystem sources while network restrictions persist, and the blocked domains should be submitted for egress approval.

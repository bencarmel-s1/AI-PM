# CLAUDE.md

See **[[GOALS.md]]** for identity, ownership areas, quarterly goals, and stakeholders.

## Folder Map (S1-PM-OS/)
```
S1-PM-OS/
├── 1-Tasks/                 ← Active + backlog tasks (root OS)
├── 2-Projects/              ← Project specs + execution logs
│   ├── active/              ← In-flight projects
│   ├── backlog/             ← Queued (not started)
│   └── archive/             ← Completed or abandoned
├── 3-Meetings/              ← All meeting notes by stream
│   ├── 1:1s/                ← Direct-report and manager 1:1s
│   ├── Customer Meetings/
│   ├── Engineering Meetings/
│   ├── General Meetings/
│   └── Personal Notes/      ← Daily notes, organized by year (2025/, 2026/)
├── 4-Workflows/             ← Repeatable processes + CLAUDE helpers
│   ├── data-analysis/
│   ├── feature-request-discovery/
│   ├── launch/
│   ├── prd-creation/
│   ├── product-strategy/
│   ├── quarterly-planning/
│   ├── story-breakdown/
│   ├── user-research-synthesis/
│   └── weekly-stakeholder-update/
├── 5-Knowledge/             ← Canonical research, OKRs, references
│   ├── People/              ← Stakeholder profiles, team context
│   ├── Reference/           ← OKRs, fiscal calendar, canonical docs
│   └── Research/            ← Market, user, and competitive research
├── 6-Data/                  ← Data files and datasets
└── .claude/
    ├── skills/              ← 20 Claude skills for PM workflows
    └── hooks/               ← skill-activator.py + model-advisor.py
```

## Ad-hoc Prompts
- `/create-plan` – Build execution plan for new workstreams; link to relevant OKRs.
- `/execute` – Step-by-step implementation when a plan exists.
- `/document` – Update docs after changes (e.g., OKR history, runbooks).

## Daily Loop Habits

These habits make every session better than the last. Each loop compounds over time.

### After each meeting
```
update people file for [Name]
```
Reads the meeting note → extracts signals → proposes dated updates to `5-Knowledge/People/[name].md`. Never auto-writes. Run within 24 hours while context is fresh. Costs 2 minutes; pays back on every future meeting prep.

### When you hit an issue or learn something
Add a rule to the `## Rules` section at the bottom of this file. Format: one sentence, what + why. These accumulate into an increasingly precise instruction set.

### Morning (daily)
```
/standup
```
Pulls from Calendar, Gmail, Jira, open tasks, and goals. Target: 5-minute orientation.

### New project start
Search `2-Projects/archive/` for past similar work before creating anything new.

### Skill refinement
If you use the same workaround twice for a skill, improve it with `skill-creator`. Quality improves with every iteration.

## Context Management Expectations
- Always cite file paths with `@path#L-L` so I can trace context.
- Use subagents (Task tool) for anything requiring >3 file reads, research sweeps, or verbose analysis. Return summaries + direct file citations.
- Stay in main context for quick edits, short reads, or decision discussions.
- Default workflow when uncertain: `/explore` → `/create-plan` → `/execute`.

## Routing Rules
When intent matches one of these, start here — regardless of exact phrasing:

| Intent | Start here |
|--------|-----------|
| Decision-making / priorities | `@GOALS.md` |
| OKR / roadmap status | `@GOALS.md` (current) + `@5-Knowledge/Reference/fy26-okr-history.md` (history) |
| Meeting prep | `@3-Meetings/` (by stream); `@3-Meetings/Customer Meetings/` for customer history |
| New spec or plan | `@2-Projects/active/`; create via `/create-plan` citing relevant OKRs. Move to `archive/` when done. |
| Research / learnings | `@5-Knowledge/Research/` |
| Stakeholder update | `@4-Workflows/weekly-stakeholder-update/` + use `weekly-update` skill |
| Task prioritization | `@1-Tasks/` + use `todo-prioritization` skill |
| Quarterly planning | `@4-Workflows/quarterly-planning/` |
| CLAUDE.md feels stale / Monday weekly review | Use `update-claude-md` skill |
| After a meeting with a stakeholder | `update people file for [Name]` |
| Starting a new project or workstream | Search `2-Projects/archive/` for past similar work first |

## Tools & Skills

### External Tools (MCP-connected)
| Tool | Use for |
|------|---------|
| **Jira** | Create/update issues, epics, sprints, worklogs — primary task tracking |
| **Confluence** | Read/write internal docs, specs, status reports |
| **Slack** | Search channels, read threads, draft and send messages |
| **Google Workspace** | Gmail, Calendar, Docs, Sheets, Drive, Slides |
| **Figma** | Read designs, generate diagrams, implement UI from specs |

> Tip: MCP tools require separate setup. See your Claude Code documentation for how to connect these.

### Claude Skills (`.claude/skills/`)
| Skill | Trigger when… |
|-------|--------------|
| `daily-loop` | **Run this every morning** — full day orchestrator: standup + today's meeting prep + compounding checklist |
| `standup` | Morning standup only — Calendar, Gmail, Jira, People context, tasks |
| `update-people-file` | After any meeting with a stakeholder — extract signals and update their People file |
| `weekly-update` | Drafting stakeholder update email |
| `meeting-prep` | Prepping for any upcoming meeting |
| `synthesize-research` | Raw notes → structured insights |
| `customer-feedback-synthesis` | Analyzing 3+ feedback sources into themes + opportunities |
| `customer-call-questionnaire` | Auditing/improving an interview guide before calls |
| `draft-prd-section` | Writing a specific PRD section grounded in project context |
| `multi-agent-review` | Parallel engineer + exec + user-researcher review on a spec |
| `backlog-prioritization` | Ranking backlog by strategic leverage |
| `todo-prioritization` | Prioritizing a personal task list |
| `stakeholder-communication` | Drafting exec updates, bad-news framing, cross-functional announcements |
| `strategic-decision-validation` | Pressure-testing a strategic direction before committing |
| `web-research` | Researching topics, competitive intel, reading URLs |
| `data-analysis` | Analyzing datasets, running Python/notebooks |
| `make-slides` | Creating HTML/CSS presentation decks |
| `skill-creator` | Creating or improving a Claude skill |
| `skill-security-review` | Auditing a skill file for malicious content before installing |
| `spin-up` | Setting up a new project's CLAUDE.md |
| `update-claude-md` | Auditing CLAUDE.md for staleness; weekly maintenance |

### Hooks (`.claude/hooks/`)
| Hook | Fires on | What it does |
|------|----------|-------------|
| `skill-activator.py` | Every prompt | Matches prompt against skill triggers; injects a YES/NO skill check |
| `model-advisor.py` | Every prompt | Scores complexity; prints a visible model recommendation in terminal |

Keep this file current whenever goals, workflows, tools, or key links change. Use it as the default starting point for any new Claude session in this workspace.

---

## Rules

*Accumulated from sessions — each entry is a specific fix or pattern learned. Add new rules here ad-hoc; audit weekly with `update-claude-md`.*

- Always run `skill-security-review` before installing any new skill — prevents prompt injection, data exfiltration, and other supply-chain risks from untrusted skill files.

# PM Operating System

A structured, Claude-powered knowledge system for product managers. Fork it, adapt it to your context, and start running a more intentional PM practice in under an hour.

---

## What This Is

This OS gives you:
- **A folder structure** that mirrors how PM work actually flows — tasks, projects, meetings, knowledge, data
- **Workflow templates** for repeatable PM activities (launches, PRDs, research synthesis, stakeholder updates)
- **Claude skills** — pre-built AI workflows triggered by slash commands (e.g. `/standup`, `/meeting-prep`, `/draft-prd-section`)
- **Hooks** that auto-suggest the right skill and right Claude model for every prompt
- **Example files** throughout — realistic dummy data showing how each piece is used

---

## Folder Map

```
S1-PM-OS/
├── 1-Tasks/           Weekly checklists + indexed task list
├── 2-Projects/        Active, backlog, and archived project plans
├── 3-Meetings/        Meeting notes organized by type and stream
├── 4-Workflows/       Repeatable PM processes with templates + examples
├── 5-Knowledge/       Stakeholder profiles, product reference, research
├── 6-Data/            Data feeds, integration metrics, usage reports
└── .claude/           Claude skills, hooks, and config
    ├── skills/        20 Claude slash commands for PM workflows
    └── hooks/         Auto skill-matching + model advisor on every prompt
```

---

## Quick Start (5 Steps)

### 1. Set your identity in `GOALS.md`
Replace the Jamie Chen placeholder with your name, role, company, product, and OKRs. This file is loaded by most Claude skills to give them context about your work.

### 2. Update `CLAUDE.md`
- Change company/product references (search for "Acme Analytics" and "Pulse")
- Update Jira project keys if you use Jira
- Add any routing rules specific to your workflow

### 3. Update `.claude/settings.json`
The hook commands use the path `.claude/hooks/...`. Update these to absolute paths pointing to your workspace:
```json
"command": "python3 /YOUR/PATH/TO/.claude/hooks/skill-activator.py"
```

### 4. Populate `5-Knowledge/People/`
Add a `.md` file for each key stakeholder you work with. See `marcus-webb.md` for the format. These are loaded during meeting prep to give Claude context about each person.

### 5. Start your first session
Open Claude Code in this folder and run:
```
/standup
```
This kicks off your morning briefing. Replace example files with real ones as you go.

---

## Claude Skills Reference

| Skill | When to use |
|-------|------------|
| `/standup` | Morning — pulls tasks, goals, Jira, calendar into a 5-min briefing |
| `/daily-loop` | Full day orchestrator — standup + meeting prep + compounding habits |
| `/meeting-prep` | Before any meeting — loads context, past notes, talking points |
| `/update-people-file` | After a stakeholder meeting — extracts signals and updates their profile |
| `/draft-prd-section` | Writing a specific PRD section grounded in project context |
| `/multi-agent-review` | Parallel engineer + exec + user-researcher review on a spec |
| `/strategic-decision-validation` | Pressure-testing a strategic direction before committing |
| `/backlog-prioritization` | Ranking backlog items by strategic leverage |
| `/todo-prioritization` | Prioritizing your personal task list |
| `/stakeholder-communication` | Drafting exec updates, cross-functional announcements |
| `/weekly-update` | Drafting your stakeholder update email |
| `/synthesize-research` | Turning raw interview notes into structured insights |
| `/customer-feedback-synthesis` | Synthesizing 3+ feedback sources into themes |
| `/customer-call-questionnaire` | Auditing/improving an interview guide |
| `/web-research` | Researching topics, reading URLs, competitive intel |
| `/data-analysis` | Analyzing datasets, running Python scripts |
| `/make-slides` | Building HTML/CSS presentation decks |
| `/skill-creator` | Creating or improving a Claude skill |
| `/skill-security-review` | Security audit before installing any skill file |
| `/update-claude-md` | Weekly CLAUDE.md audit and refresh |

---

## How Claude Hooks Work

Two hooks fire on every prompt:

**`skill-activator.py`** — Reads all skills in `.claude/skills/`, matches your prompt against their trigger phrases, and injects a YES/NO recommendation into Claude's context. You get a visible check in the terminal before Claude responds.

**`model-advisor.py`** — Scores prompt complexity and suggests the cheapest capable model:
- Simple Q&A → suggests Haiku (`claude-lite`)
- Complex strategy/analysis → suggests Opus (`claude-deep`)

Set up model aliases in your shell (e.g. `~/.zshrc`):
```bash
alias claude-lite="claude --model claude-haiku-4-5-20251001"
alias claude-deep="claude --model claude-opus-4-6"
```

---

## Adapting to Your Stack

- **No Jira?** Remove Jira references from `CLAUDE.md` and skip the `create-jira-issues` skill (not included here anyway — too company-specific to bundle).
- **Different meeting structure?** Rename the subfolders in `3-Meetings/` to match your actual meeting cadence.
- **Different data sources?** Update `6-Data/` structure and the `daily-loop` skill to pull from your actual data feeds.
- **Want to add skills?** Use `/skill-creator` — it walks you through drafting, testing, and refining new skills.

---

## Philosophy

This OS is designed around a few principles:

1. **Capture close to the source** — Meeting notes go in `3-Meetings/` immediately. Tasks get indexed same day. People profiles get updated after every 1:1.
2. **Skills compound** — Every time you use the same workaround twice, improve the skill. The OS gets smarter as you use it.
3. **Context over memory** — `CLAUDE.md` and `GOALS.md` replace the "re-explain my context every session" tax. Claude starts every session knowing who you are and what you're working on.
4. **Workflows over one-off prompts** — Repeatable work (launches, PRDs, standups) has a workflow template. Don't reconstruct the process from scratch each time.

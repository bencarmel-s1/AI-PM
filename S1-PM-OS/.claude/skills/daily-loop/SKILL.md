---
name: daily-loop
description: >
  Full daily PM workflow orchestrator. Run once each morning to kick off your day.
  Pulls standup from all sources, identifies today's stakeholders, surfaces meeting
  prep, and sets up the end-of-day compounding checklist. The single command that
  replaces 40 minutes of tab-switching. Invoke when the user says "daily loop",
  "start my day", "morning routine", or "/daily-loop".
user-invocable: true
---

# Daily Loop — PM Day Orchestrator

Everything feeds into one workflow. Run this once each morning.

---

## Phase 1: Morning Standup (pull from all sources)

Run the full standup sequence:

1. **Recent work** — `git log --since="yesterday" --oneline` for context on what was touched
2. **Open tasks** — read `1-Tasks/todo_index.md` and `1-Tasks/weekly-checklist.md` (surface unchecked items from today's day section only)
3. **Goals check** — scan `GOALS.md` for any quarterly targets with upcoming deadlines or at-risk items
4. **Jira** — query issues assigned to me, In Progress or recently Done:
   ```
   assignee = currentUser() AND status in ("In Progress", "Done") ORDER BY updated DESC
   ```
   via `mcp__atlassian-mcp-server__jira_search`
5. **Calendar** — fetch today's events via `mcp__google-workspace__calendar_get_events`
6. **Gmail signals** — query `is:unread newer_than:18h` via `mcp__google-workspace__query_gmail_emails`; scan subject + sender only; flag up to 3 urgent items from known stakeholders
7. **People context** — for each calendar attendee, check `5-Knowledge/People/` for a matching file; read their "Communication Style" and "What [Name] Cares About" sections

Output the standup block:

```
## Daily Loop — {{date}}

### Morning Signals (Gmail)
- [URGENT/FYI] {{sender}}: "{{subject}}"
- (clear if nothing flagged)

### Today's Schedule
- {{time}} — {{meeting}}
  Prep: {{1-2 sentences from People file for this attendee}}

### In Progress (Jira)
- {{ISSUE-KEY}}: {{summary}} — {{status + blocker if any}}

### Recently Completed
- {{ISSUE-KEY}}: {{summary}}

### Open Tasks
- {{item from 1-Tasks/todo_index.md}}

### Today's Recurring Checklist
{{unchecked items from today's day section in 1-Tasks/weekly-checklist.md — omit section if all checked}}

### Suggested Focus
{{1-2 sentences on what matters most today, grounded in goals + calendar + Jira}}
```

---

## Phase 2: Set up today's compounding actions

After the standup block, output a **Today's Loop Checklist** based on today's calendar:

```
## Today's Loop Checklist

### After each meeting — run update-people-file:
{{For each calendar event with a known stakeholder, list:}}
- [ ] After [time] [meeting]: update people file for [Name]

### If anything breaks or surprises you:
- [ ] Add a rule to the ## Rules section in CLAUDE.md (one sentence: what + why)

### If you start a new project today:
- [ ] Read 4-Workflows/daily-loop/project-inheritance-template.md first

### End of day:
- [ ] Anything to add to 1-Tasks/todo_index.md?
- [ ] Any skill that frustrated you today? Note it for skill-creator.
```

This checklist is the day's compounding contract — each ticked item makes tomorrow better.

---

## Phase 3: Kick off anything time-sensitive

Scan the standup output for items that need immediate action before the first meeting:

- An urgent Gmail from a stakeholder → surface it and ask if a response draft is needed
- A Jira blocker with a meeting today that could unblock it → flag the connection
- A stalled task that hasn't moved in 3+ days → surface it with a suggested next action

Only surface items that can be acted on *this morning*. Do not surface things that are FYI-only.

---

## Notes

- Total runtime target: under 2 minutes
- If any source is unavailable (Jira down, no calendar), skip gracefully
- The checklist in Phase 2 is the most important output — it is what turns a standup into a compounding system
- After completing the checklist items, the loop closes: people files are updated, rules are added, tomorrow's standup will be richer

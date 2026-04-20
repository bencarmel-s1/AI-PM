---
name: standup
description: Morning briefing from Calendar, Gmail, Jira, People files, Tasks, and Goals. Run each morning for a 5-minute orientation that replaces 40 minutes of tab-switching.
user-invocable: true
---

# Daily Standup Generator

Pull from all connected sources and synthesize a prioritized morning briefing.

## Data Sources

| Source | Tool / Path |
|--------|-------------|
| Calendar | `mcp__google-workspace__calendar_get_events` |
| People context | `5-Knowledge/People/[name].md` |
| Gmail signals | `mcp__google-workspace__query_gmail_emails` |
| Jira (in progress + recent) | `mcp__atlassian-mcp-server__jira_search` |
| Open tasks | `1-Tasks/todo_index.md` |
| Weekly checklist | `1-Tasks/weekly-checklist.md` |
| Quarterly goals | `GOALS.md` |
| Recent git activity | `git log --since="yesterday" --oneline` |

## Instructions

### 1. Gather recent work activity
- Run `git log --since="yesterday" --oneline` to see files committed or changed
- Look for recently edited PRDs, meeting notes, research docs (from git output)
- Read `1-Tasks/todo_index.md` for open items and blockers
- Read `1-Tasks/weekly-checklist.md` — surface unchecked items from today's day section only (e.g. if today is Wednesday, show only `## Wednesday` items)
- Read `GOALS.md` — scan for any quarterly targets with upcoming deadlines or at-risk items

### 2. Check Jira
- Query Jira for issues assigned to me that are In Progress or recently transitioned to Done (last 2 days):
  ```
  assignee = currentUser() AND status in ("In Progress", "Done") ORDER BY updated DESC
  ```
  via `mcp__atlassian-mcp-server__jira_search`
- Surface: issue key, summary, status, and any blockers or review flags
- If Jira is unavailable: fall back to `1-Tasks/todo_index.md` only

### 3. Check Calendar and load People context
- Fetch today's events via `mcp__google-workspace__calendar_get_events` for today
- For each event, identify named attendees
- For any attendee that matches a People file in `5-Knowledge/People/`, read their:
  - "Communication Style" section (or equivalent)
  - "What [Name] Cares About" section (or equivalent)
  - Summarize in 1-2 sentences — include one actionable tip for the meeting
- If no calendar MCP available: skip schedule, note "Calendar not connected"

### 4. Check Gmail for morning signals
- Query Gmail: `is:unread newer_than:18h` via `mcp__google-workspace__query_gmail_emails`
- Scan subject lines and sender names only — do not read full bodies unless subject looks urgent
- Flag up to 3 emails that are:
  - From a stakeholder in `5-Knowledge/People/` (Marcus, Sarah, Priya, Eli, Olivia)
  - OR contain words like "urgent", "decision", "blocked", "FYI", "action required"
  - OR from external customers or leadership
- Skip newsletters, automated notifications, calendar invites
- If inbox is clear: note "No urgent Gmail signals"

### 5. Synthesize and output
- Connect meetings → tickets → blockers (e.g. a Jira ticket blocked by today's sync)
- Prioritize by impact, not recency
- Flag anything overdue or stalled
- Keep each line item to 1 sentence

## Output Format

```
## Standup — {{today's date}}

### Today's Schedule
- {{time}} — {{meeting title}}
  Context: {{1-2 sentences from People file if attendee is a known stakeholder}}
- {{time}} — {{meeting title}} (no People file match)

### Morning Signals (Gmail)
- [{{URGENT/FYI}}] {{sender}}: "{{subject line}}"
- No urgent signals (if inbox is clear)

### In Progress (Jira)
- {{ISSUE-KEY}}: {{summary}} — {{status + next step}}

### Recently Completed
- {{ISSUE-KEY}}: {{summary}}

### Blockers & Risks
- {{blocker}}: {{impact and proposed resolution}}

### Today's Recurring Checklist
{{unchecked items from today's day section in 1-Tasks/weekly-checklist.md — omit if all checked}}

### Suggested Focus
{{1-2 sentences on what matters most today, grounded in goals + calendar + open Jira items}}
```

## Notes

- Target runtime: under 90 seconds
- If any source is unavailable (Jira down, no calendar), skip gracefully — do not fail the whole standup
- The "Suggested Focus" line is the most important output: it should synthesize across all sources, not just repeat the first task
- After running standup: if you have a meeting with a stakeholder today, consider running `/update-people-file [Name]` after that meeting to close the People Loop

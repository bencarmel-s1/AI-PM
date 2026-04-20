---
name: update-people-file
description: >
  Update a stakeholder's People file after any 1:1 or meeting. Invoke whenever
  the user says "update people file for [Name]", "log meeting with [Name]",
  "update [Name]'s profile", or after completing any 1:1 note. Reads the meeting
  note, extracts style signals, decisions, working agreements, and action items,
  then surgically updates 5-Knowledge/People/[name].md without overwriting prior
  observations. This is the core People compounding mechanic — every meeting
  should trigger this skill.
user-invocable: true
argument-hint: "[person-name] [optional: path/to/meeting-note.md]"
---

# Update People File

Close the People Loop: extract signals from a meeting note and propose surgical, dated updates to the stakeholder's profile.

## Instructions

### Step 1 — Resolve the person

Parse the argument for the person's name. Match against the files in `5-Knowledge/People/`:

| Alias | File |
|-------|------|
| Marcus, marcus-webb | `marcus-webb.md` |
| Warwick, warwick-webb | `warwick-webb.md` |
| Petr, petr-gregorica | `petr-gregorica.md` |
| Oli, olivia-grant | `olivia-grant.md` |
| Alex, alex-wazana | `alex-wazana.md` |

If no match found, list available names and ask for confirmation before proceeding.

### Step 2 — Find the meeting note

1. If a file path was passed as the second argument, read that file directly.
2. Otherwise, search for the most recent note mentioning this person:
   - Check `3-Meetings/1:1s/[Person Name] 1:1/` — read the most recently dated file
   - Also check `3-Meetings/Personal Notes/` for the most recent daily note
   - Also check `3-Meetings/General Meetings/` and `3-Meetings/Engineering Meetings/`
3. If multiple candidate notes exist, show the list and ask which to use.

Read the full note before proceeding.

### Step 3 — Extract update candidates

Scan the meeting note for signals across these categories. For each category, collect specific quotes or observations — do not paraphrase to the point of losing specificity:

- **Communication style observations**: Did they react positively to a specific framing? Push back on a format or level of detail? Prefer async vs. sync?
- **Working agreements**: New commitments made (explicit or implicit) — what they will do, what they asked you to do
- **Preferences revealed**: Time preferences, meeting length, preferred channel, presentation style
- **Relationship context**: New context about their role, team pressures, current focus, or priorities
- **Red flags observed**: Any friction signals, topics to avoid, or patterns that created tension
- **Action items**: Concrete next steps assigned to either party

Discard anything already captured in the existing People file — check before flagging as new.

### Step 4 — Present proposed edits (never auto-write)

For each proposed addition, show it as a diff with section context. Format:

```
## Proposed update to 5-Knowledge/People/[name].md

### Section: [Section Name]
ADD (at end of section):
- [2026-04-07] [Specific observation, quoted or closely paraphrased from the note]
  Source: [meeting note file path, line reference if possible]

Accept? yes / no / edit
```

Present sections one at a time or as a grouped list — ask the user's preference. Never write anything to disk before receiving explicit approval per item.

If no new signals were found, say so clearly: "No new observations found that aren't already captured in [name]'s profile."

### Step 5 — Write accepted changes

For each accepted update:
1. Append the dated observation to the relevant section in `5-Knowledge/People/[name].md`
2. Always prefix with `[YYYY-MM-DD]` so the file becomes a dated log, not a flat list
3. Preserve all existing content — only append, never overwrite

After all updates, update the `Last updated:` line at the bottom of the People file to today's date.

### Step 6 — Output summary

```
Updated 5-Knowledge/People/[name].md:
- Added [N] item(s) to "[Section]"
- Updated last-modified date to [date]

Next meeting with [Name]: run /meeting-prep [name] to load this context.
```

If nothing was updated: "No changes made to [name].md."

## Notes

- The value of this skill compounds over time: each run makes the next meeting prep richer. Run it within 24 hours of any stakeholder meeting while the context is fresh.
- If a People file doesn't yet exist for a stakeholder, offer to create one using the template at `Templates/` rather than writing to a blank file.
- Prefer specificity over completeness: 2 high-signal observations are worth more than 10 generic ones.

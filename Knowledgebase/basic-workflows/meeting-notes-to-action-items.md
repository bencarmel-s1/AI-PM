# Template: Meeting Notes → Action Items

## Before you start

**What you need:** Your meeting notes saved as a `.txt` or `.md` file (e.g. `meeting-notes.txt`). Teams transcripts, Zoom AI summaries, or your own typed notes all work.

**Where to put the file:** In the same folder where you start Claude Code. Run `claude` from that folder, then use `@filename` to reference it.

**How to save Teams/Zoom notes:** Copy the text → open a text editor → paste → save as `meeting-notes.txt`.

---

## How to use
Save your notes as a file, then in Claude Code:
`Process @meeting-notes.txt using @meeting-notes-to-action-items.md`

---

## Output Format

### Meeting Summary
**Date:** [date]
**Attendees:** [names + roles]
**Purpose:** [1 sentence]

---

### Action Items by Owner

#### [Owner Name]
| Action Item | Priority | Due Date | Source |
|---|---|---|---|
| [task] | 🔴 High / 🟡 Medium / 🟢 Low | [date] | [meeting context] |

*(repeat section for each owner)*

---

### Decisions Made
- ✅ [decision 1]
- ✅ [decision 2]

### Open Questions / Parking Lot
- ❓ [question needing follow-up]

### Key Dates This Week
- **[Day]:** [event]

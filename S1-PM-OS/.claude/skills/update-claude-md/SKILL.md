---
name: update-claude-md
description: >
  Audit CLAUDE.md against current workspace sources and suggest section-by-section updates
  for user approval. Use this skill whenever the user says 'update CLAUDE.md',
  'audit CLAUDE.md', 'CLAUDE.md review', 'weekly CLAUDE.md', or when a Monday weekly
  review session opens. Never auto-write — always present diffs and wait for explicit
  approval per section before making any changes.
user-invocable: true
---

# CLAUDE.md Maintenance Auditor

Audit CLAUDE.md section-by-section against live workspace sources. Present each flagged
section as a targeted diff for user approval. Collect all approvals first, then write
once. Never auto-write.

## Sources to Check

| CLAUDE.md Section | Sources to Read |
|-------------------|-----------------|
| `## Current Focus` | `5-Knowledge/Reference/fy27-okr-history.md`, 3 most recent files in `3-Meetings/Personal Notes/2026/` (by filename date), `1-Tasks/todo_index.md` |
| `## Folder Map` | Live directory listing of Workspace root (one level deep only) |
| `## Tools & Skills` | All directories in `.claude/skills/` + their SKILL.md `name` frontmatter field |
| `## Who I Am` / Stakeholders | `5-Knowledge/Reference/fy27-okr-history.md`, any files in `5-Knowledge/People/` |
| `## Routing Rules` | Verify every skill name referenced still exists as a directory in `.claude/skills/` |

## Instructions

### Step 1 — Load CLAUDE.md

Read ``CLAUDE.md` in the current working directory` and parse it into its `##` sections.
Hold these as the baseline. Do not write anything yet.

### Step 2 — Audit Each Section

Work through all five rows of the source table above. For each section:

- Read the listed sources.
- Identify specific factual discrepancies: outdated goals, passed milestones, missing
  or removed folders, skills added or deleted, stale immediate tasks, broken skill references.
- Be precise. Cite the exact file and detail that shows the drift
  (e.g., "fy27-okr-history.md shows Q1 GA target achieved — Current Focus still lists it as in progress").

If no drift is found in a section, note "No changes detected" and move on.

**What counts as drift:**
- A quarter or deadline milestone has passed
- An "immediate task" no longer appears anywhere in recent notes or todo_index
- A folder exists on disk but is absent from the Folder Map (or vice versa)
- A skill directory exists in `.claude/skills/` but is absent from the Tools & Skills table (or vice versa)
- A skill name in Routing Rules has no matching directory in `.claude/skills/`

**What does NOT count as drift:**
- Subfolders inside already-documented directories (the map is intentionally shallow)
- Minor prose wording differences that don't change meaning
- Hypothetical future changes not yet grounded in a source file

### Step 3 — Present Changes for Approval

For each section with detected drift, present a focused block:

```
## Section: [Section Name]

CURRENT:
  [verbatim text from CLAUDE.md — exact wording]

SUGGESTED:
  [proposed replacement text]

REASON: [one sentence citing the specific source file and detail]

Accept? [yes / no / edit]
```

Wait for a response before moving to the next section.

If the user says **"edit"**, ask them to paste the corrected text and incorporate it as
the approved version for that section.

If the user says **"no"**, skip that section entirely.

If there are multiple items to change within one section (e.g., three new skills added),
present them as a single combined block — not one interaction per item.

### Step 4 — Apply Approved Changes

After collecting approvals for all flagged sections, apply all accepted edits to
``CLAUDE.md` in the current working directory` in a single write operation.

Confirm: list each section changed, and note today's date as the audit date.

If no sections had accepted changes, close without writing and say so clearly.

## Constraints

- Never write CLAUDE.md until all sections have been reviewed.
- Never rewrite prose style — only update factual content (dates, task lists, skill names, folder names, goal statements).
- Never infer drift without citing a specific source file.
- The `## Routing Rules` table is stable — only flag it if a referenced skill directory is missing.
- This is a factual accuracy audit, not a CLAUDE.md redesign.

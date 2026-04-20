# CLAUDE.md Maintenance Workflow

This workflow audits CLAUDE.md weekly and proposes targeted updates for my approval. It keeps the file accurate without auto-overwriting anything.

## When to Trigger

- Monday mornings (automated via LaunchAgent at 9am)
- Any time CLAUDE.md feels stale or out of date
- After a significant goal shift, org change, or new skill is added

Say "audit CLAUDE.md", "CLAUDE.md review", or "update CLAUDE.md" to run manually.

## What This Produces

A section-by-section review of CLAUDE.md against live sources:
- `## Current Focus` — checked against OKR history and recent daily notes
- `## Folder Map` — checked against live directory structure
- `## Tools & Skills` — checked against actual skill directories
- `## Who I Am` / Stakeholders — checked against OKR history and People files
- `## Routing Rules` — verified that all referenced skills still exist

Each flagged section is presented as a diff with a cited source. I approve, reject, or edit each one. Changes are applied in a single write after all sections are reviewed.

## Files in This Workflow

1. `claude-md-maintenance-workflow.md` — full step-by-step process with prompts
2. `CLAUDE.md` — this file; context for Claude when folder is loaded

## Typical Runtime

~10 minutes when there are changes to review; ~2 minutes when everything is current.

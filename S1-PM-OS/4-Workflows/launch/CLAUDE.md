# Launch Workflow

Everything that happens between "it shipped" and "we're measuring it" — done in under an hour.

## When to Trigger

Say "launch pack", "feature shipped", "create launch artifacts", or "prepare launch comms" when engineering has shipped a feature and you need to notify all audiences.

## What This Produces

All 6 launch artifacts from a single session:
- Release notes (engineering + Confluence)
- Sales enablement brief (what's new, how to pitch, objection handling)
- CS enablement brief (what customers will ask, how to answer)
- Executive announcement (business-impact summary for leadership)
- Customer announcement (changelog / email)
- Internal Slack announcement

## Key Constraints

- Assess launch tier before generating artifacts (Major / Minor / Patch)
- Default to Minor when unsure — scale up if needed
- Patch launches need release notes only; Major launches need all 6 artifacts
- Run a 48-hour signal check after distribution to catch early issues
- Input required: your PRD file + Jira export or sprint notes

## Files in This Workflow

1. `launch-workflow.md` — Full 5-phase workflow, start here
2. `launch-pack-template.md` — Master template that generates all artifacts

## Launch Tiers

- Major: Net-new capability or significant workflow change → all 6 artifacts
- Minor: Enhancement or improved UX → release notes + sales/CS brief + Slack
- Patch: Bug fix or performance improvement → release notes only

## The 5-Phase Process

- Phase 1 — Readiness Check: What actually shipped vs. what was planned?
- Phase 2 — Generate Pack: One session produces all audience artifacts
- Phase 3 — Review Gate: Quick checklist + executive review before anything goes out
- Phase 4 — Distribute: Slack, Confluence, Jira, Sales/CS share
- Phase 5 — Signal Check: 48-hour post-launch check; feeds into measurement phase

## Timeline

~60 minutes total for a full Major launch pack.

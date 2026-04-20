# Quarterly Planning Workflow

This workflow guides the quarterly planning process for reviewing quarter performance and planning the next quarter's execution against FY OKRs.

## When to Trigger

Say "quarterly planning" or "Q planning" at the start of a new quarter or during the last 2 weeks of the current one.

## Two Planning Modes

**Mode A — FY OKR Setting** (start of fiscal year only)
Use the full 4-step workflow to set annual OKRs: review → gather inputs → draft OKRs → align with leadership.

**Mode B — Quarterly Execution Planning** (all other quarters)
FY OKRs are already set. Steps 1 and 3 change:
- Step 1 = score progress against FY OKRs using Jira data (themes + epics)
- Step 3 = produce a quarterly execution plan (sprint milestones, epic priorities) rather than new OKRs

## Jira Hierarchy

Understanding the two-layer structure is required before any review:

| Level | Project | What it represents |
|-------|---------|-------------------|
| Theme | [THEME project key] | Product-level commitment; maps to FY OKR KRs |
| Epic | [ENG project keys] | Engineering delivery; child of a Theme |
| Milestone | RELREC | Formal launch gate (Beta, EA, GA); child of a Theme |
| Story/Task | [ENG project key] | Sprint-level delivery; child of an Epic |

## Context Management Rule

Jira queries return large payloads. **Always save outputs to `2-Projects/active/[Q][FY]-Planning/` before context gets large.** One file per step:
- `q[N]-jira-snapshot.md` — raw Jira query results summary
- `q[N]-review.md` — scored Q review
- `q[N]-inputs-summary.md` — stakeholder input synthesis
- `q[N]-execution-plan.md` — Q execution plan (Mode B) or `q[N]-okrs-draft.md` (Mode A)
- `q[N]-stakeholder-brief.md` — leadership comms

## What This Produces

- Scored review of previous quarter performance against FY OKRs
- Theme → Epic → Milestone status snapshot
- Stakeholder input synthesis (Mode A) or carryover/risk analysis (Mode B)
- Execution plan with sprint milestones (Mode B) or draft OKRs (Mode A)
- Aligned roadmap priorities

## Key Constraints

- FY OKRs are set annually — quarterly planning aligns execution to them, not the other way around
- OKRs should be outcome-based, not output-based
- Limit to 3-4 objectives max (Mode A)
- Key Results must be measurable with a known baseline
- Get Sarah/Alex alignment before finalizing

## Files in This Workflow

1. `quarterly-planning-workflow.md` - Full step-by-step workflow with prompts
2. `1-review-last-quarter.md` - Step 1: Review previous quarter performance (Jira-grounded)
3. `2-gather-inputs.md` - Step 2: Collect stakeholder input
4. `3-draft-okrs.md` - Step 3: Draft OKRs (Mode A) or execution plan (Mode B)
5. `4-review-and-finalize.md` - Step 4: Review and lock with leadership
6. `okr-template.md` - OKR format template
7. `q[N]-capacity-planner.md` (in `2-Projects/active/[Q][FY]-Planning/`) - Team capacity roster and sprint allocation; reference during Step 2 for engineering feasibility checks

## Timeline

| Mode | Week 1 | Week 2 |
|------|--------|--------|
| Mode A (FY OKR setting) | Jira pull + review + gather inputs | Draft OKRs + review + finalize |
| Mode B (execution planning) | Jira pull + Q review | Draft execution plan + align with Sarah |

## Key Stakeholders

- **Sarah Park** (Director of Product) — manager; final approval on quarterly priorities
- **Alex Yuen** (SVP, MDR) — executive sponsor; cares about hunt findings and analyst capacity
- **Eli Torres** (Data & Analytics Lead) — data quality and capacity input
- **Marcus Webb** (Engineering Lead) — engineering capacity and feasibility input
- **Eli Torres** (Sr. Manager, MDR Hyperautomation) — cross-team data dependency

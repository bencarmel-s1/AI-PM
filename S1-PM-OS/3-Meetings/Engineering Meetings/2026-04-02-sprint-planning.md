---
title: Sprint Planning — Sprint 24
date: 2026-04-02
attendees: [Jamie Chen, Marcus Webb, Priya Nair, Eli Torres, Dev team (6 engineers)]
topic: Q2 Sprint 24 planning — Onboarding Revamp Phase 2
---

# Sprint Planning — Sprint 24 | Apr 2, 2026

## Sprint Goal
Complete frontend scaffolding for the new onboarding flow and finalize the analytics instrumentation schema.

## Committed Tickets

| Ticket | Description | Owner | Points |
|--------|-------------|-------|--------|
| PULSE-413 | New welcome flow frontend (step 1-3) | Dev team | 8 |
| PULSE-415 | Onboarding funnel instrumentation schema | Eli Torres | 5 |
| PULSE-416 | Empty state UI for dashboard (no data) | Dev team | 3 |
| PULSE-417 | Onboarding checklist component refactor | Dev team | 5 |
| PULSE-438 | Alerts discovery tooltip — copy + placement | Dev team | 3 |

**Total committed:** 24 points

## Stretch Goals
- PULSE-414: Smart defaults backend spike (Marcus + 1 eng) — 5 points
  - Only if instrumentation schema is done by Apr 8

---

## Key Discussions

**Scope clarification on PULSE-413**
The "welcome flow" scope was ambiguous — Marcus and I aligned that Sprint 24 only covers steps 1-3 (account setup + first data source connection). Steps 4-5 (dashboard configuration + invite team) move to Sprint 25.

**Instrumentation dependency**
Eli flagged that the instrumentation schema needs sign-off from legal (data retention policy). He's scheduling that review for Apr 7. If it slips, PULSE-415 will bleed into Sprint 25.

**Design assets**
Priya confirmed all Sprint 24 designs are in Figma and in handoff state. One outstanding question: the empty state illustration — should we use a generic placeholder or commission a new illustration from Brand? Decision needed by Apr 9.

---

## Action Items

| Action | Owner | Due |
|--------|-------|-----|
| Schedule legal review for instrumentation schema | Eli Torres | Apr 7 |
| Decide: placeholder vs. new illustration for empty state | Jamie Chen | Apr 9 |
| Confirm Sprint 25 scope for welcome flow steps 4-5 | Jamie Chen | Apr 14 |

---

## Tags
`#sprint-24` `#PULSE-412` `#PULSE-413` `#engineering` `#onboarding`

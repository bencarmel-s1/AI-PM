---
title: Pulse Onboarding Revamp
status: in-progress
jira-epic: PULSE-412
owner: Jamie Chen
started: 2026-03-10
target: 2026-05-30
---

# Pulse Onboarding Revamp

## Why This Exists

Time-to-first-value is 11 days against a 7-day target (OKR KR1.1). Onboarding completion rate is 64% against an 80% target (OKR KR1.2). Exit surveys point to two root causes:
1. Users don't see value in the first session — the default dashboard shows empty charts
2. The setup checklist is too long (14 steps) and lacks contextual guidance

This project redesigns the activation flow end-to-end.

---

## Goals & Success Criteria

| Metric | Baseline | Target | Deadline |
|--------|----------|--------|----------|
| Time-to-first-value | 11 days | ≤ 7 days | May 30 |
| Onboarding completion | 64% | ≥ 80% | May 30 |
| Activation NPS | 38 | ≥ 45 | June 30 (post-launch) |

---

## Approach

**Phase 1 — Discovery & Design (Mar 10 – Apr 18)**
- [x] Run 8 customer discovery calls to map activation pain points
- [x] Synthesize findings → `5-Knowledge/Research/onboarding-discovery-q1-2026.md`
- [x] Design partner review with Priya Nair
- [x] Align on scope with Marcus Webb (Engineering)

**Phase 2 — Build (Apr 21 – May 16)**
- [ ] Frontend: New welcome flow + progressive checklist (PULSE-413)
- [ ] Backend: Smart defaults — pre-populate dashboard with sample data (PULSE-414)
- [ ] Instrumentation: Funnel analytics at each onboarding step (PULSE-415)
- [ ] Copy: Contextual tooltips and empty-state messaging

**Phase 3 — A/B Test & Launch (May 19 – May 30)**
- [ ] 50/50 split: new vs. existing flow
- [ ] Define success gate: ≥ 8% improvement in completion rate
- [ ] Full rollout if gate met; iterate if not

---

## Dependencies

| Dependency | Owner | Status |
|-----------|-------|--------|
| Analytics instrumentation plan | Eli Torres | 🟡 In review |
| Onboarding copy finalized | Jamie Chen | 🟡 Draft |
| Design handoff (Figma) | Priya Nair | 🟢 Done |
| Backend API for smart defaults | Marcus Webb | 🔴 Not started |

---

## Open Questions
- Do we show real customer data or sample data in the smart defaults? (Decision needed by Apr 25)
- Should the checklist be dismissible? Risk: users skip steps that are actually needed for value.

---

## Related Links
- Jira Epic: PULSE-412
- Figma: [Onboarding v2 designs — link placeholder]
- Research synthesis: `5-Knowledge/Research/onboarding-discovery-q1-2026.md`
- Sprint planning notes: `3-Meetings/Engineering Meetings/2026-04-02-sprint-planning.md`

# Story Breakdown: [Feature Name]

**PRD Source:** `[feature]-prd-final.md`
**Destination:** [Jira: PROJECT-KEY / GitHub: org/repo]
**Date:** [YYYY-MM-DD]
**PM:** [Your name]
**Status:** [Draft / Review / Pushed]

---

## Summary

| Metric | Value |
|---|---|
| Total Epics | [N] |
| Total Stories | [N] |
| Total Story Points | [N] |
| Estimated Sprints | [N] |
| V1 Scope | [One line — what this delivers] |
| Out of Scope (V1) | [Bullet list from PRD] |

---

## Epic Overview

| # | Epic | Stories | Points | Priority |
|---|---|---|---|---|
| 1 | [Epic name] | [N] | [N] | [P0 / P1 / P2] |
| 2 | [Epic name] | [N] | [N] | [P0 / P1 / P2] |
| 3 | [Epic name] | [N] | [N] | [P0 / P1 / P2] |

---

## Epic 1: [Epic Name]

**Scope:** [One sentence — what this epic delivers and when it's done]
**Priority:** [P0 / P1 / P2]
**Suggested Sprint:** [Sprint N]
**Total Points:** [N]

---

### Story 1.1: [Title]

**User Story:**
As a [persona], I want to [action] so that [outcome].

**Description:**
[2–3 sentences of context. What does this enable? What are the edge cases the engineer needs to know about? What is NOT included in this story?]

**Acceptance Criteria:**
- [ ] [Specific, verifiable behavior — not "it works", but "when X happens, Y is shown"]
- [ ] [Second criterion]
- [ ] [Third criterion]
- [ ] [Edge case or error state, if applicable]

**Story Type:** [Feature / Bug / Tech Debt / Spike]
**Labels:** [frontend / backend / API / data / infra / design]
**Story Points:** [1 / 2 / 3 / 5 / 8]
**Dependencies:** [Story title(s) this is blocked by, or "None"]

---

### Story 1.2: [Title]

**User Story:**
As a [persona], I want to [action] so that [outcome].

**Description:**
[Context]

**Acceptance Criteria:**
- [ ] [Criterion]
- [ ] [Criterion]
- [ ] [Criterion]

**Story Type:** [Feature / Bug / Tech Debt / Spike]
**Labels:** [labels]
**Story Points:** [points]
**Dependencies:** [dependencies or "None"]

---

*(Repeat for each story in this epic)*

---

## Epic 2: [Epic Name]

**Scope:** [One sentence]
**Priority:** [P0 / P1 / P2]
**Suggested Sprint:** [Sprint N]
**Total Points:** [N]

---

### Story 2.1: [Title]

**User Story:**
As a [persona], I want to [action] so that [outcome].

**Description:**
[Context]

**Acceptance Criteria:**
- [ ] [Criterion]
- [ ] [Criterion]
- [ ] [Criterion]

**Story Type:** [Feature / Bug / Tech Debt / Spike]
**Labels:** [labels]
**Story Points:** [points]
**Dependencies:** [dependencies or "None"]

---

*(Repeat structure for all epics)*

---

## Supporting Stories

Stories that aren't tied to a specific epic but are required for the feature to ship.

### Support: Analytics & Event Tracking

**User Story:**
As a data consumer, I want all new user interactions tracked so that I can measure feature adoption and behavior.

**Acceptance Criteria:**
- [ ] [List each analytics event by name: e.g. "alert_triage_started", "alert_dismissed"]
- [ ] Events fire on the correct user action with the correct properties
- [ ] Events appear in [Amplitude / Mixpanel / your tool] within 1 hour of firing

**Story Type:** Tech Debt
**Labels:** backend, data
**Story Points:** [N]
**Dependencies:** [Story that introduces the tracked interactions]

---

### Support: Error States & Empty States

**User Story:**
As a user, I want clear feedback when something goes wrong or there's no data so that I'm never left wondering what happened.

**Acceptance Criteria:**
- [ ] [List each error state: e.g. "API timeout shows 'Something went wrong' with retry button"]
- [ ] Empty state shown when [condition], not a blank screen
- [ ] All error messages are actionable (tell the user what to do next)

**Story Type:** Feature
**Labels:** frontend
**Story Points:** [N]
**Dependencies:** [Stories that introduce the affected UI states]

---

## Dependency Map

```
[Story 1.1] → blocks → [Story 1.3]
[Story 1.2] → blocks → [Story 2.1]
[Story 2.1] → blocks → [Story 2.2]
```

*(Add more as needed. Stories not listed here have no dependencies.)*

---

## Out of Scope (V1)

These items are explicitly excluded from this breakdown. They should be tracked as future backlog items, not added to this sprint.

- [Item from PRD out-of-scope section]
- [Item]
- [Item]

---

## Open Questions

Items that were ambiguous in the PRD and need a decision before the story can be built.

| # | Question | Owner | Needed By |
|---|---|---|---|
| 1 | [Question] | [PM / Eng / Design] | [Sprint N start] |
| 2 | [Question] | [PM / Eng / Design] | [Sprint N start] |

---

## Push Log

*(Filled in after Phase 5)*

| Epic | Jira Epic Key / GitHub Milestone | Stories Created |
|---|---|---|
| [Epic name] | [e.g. WF-1234 / Milestone #3] | [e.g. WF-1235, WF-1236, WF-1237] |
| [Epic name] | [key] | [keys] |

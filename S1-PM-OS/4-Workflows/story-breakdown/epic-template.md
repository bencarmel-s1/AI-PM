# Epic Template

*Use this when pushing a single epic to Jira or GitHub, or when Claude needs a reference for epic structure.*

---

## Epic: [Epic Name]

**Project / Repo:** [Jira: PROJECT-KEY / GitHub: org/repo]
**Feature:** [Parent feature or PRD name]
**PRD Link:** [Link or filename]
**Priority:** [P0 / P1 / P2]
**Target Sprint:** [Sprint N or Q[X] [Year]]

---

### Summary

[2–3 sentences describing what this epic delivers. What does "done" look like for this epic? What customer problem does it solve?]

---

### Scope

**In scope:**
- [Bullet list of what is included in this epic]
- [Be specific enough that an engineer can determine if a task belongs here]

**Out of scope:**
- [What is explicitly NOT in this epic — prevents scope creep]

---

### Stories in This Epic

| # | Story Title | Points | Type | Status |
|---|---|---|---|---|
| 1 | [Story title] | [N] | [Feature / Bug / Tech Debt / Spike] | [To Do] |
| 2 | [Story title] | [N] | [Feature / Bug / Tech Debt / Spike] | [To Do] |
| 3 | [Story title] | [N] | [Feature / Bug / Tech Debt / Spike] | [To Do] |

**Total Points:** [N]

---

### Definition of Done

This epic is complete when:
- [ ] All child stories are closed
- [ ] Feature is deployed to [staging / production]
- [ ] QA has signed off on acceptance criteria
- [ ] Analytics events are firing correctly
- [ ] No P0/P1 bugs open against this epic
- [ ] Release notes drafted (hand off to `../launch/` workflow)

---

### Dependencies

**Blocked by:** [Epic name / ticket key, or "None"]
**Blocks:** [Epic name / ticket key, or "None"]

---

### Labels / Components

[frontend / backend / API / data / infra / design — select all that apply]

---

### Notes

[Any additional context for the engineering team. Architecture decisions made in the PRD. Known risks. Links to design files or specs.]

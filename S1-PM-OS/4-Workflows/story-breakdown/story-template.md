# Story Template

*Use this when pushing a single story to Jira or GitHub, or when Claude needs a reference for story structure.*

---

## Story: [Story Title]

**Project / Repo:** [Jira: PROJECT-KEY / GitHub: org/repo]
**Parent Epic:** [Epic name / Jira Epic key / GitHub Milestone]
**Story Type:** [Feature / Bug / Tech Debt / Spike]
**Priority:** [P0 / P1 / P2 / P3]

---

### User Story

As a **[persona]**, I want to **[action]** so that **[outcome]**.

> Use the personas defined in the PRD. If the story is internal/technical (e.g. logging, infrastructure), use "As an engineer" or "As a data consumer".

---

### Description

[2–3 sentences of context. Answer: what does this enable? What are the important edge cases? What is NOT included in this story that an engineer might expect?]

---

### Acceptance Criteria

Each criterion must be independently verifiable by QA without asking the PM.

- [ ] [Specific behavior: "When [condition], [system] does [action]"]
- [ ] [Second criterion]
- [ ] [Third criterion]
- [ ] [Edge case: "If [edge condition], [system] shows/does [specific fallback]"]
- [ ] [Error state: "If [error], user sees [specific message] with [specific action]"]

> **AC quality check:** If a criterion uses the words "correctly", "properly", "well", or "easily" — rewrite it. Those words are not verifiable.

---

### Out of Scope

[Explicit list of what this story does NOT cover. Prevents scope creep mid-sprint.]

- [Not included item]
- [Not included item]

---

### Design Reference

[Link to Figma file, design spec, or mockup. "TBD" if design is not ready yet — in that case, flag as blocked by design.]

---

### Labels / Components

[frontend / backend / API / data / infra / design — select all that apply]

---

### Story Points

**Estimate:** [1 / 2 / 3 / 5 / 8]

| Points | Meaning |
|---|---|
| 1 | Trivial — less than half a day |
| 2 | Small — about 1 day |
| 3 | Medium — 2–3 days |
| 5 | Large — about 1 week |
| 8 | Needs splitting — flag before planning |

---

### Dependencies

**Blocked by:** [Story title / ticket key, or "None"]
**Blocks:** [Story title / ticket key, or "None"]

---

### Notes

[Any implementation context, architecture decisions, or links to relevant documentation. Keep this short — if it needs a long explanation, that's a sign the story scope is too large.]

# Standup Eval Rubric

**DO NOT MODIFY THIS FILE.** It is the immutable eval harness.
The agent optimizes SKILL.md against these criteria — not the criteria against the skill.

Each criterion is worth 10 points. Max score: 100.

---

## Criteria

### C1 — Date header present (structural)
Output must contain a line matching `## Standup — YYYY-MM-DD` or `## Standup — [date]`.
- 10: header present
- 0: missing

### C2 — Schedule section present (structural)
Output must contain a `### Today's Schedule` section (or equivalent heading).
- 10: section present with at least one entry
- 5: section present but empty
- 0: section missing entirely

### C3 — People file context used (quality)
For scenarios with known stakeholders (Marcus, Sarah, Priya, Eli), at least one meeting entry must include a "Context:" or insight line about the stakeholder.
- 10: stakeholder insight present with an actionable tip
- 5: stakeholder mentioned but no insight
- 0: no stakeholder context despite known attendees

### C4 — Gmail signals section present (structural)
Output must contain a `### Morning Signals` or equivalent section.
- 10: section present, newsletters/automated notifications filtered out
- 5: section present but includes noise (newsletters, build bots)
- 0: section missing

### C5 — Jira section present with ticket keys (structural)
Output must contain an In Progress section with Jira ticket keys (e.g. WAY-XXXX format).
- 10: section present with at least one ticket key
- 5: section present but no ticket keys
- 0: section missing

### C6 — Blockers surfaced (quality)
For Scenario C (blocked day), the output must explicitly call out blocked tickets and who is needed.
- 10: blocker named, impact noted, resolution suggested
- 5: blocker mentioned but no resolution
- 0: blocker not mentioned (critical failure for scenario C)
- N/A (10 pts awarded): scenario has no blockers

### C7 — Suggested Focus section is synthetic (quality)
`### Suggested Focus` must reference at least one of: a goal/OKR, a Jira ticket key, or a meeting + ticket connection. Must NOT just restate the first task.
- 10: synthesizes across 2+ sources (e.g. meeting + Jira + goal)
- 5: references one source only
- 0: missing or just restates a task

### C8 — Conciseness (quality)
Total word count of the output should be under 450 words. A standup is orientation, not a report.
- 10: under 350 words
- 7: 350–450 words
- 3: 450–600 words
- 0: over 600 words

### C9 — Graceful fallbacks (resilience)
If a section has no data, it must say so explicitly (e.g. "No urgent Gmail signals") rather than omitting the section or leaving it blank.
- 10: all sections present, empty ones have a fallback message
- 5: some sections silently missing
- 0: multiple sections missing with no explanation

### C10 — Cross-source connection (quality)
The output must draw at least one explicit connection across sources — e.g. "today's 1:1 with Marcus is blocking PULSE-412" or "Gmail from Sarah + PULSE-438 are related."
- 10: explicit connection drawn between meeting/email and a Jira ticket
- 5: connection implied but not stated
- 0: no connections drawn across sources

# Step 1: Review Last Quarter

## Purpose

Honestly assess last quarter's performance to inform next quarter's planning. Learn from what worked and what didn't.

## Jira-Grounded Review Process

Before scoring anything, pull live data from Jira. This is the authoritative source — don't rely on memory or OKR files alone.

### Step A — Pull active themes
```
issuetype = Theme AND assignee = "[Your Name]" ORDER BY priority DESC
```
These are your product-level commitments. Each theme maps to one or more FY OKR KRs.

### Step B — Pull child epics per theme
```
parent = <THEME-XXXX> ORDER BY status ASC
```
Run for each active theme. This surfaces:
- Engineering epics (PULSE, GROW, etc.) — the actual delivery work
- RELREC milestones (Beta, EA, GA) — the formal launch gates

### Step C — Pull sprint delivery
```
team = "[Your Team]" AND fixVersion in ("<Q sprint versions>") AND issuetype in (Epic, Story) ORDER BY status ASC
```
Cross-reference with Step B to see what actually shipped vs. what was planned.

### Step D — Score each theme using Jira data

| Score | Signal in Jira |
|-------|---------------|
| 1.0 | All child epics Closed, at least one RELREC milestone progressing |
| 0.7 | Most epics Closed, Beta or EA milestone open but on track |
| 0.5 | Core epics in progress, all milestones Open but timeline intact |
| 0.3 | Epics still in analysis/refinement, no milestone movement |
| 0.0 | No engineering epics started under this theme |

---

## Process

### 1. Score Each Key Result

For each Key Result from last quarter:

| Score | Meaning |
|-------|---------|
| 1.0 | Fully achieved or exceeded |
| 0.7 | Substantially achieved |
| 0.5 | Made progress but fell short |
| 0.3 | Limited progress |
| 0.0 | No meaningful progress |

**Note:** A "good" OKR score is typically 0.6-0.7. Consistently hitting 1.0 means you're sandbagging.

### 2. Document Each Objective

For each Objective, capture:

```markdown
## Objective: [Name]

**Overall Score:** X.X (average of KRs)

### Key Results

| KR | Target | Actual | Score | Notes |
|----|--------|--------|-------|-------|
| KR1 | ... | ... | ... | ... |
| KR2 | ... | ... | ... | ... |
| KR3 | ... | ... | ... | ... |

### Engineering Epics (from Jira: parent = <THEME-XXXX>)

| Epic | Key | Status | Notes |
|------|-----|--------|-------|
| [Epic name] | PULSE-XXXX | ✅ / 🔄 / ⬜ | |

### Milestone Status (RELREC)

| Milestone | Key | Status | Notes |
|-----------|-----|--------|-------|
| Beta | RELREC-XXXX | Open / In Progress / Closed | |
| EA | RELREC-XXXX | Open / In Progress / Closed | |
| GA | RELREC-XXXX | Open / In Progress / Closed | |

### What Worked
- [Specific thing that contributed to success]
- [Another success factor]

### What Didn't Work
- [Challenge or blocker]
- [Thing we'd do differently]

### Carryover
- [ ] [Unfinished epic/item to consider for next Q]
```

### 3. Identify Cross-Cutting Themes

Look across all objectives for patterns:
- What systemic issues affected multiple objectives?
- What capabilities or processes helped?
- What external factors impacted results?

### 4. Capture Lessons Learned

Document 3-5 lessons to apply next quarter:
- Process improvements
- Planning adjustments
- Dependency management
- Scope/ambition calibration

## Quarter Review Template

```markdown
# Q[N] Review - Product Team

**Review Date:** [Date]
**Quarter:** [Q1/Q2/Q3/Q4 YYYY]
**Overall Score:** X.X (average across objectives)

---

## Summary

[2-3 sentences on overall quarter performance]

**Highlights:**
- [Top win 1]
- [Top win 2]

**Lowlights:**
- [Top miss 1]
- [Top miss 2]

---

## Objective 1: [Name]

[Use template from above]

---

## Objective 2: [Name]

[Use template from above]

---

## Cross-Cutting Themes

### What Enabled Success
- [Theme 1]
- [Theme 2]

### What Blocked Progress
- [Blocker 1]
- [Blocker 2]

---

## Lessons Learned

1. [Lesson 1]
2. [Lesson 2]
3. [Lesson 3]

---

## Carryover Items

Items to consider for next quarter:
- [ ] [Item 1]
- [ ] [Item 2]
- [ ] [Item 3]

---

## Appendix: Full KR Scorecard

| Objective | KR | Target | Actual | Score |
|-----------|-----|--------|--------|-------|
| ... | ... | ... | ... | ... |
```

## Tips for Honest Review

- **Score based on outcomes, not effort**: Hard work doesn't count if results didn't materialize
- **Don't rationalize misses**: "We learned a lot" is fine, but still score the KR honestly
- **Give credit for pivots**: If you intentionally deprioritized something, note why
- **Include external factors**: Market changes, team changes, etc. are valid context
- **Be specific**: "Execution issues" is less useful than "underestimated integration complexity"

## Who Should Be Involved

- **PM (you)** — drives the review; pulls Jira data and scores themes
- **Marcus Webb** — engineering input on epic status and what caused slippage
- **Eli Torres** — data quality and analytics context
- **Sarah Park** — reviews final assessment and aligns on Q priorities

---

## Continue in New Session

Paste this prompt to start Step 1 (or resume it) in a new context window:

```
I'm starting Step 1 of quarterly planning: reviewing last quarter's performance.

Workflow reference: @4-Workflows/quarterly-planning/1-review-last-quarter.md
Full workflow: @4-Workflows/quarterly-planning/quarterly-planning-workflow.md
OKR history: @5-Knowledge/Reference/fy27-okr-history.md
Output file (fill in): @2-Projects/active/[Q][FY]-Planning/q[N]-review.md

Mode: [A (FY OKR setting) or B (Quarterly execution planning)]

Steps to complete:
1. Pull Jira data — active themes (issuetype = Theme AND assignee = "[Your Name]"), child epics per theme (parent = <THEME-XXXX>), sprint delivery (team = "[Your Team]" AND fixVersion in ("<Q sprint versions>"))
2. Score each theme using the Jira-grounded scoring guide (0.0–1.0)
3. Document what worked / what didn't / carryover items per theme
4. Identify 3–5 cross-cutting lessons to apply next quarter
5. Save output to 2-Projects/active/[Q][FY]-Planning/q[N]-review.md

When done, move to Step 2: @4-Workflows/quarterly-planning/2-gather-inputs.md
```

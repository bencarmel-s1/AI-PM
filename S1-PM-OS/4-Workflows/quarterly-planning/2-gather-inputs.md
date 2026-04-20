# Step 2: Gather Inputs

## Purpose

Collect perspectives from stakeholders, customers, and the team to inform quarterly priorities. Good planning requires good inputs.

---

## First Action: Create the Input Files

**Before any stakeholder calls, Claude must create two files in `2-Projects/active/[Q][FY]-Planning/`:**

1. **`q[N]-stakeholder-inputs.md`** — questions to take into each stakeholder call; fill in afterward so Claude can populate the planning docs
2. **`q[N]-pm-inputs.md`** — PM's personal list of items (Jira key + reason) to validate against or add to the execution plan

**Claude prompt to generate both input files:**
```
Create the input files for Q[N] FY[YY] planning:
1. Stakeholder questionnaire → 2-Projects/active/[Q][FY]-Planning/q[N]-stakeholder-inputs.md
2. PM inputs list → 2-Projects/active/[Q][FY]-Planning/q[N]-pm-inputs.md
Use the templates in 2-gather-inputs.md.
```

Once filled in, hand them back with:
```
Fill in the planning docs from q[N]-stakeholder-inputs.md
Update the execution plan from q[N]-pm-inputs.md
```

---

## Stakeholder Inputs Questionnaire Template

```markdown
# Q[N] FY[YY] Stakeholder Inputs — Fill-in Questionnaire
**Fill this out after each stakeholder call, then hand back to Claude to complete the planning docs.**

---

## Sarah Park (Engineering Director)
*Call goal: Approve Q[N] plan; confirm Kafka deferral; validate Identity GA as #1*

**1. What are his top 1–2 priorities for Q[N]?**
- Priority 1:
- Priority 2:

**2. Any non-negotiables he named explicitly?**
-

**3. Any concerns or pushback on the current plan?**
-

**4. Decision on Kafka migrations — OUT to Q[N+1] or STRETCH in S5–S6?**
- Decision:
- Reasoning he gave:

**5. Anything else noteworthy from the call?**
-

---

## Eli Torres (Data & Analytics)
*Call goal: Align on Identity GA timeline; surface Cloud TH risk*

**6. What are his Identity GA readiness expectations? (timeline, what "ready" means to ops)**
-

**7. Cloud TH Q[N+1] GA — does he still think it's realistic if discovery doesn't start until S3–S4?**
-

**8. Any operational priorities or hunting use case inputs for Q[N]?**
-

**9. Any concerns about data engineering capacity or scope dependencies?**
-

**10. Anything else noteworthy from the call?**
-

---

## Marcus Webb (Engineering Manager)
*Call goal: Confirm capacity allocation; commit to PULSE-[EPIC-NUMBER] closure by S1*

**11. Did Petr commit to closing [EPIC-KEY] by end of sprint?**
- Committed? (yes / no / conditional):
- Any caveats or risks he flagged:

**12. Is the ~50% Identity allocation feasible given current team state?**
-

**13. Vacation concentration in S1–S2 — confirmed actuals?**
- Who is out and when (Marek / Zbynek / Stanislav / Valeria):

**14. Marek utilisation — is 10% permanent or temporary?**
-

**15. Cloud TH discovery — does Petr have bandwidth for scoping in S3–S4?**
-

**16. Anything else noteworthy from the call?**
-

---

## Eli Torres (Data dependencies)
*Call goal: Confirm TSET-1134 and QA-1179 timeline*

**17. TSET-1134 (HA Workflow for Identity Alerts) — when can it land? Is S4 realistic?**
- Target sprint:
- Any blockers or dependencies he flagged:

**18. QA-1179 (Security compliance testing) — timeline? Also S4?**
- Target sprint:
- Any blockers or dependencies he flagged:

**19. Can TSET-1134 and QA-1179 run in parallel in S4, or do they need to be sequenced?**
-

**20. Anything else noteworthy from the call?**
-

---

## Customer & Product Signals

**21. Identity GA beta readiness — any signals from beta customers or the ops team?**
-

**22. Enterprise compliance customers — any commitments made for Q[N] delivery you're aware of?**
-

**23. Any other customer input that should shape Q[N] priorities?**
-

---

*Once filled in, hand this file back to Claude with: "Fill in the planning docs from q[N]-stakeholder-inputs.md"*
```

---

## Input Sources

### 1. CEO/Leadership Strategic Priorities

**Meeting:** 30-min 1:1 with Sarah

**Questions to ask:**
- What are the company's top 3 priorities for next quarter?
- Are there any non-negotiable initiatives?
- What would make this a successful quarter for the company?
- Any concerns about current product direction?
- What external factors should we be aware of? (funding, competition, market)

**Capture:**
- Explicit priorities
- Implicit concerns
- Hard constraints

### 2. CTO/Engineering Capacity

**Meeting:** 30-min 1:1 with James

**Questions to ask:**
- What's our engineering capacity next quarter? (headcount, availability)
- Any major technical debt or infrastructure work planned?
- What's feasible vs. ambitious vs. unrealistic?
- Any technical risks or dependencies?
- What didn't get done last quarter that should carry over?

**Capture:**
- Available eng days (1 story point = 1 day)
- Technical priorities/constraints
- Feasibility estimates for big bets

### 3. VP Product/Strategy Alignment

**Meeting:** 30-min 1:1 with Priya

**Questions to ask:**
- How does our roadmap connect to company strategy?
- What user problems should we prioritize?
- Any new research or insights to factor in?
- Cross-team dependencies?
- What's the right balance between new features vs. optimization?

**Capture:**
- Strategic direction
- User problem priorities
- Cross-team considerations

### 4. Customer Feedback & Research

**Self-serve analysis:**
- Review last quarter's user research findings
- Pull top feature requests from Intercom
- Check NPS verbatims for themes
- Review churned customer feedback
- Look at support ticket trends

**Capture:**
- Top 5 user pain points
- Most requested features
- Churn drivers
- Satisfaction trends

### 5. Product Team Input

**Async survey or team meeting:**
- What should we start doing?
- What should we stop doing?
- What should we continue?
- What's the most impactful thing we could build?
- What's holding us back?

**Capture:**
- Team insights on opportunities
- Process improvements
- Morale/capacity considerations

### 6. Competitive & Market Intelligence

**Self-serve research:**
- What have competitors launched recently?
- Any new entrants to watch?
- Market trends affecting our space?
- Customer behavior changes?

**Capture:**
- Competitive threats
- Market opportunities
- External trends

## Input Summary Template

```markdown
# Q[N] Planning Inputs Summary

**Prepared:** [Date]
**Planning for:** Q[N] [Year]

---

## Leadership Priorities

**From Sarah (CEO):**
- Priority 1: [Description]
- Priority 2: [Description]
- Priority 3: [Description]

**Non-negotiables:**
- [Must-do item]

**Concerns:**
- [Concern to address]

---

## Engineering Capacity

**From James (CTO):**
- Available capacity: [X] eng days (1 story point = 1 day)
- Planned tech work: [Infrastructure, debt, etc.]
- Feasibility notes: [What's realistic]

**Technical constraints:**
- [Constraint 1]
- [Constraint 2]

---

## Strategic Direction

**From Priya (VP Product):**
- Strategic focus: [Direction]
- User problems to prioritize: [Problems]
- Cross-team dependencies: [Dependencies]

---

## Customer Voice

**Top pain points:**
1. [Pain point] - frequency/severity
2. [Pain point] - frequency/severity
3. [Pain point] - frequency/severity

**Top requests:**
1. [Feature] - [# of requests]
2. [Feature] - [# of requests]

**Churn drivers:**
- [Reason 1]
- [Reason 2]

---

## Team Input

**Start doing:**
- [Suggestion]

**Stop doing:**
- [Suggestion]

**Continue doing:**
- [Suggestion]

**Blockers identified:**
- [Blocker]

---

## Market Context

**Competitive moves:**
- [Competitor action]

**Market trends:**
- [Trend]

---

## Synthesis: Emerging Themes

Based on all inputs, key themes for next quarter:

1. **[Theme 1]**: [Brief description, supported by which inputs]
2. **[Theme 2]**: [Brief description, supported by which inputs]
3. **[Theme 3]**: [Brief description, supported by which inputs]
```

## PM Inputs List Template

```markdown
# Q[N] FY[YY] PM Inputs — Items to Consider for Execution
**Owner:** [Your Name]
**Quarter:** Q[N] FY[YY]
**Purpose:** PM's personal list of items to validate against or add to the execution plan. Fill in, then hand to Claude with the handover prompt at the bottom.

---

## How to use this
- `IN` — you want this committed in Q[N]
- `STRETCH` — only if capacity allows after priorities are locked
- `FLAG` — needs a conversation before deciding (dependency, scope unclear, stakeholder input needed)

---

## Items

| # | Item | Jira Key | Status | Why it matters |
|---|------|----------|--------|----------------|
| 1 | | | IN / STRETCH / FLAG | |
| 2 | | | IN / STRETCH / FLAG | |
| 3 | | | IN / STRETCH / FLAG | |
| 4 | | | IN / STRETCH / FLAG | |
| 5 | | | IN / STRETCH / FLAG | |

---

## Notes / Context
*Anything that doesn't fit in the table — dependencies, timing constraints, open questions.*

-

---

*Once filled in, use the handover prompt below.*
```

---

## Timeline

| Day | Activity |
|-----|----------|
| Day 1 | Schedule stakeholder meetings |
| Day 2 | Meet with Sarah (CEO) |
| Day 3 | Meet with James (CTO), Priya (VP Product) |
| Day 4 | Pull customer data, team survey |
| Day 5 | Synthesize into Input Summary |

## Tips

- **Listen more than pitch**: This is about gathering, not advocating
- **Look for convergence**: Where multiple sources point to the same thing
- **Note surprises**: Things you didn't expect are often the most valuable
- **Quantify when possible**: "Many customers" is weaker than "47 requests"

---

## Continue in New Session

Paste this prompt to start Step 2 (or resume it) in a new context window:

```
I'm on Step 2 of quarterly planning: gathering stakeholder inputs before drafting the execution plan.

Workflow reference: @4-Workflows/quarterly-planning/2-gather-inputs.md
Full workflow: @4-Workflows/quarterly-planning/quarterly-planning-workflow.md
Q review (done): @2-Projects/active/[Q][FY]-Planning/q[N]-review.md
Capacity planner (done): @2-Projects/active/[Q][FY]-Planning/q[N]-capacity-planner.md
Output file (fill in): @2-Projects/active/[Q][FY]-Planning/q[N]-inputs-summary.md

Mode: [A (FY OKR setting) or B (Quarterly execution planning)]

Steps to complete:
1. Create both input files using the templates in 2-gather-inputs.md:
   - q[N]-stakeholder-inputs.md (stakeholder call questionnaire)
   - q[N]-pm-inputs.md (PM's personal items list)
2. Review what was learned in q[N]-review.md — carryover items and lessons
3. Fill in both input files (you do this; Claude waits)
4. Hand back stakeholder inputs: "Fill in the planning docs from q[N]-stakeholder-inputs.md"
5. Hand back PM inputs: use the handover prompt at the bottom of q[N]-pm-inputs.md
6. Claude verifies all inputs, runs capacity sanity check, updates q[N]-execution-plan.md

When done, move to Step 3: @4-Workflows/quarterly-planning/3-draft-okrs.md
```

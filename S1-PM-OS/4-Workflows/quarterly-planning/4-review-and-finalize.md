# Step 4: Review and Finalize

## Purpose

Get leadership alignment on OKRs, incorporate feedback, and communicate final priorities to the team and company.

## Review Process

### 1. Pre-Meeting Prep

**Before the leadership review:**
- Share draft OKRs doc 24 hours in advance
- Highlight key decisions/tradeoffs for discussion
- Note any risks or dependencies that need input
- Prepare context on any controversial choices

**Attendees:**
- Alex (PM, presenting)
- Sarah (CEO)
- James (CTO)
- Priya (VP Product)

### 2. Leadership Review Meeting

**Agenda (60 min):**
- 5 min: Last quarter recap (scored OKRs)
- 10 min: Input summary highlights
- 25 min: Walk through draft OKRs
- 15 min: Discussion and feedback
- 5 min: Align on next steps

**Discussion questions to prepare for:**
- Why these objectives vs. alternatives?
- Are the targets ambitious enough? Too ambitious?
- What are we explicitly NOT doing and why?
- What happens if we miss a KR?
- Do we have the capacity for this?

**Capture:**
- Explicit feedback on each OKR
- Requests for changes
- Points of alignment
- Unresolved questions

### 3. Incorporate Feedback

After the meeting:
- Update OKRs based on feedback
- Resolve any open questions with follow-ups
- Get async approval on changes if significant
- Prepare final version

**Common feedback types:**

| Feedback Type | How to Handle |
|---------------|---------------|
| "Target too low" | Re-evaluate, find middle ground |
| "Target too high" | Discuss what would need to be true |
| "Wrong objective" | Understand why, consider reprioritizing |
| "Missing something" | Evaluate tradeoffs, might need to swap |
| "Wording unclear" | Clarify and rewrite |

### 4. Final Alignment

Before publishing, confirm:
- [ ] All stakeholders have seen final version
- [ ] No unresolved objections
- [ ] Targets are agreed upon
- [ ] Capacity has been validated
- [ ] Roadmap aligns with OKRs

### 5. Team Communication

**All-hands or team meeting:**
- Present final OKRs
- Explain the "why" behind each objective
- Show how roadmap connects to OKRs
- Answer questions

**Async documentation:**
- Publish OKRs to team wiki/Notion
- Link to roadmap
- Include FAQ for common questions

### 6. Company Communication

**For broader company:**
- Share summary in company all-hands
- Post in #announcements channel
- Include context on how product OKRs ladder to company goals

## Finalization Checklist

```markdown
## Q[N] OKR Finalization Checklist

### Pre-Review
- [ ] Draft shared with leadership 24+ hours before meeting
- [ ] Key decisions/tradeoffs highlighted
- [ ] Baseline data confirmed for all KRs

### Review Meeting
- [ ] Meeting held with CEO, CTO, VP Product
- [ ] All feedback captured
- [ ] Alignment on objectives confirmed
- [ ] Open questions identified

### Post-Review
- [ ] Feedback incorporated into OKRs
- [ ] Follow-up discussions completed
- [ ] Final version approved by leadership

### Communication
- [ ] OKRs published to team wiki
- [ ] Team meeting held to present OKRs
- [ ] Roadmap updated and aligned
- [ ] Company update shared

### Operationalization
- [ ] Tracking dashboard set up
- [ ] Weekly check-in cadence established
- [ ] First progress review scheduled
```

## Final OKR Document Format

See `okr-template.md` for the full template.

The final document should include:
1. Executive summary (1-page overview)
2. Full OKRs with initiatives
3. What we're NOT doing (explicit tradeoffs)
4. Quarterly roadmap view
5. Appendix: inputs and review notes

## Ongoing Governance

Once OKRs are set:
- **Weekly:** Quick progress check in team standup
- **Bi-weekly:** KR metric review and course correction
- **Monthly:** Deep dive on one objective
- **End of quarter:** Full scoring and review (back to Step 1)

## When to Change OKRs Mid-Quarter

OKRs should generally be stable, but change if:
- Major company pivot (rare)
- External shock (market, competitor)
- Fundamental assumption proved wrong
- Resource availability changed dramatically

Process for mid-quarter change:
1. Document why change is needed
2. Get leadership alignment
3. Communicate change and rationale to team
4. Adjust roadmap accordingly

---

## Continue in New Session

Paste this prompt to start Step 4 (or resume it) in a new context window:

```
I'm on Step 4 of quarterly planning: reviewing and finalizing with leadership.

Workflow reference: @4-Workflows/quarterly-planning/4-review-and-finalize.md
Full workflow: @4-Workflows/quarterly-planning/quarterly-planning-workflow.md
Draft plan or OKRs: @2-Projects/active/[Q][FY]-Planning/q[N]-execution-plan.md (Mode B) or q[N]-okrs-draft.md (Mode A)
Inputs summary: @2-Projects/active/[Q][FY]-Planning/q[N]-inputs-summary.md
Q review: @2-Projects/active/[Q][FY]-Planning/q[N]-review.md

Mode: [A or B]

Steps to complete:
1. Prepare q[N]-stakeholder-brief.md — one-page summary for Sarah/Alex review meeting
   - Key decisions embedded in the plan (what we're choosing to do vs. not do)
   - 2–3 things leadership is most likely to push back on, with prepared responses
   - Open questions to resolve in the meeting
2. Run the meeting — capture feedback explicitly per epic/OKR
3. Incorporate feedback; flag any changes needing follow-up approval
4. Finalize: save q[N]-okrs-final.md (Mode A) or lock q[N]-execution-plan.md (Mode B)
5. Draft team communication explaining the "why" behind each priority

Key stakeholders: Sarah Park (final approval), Alex Yuen (executive sponsor)
```

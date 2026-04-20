# Quarterly Planning Workflow with Claude Code
*A repeatable AI-assisted process for setting clear, aligned OKRs every quarter*

---

## The Core Principle

Good quarterly planning is about making hard choices, not listing everything you want to do.

Three or four objectives, firmly prioritized, with measurable key results and leadership alignment — that's what enables a team to execute. Claude accelerates the synthesis and drafting; the decisions are still yours.

---

## Before You Start

Run this workflow in the last two weeks of the current quarter. Earlier than that and you don't have enough performance data. Later and there's no time for proper alignment.

**Two modes — pick the right one:**
- **Mode A (FY OKR Setting):** Used at the start of the fiscal year. Follow all 4 steps to set new annual OKRs.
- **Mode B (Quarterly Execution Planning):** Used every other quarter. FY OKRs are already set. Step 1 becomes a Jira-grounded performance review; Step 3 becomes a sprint-level execution plan rather than new OKRs.

**What you need:**
- Jira access (Themes in PULSE (or your Jira project key))
- Last quarter's OKR file or `@5-Knowledge/Reference/fy27-okr-history.md`
- Access to your key stakeholders for input sessions
- Your product metrics baselines for any KRs you plan to set

> **Context management:** Jira queries return large payloads. Save each step's output to `2-Projects/active/[Q][FY]-Planning/` as its own .md file before the context gets heavy. This also makes outputs reusable across sessions.

---

## The Workflow (Step 0 + 4 Steps)

---

### Step 0 — Pull Jira Context (30 min, before anything else)

**What you're doing:** Getting a live snapshot of theme and epic status from Jira before reviewing any OKR file. This replaces guessing from memory.

Run these three queries in order:

**1. Active themes (your product-level commitments):**
```
issuetype = Theme AND assignee = "[Your Name]" ORDER BY priority DESC
```

**2. Engineering epics per sprint (what actually shipped):**
```
team = "[Your Team]" AND fixVersion in ("<Q sprint versions>") AND issuetype in (Epic, Story) ORDER BY status ASC
```
Sprint version format: e.g. `"27.Q1.S1 (28/Jan-10/Feb)", "27.Q1.S2 (11/Feb-24/Feb)", ...`

**3. Child epics per theme (run for each active theme):**
```
parent = <THEME-XXXX> ORDER BY status ASC
```
This reveals engineering epics and milestones linked to each theme.

**Save the output** to `2-Projects/active/[Q][FY]-Planning/q[N]-jira-snapshot.md` before proceeding to Step 1.

---

### Step 1 — Review Last Quarter (Days 1–2)

**What you're doing:** Honestly scoring last quarter's performance before planning the next one.

This step is often skipped or rushed. Don't. The lessons from last quarter are the most grounded input you have. Teams that skip this tend to repeat the same planning mistakes quarter after quarter.

See `1-review-last-quarter.md` for the full scoring guide and templates.

**Opening prompt:**
```
I want to start quarterly planning with a review of last quarter.
Use @1-review-last-quarter.md to guide me.
Reference my FY OKRs: @5-Knowledge/Reference/fy27-okr-history.md
Jira snapshot: @2-Projects/active/[Q][FY]-Planning/q[N]-jira-snapshot.md

For each theme (scored against FY OKRs):
1. Score each Theme's delivery on a 0.0–1.0 scale using the Jira-grounded scoring guide
2. Note which engineering epics are Done vs. in progress vs. not started
3. Check RELREC milestone status (Beta, EA, GA)
4. Summarize what worked and what didn't
5. Identify carryover epics and risks for next quarter
6. Extract 3–5 lessons to apply going forward

Save the output as 2-Projects/active/[Q][FY]-Planning/q[N]-review.md
```

**What Claude will produce:**
- Scored KR table for each objective
- What worked / what didn't per objective
- Cross-cutting themes across the quarter
- Carryover items list
- Lessons learned

**Key constraint:** Score based on outcomes, not effort. Hard work that didn't move the metric is a 0.3, not a 0.7.

---

### Step 2 — Gather Inputs (Days 3–5)

**What you're doing:** Collecting perspectives from leadership, customers, and the team before drafting a single OKR.

Good OKRs are built on good inputs. The most common planning failure is starting with draft OKRs before hearing from stakeholders — then "gathering input" becomes defending what you already wrote.

See `2-gather-inputs.md` for the full list of input sources, meeting questions, and the input summary template.

**Prompt after gathering inputs:**
```
I've completed stakeholder input sessions and want to synthesize the inputs before drafting OKRs.

My inputs:
- CEO priorities: [paste notes]
- Engineering capacity: @2-Projects/active/[Q][FY]-Planning/q[N]-capacity-planner.md
- VP Product / strategy direction: [paste notes]
- Top customer pain points / feature requests: [paste or reference file]
- Team survey results: [paste or summarize]

Use @2-gather-inputs.md for the input summary format.

Identify:
1. Convergence points — where multiple sources point to the same priority
2. Tensions — where inputs conflict and a tradeoff decision is needed
3. Surprises — anything that challenges your current plan
4. The 3–4 themes most worth turning into Objectives

Save as q[N]-inputs-summary.md
```

**What Claude will produce:**
- Structured inputs summary by source
- Convergence and tension analysis
- 3–4 candidate themes for Objectives

---

### Step 3 — Draft OKRs (Days 6–7)

**What you're doing:** Translating the themes from Step 2 into well-formed OKRs.

See `3-draft-okrs.md` for the full OKR principles, bad vs. good examples, and the drafting checklist.

**Prompt:**
```
Based on the inputs summary @q[N]-inputs-summary.md and my review @q[N]-review.md,
help me draft OKRs for next quarter.

Use @3-draft-okrs.md for OKR quality principles.
Use @okr-template.md for the output format.

For each of the 3–4 themes we identified:
1. Draft an Objective using active, inspiring language
2. Define 2–4 Key Results using the formula: [Metric] from [baseline] to [target]
3. Map the initiatives I've mentioned to the specific KRs they move
4. Flag any KR where I don't have a baseline yet

Hard constraints:
- Maximum 4 objectives
- Key Results must be outcome-based, not output-based
- Each KR must have a known or inferable baseline

Save as q[N]-okrs-draft.md
```

**What Claude will produce:**
- Draft OKRs in the standard format
- Initiative-to-KR mapping
- Flags for missing baselines
- Sanity check on each KR against the "how will we know?" test

**Common mistakes to catch before the review:**
- KRs that say "launch X" instead of "achieve Y"
- Objectives that are really just feature lists
- More than 4 objectives (cut before the review, not after)
- Targets with no baseline

---

### Step 4 — Review & Finalize (Days 8–10)

**What you're doing:** Getting leadership alignment, incorporating feedback, and communicating final priorities.

See `4-review-and-finalize.md` for the meeting agenda, common feedback types, and the finalization checklist.

**Prep prompt (24 hours before the leadership meeting):**
```
I have a leadership review of our draft OKRs tomorrow.
Review @q[N]-okrs-draft.md and help me prepare.

1. Summarize the key decisions embedded in these OKRs
   (what are we choosing to do vs. not do?)
2. Identify the 2–3 things leadership is most likely to push back on
3. Prepare responses to the likely pushback
4. Identify any open questions I should resolve in the meeting
5. Format the draft as a clean one-page summary for the leadership review

Save the one-page summary as q[N]-okrs-leadership-brief.md
```

**Post-meeting prompt:**
```
Here's the feedback from the leadership review: [paste notes]

Update @q[N]-okrs-draft.md to incorporate the feedback.
Flag any changes that need follow-up approval.
Then produce the final version using @okr-template.md.
Save as q[N]-okrs-final.md
```

**Final comms prompt:**
```
The OKRs are finalized. Help me write two communications:
1. A team-facing summary (for an all-hands or async doc) that explains
   the "why" behind each objective and how the roadmap connects
2. A company-facing summary (1 paragraph) for the all-hands announcement

Use @q[N]-okrs-final.md as the source.
```

---

## File Naming Convention

All files live in `2-Projects/active/[Q][FY]-Planning/` (e.g. `2-Projects/Q2-FY27-Planning/`).

| File | Purpose |
|---|---|
| `q[N]-jira-snapshot.md` | Raw Jira query summary (Step 0) — save before context grows |
| `q[N]-review.md` | Scored quarter review by theme, with epic/milestone status |
| `q[N]-inputs-summary.md` | Synthesized stakeholder inputs (Mode A) |
| `q[N]-execution-plan.md` | Sprint-level execution plan by theme (Mode B) |
| `q[N]-okrs-draft.md` | Draft OKRs before leadership review (Mode A) |
| `q[N]-stakeholder-brief.md` | One-page summary for Sarah/Alex review |
| `q[N]-okrs-final.md` | Published, approved OKRs (Mode A) |
| `q[N]-capacity-planner.md` | Team capacity roster, utilisation factors, sprint allocation (Step 2 input); 1 story point = 1 day |
| `q[N]-capacity-vs-work.md` | Sprint-by-sprint capacity vs. allocated work tracker; buffer remaining; theme status (Mode B, created during Step 3) |

---

## Common Failure Modes

| Failure | Prevention |
|---|---|
| Too many objectives | Hard cap at 4 — cut before the review, not after |
| Vague key results | Apply "how will we know?" test to every KR |
| No capacity check | Get engineering input in Step 2 before drafting |
| OKRs ≠ roadmap | Explicitly map roadmap initiatives to KRs in Step 3 |
| Skipping the review | Review last quarter first — lessons shape next quarter |
| Sandbagging targets | Ask: "would I be proud to hit 70% of this?" |

---

## Time Estimate

| Step | Time |
|---|---|
| Step 1 — Review last quarter | 30–45 min |
| Step 2 — Gather inputs | 2–3 days (meetings + async) |
| Step 3 — Draft OKRs | 60–90 min |
| Step 4 — Review & finalize | 1–2 days (meeting + revisions) |
| **Total** | **~2 weeks end-to-end** |

---

*Last updated: April 2026 (added Jira-grounded Step 0, two planning modes, context management pattern) · Part of the Product Management Lifecycle*

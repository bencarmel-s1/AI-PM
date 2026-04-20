# Weekly Stakeholder Update Workflow with Claude Code
*A repeatable AI-assisted process for producing a consistent, high-signal Friday update in 15 minutes*

---

## The Core Principle

Leadership doesn't need to know everything you did. They need to know if the product is on track, what's at risk, and what comes next.

Every word in this update is competing for 2 minutes of attention. Lead with numbers. Put problems in a dedicated section so they can't be missed. Keep it under 500 words. Send it on Friday.

---

## Before You Start

- [ ] Access to Amplitude, Stripe, Intercom (or your metrics sources)
- [ ] Notes on what shipped this week
- [ ] Any blockers or risks to surface
- [ ] Know your stakeholder preferences — see `stakeholder-preferences.md`

---

## The Workflow (4 Steps)

---

### Step 1 — Gather Metrics (5 min)

**What you're doing:** Pulling this week's numbers before writing a single word.

This step comes first intentionally. PMs who write the narrative first and then find metrics to support it produce updates that read as spin. Metrics first forces honesty.

See `gather-metrics.md` for where to pull each metric and what to include.

**Opening prompt:**
```
I need to write my weekly stakeholder update for the week of [date].
Use @weekly-stakeholder-update-workflow.md to guide me.

Step 1: Here are my metrics for this week:
- Teacher Activation Rate: [X%] (last week: [X%], target: [X%])
- MRR: $[X]K ([+/-$X]K WoW)
- Trial Conversion: [X%] (last week: [X%], target: [X%])
- Support tickets: [N] (last week: [N])
- [Any other notable metric]

Flag any metric that is red (>10% below target) — I want to make sure
I don't bury bad news in the draft.
```

**What Claude will produce:**
- Metric snapshot with red/yellow/green status
- Flags for anything that needs to be called out in the TL;DR

---

### Step 2 — Draft Update (8 min)

**What you're doing:** Structuring your inputs into the standard email format.

See `draft-template.md` for the full email structure and section guidelines.
Reference `past-updates/` for tone — the most useful reference is the update from 4 weeks ago (same rhythm, comparable metrics).

**Prompt:**
```
Now draft the update using @draft-template.md.

This week's inputs:
- Metrics (from Step 1 above)
- What shipped: [bullet list]
- In progress: [top 2–3 active projects + status]
- Blockers: [any, or "none this week"]
- Next week priorities: [3 items, tied to OKRs if possible]

Constraints:
- Under 500 words total
- TL;DR max 3 bullets — lead with the most important metric or outcome
- Blockers must include a proposed next step (never just raise a problem)
- Next week priorities must connect to our current OKRs

Use @past-updates/[most-recent-update].md for tone reference.
```

**What Claude will produce:**
- Full draft email following the standard structure
- Flagged sections where tone or content might need your review

---

### Step 3 — Review & Adjust (2 min)

**What you're doing:** A fast quality check before sending.

**Checklist:**
- [ ] All numbers are current (not last week's)
- [ ] No metric is buried that should be in the TL;DR
- [ ] Every blocker has a proposed next step
- [ ] Tone is confident but honest — not spin, not catastrophizing
- [ ] Nothing confidential that shouldn't be in an email

**Prompt if anything needs adjusting:**
```
Adjust the following:
- [Specific change: e.g. "The MRR number is wrong — it's $49.2K not $47.2K"]
- [Specific change: e.g. "Add a next step to the auth blocker"]
- [Specific change: e.g. "The tone on the activation miss reads as defensive — rewrite more directly"]
```

---

### Step 4 — Send & Archive

**What you're doing:** Sending the update and saving a copy for future reference.

**Recipients:** See `stakeholder-preferences.md` for who gets what.

**Standard recipients:**
```
To: [CEO, CTO, VP Product — see stakeholder-preferences.md]
CC: [product-team]
Subject: Product Update - Week of [Month Day, Year]
```

**Archive prompt:**
```
Save the final update as past-updates/[YYYY-MM-DD].md
```

Past updates are used in two ways:
1. Tone reference when drafting future updates
2. Source material for quarterly OKR scoring — the most honest record of what actually happened week to week

---

## File Naming Convention

| File | Purpose |
|---|---|
| `past-updates/YYYY-MM-DD.md` | Archived weekly updates |

---

## Failure Modes to Avoid

| Failure | Prevention |
|---|---|
| Missing metrics | Pull from dashboards first — never write without numbers |
| Too long | Enforce 500-word limit; use bullets, not paragraphs |
| Burying bad news | Red metrics go in TL;DR, blockers get their own section |
| Vague priorities | Tie next week focus to specific OKR key results |
| Skipping a week | One missed update breaks the trust the cadence builds |
| Writing before checking numbers | Metrics first, always |

---

## Time Estimate

| Step | Time |
|---|---|
| Step 1 — Gather metrics | 5 min |
| Step 2 — Draft update | 8 min |
| Step 3 — Review and adjust | 2 min |
| Step 4 — Send and archive | 1 min |
| **Total** | **~15 min with Claude assistance** |

---

*Last updated: April 2026 · Part of the Product Management Lifecycle*

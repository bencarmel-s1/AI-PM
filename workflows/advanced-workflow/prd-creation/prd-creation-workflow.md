# PRD Creation Workflow with Claude Code
*A repeatable AI-assisted process for writing better PRDs faster*

---

## The Core Principle

AI is your thinking partner, not your ghostwriter.

You drive every decision — which template, which strategic angle, which feedback to address. Claude augments your thinking and speeds up execution. The PRD is still yours.

---

## The Workflow (5 Phases)

### Phase 1: Context Setup

Before writing a single word, load full context into Claude.

**@ mention these files in your opening prompt:**
- Your chosen PRD template (`@Carls-PRD-Template.md` or `@Lennys-PRD-Template.md`)
- Your product/company context file (`@your-company-context.md`)
- The Socratic questioning framework (`@socratic-questioning.md`)
- Any relevant user research (`@pain-points.md`, `@survey-results.md`, etc.)

**Opening prompt formula:**
```
Please help me fill out @[your-template] for [feature idea].
Use @[company-context] for product context.
Guide me through the process using @socratic-questioning.md.
My initial ideas are: [brief description of the feature]
```

**Why this works:** Claude has full context about your product, users, and goals — so every question and suggestion is grounded in your actual situation, not generic advice.

---

### Phase 2: Socratic Sharpening (3–5 questions)

Before drafting, Claude asks 3–5 targeted questions to sharpen your thinking:

1. **Problem clarity** — What specific pain point does this solve?
2. **Solution validation** — Why this solution vs. alternatives?
3. **Success criteria** — How will you measure if it worked?
4. **Constraints** — What is explicitly NOT in V1?
5. **Strategic fit** — Why this feature, why now?

**You can answer each question or say "skip"** — Claude will fill in reasonable answers based on your company context. In practice, you'll want to think through at least 2–3 yourself. These answers become the backbone of the PRD.

---

### Phase 3: Generate Multiple Strategic Approaches

Instead of one draft, generate 3 versions with different strategic angles:

- **Version A:** One strategic approach (e.g., conversation-first)
- **Version B:** Another approach (e.g., existing-UI-enhancement)
- **Version C:** Balanced approach (e.g., dual-mode)

**Prompt:**
```
Spin up 3 agents to generate 3 PRD drafts using [template].
Use all the context from our conversation and the research files.
Version 1: [approach A]
Version 2: [approach B]
Version 3: [approach C]
```

This surfaces trade-offs you wouldn't see writing a single draft. You pick the angle that fits — or mix elements from multiple versions.

---

### Phase 4: Multi-Perspective Review

Before sharing with your team, run the PRD through 3 specialist sub-agents:

- **(@_@) Engineer** — Technical feasibility, missing architecture decisions, implementation risks
- **(ಠ_ಠ) Executive** — Business case, revenue framing, what leadership will push back on
- **(^◡^) User Researcher** — Problem validation, user segment gaps, usability risks

**Prompt:**
```
Get reviews from the Engineer, Executive, and User Researcher
sub-agents on [your-prd.md] and consolidate into a review doc.
```

You get expert feedback in minutes instead of waiting for calendar time. Address the feedback before anyone sees your draft.

---

### Phase 5: Address Feedback & Finalize

Work through the review feedback selectively:

- Some items you'll address immediately (missing revenue math, deferred decisions that should be resolved)
- Some you'll defer intentionally (out-of-scope concerns you've already decided against)
- Some will spark new thinking worth incorporating

**Prompt:**
```
Address all the feedback across all three reviewers and save as [feature]-prd-final.md
```

Or selectively:
```
Address the executive feedback — add the revenue math and take a clear position on pricing
```

---

## File Naming Convention

| File | Purpose |
|---|---|
| `[feature]-prd-v1.md` | Strategic approach A |
| `[feature]-prd-v2.md` | Strategic approach B |
| `[feature]-prd-v3.md` | Strategic approach C |
| `[feature]-prd-combined.md` | Mixed version with your chosen elements |
| `[feature]-prd-review.md` | Consolidated agent feedback |
| `[feature]-prd-final.md` | Production-ready PRD |

---

## Time Estimate

| Phase | Time |
|---|---|
| Context setup + Socratic questions | 10–15 min |
| Reviewing 3 draft versions | 10–15 min |
| Reviewing agent feedback | 10 min |
| Addressing feedback | 15–20 min |
| **Total** | **~45–60 min for a production-quality PRD** |

Compare to writing a PRD from scratch: typically 4–8 hours.

---

## What Makes a Good Company Context File

The richer your `company-context.md`, the better every PRD will be. Include:

- Product description and key differentiators
- Target personas (with job titles and core needs)
- Current priorities and goals (quarterly)
- Competitive landscape
- Key metrics (ARR, churn, NPS, etc.)
- Team structure and squad ownership
- Revenue model and pricing tiers

Store this file in your project's `.claude/` folder as `CLAUDE.md` so Claude loads it automatically every session.

---

## Which Template to Use?

**Carl's PRD Template** — use when:
- Complex feature with multiple stakeholders
- Need to align on both problem AND solution
- Enterprise customers require detailed specs
- Engineering team prefers detailed requirements

**Lenny's PRD Template** — use when:
- Smaller feature or early-stage idea
- Want to move fast and iterate
- Discovery phase — validating direction before full spec
- New stakeholders need a quick read

Both work with this workflow. The Socratic questions and agent review apply equally to either.

---

## Sub-Agents Required

This workflow uses these sub-agents from `.claude/agents/`:
- `engineer.md` — (@_@) Technical feasibility specialist
- `executive.md` — (ಠ_ಠ) Strategic framing specialist
- `user-researcher.md` — (^◡^) Research synthesis specialist

If you don't have these set up, copy them from the course materials or the community agent library.

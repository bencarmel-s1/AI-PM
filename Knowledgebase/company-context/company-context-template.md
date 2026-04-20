# [Company Name] — Product Context

> **How to use this file:** Fill in each section for your product. The richer this file, the better every PRD Claude writes will be. @ mention it at the start of any PRD session: `@company-context.md`
>
> Store the filled-in version in your project's `.claude/` folder as `CLAUDE.md` so Claude loads it automatically every session without you having to mention it.

---

## Company Overview

**[Company Name]** is a [brief description — what it does and for whom].

**Founded:** [year]
**Employees:** [total] ([breakdown by department if useful])
**Customers:** [number and type]
**Revenue:** [$X ARR / MRR], growing [X]% [month/quarter]-over-[month/quarter]
**Funding:** [stage and amount, e.g. Series A — $8M]

---

## Product

[2-3 sentences describing the core product. What are the main modules or surfaces?]

**Key differentiator:** [What makes this product different from alternatives in one sentence?]

---

## Target Customers

**Primary segment:** [e.g. Mid-size tech companies, 50-200 employees]

**Personas:**

- **[Persona 1 title]** — [What they need from the product, what their day looks like]
- **[Persona 2 title]** — [What they need from the product, what their day looks like]
- **[Persona 3 title]** — [What they need from the product, what their day looks like]

---

## Market Position

**Key competitors:**
- **[Competitor 1]** — [1-line description of their positioning and your differentiation]
- **[Competitor 2]** — [1-line description]
- **[Competitor 3]** — [1-line description]

**Our edge:** [What we do better than anyone else, in plain language]

---

## Current Priorities

**[Quarter/Year] Goals:**
1. [Goal 1 — ideally with a specific metric]
2. [Goal 2]
3. [Goal 3]

**Strategic initiatives:**
- **[Initiative name]** — [1-2 sentences on what it is and why it matters now]
- **[Initiative name]** — [1-2 sentences]

---

## Team Structure

**Leadership:**
- **[Name]** — [Title] ([brief background])
- **[Name]** — [Title]
- **[Name]** — [Title, your direct manager]

**Product team:**
- [X] Product Managers
- [X] Engineers ([squad structure if relevant])
- [X] Designers
- [X] User Researchers

---

## Customer Insights

**What customers love:**
- "[Direct quote from a customer]"
- "[Direct quote]"

**What customers want more of:**
- [Top feature request 1]
- [Top feature request 2]
- [Top feature request 3]

**Recent signals:**
- [X]% of churned customers cited [reason] as primary reason for leaving
- [X]% of support tickets are about [topic]
- NPS score: [X] (industry average: [X])

---

## Business Model

**Pricing tiers:**
- **[Tier name]:** $[X]/user/month — [what's included]
- **[Tier name]:** $[X]/user/month — [what's included]
- **[Tier name]:** $[X]/user/month — [what's included]

**Key metrics:**
- Average deal size: $[X]/year
- CAC: $[X]
- LTV: $[X]
- Payback period: [X] months
- Monthly churn: [X]%

---

## How to Use This File

When starting a PRD session with Claude, include this file in your prompt:

```
Please help me fill out @Carls-PRD-Template.md for [feature].
Use @company-context.md for product context.
Guide me through the process using @socratic-questioning.md.
My initial ideas are: [brief description]
```

Claude will use everything in this file to tailor its questions, draft the problem statement, suggest realistic success metrics, and frame the business case in terms of your actual goals — not generic product advice.

---

## Example (Filled In)

> **[Your Product]** is an enterprise cybersecurity platform (endpoint + cloud + identity security) for mid-size and enterprise security teams.
>
> **Founded:** 2020 | **Employees:** 120 | **Customers:** 850 enterprise accounts | **Revenue:** $4.2M ARR, targeting $6M | **Funding:** Series B — $32M
>
> **Personas:**
> - **SOC Analysts (Tier 1)** — need fast alert triage with inline context; processing 80+ alerts/day, <5 min per alert
> - **Threat Hunters** — need deep multi-turn investigation sessions across endpoint, cloud, and identity telemetry
> - **CISOs** — need MTTD/MTTR improvements for board reporting and ROI justification on platform spend
>
> **Q2 Goals:** (1) Reach $6M ARR, (2) Launch AI Investigation Assistant, (3) Reduce churn driven by "too manual" complaints
>
> **Key metrics:** Avg deal $4,900/yr · CAC $3,200 · LTV $18,000 · Churn 2.1%/mo

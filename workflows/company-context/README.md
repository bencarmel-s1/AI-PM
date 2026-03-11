# Company Context Workflow

This folder contains templates and examples for giving Claude persistent, accurate context about SentinelOne — so every PRD, spec, and analysis Claude writes is grounded in how we actually work, who our customers are, and what our priorities are.

Without this context, Claude gives generic product advice. With it, Claude reasons about your specific tradeoffs, personas, and business model.

---

## What's in this folder

| File | Purpose |
|---|---|
| `company-context-template.md` | Blank template — use this to understand the structure |
| `company-context-sentinelone.md` | Starting point for SentinelOne PMs — company-wide info pre-filled, area-specific sections left for you to complete |

---

## How to use it

### Step 1 — Copy and fill in your version

Copy `company-context-sentinelone.md` and save it as `CLAUDE.md` inside your project's `.claude/` folder:

```
your-project/
└── .claude/
    └── CLAUDE.md    ← paste your filled-in context here
```

Claude loads `CLAUDE.md` automatically at the start of every session in that folder — no need to reference it manually.

### Step 2 — Fill in the `[YOUR AREA]` sections

The pre-filled file contains two types of sections:

- **Company-wide** — already filled in with SentinelOne's public information. Review and correct anything that's outdated, but don't rewrite these from scratch.
- **`[YOUR AREA]`** — intentionally left blank. These sections are specific to your product squad: your current OKRs, your team structure, customer quotes from your interviews, metrics relevant to your surface.

The more you fill in, the better Claude performs. A context file with real quotes, real metrics, and real tradeoffs is dramatically more useful than one with placeholders.

### Step 3 — Reference it in your sessions

If you haven't set up `CLAUDE.md` yet, you can still reference the file manually at the start of any session:

```
Please help me write a PRD for [feature].
Use @company-context.md for product context.
My initial ideas: [brief description]
```

For the full PRD workflow, combine it with the other files in `workflows/advanced-workflow/prd-creation/`:

```
Please help me fill out @Carls-PRD-Template.md for [feature].
Use @company-context.md for product context.
Guide me through the process using @socratic-questioning.md.
My initial ideas: [brief description]
```

---

## What to put in each section

### Current Priorities
Your squad's current OKRs or quarterly goals — ideally with specific metrics. This is the most valuable section because it lets Claude push back when a proposed feature doesn't connect to anything you're actually trying to move.

Example:
> **Q2 2026 Goals:**
> 1. Increase Purple AI weekly active users from 12% to 25% of licensed accounts
> 2. Reduce mean time to investigate (MTTI) for SOC analysts using AI triage by 40%
> 3. Achieve CSAT ≥ 4.4/5 for the AI features onboarding experience

### Customer Insights
Real quotes from customer interviews, NPS verbatims, or support ticket patterns. These give Claude the language and pain points to use when framing problems — much more effective than describing your users in abstract terms.

### Team Structure
Your squad's actual composition. Helps Claude calibrate scope — it won't suggest a 6-month build if it knows you have 3 engineers.

---

## Keeping it current

A stale context file is worse than a sparse one — Claude will reason from outdated goals and metrics.

Update your context file:
- At the start of each quarter (priorities, OKRs)
- After major customer research rounds (new quotes, shifted pain points)
- When your team structure changes

A good rule of thumb: if you'd update your team's onboarding doc, update this file too.

---

## Related files

- [`getting-started/claude-md-setup.md`](../../getting-started/claude-md-setup.md) — How to set up `CLAUDE.md` for persistent context
- [`workflows/advanced-workflow/prd-creation/`](../advanced-workflow/prd-creation/) — Full PRD creation workflow that uses this context file
- [`skills/context-management.md`](../../skills/context-management.md) — How Claude's context window works and how to manage long sessions

# PRD Creation with Claude Code

A complete system for writing better PRDs faster using AI as a thinking partner.

---

## What's in This Folder

| File | What It Is |
|---|---|
| `prd-creation-workflow.md` | The full step-by-step workflow — start here |
| `Carls-PRD-Template.md` | Comprehensive template (Problem → Solution → Launch) |
| `Lennys-PRD-Template.md` | Minimal 7-question template for faster PRDs |
| `socratic-questioning.md` | Question framework Claude uses to sharpen your thinking |

---

## Quick Start (30 seconds)

Open Claude Code in your project and paste this:

```
Please help me fill out @Carls-PRD-Template.md for [your feature].
Use @[your-company-context.md] for product context.
Guide me through the process using @socratic-questioning.md.
My initial ideas are: [2-3 sentences about the feature]
```

Don't have a company context file yet? Start with [`workflows/company-context/company-context-sentinelone.md`](../../company-context/company-context-sentinelone.md) — the SentinelOne sections are pre-filled, just add your area's goals and team details.

Claude will ask you 3–5 sharpening questions, then generate multiple strategic drafts for you to choose from.

---

## The 5-Phase Process

```
1. Context Setup     → @ mention template + company context + research
2. Socratic Questions → Claude sharpens your thinking (3-5 questions)
3. Generate 3 Drafts  → Different strategic angles, pick what fits
4. Agent Reviews      → Engineer + Executive + User Researcher feedback
5. Address & Finalize → Fix what matters, ship the final doc
```

Full details in `prd-creation-workflow.md`.

---

## What You Get at the End

- A production-quality PRD reviewed from 3 expert perspectives
- Before anyone on your team has seen it
- In ~45–60 minutes instead of 4–8 hours

---

## Requirements

This workflow requires these Claude Code sub-agents in your `.claude/agents/` folder:
- `engineer.md` — technical feasibility reviews
- `executive.md` — strategic framing reviews
- `user-researcher.md` — user perspective reviews

These are NOT stored here — they live in `.claude/agents/` because they're project-level AI configuration, not portable templates.

---

## Sharing With Other PMs

Share this entire `prd-creation/` folder. They'll need to:
1. Copy the files into their own project
2. Have the 3 sub-agents set up in their `.claude/agents/` folder
3. Have (or create) a `company-context.md` file for their product — use [`workflows/company-context/company-context-sentinelone.md`](../../company-context/company-context-sentinelone.md) as a starting point

The workflow is the same regardless of product or company.

---

## Template Choice Guide

| Situation | Use |
|---|---|
| Complex feature, multiple stakeholders | Carl's template |
| Simple feature, move fast | Lenny's template |
| Early discovery, validating direction | Lenny's template |
| Enterprise customers need detailed specs | Carl's template |
| You have your own template | Use yours — the workflow adapts |

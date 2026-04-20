# PRD Creation Workflow

A complete system for writing better PRDs faster using AI as a thinking partner.

## When to Trigger

Say "write a PRD", "create a PRD", or "help me spec this feature" when you have a feature idea ready to formalize into a requirements document.

## What This Produces

- A production-quality PRD reviewed from 3 expert perspectives (engineer, executive, user researcher)
- In ~45–60 minutes instead of 4–8 hours
- Before anyone on your team has seen it

## Key Constraints

- Requires 3 sub-agents in `.claude/agents/`: `engineer.md`, `executive.md`, `user-researcher.md`
- Choose template based on complexity: Carl's (complex/enterprise) vs. Lenny's (fast/simple)
- Always run Socratic questioning before drafting — sharpens thinking upfront
- Generate 3 strategic drafts and choose, don't accept the first output

## Files in This Workflow

1. `prd-creation-workflow.md` — Full 5-phase workflow, start here
2. `Carls-PRD-Template.md` — Comprehensive template (Problem → Solution → Launch)
3. `Lennys-PRD-Template.md` — Minimal 7-question template for faster PRDs
4. `socratic-questioning.md` — Question framework Claude uses to sharpen your thinking
5. `example-prd-final.md` — Complete reference PRD

## Template Choice Guide

- Complex feature, multiple stakeholders → Carl's template
- Simple feature, move fast → Lenny's template
- Early discovery, validating direction → Lenny's template
- Enterprise customers need detailed specs → Carl's template

## The 5-Phase Process

- Phase 1 — Context Setup: @ mention template + company context + research
- Phase 2 — Socratic Questions: Claude sharpens your thinking (3–5 questions)
- Phase 3 — Generate 3 Drafts: Different strategic angles, pick what fits
- Phase 4 — Agent Reviews: Engineer + Executive + User Researcher feedback
- Phase 5 — Address & Finalize: Fix what matters, ship the final doc

## What's Next

Once the PRD is finalized, use `../launch/` to generate all launch artifacts when the feature ships.

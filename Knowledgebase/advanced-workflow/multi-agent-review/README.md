← [Back to advanced workflows](../README.md)

# Multi-Agent Review with Claude Code
*Run all 3 specialist agents in parallel on any spec or PRD — get a unified review in one session*

---

## The Core Principle

Three perspectives catch more than one. Instead of running the engineer, executive, and user-researcher agents separately and stitching their feedback together manually, this workflow fans them out in parallel and synthesizes their input into a single, prioritized review document.

---

## What's in This Folder

| File | What It Is |
|---|---|
| `README.md` | This guide — start here |

> As the team builds on this workflow, add supporting files (example reviews, custom agent configurations) to this folder.

---

## Quick Start (30 seconds)

```
Run the engineer, executive, and user-researcher agents in parallel on @[your-spec.md].
Consolidate all three reviews into a single document organized by priority.
Save the result to [feature]-multi-agent-review.md.
```

That's it. Claude will invoke all three agents, collect their output, and synthesize a unified review.

---

## The 3-Phase Process

### Phase 1: Fan-Out — Run Agents in Parallel

All three specialist agents review the same document simultaneously:

- **(@_@) Engineer** — Finds technical gaps, missing architecture decisions, implementation risks, and edge cases
- **(ಠ_ಠ) Executive** — Evaluates business case, revenue framing, strategic fit, and what leadership will push back on
- **(^◡^) User Researcher** — Checks problem validation, user segment coverage, usability risks, and research gaps

```
Review @[your-spec.md] using all three agents (engineer, executive, user-researcher) in parallel.
Give each agent the full document. Don't summarize or filter the input.
```

### Phase 2: Collect — Gather Perspectives

Each agent produces its standard output:

| Agent | Output Sections |
|---|---|
| Engineer | Ambiguities, Technical Risks, Missing Edge Cases, Complexity Assessment |
| Executive | Strategic Fit, Business Case Gaps, Leadership Concerns, Decision Points |
| User Researcher | Top Themes, Pain Point Validation, Segment Gaps, Research Recommendations |

### Phase 3: Synthesize — Unified Review

The three reviews are merged into a single document, organized by priority rather than by reviewer:

```
Synthesize the three agent reviews into a unified review document.
Organize by priority (critical → important → nice-to-have), not by reviewer.
Where agents agree, call it out as a consensus signal.
Where they disagree, surface the tension and explain both sides.
Save to [feature]-multi-agent-review.md.
```

---

## What You Get at the End

- **One review document** with issues prioritized across all three perspectives
- **Consensus signals** where multiple agents flagged the same concern
- **Tension points** where agents disagree (e.g., engineer says "too complex" while executive says "not ambitious enough")
- **Clear next steps** organized by what to address before sharing the spec

---

## When to Use This

- Before handing off any major spec or PRD to stakeholders
- Before a leadership review or planning session
- After writing a PRD with `/prd-creation` — run this as a final quality gate
- When you want a quick gut-check from multiple perspectives without scheduling 3 separate reviews

---

## Subagents vs Agent Teams

Claude Code offers two ways to run multiple agents:

| Approach | How It Works | Best For |
|---|---|---|
| **Subagents** (default) | Claude spawns agents within a single session — you see all output in one conversation | Most PM workflows. Simpler, faster, all context stays together. |
| **Agent Teams** (experimental) | Multiple Claude instances work in parallel with shared task lists and inter-agent messaging | Very large tasks where agents need to work independently for extended periods (e.g., parallel competitive research across 5+ competitors). |

For spec review, **subagents are the right choice** — the task is well-scoped and benefits from centralized synthesis.

---

## Requirements

This workflow uses these sub-agents from `.claude/agents/`:
- `engineer.md` — (@_@) Technical feasibility specialist
- `executive.md` — (ಠ_ಠ) Strategic framing specialist
- `user-researcher.md` — (^◡^) Research synthesis specialist

All three are pre-installed in this repo. No additional setup required.

---

## File Naming Convention

| File | Purpose |
|---|---|
| `[feature]-multi-agent-review.md` | Unified review document (synthesized from all 3 agents) |

---

## Tips

- **Give agents the full document.** Don't pre-summarize or cherry-pick sections — each agent is designed to scan the entire spec and find what matters from their perspective.
- **Run this after your own editing pass.** The agents will find things you missed, but they're most useful when the spec is already in reasonable shape — not a rough draft.
- **Use the consensus signals.** When all three agents flag the same issue, that's a strong signal to address it before sharing.
- **Don't address everything.** Some feedback will be out of scope or intentionally deferred. The synthesis step helps you triage.

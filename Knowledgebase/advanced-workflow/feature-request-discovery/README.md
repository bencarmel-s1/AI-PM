# Feature Request Discovery with Claude Code

Surface, quantify, and prioritize customer feature requests from Jira — with OKR alignment scoring, revenue weighting, and competitive context — before you start a PRD.

---

## What's in This Folder

| File | What It Is |
|------|------------|
| `feature-request-discovery-workflow.md` | The full 4-phase workflow — start here |
| `feature-request-discovery-template.md` | Blank output template for Claude to fill in |
| `example-feature-request-discovery.md` | Fully worked example (Purple AI) — shows what a finished discovery brief looks like |
| `okr-template.md` | Blank OKR file — fill this in before your first session |

---

## Requirements

**Jira MCP:** Required. Claude queries the "Feature Suggestion and Roadmap" project directly via the Atlassian MCP integration. If you haven't set this up, see [`getting-started/mcp-configuration/`](../../../getting-started/mcp-configuration/).

**Salesforce MCP:** Optional but recommended. Used to pull additional account and deal context for revenue signal. Works without it — Claude will use the `SFDC Acct ACV` and `SFDC Opp ACV` fields already on Jira issues.

**Your OKR file:** Required. Fill in `okr-template.md` before your session and save it as `okrs-[your-name].md` in this folder (or your project folder).

---

## Quick Start (30 seconds)

Open Claude Code in this folder, then paste:

```
I want to run a feature request discovery session for my product line.
Use @feature-request-discovery-workflow.md to guide me.
My product line in Jira is: [YOUR PRODUCT LINE VALUE]
My OKRs are in @okrs-[your-name].md
```

Claude will run the full 4-phase discovery, query Jira live, score every theme against your OKRs, surface revenue signal, flag competitive gaps, and produce a discovery brief ready to hand off to PRD creation.

> **New to Claude Code?** The `@filename` syntax tells Claude to read that file as part of your prompt. Store your OKR file in the same folder you open Claude Code from, then reference it with `@okrs-yourname.md`. Claude reads it directly — no copy-pasting needed.

---

## The 4-Phase Process

```
Phase 1 — Scope & Pull         → Define your area, fetch live Jira issues via MCP
Phase 2 — Quantify & Rank      → Count, rank, age-check, and flag stale requests
Phase 3 — Theme & OKR Align    → Cluster into themes, score each against your OKRs
Phase 4 — Revenue & Synthesis  → Layer in ACV data, competitive flags, 2x2 matrix, brief
```

Full details in `feature-request-discovery-workflow.md`.

---

## What You Get at the End

- A ranked list of feature requests for your product line (top 20 by votes + ACV)
- 4–8 themes with OKR alignment scores (High / Medium / Low / None)
- Revenue signal per theme: ARR represented + Opp ACV at risk (different urgency levels)
- Competitive flags where themes map to known gaps vs. CrowdStrike, Microsoft, Palo Alto, or others
- Staleness warnings for high-vote themes where the underlying requests are 12+ months old
- A 2x2 prioritization matrix (OKR Alignment × Revenue Signal)
- A one-paragraph "recommended starting point for PRD" — defensible, not just Claude's opinion

---

## What's Next

Once you have your discovery brief, the next step is writing the PRD.

Use [`../prd-creation/`](../prd-creation/) to turn your highest-priority finding into a production-quality requirements document — with Socratic questioning and expert agent reviews built in.

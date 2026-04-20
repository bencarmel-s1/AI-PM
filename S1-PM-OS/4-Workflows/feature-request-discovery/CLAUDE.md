# Feature Request Discovery Workflow

Surface, quantify, and prioritize customer feature requests from Jira — with OKR alignment scoring, revenue weighting, and competitive context — before starting a PRD.

## When to Trigger

Say "feature request discovery", "prioritize feature requests", or "what should I build next" when you want to run a structured discovery session against your Jira backlog.

## What This Produces

- A ranked list of feature requests for your product line (top 20 by votes + ACV)
- 4–8 themes with OKR alignment scores (High / Medium / Low / None)
- Revenue signal per theme: ARR represented + Opp ACV at risk
- Competitive flags vs. CrowdStrike, Microsoft, Palo Alto, or others
- Staleness warnings for high-vote themes with 12+ month old requests
- A 2x2 prioritization matrix (OKR Alignment × Revenue Signal)
- A recommended starting point for PRD creation

## Key Constraints

- Requires Jira MCP (Atlassian integration) — queries the "Feature Suggestion and Roadmap" project live
- Salesforce MCP is optional but recommended for revenue signal
- Fill in `okr-template.md` before your session and save as `okrs-[your-name].md`
- OKR file must be current — stale OKRs produce misaligned scoring

## Files in This Workflow

1. `feature-request-discovery-workflow.md` — Full 4-phase workflow, start here
2. `feature-request-discovery-template.md` — Blank output template for Claude to fill in
3. `okr-template.md` — Fill this in before your first session
4. `example-feature-request-discovery.md` — Fully worked example (Pulse Analytics)

## The 4-Phase Process

- Phase 1 — Scope & Pull: Define your area, fetch live Jira issues via MCP
- Phase 2 — Quantify & Rank: Count, rank, age-check, and flag stale requests
- Phase 3 — Theme & OKR Align: Cluster into themes, score each against your OKRs
- Phase 4 — Revenue & Synthesis: Layer in ACV data, competitive flags, 2x2 matrix, brief

## What's Next

Once you have your discovery brief, use `../prd-creation/` to turn the highest-priority finding into a production-quality PRD.

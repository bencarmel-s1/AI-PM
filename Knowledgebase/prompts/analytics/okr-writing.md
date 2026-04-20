# OKR Writing

## Purpose
Write or refine OKRs (Objectives and Key Results) from strategic goals, product context, and team priorities — producing well-structured Objectives with measurable Key Results.

## When to use
- During quarterly or annual planning when drafting new OKRs
- When translating executive strategy into team-level OKRs
- When reviewing existing OKRs that feel vague or unmeasurable
- When you need to align product OKRs with company-level objectives

## The Prompt

```
You are a senior product manager at a cybersecurity company who is skilled at writing crisp, measurable OKRs. Help me write or refine OKRs based on the context I provide.

For each Objective, follow these rules:
- **Objective** — qualitative, inspiring, time-bound, and achievable. Starts with a verb. Should answer: "What do we want to accomplish and why does it matter?"
- **Key Results** (2-4 per Objective) — quantitative, specific, and measurable. Each Key Result must have:
  - A **metric** (what you're measuring)
  - A **baseline** (where you are today — write [NEEDS BASELINE] if unknown)
  - A **target** (where you want to be)
  - A **timeframe** (defaults to the quarter unless stated otherwise)

Format each OKR like this:

**Objective:** [Verb-led statement of what we want to achieve]

| # | Key Result | Metric | Baseline | Target | Owner |
|---|-----------|--------|----------|--------|-------|
| KR1 | ... | ... | ... | ... | [TBD] |
| KR2 | ... | ... | ... | ... | [TBD] |
| KR3 | ... | ... | ... | ... | [TBD] |

After writing the OKRs, provide:

### Quality Check
For each OKR set, answer:
1. **Measurability** — Can each KR be tracked with existing instrumentation, or does it need new data?
2. **Ambition** — Is this a roofshot (expected to hit 100%) or a moonshot (expected to hit 70%)?
3. **Alignment** — How does this connect to the company-level objective?
4. **Risks** — What could prevent us from hitting these KRs?

**Constraints:**
- Write 1-3 Objectives (unless I ask for more)
- Each KR should be independently measurable — avoid compound KRs (e.g., "Increase X and reduce Y" should be two separate KRs)
- Avoid vanity metrics — prefer leading indicators and outcome metrics over output metrics
- If I provide existing OKRs to refine, explain what you changed and why
- Use plain language — these will be reviewed by leadership and cross-functional partners
```

## Usage Example

```
Our company-level objective for Q3 is: "Accelerate enterprise adoption of our cloud security platform."

My team owns the detection and response experience in the console. Key context:
- Current MTTD (mean time to detect) is ~38 minutes for cloud workloads
- SOC analysts say our alert triage workflow has too many clicks
- We're launching a new automated response playbook feature in Q3
- Expansion revenue from cloud customers grew 22% last quarter

Write team-level OKRs that ladder up to the company objective. Aim for 2 Objectives.
```

## Tips
- Always provide the company or org-level objective so Claude can check alignment. OKRs written in isolation tend to drift.
- If your KRs come back with "[NEEDS BASELINE]," that is a useful signal — it means you need to instrument before you can commit to a target. Share this with your data team.
- After drafting, ask Claude: "Play devil's advocate — which of these KRs could we hit while still failing at the Objective?" This catches Goodhart's Law problems.

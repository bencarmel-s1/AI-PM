# Skill: Strategic Decision Validation

Before you present a direction to leadership or commit to a roadmap bet, Claude can help you pressure-test it — surfacing hidden assumptions, alignment gaps, and risk areas you may not have considered.

---

## What this is (and isn't)

Claude won't tell you what decision to make. That's your call. What it will do is help you get clearer on what you're assuming, where you might be exposed, and what questions need explicit alignment before you move.

Think of it as a senior peer reviewing your thinking before the executive presentation.

---

## When to use it

- Before committing to roadmap priorities or major investments
- When you're confident in a direction but want to check your reasoning
- Before leadership or exec reviews where you'll be challenged
- When cross-functional alignment is required but not yet confirmed

---

## How to use it

Give Claude the decision and its rationale:

```
We're planning to prioritize the self-serve onboarding flow over the enterprise customization work next quarter.
Here's our rationale: @q3-decision-brief.md
What assumptions are embedded in this decision? Where are we most exposed?
```

Claude will:
- Surface implicit assumptions about customers, strategy, and constraints
- Assess how well the decision aligns with your stated product goals
- Highlight areas of confidence vs. uncertainty
- Frame the key tensions that need explicit alignment

---

## Going deeper

If you have strategy documents or customer research available, reference them alongside the decision brief:

```
Validate @q3-decision-brief.md against @product-strategy.md and @customer-themes.md.
Where does this decision have strong backing, and where is the support thinner?
```

This gives Claude the context to assess alignment against *your* specific strategy — not just general logic.

---

## Tips

**Use this before, not after.** The output is most useful when there's still time to sharpen your reasoning or pre-align stakeholders — not as a post-hoc rationalization.

**Ask for the tension framing explicitly.** Ending your prompt with "What questions should I be ready to answer in the review?" turns the output into prep material for your actual meeting.

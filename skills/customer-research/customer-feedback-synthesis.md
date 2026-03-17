# Skill: Customer Feedback Synthesis

Claude can help you transform raw customer notes into clear, structured insight — moving from messy inputs to a decision-ready summary without skipping any of the interpretive steps.

---

## What this covers

This skill walks through a four-stage workflow:

1. **Synthesize** — consolidate feedback into recurring themes
2. **Extract pain points** — identify what's actually frustrating customers, grouped by underlying problem
3. **Frame opportunities** — restate pain points as product improvement opportunities
4. **Summarize for decisions** — distill everything into a crisp, strategic summary

You can ask Claude to do all four at once, or step through them individually if you want checkpoints along the way.

---

## Synthesize: themes from raw feedback

Use this after customer calls, interviews, or feedback reviews — any time you have notes that need to become signal.

```
Synthesize the key themes across these customer call notes: @calls/
Focus on what's coming up repeatedly. Don't add interpretation — just surface what customers are actually saying.
```

Claude will group themes by what customers are expressing, not by what individual people said. Useful output before a planning session or stakeholder readout.

---

## Extract: what's actually frustrating them

Once you have themes, or if your feedback is already specific enough, Claude can pull out the underlying pain points:

```
Read @call-notes.md and identify the key customer pain points.
Group them by the underlying problem — not by individual comments.
Describe each pain point in neutral, customer-centric language.
```

The goal is a clean, evidence-based problem list — not a list of complaints or feature requests.

---

## Frame: from pain points to opportunities

Before a roadmap session, translate pain points into opportunity statements:

```
Based on the pain points we identified, reframe each as a potential improvement opportunity.
Use outcome-oriented language. Don't propose specific features or designs.
```

This gives you a product-relevant frame for prioritization conversations without prematurely locking in solutions.

---

## Summarize for decisions

When you need something leadership-ready — before a prioritization call, quarterly review, or investment decision:

```
Consolidate the themes, pain points, and opportunities from this session into a concise decision-support summary.
Highlight the key strategic implications. Don't recommend a specific path.
```

---

## Tips

**Run all four stages in one pass** if the feedback is dense enough:

```
Process @customer-calls/ through these stages:
1. Synthesize themes
2. Extract pain points
3. Frame as opportunities
4. Produce a decision-support summary
```

**Save intermediate outputs.** On longer sessions, write each stage to a file before moving on:

```
Write the themes synthesis to customer-themes.md
```

This gives you a checkpoint you can `@reference` in future sessions — useful if the conversation gets long or you need to pick up where you left off.

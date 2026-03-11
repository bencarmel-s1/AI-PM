# Product Strategy Workflow with Claude Code
*A repeatable AI-assisted process for developing defensible product strategies*

---

## The Core Principle

Strategy is about choices, not documents.

AI can research faster, apply frameworks more rigorously, and challenge your thinking harder than a solo brainstorm. But only you have the context, judgment, and understanding of your constraints to make the actual decisions. The strategy is yours — AI helps you think it through.

---

## The Workflow (3 Phases)

### Phase 1: Diagnose — Understand the Situation

**Goal:** Build a clear picture of the competitive landscape and your strategic challenge before making any choices.

**What to bring:**
- Your product context (target customer, team size, budget, constraints)
- The strategic question leadership asked you
- Any existing competitive knowledge

**Opening prompt:**
```
I need to develop a product strategy for [area].
My context:
- Product: [what it does, who it serves]
- Team: [size and composition]
- Budget/constraints: [key limits]
- Question from leadership: [what they asked]

First, spin up parallel agents to research our top 3 competitors:
[Competitor 1], [Competitor 2], [Competitor 3]

Each agent should research: AI/feature strategy, pricing, target segment,
what's working vs not, and where there's whitespace.
```

**What Claude will do:**
- Launch 3 parallel agents (one per competitor)
- Each researches features, pricing, target market, gaps
- Consolidate findings with key insights and whitespace analysis
- Synthesize a diagnosis: what's the real strategic challenge?

**Key outputs:**
- Competitive landscape summary
- Your strategic whitespace (where you can win)
- A crisp diagnosis statement

---

### Phase 2: Make Choices — Build Your Guiding Policy

**Goal:** Make 5 hard strategic decisions that will define your approach. Each choice has real tradeoffs.

**The 5 Strategic Choice Categories:**

1. **Focus vs Breadth** — Where do you concentrate limited resources?
2. **Competitive Response** — How do you react to (or ignore) competitor moves?
3. **Business Model** — How does your strategy interact with pricing and margins?
4. **Product Scope** — Where does this initiative live in your product?
5. **Risk Tolerance** — How fast do you move given uncertainty?

**Prompt for each choice:**
```
Present me with 3 options (A/B/C) for [choice category].
After I choose, play devil's advocate — challenge my choice with
the strongest possible counterargument. Then let me stick with it
or reconsider.
```

**How devil's advocate works:**
- You choose A, B, or C
- Claude challenges your choice with the toughest pushback
- You either stick with it (and explain why) or reconsider
- Your final answer is recorded

**Why this matters:** Better to hear hard questions from Claude than from your CEO. Every choice you defend becomes more defensible.

**Tracking your choices:**
```
Choice 1 (Focus): [Your final answer]
Choice 2 (Competition): [Your final answer]
Choice 3 (Business model): [Your final answer]
Choice 4 (Scope): [Your final answer]
Choice 5 (Risk): [Your final answer]
```

---

### Phase 3: Synthesize — Create the Strategy Document

**Goal:** Turn your 5 choices into a complete, coherent strategy using Rumelt's Kernel.

**Prompt:**
```
Based on my 5 strategic choices, synthesize a complete strategy
using Rumelt's Strategy Kernel framework. Save as [product]-strategy.md.

Structure:
- Diagnosis: The strategic challenge (from competitive research + situation)
- Guiding Policy: My strategic approach (from my 5 choices)
- Coherent Actions: 6-month roadmap (Q1 + Q2 initiatives, sequenced)
- Critical Assumptions: What needs to be true + how we'll test each
- Competitive Positioning: Why customers choose us vs alternatives
- Risks & Mitigation: Top 5 risks with likelihood and mitigation

Make it feel like MY strategy — reference the specific tradeoffs I made
and show how my choices reinforce each other.
```

**Then create the executive presentation:**
```
Create an executive slide deck outline from [product]-strategy.md.
13 slides: Title, Executive Summary, Diagnosis, Competitive Landscape,
Strategic Direction, Tradeoffs, Roadmap Q1, Roadmap Q2, Success Metrics,
Critical Assumptions, Why We'll Win, Risks & Mitigation, The Ask.
Save as [product]-strategy-slides.md.
```

**Key outputs:**
- `[product]-strategy.md` — Complete strategy doc
- `[product]-strategy-slides.md` — Executive presentation outline

---

## Common Prompt Patterns

**Research competitors in parallel:**
```
Spin up 3 agents in parallel to research [Competitor 1], [Competitor 2],
[Competitor 3]. Each should cover: features launched, pricing model,
target segment, what's working, what's not, and whitespace.
Consolidate findings with 3 key insights.
```

**Make a strategic choice:**
```
Present 3 options for [strategic area]. After I choose, challenge it
as devil's advocate, then let me stick or reconsider.
```

**Pressure-test a strategy:**
```
Read @[strategy.md]. Apply @gibson-biddle-dhm.md to score each
strategic initiative: Is it delightful? Hard to copy? Margin-enhancing?
Flag anything that scores low on Hard to Copy — that's where we lack defensibility.
```

**SWOT before strategy:**
```
Before I develop my strategy, help me run a SWOT analysis using
@swot-analysis.md. My context: [product + situation]. Focus especially
on Threats (what could make this strategy fail?) and Opportunities
(what's the market giving us right now that won't last?).
```

---

## File Naming Convention

| File | Purpose |
|------|---------|
| `[product]-strategy.md` | Complete Rumelt Kernel strategy doc |
| `[product]-strategy-slides.md` | Executive presentation outline |
| `[product]-swot.md` | Optional: SWOT analysis pre-strategy |

---

## What Makes a Good Strategy

**The Rumelt test — fill in these blanks:**

> "The key challenge is ___. Our approach is to ___ for ___ [target customer]. We'll differentiate by ___. This means we won't ___."

If you can't fill in the last blank (what you WON'T do), you don't have a strategy yet.

**The coherence test:**
- Do all your Q1 and Q2 initiatives reinforce each other?
- Would removing any one initiative weaken the whole strategy?
- Are there any initiatives that contradict each other?

**The tradeoff test:**
- Would a reasonable person disagree with your guiding policy?
- If everyone would agree with it, it's probably a goal, not a strategy.

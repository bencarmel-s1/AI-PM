# /product-strategy

Build a structured product strategy — competitive research, five strategic choices, and a Rumelt Kernel strategy document with executive presentation outline.

Strategy is about choices, not documents. AI helps you think it through. Only you have the context to make the decisions.

## Step 1: Set the scope

Ask the user:
1. What product area are you building strategy for? (e.g., "Singularity Endpoint", "Purple AI", "Cloud CNAPP")
2. What is your time horizon? (6 months or 12 months)
3. What is the key strategic question you're trying to answer?
4. Do you have any existing strategy docs, OKRs, or competitive research to include? (@ mention them, or say "none")

## Step 2: Load frameworks and context

Read:
- `@workflows/advanced-workflow/product-strategy/frameworks/rumelt-strategy-kernel.md`
- `@workflows/advanced-workflow/product-strategy/frameworks/gibson-biddle-dhm.md`
- `@workflows/company-context/company-context-sentinelone.md`
- Any files the user @ mentioned

## Phase 1: Competitive landscape research

Launch 3 parallel agents to research the competitive landscape:
- **Agent 1:** CrowdStrike Falcon — AI/automation strategy, recent product moves, pricing approach, what is and isn't working, whitespace to exploit
- **Agent 2:** Microsoft Defender XDR and Palo Alto Cortex XDR — same dimensions
- **Agent 3:** Emerging threats and whitespace — new entrants, category shifts, underserved segments, areas where all incumbents are weak

Each agent returns: key differentiators, recent strategic moves, customer perception signals, and identified whitespace.

Synthesize into:
- A competitive landscape summary (2-3 paragraphs)
- Your strategic whitespace — where competitors are weak or absent
- A crisp diagnosis statement: "The key challenge is ___"

## Phase 2: Five strategic choices

For each choice below, present 3 options (A/B/C), let the user choose via AskUserQuestion, then challenge their choice briefly before they confirm.

**Choice 1: Focus vs. Breadth** — Where do you concentrate resources?
- A: Double down on your strongest existing segment
- B: Expand into an adjacent segment where you have a beachhead
- C: Broad platform play — defend everywhere

**Choice 2: Competitive Response** — How do you respond to competitor moves?
- A: Ignore and outpace — build what only you can build
- B: Match and differentiate — match table stakes, win on something specific
- C: Actively counter — target their weakest points directly

**Choice 3: Business Model alignment** — How does strategy interact with pricing/margins?
- A: Lead with platform value — drive seat expansion
- B: Lead with module depth — drive upsell per customer
- C: Lead with ecosystem — drive partner/integration revenue

**Choice 4: Product scope** — Where does this strategy live in your product?
- A: Core platform — deeply integrated, hard to extract
- B: Adjacent module — fast to ship, easy to position
- C: New surface — greenfield, separate buyer motion

**Choice 5: Risk tolerance** — How fast do you move given uncertainty?
- A: Fast and bold — ship to learn, accept higher failure rate
- B: Staged — validate with a lighthouse cohort before broad rollout
- C: Conservative — full confidence before broad commitment

## Phase 3: Strategy document

Using the Rumelt Kernel framework, synthesize the competitive research and strategic choices into a strategy document:

1. **Diagnosis** — What is the competitive reality and your key challenge?
2. **Guiding Policy** — Your 5 strategic choices and their rationale
3. **Coherent Actions** — Q1 and Q2 roadmap initiatives that directly execute the strategy (each initiative should reinforce the others)
4. **Critical Assumptions** — What needs to be true for this strategy to work, and how to test each
5. **Competitive Positioning** — Why customers choose you over alternatives (use Gibson-Biddle DHM lens: Delightful, Hard to copy, Margin-enhancing)
6. **Risks and Mitigation** — Top 5 risks with likelihood, impact, and mitigation

Apply the Rumelt test before finalizing:
"The key challenge is ___. Our approach is to ___ for ___ [target customer]. We will differentiate by ___. This means we won't ___."

If the last blank cannot be filled, the strategy is not specific enough yet. Surface this to the user.

Save as `[product-area]-strategy.md`.

## Step 4: Executive presentation outline

Generate a 13-slide executive presentation outline:
1. Situation and key challenge
2-4. Competitive landscape (one slide per major competitor)
5. Our strategic whitespace
6-10. Strategic choices (one slide per choice)
11. 6-month roadmap
12. Critical assumptions and how we will test them
13. What we need from leadership

Save as `[product-area]-strategy-slides.md`.

Confirm: "Strategy complete. Files saved: `[product-area]-strategy.md` and `[product-area]-strategy-slides.md`."

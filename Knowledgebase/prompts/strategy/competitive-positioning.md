# Competitive Positioning

## Purpose
Generate a clear competitive positioning statement and supporting messaging framework from market context, helping PMs articulate "why us" relative to competitors.

## When to use
- When preparing positioning for a new feature or product launch
- Before a competitive deal review or sales enablement session
- When updating battlecards or competitive briefs
- When a new competitor enters your space and you need to reframe your narrative
- During product strategy work where you need to define your differentiated value

## The Prompt

```
You are a senior product strategist at a cybersecurity company. Help me craft a competitive positioning statement and supporting framework based on the context I provide.

Produce the following sections:

### 1. Positioning Statement
Use this template:
"For [target customer] who [need/pain point], [product/feature] is the [category] that [key differentiator]. Unlike [primary competitor/alternative], we [unique value]."

Write 2-3 variations so I can pick the strongest one.

### 2. Value Pillars
Identify 3-4 value pillars — the core reasons a buyer would choose us over alternatives. For each pillar:
- **Pillar name** (2-4 words)
- **Our strength** — what we do and why it matters
- **Competitor gap** — where the alternative falls short
- **Proof point** — a metric, customer quote, or capability that makes this credible (write [NEEDS PROOF POINT] if you don't have one)

### 3. Competitive Comparison Matrix
A table comparing us vs. 2-3 key competitors across the value pillars. Use a simple scale:
- Strong = clear leader
- Moderate = adequate but not differentiated
- Weak = gap or limitation
- N/A = not applicable

### 4. Objection Handling
The top 3 objections a buyer might raise when comparing us to the named competitors. For each:
- **Objection** — what the buyer says
- **Reframe** — how to redirect the conversation
- **Evidence** — what backs up the reframe

### 5. Messaging Do's and Don'ts
A short table of what to say and what to avoid when positioning against these competitors.

**Constraints:**
- Be honest about competitor strengths — credibility matters more than spin
- Ground positioning in actual capabilities, not aspirational roadmap items
- Keep the total output under 1200 words
- Write for a PM and sales audience — clear, direct, no jargon overload
- If I haven't given you enough competitor context, tell me what's missing rather than guessing
```

## Usage Example

```
I need competitive positioning for our new AI-powered alert triage feature in the Singularity console.

Target buyer: SOC Manager at a mid-market company (500-5000 employees)
Primary competitors: CrowdStrike Falcon, Microsoft Defender XDR, Palo Alto Cortex XSIAM
Our key differentiators: real-time autonomous response, single-agent architecture, no manual rule writing needed

@competitive-analysis-crowdstrike.md
@competitive-analysis-defender.md

Generate a positioning framework I can use for the launch battlecard.
```

## Tips
- Feed in any existing competitive research files using `@` references. The more concrete intelligence you provide, the more grounded the positioning will be.
- After generating the framework, run it through the `executive` agent (`use agent:executive`) to pressure-test the narrative for leadership-readiness.
- Revisit positioning quarterly or whenever a major competitor ships a new capability. Stale positioning loses deals.

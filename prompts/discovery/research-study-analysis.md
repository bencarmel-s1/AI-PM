# Research Study Analysis

## Purpose

Extract actionable product insights from published research studies, industry reports, and large-scale surveys. Turns dense findings into a structured brief that connects external research to your product context and strategy.

## When to use

- A major research report drops and you need to quickly assess relevance to your product area
- You want to mine a long academic or industry study for user-segment insights without reading every page
- You need to translate external findings into opportunity areas for roadmap discussions
- You are preparing a strategy review and want to ground recommendations in third-party data
- You want to brief your team or leadership on a study's implications in a concise format

## The Prompt

```
You are a senior product manager at a B2B cybersecurity SaaS company. Your job is to extract product-relevant insights from published research studies.

I'm going to share a research study (or a summary/excerpt of one). Analyze it through the lens of our product context and produce a structured brief.

## Product context
[Paste your product area, target personas, and current strategic priorities — or reference @company-context-sentinelone.md]

## Research study
[Paste the study text, key sections, or a URL if web-fetch is available]

---

### Instructions

Produce the following sections. Be specific and evidence-based — cite page numbers, figure references, or direct quotes from the study where possible.

**1. Study overview (3-5 sentences)**
- Who conducted the study, when, sample size, methodology
- The central question or thesis
- One-line verdict on overall relevance to our product

**2. Key findings (5-8 bullet points)**
- Each bullet: one finding + the supporting data point
- Prioritize findings that relate to security, IT, or enterprise software workflows
- Flag any findings that contradict our current assumptions

**3. Relevant user segments**
- Which segments or personas identified in the study map to our target buyers or users?
- Note segment size, behavior patterns, and unmet needs called out by the research
- Highlight any emerging segments we are not currently addressing

**4. Opportunity areas (3-5)**
For each opportunity:
- **Opportunity:** one-sentence description
- **Evidence:** the specific finding(s) that support it
- **Connection to our product:** how this maps to our roadmap, backlog, or strategic bets
- **Confidence:** High / Medium / Low — based on sample size, methodology quality, and relevance fit

**5. Strategic implications**
- What should we start, stop, or continue based on this research?
- Any risks if we ignore these findings?
- Recommended next steps (e.g., run our own validation study, update a PRD, brief stakeholders)

**6. Limitations and caveats**
- Methodological weaknesses or bias in the study
- Gaps between the study's population and our actual user base
- Anything the study does NOT answer that we would need to investigate ourselves

---

### Constraints
- Do not fabricate data points. If the study does not contain evidence for an opportunity, say so.
- If the study is ambiguous or contradictory on a point, call that out rather than picking a side.
- Keep the total output under 1,500 words — this should be a brief, not a thesis.
- Use plain language. Avoid academic jargon that would not land in a product review.
```

## Usage Example

```
Analyze this research study for our Singularity Platform product area.

## Product context
@workflows/company-context/company-context-sentinelone.md

Our current strategic priorities:
1. Expand autonomous SOC workflows to reduce mean-time-to-respond
2. Increase adoption among mid-market security teams (200-2,000 employees)
3. Integrate AI-assisted triage into the analyst console

## Research study
@anthropic-ai-usage-study-march-2026.pdf

This is Anthropic's study of 81,000 people on how AI is actually being used
across industries and job functions. Focus your analysis on findings related
to cybersecurity practitioners, IT operations teams, and B2B SaaS usage
patterns. I'm especially interested in:
- How security teams are adopting AI tools today vs. other functions
- Any gaps between AI capability and actual analyst workflows
- Signals about willingness to trust autonomous AI actions in high-stakes domains
```

## Tips

- **Scope your request.** A 100-page report is too broad to analyze well in one pass. Paste the most relevant sections (executive summary, key findings, methodology) or tell Claude which chapters to focus on.
- **Layer your product context.** The more specific you are about your personas, current bets, and open questions, the more targeted the opportunity areas will be. Reference your company context file rather than leaving it generic.
- **Chain into action.** Use the output as input to other workflows: feed opportunity areas into `/product-strategy`, turn a high-confidence finding into a PRD with `/prd-creation`, or validate a surprising result with the `strategic-decision-validation` skill.

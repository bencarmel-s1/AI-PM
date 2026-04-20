# User Research Synthesis Workflow with Claude Code
*A repeatable AI-assisted process for turning raw interview data into structured, actionable insights*

---

## The Core Principle

Synthesis is not summarizing. Summarizing tells you what each person said. Synthesis tells you what it means across all of them.

The goal is to find patterns that are strong enough to act on, while being honest about what you don't know. Claude helps you move faster through the extraction and pattern work — but the judgement on what matters is still yours.

---

## Before You Start

- [ ] All interviews completed and notes/transcripts captured
- [ ] Clear research question documented (what were you trying to learn?)
- [ ] You know what decision this research will inform
- [ ] Minimum 5 interviews (fewer than 5 and patterns are unreliable)

---

## The Workflow (4 Steps)

---

### Step 1 — Review Each Interview (5–10 min per interview)

**What you're doing:** Extracting key observations from each interview while preserving context and nuance.

See `interview-review.md` for the full extraction guide.

**Opening prompt:**
```
I have [N] user research interviews to synthesize.
Use @user-research-synthesis-workflow.md to guide me through all 4 steps.

My research question: [What you were investigating]
This will inform: [What product decision]

Interview notes are in: @[file or folder]

Start with Step 1. For each interview, produce a structured summary using
the format in @interview-review.md:
- Participant context
- Key quotes (exact words, not paraphrased)
- Main pain points
- Workarounds and current behaviors
- Tags/themes
- Any surprising or unexpected observations
```

**What Claude will produce per interview:**
- Structured summary with exact quotes preserved
- Tags for each emerging theme
- Surprise/notable flags

**Key constraint:** Do not paraphrase quotes. The participant's exact words carry meaning that summaries lose. If Claude paraphrases, ask it to go back to the source.

---

### Step 2 — Extract Patterns (15 min)

**What you're doing:** Finding what's true across participants, not just within each one.

See `pattern-extraction.md` for the clustering methodology and evidence-strength framework.

**Prompt:**
```
Now move to Step 2. Using all the interview summaries from Step 1,
identify patterns across participants.

Use @pattern-extraction.md for the methodology.

For each pattern:
1. Name it clearly (the underlying user need, not the surface feature request)
2. Rate evidence strength: Strong (5–6/6), Moderate (3–4/6), Emerging (2/6), Outlier (1/6)
3. List supporting quotes from multiple participants
4. Note any contradictions or variation within the pattern
5. Write one sentence on what it implies for the product

Also:
- Flag any contradictions where participants disagreed significantly
- Identify the most surprising pattern (challenges a current assumption)
- Note anything that appeared in the data but doesn't fit any pattern
```

**What Claude will produce:**
- 4–8 named patterns with evidence strength ratings
- Participant-attributed supporting quotes
- Contradiction analysis
- "Surprising insight" callout

**Calibration guidance:**
- Aim for 4–8 patterns. Fewer may mean you're grouping too broadly; more fragments the findings
- "Strong" patterns (5–6 of 6 participants) are actionable. "Emerging" patterns (2 of 6) are worth noting but not acting on alone
- If you find mostly "Outlier" patterns, the research question may have been too broad

---

### Step 3 — Write Synthesis (15–20 min)

**What you're doing:** Translating the patterns into a structured document your team can act on.

See `synthesis-template.md` for the full output format.

**Prompt:**
```
Now write the synthesis document using @synthesis-template.md.

Structure:
1. Executive summary — 3–5 bullets capturing the most important findings
2. Research context — question, method, participants
3. Key findings — top 3–5 patterns with evidence and supporting quotes
4. Opportunities — what these findings suggest we should consider building or changing
5. Recommendations — specific, actionable next steps
6. Appendix — participant details, methodology notes

Quality requirements:
- Every finding must include participant count ("5 of 6 participants...")
- Include at least one disconfirming data point or caveat per major finding
- Opportunities must connect to specific findings (not generic PM instinct)
- Recommendations must be actionable by a specific team member

Save as [research-topic]-synthesis.md
```

**What Claude will produce:**
- Full synthesis document following the template
- Evidence-anchored findings
- Opportunity and recommendation sections

**Quality checklist before finalizing:**
- [ ] Every finding has supporting quotes from multiple participants
- [ ] Disconfirming evidence is acknowledged
- [ ] Participant count is clear for every claim
- [ ] Findings are tied to specific opportunities
- [ ] Recommendations are actionable and specific
- [ ] No identifying information if participants requested anonymity

---

### Step 4 — Share & Discuss

**What you're doing:** Getting the findings in front of your team and documenting what decisions were made.

**Prompt:**
```
The synthesis is ready to share. Help me write:
1. A short async summary (Slack or email) to share with the team
   before the discussion — 3–4 bullets, just the top findings
2. A 30-minute discussion agenda that surfaces the most debated or
   surprising findings and pushes toward decisions

Key decisions this research should inform: [list them]
```

**After the discussion, document decisions:**
```
Based on our team discussion, document the decisions made from this research:
- What we will act on and when
- What we're monitoring but not acting on yet
- What we explicitly decided not to pursue (and why)

Append this to [research-topic]-synthesis.md as a "Decisions" section.
```

---

## File Naming Convention

| File | Purpose |
|---|---|
| `[topic]-synthesis.md` | Full synthesis document |
| `[topic]-interview-summaries.md` | Individual summaries from Step 1 (optional) |

---

## Common Pitfalls

| Pitfall | How to Avoid |
|---|---|
| Confirmation bias | Actively search for disconfirming evidence in Step 2 |
| Over-generalizing | Always include participant counts — "most" is not a count |
| Losing nuance | Preserve verbatim quotes, not just summaries |
| No action | Tie every finding to a specific decision or opportunity |
| Recency bias | Weight all interviews equally — the last interview isn't more true |
| Reporting only support | Synthesis without contradictions is not synthesis |

---

## Time Estimate

| Step | Time |
|---|---|
| Step 1 — Review interviews (6 interviews) | 30–45 min |
| Step 2 — Pattern extraction | 15 min |
| Step 3 — Write synthesis | 15–20 min |
| Step 4 — Share and discuss | 30 min async prep + 30 min meeting |
| **Total** | **~45–60 min with Claude assistance** |

---

*Last updated: April 2026 · Part of the Product Management Lifecycle*

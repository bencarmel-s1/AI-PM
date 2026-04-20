# Feature Request Discovery Workflow
*A structured AI-assisted process for surfacing, quantifying, and prioritizing customer feature requests before you start a PRD*

---

## The Core Principle

Feature requests tell you what customers want. Your OKRs tell you what you're trying to achieve. Revenue data tells you whose opinion matters most right now. This workflow combines all three — so you go into PRD creation with a defensible recommendation, not a gut feeling.

Claude queries Jira, reads your OKRs, surfaces the revenue signal, and flags competitive gaps. You decide what to build.

---

## Before You Start

**What you need:**
- Jira MCP connected (Claude queries "Feature Suggestion and Roadmap" directly)
- Your `Product Line` value — the custom Jira field that scopes issues to your area
- Your OKR file: fill in `okr-template.md` and save as `okrs-[your-name].md`
- Optional: Salesforce MCP for deeper account context beyond what's already on Jira issues

**What Claude will use from Jira:**
- Issue title, description, votes, comment count, creation date
- `SFDC Acct ACV` — account-level ACV of the requesting customer
- `SFDC Opp ACV` — opportunity-level ACV where this feature is a deal factor
- Any linked Salesforce account or opportunity references

**`@filename` syntax:** Throughout this workflow, prompts use `@filename.md` to reference your files. Store your OKR file in the same folder you open Claude Code from and reference it by name. Claude reads it directly.

---

## The Workflow (4 Phases)

### Phase 1 — Scope & Pull

**Goal:** Define your area and fetch all matching Jira issues via MCP.

**What to bring:**
- Your `Product Line` value (e.g. "Purple AI", "Endpoint", "Cloud Security")
- Optional: date range filter (e.g. issues created in the last 18 months)
- Optional: minimum vote threshold (e.g. only issues with ≥ 2 votes)

**Opening prompt:**
```
I want to run a feature request discovery for my product area.
Use @feature-request-discovery-workflow.md to guide me through all 4 phases.

My inputs:
- Product Line: [YOUR PRODUCT LINE VALUE]
- My OKRs: @okrs-[your-name].md
- Date range: [e.g. last 18 months — or leave blank for all]
- Min votes: [e.g. 2 — or leave blank for all]

Start by querying the "Feature Suggestion and Roadmap" Jira project filtered by
my Product Line. Pull title, description, votes, comments, creation date,
SFDC Acct ACV, and SFDC Opp ACV for each issue. Tell me how many issues you found
before moving to Phase 2.
```

**What Claude will do:**
- Run a JQL query: `project = "Feature Suggestion and Roadmap" AND "Product Line" = "[YOUR VALUE]" ORDER BY votes DESC`
- Fetch issue fields including revenue custom fields
- Report total issue count as a checkpoint before proceeding

---

### Phase 2 — Quantify & Rank

**Goal:** Surface the size and shape of your request backlog before you start theming.

**Opening prompt (or continue from Phase 1):**
```
Now analyze the issues you pulled. Produce:
1. Total request count
2. A ranked list of the top 20 by votes (include SFDC Acct ACV and SFDC Opp ACV for each)
3. Age distribution — how many requests are < 6 months, 6–12 months, 12–18 months, 18+ months old
4. Staleness flags — for any request in the top 20 that is 12+ months old, flag it as
   "⚠️ Validate before building — confirm this is still live customer pain"
5. Any outliers with unusually high engagement relative to their vote count
```

**What Claude will produce:**
- Top 20 ranked list with vote count, SFDC Acct ACV, SFDC Opp ACV, and age
- Age distribution summary
- Staleness warnings on any high-ranking request ≥ 12 months old
- Engagement outliers (high comment count relative to votes)

**Calibration guidance:**
- A healthy active backlog for a single product line is typically 50–200 open requests
- If you have < 20 requests, the data may be thin — consider widening filters or cross-checking with other signal sources (support tickets, sales notes)
- If you have > 300 requests, consider narrowing by minimum vote threshold (≥ 3 votes) before theming

---

### Phase 3 — Theme, Cluster & OKR Alignment

**Goal:** Group individual requests into meaningful themes and score each against your OKRs.

**Opening prompt:**
```
Now group all the requests into 4–8 themes based on the underlying customer need
(not the surface-level feature). For each theme:

1. Name the theme clearly (what customer need it addresses)
2. List the request count and top 3 representative Jira tickets
3. Show total votes and total SFDC Acct ACV across the theme
4. Score OKR alignment: High / Medium / Low / None
   - High = directly moves one of my OKRs
   - Medium = indirectly supports an OKR
   - Low = tangentially related
   - None = no connection to current OKRs
5. Write a one-line rationale for the OKR alignment score
6. Flag any theme where top 3 tickets are 12+ months old with ⚠️

Use @okrs-[your-name].md as the source of truth for scoring.
```

**What Claude will produce:**
- 4–8 named themes with request count, representative tickets, vote total, ACV total
- OKR alignment score + rationale for each theme
- Staleness flags where applicable

**Calibration guidance:**
- Aim for 4–8 themes. Fewer than 4 may mean you're grouping too broadly; more than 8 fragments the signal.
- "High OKR alignment" means the theme would directly contribute to hitting a key result — not just "it's good for customers"
- If most themes score None, that's a useful signal: either your OKRs are set too narrowly, or the feature request backlog has drifted from strategic intent

---

### Phase 4 — Revenue Signal, Competitive Flags & Synthesis

**Goal:** Layer in revenue urgency, surface competitive gaps, and produce a defensible recommendation.

**Opening prompt:**
```
Now complete the discovery brief. For each theme:

1. Revenue signal:
   - Total SFDC Acct ACV represented (existing customers asking)
   - Total SFDC Opp ACV at risk (open deals where this is a stated factor)
   - Note: Opp ACV at risk signals more urgency than Acct ACV — weight it higher
   - Flag any individual request tied to Opp ACV > $[your threshold, e.g. $500K]

2. Competitive flags:
   - Cross-reference each theme against @company-context.md (competitive section)
   - Flag any theme that maps to a known gap vs. CrowdStrike, Microsoft, Palo Alto, or others
   - One line per flag: [Theme] → [Competitor] has [X capability]; we [gap description]

3. 2x2 prioritization matrix:
   Place each theme in the appropriate quadrant:
   - High OKR / High Revenue → Build now candidates
   - High OKR / Low Revenue  → Strategic bets
   - Low OKR / High Revenue  → Negotiate / delegate to roadmap review
   - Low OKR / Low Revenue   → Park for now

4. Synthesis brief:
   - One quick-start paragraph: the single most important finding in 3–4 sentences
   - Recommended starting point for PRD: the highest-priority theme with rationale
     (cite OKR alignment + revenue signal + competitive context)

Save the full output to [product-line]-feature-request-discovery.md using
@feature-request-discovery-template.md as the structure.
```

**What Claude will produce:**
- Revenue signal per theme (ARR represented vs. Opp ACV at risk — differentiated)
- Competitive gap flags
- 2x2 matrix with all themes placed
- Quick-start paragraph + PRD recommendation
- Saved discovery brief ready for handoff

---

## File Naming Convention

| File | Purpose |
|------|---------|
| `okrs-[your-name].md` | Your current OKRs — Claude reads this every session |
| `[product-line]-feature-request-discovery.md` | Output from this workflow — your discovery brief |

---

## Common Prompt Patterns

**Re-run for a specific time window:**
```
Re-pull the Jira issues but filter to the last 12 months only.
Show me how the theme ranking changes.
```

**Dig into a single theme:**
```
Pull the full list of Jira issues in the [theme name] theme.
Show me the description of each one and any customer names mentioned.
```

**Check a high-ACV request:**
```
For the issue [JIRA-KEY], search Salesforce for the associated account
and tell me their current ARR, contract renewal date, and open opportunities.
```

**Update after sales input:**
```
The sales team has told me [X] is a blocker for [deal/account].
Find all Jira issues in the "Feature Suggestion and Roadmap" project that relate to [X]
and add them to the discovery brief. Recalculate the Opp ACV at risk.
```

---

## Time Estimate

| Phase | Time |
|-------|------|
| Phase 1 — Scope & Pull | 5–10 min |
| Phase 2 — Quantify & Rank | 10–15 min |
| Phase 3 — Theme & OKR Align | 15–20 min |
| Phase 4 — Revenue & Synthesis | 15–20 min |
| **Total** | **45–65 min** |

---

## What's Next

Your discovery brief is the input to PRD creation.

Use [`../prd-creation/`](../prd-creation/) to take your top-priority theme and turn it into a production-quality requirements document — with Socratic questioning and expert agent reviews built in.

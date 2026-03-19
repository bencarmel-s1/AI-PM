# /feature-request-discovery

Pull, analyze, and prioritize feature requests from Jira — surfacing what customers want most, how it maps to your OKRs, and where the revenue signal is strongest.

**Requires:** Jira MCP connected.

## Step 1: Gather inputs

Ask the user:
1. What is your Product Line value in Jira? (e.g., "Endpoint", "Cloud", "Identity")
2. Do you have an OKR file to align against? (@ mention it, or use `@workflows/advanced-workflow/feature-request-discovery/okr-template.md` to create one)
3. Date range filter — how far back should we look? (default: last 18 months)
4. Minimum vote threshold — what's the minimum number of votes to include? (default: 3)

## Step 2: Load context

Read:
- `@workflows/advanced-workflow/feature-request-discovery/feature-request-discovery-template.md`
- `@workflows/company-context/company-context-sentinelone.md`
- The OKR file the user provided

## Phase 1: Scope and pull (5-10 min)

Query Jira using the Jira MCP:

```
project = "Feature Suggestion and Roadmap"
AND "Product Line" = "[USER'S VALUE]"
AND created >= "[DATE RANGE START]"
AND votes >= [MIN VOTES]
ORDER BY votes DESC
```

For each issue fetch: title, description, vote count, comment count, creation date, SFDC Account ACV (if available), SFDC Opportunity ACV (if available).

Report: total issues found, date range covered, fields available.

## Phase 2: Quantify and rank (10-15 min)

Produce:
- **Top 20 by votes** — title, votes, ACV where available, age
- **Age distribution** — count by bucket: less than 6 months, 6-12 months, 12-18 months, 18+ months
- **Staleness flags** — requests 12+ months old with high votes
- **Engagement outliers** — requests with high comment-to-vote ratios

## Phase 3: Theme, cluster, and OKR alignment (15-20 min)

Group top requests into 4-8 themes based on underlying customer need (not surface feature descriptions).

For each theme:
- Theme name and one-sentence description
- Customer need being expressed
- Total votes across requests in this theme
- Total ACV where available
- OKR alignment score: High / Medium / Low / None — with rationale referencing the user's OKR file

## Phase 4: Revenue signal, competitive flags, and synthesis (15-20 min)

**Revenue signal:** Weight Opportunity ACV (active deals at risk) higher than Account ACV (existing customer requests). Flag themes where Opp ACV concentration suggests deal-blockers vs. retention/expansion signals.

**Competitive flags:** Cross-reference themes against SentinelOne's key competitors (CrowdStrike, Microsoft Defender XDR, Palo Alto Cortex XDR) using context from `company-context-sentinelone.md`. Flag themes where a competitor capability gap may be driving requests.

**2x2 prioritization matrix:** Plot themes on OKR alignment (vertical) x Revenue signal (horizontal):
- High OKR + High Revenue: Build now candidates
- High OKR + Low Revenue: Strategic bets
- Low OKR + High Revenue: Deal-specific exceptions
- Low OKR + Low Revenue: Deprioritize

**Synthesis brief:** 3-5 bullet executive summary answering: What are customers asking for most? What should we build next and why?

## Step 5: Save output

Save the full discovery brief as `[product-line]-feature-request-discovery.md`.

Confirm: "Discovery brief saved to `[product-line]-feature-request-discovery.md`."

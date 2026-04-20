---
name: weekly-pipeline-digest
description: >
  Generates a weekly leadership-ready pipeline digest from Salesforce for any set of products.
  Queries open pipeline, closed won/lost deals, and at-risk opportunities, then delivers a
  formatted executive summary and per-product deep-dive — both in Claude and to a Slack channel.

  Use this skill whenever a PM asks to "run the weekly digest", "generate a pipeline report",
  "send the Friday pipeline update", "create a deals summary", or "pull the weekly Salesforce
  briefing". Also trigger for any variant of "weekly sales update", "pipeline health check",
  or "what closed this week". If a user has a scheduled digest task or mentions sending pipeline
  data to Slack, this skill should handle it.
---

# Weekly Pipeline Digest

This skill produces a leadership-ready weekly pipeline briefing from Salesforce. It covers
open pipeline, wins, losses, at-risk deals, and advancing deals — delivered both in Claude
and posted to a Slack channel.

---

## ⚙️ SETUP — Configure Before First Use

> **PMs: Edit this section once before using the skill as a scheduled task.**
> Everything below the dashed line runs automatically — you only need to touch this block.

### Products to Track

Define 2–5 products. For each, provide:
- A display name and emoji color (for visual separation in the digest)
- Three Salesforce SOQL WHERE clauses: one for open deals, one for closed-won this week,
  one for closed-lost in the last 30 days. These filters go inside `WHERE (...) AND ...`

```
PRODUCT_1:
  name: "Your Product Name"
  emoji: "🔵"
  soql_filter: |
    Name LIKE '%YourProduct%'

PRODUCT_2:
  name: "Your Second Product"
  emoji: "🟠"
  soql_filter: |
    (Name LIKE '%Product2%' OR Name LIKE '%P2 Variant%')
    AND Name NOT LIKE '%exclude this%'

PRODUCT_3:
  name: "Your Third Product"         (delete this block if you only have 2 products)
  emoji: "🟣"
  soql_filter: |
    Name LIKE '%ThirdProduct%' OR Name LIKE '%Product Three%'
```

### Slack Channel

```
SLACK_CHANNEL_ID: "C00000000"    ← replace with your channel's ID
```

To find your channel ID: right-click the channel in Slack → "Copy link" →
the ID is the string starting with C at the end of the URL.

---

## How This Works

When triggered (manually or on schedule), Claude will:

1. Query Salesforce for open pipeline, wins, and losses for each configured product
2. Calculate key metrics (pipeline value, weighted value, at-risk, advancing)
3. Render a full digest here in Claude
4. Post a concise summary to your Slack channel

---

## STEP 1 — SALESFORCE QUERIES

Run all queries in parallel using `execute_soql_query`. Use `Account.Name` (not `AccountName`).

For **each product** defined in the configuration above, run these three queries, substituting
that product's `soql_filter` in the WHERE clause:

**Open pipeline:**
```sql
SELECT Id, Name, StageName, Amount, CloseDate, Account.Name, Owner.Name,
       Probability, LastActivityDate
FROM Opportunity
WHERE (<PRODUCT_SOQL_FILTER>)
  AND IsClosed = false
ORDER BY CloseDate ASC
```

**Closed this week:**
```sql
SELECT Id, Name, StageName, Amount, CloseDate, Account.Name, Owner.Name
FROM Opportunity
WHERE (<PRODUCT_SOQL_FILTER>)
  AND IsClosed = true
  AND CloseDate = THIS_WEEK
ORDER BY CloseDate DESC
```

**Lost in the last 30 days:**
```sql
SELECT Id, Name, StageName, Amount, CloseDate, Account.Name, Owner.Name, Description
FROM Opportunity
WHERE (<PRODUCT_SOQL_FILTER>)
  AND IsWon = false
  AND IsClosed = true
  AND CloseDate = LAST_N_DAYS:30
ORDER BY CloseDate DESC
```

> If Salesforce returns no results for a product, note this in the digest and flag that the
> SOQL filter should be verified — it may not match current deal naming conventions.

---

## STEP 2 — CALCULATIONS

Compute the following for **each product** from the raw Salesforce results:

| Metric | How to Compute |
|---|---|
| Open deal count | Count of open pipeline rows |
| Total pipeline value | Sum of Amount for open deals (skip nulls) |
| Weighted pipeline value | Sum of (Amount × Probability/100) for open deals |
| Won this week | Count + total Amount where IsClosed=true, IsWon=true, CloseDate=THIS_WEEK |
| Lost this week | Count + total Amount where IsClosed=true, IsWon=false, CloseDate=THIS_WEEK |
| At-risk deals | Open deals where ANY of: CloseDate is past; LastActivityDate is null OR >14 days ago; Probability <30%; Stage 1 or 2 with CloseDate within 14 days |
| Advancing deals | Open deals in Stage 4–5; OR Stage 3 with LastActivityDate within 7 days; OR Probability ≥70% |

Then compute **cross-product totals** (sum across all products) for the executive summary.

---

## STEP 3 — CLAUDE DIGEST FORMAT

Output the full report using this exact structure. Replace `[PRODUCT N]` placeholders with
the configured product names and emojis. Add or remove product sections to match your count.

```
# 📊 [Your Product Area] — Weekly Pipeline Digest
**Week ending: [Today's date] | Prepared every Friday**

---

## 🏢 Executive Summary

> *This section is for leadership. One view across all products.*

| Metric | [Product 1] | [Product 2] | [Product 3] | Combined |
|---|---|---|---|---|
| Open Deals | N | N | N | N |
| Total Pipeline | $X | $X | $X | $X |
| Weighted Pipeline | $X | $X | $X | $X |
| Won This Week | N deals · $X | N deals · $X | N deals · $X | N deals · $X |
| Lost This Week | N deals · $X | N deals · $X | N deals · $X | N deals · $X |
| At-Risk Deals | N | N | N | N |

**Weekly highlight:** [1–2 sentence plain-English summary of the most important thing
leadership needs to know — biggest win, most urgent risk, or key pattern.]

---

## 🎯 Cross-Product Recommended Actions

*Top priorities this week, ranked by urgency and deal size:*

1. [Action — include product name, account, amount, and specific reason]
2. [Action]
3. [Action]
4. [Action — max 5 total]

---

## ─────────────────────────────────
## [EMOJI] PRODUCT 1: [Product Name]
## ─────────────────────────────────

### 🏆 Deals Closed This Week
| Account | Deal Name | Amount | Outcome | Close Date | Owner |
Won deals show ✅, lost deals show ❌.
If none: *No deals closed this week.*

### ✅ Pipeline Overview
- Open deals: N | Pipeline: $X | Weighted: $X
- By stage: Stage 1: N · Stage 2: N · Stage 3: N · Stage 4: N · Stage 5: N

### 🔴 At-Risk Deals
| Account | Amount | Close Date | Risk Reason | Owner |
If none: *No at-risk deals this week.*

### 📈 Advancing Deals
| Account | Amount | Stage | Close Date | Signal |
If none: *No deals actively advancing this week.*

### 💔 Loss Reasons (Last 30 Days)
| Account | Amount | Notes / Description |
*Loss theme: [1–2 sentences on patterns. If most have no notes, flag as a data quality issue.]*

---

[Repeat the product section for each additional product]
```

---

## STEP 4 — SLACK MESSAGE

Send a single Slack message to the configured `SLACK_CHANNEL_ID` using `slack_send_message`.
Keep it concise and scannable — full detail lives in the Claude digest above.

Use this structure:

```
*📊 [Product Area] Weekly Pipeline Digest — [Date]*

━━━━━━━━━━━━━━━━━━━━━━
*🏢 Executive Summary*
━━━━━━━━━━━━━━━━━━━━━━

| | [Product 1] | [Product 2] | [Product 3] | Total |
|---|---|---|---|---|
| Open Deals | N | N | N | N |
| Pipeline | $X | $X | $X | $X |
| Weighted | $X | $X | $X | $X |
| Won This Week | N · $X | N · $X | N · $X | N · $X |
| At-Risk | N | N | N | N |

📌 *This week:* [1-sentence highlight]

━━━━━━━━━━━━━━━━━━━━━━
*🎯 Actions This Week*
━━━━━━━━━━━━━━━━━━━━━━
• [Action 1 — product | account | amount]
• [Action 2]
• [Action 3]

━━━━━━━━━━━━━━━━━━━━━━
*[EMOJI] [Product 1 Name]*
━━━━━━━━━━━━━━━━━━━━━━
*Closed:* [won/lost count summary]
*Pipeline:* $X across N deals · Weighted: $X
*At-Risk:* [top 2–3 accounts with reason, or "None"]
*Advancing:* [top 2–3 accounts, or "None"]
*Loss themes:* [1 sentence, or "No losses this period"]

[Repeat per product]
```

---

## CONSTRAINTS

- **Never hallucinate** deal names, amounts, or dates. Only report what Salesforce returns.
- If a product returns no data, say so explicitly and note what filter was searched — the
  naming convention may have changed.
- **Always send the Slack message**, even if data is sparse. Note any gaps explicitly.
- Round dollar amounts to the nearest dollar in tables. Use $XM format (e.g., $2.3M) in
  summary sentences.
- Flag data quality issues: if more than half of lost deals have no `Description`, call this
  out as a data hygiene problem in the loss reasons section.
- Keep Slack concise. The full detail lives in the Claude response — Slack is the trigger
  for leadership to know the digest ran.
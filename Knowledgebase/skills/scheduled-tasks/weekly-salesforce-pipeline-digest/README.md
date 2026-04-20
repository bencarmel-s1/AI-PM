# Weekly Pipeline Digest — Claude Skill

A Claude skill that generates a **leadership-ready weekly pipeline briefing** from Salesforce. Configured once per PM, it runs automatically every Friday (or on demand), delivers a full digest inside Claude, and posts a concise summary to a Slack channel.

Originally built for Wayfinder products. Generalized so any PM can adapt it for their own product area in under 10 minutes.

---

## What It Produces

**In Claude** — a full structured report:
- Executive summary table across all products (open pipeline, weighted pipeline, won/lost this week, at-risk count)
- 1–2 sentence leadership highlight + prioritized recommended actions
- Per-product deep-dives covering pipeline by stage, at-risk deals with reasons, advancing deals, and loss themes from the last 30 days

**In Slack** — a concise scannable summary posted to your team's channel, with the same executive table and top actions.

---

## Prerequisites

Before setting up the skill, make sure you have:

- **Claude desktop app** with Cowork mode enabled
- **Salesforce connector** connected in Claude (used to run SOQL queries against your org's Opportunity object)
- **Slack connector** connected in Claude (used to post the digest to your channel)
- Basic familiarity with how your deals are named in Salesforce — you'll need to know the naming pattern (e.g., `"Threat Hunting"`, `"MDR Elite"`) to write your SOQL filter

---

## Installation

1. Download `weekly-pipeline-digest.skill` from this repo
2. Open the Claude desktop app
3. Go to **Settings → Skills** and click **"Install Skill"** (or drag the `.skill` file into the window)
4. The skill will appear in your skills list as **weekly-pipeline-digest**

---

## Configuration

After installing, open the skill file and edit the **Setup block** near the top of `SKILL.md`. This is the only section you need to touch — everything else runs automatically.

### Step 1 — Define your products

Add one block per product (2–5 products supported). For each you need:

- **name** — how the product appears in the digest headings
- **emoji** — a colored circle emoji for visual separation (🔵 🟠 🟣 🟢 🔴)
- **soql_filter** — the `WHERE` clause fragment that identifies this product's deals in Salesforce

```
PRODUCT_1:
  name: "Threat Hunting"
  emoji: "🔵"
  soql_filter: |
    Name LIKE '%Threat Hunting%'

PRODUCT_2:
  name: "MDR Essentials"
  emoji: "🟠"
  soql_filter: |
    (Name LIKE '%MDR essential%' OR Name LIKE '%MDR Essentials%' OR Name LIKE '%WF MDR%')
    AND Name NOT LIKE '%Elite%'

PRODUCT_3:
  name: "MDR Elite"
  emoji: "🟣"
  soql_filter: |
    Name LIKE '%Wayfinder Elite%' OR Name LIKE '%MDR Elite%'
```

**Tips for writing your SOQL filter:**
- Use `LIKE '%keyword%'` for partial name matches (case-insensitive in Salesforce)
- Chain conditions with `OR` to catch naming variations
- Use `AND Name NOT LIKE '%...'` to exclude deals that would otherwise match another product
- Test your filter first in Salesforce's query editor (Setup → Developer Console → Query Editor) to confirm it returns the right deals

### Step 2 — Set your Slack channel

```
SLACK_CHANNEL_ID: "C07A2015FPH"    ← replace with your channel's ID
```

**To find your channel ID:**
1. Right-click the channel name in Slack
2. Select "Copy link"
3. The URL looks like `https://app.slack.com/client/T.../C07A2015FPH` — the part starting with `C` is your channel ID

---

## Running the Digest

### Option A — Scheduled (recommended)

Set it up as a recurring task in Claude so it runs automatically every Friday afternoon:

1. In Claude, say: *"Create a scheduled task to run the weekly pipeline digest every Friday at 4pm"*
2. Claude will create the task using this skill
3. Every Friday it will query Salesforce, build the digest, and post to Slack automatically

### Option B — On demand

Trigger it manually anytime by saying things like:
- *"Run the weekly pipeline digest"*
- *"Generate a pipeline report and post it to Slack"*
- *"What closed this week? Run the deals digest."*
- *"Send the Friday pipeline update"*

---

## What Gets Calculated

For each product, the skill computes:

| Metric | Definition |
|---|---|
| Open pipeline value | Sum of `Amount` for all open deals |
| Weighted pipeline | Sum of `Amount × Probability/100` |
| Won this week | Deals where `IsClosed=true`, `IsWon=true`, `CloseDate=THIS_WEEK` |
| Lost this week | Deals where `IsClosed=true`, `IsWon=false`, `CloseDate=THIS_WEEK` |
| **At-risk** | Open deals where: close date is past, OR last activity >14 days ago, OR probability <30%, OR stage 1–2 with close date within 14 days |
| **Advancing** | Open deals in stage 4–5, OR stage 3 with activity in last 7 days, OR probability ≥70% |

---

## Troubleshooting

**"No data found" for a product**
The SOQL filter didn't match any deals. Common causes: deal naming changed in Salesforce, typo in the filter, or the product is tracked under a different name. Check your filter in the Salesforce Developer Console.

**Slack message not sending**
Confirm your Slack connector is connected in Claude (Settings → Connectors) and that you're a member of the target channel.

**Deals missing that should appear**
Salesforce LIKE queries are case-insensitive but require `%` wildcards on both sides. `'%MDR%'` will match "WF MDR Elite" but `'MDR'` (no wildcards) will only match an exact string.

**Loss reasons mostly blank**
This is a data quality issue in Salesforce — the `Description` field isn't being filled in when deals are closed lost. The skill will flag this automatically. Consider reminding your sales team to add close reasons.

---

## Customization

**Change the cadence** — When setting up the scheduled task, specify a different day or time. The skill runs whenever triggered and always uses the current date.

**Add more products** — Copy an existing product block in the Setup section and fill in the new name, emoji, and filter. Up to 5 products are supported.

**Change the Slack format** — The Slack message template is in the `STEP 4` section of `SKILL.md`. Edit the structure there to add or remove fields.

**Track a different time window for losses** — The default is last 30 days. Change `LAST_N_DAYS:30` in the lost-deals query (Step 1 of the skill) to any number.

---

## File Structure

```
weekly-pipeline-digest/
└── SKILL.md          # All skill logic and configuration lives here
```

The skill is self-contained in a single file. No external scripts or dependencies.

---

## Questions?

Reach out to Ingemar Dvorsky (ingemar.dvorsky@sentinelone.com) — he built the original Wayfinder version this template is based on.
---
title: Integration Usage Report — Q1 2026
generated: 2026-04-02
source: Data warehouse (Snowflake) — integrations_active table
---

# Integration Usage Report — Q1 2026

## Summary

This report tracks which integrations are actively used across Pulse's paying customer base, to inform Integration Catalog v2 prioritization.

**Reporting period:** Jan 1 – Mar 31, 2026
**Active customers:** 312
**Average active integrations per customer:** 1.8 (target: 3.0)

---

## Top 20 Active Integrations

| Rank | Integration | Active Customers | % of Customer Base | 30d Events (M) |
|------|------------|-----------------|-------------------|----------------|
| 1 | Slack | 248 | 79% | 142.3 |
| 2 | Segment | 187 | 60% | 89.1 |
| 3 | Google Analytics | 156 | 50% | 67.8 |
| 4 | HubSpot | 134 | 43% | 45.2 |
| 5 | Intercom | 98 | 31% | 38.9 |
| 6 | Zendesk | 87 | 28% | 31.4 |
| 7 | Salesforce | 72 | 23% | 28.7 |
| 8 | Stripe | 64 | 21% | 22.1 |
| 9 | Amplitude (export) | 43 | 14% | 18.3 |
| 10 | Jira | 41 | 13% | 15.6 |
| 11 | GitHub | 38 | 12% | 12.4 |
| 12 | Mixpanel (export) | 31 | 10% | 9.8 |
| 13 | BigQuery | 28 | 9% | 44.1 |
| 14 | Snowflake | 24 | 8% | 38.7 |
| 15 | Webhooks (custom) | 22 | 7% | 6.2 |
| 16 | Zapier | 19 | 6% | 4.1 |
| 17 | Shopify | 14 | 4% | 5.3 |
| 18 | Klaviyo | 12 | 4% | 3.8 |
| 19 | Braze | 11 | 4% | 4.2 |
| 20 | Marketo | 8 | 3% | 2.9 |

---

## Observations

**High adoption (>40% of customers):** Slack, Segment, Google Analytics, HubSpot — these are working well. No catalog improvement needed.

**Mid-tier with setup friction:** Salesforce (23%), Stripe (21%), Jira (13%) — these have high demand signals from support tickets but lower adoption than expected. CS reports that setup requires manual API configuration that many customers abandon mid-process.

**Shopify gap:** Only 14 active customers (4%), despite 3 explicit customer requests for a native connector in Q1. Current workaround (custom webhook) breaks on Shopify API updates. Shopify customer base in our ICP is ~12% — we're underserving them.

**Custom webhooks:** 22 customers using custom webhooks. These are proxy signals for missing native integrations — dig into which integrations they're building.

---

## Category Breakdown

| Category | Active Integrations | % Customers Using ≥1 |
|---------|--------------------|--------------------|
| Communication (Slack, Intercom) | 346 | 84% |
| CRM (HubSpot, Salesforce) | 206 | 56% |
| Analytics (GA, Amplitude, Mixpanel) | 230 | 62% |
| Data Warehouse (BigQuery, Snowflake) | 52 | 16% |
| E-commerce (Shopify, Klaviyo) | 26 | 8% |
| Dev Tools (Jira, GitHub) | 79 | 24% |

---

## Recommendations

1. **Prioritize Salesforce and Shopify for native connector builds** — Salesforce has high demand + enterprise deal-blocker status; Shopify has gap vs. e-commerce ICP.
2. **Invest in setup UX for mid-tier integrations** — Stripe and Jira are losing customers to setup friction, not product gaps.
3. **Audit custom webhook users** — 22 customers are self-serving integrations we're not offering natively; these are new connector candidates.

---

*Next report: Q2 FY26, due July 5, 2026.*

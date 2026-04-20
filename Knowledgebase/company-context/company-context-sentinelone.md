# SentinelOne — Product Context

> **How to use this file:** This is your starting point. The company-wide sections are pre-filled with public information. Fill in the sections marked `[YOUR AREA]` based on your product area, team, and current priorities. The richer this file, the better every PRD Claude writes will be.
>
> Once filled in, store it in your project's `.claude/` folder as `CLAUDE.md` so Claude loads it automatically every session.
>
> @ mention it at the start of any PRD session: `@company-context.md`

---

## Company Overview

**SentinelOne** is an AI-powered cybersecurity company that provides autonomous endpoint, cloud, and identity protection for enterprises.

**Founded:** 2013
**HQ:** Mountain View, CA
**Exchange:** NYSE: S (IPO June 2021)
**Employees:** ~3,000+
**Customers:** 10,000+ organizations, including a significant share of the Fortune 500 and major government agencies
**Revenue:** [Current ARR — check latest earnings release]
**Business model:** SaaS subscription; priced per endpoint/agent, tiered by capability

---

## Product

SentinelOne's core offering is the **Singularity Platform** — a unified AI security platform that consolidates endpoint, cloud, identity, and data lake capabilities into a single agent and console.

Key platform pillars:
- **Singularity Endpoint** — AI-powered EPP + EDR + XDR; autonomous threat prevention, detection, and response at machine speed
- **Singularity Cloud** — CNAPP covering cloud workload protection, CSPM, and container/Kubernetes security
- **Singularity Identity** — Active Directory and identity threat detection & response (ITDR)
- **Singularity Data Lake** — Unified security data ingestion, retention, and querying across all telemetry sources
- **Purple AI** — Generative AI security analyst; natural language threat hunting, automated investigations, and alert triage

**Key differentiator:** Autonomous, real-time protection that operates without human intervention — SentinelOne's AI acts at machine speed to stop threats before humans can even see them, without relying on cloud lookups or signature updates.

---

## Target Customers

**Primary segments:**
- Large enterprise (1,000+ endpoints)
- Mid-market (250–1,000 endpoints)
- MSSPs and MDR providers (resell or operate Singularity on behalf of their customers)
- Government and public sector (FedRAMP authorized)

**Personas:**

- **CISO / VP Security** — Owns the security strategy and budget. Needs to justify security spend to the board, demonstrate compliance, and prove the platform reduces risk exposure. Cares about analyst recognition (Gartner MQ, Forrester Wave) and peer validation.
- **Security Operations (SOC) Analyst / Threat Hunter** — Lives in the console every day. Needs fast alert triage, low false positives, and tools that reduce alert fatigue. Evaluates platforms on detection quality, workflow speed, and automation depth.
- **IT / Security Engineering Lead** — Owns deployment, agent management, and integrations. Cares about rollout complexity, performance impact on endpoints, API quality, and compatibility with the existing security stack.
- **MSSP / MDR Operator** — Manages Singularity on behalf of multiple customer tenants. Needs multi-tenancy, white-labeling capability, and operational efficiency at scale.

---

## Market Position

**Key competitors:**
- **CrowdStrike (Falcon)** — Primary head-to-head competitor; strong brand and installed base. We differentiate on autonomous response (not requiring human confirmation), a unified data lake, and more aggressive AI/automation investment.
- **Microsoft Defender (XDR)** — Default choice for Microsoft-heavy organizations; bundled pricing creates low switching friction. We differentiate on cross-platform support, detection quality, and independence from a single OS vendor.
- **Palo Alto Networks (Cortex XDR)** — Strong in enterprises that run full Palo Alto stacks; broader network security portfolio. We differentiate on endpoint-native telemetry quality and simplicity of deployment.
- **Trend Micro / Trellix / Broadcom (legacy AV players)** — Displacement targets in mid-market and enterprise refresh cycles. We differentiate on modern architecture, single-agent simplicity, and AI-native detection vs. signature-based approaches.

**Our edge:** The only platform where the AI acts — not just alerts. SentinelOne's Storyline technology correlates every event across an entire attack timeline automatically, and the autonomous response engine can contain, remediate, and roll back threats in real time without analyst involvement.

---

## Current Priorities

> **[YOUR AREA — fill in your team's current OKRs and initiatives]**

**[Quarter/Year] Goals:**
1. [Goal 1 — with a specific metric tied to your product area]
2. [Goal 2]
3. [Goal 3]

**Strategic initiatives:**
- **[Initiative name]** — [1-2 sentences on what it is and why it matters now]
- **[Initiative name]** — [1-2 sentences]

---

## Team Structure

> **[YOUR AREA — fill in your squad's actual structure]**

**Leadership:**
- **[Name]** — [Title] ([brief background])
- **[Name]** — [Title, your direct manager]

**Product team (your squad):**
- [X] Product Managers
- [X] Engineers ([squad name if applicable])
- [X] Designers
- [X] User Researchers / Data Scientists

---

## Customer Insights

> **[YOUR AREA — fill in with signals from your product area]**

**What customers love:**
- "[Direct quote — from a customer interview, NPS response, or sales call]"
- "[Direct quote]"

**What customers want more of:**
- [Top feature request for your area]
- [Second most common request]
- [Third]

**Recent signals:**
- [X]% of churned customers in your segment cited [reason]
- [X]% of support tickets in your area are about [topic]
- NPS score: [X] (or CSAT for your feature area)

---

## Business Model

**Pricing model:**
SentinelOne sells annual SaaS subscriptions priced per endpoint/agent, with capability tiers (Core, Control, Complete, Commercial, Enterprise). Additional modules (Cloud, Identity, Data Retention, Purple AI) are sold as add-ons. MSSPs purchase through a partner program with usage-based billing.

**Key metrics to know for your PRD:**
- Average deal size for your segment: $[X]/year — [ask your aligned AE or RevOps]
- Common expansion triggers in your area: [e.g. endpoint count growth, new platform module adoption]
- Churn signals in your area: $[fill in from CS/data team]

---

## How to Use This File

When starting a PRD session with Claude, include this file in your prompt:

```
Please help me fill out @Carls-PRD-Template.md for [feature].
Use @company-context.md for product context.
Guide me through the process using @socratic-questioning.md.
My initial ideas are: [brief description]
```

Claude will use the company context to:
- Frame your problem statement in terms of SentinelOne's actual positioning
- Suggest success metrics grounded in our business model and customer segments
- Challenge scope creep against our current strategic priorities
- Tailor the business case to the personas and use cases that matter most for your area

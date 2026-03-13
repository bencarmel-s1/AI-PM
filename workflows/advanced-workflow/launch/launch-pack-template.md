# Launch Pack Template
*Use this with Claude Code to generate all launch artifacts in a single session*

---

## How to Use This Template

Reference this file alongside your PRD and sprint notes to generate a complete launch pack:

```
Generate a full launch pack using @launch-pack-template.md.
Inputs: @[your-prd-final.md] @[sprint-notes-or-jira-export.md]
Context: @company-context-sentinelone.md
Feature name: [feature name]
Launch tier: [Major / Minor / Patch]
```

Claude will fill in every section below using your PRD and sprint context.
See `example-launch-pack.md` for a fully worked Purple AI example.

---

## Readiness Check

**Feature name:** [feature name]
**Launch date:** [YYYY-MM-DD]
**Launch tier:** 🔴 Major / 🟡 Minor / 🟢 Patch
**PM owner:** [name]
**Eng lead:** [name]
**PMM contact:** [name if applicable]

### What shipped vs. what was planned

| PRD Goal | Shipped? | Notes |
|---|---|---|
| [Goal from PRD] | ✅ Yes / ⚠️ Partial / ❌ Deferred | [scope change or note] |
| [Goal from PRD] | ✅ Yes / ⚠️ Partial / ❌ Deferred | [scope change or note] |
| [Goal from PRD] | ✅ Yes / ⚠️ Partial / ❌ Deferred | [scope change or note] |

### Deferred scope
> List anything that was planned but not shipped. If nothing was deferred, write "None."

- [deferred item] — deferred because [reason] — targeted for [next sprint / Q3 / future]

### Launch blockers
> Is anything preventing us from distributing the launch pack today?

- [ ] Release notes written and reviewed
- [ ] CS brief shared with CS team lead
- [ ] Sales brief shared with PMM or SE lead
- [ ] Executive announcement reviewed by manager
- [ ] Confluence page published
- [ ] No unresolved P0/P1 bugs in shipped scope

---

## Artifact 1 — Release Notes

> **Audience:** Engineering team, Confluence Product Updates space, Jira epic
> **Tone:** Precise and technical. What changed, what it does, any migration notes.

### [Feature Name] — Release Notes
**Version:** [vX.X]
**Release date:** [date]
**Platform area:** [Singularity Endpoint / Cloud / Identity / Data Lake / Purple AI]

#### What's new

| Capability | Description | Available to |
|---|---|---|
| [capability 1] | [what it does, one sentence] | [All tiers / Complete+ / Enterprise] |
| [capability 2] | [what it does, one sentence] | [All tiers / Complete+ / Enterprise] |
| [capability 3] | [what it does, one sentence] | [All tiers / Complete+ / Enterprise] |

#### How it works
[2–3 sentences on the technical implementation. Enough for an SE to understand what's happening under the hood.]

#### What changed in the UI
[List any navigation changes, new menu items, new console sections. Be specific — include where in the console this lives.]

#### API / integration notes
[Any new endpoints, changed parameters, or integration dependencies. If none, write "No API changes."]

#### Migration / enablement
[Is this on by default? Does it require an admin to enable? Any tenant-level configuration needed?]

#### Known limitations
[What doesn't work yet, edge cases, scale limits, or planned improvements. Being honest here builds trust with engineering.]

---

## Artifact 2 — Sales Enablement Brief

> **Audience:** Sales reps and SEs
> **Tone:** Confident and outcome-focused. Lead with what the customer can do now that they couldn't before. Include the competitive angle.
> **Length:** 1 page / 5-minute read

### [Feature Name] — Sales Enablement Brief

**What's new in one sentence:**
[Plain-language statement of the new capability and its business outcome]

**The customer problem we're solving:**
[2–3 sentences. Describe the pain in the customer's words, not our product language.]

**What they can do now:**
- [Outcome 1 — what the customer achieves, not what the feature does]
- [Outcome 2]
- [Outcome 3]

**Who to lead with:**
| Persona | Why they care | Opening line |
|---|---|---|
| [CISO / VP Security] | [business outcome they care about] | "[suggested opener]" |
| [SOC Analyst / Threat Hunter] | [workflow outcome they care about] | "[suggested opener]" |
| [IT / Security Engineering] | [deployment/integration outcome] | "[suggested opener]" |

**Competitive angle:**

| Competitor | Their approach | Our advantage |
|---|---|---|
| CrowdStrike | [how they handle this] | [what we do better] |
| Microsoft Defender | [how they handle this] | [what we do better] |
| [Other] | [how they handle this] | [what we do better] |

**Objections and responses:**

*"We already have [competitor capability]..."*
> [Response]

*"How is this different from what we have today?"*
> [Response]

*"Is this included in our current tier or is it an add-on?"*
> [Tier availability and pricing guidance — confirm with PMM before using]

**Demo path:**
[1–3 steps for an SE to demonstrate this capability in a live environment. Keep it simple.]

---

## Artifact 3 — CS & Support Brief

> **Audience:** Customer Success managers and Support agents
> **Tone:** Practical and Q&A-driven. CS needs to know what customers will ask before customers ask it.
> **Length:** 1 page

### [Feature Name] — CS & Support Brief

**What shipped:**
[One paragraph. What is this, who it's for, what problem it solves. Written for someone who doesn't follow sprint releases.]

**Which customers have access:**
[Tier, plan, region, or rollout phase. Be specific — "all tenants on Complete and above" not "most customers."]

**How customers will find it:**
[Where in the console does this appear? Is there an in-app notification, a tooltip, an onboarding modal?]

**Top questions customers will ask:**

*Q: [Most common expected question]*
A: [Answer]

*Q: [Second most common question]*
A: [Answer]

*Q: [Third most common question]*
A: [Answer]

*Q: What if it doesn't work / gives wrong results?*
A: [Troubleshooting steps and escalation path]

*Q: Is this replacing [existing feature]?*
A: [Answer — be clear if anything is deprecated]

**Escalation path:**
[Who does CS contact if they can't resolve a customer issue? Eng contact, Slack channel, or JIRA project.]

**Known issues / limitations to communicate proactively:**
[Anything CS should get ahead of rather than waiting for a customer to hit it.]

---

## Artifact 4 — Executive Announcement

> **Audience:** VP Product, CPO, CRO, or your direct manager
> **Tone:** Business-impact first. Strategic framing. Metrics tied back to goals stated in the PRD.
> **Length:** Half a page — exec time is limited

### [Feature Name] — Shipped

**What we shipped:**
[One sentence. Feature name, what it does, who it's for.]

**Why it matters (business impact):**
[2–3 bullet points connecting this to a business goal — ARR, churn reduction, competitive win rate, analyst productivity. Use numbers where possible. Pull from the PRD success metrics.]

- [Impact 1 — e.g., "Targets the 34% of trials that churned citing investigation workflow friction"]
- [Impact 2 — e.g., "Closes the primary technical gap cited in 12 competitive losses to CrowdStrike in Q4"]
- [Impact 3 — e.g., "Directly supports the Purple AI ARR goal of $Xm by end of FY26"]

**What was deferred and why:**
[Be transparent. If something didn't ship, say so and explain the decision. One sentence per item.]

**Success metrics we're watching:**
| Metric | Baseline | Target | How we'll measure |
|---|---|---|---|
| [Metric from PRD] | [current value] | [target] | [tool / query] |
| [Metric from PRD] | [current value] | [target] | [tool / query] |

**What's next:**
[One sentence on the next milestone — next sprint, planned follow-up, or upcoming validation.]

---

## Artifact 5 — Customer-Facing Announcement

> **Audience:** Customers (CISOs, SOC Analysts, IT/Security leads)
> **Tone:** Clear, benefit-first, no internal jargon. Customers don't care about sprint velocity.
> **Format:** Suitable for product changelog, release email, or in-app notification

### [Feature Name] is now available

**The short version:**
[One sentence. What's new and what can they do now that they couldn't before.]

**What this means for your team:**
[2–3 sentences describing the customer benefit. Write in second person ("your SOC team", "you can now"). Focus on the workflow improvement, not the feature mechanics.]

**How to get started:**
1. [Step 1 — where to find it in the console]
2. [Step 2 — any setup or configuration needed]
3. [Step 3 — first action to try]

**Available on:** [tier / plan]

**Learn more:** [link to help doc, release notes, or demo video — placeholder if not yet published]

---

## Artifact 6 — Internal Slack Announcement

> **Audience:** Internal team (`#product-announcements` or squad channel)
> **Tone:** Human, celebratory, concise. One paragraph. Link to the Confluence page for details.
> **Length:** 3–5 sentences maximum

🚀 **[Feature Name] is live.**

[One sentence on what shipped.] [One sentence on the customer problem it solves.] [One sentence on why the team should be proud of this one — the hard part, the breakthrough, or the impact.] Full details in Confluence: [link] — and the sales and CS briefs are ready to share.

---

## Launch Checklist

Run through this before distributing anything:

**Content**
- [ ] Release notes are accurate — scope matches what actually shipped
- [ ] Deferred items are documented and not mentioned in customer-facing artifacts
- [ ] Metrics in the exec announcement trace back to goals in the PRD
- [ ] CS brief addresses the 3 most predictable customer questions
- [ ] Sales brief has a concrete competitive angle (not just "we're better")
- [ ] Customer announcement has no internal jargon or acronyms

**Review**
- [ ] Exec announcement reviewed by your manager or GPM
- [ ] CS brief shared with CS team lead (get a thumbs up before distributing)
- [ ] Sales brief shared with PMM or SE lead for accuracy check

**Distribution**
- [ ] Release notes published to Confluence (Product Updates space)
- [ ] Release notes linked to the Jira epic
- [ ] Sales brief added to shared sales folder / Highspot
- [ ] CS brief posted to CS Confluence space and mentioned in CS Slack channel
- [ ] Slack announcement posted to `#product-announcements`
- [ ] Epic marked as Done in Jira

---

*See `example-launch-pack.md` for a fully worked example using Purple AI.*
*Part of the [Launch Workflow](launch-workflow.md) · [Product Management Lifecycle](../README.md)*

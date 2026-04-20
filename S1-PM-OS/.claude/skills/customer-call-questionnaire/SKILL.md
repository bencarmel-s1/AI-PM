---
name: customer-call-questionnaire
description: Audit and improve a customer interview guide. Invoke when you have a questionnaire draft and want to stress-test the questions before running calls.
---

# Skill: Customer Call Questionnaire Improvement

Your interview questions shape the quality of everything you learn from customers. Claude can audit your current questions, identify structural gaps, and help you iterate toward sharper, more insight-generating conversations.

---

## When to use this

- Before launching a new research cycle
- When customer calls keep producing vague or inconsistent insights
- When you want to standardize discovery practice across your team
- When preparing for a research sprint with exec-level output expectations

---

## Step 1: Analyze the existing questionnaire

Start with a diagnostic before making any changes:

```
Review this customer call questionnaire: @interview-template.md
Assess its clarity, flow, coverage, and signal quality.
Identify leading, vague, or redundant questions.
Summarize strengths and weaknesses — don't rewrite anything yet.
```

Claude will map each question for quality, flag structural issues, and give you an overview before suggesting any changes.

---

## Step 2: Assess individual questions

If you want to drill into specific questions — or review questions one-by-one with your team:

```
For each question in @interview-template.md, classify it (open-ended, leading, behavioral, etc.)
and flag any that might produce weak signal or biased responses.
```

---

## Step 3: Identify gaps

Ask Claude to check whether your questionnaire covers the discovery dimensions you need:

```
Map the questions in @interview-template.md against core discovery dimensions:
problem context, current behavior, alternatives considered, decision drivers, outcomes, constraints.
Where are the gaps?
```

This is especially useful when feedback keeps coming back shallow — it often means whole areas of customer experience aren't being explored.

---

## Step 4: Get improvement recommendations

Once you understand the issues:

```
Based on the analysis, suggest improvements to the questionnaire.
Focus on better question formulations and sequencing.
Keep the intent of each original question intact.
```

---

## Step 5: Frame for leadership (if needed)

If you're presenting research process improvements to stakeholders or justifying a change in discovery approach:

```
Summarize the questionnaire analysis in an executive-level format.
Highlight the risks of the current structure and how the improvements increase strategic clarity.
```

---

## Tips

**Provide your research goals upfront.** Claude gives better recommendations when it knows what you're trying to learn:

```
Our goal for this cycle is to understand why enterprise accounts churn in the first 90 days.
With that in mind, review @interview-template.md for gaps.
```

**Run this before every major research cycle.** It takes 5 minutes and meaningfully sharpens the signal you'll get back.

# [Feature Name]: Experiment Readout
**Author:** [Your Name], [Your Role]
**Date:** [Date]
**Status:** [Recommendation ready / Under review]

> **How to use this template:** Fill in each section after your A/B test completes. Work through the analysis in order: topline → segmentation → quality → leading indicators. Never stop at topline. Delete placeholder text before sharing.

---

## Executive Summary

[One clear recommendation. Ship / iterate / kill — and for which segments.]

✅ **[ACTION] for [segment]**
❌ **[ACTION] for [segment]**

[2-3 sentences: what the key metrics showed and why you're making this recommendation.]

---

## Experiment Design

| Parameter | Value |
|-----------|-------|
| Experiment type | A/B test ([split]) |
| Total users | [number] |
| Control group | [number] users — [describe experience] |
| Treatment group | [number] users — [describe experience] |
| Run time | [duration] |
| Primary metric | [metric name] |
| Secondary metrics | [metric names] |
| Leading indicators | [metric names] |

---

## Topline Results

| Group | Users | [Primary Metric] | Rate |
|-------|-------|-----------------|------|
| Control | [number] | [number] | [%] |
| Treatment | [number] | [number] | [%] |
| **Lift** | | **[+/-number]** | **[+/-pp]** |

- p-value = [value] ([significant / not significant] at p < 0.05)
- 95% CI: [[lower]%, [upper]%]

**Why the topline [overstates / understates / tells the full story]:** [Explain if segmentation is needed to understand the result.]

---

## Segment Analysis

| Segment | Control Rate | Treatment Rate | Lift | Significance |
|---------|-------------|----------------|------|--------------|
| [Segment 1 — target] | [%] | [%] | [+pp] | p = [value] [✓/—] |
| [Segment 2] | [%] | [%] | [+pp] | p = [value] |
| [Segment 3] | [%] | [%] | [+/-pp] | p = [value] |

**Key finding:** [Describe what the segmentation reveals. Which segment is driving the result? Which segment is being hurt?]

**Why this pattern makes sense:** [Connect the data to your mental model of the users.]

---

## Quality Metrics

*Filtered to [activated / converted] users only.*

| Metric | Control | Treatment | Lift |
|--------|---------|-----------|------|
| [Retention metric] | [%] | [%] | [+pp] |
| [Engagement metric] | [number] | [number] | [X]x |
| p-value | | | < [threshold] |

**Interpretation:** [Did we get more activations, or better ones? What does the engagement data say about user quality?]

---

## Leading Indicators

| Metric | Control | Treatment | Lift |
|--------|---------|-----------|------|
| [Feature adoption rate] | [%] | [%] | [X]x |
| [Viral/growth indicator] | [%] | [%] | [X]x |

**Why these matter:** [Explain why each leading indicator predicts long-term retention or growth. Include any historical correlation data you have.]

---

## Expected Impact at Full Rollout

*For [target segment] only:*

| Metric | Projection |
|--------|------------|
| [Segment] signups/month | [number] |
| Adoption rate | [%] |
| Users exposed/month | [number] |
| Activation/conversion lift | [+pp] |
| Incremental users/month | [+number] |
| MRR lift | +$[X]/month |
| ARR lift | +$[X]/year |
| 3-year LTV | $[X] |
| 3-year ROI | [X]x |

---

## Recommendation

**[Ship / Iterate / Kill] — [for which segments].**

[2-3 bullet points summarizing why:
- Key metric result
- Quality signal
- Strategic rationale]

**Explicitly exclude [segment] because:** [reason — what would need to be true for this segment to get the feature?]

---

## Next Steps

| Action | Owner | Timeline |
|--------|-------|----------|
| [Action 1] | [Role] | [When] |
| [Action 2] | [Role] | [When] |
| [Action 3] | [Role] | [When] |

**Watch for:** [Any metrics to monitor post-launch that could trigger revisiting the decision.]

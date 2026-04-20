# Data Analysis Workflow

A complete system for making confident, data-driven product decisions using AI as your analysis partner.

## When to Trigger

Say "data analysis", "analyze my data", "impact estimate", or "experiment readout" when you have CSV data files and want to build a data-backed case.

## What This Produces

- A data-backed problem analysis document (shareable with leadership)
- A three-scenario ROI model (pessimistic / realistic / optimistic)
- An experiment readout with segmentation, quality metrics, and ship/kill recommendation

## Key Constraints

- No special setup needed — works with CSV exports from any analytics tool (Mixpanel, Amplitude, etc.)
- Place data files in the same folder you open Claude Code from
- Use `@filename.csv` syntax to reference data files directly
- Decision rule: if pessimistic case >2x ROI over 3 years, build it

## Files in This Workflow

1. `data-analysis-workflow.md` — Full step-by-step workflow, start here
2. `impact-estimation-framework.md` — Formula and methodology for estimating feature ROI
3. `problem-analysis-template.md` — Fillable template for problem discovery documents
4. `experiment-readout-template.md` — Fillable template for A/B test readouts
5. `example-problem-analysis.md` — Complete reference problem analysis
6. `example-impact-estimate.md` — Complete reference impact model
7. `example-experiment-readout.md` — Complete reference experiment readout

## The 3-Phase Process

- Phase 1 — Discovery: Analyze funnels and surveys to find the root cause
- Phase 2 — Impact Estimation: Build ROI model with 3 scenarios to justify building
- Phase 3 — Experiment Analysis: Analyze A/B test results with segmentation + quality metrics

## What's Next

Once you have your problem analysis and impact model, use `../prd-creation/` to turn your findings into a production-quality PRD.

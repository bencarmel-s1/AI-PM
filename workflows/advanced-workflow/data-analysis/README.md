# Data Analysis with Claude Code

A complete system for making confident, data-driven product decisions using AI as your analysis partner.

---

## What's in This Folder

| File | What It Is |
|------|------------|
| `data-analysis-workflow.md` | The full step-by-step workflow — start here |
| `impact-estimation-framework.md` | The formula and methodology for estimating feature ROI |
| `problem-analysis-template.md` | Fillable template for problem discovery documents |
| `experiment-readout-template.md` | Fillable template for A/B test readouts |
| `example-problem-analysis.md` | A complete reference problem analysis — shows what a finished doc looks like |
| `example-impact-estimate.md` | A complete reference impact model |
| `example-experiment-readout.md` | A complete reference experiment readout |

---

## Requirements

**No special setup needed.** This workflow is standalone — it doesn't require sub-agents or any pre-configuration. You just need:
- Claude Code open in any folder
- Your data files (CSV exports from Mixpanel, Amplitude, or any analytics tool) in the same folder you open Claude Code from

---

## Quick Start (30 seconds)

Open Claude Code in the folder where your data files live, then paste this:

```
I have product data I want to analyze to find and fix a problem.
Use @data-analysis-workflow.md to guide me through the process.
My data files are: [list your CSV/data files]
The problem I'm investigating: [1-2 sentences]
```

> **New to Claude Code?** The `@filename` syntax tells Claude to read that file as part of your prompt. Put your CSV files in the same folder as this workflow, then use `@your-file.csv` to reference them. Claude reads the data directly — you don't need to paste anything.

Claude will guide you through discovery, impact estimation, and experiment analysis — and create polished documents at each step.

---

## The 3-Phase Process

```
Phase 1 — Discovery        → Analyze funnels and surveys to find the root cause
Phase 2 — Impact Estimation → Build ROI model with 3 scenarios to justify building
Phase 3 — Experiment Analysis → Analyze A/B test results with segmentation + quality metrics
```

Full details in `data-analysis-workflow.md`.

---

## What You Get at the End

- A data-backed problem analysis document (shareable with leadership)
- A three-scenario ROI model (justifies build vs. no-build decision)
- An experiment readout with segmentation, quality metrics, and clear ship/kill recommendation
- All before you present to a single stakeholder

---

## The Documents You'll Create

| Document | Purpose |
|----------|---------|
| `[feature]-problem-analysis.md` | Problem statement, funnel data, survey evidence, proposed solution |
| `[feature]-impact-estimate.md` | ROI model with realistic/pessimistic/optimistic scenarios |
| `[feature]-roi-scenarios.md` | Three-scenario comparison table |
| `[feature]-experiment-readout.md` | A/B test results, segmentation, quality metrics, recommendation |

---

## What Makes This Workflow Powerful

Claude Code can:
- Read and analyze CSV files from Mixpanel, Amplitude, LaunchDarkly, or any analytics tool
- Process thousands of rows of event data instantly
- Segment results by any dimension (company size, role, plan, geography)
- Calculate statistical significance and confidence intervals
- Build ROI models and scenario analyses
- Create polished documents ready to share with leadership

You bring the data. Claude does the analysis. You make the decisions.

---

## What's Next

Once you have your problem analysis, impact model, and experiment readout, the next step is writing the PRD.

Use [`../prd-creation/`](../prd-creation/) to turn your findings into a production-quality requirements document — with Socratic questioning and expert agent reviews built in.

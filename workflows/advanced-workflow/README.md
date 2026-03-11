← [Back to all workflows](../README.md)

# Advanced Workflows

Multi-phase workflows for larger, more complex PM work. Each is a complete system — not just prompts, but a repeatable process with templates, examples, and guidance for getting to a polished output.

---

## Workflows

| Folder | What It Does | Time | Needs Setup? |
|--------|--------------|------|--------------|
| [`prd-creation/`](./prd-creation/) | Write a production-quality PRD with Socratic questioning + 3 expert agent reviews | 45–60 min | Yes — 3 sub-agents required |
| [`data-analysis/`](./data-analysis/) | Analyze funnels and surveys, build ROI models, and read out A/B test results | 30–90 min | No — works out of the box |
| [`product-strategy/`](./product-strategy/) | Develop a defensible product strategy using Rumelt's Kernel — diagnosis, strategic choices, and executive slide deck | 60–90 min | No — works out of the box |

---

## Which One Should I Use?

- **Starting a new feature from scratch?** → Use `prd-creation/`
- **Have data and need to understand it or justify a decision?** → Use `data-analysis/`
- **Running an experiment and need a readout?** → Use `data-analysis/` (Phase 3)
- **Need to develop or present a product strategy?** → Use `product-strategy/`

---

## New to Claude Code?

Both workflows use `@filename` syntax to reference files. This tells Claude to read that file as part of your prompt. Example:

```
Use @data-analysis-workflow.md to guide me.
My data is in @funnel-export.csv
```

Claude will read both files and use them in its response. You don't need to paste the contents manually.

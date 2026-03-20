← [Back to all workflows](../README.md)

# Advanced Workflows

Multi-phase workflows for larger, more complex PM work. Each is a complete system — not just prompts, but a repeatable process with templates, examples, and guidance for getting to a polished output.

---

## Workflows

| Folder | What It Does | Time | Needs Setup? |
|--------|--------------|------|--------------|
| [`feature-request-discovery/`](./feature-request-discovery/) | Query Jira live for feature requests, theme and quantify them, score against OKRs, surface revenue signal and competitive gaps — full discovery brief in one session | 45–65 min | Yes — Jira MCP required |
| [`prd-creation/`](./prd-creation/) | Write a production-quality PRD with Socratic questioning + 3 expert agent reviews | 45–60 min | Yes — 3 sub-agents required |
| [`data-analysis/`](./data-analysis/) | Analyze funnels and surveys, build ROI models, and read out A/B test results | 30–90 min | No — works out of the box |
| [`product-strategy/`](./product-strategy/) | Develop a defensible product strategy using Rumelt's Kernel — diagnosis, strategic choices, and executive slide deck | 60–90 min | No — works out of the box |
| [`multi-agent-review/`](./multi-agent-review/) | Run engineer, executive, and user-researcher agents in parallel on a spec — unified synthesis in one session | 30–45 min | No — 3 sub-agents pre-installed |

---

## Which One Should I Use?

- **Need to understand what customers are requesting and what to build next?** → Use `feature-request-discovery/`
- **Starting a new feature from scratch?** → Use `prd-creation/`
- **Have data and need to understand it or justify a decision?** → Use `data-analysis/`
- **Running an experiment and need a readout?** → Use `data-analysis/` (Phase 3)
- **Need to develop or present a product strategy?** → Use `product-strategy/`
- **Have a spec or PRD that needs multi-perspective review?** → Use `multi-agent-review/`

---

## New to Claude Code?

Both workflows use `@filename` syntax to reference files. This tells Claude to read that file as part of your prompt. Example:

```
Use @data-analysis-workflow.md to guide me.
My data is in @funnel-export.csv
```

Claude will read both files and use them in its response. You don't need to paste the contents manually.

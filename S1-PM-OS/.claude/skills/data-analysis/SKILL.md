---
name: data-analysis
description: >
  Data analysis and exploration for Python scripts, Jupyter notebooks, and datasets.
  Use when: user shares a dataset (CSV, Excel, JSON, Parquet) and wants insights;
  user asks to 'analyze this data', 'explore this dataset', 'run EDA', 'data analysis',
  or 'visualize' data; user says 'run this python script', 'help with this notebook',
  'what does this script do', '.ipynb', 'jupyter notebook', 'run this .py', 'pandas',
  'matplotlib', or references data wrangling, statistics, or charting.
  Also trigger when the user shares a .py or .ipynb file and asks what it does or
  how to improve it — even if they don't say "data analysis" explicitly.
user-invocable: true
---

# Data Analysis

Guide exploratory data analysis (EDA) for any tabular dataset or Python/Jupyter
data script. Follow the 5-step workflow below, adapting depth to what the user needs.

---

## 5-Step EDA Workflow

### Step 1 — Load

Determine file type and load accordingly:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# CSV
df = pd.read_csv("data.csv")

# Excel
df = pd.read_excel("data.xlsx", sheet_name=0)

# JSON (records)
df = pd.read_json("data.json")

# Parquet
df = pd.read_parquet("data.parquet")
```

If the file path is unknown, ask the user. If the format is ambiguous, check the
extension or peek at the first few bytes.

---

### Step 2 — Inspect

Run a quick health check to understand shape, types, and data quality:

```python
# Shape and types
print(df.shape)
print(df.dtypes)

# First look
df.head()

# Summary statistics
df.describe(include="all")

# Null counts
df.isnull().sum().sort_values(ascending=False)

# Duplicate rows
df.duplicated().sum()

# Column cardinality (useful for categoricals)
df.nunique().sort_values()
```

Summarize the findings: row/column count, any columns with high null rates, obvious
type mismatches (e.g., dates stored as strings), and duplicate rows.

---

### Step 3 — Clean

Address the issues surfaced in Step 2 — but only what's necessary for the
analysis at hand. Don't over-engineer cleaning for a quick EDA.

Common patterns:

```python
# Drop columns with >50% nulls
df = df.dropna(thresh=len(df) * 0.5, axis=1)

# Fill nulls — numeric with median, categorical with mode
df["price"] = df["price"].fillna(df["price"].median())
df["category"] = df["category"].fillna(df["category"].mode()[0])

# Parse dates
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Strip whitespace from string columns
df["name"] = df["name"].str.strip()

# Rename for convenience
df = df.rename(columns={"old name": "clean_name"})

# Cast types
df["id"] = df["id"].astype(str)
```

---

### Step 4 — Visualize

Pick charts that match the question and the column types:

| Goal | Chart | Code |
|------|-------|------|
| Distribution of a numeric col | Histogram + KDE | `sns.histplot(df["col"], kde=True)` |
| Compare groups | Box plot | `sns.boxplot(x="group", y="value", data=df)` |
| Relationship between two numerics | Scatter | `sns.scatterplot(x="a", y="b", data=df)` |
| Correlation matrix | Heatmap | `sns.heatmap(df.corr(), annot=True)` |
| Trend over time | Line plot | `df.set_index("date")["value"].plot()` |
| Category counts | Bar chart | `df["category"].value_counts().plot(kind="bar")` |
| Pairwise overview | Pair plot | `sns.pairplot(df[numeric_cols])` |

Always label axes and add a title:

```python
fig, ax = plt.subplots(figsize=(8, 4))
sns.histplot(df["revenue"], kde=True, ax=ax)
ax.set_title("Revenue Distribution")
ax.set_xlabel("Revenue ($)")
plt.tight_layout()
plt.show()
```

---

### Step 5 — Summarize

Close with a plain-language insight report using this structure:

```
## Dataset Overview
- Rows: X, Columns: Y
- Key columns: <list with types>
- Data quality: <null rates, duplicates, type issues found>

## Key Findings
1. <most important pattern or stat>
2. <second finding>
3. <third finding>

## Anomalies / Watch-outs
- <outliers, unexpected nulls, skewed distributions, etc.>

## Suggested Next Steps
- <specific analysis or question worth pursuing>
```

---

## Execution Modes

### In JupyterLab / IDE with `mcp__ide__executeCode`

If the `mcp__ide__executeCode` tool is available, run code directly in the active
kernel and show live output. Prefer this over generating static code blocks.

```
→ Use mcp__ide__executeCode to run each step interactively
→ Capture outputs (df.head(), describe(), charts) and narrate findings
→ Ask before overwriting data — always clean into a new variable (df_clean)
```

### Without live execution

Generate clean, runnable code blocks the user can paste into a notebook or script.
Keep cells self-contained so they can be run in order without modification.

---

## Tips

- **Don't assume column meaning** — ask if the schema is unfamiliar (e.g., "what does `flag_x` mean?")
- **Prefer pandas over raw Python loops** — it's faster and more readable
- **Always keep the original df untouched** — clean into `df_clean`, transform into `df_transformed`
- **Use `plt.tight_layout()`** before `plt.show()` to prevent label clipping
- **For large files (>100k rows)**, sample first: `df.sample(10_000, random_state=42)`
- **datetime handling**: always `pd.to_datetime()` with `errors="coerce"` to avoid crashes on bad dates

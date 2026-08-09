# Week 6 — Data Analysis with pandas

Move from plain Python to **pandas** — the library accountants and analysts use to slice, group, and summarize tables of data in just a line or two.

**Live site:** https://benchvue.github.io/python-lesson/week-6/

## Setup

```bash
pip3 install pandas
```

## Topics

DataFrames · Column math · `groupby` · Boolean filtering · `read_csv` · Missing values (`NaN` / `fillna`) · Pivot tables

## Lessons

| # | Topic | Animation | Code | Idea |
|---|-------|-----------|------|------|
| 01 | DataFrame basics | [▶ Demo](https://benchvue.github.io/python-lesson/week-6/01_dataframe_basics.html) | [.py](01_dataframe_basics.py) | A dict of lists becomes a table; sum a column. |
| 02 | groupby | [▶ Demo](https://benchvue.github.io/python-lesson/week-6/02_group_expenses.html) | [.py](02_group_expenses.py) | Total amounts per category. |
| 03 | Filtering | [▶ Demo](https://benchvue.github.io/python-lesson/week-6/03_filter_transactions.html) | [.py](03_filter_transactions.py) | A True/False mask keeps matching rows. |
| 04 | read_csv | [▶ Demo](https://benchvue.github.io/python-lesson/week-6/04_read_csv.html) | [.py](04_read_csv.py) | Load a whole CSV in one line. |
| 05 | Missing values | [▶ Demo](https://benchvue.github.io/python-lesson/week-6/05_missing_values.html) | [.py](05_missing_values.py) | Find `NaN` with `isna()`, fix with `fillna()`. |

## Putting it together

| # | Topic | Animation | Code | Idea |
|---|-------|-----------|------|------|
| 06 | Pivot table | [▶ Demo](https://benchvue.github.io/python-lesson/week-6/06_pivot_summary.html) | [.py](06_pivot_summary.py) | Reshape a long list into a Month × Category grid. |

**02 output** — a total per category (pandas sorts them):

```
Category
Meals       90
Office     350
Travel    1250
Name: Amount, dtype: int64
```

**06 output** — long data reshaped into a compact grid:

```
Category  Office  Travel
Month
Feb          150     450
Jan          200     800
Mar          300     600
```

## Quiz

Test yourself after the lessons — 6 quick questions with instant feedback and score.

| Quiz | Open | Covers |
|------|------|--------|
| Week 6 Quiz | [▶ Start](https://benchvue.github.io/python-lesson/week-6/quiz_week6.html) | import, column sum, groupby, filtering, fillna, read_csv. |

**Questions**

1. Usual pandas import → **`import pandas as pd`**
2. `df["Amount"].sum()` of `[100, -30, -20]` → **50**
3. `df.groupby("Category")["Amount"].sum()` → **a total per category**
4. `df[df["Account"] == "Revenue"]` → **only the Revenue rows**
5. `fillna(0)` on missing values → **replaces NaN with 0**
6. Load a CSV into a DataFrame → **`pd.read_csv("file.csv")`**

## From Week 4/5 to pandas

| The long way (Weeks 4–5) | The pandas way (Week 6) |
|--------------------------|--------------------------|
| `open()` + `csv.DictReader` + loop | `pd.read_csv("file.csv")` |
| `defaultdict` to group + sum | `df.groupby("col")["val"].sum()` |
| `if row["x"] == ...` inside a loop | `df[df["x"] == ...]` |
| `try/except` around `float()` | `fillna()` / `dropna()` |

## Run in Terminal (macOS)

```bash
cd /Users/you/Documents/python-lesson/week-6   # go to the folder
python3 01_dataframe_basics.py                 # build a DataFrame
python3 04_read_csv.py                         # load a CSV
```

Tip: type the start of a filename and press **Tab ⇥** to auto-complete it.

## Practice

Load a transactions CSV with `read_csv`, `fillna(0)` any gaps, then
`groupby("account")["amount"].sum()` to get a total per account.

Every animation has **▶ Play / ❚❚ Pause / ⤓ Step Into / ⤾ Step Over / ■ Stop** —
Step Into walks each row into its group; Step Over runs the whole operation as one step.

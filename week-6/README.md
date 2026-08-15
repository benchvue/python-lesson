# Week 6 — Data Visualization with matplotlib

Turn accounting numbers into **charts**. This week draws bar, line and pie charts with
**matplotlib**, styles them for a report, and finishes by letting **pandas** plot for you.

**Live site:** https://benchvue.github.io/python-lesson/week-6/

## Setup

```bash
pip3 install matplotlib pandas
```

## Topics

`plt.bar` · `plt.plot` (line) · `plt.pie` · grouped bars · colors / `axhline` / `grid` / `legend` · `savefig` · `DataFrame.plot()`

## Lessons

| # | Topic | Animation | Code | Idea |
|---|-------|-----------|------|------|
| 01 | Bar chart | [▶ Demo](https://benchvue.github.io/python-lesson/week-6/01_expense_chart.html) | [.py](01_expense_chart.py) | `plt.bar()` — one bar per category. |
| 02 | Line chart | [▶ Demo](https://benchvue.github.io/python-lesson/week-6/02_revenue_line.html) | [.py](02_revenue_line.py) | `plt.plot()` — a trend over months. |
| 03 | Pie chart | [▶ Demo](https://benchvue.github.io/python-lesson/week-6/03_expense_pie.html) | [.py](03_expense_pie.py) | `plt.pie()` — shares of a whole. |
| 04 | Grouped bars | [▶ Demo](https://benchvue.github.io/python-lesson/week-6/04_revenue_vs_expense.html) | [.py](04_revenue_vs_expense.py) | Two series side by side + legend. |
| 05 | Styling a chart | [▶ Demo](https://benchvue.github.io/python-lesson/week-6/05_styled_chart.html) | [.py](05_styled_chart.py) | Colors, zero line, grid. |

## Putting it together

| # | Topic | Animation | Code | Idea |
|---|-------|-----------|------|------|
| 06 | DataFrame.plot() | [▶ Demo](https://benchvue.github.io/python-lesson/week-6/06_dataframe_plot.html) | [.py](06_dataframe_plot.py) | `groupby` then `.plot(kind="bar")` in one line. |

Every script ends with `plt.savefig("...png")`, so running it drops a real image next to the file.

**01** → `monthly_expenses.png`  ·  **02** → `revenue_trend.png`  ·  **03** → `expense_pie.png`
**04** → `revenue_vs_expenses.png`  ·  **05** → `monthly_profit.png`  ·  **06** → `spending_by_category.png`

**06 also prints the grouped Series before plotting it:**

```
Category
Meals       90
Office     350
Travel    1250
Name: Amount, dtype: int64
```

## Chart cheat-sheet

| You want to show… | Use | Key call |
|-------------------|-----|----------|
| Compare categories | Bar | `plt.bar(labels, values)` |
| A trend over time | Line | `plt.plot(x, y, marker="o")` |
| Parts of a whole | Pie | `plt.pie(values, labels=..., autopct="%1.1f%%")` |
| Two series compared | Grouped bars | `plt.bar()` twice, x-positions shifted |
| Positive vs negative | Colored bars | `color=["green" if v>=0 else "red" ...]` |
| A pandas summary | Any | `series.plot(kind="bar")` |

## Quiz

| Quiz | Open | Covers |
|------|------|--------|
| Week 6 Quiz | [▶ Start](https://benchvue.github.io/python-lesson/week-6/quiz_week6.html) | import, `bar`, `savefig`, `autopct`, grouped bars, `DataFrame.plot()`. |

**Questions**

1. Import for plotting → **`import matplotlib.pyplot as plt`**
2. Draw a bar chart → **`plt.bar()`**
3. `plt.savefig("chart.png")` → **saves the chart to an image file**
4. `autopct="%1.1f%%"` in a pie → **prints each slice's percentage**
5. Two bar series side by side → **call `plt.bar()` twice with shifted x-positions**
6. `summary.plot(kind="bar")` → **draws a bar chart via matplotlib**

## Run in Terminal (macOS)

```bash
cd /Users/you/Documents/python-lesson/week-6   # go to the folder
python3 01_expense_chart.py                    # writes monthly_expenses.png
open monthly_expenses.png                      # view the saved image
```

Tip: type the start of a filename and press **Tab ⇥** to auto-complete it.

## Practice

Take the `groupby` total from Week 6's pandas lessons and chart it:
`summary.plot(kind="bar", title="Spending by Category")`, then `plt.savefig()`.
Swap `kind="bar"` for `kind="line"` or `kind="pie"` and compare which tells the story best.

Every animation has **▶ Play / ❚❚ Pause / ⤓ Step Into / ⤾ Step Over / ■ Stop** —
watch each chart draw itself as the matplotlib calls run line by line.

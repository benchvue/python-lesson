# Week 4 — Files, CSV, Dates & Excel

Read and write the files accountants actually use: text, CSV, and Excel — plus date handling.

**Live site:** https://benchvue.github.io/python-lesson/week-4/

## Topics

Text files · CSV files · `datetime` · Month-end dates · Excel with `openpyxl` · Formulas · File automation

## Lessons

| # | Topic | Animation | Code | Idea |
|---|-------|-----------|------|------|
| 01 | Write a text file | [▶ Demo](https://benchvue.github.io/python-lesson/week-4/01_write_report.html) | [.py](01_write_report.py) | `open(..., "w")` + `with` saves and closes. |
| 02 | Read a CSV | [▶ Demo](https://benchvue.github.io/python-lesson/week-4/02_read_csv_transactions.html) | [.py](02_read_csv_transactions.py) | `DictReader` rows → running total. |
| 03 | Dates | [▶ Demo](https://benchvue.github.io/python-lesson/week-4/03_date_example.html) | [.py](03_date_example.py) | `strftime`, `.year`, `.month`, `.day`. |
| 04 | Create Excel | [▶ Demo](https://benchvue.github.io/python-lesson/week-4/04_create_excel_report.html) | [.py](04_create_excel_report.py) | Build a sheet, `append()` rows, `save()`. |
| 05 | Read Excel | [▶ Demo](https://benchvue.github.io/python-lesson/week-4/05_read_excel_report.html) | [.py](05_read_excel_report.py) | `load_workbook` + `iter_rows` → tuples. |
| 06 | Excel formula | [▶ Demo](https://benchvue.github.io/python-lesson/week-4/06_excel_formula.html) | [.py](06_excel_formula.py) | Store `"=B1-B2"`; Excel computes it. |

## Advanced

| # | Topic | Animation | Code | Idea |
|---|-------|-----------|------|------|
| 07 | Many CSV lines | [▶ Demo](https://benchvue.github.io/python-lesson/week-4/07_csv_many_rows.html) | [.py](07_csv_many_rows.py) | 12 rows → group by account, summarize, write a new CSV. |
| 08 | 5-year quarterly revenue | [▶ Demo](https://benchvue.github.io/python-lesson/week-4/08_excel_quarterly_revenue.html) | [.py](08_excel_quarterly_revenue.py) | 5 × 4 grid with `SUM`, YoY growth %, `AVERAGE`. |

**07 output** — read → convert → group → report → write:

```
Account       Lines         Total
Revenue           4     21,550.00
Supplies          2       -670.00
Rent              3     -5,400.00
Payroll           3     -9,450.00
NET              12      6,030.00
```

**08 output** — Python writes the grid, Excel keeps the formulas live:

```
Year           Total    Growth
2022         533,000
2023         612,000     14.8%
2024         714,000     16.7%
2025         828,000     16.0%
2026         943,000     13.9%
```

## Quiz

Test yourself after the lessons — 6 quick questions with instant feedback and score.

| Quiz | Open | Covers |
|------|------|--------|
| Week 4 Quiz | [▶ Start](https://benchvue.github.io/python-lesson/week-4/quiz_week4.html) | file modes, CSV casting, dates, Excel save & formulas, grouping. |

**Questions**

1. What does `"w"` mode do to an existing file? → **Overwrites everything**
2. Why is `float()` needed on `row["amount"]`? → **CSV values come in as strings**
3. `strftime("%Y-%m-%d")` on 17 Mar 2026 → **2026-03-17**
4. What makes an openpyxl workbook appear on disk? → **`wb.save("file.xlsx")`**
5. What does Python compute for `sheet["B3"] = "=B1-B2"`? → **Nothing — Excel computes it**
6. Three Rent rows of −1800 in a `defaultdict` total → **−5400.0**

## Setup

Lessons 04–06 and 08 need openpyxl:

```bash
pip3 install openpyxl
```

## Run in Terminal (macOS)

```bash
cd /Users/you/Documents/python-lesson/week-4   # go to the folder
python3 01_write_report.py                     # creates monthly_report.txt
python3 07_csv_many_rows.py                    # creates ledger.csv + account_summary.csv
python3 08_excel_quarterly_revenue.py          # creates quarterly_revenue.xlsx
```

Tip: type the start of a filename and press **Tab ⇥** to auto-complete it.

## Practice

Export a month of transactions to CSV, group them by account with `07`'s pattern,
then write the result to an Excel file with a `=SUM()` total row.

Every animation has **▶ Play / ❚❚ Pause / ⤓ Step Into / ⤾ Step Over / ■ Stop** —
Step Into walks each loop pass, Step Over skips the whole loop.

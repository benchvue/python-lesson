"""Advanced: handle a CSV with MANY lines.

Reads every transaction, groups the amounts by account,
counts the rows, and writes a summary CSV back out.
"""
import csv
from collections import defaultdict

SOURCE = "ledger.csv"
SUMMARY = "account_summary.csv"

# --- build a bigger sample file (12 data lines) ---
rows = [
    ["date", "account", "amount"],
    ["2026-01-03", "Revenue",  "5200"],
    ["2026-01-07", "Rent",     "-1800"],
    ["2026-01-11", "Payroll",  "-3100"],
    ["2026-01-15", "Revenue",  "4400"],
    ["2026-02-02", "Supplies", "-260"],
    ["2026-02-09", "Revenue",  "6100"],
    ["2026-02-14", "Rent",     "-1800"],
    ["2026-02-21", "Payroll",  "-3100"],
    ["2026-03-01", "Revenue",  "5850"],
    ["2026-03-08", "Supplies", "-410"],
    ["2026-03-16", "Rent",     "-1800"],
    ["2026-03-27", "Payroll",  "-3250"],
]

with open(SOURCE, "w", newline="", encoding="utf-8") as file:
    csv.writer(file).writerows(rows)

# --- read every line, accumulate per account ---
totals = defaultdict(float)   # account -> running total
counts = defaultdict(int)     # account -> number of lines
grand_total = 0.0
line_count = 0

with open(SOURCE, "r", encoding="utf-8") as file:
    for row in csv.DictReader(file):
        amount = float(row["amount"])       # text -> number
        totals[row["account"]] += amount
        counts[row["account"]] += 1
        grand_total += amount
        line_count += 1

# --- report, biggest total first ---
print(f"Read {line_count} transactions\n")
print(f"{'Account':<12}{'Lines':>7}{'Total':>14}")
print("-" * 33)
for account, total in sorted(totals.items(), key=lambda kv: kv[1], reverse=True):
    print(f"{account:<12}{counts[account]:>7}{total:>14,.2f}")
print("-" * 33)
print(f"{'NET':<12}{line_count:>7}{grand_total:>14,.2f}")

# --- write the summary back to a new CSV ---
with open(SUMMARY, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["account", "lines", "total"])
    for account, total in sorted(totals.items()):
        writer.writerow([account, counts[account], f"{total:.2f}"])

print(f"\n{SUMMARY} created.")

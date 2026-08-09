# Putting it together: read a CSV where one row is broken,
# and total the good rows without crashing.
import csv

rows = [
    ["date", "amount"],
    ["2026-01-01", "1500"],
    ["2026-01-02", "oops"],    # bad data
    ["2026-01-03", "2200"],
    ["2026-01-04", ""],        # empty
]

with open("data.csv", "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(rows)

total = 0
skipped = 0

with open("data.csv", "r", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        try:
            total += float(row["amount"])
        except ValueError:
            skipped += 1
            print("Skipped bad row:", row["amount"] or "(empty)")

print("Total of good rows:", total)
print("Rows skipped:", skipped)

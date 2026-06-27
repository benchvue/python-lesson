import csv

csv_file = "transactions.csv"

sample_data = [
    ["date", "account", "amount"],
    ["2026-01-01", "Cash", "1000"],
    ["2026-01-02", "Supplies Expense", "-150"],
    ["2026-01-03", "Revenue", "2500"]
]

with open(csv_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(sample_data)

total = 0

with open(csv_file, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        total += float(row["amount"])

print("Total transaction amount:", total)

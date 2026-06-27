report = """Monthly Report
Revenue: 100000
Expenses: 75000
Net Income: 25000
"""

with open("monthly_report.txt", "w", encoding="utf-8") as file:
    file.write(report)

print("monthly_report.txt created.")

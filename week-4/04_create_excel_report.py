from openpyxl import Workbook

workbook = Workbook()
sheet = workbook.active
sheet.title = "Income Statement"

sheet["A1"] = "Account"
sheet["B1"] = "Amount"

data = [
    ("Revenue", 100000),
    ("Expenses", 70000),
    ("Net Income", 30000)
]

for row in data:
    sheet.append(row)

workbook.save("income_statement.xlsx")
print("income_statement.xlsx created.")

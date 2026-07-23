from openpyxl import Workbook

workbook = Workbook()
sheet = workbook.active
sheet.title = "Profit"

sheet["A1"] = "Revenue"
sheet["B1"] = 120000

sheet["A2"] = "Expenses"
sheet["B2"] = 80000

sheet["A3"] = "Profit"
sheet["B3"] = "=B1-B2"

workbook.save("profit_formula.xlsx")
print("profit_formula.xlsx created with formula.")

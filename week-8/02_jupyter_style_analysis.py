# This file uses a simple style similar to Jupyter Notebook cells.

import pandas as pd

transactions = pd.DataFrame({
    "Account": ["Revenue", "Expense", "Revenue", "Expense"],
    "Amount": [1000, -300, 2500, -700]
})

print("Data Preview")
print(transactions.head())

print("\nTotal Amount")
print(transactions["Amount"].sum())

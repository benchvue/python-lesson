import pandas as pd

data = {
    "Account": ["Revenue", "Rent Expense", "Salary Expense"],
    "Amount": [100000, -12000, -45000]
}

df = pd.DataFrame(data)

print(df)
print("Total:", df["Amount"].sum())

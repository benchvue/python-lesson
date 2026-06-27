import pandas as pd

data = {
    "Date": ["2026-01-01", "2026-01-02", "2026-01-03", "2026-01-04"],
    "Account": ["Revenue", "Rent Expense", "Revenue", "Office Expense"],
    "Amount": [10000, -2000, 8000, -500]
}

df = pd.DataFrame(data)

summary = df.groupby("Account")["Amount"].sum().reset_index()
net_income = df["Amount"].sum()

print("Account Summary")
print(summary)

print("\nNet Income:", net_income)

summary.to_csv("account_summary.csv", index=False)
print("\naccount_summary.csv created.")

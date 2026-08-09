import pandas as pd

data = {
    "Date": ["2026-01-01", "2026-01-02", "2026-01-03"],
    "Account": ["Revenue", "Supplies Expense", "Revenue"],
    "Amount": [5000, -250, 3200]
}

df = pd.DataFrame(data)

revenue_df = df[df["Account"] == "Revenue"]

print(revenue_df)

# Real data has gaps. pandas marks them NaN - fill or drop them.
import pandas as pd

data = {
    "Account": ["Revenue", "Rent", "Supplies", "Payroll"],
    "Amount":  [5000, None, -250, None]     # two missing values
}

df = pd.DataFrame(data)

print("Missing per column:")
print(df.isna().sum())

df["Amount"] = df["Amount"].fillna(0)      # replace NaN with 0

print("\nAfter fillna(0):")
print(df)
print("Total:", df["Amount"].sum())

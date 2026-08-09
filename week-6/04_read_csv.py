# Read a CSV straight into a DataFrame - one line does it all.
import pandas as pd

# make a sample file first
sample = "date,account,amount\n2026-01-01,Cash,1000\n2026-01-02,Supplies,-150\n2026-01-03,Revenue,2500\n"
with open("ledger.csv", "w", encoding="utf-8") as f:
    f.write(sample)

df = pd.read_csv("ledger.csv")

print(df)
print("Rows:", len(df))
print("Columns:", list(df.columns))
print("Total amount:", df["amount"].sum())

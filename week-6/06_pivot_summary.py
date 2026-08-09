# A pivot table summarizes a long list into a compact grid.
import pandas as pd

data = {
    "Month":    ["Jan", "Jan", "Feb", "Feb", "Mar", "Mar"],
    "Category": ["Office", "Travel", "Office", "Travel", "Office", "Travel"],
    "Amount":   [200, 800, 150, 450, 300, 600]
}

df = pd.DataFrame(data)

pivot = df.pivot_table(
    index="Month",
    columns="Category",
    values="Amount",
    aggfunc="sum"
)

print(pivot)
print("\nGrand total:", df["Amount"].sum())

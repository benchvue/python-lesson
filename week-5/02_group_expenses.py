import pandas as pd

data = {
    "Category": ["Office", "Travel", "Office", "Meals", "Travel"],
    "Amount": [200, 800, 150, 90, 450]
}

df = pd.DataFrame(data)

summary = df.groupby("Category")["Amount"].sum()

print(summary)

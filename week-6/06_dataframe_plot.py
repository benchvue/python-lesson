import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Category": ["Office", "Travel", "Office", "Meals", "Travel"],
    "Amount": [200, 800, 150, 90, 450]
}

df = pd.DataFrame(data)
summary = df.groupby("Category")["Amount"].sum()

summary.plot(kind="bar", title="Spending by Category")
plt.ylabel("Amount")
plt.tight_layout()
plt.savefig("spending_by_category.png")

print(summary)
print("spending_by_category.png created.")

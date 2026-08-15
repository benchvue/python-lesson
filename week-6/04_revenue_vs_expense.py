import matplotlib.pyplot as plt

quarters = ["Q1", "Q2", "Q3", "Q4"]
revenue = [50000, 62000, 58000, 70000]
expenses = [40000, 45000, 43000, 50000]

x = range(len(quarters))
plt.bar([i - 0.2 for i in x], revenue, width=0.4, label="Revenue")
plt.bar([i + 0.2 for i in x], expenses, width=0.4, label="Expenses")

plt.xticks(list(x), quarters)
plt.title("Revenue vs Expenses")
plt.legend()
plt.savefig("revenue_vs_expenses.png")

print("revenue_vs_expenses.png created.")
plt.show()

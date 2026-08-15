import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]
profit = [8000, -3000, 5000, 12000]

colors = ["green" if p >= 0 else "red" for p in profit]

plt.figure(figsize=(7, 4))
plt.bar(months, profit, color=colors)
plt.axhline(0, color="black", linewidth=0.8)
plt.title("Monthly Profit")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.savefig("monthly_profit.png")

print("monthly_profit.png created.")

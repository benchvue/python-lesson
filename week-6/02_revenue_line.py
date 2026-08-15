import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
revenue = [12000, 15000, 14000, 18000, 21000]

plt.plot(months, revenue, marker="o")
plt.title("Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.savefig("revenue_trend.png")

print("revenue_trend.png created.")

import matplotlib.pyplot as plt

categories = ["Rent", "Salary", "Office", "Travel"]
amounts = [12000, 45000, 2500, 8000]

plt.bar(categories, amounts)
plt.title("Monthly Expenses")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.savefig("monthly_expenses.png")

print("monthly_expenses.png created.")

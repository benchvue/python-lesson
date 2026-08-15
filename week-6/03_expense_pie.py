import matplotlib.pyplot as plt

labels = ["Rent", "Salary", "Office", "Travel"]
amounts = [12000, 45000, 2500, 8000]

plt.pie(amounts, labels=labels, autopct="%1.1f%%")
plt.title("Expense Breakdown")
plt.savefig("expense_pie.png")

print("expense_pie.png created.")
plt.show()

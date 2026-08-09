# Sometimes YOU want to signal an error on purpose with raise.

def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount

try:
    new_balance = withdraw(100, 250)
    print("New balance:", new_balance)
except ValueError as error:
    print("Denied:", error)

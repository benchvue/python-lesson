def add_tax(price, rate):
    return price + price * rate

total = add_tax(100, 0.1)
print("Total with tax:", total)

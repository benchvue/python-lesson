def calculate_sales_tax(amount, tax_rate):
    return amount * tax_rate

invoice_amount = 1000
tax_rate = 0.06

tax = calculate_sales_tax(invoice_amount, tax_rate)
total = invoice_amount + tax

print("Invoice amount:", invoice_amount)
print("Sales tax:", tax)
print("Total:", total)

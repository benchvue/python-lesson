# 09 fprint · PY
# 09_fprint.py
# f-strings can FORMAT numbers as they print them --
# something a plain print() cannot do on its own.
#
# Format mini-language used below (inside the {value:...} part):
#   ,      -> group thousands with commas     1300   -> 1,300
#   .2f    -> fixed-point, 2 decimals (cents)  1300   -> 1300.00
#   ,.2f   -> both together                    1300   -> 1,300.00
#   <10 / >10 -> left / right align in width 10 (line things up)
 
revenue = 2500
expenses = 1200
profit = revenue - expenses
 
# --- 1) Plain print(): you only get the raw number ---
print("Plain print()")
print("Revenue:", revenue)      # Revenue: 2500
print("Expenses:", expenses)    # Expenses: 1200
print("Profit:", profit)        # Profit: 1300
 
print()  # blank line
 
# --- 2) f-strings: add thousands "," and cents ".2f" ---
print("Formatted with f-strings")
print(f"Revenue:  ${revenue:,.2f}")     # Revenue:  $2,500.00
print(f"Expenses: ${expenses:,.2f}")    # Expenses: $1,200.00
print(f"Profit:   ${profit:,.2f}")      # Profit:   $1,300.00
 
print()
 
 
# Expected output:
# Plain print()
# Revenue: 2500
# Expenses: 1200
# Profit: 1300
#
# Formatted with f-strings
# Revenue:  $2,500.00
# Expenses: $1,200.00
# Profit:   $1,300.00 
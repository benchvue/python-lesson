# Different problems raise different errors.
# You can catch each kind separately and give a helpful message.

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Both values must be numbers"

print(safe_divide(10, 2))     # 5.0
print(safe_divide(10, 0))     # Cannot divide by zero
print(safe_divide(10, "x"))   # Both values must be numbers

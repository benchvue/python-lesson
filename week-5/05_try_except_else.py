# else runs only when NO error happened in the try block.
# Great for the "everything worked" follow-up step.

amounts = ["1200", "not-a-number", "300"]

for value in amounts:
    try:
        amount = int(value)
    except ValueError:
        print(value, "-> skipped (not a number)")
    else:
        print(value, "-> added", amount)

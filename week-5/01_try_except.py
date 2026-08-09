# A crash stops the whole program. try/except catches the error
# so the program can keep running.

price = "abc"   # oops - not a number

try:
    number = int(price)          # this line raises ValueError
    print("Number:", number)
except ValueError:
    print("That wasn't a valid number.")

print("Program keeps running.")

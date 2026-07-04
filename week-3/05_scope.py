company = "Acme"          # global - visible everywhere

def show():
    note = "internal"     # local - only inside this function
    print(company, note)  # can read global + local

show()
print(company)            # works - company is global
# print(note)             # NameError - note is local to show()

from datetime import datetime

today = datetime.today()

print("Today:", today.strftime("%Y-%m-%d"))
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)

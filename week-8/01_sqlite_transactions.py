import sqlite3

connection = sqlite3.connect("accounting.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY,
    account TEXT,
    amount REAL
)
""")

cursor.execute("DELETE FROM transactions")

records = [
    ("Revenue", 5000),
    ("Revenue", 3200),
    ("Rent Expense", -1200),
    ("Office Expense", -300)
]

cursor.executemany(
    "INSERT INTO transactions (account, amount) VALUES (?, ?)",
    records
)

cursor.execute("""
SELECT account, SUM(amount)
FROM transactions
GROUP BY account
""")

for row in cursor.fetchall():
    print(row)

connection.commit()
connection.close()

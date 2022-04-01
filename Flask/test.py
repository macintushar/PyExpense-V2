import sqlite3 as sql

conn = sql.connect(r'./Expenses.db')
cursor = conn.cursor()

newLimit = 1000

cursor.execute("UPDATE Other SET Exp_Limit = (?)", (newLimit,))
conn.commit()
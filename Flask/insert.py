import sqlite3 as sql

con = sql.connect('Expenses.db')
cur = con.cursor()

cur.execute("INSERT INTO Transactions(Amount, Description, Method, Category) VALUES (100, 'Food', 'GPay', 'Travel')")

con.commit()
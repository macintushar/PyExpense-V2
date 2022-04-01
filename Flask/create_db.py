import sqlite3 as sql

#connect to SQLite
con = sql.connect('Expenses.db')

#Create a Connection
cur = con.cursor()

#Drop users table if already exsist.
cur.execute("DROP TABLE IF EXISTS Transactions")

cur.execute("CREATE TABLE Transactions (Trxn_ID INTEGER PRIMARY KEY AUTOINCREMENT, Timestamp DATE DEFAULT (datetime('now','localtime')), Amount INT, Description TEXT, Method TEXT)")

cur.execute("DROP TABLE IF EXISTS Other")
cur.execute("CREATE TABLE Other (Exp_Limit INT)")
cur.execute("INSERT INTO Other VALUES (1)")
#commit changes
con.commit()

#close the connection
con.close()
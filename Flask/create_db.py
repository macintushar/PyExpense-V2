import sqlite3 as sql

con = sql.connect('Expenses.db')
cur = con.cursor()


cur.execute("DROP TABLE IF EXISTS Categories")
cur.execute("CREATE TABLE Categories (Category_ID INTEGER, Category TEXT)")
cur.execute("INSERT INTO Categories VALUES (1, 'None')")

cur.execute("DROP TABLE IF EXISTS Transactions")
cur.execute("CREATE TABLE Transactions (Trxn_ID INTEGER PRIMARY KEY AUTOINCREMENT, Timestamp DATE DEFAULT (datetime('now','localtime')), Amount INT, Description TEXT, Method TEXT, Category TEXT, FOREIGN KEY(Category) REFERENCES Categories(Category))")

cur.execute("DROP TABLE IF EXISTS Other")
cur.execute("CREATE TABLE Other (Exp_Limit INT)")
cur.execute("INSERT INTO Other VALUES (1)")
#commit changes
con.commit()

#close the connection
con.close()
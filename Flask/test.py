import sqlite3 as sql

conn = sql.connect(r'./Expenses.db')
cur = cursor = conn.cursor()

newCategory = ["Apps"]

cur.execute("SELECT COUNT(Category_ID) FROM Categories")
count = cur.fetchone()

cid = []
num = count[0]+1

cid.append(num)

print(cid[0], newCategory[0])

cur.execute('INSERT INTO Categories(Category_ID, Category) VALUES (?,?)',(cid[0],newCategory[0],))
conn.commit()

categories = []
for category in cursor.execute('SELECT Category FROM Categories'):
    categories.append(category[0])

print(categories)
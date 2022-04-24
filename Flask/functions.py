import sqlite3 as sql
import matplotlib.pyplot as plt
import numpy as np

def generatePie():
    conn = sql.connect(r'./Expenses.db')
    cursor = conn.cursor()
    
    amounts=[]
    for price in cursor.execute('SELECT Amount FROM Transactions'):
        amounts.append(int(price[0]))

    labels=[]
    for name in cursor.execute('SELECT Description FROM Transactions'):
        labels.append(str(name[0]))

    amounts = list(amounts)

    if (len(amounts)>=1 or len(labels)>=1):
        y = np.array(amounts)
        x = np.array(labels)

        plt.pie(y, labels=labels, autopct='%.0f%%')
        plt.savefig("./static/images/pie.png")
    
    elif(len(amounts)==0 or len(name)==0):
        return("Chart unable to generate")

def generateBar():
    conn = sql.connect(r'./Expenses.db')
    cursor = conn.cursor()
    
    amounts=[]
    for price in cursor.execute('SELECT Amount FROM Transactions'):
        amounts.append(int(price[0]))

    labels=[]
    for name in cursor.execute('SELECT Description FROM Transactions'):
        labels.append(str(name[0]))

    if (len(amounts)>=1 or len(labels)>=1):
        y = np.array(amounts)
        x = np.array(labels)

        plt.bar(x,y)
        plt.savefig("./static/images/bar.png")
        
    elif(len(amounts)==0 or len(name)==0):
        return("Chart unable to generate")


def Add_Limit(limit):
    conn = sql.connect(r'./Expenses.db')
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS Other(Limit INTEGER)")
    conn.commit()

    cursor.execute("INSERT INTO Other VALUES (?)", (limit))
    conn.commit()

def Edit_Limit(newLimit):
    conn = sql.connect(r'./Expenses.db')
    cursor = conn.cursor()

    cursor.execute("UPDATE Other SET Exp_Limit = (?)", (newLimit,))
    conn.commit()

def CurrentLimit():
    conn = sql.connect(r'./Expenses.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Other")
    lim = cursor.fetchone()
    lim = list(lim)

    return lim[0]

def viewCategories():
    conn = sql.connect(r'./Expenses.db')
    cursor = conn.cursor()
    
    categories = []
    for category in cursor.execute('SELECT Category FROM Categories'):
        categories.append(int(category[0]))
    
    return(categories)

def addCategories(newCategory):
    conn = sql.connect(r'./Expenses.db')
    cursor = conn.cursor()
    
    cur.execute("SELECT COUNT(Category_ID) FROM Categories")
    count = cur.fetchone()

    cid = []
    num = count[0]+1

    cid.append(num)

    cur.execute('INSERT INTO Categories(Category_ID, Category) VALUES (?,?)',(cid[0],newCategory[0],))



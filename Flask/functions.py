import sqlite3 as sql
import matplotlib.pyplot as plt
import numpy as np

def View_Chart():
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
        plt.savefig("./static/images/pie.jpg")
    
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

def Limit_Checker(price):
    print()
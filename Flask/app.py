from flask import Flask,render_template,request,redirect,url_for,flash
import sqlite3 as sql
from functions import View_Chart, CurrentLimit, Edit_Limit

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    con=sql.connect("Expenses.db")
    con.row_factory=sql.Row
    cur=con.cursor()

    cur.execute("SELECT * FROM Transactions")
    data=cur.fetchall()
    
    cur.execute('SELECT SUM(Amount) FROM Transactions')
    price = list(cur.fetchone())

    limit = CurrentLimit()
    limit += 0

    if price[0]>limit:
        color="danger"
        txt="Warning! Limit crossed."
    
    elif price[0]<limit:
        color="success" 
        lim=limit
        txt = "Expenditure under the Limit"

    return render_template("index.html",datas=data, total=price, color=color, text=txt, limit=limit) 
   

@app.route("/add",methods=['POST','GET'])
def add():
    if request.method=='POST':
        amount = request.form['amount']
        desc = request.form['desc']
        method = request.form['method']

        con=sql.connect("Expenses.db")
        cur=con.cursor()

        cur.execute("INSERT INTO Transactions(Amount,Description,Method) VALUES (?,?,?)",(amount,desc,method))
        con.commit()
        flash('Expense Added','success')
        return redirect(url_for("index"))
    return render_template("add.html")

@app.route("/edit/<string:uid>",methods=['POST','GET'])
def edit(uid):
    if request.method=='POST':
        amount = request.form['amount']
        desc = request.form['desc']
        method = request.form['method']

        con=sql.connect("Expenses.db")
        cur=con.cursor()

        cur.execute("UPDATE Transactions SET Amount=?, Description=?, Method=? WHERE Trxn_ID=?",(amount,desc,method,uid))
        con.commit()

        flash('Expense Updated','success')
        return redirect(url_for("index"))
    
    con=sql.connect("Expenses.db")
    con.row_factory=sql.Row
    cur=con.cursor()

    cur.execute("SELECT * FROM Transactions WHERE Trxn_ID=?",(uid))
    data=cur.fetchone()

    return render_template("edit.html",datas=data)
    
@app.route("/delete/<string:uid>",methods=['GET'])
def delete(uid):
    con=sql.connect("Expenses.db")
    cur=con.cursor()
    cur.execute("DELETE FROM Transactions where Trxn_ID=?",(uid,))
    con.commit()
    flash('Expense Deleted','warning')
    return redirect(url_for("index"))


@app.route("/charts")
def charts():
    View_Chart()
    return render_template('chart.html')


@app.route("/limit",methods=['POST','GET'])
def limit():
    con=sql.connect("Expenses.db")
    cur=con.cursor()
    if request.method=='POST':
        limit = request.form['limit']
        Edit_Limit(newLimit=limit)
        flash('Limit Changed','success')
        return redirect(url_for("index"))
    
    cur.execute("SELECT Exp_Limit FROM Other")
    data=cur.fetchone()

    return render_template("limit.html", datas=data)

if __name__=='__main__':
    app.secret_key='admin123'
    app.run(debug=True)
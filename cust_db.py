import sqlite3

def creat_db():
    con = sqlite3.connect(database=r'rms.db')
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS customer(cid INTEGER PRIMARY KEY AUTOINCREMENT,date text,name text,gender text,device text,contact text,email text,aadhar text,problem text,charges text,advance text,address text,days_to_repair text)')
    con.commit()
    #date,cid,contact,aadhar,balance,status
    cur.execute('CREATE TABLE IF NOT EXISTS repair(cid INTEGER,date text,contact text,aadhar text,fault text,balance text,status text,clearbalanced text,setwithdraw text,clearbalancedwithdraw text)')
    con.commit()
    

creat_db()
    
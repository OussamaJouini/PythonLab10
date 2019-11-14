import sqlite3
import base64
import browser

def dbtest():
    conn = sqlite3.connect("week10.db")
    cur = conn.cursor()
    cur.execute("select* from lab10")
    data = cur.fetchone()
    print (data)

dbtest()

 
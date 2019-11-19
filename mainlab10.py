import sqlite3
import base64
import webbrowser
def displayWeb(y):
    con = sqlite3.connect("week10.db")
    cur = con.cursor()
    cur.execute("select link from Lab10 where id ="+ y)
    data=cur.fetchone()
    webbrowser.open(base64.b64decode(data[0]))
    city = input("Kindly Enter the name of the associated City:")
    country = input("Kindly Enter the name of the associated Country:")
    values = (city, country,y)
    cur.execute('update Lab10 set city =?, country =? where id =?',values)
    con.commit()

run=True
while run == True:
    y = input("Kindly Enter a number between 1 and 24 or q to quit:")
    if y == "q":
        run = False
    elif (1 <= int(y) <= 24):
        displayWeb(y)
    else: print('The number you entered is invalid, please make sure to enter a number between 1 and 24 !!')




 

id = int(input("Enter IDNO : "))
na = input("Enter Name : ")
avg = float(input("Enter Average : "))

import sqlite3 as sql
conn = sql.connect("sathya.db")
curs = conn.cursor()
try:
    curs.execute("insert into Student values (?,?,?)",(id,na,avg))
    conn.commit()
    print("Student ",id," inserted")
except sql.IntegrityError:
    print("Student ", id, " Available")
finally:
    curs.close()
    conn.close()
    print("Thanks")



import sqlite3 as sql
conn = sql.connect("sathya.db")
curs = conn.cursor()
idno = int(input("Enter IDNO : "))
curs.execute("select * from student where idno = ?",(idno,))
res = curs.fetchone()
if res == None:
    print("Invalid IDNO")
else:
    print(res)

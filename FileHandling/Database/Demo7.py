
import sqlite3 as sql
conn = sql.connect("sathya.db")
curs = conn.cursor()
curs.execute("select * from student")
res = curs.fetchall()

for x in res:
    print(x[0],x[1],x[2])
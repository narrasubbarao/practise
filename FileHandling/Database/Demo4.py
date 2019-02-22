
import sqlite3 as sql
conn = sql.connect("sathya.db")
curs = conn.cursor()
curs.execute("create table if not exists Student(idno number primary key,name text,average real )")
print("Table Created")
curs.close()
conn.close()
print("Thanks")
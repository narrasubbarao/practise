
import sqlite3 as sql
conn = sql.connect("sathya.db")
curs = conn.cursor()
try:
    curs.execute("insert into student values(102,'kumar',98.35) ")
    conn.commit()
    print("Data Inserted")
except sql.IntegrityError:
    print("Idno is Available")
finally:
    curs.close()
    conn.close()
    print("Thanks")


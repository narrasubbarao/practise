
import sqlite3 as sql
conn = sql.connect("sathya.db")
curs = conn.cursor()
idno = int(input("Enter IDNO : "))
curs.execute("delete from student where idno = ?",(idno,))
conn.commit()
print(idno," Student is deleted")
print("Thanks")


# Example Program to Create a Table
# Table Name Student
# Cols : ID, Name, average

import sqlite3 as sql
con = sql.connect("sathya.db")
curs = con.cursor()
curs.execute("create table if not exists "
             "student(id number,name text,average real)")
print("Table Created")
curs.close()
con.close()
print("Thanks")
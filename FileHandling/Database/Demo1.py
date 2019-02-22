
# Example Program to Make a Connection

import sqlite3 as sql

connection = sql.connect("sathya.db")

print(connection)

print(type(connection))


# <sqlite3.Connection object at .....>
# <class 'sqlite3.Connection'>
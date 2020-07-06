import sqlite3
con=sqlite3.connect("s.db")
print("connected with oracle")
cur=con.cursor()
print("cursor crea")
cur.execute("select * from course")
row=cur.fetchall()
print(row[0][1])


import sqlite3
#Create new database
conn=sqlite3.connect('Student.db')
#Create cursor to execute queries
cur=conn.cursor()
cur.execute('CREATE TABLE Students_Record(Roll_No INTEGER, Student_Name TEXT, Age INTEGER);')
print("Table created")
print("Database created")
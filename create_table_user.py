import sqlite3
conn=sqlite3.connect('Todo.db')
conn.execute('CREATE TABLE user(id INTEGER PRIMARY KEY, username TEXT, password TEXT, confirmpassword TEXT, email TEXT)')
print("TABLE CREATED!")
conn.close()













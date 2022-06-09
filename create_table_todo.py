import sqlite3
conn=sqlite3.connect('Todo.db')
conn.execute("CREATE TABLE todo(id INTEGER PRIMARY KEY, task_name TEXT, priority TEXT, status TEXT)")
print("created db successfully!")
conn.close()














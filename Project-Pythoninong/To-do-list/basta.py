import sqlite3
conn = sqlite3.connect("todo_list.db")
cursor = conn.cursor()



with open("todo_list.sql", "r") as f:
    contents = f.read()

cursor.execute(contents)
cursor.execute(
    "INSERT INTO todo_list (task, done, created_at, deadline) VALUES (?, ?, ?, ?)", 
    ('buy milk', 0, '07/30/26', '08/05/26'))
conn.commit()
import sqlite3
conn = sqlite3.connect("notes_app.db")
cursor = conn.cursor()
with open("notes_app.sql", "r") as f:
    contents = f.read()

conn.commit()

temp = True

while temp:
    print("**********************")
    print("1. Add a note:")
    print("2. Update a note:")
    print("3. Remove a note:")
    print("4. Show all the notes:")
    print("**********************")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        title = input("Enter the title:")
        body = input("Enter the body:")
        created = input("Date created:")
        update = input("Date updated")
        cursor.execute(contents)
        cursor.execute("INSERT INTO notes_app(title, body, created_at, updated_at) VALUES (?, ?, ?, ?)", (title, body, created, update))
        conn.commit()




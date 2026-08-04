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
    print("5. Exit")
    print("**********************")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        title = input("Enter the title:")
        body = input("Enter the body:")
        created = input("Date created:")
        update = input("Date updated:")
        cursor.execute(contents)
        cursor.execute("INSERT INTO notes_app(title, body, created_at, updated_at) VALUES (?, ?, ?, ?)", (title, body, created, update))
        conn.commit()
    elif choice == 2:
        user_id = input('Enter the id you want to change:')
        user_temp = input('Type 1 to change the title, Type 2 for the body:')
        if user_temp == '1':
            temp_x = input("Enter the new title: ")
            cursor.execute("UPDATE notes_app SET title = ? WHERE id = ?", (temp_x, user_id))
            conn.commit()
        elif user_temp == '2':
            temp_y = input("Enter the new body: ")
            cursor.execute("UPDATE notes_app SET body = ? WHERE id = ?", (temp_y, user_id))
            conn.commit()
    elif choice == 3:
        user_delete = input("Enter the ID of the note you want to remove:")
        cursor.execute("DELETE FROM notes_app WHERE id = ?", (user_delete,))
        conn.commit()
    elif choice == 4:
        cursor.execute("SELECT * FROM notes_app")
        rows =cursor.fetchall()
        conn.commit()
        for row in rows:
            print("ID", row[0], "|Title:", row[1], "|Content:", row[2], "|Date created:", row[3], "|Updated:", row[4])
        temp1 = input("Press Enter to Proceed")    
    elif choice == 5:
        print("tank you")
        temp = False



import sqlite3
conn = sqlite3.connect("todo_list.db")
cursor = conn.cursor()
with open("todo_list.sql", "r") as f:
    contents = f.read()

conn.commit()

temp = True
while temp:
    print('MENU SYSTEM')
    print('1. Add a new task')
    print('2. View all task')
    print('3. Update task')
    print('4. Remove a task')
    print('5. Quit')
    choice = input('Enter your choice: ')
    if choice == '1':
        task = input('To do:')
        if_done = int(input('input num 1 if done 0 if not done: '))
        created_at = input('date created: ')
        deadline =  input('deadline: ')
        cursor.execute(contents)
        cursor.execute("INSERT INTO todo_list(task, done, created_at, deadline) VALUES (?, ?, ?, ?)", (task, if_done, created_at, deadline))
        conn.commit()
    elif choice == '2':
        cursor.execute("SELECT * FROM todo_list")
        rows = cursor.fetchall()
        for row in rows:
            print('ID:', row[0], '| Task:', row[1], '| Done:', row[2], '| Created:', row[3], '| Dealine:', row[4])
    elif choice == '3':
        user_temp = int(input('Enter the ID you want to update: '))
        change = int(input('Input 1(done) 0(not done): '))
        cursor.execute("UPDATE todo_list SET done = ? WHERE id = ?", (change, user_temp))
        conn.commit()
    elif choice == '4':
        user_temp1 = input('Enter the IDS of the task to remove: ')
        temp1 = [int(item.strip()) for item in user_temp1.split(',')]
        for item in temp1:
            cursor.execute("DELETE FROM todo_list WHERE id = ?", (item,))

        conn.commit()
    elif choice == '5':
        temp = False
        print('tank you.')
    else:
        print('Invalid Input.')

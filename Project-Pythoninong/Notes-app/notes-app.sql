CREATE TABLE IF NOT EXISTS notes_app(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    body TEXT NOT NULL,
    created_at TEXT NOT NULL,
    updated_at TEXT NULL
)

"""
1. add notes
contains:
id auto_increment, enter title, when it was created, paragraph, done, save

2. update notes
contains:
enter the ID, enter 1 if its the title to change enter 2 if its paragraph, save

3. remove a note
enter the ID to remove

4. show all notes

"""
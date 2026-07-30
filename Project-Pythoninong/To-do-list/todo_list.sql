CREATE TABLE IF NOT EXISTS todo_list(
    id INTEGER PRIMARY KEY,
    task TEXT NOT NULL,
    done INTEGER,
    created_at DATE,
    deadline DATE NULL
)

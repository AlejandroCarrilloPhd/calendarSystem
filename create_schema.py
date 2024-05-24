import sqlite3

# Connect to a SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('tasks.db')

# Create a cursor object
cur = conn.cursor()

# Create a table for tasks
cur.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        priority TEXT,
        deadline TEXT,
        duration INTEGER,
        project TEXT,
        completed BOOLEAN NOT NULL CHECK (completed IN (0, 1))
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database schema created successfully.")

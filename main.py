import sqlite3

def main():
    print("Welcome to the Task Scheduling System")

    # Connect to the SQLite database
    conn = sqlite3.connect('tasks.db')
    cur = conn.cursor()

    # Example query to fetch tasks
    cur.execute('SELECT * FROM tasks')
    tasks = cur.fetchall()

    # Display the tasks
    for task in tasks:
        print(task)

    # Close the connection
    conn.close()

if __name__ == "__main__":
    main()

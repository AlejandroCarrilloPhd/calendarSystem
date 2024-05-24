# main.py

import sqlite3

def add_task(title, description, priority, deadline, duration, project):
    conn = sqlite3.connect('tasks.db')
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO tasks (title, description, priority, deadline, duration, project, completed)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (title, description, priority, deadline, duration, project, False))
    conn.commit()
    conn.close()

def view_tasks():
    conn = sqlite3.connect('tasks.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM tasks')
    tasks = cur.fetchall()
    conn.close()
    return tasks

def main():
    print("Welcome to the Task Scheduling System")

    # Example: Adding a new task
    add_task("Task 1", "Description for Task 1", "High", "2024-06-01", 2, "Project 1")

    # Example: Viewing all tasks
    tasks = view_tasks()
    for task in tasks:
        print(task)

if __name__ == "__main__":
    main()

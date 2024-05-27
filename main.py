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

def update_task(task_id, title, description, priority, deadline, duration, project, completed):
    conn = sqlite3.connect('tasks.db')
    cur = conn.cursor()
    cur.execute('''
        UPDATE tasks
        SET title = ?, description = ?, priority = ?, deadline = ?, duration = ?, project = ?, completed = ?
        WHERE id = ?
    ''', (title, description, priority, deadline, duration, project, completed, task_id))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = sqlite3.connect('tasks.db')
    cur = conn.cursor()
    cur.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()


def main():
    print("Welcome to the Task Scheduling System")
    while True:
        # Display the menu options
        print("\nMenu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")  # Get user input

        if choice == '1':
            # Add a new task
            title = input("Title: ")
            description = input("Description: ")
            priority = input("Priority: ")
            deadline = input("Deadline: ")
            duration = int(input("Duration (hours): "))
            project = input("Project: ")
            add_task(title, description, priority, deadline, duration, project)
        elif choice == '2':
            # View all tasks
            tasks = view_tasks()
            for task in tasks:
                print(task)
        elif choice == '3':
            # Update an existing task
            task_id = int(input("Task ID: "))
            title = input("Title: ")
            description = input("Description: ")
            priority = input("Priority: ")
            deadline = input("Deadline: ")
            duration = int(input("Duration (hours): "))
            project = input("Project: ")
            completed = input("Completed (0 or 1): ")
            update_task(task_id, title, description, priority, deadline, duration, project, bool(int(completed)))
        elif choice == '4':
            # Delete a task
            task_id = int(input("Task ID: "))
            delete_task(task_id)
        elif choice == '5':
            # Exit the program
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
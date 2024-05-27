import tkinter as tk  # Import the tkinter library for GUI
from tkinter import messagebox  # Import messagebox for displaying messages
import sqlite3  # Import the SQLite library

# Function to add a task to the database
def add_task(title, description, priority, deadline, duration, project):
    conn = sqlite3.connect('tasks.db')  # Connect to the SQLite database
    cur = conn.cursor()  # Create a cursor object
    # Execute the insert query
    cur.execute('''
        INSERT INTO tasks (title, description, priority, deadline, duration, project, completed)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (title, description, priority, deadline, duration, project, False))
    conn.commit()  # Commit the changes
    conn.close()  # Close the connection

# Function to view all tasks from the database
def view_tasks():
    conn = sqlite3.connect('tasks.db')  # Connect to the SQLite database
    cur = conn.cursor()  # Create a cursor object
    # Execute the select query
    cur.execute('SELECT * FROM tasks')
    tasks = cur.fetchall()  # Fetch all results
    conn.close()  # Close the connection
    return tasks

# Function to display tasks in the console (for testing purposes)
def show_tasks():
    tasks = view_tasks()
    for task in tasks:
        print(task)

# Function to create a new task using the GUI
def add_task_gui():
    def submit():
        title = title_entry.get()
        description = desc_entry.get()
        priority = priority_entry.get()
        deadline = deadline_entry.get()
        duration = int(duration_entry.get())
        project = project_entry.get()
        add_task(title, description, priority, deadline, duration, project)
        messagebox.showinfo("Success", "Task added successfully")  # Show success message
        add_task_window.destroy()  # Close the add task window

    add_task_window = tk.Toplevel(root)  # Create a new window for adding a task
    add_task_window.title("Add Task")

    # Create and place labels and entry fields for task details
    tk.Label(add_task_window, text="Title").grid(row=0, column=0)
    title_entry = tk.Entry(add_task_window)
    title_entry.grid(row=0, column=1)

    tk.Label(add_task_window, text="Description").grid(row=1, column=0)
    desc_entry = tk.Entry(add_task_window)
    desc_entry.grid(row=1, column=1)

    tk.Label(add_task_window, text="Priority").grid(row=2, column=0)
    priority_entry = tk.Entry(add_task_window)
    priority_entry.grid(row=2, column=1)

    tk.Label(add_task_window, text="Deadline").grid(row=3, column=0)
    deadline_entry = tk.Entry(add_task_window)
    deadline_entry.grid(row=3, column=1)

    tk.Label(add_task_window, text="Duration (hours)").grid(row=4, column=0)
    duration_entry = tk.Entry(add_task_window)
    duration_entry.grid(row=4, column=1)

    tk.Label(add_task_window, text="Project").grid(row=5, column=0)
    project_entry = tk.Entry(add_task_window)
    project_entry.grid(row=5, column=1)

    tk.Button(add_task_window, text="Submit", command=submit).grid(row=6, columnspan=2)  # Submit button

root = tk.Tk()  # Create the main application window
root.title("Task Scheduling System")

# Create and place buttons for adding and viewing tasks
tk.Button(root, text="Add Task", command=add_task_gui).pack()
tk.Button(root, text="View Tasks", command=show_tasks).pack()

root.mainloop()  # Start the Tkinter event loop

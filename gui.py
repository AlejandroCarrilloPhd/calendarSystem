import tkinter as tk
from tkinter import messagebox, ttk  # Import ttk for Treeview
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

def add_task_gui():
    def submit():
        title = title_entry.get()
        description = desc_entry.get()
        priority = priority_entry.get()
        deadline = deadline_entry.get()
        duration = int(duration_entry.get())
        project = project_entry.get()
        add_task(title, description, priority, deadline, duration, project)
        messagebox.showinfo("Success", "Task added successfully")
        add_task_window.destroy()

    add_task_window = tk.Toplevel(root)
    add_task_window.title("Add Task")

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

    tk.Button(add_task_window, text="Submit", command=submit).grid(row=6, columnspan=2)

# Function to display tasks in the GUI
def view_tasks_gui():
    view_tasks_window = tk.Toplevel(root)
    view_tasks_window.title("View Tasks")

    # Create a Treeview widget to display tasks
    tree = ttk.Treeview(view_tasks_window, columns=('ID', 'Title', 'Description', 'Priority', 'Deadline', 'Duration', 'Project', 'Completed'), show='headings')
    tree.heading('ID', text='ID')
    tree.heading('Title', text='Title')
    tree.heading('Description', text='Description')
    tree.heading('Priority', text='Priority')
    tree.heading('Deadline', text='Deadline')
    tree.heading('Duration', text='Duration')
    tree.heading('Project', text='Project')
    tree.heading('Completed', text='Completed')

    tasks = view_tasks()
    for task in tasks:
        tree.insert('', tk.END, values=task)

    tree.pack(expand=True, fill=tk.BOTH)

# Function to update a task in the database
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

# Function to delete a task from the database
def delete_task(task_id):
    conn = sqlite3.connect('tasks.db')
    cur = conn.cursor()
    cur.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()

# Function to create the task update GUI
def update_task_gui():
    def submit():
        task_id = int(task_id_entry.get())
        title = title_entry.get()
        description = desc_entry.get()
        priority = priority_entry.get()
        deadline = deadline_entry.get()
        duration = int(duration_entry.get())
        project = project_entry.get()
        completed = bool(int(completed_entry.get()))
        update_task(task_id, title, description, priority, deadline, duration, project, completed)
        messagebox.showinfo("Success", "Task updated successfully")
        update_task_window.destroy()

    update_task_window = tk.Toplevel(root)
    update_task_window.title("Update Task")

    tk.Label(update_task_window, text="Task ID").grid(row=0, column=0)
    task_id_entry = tk.Entry(update_task_window)
    task_id_entry.grid(row=0, column=1)

    tk.Label(update_task_window, text="Title").grid(row=1, column=0)
    title_entry = tk.Entry(update_task_window)
    title_entry.grid(row=1, column=1)

    tk.Label(update_task_window, text="Description").grid(row=2, column=0)
    desc_entry = tk.Entry(update_task_window)
    desc_entry.grid(row=2, column=1)

    tk.Label(update_task_window, text="Priority").grid(row=3, column=0)
    priority_entry = tk.Entry(update_task_window)
    priority_entry.grid(row=3, column=1)

    tk.Label(update_task_window, text="Deadline").grid(row=4, column=0)
    deadline_entry = tk.Entry(update_task_window)
    deadline_entry.grid(row=4, column=1)

    tk.Label(update_task_window, text="Duration (hours)").grid(row=5, column=0)
    duration_entry = tk.Entry(update_task_window)
    duration_entry.grid(row=5, column=1)

    tk.Label(update_task_window, text="Project").grid(row=6, column=0)
    project_entry = tk.Entry(update_task_window)
    project_entry.grid(row=6, column=1)

    tk.Label(update_task_window, text="Completed (0 or 1)").grid(row=7, column=0)
    completed_entry = tk.Entry(update_task_window)
    completed_entry.grid(row=7, column=1)

    tk.Button(update_task_window, text="Submit", command=submit).grid(row=8, columnspan=2)

# Function to create the task deletion GUI
def delete_task_gui():
    def submit():
        task_id = int(task_id_entry.get())
        delete_task(task_id)
        messagebox.showinfo("Success", "Task deleted successfully")
        delete_task_window.destroy()

    delete_task_window = tk.Toplevel(root)
    delete_task_window.title("Delete Task")

    tk.Label(delete_task_window, text="Task ID").grid(row=0, column=0)
    task_id_entry = tk.Entry(delete_task_window)
    task_id_entry.grid(row=0, column=1)

    tk.Button(delete_task_window, text="Submit", command=submit).grid(row=1, columnspan=2)

root = tk.Tk()
root.title("Task Scheduling System")

tk.Button(root, text="Add Task", command=add_task_gui).pack()
tk.Button(root, text="View Tasks", command=view_tasks_gui).pack()
tk.Button(root, text="Update Task", command=update_task_gui).pack()
tk.Button(root, text="Delete Task", command=delete_task_gui).pack()

root.mainloop()

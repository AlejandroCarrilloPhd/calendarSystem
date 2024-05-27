import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
from tkcalendar import Calendar
from main import schedule_tasks, WORK_HOURS, DAYS_OF_WEEK

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

# Importing the schedule_tasks function from main.py
from main import schedule_tasks

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

def view_tasks_gui():
    view_tasks_window = tk.Toplevel(root)
    view_tasks_window.title("View Tasks")

    tree = ttk.Treeview(view_tasks_window, columns=('ID', 'Title', 'Description', 'Priority', 'Deadline', 'Duration', 'Project', 'Completed'), show='headings')
    tree.heading('ID', text='ID')
    tree.heading('Title', text='Title')
    tree.heading('Description', text='Description')
    tree.heading('Priority', text='Priority')
    tree.heading('Deadline', text='Deadline')
    tree.heading('Duration', text='Duration')
    tree.heading('Project', text='Project')
    tree.heading('Completed', text='Completed')

    sorted_tasks = schedule_tasks()  # Use the scheduling algorithm to get sorted tasks
    for task in sorted_tasks:
        tree.insert('', tk.END, values=task)

    tree.pack(expand=True, fill=tk.BOTH)

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

def view_calendar_gui():
    def get_task_info(date):
        date_tasks = [task for task in sorted_tasks if task[4] == date]  # Filter tasks by selected date
        task_info = "\n".join([f"Title: {task[1]}, Priority: {task[3]}" for task in date_tasks])
        task_info_label.config(text=task_info if task_info else "No tasks for this date")

    sorted_tasks = schedule_tasks()  # Get sorted tasks

    view_calendar_window = tk.Toplevel(root)
    view_calendar_window.title("Task Calendar")

    cal = Calendar(view_calendar_window, selectmode='day')
    cal.pack(pady=20)

    task_info_label = tk.Label(view_calendar_window, text="", justify=tk.LEFT)
    task_info_label.pack(pady=10)

    view_button = tk.Button(view_calendar_window, text="View Tasks", command=lambda: get_task_info(cal.get_date()))
    view_button.pack(pady=10)

def view_hourly_calendar_gui():
    def get_task_info(hour):
        hour_tasks = [task[1] for task in scheduled_tasks if task[0] == hour]
        task_info = "\n".join([f"{task[1]}, Priority: {task[3]}, Duration: {task[5]} hrs" for task in hour_tasks])
        task_info_label.config(text=task_info if task_info else "No tasks for this hour")

    scheduled_tasks = schedule_tasks()  # Get scheduled tasks

    view_hourly_calendar_window = tk.Toplevel(root)
    view_hourly_calendar_window.title("Hourly Task Calendar")

    for hour in WORK_HOURS:
        hour_label = tk.Label(view_hourly_calendar_window, text=f"{hour}:00")
        hour_label.grid(row=hour - WORK_HOURS[0], column=0, padx=10, pady=5)

        task_info_label = tk.Label(view_hourly_calendar_window, text="", justify=tk.LEFT)
        task_info_label.grid(row=hour - WORK_HOURS[0], column=1, padx=10, pady=5)

        view_button = tk.Button(view_hourly_calendar_window, text="View Tasks", command=lambda h=hour: get_task_info(h))
        view_button.grid(row=hour - WORK_HOURS[0], column=2, padx=10, pady=5)

def view_weekly_hourly_calendar_gui():
    scheduled_tasks = schedule_tasks()  # Get scheduled tasks

    view_weekly_hourly_calendar_window = tk.Toplevel(root)
    view_weekly_hourly_calendar_window.title("Weekly Hourly Task Calendar")

    # Create headers for days of the week
    for col, day in enumerate(DAYS_OF_WEEK):
        day_label = tk.Label(view_weekly_hourly_calendar_window, text=day)
        day_label.grid(row=0, column=col + 1, padx=10, pady=5)

    # Create rows for each hour
    for row, hour in enumerate(WORK_HOURS):
        hour_label = tk.Label(view_weekly_hourly_calendar_window, text=f"{hour % 12 or 12} {'AM' if hour < 12 else 'PM'}")
        hour_label.grid(row=row + 1, column=0, padx=10, pady=5)

        for col, day in enumerate(DAYS_OF_WEEK):
            hour_tasks = [task[1] for task in scheduled_tasks[day] if task[0] == hour]
            task_info = "\n".join([f"{task[1]}, Priority: {task[3]}" for task in hour_tasks])
            task_info_label = tk.Label(view_weekly_hourly_calendar_window, text=task_info if task_info else "No tasks", justify=tk.LEFT)
            task_info_label.grid(row=row + 1, column=col + 1, padx=10, pady=5)

root = tk.Tk()
root.title("Task Scheduling System")

tk.Button(root, text="Add Task", command=add_task_gui).pack()
tk.Button(root, text="View Tasks", command=view_tasks_gui).pack()
tk.Button(root, text="Update Task", command=update_task_gui).pack()
tk.Button(root, text="Delete Task", command=delete_task_gui).pack()
tk.Button(root, text="View Calendar", command=view_calendar_gui).pack()
tk.Button(root, text="View Hourly Calendar", command=view_hourly_calendar_gui).pack()
tk.Button(root, text="View Weekly Hourly Calendar", command=view_weekly_hourly_calendar_gui).pack()


root.mainloop()

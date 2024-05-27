# Personal Task Scheduling System

## Project Overview
This project aims to build a personal task scheduling system that uses AI to optimize and manage tasks. The system is inspired by the Motion app but will be custom-built to suit personal needs and preferences. The goal is to create an intelligent task manager that dynamically schedules tasks and integrates with a built-in calendar interface.

## Objectives
- **Task Input and Scheduling:** Allow users to input tasks and create calendar events that adjust based on priority and new task entries.
- **Completion Tracking:** Enable task completion tracking to facilitate rescheduling and progress tracking.
- **Integrated Calendar System:** Develop a calendar system as part of the interface, without relying on external calendar systems.
- **Project Progress Dashboard:** Track the overall progress of different projects in a separate dashboard.
- **Scheduling Constraints:** Allow scheduling within defined working hours and manage scheduling up to 3 months ahead.
- **Advanced Features:** Plan for future enhancements such as color coding, integration with external calendars, and intuitive GUI features.

## Setup Instructions

### Prerequisites
- Python 3.x

### Initial Setup
1. **Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Create Database Schema:**
    ```bash
    python create_schema.py
    ```

4. **Run the Application:**
    ```bash
    python main.py
    ```

### GUI Instructions
1. **Run the GUI:**
    ```bash
    python gui.py
    ```

2. **Use the GUI:**
    - **Add Task:** Opens a form to add a new task.
    - **View Tasks:** Displays all tasks in a table.
    - **Update Task:** Opens a form to update an existing task.
    - **Delete Task:** Opens a form to delete a task by ID.

## Technical Details
- **Programming Languages and Libraries:**
  - Python will be the primary language.
  - Libraries: `pandas`, `sqlite3`, `tkinter`.
- **Data Storage:**
  - Utilize `sqlite3` for task and project data storage.
- **User Interface:**
  - Initially, a GUI using `tkinter`.

## Scheduling Algorithm
- **Criteria:** Priority of task, project priority, deadlines, task length, and difficulty.
- **Conflict Resolution:** Prioritize tasks and projects based on set criteria, ensuring deadlines are met. Allow user intervention for severe overlaps.


## Contributing
Contributions are currently not welcome, sorry!

## Contact
For any questions or suggestions, please reach out to alejandro.carrillo.phd@gmail.com.

---

*This project is a personal initiative to create a dynamic task scheduling system, leveraging skills in Python and AI, and aiming for continuous improvement and learning.*

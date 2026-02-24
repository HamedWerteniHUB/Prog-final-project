# Student’s Task Manager

**Author:** Hamed Werteni

Student’s Task Manager is a simple FastAPI backend to manage tasks, like a personal to-do list.  
You can create tasks, mark them as completed, update them, or delete them.  
All tasks are stored in `tasks.txt` using JSON Lines format, so they persist even after restarting the server.

## Example Tasks

Here are some example tasks you might have as a student:

- Studying German  
- Going to the gym  
- Homework for school  
- Grocery shopping  
- Reading a book  

> These example tasks are created by **Hamed Werteni**.

## Features

- Add new tasks with a title and optional description  
- Update existing tasks  
- Mark tasks as completed  
- Delete single tasks or all tasks  
- Filter tasks by completion status  
- View task statistics (total, completed, pending, completion percentage)  
- Auto-generated task IDs  
- Simple file-based persistence (no database required)  

## How to Run

1. Install dependencies:

```bash
pip install fastapi uvicorn
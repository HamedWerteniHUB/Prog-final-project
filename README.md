# Student’s Task Manager

**Author:** Hamed Werteni / AKA MEYO

Student’s Task Manager is a simple FastAPI backend for managing tasks, similar to a personal to-do list.
You can create tasks, update them, mark them as completed, or delete them.
All tasks are stored in a local file (`tasks.txt`) using JSON Lines format, so data persists after restarting the server.

---

## Example Tasks

- Studying German
- Going to the gym
- Homework for school
- Grocery shopping
- Reading a book

> Example tasks created by **Hamed Werteni**

---

## Features

- Create new tasks with a title and optional description
- Update tasks (title, description, and completion status)
- Mark tasks as completed or pending
- Delete individual tasks or all tasks
- Filter tasks by completion status
- View task statistics (total, completed, pending, completion percentage)
- Auto-generated task IDs
- Simple file-based persistence (no database required)
- Auto-generated API documentation (Swagger UI)

---

## How to Run

### 1. Install dependencies

Run the following command:

    pip install fastapi uvicorn

### 2. Start the server

Run:

    uvicorn main:app --reload

### 3. Open API documentation

After starting the server, open your browser and visit:

    http://127.0.0.1:8000/docs

---

## API Endpoints Overview

GET /  
GET /tasks  
GET /tasks?completed=true  
GET /tasks/{id}  
POST /tasks  
PUT /tasks/{id}  
DELETE /tasks/{id}  
DELETE /tasks  

---

## Notes

- This project uses file-based storage and is intended for learning purposes.
- It is not designed for concurrent or multi-user environments.


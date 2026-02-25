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

### Create new tasks
Create a task by sending a `POST /tasks` request with a title and an optional description.
Each task is automatically assigned a unique ID and starts with `completed = false`.

### Update tasks
Update an existing task using `PUT /tasks/{id}`.
You can modify the title, description, and completion status.
Partial updates are supported, so you only need to send the fields you want to change.

### Mark tasks as completed or pending
Tasks can be marked as completed or set back to pending by updating the `completed` field.
For example, sending `{ "completed": true }` marks a task as completed.

### Delete individual tasks or all tasks
Delete a single task using `DELETE /tasks/{id}`.
Delete all tasks at once using `DELETE /tasks`.

### Filter tasks by completion status
Tasks can be filtered by their completion state using a query parameter.
For example:
- `/tasks?completed=true` returns only completed tasks
- `/tasks?completed=false` returns only pending tasks

### View task statistics
Get an overview of your tasks using `GET /tasks/stats`.
This endpoint returns the total number of tasks, how many are completed, how many are pending, and the completion percentage.

### Auto-generated task IDs
Each new task receives an automatically generated numeric ID.
IDs are sequential and unique, even after restarting the server.

### Simple file-based persistence
Tasks are stored locally in a file (`tasks.txt`) using JSON Lines format.
This allows tasks to persist even when the server is stopped or restarted.

### Auto-generated API documentation
FastAPI automatically generates interactive API documentation using Swagger UI.
After starting the server, you can explore and test all endpoints at `/docs`.

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


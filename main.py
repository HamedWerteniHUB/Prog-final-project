"""
Student’s Task Manager - FastAPI Project
Author: Hamed Werteni
"""

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from task_controller import load_tasks, save_tasks, get_next_id

# -----------------------------
# FastAPI App Setup
# -----------------------------
app = FastAPI(
    title="Student’s Task Manager",
    docs_url="/docs",      # Swagger UI accessible
    redoc_url=None,        # ReDoc disabled
    openapi_url="/openapi.json"  # OpenAPI JSON available for Swagger
)

# -----------------------------
# Pydantic Models
# -----------------------------
class Task(BaseModel):
    id: int
    title: str
    description: str | None = None
    completed: bool = False


class TaskCreate(BaseModel):
    title: str
    description: str | None = None


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None

# -----------------------------
# Root Endpoint
# -----------------------------
@app.get("/")
def root():
    return {"message": "Student’s Task Manager is running — by Hamed Werteni"}

# -----------------------------
# Get All Tasks
# -----------------------------
@app.get("/tasks")
def get_all_tasks(completed: bool | None = Query(default=None)):
    tasks = load_tasks()
    if completed is None:
        return tasks
    return [task for task in tasks if task["completed"] == completed]

# -----------------------------
# Task Statistics
# -----------------------------
@app.get("/tasks/stats")
def get_stats():
    tasks = load_tasks()
    total = len(tasks)
    completed = sum(1 for t in tasks if t["completed"])
    pending = total - completed
    percentage = round((completed / total) * 100, 2) if total > 0 else 0
    return {
        "total": total,
        "completed": completed,
        "pending": pending,
        "completion_percentage": percentage,
        "signature": "Hamed Werteni"
    }

# -----------------------------
# Get Single Task
# -----------------------------
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(
        status_code=404,
        detail=f"Task {task_id} not found — by Hamed Werteni"
    )

# -----------------------------
# Create Task
# -----------------------------
@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    tasks = load_tasks()
    new_task = {
        "id": get_next_id(tasks),
        "title": task.title,
        "description": task.description,
        "completed": False
    }
    tasks.append(new_task)
    save_tasks(tasks)
    return new_task

# -----------------------------
# Update Task (Partial Update Supported)
# -----------------------------
@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: TaskUpdate):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:

            if updated_task.title is not None:
                task["title"] = updated_task.title

            if updated_task.description is not None:
                task["description"] = updated_task.description

            if updated_task.completed is not None:
                task["completed"] = updated_task.completed

            save_tasks(tasks)
            return task

    raise HTTPException(
        status_code=404,
        detail=f"Task {task_id} not found — by Hamed Werteni"
    )

# -----------------------------
# Delete Single Task
# -----------------------------
@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task["id"] != task_id]

    if len(new_tasks) == len(tasks):
        raise HTTPException(
            status_code=404,
            detail=f"Task {task_id} not found — by Hamed Werteni"
        )

    save_tasks(new_tasks)
    return

# -----------------------------
# Delete All Tasks
# -----------------------------
@app.delete("/tasks", status_code=204)
def delete_all_tasks():
    save_tasks([])
    return
"""
Task Controller Functions
Author: Hamed Werteni

This file handles all task operations: loading, saving,
and generating new task IDs. Used by Student's Task Manager.
"""

import json
import os

FILE_NAME = "tasks.txt"

# -----------------------------
# Load Tasks
# -----------------------------
def load_tasks():
    """
    Load tasks from tasks.txt and return as a list of dictionaries.
    If the file does not exist, return an empty list.
    """
    if not os.path.exists(FILE_NAME):
        return []

    tasks = []
    with open(FILE_NAME, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                tasks.append(json.loads(line))
    return tasks

# -----------------------------
# Save Tasks
# -----------------------------
def save_tasks(tasks):
    """
    Save the list of tasks back to tasks.txt.
    Overwrites the file with the current tasks.
    """
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(json.dumps(task) + "\n")

# -----------------------------
# Get Next ID
# -----------------------------
def get_next_id(tasks):
    """
    Generate the next sequential ID for a new task.
    If no tasks exist, start with ID 1.
    """
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1
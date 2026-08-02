from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

app = FastAPI()

class Task(BaseModel):
    id: Optional[int] = None
    title: str
    description: Optional[str] = None
    status: str = "pending"
    created_at: Optional[datetime] = None


tasks = []
task_id_counter = 1


@app.get("/")
def home():
    return {
        "message": "Task Manager API is running!"
    }


@app.post("/tasks")
def create_task(task: Task):
    global task_id_counter

    if task.title.strip() == "":
        raise HTTPException(
            status_code=400,
            detail="Title cannot be empty"
        )

    task.id = task_id_counter
    task.created_at = datetime.now()

    tasks.append(task)
    task_id_counter += 1

    return {
        "message": "Task created successfully",
        "task": task
    }


@app.get("/tasks")
def get_tasks():
    return tasks


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):

    for index, old_task in enumerate(tasks):
        if old_task.id == task_id:

            if task.title.strip() == "":
                raise HTTPException(
                    status_code=400,
                    detail="Title cannot be empty"
                )

            task.id = task_id
            task.created_at = old_task.created_at

            tasks[index] = task

            return {
                "message": "Task updated successfully",
                "task": task
            }

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):

    for index, task in enumerate(tasks):
        if task.id == task_id:

            deleted_task = tasks.pop(index)

            return {
                "message": "Task deleted successfully",
                "task": deleted_task
            }

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )

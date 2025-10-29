from fastapi import FastAPI, HTTPException
from app.application.services.task_service import TaskService
from app.adapters.persistence.memory_task_repository import MemoryTaskRepository

repo = MemoryTaskRepository()
service = TaskService(repo)
app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/tasks")
def get_tasks():
    return service.list_tasks()

@app.post("/tasks")
def create_task(task: dict):
    try:
        new_task = service.create_task(task["title"], task["status"])
        return new_task
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

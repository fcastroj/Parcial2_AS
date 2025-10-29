from app.application.ports.task_repository import TaskRepository
from app.domain.task import Task

class MemoryTaskRepository(TaskRepository):
    def __init__(self):
        self.tasks = []
        self.counter = 1

    def add(self, task: Task) -> Task:
        task.id = self.counter
        self.tasks.append(task)
        self.counter += 1
        return task

    def get_all(self):
        return self.tasks

from app.domain.task import Task

class TaskService:
    def __init__(self, repository):
        self.repository = repository

    def create_task(self, title: str, status: str):
        task = Task(id=0, title=title, status=status)
        return self.repository.add(task)

    def list_tasks(self):
        return self.repository.get_all()

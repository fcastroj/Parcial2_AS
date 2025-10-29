from abc import ABC, abstractmethod
from typing import List
from app.domain.task import Task

class TaskRepository(ABC):

    @abstractmethod
    def add(self, task: Task) -> Task:
        pass

    @abstractmethod
    def get_all(self) -> List[Task]:
        pass

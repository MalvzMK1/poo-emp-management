from typing import TypedDict
from typing_extensions import ReadOnly
from app.models import Task
from app.models.employee import Employee
from app.repositories.base_repository import BaseRepository
from app.utils.decorators import database_operation
from app.config import session

class UpdateTaskInput(TypedDict):
    name: ReadOnly[str]

class TaskRepository(BaseRepository[Task]):
    def __init__(self):
        super().__init__(Task)

    @database_operation(session)
    def create(self, data: Task) -> None:
        if data.is_done:
            raise Exception('Cannot create a done task')

        if data.owner_id is not None:
            owner = self._db.query(Employee).filter(Employee.id == data.owner_id).first()

            if owner is None:
                raise Exception('Task owner not found')
        
        self._db.add(data)
        self._db.commit()
        self._db.refresh(data)


    @database_operation(session)
    def update(self, id: int, data: UpdateTaskInput) -> Task:
        task = self._db.query(Task).filter(Task.id == id).first()

        if not task:
            raise Exception('Task not found')

        task.name = data['name']

        self._db.commit()
        self._db.refresh(task)

        return task

    @database_operation(session)
    def toggle_task_status(self, id: int) -> Task:
        task = self._db.query(Task).filter(Task.id == id).first()

        if not task:
            raise Exception('Task not found')

        task.is_done = not task.is_done

        self._db.commit()
        self._db.refresh(task)

        return task

    @database_operation(session)
    def change_owner(self, owner_id: int, task_id: int) -> Task:
        task = self._db.query(Task).filter(Task.id == task_id).first()

        if not task:
            raise Exception('Task not found')

        if task.is_done:
            raise Exception('Cannot change the owner of a done task')

        owner = self._db.query(Employee).filter(Employee.id == owner_id).first()

        if owner is None:
            raise Exception('Employee not found')

        task.owner_id = owner_id

        self._db.commit()
        self._db.refresh(task)

        return task


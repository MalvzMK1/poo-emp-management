from typing import TypedDict
from typing_extensions import ReadOnly
from app.models import Employee
from app.models.department import Department
from app.models.task import Task
from app.repositories.base_repository import BaseRepository
from app.utils.decorators import database_operation
from app.utils.enums import RolesEnum
from app.config import session

class UpdateEmployeeInput(TypedDict):
    name: ReadOnly[str]
    document: ReadOnly[str]
    role_id: ReadOnly[int]
    department_id: ReadOnly[int]

class EmployeeRepository(BaseRepository[Employee]):
    def __init__(self):
        super().__init__(Employee)

    @database_operation(session)
    def update(self, id: int, data: UpdateEmployeeInput) -> None:
        employee = self._db.query(Employee).filter(Employee.id == id).first()

        if not employee:
            raise Exception('Employee not found')

        employee.name = data['name']
        employee.document = data['document']
        employee.role_id = data['role_id']
        employee.department_id = data['department_id']

        self._db.commit()

    @database_operation(session)
    def update_managed_department(self, manager_id: int, department_id: int):
        manager = self._db.query(Employee).filter(Employee.id == manager_id).first()

        if manager is None:
            raise Exception('Manager not found')
        
        if manager.role_id is not RolesEnum.MANAGER:
            raise Exception('User is not a manager')

        department = self._db.query(Department).filter(Department.id == department_id).first()

        if department is None:
            raise Exception('Department not found')

        department.manager_id = manager_id
        manager.managed_department_id = department_id

        self._db.commit()

    @database_operation(session)
    def find_many_tasks(self, id: int) -> list[Task]:
        employee = self._db.query(Employee).filter(Employee.id == id).first()

        if employee is None:
            raise Exception('Employee not found')

        return self._db.query(Task).filter(Task.owner_id == employee.id).all()

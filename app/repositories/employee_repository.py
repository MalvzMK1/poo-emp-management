from typing import TypedDict
from typing_extensions import ReadOnly
from app.models import Employee, Department, Role
from app.repositories.base_repository import BaseRepository
from app.utils.decorators import database_operation
from app.utils.enums import RolesEnum
from app.config import session

class UpdateEmployeeInput(TypedDict):
    name: ReadOnly[str]
    document: ReadOnly[str]

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

        self._db.commit()

    @database_operation(session)
    def update_managed_department(self, manager_id: int, department_id: int | None):
        manager = self._db.query(Employee).filter(Employee.id == manager_id).first()

        if manager is None:
            raise Exception('Manager not found')

        if department_id is None:
            manager.managed_department_id = None
        else:
            if manager.role_id is not RolesEnum.MANAGER.value:
                raise Exception('User is not a manager')

            department = self._db.query(Department).filter(Department.id == department_id).first()

            if department is None:
                raise Exception('Department not found')

            department.manager_id = manager_id
            manager.managed_department_id = department_id

        self._db.commit()

    @database_operation(session)
    def update_role(self, employee_id: int, role_id: int) -> None:
        employee = self._db.query(Employee).filter(Employee.id == employee_id).first()

        if employee is None:
            raise Exception('Employee not found')

        role = self._db.query(Role).filter(Role.id == role_id).first()

        if role is None:
            raise Exception('Role not found')

        employee.role_id = role.id

        self._db.commit()

    @database_operation(session)
    def update_department(self, employee_id, department_id) -> None:
        employee = self._db.query(Employee).filter(Employee.id == employee_id).first()

        if employee is None:
            raise Exception('Employee not found')

        department = self._db.query(Department).filter(Department.id == department_id).first()

        if department is None:
            raise Exception('Role not found')

        employee.department_id = department.id

        self._db.commit()


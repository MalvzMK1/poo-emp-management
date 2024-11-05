from app.models import Department, Employee
from app.repositories.base_repository import BaseRepository
from app.utils.decorators import database_operation
from app.config import session

class DepartmentRepository(BaseRepository[Department]):
    def __init__(self):
        super().__init__(Department)

    @database_operation(session)
    def create(self, data: Department) -> None:
        existent_department = self._db.query(Department).filter(Department.name == data.name).first()

        if existent_department is not None:
            raise Exception('The department name is not available')

        self._db.add(data)
        self._db.commit()
        self._db.refresh(data)

    @database_operation(session)
    def update(self, id: int, data: Department) -> None:
        department = self._db.query(Department).filter(Department.id == id).first()

        if not department:
            raise Exception('Department not found')

        department.name = data.name
        department.manager_id = data.manager_id

        self._db.commit()

    @database_operation(session)
    def change_manager(self, department_id: int, manager_id: int) -> Department:
        department = self._db.query(Department).filter(Department.id == department_id).first()

        if not department:
            raise Exception('Department not found')

        manager = self._db.query(Employee).filter(Employee.id == manager_id).first()

        if not manager:
            raise Exception('Manager not found')

        department.manager_id = manager.id

        self._db.commit()
        self._db.refresh(department)

        return department
    
    @database_operation(session)
    def find_many_employees(self, department_id: int) -> list[Employee]:
        department = self._db.query(Department).filter(Department.id == department_id).first()

        if department is None:
            raise Exception('Department not found')

        return self._db.query(Employee).filter(Employee.department_id == department_id).all()

from app.models import Employee
from app.repositories.base_repository import BaseRepository 

class EmployeeRepository(BaseRepository[Employee]):
    def __init__(self):
        super().__init__(Employee)

    def update(self, id: int, data: Employee) -> None:
        employee = self._db.query(Employee).filter(Employee.id == id).first()

        if not employee:
            raise Exception('Employee not found')

        employee.name = data.name
        employee.document = data.document
        employee.role_id = data.role_id
        employee.department_id = data.department_id
        employee.managed_department_id = data.managed_department_id

        self._db.commit()


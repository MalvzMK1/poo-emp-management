from app.models import Role, Employee
from app.repositories.base_repository import BaseRepository
from app.utils.decorators import database_operation
from app.config import session

class RoleRepository(BaseRepository[Role]):
    def __init__(self):
        super().__init__(Role)

    @database_operation(session)
    def create(self, data: Role) -> None:
        existent_role = self._db.query(Role).filter(Role.name == data.name).first()

        if existent_role is not None:
            raise Exception('A role with this name already exists')

        self._db.add(data)
        self._db.commit()
        self._db.refresh(data)

    @database_operation(session)
    def update(self, id: int, data: Role) -> Role:
        existent_role = self._db.query(Role).filter(Role.name == data.name).first()

        if existent_role is not None:
            raise Exception('A role with this name already exists')

        role = self._db.query(Role).filter(Role.id == id).first()

        if not role:
            raise Exception('Role not found')

        role.name = data.name

        self._db.commit()
        self._db.refresh(role)

        return role

    @database_operation(session)
    def delete(self, id: int) -> None:
        role = self._db.query(Role).filter(Role.id == id).first()

        if role is None:
            raise Exception('Role not found')

        employees_count = self._db.query(Employee).filter(Employee.role_id == id).count()

        if employees_count > 0:
            raise Exception('There are employees with this role')

        self._db.delete(role)
        self._db.commit()

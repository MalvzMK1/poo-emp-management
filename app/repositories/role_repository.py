from app.models.role import Role
from app.repositories.base_repository import BaseRepository

class RoleRepository(BaseRepository[Role]):
    def __init__(self):
        super().__init__(Role)

    def update(self, id: int, data: Role) -> None:
        role = self._db.query(Role).filter(Role.id == id).first()

        if not role:
            raise Exception('Role not found')

        role.name = data.name

        self._db.commit()

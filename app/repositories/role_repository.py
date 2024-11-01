from .base_repository import BaseRepository
from ..models import Role

class RoleRepository(BaseRepository):
    def __init__(self):
        super().__init__()

    def create(self, data: Role) -> None:
        pass

    def update(self, id: int, data: Role) -> None:
        pass

    def delete(self, id: int) -> None:
        pass

    def find_by_id(self, id: int) -> Role:
        pass

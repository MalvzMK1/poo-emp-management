from app.repositories import RoleRepository
from tabulate import tabulate

class RoleService:
    def __init__(self) -> None:
        self.__role_repository = RoleRepository()

    def list_all(self) -> None:
        roles = self.__role_repository.find_all()

        headers = ('ID', 'Name')
        filtered_data: list[tuple[int, str]] = []

        for role in roles:
            filtered_data.append((role.id, role.name))

        print('\n--- Roles ---\n')
        print(tabulate(filtered_data, headers=headers))
        print(f'Total count: {len(roles)}\n')


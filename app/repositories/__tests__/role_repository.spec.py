from app.models.role import Role
from app.repositories.role_repository import RoleRepository


def test():
    role_repository = RoleRepository()

    new_role = role_repository.create(Role('Testing'))

    assert new_role is not None

    role_repository.update(new_role.id, Role('Test update'))

    assert new_role.name == 'Test update'

test()

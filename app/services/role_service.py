from typing import TypedDict
from typing_extensions import ReadOnly
from app.models import department
from app.models.role import Role
from app.repositories import RoleRepository
from tabulate import tabulate

class BaseInfosOutput(TypedDict):
    name: ReadOnly[str]

class RoleService:
    def __init__(self) -> None:
        self.__role_repository = RoleRepository()
        self.__options = (
            ('List All', self.list_all),
            ('Create', self.__create),
            ('Delete', self.__delete),
            ('Update', self.__update),
            ('List Employees', self.__list_employees),
        )

    def __print_options(self) -> None:
        print()
        for idx, option in enumerate(self.__options):
            print(f'{idx + 1} - {option[0]}')

    def main(self) -> None:
        self.__print_options()

        choosen_option = int(input('\nSelecione a opção: '))

        if choosen_option < 0 or choosen_option > self.__options.__len__():
            print('\nOpção inválida')

            return

        module = self.__options[choosen_option - 1][1]

        module()

    def __create(self) -> None:
        role = Role(**self.__get_base_infos())

        try:
            self.__role_repository.create(role)

            print('\nrole created successfully')
        except Exception as e:
            print(f'\nCould not create a role\n\nError: {e}')

    def __delete(self) -> None:
        try:
            role_id = self.__get_role_id()
        except Exception as e:
            print(f'\nCould not get role id\n\nError: {e}')

            return

        employees_in_role = self.__role_repository.get_employees(role_id)

        if employees_in_role.__len__() > 0:
            print('\nCannot delete role\nThere are employees in this role')

            return

        decision = input('\nAre you sure? [Y/N]: ')

        if decision[0] == 'y':
            self.__role_repository.delete(role_id)

            print('\nrole deleted successfully')
        elif decision[0] == 'n':
            print('\nOperation canceled')
        else:
            print('\nThe provided char is not valid')

    def __update(self) -> None:
        try:
            role_id = self.__get_role_id()
        except Exception as e:
            print(f'\nCould not get role id\n\nError: {e}')

            return

        data = self.__get_base_infos()

        try:
            self.__role_repository.update(role_id, data)

            print('\nrole updated successfully')
        except Exception as e:
            print(f'\nCould not update role\n\nError: {e}')

    def list_all(self) -> None:
        roles = self.__role_repository.find_all()

        headers = ('ID', 'Name')
        filtered_data = []

        for role in roles:
            filtered_data.append((role.id, role.name))

        print('\n--- Roles ---\n')
        print(tabulate(filtered_data, headers=headers))
        print(f'Total count: {len(roles)}\n')

    def __list_employees(self) -> None:
        try:
            role_id = self.__get_role_id()
        except Exception as e:
            print(f'\nCould not get role id\n\nError: {e}')

            return

        employees = self.__role_repository.get_employees(role_id)

        headers = ('ID', 'Name', 'Document', 'Department')
        filtered_data = []

        for employee in employees:
            filtered_data.append(
                (
                    employee.id,
                    employee.name,
                    employee.document,
                    employee.department.name if employee.department else 'Not Setted',
                )
            )

        print('\n--- Employees ---\n')
        print(tabulate(filtered_data, headers=headers))
        print(f'Total count: {len(employees)}\n')

    def __get_role_id(self) -> int:
        self.list_all()

        return int(input('Role ID: '))
        
    def __get_base_infos(self) -> BaseInfosOutput:
        name = input('\nName: ')

        return BaseInfosOutput(name=name)

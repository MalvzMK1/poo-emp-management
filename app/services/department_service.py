from typing import TypedDict
from typing_extensions import ReadOnly
from app.models.department import Department
from app.repositories import DepartmentRepository
from tabulate import tabulate

class BaseInfosOutput(TypedDict):
    name: ReadOnly[str]

class DepartmentService:
    def __init__(self) -> None:
        self.__department_repository = DepartmentRepository()
        self.__options = (
            ('List All', self.list_all),
            ('Create', self.__create),
            ('Delete', self.__delete),
            ('Update', self.__update),
            ('List Employees', self.__list_employees),
            ('Show Manager', self.__print_manager)
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

    def list_all(self) -> None:
        departments = self.__department_repository.find_all()

        headers = ('ID', 'Name')
        filtered_data = []

        for department in departments:
            filtered_data.append((department.id, department.name))

        print('\n--- departments ---\n')
        print(tabulate(filtered_data, headers=headers))
        print(f'Total count: {len(departments)}\n')

    def __create(self) -> None:
        department = Department(**self.__get_base_infos())

        try:
            self.__department_repository.create(department)

            print('\nDepartment created successfully')
        except Exception as e:
            print(f'\nCould not create a department\n\nError: {e}')

    def __delete(self) -> None:
        try:
            department_id = self.__get_department_id()
        except Exception as e:
            print(f'\nCould not get department id\n\nError: {e}')

            return

        employees_in_department = self.__department_repository.find_many_employees(department_id)

        if employees_in_department.__len__() > 0:
            print('\nCannot delete department\nThere are employees in this department')

            return

        decision = input('\nAre you sure? [Y/N]: ')

        if decision[0] == 'y':
            self.__department_repository.delete(department_id)

            print('\nDepartment deleted successfully')
        elif decision[0] == 'n':
            print('\nOperation canceled')
        else:
            print('\nThe provided char is not valid')

    def __update(self) -> None:
        try:
            department_id = self.__get_department_id()
        except Exception as e:
            print(f'\nCould not get department id\n\nError: {e}')

            return

        data = self.__get_base_infos()

        try:
            self.__department_repository.update(department_id, data)

            print('\nDepartment updated successfully')
        except Exception as e:
            print(f'\nCould not update department\n\nError: {e}')

    def __list_employees(self) -> None:
        try:
            department_id = self.__get_department_id()
        except Exception as e:
            print(f'\nCould not get department id\n\nError: {e}')

            return

        employees = self.__department_repository.find_many_employees(department_id)

        headers = ('ID', 'Name', 'Document', 'Role')
        filtered_data = []

        for employee in employees:
            filtered_data.append(
                (
                    employee.id,
                    employee.name,
                    employee.document,
                    employee.role.name if employee.role else 'Not Setted',
                )
            )

        print('\n--- Employees ---\n')
        print(tabulate(filtered_data, headers=headers))
        print(f'Total count: {len(employees)}\n')

    def __print_manager(self) -> None:
        try:
            department_id = self.__get_department_id()
        except Exception as e:
            print(f'\nCould not get department id\n\nError: {e}')

            return

        manager = self.__department_repository.find_manager(department_id)

        if manager is None:
            print('The department has no manager')

            return

        print('\n--- Manager ---')
        print(f'Name: {manager.name}')
        print(f'Document: {manager.document}')
        
    def __get_department_id(self) -> int:
        self.list_all()

        return int(input('Department ID: '))
        
    def __get_base_infos(self) -> BaseInfosOutput:
        name = input('\nName: ')

        return BaseInfosOutput(name=name)

from typing import TypedDict
from typing_extensions import ReadOnly
from app.models import Employee
from app.repositories import EmployeeRepository
from app.repositories.department_repository import DepartmentRepository
from app.repositories.task_repository import TaskRepository
from app.services.department_service import DepartmentService
from app.services.role_service import RoleService
from tabulate import tabulate

from app.utils.enums.roles_enum import RolesEnum

class BaseInfosOutput(TypedDict):
    name: ReadOnly[str]
    document: ReadOnly[str]

class EmployeeService:
    def __init__(self) -> None:
        self.__employee_repository = EmployeeRepository()
        self.__role_service = RoleService()
        self.__department_service = DepartmentService()
        self.__task_repository = TaskRepository()
        self.__department_repository = DepartmentRepository()
        self.__min_document_length = 9
        self.__options = (
            ('Create', self.__create),
            ('List All', self.list_all),
            ('Update Base Data', self.__update_base_data),
            ('Update Employee Department', self.__update_employee_department),
            ('Update the Department That The User Manages', self.__update_managed_department),
            ('Update Employee Role', self.__update_employee_role),
            ('List Tasks', self.__list_tasks),
            ('Delete', self.__delete)
        )

    def __print_options(self) -> None:
        print()
        for idx, option in enumerate(self.__options):
            print(f'{idx + 1} - {option[0]}')

    def main(self) -> None:
        self.__print_options()

        try:
            choosen_option = int(input('\nSelecione a opção: '))
        except Exception as e:
            print(f'\nCould not get option\n\nError: {e}')

            return

        if choosen_option < 0 or choosen_option > self.__options.__len__():
            print('\nOpção inválida')

            return

        module = self.__options[choosen_option - 1][1]

        module()

    def __create(self) -> None:
        employee = Employee(**self.__get_base_infos())

        if len(str(employee.document)) < self.__min_document_length:
            print(f'Document need to have at least {self.__min_document_length} chars')

            return

        try:
            self.__employee_repository.create(employee)
        except Exception as e:
            print(f'Could not create employee\n\nError: {e}')

            return

        print(f'Employee created successfully\n\nID: {employee.id}')

    def list_all(self) -> int:
        employees = self.__employee_repository.find_all()

        if not employees:
            print('No employees found')

            return 0
        
        headers = ('ID', 'Name', 'Document', 'Department', 'Role')
        filtered_data = []

        for employee in employees:
            filtered_data.append(
                (
                    employee.id,
                    employee.name,
                    employee.document,
                    employee.department.name if employee.department else 'Not Setted',
                    employee.role.name if employee.role else 'Not Setted'
                 )
            )

        print('\n--- Employees ---\n')
        print(tabulate(filtered_data, headers=headers))
        print(f'Total count: {len(employees)}\n')

        return len(employees)

    def __update_base_data(self) -> None:
        try:
            employee_id = self.get_employee_id()
        except Exception as e:
            print(f'Could not get employee ID\n\nError: {e}')

            return

        data = self.__get_base_infos()

        try:
            self.__employee_repository.update(employee_id, data)
            
            print('Employee successfully updated') 
        except Exception as e:
            print(f'Could not update employee\n\nError: {e}')

    def __update_employee_role(self) -> None:
        self.list_all()

        try:
            employee_id = int(input('Employee ID to update: '))
        except Exception as e:
            print(f'Could not get employee ID\n\nError: {e}')

            return

        employee = self.__employee_repository.find_by_id(employee_id)

        if employee is None:
            print('Employee not found')

            return

        self.__role_service.list_all()

        try:
            role_id = int(input('Role ID: '))
        except Exception as e:
            print(f'Could not get role ID\n\nError: {e}')

            return

        try:
            self.__employee_repository.update_role(employee_id, role_id)
            if \
                employee.managed_department_id is not None \
                and role_id is not RolesEnum.MANAGER.value \
            :
                self.__employee_repository.update_managed_department(employee_id, None)
        except Exception as e:
            print(f'Could not update employee role\n\nError: {e}')

            return

        print('Employee role updated successfully')

    def __update_employee_department(self) -> None:
        try:
            employee_id = self.get_employee_id()
        except Exception as e:
            print(f'Could not get employee ID\n\nError: {e}')

            return

        self.__department_service.list_all()

        try:
            department_id = int(input('Department ID: '))
        except Exception as e:
            print(f'Could not get department ID\n\nError: {e}')

            return
        
        try:
            self.__employee_repository.update_department(employee_id, department_id)
        except Exception as e:
            print(f'Could not update employee department\n\nError: {e}')

            return

        print('Employee department updated successfully')

    def __update_managed_department(self) -> None:
        try:
            employee_id = self.get_employee_id()
        except Exception as e:
            print(f'Could not get employee ID\n\nError: {e}')

            return

        self.__department_service.list_all()

        try:
            department_id = int(input('Department ID [0 for null]: '))
        except Exception as e:
            print(f'Could not get department ID\n\nError: {e}')

            return

        if department_id != 0:
            department = self.__department_repository.find_by_id(department_id)

            if department is None:
                print('\nDepartment not found')

                return

            if department.manager is not None:
                print('The department alredy have a manager')
        
        try:
            self.__employee_repository.update_managed_department(employee_id, department_id if department_id != 0 else None)

            print('\nUpdated user managed department successfully')
        except Exception as e:
            print(f'Could not update employee department\n\nError: {e}')

    def __delete(self) -> None:
        try:
            employee_id = self.get_employee_id()
        except Exception as e:
            print(f'Could not get employee ID\n\nError: {e}')

            return
        
        decision = input('\nAre you sure? [Y/N]: ')

        if decision[0] == 'y':
            self.__employee_repository.delete(employee_id)

            print('\nEmployee deleted successfully')
        elif decision[0] == 'n':
            print('\nOperation canceled')
        else:
            print('\nThe provided char is not valid')

    def __list_tasks(self) -> None:
        try:
            employee_id = self.get_employee_id()
        except Exception as e:
            print(f'Could not get employee ID\n\nError: {e}')

            return

        tasks = self.__task_repository.find_employee_tasks(employee_id)

        headers = ('ID', 'Name', 'Status')
        filtered_data = []

        for task in tasks:
            filtered_data.append((
                task.id, 
                task.name, 
                'Done' if task.is_done else 'Not done',
            ))

        print('\n--- tasks ---\n')
        print(tabulate(filtered_data, headers=headers))
        print(f'Total count: {len(tasks)}\n')

    def get_employee_id(self) -> int:
        total_count = self.list_all()

        if total_count > 0:
            return int(input('Employee ID: '))
        return 0
        
    def __get_base_infos(self) -> BaseInfosOutput:
        name = input('Name: ')
        document = input('Document: ')

        return BaseInfosOutput(name=name, document=document)


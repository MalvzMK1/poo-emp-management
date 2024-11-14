from typing import TypedDict
from typing_extensions import ReadOnly
from app.models.task import Task
from app.repositories import TaskRepository
from tabulate import tabulate

from app.services.employee_service import EmployeeService

class BaseInfosOutput(TypedDict):
    name: ReadOnly[str]

class TaskService:
    def __init__(self) -> None:
        self.__task_repository = TaskRepository()
        self.__employee_service = EmployeeService()
        self.__options = (
            ('List All', self.list_all),
            ('Create', self.__create),
            ('Delete', self.__delete),
            ('Update name', self.__update_name),
            ('Change Owner', self.__update_owner),
            ('Change Task Status', self.__toggle_status)
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
        task = Task(**self.__get_base_infos())

        try:
            self.__task_repository.create(task)

            print('\nTasks Created Successfully')
        except Exception as e:
            print('\nCould not create task\n\nError: {e}')

    def __delete(self) -> None:
        try:
            id = self.__get_task_id()
        except Exception as e:
            print(f'\nCould not get task id\n\nError: {e}')

            return

        decision = input('\nAre you sure? [Y/N]: ')

        if decision[0] == 'y':
            self.__task_repository.delete(id)

            print('\nTask deleted successfully')
        elif decision[0] == 'n':
            print('\nOperation canceled')
        else:
            print('\nThe provided char is not valid')

    def __update_name(self) -> None:
        try:
            id = self.__get_task_id()
        except Exception as e:
            print(f'\nCould not get task id\n\nError: {e}')

            return
        
        new_name = input('\nNew task name: ')

        try:
            self.__task_repository.update(id, {'name': new_name})

            print('\nTask updated successfully')
        except Exception as e:
            print('\nCould not update the task name\n\nError: {e}')

    def __update_owner(self) -> None:
        try:
            id = self.__get_task_id()
        except Exception as e:
            print(f'\nCould not get task id\n\nError: {e}')

            return
        
        try:
            new_owner_id = self.__employee_service.get_employee_id()
        except Exception as e:
            print(f'\nCould not get new owner id\n\nError: {e}')

            return

        try:
            self.__task_repository.change_owner(new_owner_id, id)

            print('\nTask owner changed successfully')
        except Exception as e:
            print(f'\nCould not change task owner\n\nError: {e}')

    def __toggle_status(self) -> None:
        try:
            id = self.__get_task_id()
        except Exception as e:
            print(f'\nCould not get task id\n\nError: {e}')

            return

        task = self.__task_repository.find_by_id(id)

        if task is None:
            print('\nTask not found')

            return

        action = 'done' if not task.is_done else 'undone'

        try:
            self.__task_repository.toggle_task_status(id)

            print(f'Task marked as {action}')
        except Exception as e:
            print(f'\nCould not toggle task status\n\nError: {e}')

    def list_all(self) -> None:
        tasks = self.__task_repository.find_all()

        headers = ('ID', 'Name', 'Status', 'Owner ID', 'Owner name')
        filtered_data = []

        for task in tasks:
            filtered_data.append((
                task.id, 
                task.name, 
                'Done' if task.is_done else 'Not done',
                task.owner_id,
                task.owner.name if task.owner else None
            ))

        print('\n--- tasks ---\n')
        print(tabulate(filtered_data, headers=headers))
        print(f'Total count: {len(tasks)}\n')

    def __get_task_id(self) -> int:
        self.list_all()

        return int(input('task ID: '))
        
    def __get_base_infos(self) -> BaseInfosOutput:
        name = input('\nName: ')

        return BaseInfosOutput(name=name)

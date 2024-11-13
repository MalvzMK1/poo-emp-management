from app.repositories import TaskRepository
from tabulate import tabulate

class TaskService:
    def __init__(self) -> None:
        self.__task_repository = TaskRepository()

    def main(self) -> None:
        print('I\'m in task service main function')
        pass

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

    def list_employee_tasks(self, employee_id: int) -> None:
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

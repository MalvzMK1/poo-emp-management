from app.services.department_service import DepartmentService
from app.services.employee_service import EmployeeService
from app.services.role_service import RoleService
from app.services.task_service import TaskService

class MainService:
    def __init__(self) -> None:
        self.__modules = [EmployeeService(), DepartmentService(), TaskService(), RoleService()]

    def main(self) -> None:
        print('--- EMPLOYEE MANAGEMENT CLI SYSTEM ---')

        self.__list_modules()

        while True:
            choosen_module: str | int = input('\nChoose a module (lm to list available modules / exit to exit): ')

            if choosen_module == 'lm':
                self.__list_modules()

                continue
            elif choosen_module == 'exit':
                print('\nGoodbye, thanks! :D\n')
                return

            try:
                choosen_module = int(choosen_module)
            except Exception as e:
                print(f'\nCould not convert module to integer\n\nError: {e}')

                continue

            if choosen_module > self.__modules.__len__():
                print('\nInvalid value')

                continue

            module = self.__modules[choosen_module - 1]

            if module is None:
                print(f'\nOpção {choosen_module} indisponível\n')

                continue

            module.main()

    def __list_modules(self) -> None:
        print()
        print('1 - Employee Module')
        print('2 - Department Module')
        print('3 - Task Module')
        print('4 - Role Module')
        print()

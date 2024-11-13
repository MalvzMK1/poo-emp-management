from app.repositories import DepartmentRepository
from tabulate import tabulate

class DepartmentService:
    def __init__(self) -> None:
        self.__department_depository = DepartmentRepository()

    def main() -> None:
        pass

    def list_all(self) -> None:
        departments = self.__department_depository.find_all()

        headers = ('ID', 'Name')
        filtered_data = []

        for department in departments:
            filtered_data.append((department.id, department.name))

        print('\n--- departments ---\n')
        print(tabulate(filtered_data, headers=headers))
        print(f'Total count: {len(departments)}\n')

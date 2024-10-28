from .sqlite import engine
from ...models import Department, Role, Task, Employee
from ...models.base_entity import Base

def migrate():
  print(Base.metadata.tables.keys())
  Base.metadata.create_all(engine)

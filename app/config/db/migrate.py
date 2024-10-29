from .sqlite import engine
from ...models import Department, Role, Task, Employee
from ...models.base_entity import Base
from .seed import seed

def migrate():
  Base.metadata.create_all(engine)

  seed()

from . import departments, roles
from .. import session

def seed():
  seeds_functions = [
    departments.run,
    roles.run
  ]

  for execute in seeds_functions:
    execute(session)
from sqlalchemy.orm import Session
from ....models import Role
from ....utils import decorate_seed 

@decorate_seed('Roles')
def run(db: Session):

  roles: list[Role] = [Role('manager'), Role('developer'), Role('tech-lead')]

  for role in roles:
    db.add(role)
  
  db.commit()

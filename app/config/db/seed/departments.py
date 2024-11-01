from sqlalchemy.orm import Session
from ....models import Department
from ....utils import decorate_seed 

@decorate_seed('Departments')
def run(db: Session):

  departments: list[Department] = [Department('Technology'), Department('HR'), Department('Sales')]

  for department in departments:
    db.add(department)
  
  db.commit()

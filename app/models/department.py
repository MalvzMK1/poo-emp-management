from typing import Any
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, Mapped
from .base_entity import BaseEntity

class Department(BaseEntity):
  def __init__(self, name: str, **kw: Any):
    super().__init__(**kw)
    self.name = name

  __tablename__ = 'departments'

  name: Mapped[str] = Column(String, unique=True)
  manager_id: Mapped[int] = Column(Integer, ForeignKey('employees.id'), unique=True)

  manager: Mapped['Employee'] = relationship('Employee', backref='managed_department')
  employees: Mapped[list['Employee']] = relationship()

  def __repr__(self) -> str:
    return f'''<Department(
      name={self.name}, 
      manager_id={self.manager_id}, 
      manager={self.manager}, 
      employees={self.employees}
    )>'''
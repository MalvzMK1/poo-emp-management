from typing import Any
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import relationship, mapped_column
from .base_entity import BaseEntity

class Department(BaseEntity):
  def __init__(self, name: str, **kw: Any):
    super().__init__(**kw)
    self.name = name

  __tablename__ = 'departments'

  name = mapped_column(String, unique=True)
  manager_id = mapped_column(Integer, ForeignKey('employees.id'), unique=True)

  manager = relationship('Employee', foreign_keys=[manager_id], backref='managed_departments')

  def __repr__(self) -> str:
    return f'''<Department(
      id={self.id},
      name={self.name}, 
      manager_id={self.manager_id}
    )>'''

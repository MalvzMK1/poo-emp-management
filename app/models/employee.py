from typing import Any
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import relationship, mapped_column
from .base_entity import BaseEntity

class Employee(BaseEntity):
  def __init__(self, name: str, document: str, **kw: Any):
    super().__init__(**kw)
    self.name = name
    self.document = document

  __tablename__ = 'employees'

  name = mapped_column(String)
  document = mapped_column(String, unique=True)
  managed_department_id = mapped_column(Integer, ForeignKey('departments.id'), nullable=True)
  department_id = mapped_column(Integer, ForeignKey('departments.id'))
  role_id = mapped_column(Integer, ForeignKey('roles.id'))

  managed_department = relationship('Department', foreign_keys=[managed_department_id])
  department = relationship('Department', foreign_keys=[department_id], backref='employees')
  role = relationship('Role', back_populates='employees')
  tasks = relationship('Task', back_populates='owner')

  def __repr__(self) -> str:
    return f'''<Employee(
      id={self.id},
      name={self.name}, 
      document={self.document},
      managed_department_id={self.managed_department_id},
      department_id={self.department_id},
      role_id={self.role_id}
    )>'''

from typing import Any
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, Mapped
from .base_entity import BaseEntity
from . import Department, Role, Task

class Employee(BaseEntity):
  def __init__(self, name: str, document: str, **kw: Any):
    super().__init__(**kw)
    self.name = name
    self.document = document

  __tablename__ = 'employees'

  name: Mapped[str] = Column(String)
  document: Mapped[str] = Column(String, unique=True)
  managed_department_id: Mapped[int] = Column(Integer, ForeignKey('departments.id'), nullable=True)
  department_id: Mapped[int] = Column(Integer, ForeignKey('departments.id'))
  role_id: Mapped[int] = Column(Integer, ForeignKey('roles.id'))

  department: Mapped[Department] = relationship('Department', backref='employee')
  managed_department: Mapped[Department] = relationship('Department', backref='manager')
  role: Mapped[Role] = relationship('Role', backref="employees")
  tasks: Mapped[list[Task]] = relationship()

  def __repr__(self) -> str:
    return f'''<Employee(
      name={self.name}, 
      document={self.document}
    )>'''
from typing import Any
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, Mapped
from .base_entity import BaseEntity

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

  managed_department: Mapped['Department'] = relationship('Department', foreign_keys=[managed_department_id])
  department: Mapped['Department'] = relationship('Department', foreign_keys=[department_id], backref='employees')
  role: Mapped['Role'] = relationship('Role', back_populates='employees')
  tasks: Mapped[list['Task']] = relationship('Task', back_populates='owner')

  def __repr__(self) -> str:
    return f'''<Employee(
      name={self.name}, 
      document={self.document},
      managed_department_id={self.managed_department_id},
      department_id={self.department_id},
      role_id={self.role_id},
      managed_department={self.managed_department},
      department={self.department},
      role={self.role},
      tasks={self.tasks}
    )>'''
from typing import Any
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship, Mapped
from .base_entity import BaseEntity
from .employee import Employee

class Task(BaseEntity):
  def __init__(self, name: str, **kw: Any):
    super().__init__(**kw)
    self.name = name
  
  __tablename__ = 'tasks'
  
  name = Column(String)
  is_done = Column(Boolean, default=False)
  owner_id = Column(Integer, ForeignKey('employees.id'), nullable=True)

  owner = relationship('Employee', back_populates='tasks')

  def __repr__(self) -> str:
    return f'''<Task(
      id={self.id},
      name={self.name},
      is_done={self.is_done},
      owner_id={self.owner_id},
    )>'''

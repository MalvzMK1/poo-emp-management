from typing import Any
from sqlalchemy import String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship, mapped_column
from .base_entity import BaseEntity

class Task(BaseEntity):
  def __init__(self, name: str, **kw: Any):
    super().__init__(**kw)
    self.name = name
  
  __tablename__ = 'tasks'
  
  name = mapped_column(String)
  is_done = mapped_column(Boolean, default=False)
  owner_id = mapped_column(Integer, ForeignKey('employees.id'), nullable=True)

  owner = relationship('Employee', back_populates='tasks')

  def __repr__(self) -> str:
    return f'''<Task(
      id={self.id},
      name={self.name},
      is_done={self.is_done},
      owner_id={self.owner_id},
    )>'''

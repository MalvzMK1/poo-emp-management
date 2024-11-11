from typing import Any
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, Mapped
from .base_entity import BaseEntity
from . import Employee

class Role(BaseEntity):
  def __init__(self, name: str, **kw: Any):
    super().__init__(**kw)
    self.name = name

  __tablename__ = 'roles'

  name = Column(String, unique=True)

  employees = relationship('Employee', back_populates='role')

  def __repr__(self) -> str:
    return f'''<Role(
      id={self.id},
      name={self.name}
    )>'''

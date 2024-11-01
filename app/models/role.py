from typing import Any
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped
from .base_entity import BaseEntity
from . import Employee

class Role(BaseEntity):
  def __init__(self, name: str, **kw: Any):
    super().__init__(**kw)
    self.name = name

  __tablename__ = 'roles'

  name: Mapped[str] = Column(String, unique=True)

  employees: Mapped['Employee'] = relationship('Employee', back_populates='role')

  def __repr__(self) -> str:
    return f'''<Role(
      name={self.name},
      employees={self.employees}
    )>'''
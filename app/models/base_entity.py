from sqlalchemy import Column, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped

class BaseEntity(DeclarativeBase):
  id: Mapped[int] = Column(Integer, primary_key=True)
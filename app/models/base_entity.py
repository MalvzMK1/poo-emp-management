from sqlalchemy import Column, Integer
from sqlalchemy.orm import Mapped, declarative_base

Base = declarative_base()

class BaseEntity(Base):
  __abstract__ = True

  id = Column(Integer, primary_key=True)

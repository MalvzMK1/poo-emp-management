from sqlalchemy import Integer
from sqlalchemy.orm import mapped_column, declarative_base

Base = declarative_base()

class BaseEntity(Base):
  __abstract__ = True

  id = mapped_column(Integer, primary_key=True)

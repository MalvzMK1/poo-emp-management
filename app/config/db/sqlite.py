from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('sqlite:///employees.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///employees.db')
Session = sessionmaker(autocommit=False, bind=engine)
session = Session()

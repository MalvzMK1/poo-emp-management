from sqlite import engine, Base

def migrate():
  Base.metadata.create_all(engine)
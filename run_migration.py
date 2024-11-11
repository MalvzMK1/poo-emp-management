from time import time
from app.config import migrate

if __name__ == '__main__':
  print('\nMigrating data...')

  start_time = time()
  migrate()
  end_time = time()

  print('\nMigration executed succesfully.\n')
def decorate_seed(name: str):
  def decorator(fn):
    def wrapper(*args, **kwargs):
      print(f'[ ] - Creating {name}')

      fn(*args, **kwargs)

      print(f'[✔] - {name} created successfully')

    return wrapper
  
  return decorator
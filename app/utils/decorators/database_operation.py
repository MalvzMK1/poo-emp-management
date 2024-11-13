from sqlalchemy.orm import Session

def database_operation(session: Session):
    def decorator(fun):
        def wrapper(*args, **kwargs):
            try:
                fun(*args, **kwargs)
            except Exception as e:
                session.rollback()

                raise e

        return wrapper
    return decorator

from sqlalchemy.orm import Session

def database_operation(session: Session):
    def decorator(fun):
        def wrapper(*args, **kwargs):
            try:
                fun(*args, **kwargs)
            except Exception:
                session.rollback()

                raise Exception
            finally:
                session.close()

        return wrapper
    return decorator

from abc import ABC, abstractmethod
from typing import Any, Generic, Optional, Type, TypeVar
from app.models.base_entity import BaseEntity
from app.utils import database_operation
from app.config import session

T = TypeVar('T', bound=BaseEntity)

class BaseRepository(ABC, Generic[T]):
    def __init__(self, model: Type[T]):
        self._db = session
        self._model = model

    @database_operation(session)
    def create(self, data: T) -> T:
        self._db.add(data)

        try:
            self._db.commit()
        except Exception:
            self._db.rollback()

            raise Exception

        self._db.refresh(data)

        return data

    @abstractmethod
    @database_operation(session)
    def update(self, id: int, data: T) -> Any:
        pass

    @database_operation(session)
    def delete(self, entity: T) -> None:
        self._db.delete(entity)

        self._db.commit()

    @database_operation(session)
    def find_by_id(self, id: int) -> Optional[T]:
        return self._db \
            .query(self._model) \
            .filter(self._model.id == id) \
            .first()


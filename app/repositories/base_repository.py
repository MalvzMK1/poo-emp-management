from abc import ABC, abstractmethod
from typing import Any, Generic, Optional, TypeVar
from app.models.base_entity import BaseEntity
from app.utils import database_operation
from app.config import session

T = TypeVar('T', bound=BaseEntity)

class BaseRepository(ABC, Generic[T]):
    def __init__(self, model: T):
        self._db = session
        self._model = model

    @database_operation(session)
    def create(self, data: T) -> None:
        self._db.add(data)

        self._db.commit()

        self._db.refresh(data)

    @abstractmethod
    @database_operation(session)
    def update(self, id: int, data: T) -> Any:
        pass

    @database_operation(session)
    def delete(self, id: int) -> None:
        entity = self._db.query(self._model).filter(self._model.id == id).first()

        self._db.delete(entity)

        self._db.commit()

    def find_by_id(self, id: int) -> Optional[T]:
        return self._db \
            .query(self._model) \
            .filter(self._model.id == id) \
            .first()

    def find_all(self) -> list[T]:
        return self._db \
            .query(self._model) \
            .all()

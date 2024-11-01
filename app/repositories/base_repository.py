from ..config import session
from abc import ABC, abstractmethod

class BaseRepository(ABC):
    def __init__(self):
        self._db = session

    @abstractmethod
    def create(self, data):
        pass

    @abstractmethod
    def update(self, id: int, data):
        pass

    @abstractmethod
    def delete(self, id: int):
        pass

    @abstractmethod
    def find_by_id(self, id: int):
        pass

from abc import ABC, abstractmethod

from cafe.cafe_core.output.repositories.cafe_repository import CafeRepository


class CafeUow(ABC):

    cafe_repository: CafeRepository

    @abstractmethod
    async def __aenter__(self):
        ...

    @abstractmethod
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        ...

    @abstractmethod
    async def commit(self):
        ...

    @abstractmethod
    async def rollback(self):
        ...
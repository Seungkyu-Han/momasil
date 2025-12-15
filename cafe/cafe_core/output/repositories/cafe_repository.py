from abc import ABC, abstractmethod
from cafe.cafe_core import Cafe


class CafeRepository(ABC):

    @abstractmethod
    async def save(self, cafe: Cafe) -> Cafe:
        ...

    @abstractmethod
    async def find_all(self) -> list[Cafe]:
        ...

    @abstractmethod
    async def find_by_id(self, id_: int) -> Cafe | None:
        ...

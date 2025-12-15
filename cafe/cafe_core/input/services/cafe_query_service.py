from abc import ABC, abstractmethod

from cafe.cafe_core.domains.cafe import Cafe
from cafe.cafe_core.output.repositories.cafe_repository import CafeRepository


class CafeQueryService(ABC):
    cafe_repository: CafeRepository

    @abstractmethod
    async def find_all(self) -> list[Cafe]:
        ...

    @abstractmethod
    async def find_by_id(self, id_: int) -> Cafe:
        ...

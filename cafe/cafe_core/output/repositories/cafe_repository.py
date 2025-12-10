from abc import ABC, abstractmethod
from cafe.cafe_core import Cafe


class CafeRepository(ABC):

    @abstractmethod
    async def save(self, cafe: Cafe):
        pass
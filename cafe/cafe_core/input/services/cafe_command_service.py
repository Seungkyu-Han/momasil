from abc import ABC, abstractmethod

from cafe.cafe_core.domains.cafe import Cafe
from cafe.cafe_core.output.uow.cafe_uow import CafeUow


class CafeCommandService(ABC):
    cafe_uow: CafeUow

    @abstractmethod
    async def save(self, name: str, img: str, banner: str) -> Cafe:
        ...

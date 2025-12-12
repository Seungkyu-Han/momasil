from abc import ABC

from cafe.cafe_core.domains.cafe import Cafe
from cafe.cafe_core.output.uow.cafe_uow import CafeUow


class CafeQueryService(ABC):

    cafe_uow: CafeUow

    async def find_all(self) -> list[Cafe]:
        ...
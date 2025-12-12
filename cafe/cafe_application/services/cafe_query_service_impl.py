from cafe.cafe_core import CafeQueryService, CafeUow, Cafe


class CafeQueryServiceImpl(CafeQueryService):

    def __init__(self, cafe_uow: CafeUow):
        self.cafe_uow = cafe_uow

    async def find_all(self) -> list[Cafe]:
        async with self.cafe_uow.cafe_repository as cafe_repository:
            return await cafe_repository.find_all()
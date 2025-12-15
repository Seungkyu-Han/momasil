from cafe.cafe_core import CafeQueryService, Cafe, CafeRepository


class CafeQueryServiceImpl(CafeQueryService):
    def __init__(self, cafe_repository: CafeRepository):
        self.cafe_repository = cafe_repository

    async def find_all(self) -> list[Cafe]:
        return await self.cafe_repository.find_all()

    async def find_by_id(self, id_: int) -> Cafe:

        cafe: Cafe | None = await self.cafe_repository.find_by_id(id_=id_)

        if cafe is None:
            raise Exception

        return cafe

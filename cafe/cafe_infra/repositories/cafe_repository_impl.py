from sqlalchemy.ext.asyncio import AsyncSession

from cafe.cafe_core import CafeRepository
from cafe.cafe_core.domains.cafe import Cafe
from cafe.cafe_infra.entities.cafe_entity import CafeEntity
from cafe.cafe_infra.mappers import cafe_mapper


class CafeRepositoryImpl(CafeRepository):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def save(self, cafe: Cafe):
        cafe_entity: CafeEntity = cafe_mapper.to_entity(cafe=cafe)

        self.session.add(cafe_entity)
from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession

from cafe.cafe_core import CafeRepository, Cafe
from cafe.cafe_infra.entities.cafe_entity import CafeEntity
from cafe.cafe_infra.mappers import cafe_mapper
from sqlalchemy import select


class CafeRepositoryImpl(CafeRepository):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def save(self, cafe: Cafe):
        cafe_entity: CafeEntity = cafe_mapper.to_entity(cafe=cafe)

        self.session.add(cafe_entity)

    async def find_all(self) -> list[Cafe]:

        stmt = select(CafeEntity)

        result = await self.session.execute(stmt)

        cafe_entities: Sequence[CafeEntity] = result.scalars().all()

        return [cafe_mapper.to_domain(cafe_entity) for cafe_entity in cafe_entities]

    async def find_by_id(self, id_: int) -> Cafe | None:
        stmt = select(CafeEntity).where(CafeEntity.id_==id_)

        result = await self.session.execute(stmt)

        cafe_entity: CafeEntity | None = result.scalar_one_or_none()

        if cafe_entity:
            return cafe_mapper.to_domain(cafe_entity=cafe_entity)
        else:
            return None
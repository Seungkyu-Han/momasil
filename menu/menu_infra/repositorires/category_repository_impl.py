from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete

from menu.menu_core import CategoryRepository, Category
from menu.menu_infra.entities.category_entity import CategoryEntity
from menu.menu_infra.mappers import category_mapper


class CategoryRepositoryImpl(CategoryRepository):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def save(self, category: Category) -> Category:
        category_entity: CategoryEntity = category_mapper.to_entity(category=category)

        self.session.add(category_entity)

        return category

    async def find_by_cafe_id(self, cafe_id: int) -> list[Category]:
        stmt = select(CategoryEntity).where(
            CategoryEntity.cafe_id == cafe_id
        )

        result = await self.session.execute(stmt)

        category_entities: Sequence[CategoryEntity] = result.scalars().all()

        return [
            category_mapper.to_domain(category_entity=category_entity) for category_entity in category_entities
        ]

    async def delete_by_cafe_id(self, cafe_id: int):
        await self.session.execute(
            delete(CategoryEntity).where(CategoryEntity.cafe_id == cafe_id)
        )

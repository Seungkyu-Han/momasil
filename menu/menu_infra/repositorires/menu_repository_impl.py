from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete

from menu.menu_core import MenuRepository, Menu
from menu.menu_infra.entities.menu_entity import MenuEntity
from menu.menu_infra.mappers import menu_mapper



class MenuRepositoryImpl(MenuRepository):

    def __init__(
            self,
            session: AsyncSession,
    ):
        self.session = session

    async def save(self, menu: Menu) -> Menu:
        menu_entity: MenuEntity = menu_mapper.to_entity(menu=menu)

        self.session.add(menu_entity)

        return menu

    async def find_by_category_id_in(self, category_ids: list[int]) -> list[Menu]:
        stmt = select(MenuEntity).where(
            MenuEntity.category_id.in_(category_ids)
        )

        result = await self.session.execute(stmt)

        menu_entities: Sequence[MenuEntity] = result.scalars().all()


        return [
            menu_mapper.to_domain(menu_entity=menu_entity) for menu_entity in menu_entities
        ]

    async def delete_all(self, menus: list[Menu]):

        menu_ids = [menu.id_ for menu in menus]

        await self.session.execute(
            delete(MenuEntity).where(MenuEntity.id_.in_(menu_ids))
        )


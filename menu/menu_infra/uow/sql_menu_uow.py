from typing import Callable

from sqlalchemy.ext.asyncio import AsyncSession

from menu.menu_core import MenuUow, CategoryRepository, MenuRepository


class SqlMenuUow(MenuUow):

    def __init__(
            self,
            session: AsyncSession,
            category_repository_factory: Callable[[AsyncSession], CategoryRepository],
            menu_repository_factory: Callable[[AsyncSession], MenuRepository],
    ):
        self.session = session
        self.category_repository = category_repository_factory(session)
        self.menu_repository = menu_repository_factory(session)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            await self.rollback()
        else:
            await self.commit()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()

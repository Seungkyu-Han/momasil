from abc import ABC, abstractmethod

from menu.menu_core.domains.menu import Menu


class MenuRepository(ABC):

    @abstractmethod
    async def save(self, menu: Menu) -> Menu:
        ...

    @abstractmethod
    async def find_by_category_id_in(self, category_ids: list[int]) -> list[Menu]:
        ...

    @abstractmethod
    async def delete_all(self, menus: list[Menu]):
        ...

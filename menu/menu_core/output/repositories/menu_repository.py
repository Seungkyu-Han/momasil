from abc import ABC, abstractmethod

from menu.menu_core.domains.menu import Menu


class MenuRepository(ABC):

    @abstractmethod
    async def save(self, menu: Menu) -> Menu:
        ...

    @abstractmethod
    async def find_by_cafe_id(self, cafe_id: int) -> list[Menu]:
        ...


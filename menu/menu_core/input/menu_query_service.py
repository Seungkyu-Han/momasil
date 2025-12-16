from abc import ABC, abstractmethod

from menu.menu_core.models.category_menu import CategoryMenu


class MenuQueryService(ABC):

    @abstractmethod
    async def retrieve_menus_by_cafe_id(self, cafe_id: int) -> list[CategoryMenu]:
        ...

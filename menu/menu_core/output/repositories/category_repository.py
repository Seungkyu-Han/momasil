from abc import ABC, abstractmethod

from menu.menu_core.domains.category import Category


class CategoryRepository(ABC):

    @abstractmethod
    async def save(self, category: Category) -> Category:
        ...

    @abstractmethod
    async def find_by_cafe_id(self, cafe_id: int) -> list[Category]:
        ...

    @abstractmethod
    async def delete_by_cafe_id(self, cafe_id: int):
        ...


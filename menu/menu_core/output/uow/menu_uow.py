from abc import ABC, abstractmethod

from menu.menu_core import CategoryRepository, MenuRepository


class MenuUow(ABC):

    category_repository: CategoryRepository
    menu_repository: MenuRepository

    @abstractmethod
    async def __aenter__(self):
        ...

    @abstractmethod
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        ...

    @abstractmethod
    async def commit(self):
        ...

    @abstractmethod
    async def rollback(self):
        ...

from abc import ABC, abstractmethod

from cart.cart_core.output.repository.basket_repository import BasketRepository


class BasketUow(ABC):

    basket_repository: BasketRepository

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

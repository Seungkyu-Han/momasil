from abc import ABC, abstractmethod

from cart.cart_core.domains.basket import Basket


class BasketRepository(ABC):

    @abstractmethod
    async def save(self, basket: Basket) -> Basket:
        ...

    @abstractmethod
    async def find_by_id(self, id_: int) -> Basket:
        ...
from abc import ABC, abstractmethod

from cart.cart_core.domains.basket import Basket


class BasketRepository(ABC):

    @abstractmethod
    async def save(self, basket: Basket) -> Basket:
        ...
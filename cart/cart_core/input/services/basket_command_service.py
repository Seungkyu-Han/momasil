from abc import ABC, abstractmethod

from cart.cart_core.domains.basket import Basket
from cart.cart_core.domains.item import Item


class BasketCommandService(ABC):

    @abstractmethod
    async def create_basket(
            self,
            cafe_id: int,
            name: str,
    ) -> Basket:
        ...

    @abstractmethod
    async def update_basket(
            self,
            basket_id: int,
            items: list[Item]
    ) -> Basket:
        ...
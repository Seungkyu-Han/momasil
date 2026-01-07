from abc import ABC, abstractmethod

from cart.cart_core.domains.basket import Basket


class BasketCommandService(ABC):

    @abstractmethod
    async def create_basket(
            self,
            cafe_id: int,
            name: str,
    ) -> Basket:
        ...
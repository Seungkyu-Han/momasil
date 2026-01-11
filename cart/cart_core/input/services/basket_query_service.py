from abc import ABC, abstractmethod

from cart.cart_core.domains.basket import Basket


class BasketQueryService(ABC):

    @abstractmethod
    async def retrieve_basket(self, basket_id) -> Basket:
        ...
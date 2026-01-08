from cart.cart_core import BasketQueryService, Basket, BasketRepository


class BasketQueryServiceImpl(BasketQueryService):

    def __init__(self, basket_repository: BasketRepository):
        self.basket_repository = basket_repository

    async def retrieve_basket(self, basket_id) -> Basket:
        return await self.basket_repository.find_by_id(basket_id)

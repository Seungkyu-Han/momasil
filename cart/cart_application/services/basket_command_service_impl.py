from snowflake import SnowflakeGenerator

from cart.cart_core import BasketCommandService, BasketUow, Basket


class BasketCommandServiceImpl(BasketCommandService):

    def __init__(
            self,
            basket_uow: BasketUow,
            snowflake_generator: SnowflakeGenerator
    ):
        self.basket_uow = basket_uow
        self.snowflake_generator = snowflake_generator

    async def create_basket(
            self,
            cafe_id: int,
            name: str
    ) -> Basket:
        basket: Basket = Basket(
            id_=next(self.snowflake_generator),
            cafe_id=cafe_id,
            name=name,
        )

        async with self.basket_uow:
            await self.basket_uow.basket_repository.save(basket)

        return basket
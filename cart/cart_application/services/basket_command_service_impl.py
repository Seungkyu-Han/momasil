from snowflake import SnowflakeGenerator

from cart.cart_core import BasketCommandService, BasketUow, Basket
from cart.cart_core.domains.item import Item


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

    async def update_basket(
            self,
            basket_id: int,
            items: list[Item]
    ) -> Basket:
        async with self.basket_uow:
            basket: Basket | None = await self.basket_uow.basket_repository.find_by_id(basket_id)

            if basket is None:
                raise Exception

            basket.items = items

            await self.basket_uow.basket_repository.save(basket)

            return basket
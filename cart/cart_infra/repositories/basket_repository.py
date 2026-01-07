from sqlalchemy.ext.asyncio import AsyncSession

from cart.cart_core import Basket, BasketRepository
from cart.cart_infra.entities.basket_entity import BasketEntity
from cart.cart_infra.mappers import basket_mapper


class BasketRepositoryImpl(BasketRepository):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def save(self, basket: Basket) -> Basket:
        basket_entity: BasketEntity = basket_mapper.to_entity(basket=basket)

        self.session.add(basket_entity)

        return basket
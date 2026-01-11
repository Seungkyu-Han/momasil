from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from cart.cart_core import Basket, BasketRepository
from cart.cart_infra.entities.basket_entity import BasketEntity
from cart.cart_infra.mappers import basket_mapper


class BasketRepositoryImpl(BasketRepository):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def save(self, basket: Basket) -> Basket:
        basket_entity: BasketEntity = basket_mapper.to_entity(basket=basket)

        await self.session.merge(basket_entity)

        return basket

    async def find_by_id(self, id_: int) -> Basket | None:
        stmt = select(BasketEntity).where(
            BasketEntity.id_ == id_
        )

        result = await self.session.execute(stmt)

        basket_entity: BasketEntity = result.scalar_one_or_none()

        return basket_mapper.to_domain(basket_entity=basket_entity)
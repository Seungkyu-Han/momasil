from typing import Annotated

from fastapi import Depends

from database import SessionDep
from cart.cart_core import BasketRepository, BasketUow
from cart.cart_infra import BasketRepositoryImpl, BasketUowImpl


def get_basket_repository(session: SessionDep) -> BasketRepository:
    return BasketRepositoryImpl(session=session)

BasketRepositoryDep = Annotated[BasketRepository, Depends(get_basket_repository)]

def get_basket_uow(
        session: SessionDep,
) -> BasketUow:
    return BasketUowImpl(
        session=session,
        basket_repository_factory=get_basket_repository
    )

BasketUowDep = Annotated[BasketUow, Depends(get_basket_uow)]
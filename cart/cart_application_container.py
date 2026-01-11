from typing import Annotated

from fastapi import Depends

from cart.cart_application.services.basket_query_service_impl import BasketQueryServiceImpl
from cart.cart_core.input.services.basket_query_service import BasketQueryService
from config.snowflake_generator import SnowflakeGeneratorDep
from cart.cart_core import BasketCommandService
from cart.cart_application import BasketCommandServiceImpl
from cart.cart_infra_container import BasketUowDep, BasketRepositoryDep


def get_basket_command_service(
        basket_uow: BasketUowDep,
        snowflake_generator: SnowflakeGeneratorDep,
) -> BasketCommandService:
    return BasketCommandServiceImpl(
        basket_uow = basket_uow,
        snowflake_generator=snowflake_generator,
    )

BasketCommandServiceDep = Annotated[BasketCommandService, Depends(get_basket_command_service)]

def get_basket_query_service(
        basket_repository: BasketRepositoryDep
) -> BasketQueryService:
    return BasketQueryServiceImpl(
        basket_repository
    )
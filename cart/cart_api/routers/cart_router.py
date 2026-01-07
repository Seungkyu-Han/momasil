from fastapi import APIRouter

from cart.cart_api.dto.request.create_cart_request import CreateCartRequest
from cart.cart_api.routers.response.create_cart_response import CreateCartResponse
from cart.cart_application_container import BasketCommandServiceDep
from cart.cart_core import Basket

cart_router = APIRouter(
    prefix="/carts",
    tags=["cart"]
)

@cart_router.post(
    path="",
    description="새로운 카트를 생성",
    response_model=CreateCartResponse,
)
async def create_cart_api(
        basket_command_service: BasketCommandServiceDep,
        create_cart_request: CreateCartRequest,
) -> CreateCartResponse:
    cafe_id = int(create_cart_request.cafe_id)
    basket: Basket = await basket_command_service.create_basket(cafe_id=cafe_id, name="")

    return CreateCartResponse(
        cart_id=str(basket.id_)
    )
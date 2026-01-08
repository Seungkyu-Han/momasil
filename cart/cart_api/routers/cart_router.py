from fastapi import APIRouter, WebSocket

from cart.cart_api.dto.request.create_cart_request import CreateCartRequest
from cart.cart_api.dto.request.retrieve_cart_request import RetrieveCartRequest
from cart.cart_api.routers.response.create_cart_response import CreateCartResponse
from cart.cart_api.routers.response.item_response import ItemResponse
from cart.cart_api.routers.response.retrieve_cart_response import RetrieveCartResponse
from cart.cart_application_container import BasketCommandServiceDep, get_basket_query_service
from cart.cart_core import Basket
from cart.cart_infra_container import get_basket_repository
from database.session import async_session_maker

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


@cart_router.websocket(
    path="/websocket"
)
async def cart_websocket(
        websocket: WebSocket,
):

    await websocket.accept()

    retrieve_cart_request = RetrieveCartRequest.model_validate(await websocket.receive_json())

    async with async_session_maker() as session:

        basket_query_service = get_basket_query_service(
            basket_repository=get_basket_repository(session = session)
        )

        basket: Basket = await basket_query_service.retrieve_basket(int(retrieve_cart_request.cart_id))

        retrieve_cart_response: RetrieveCartResponse = RetrieveCartResponse(
            cart_id=str(basket.id_),
            items=[ItemResponse(
                name=str(item.id_),
                img=str(item.id_),
                count=item.count
            ) for item in basket.items]
        )

        await websocket.send_json(retrieve_cart_response.model_dump())

        await session.close()

    while True:
        data = await websocket.receive_text()

        print(data)
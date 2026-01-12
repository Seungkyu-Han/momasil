from fastapi import APIRouter, WebSocket
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.websockets import WebSocketDisconnect

from cart.cart_api.dto.request.create_cart_request import CreateCartRequest
from cart.cart_api.dto.request.item_request import ItemRequest
from cart.cart_api.dto.request.retrieve_cart_request import RetrieveCartRequest
from cart.cart_api.dto.request.update_cart_request import UpdateCartRequest
from cart.cart_api.dto.response.create_cart_response import CreateCartResponse
from cart.cart_api.dto.response.item_response import ItemResponse
from cart.cart_api.dto.response.retrieve_cart_response import RetrieveCartResponse
from cart.cart_application_container import BasketCommandServiceDep, get_basket_query_service, \
    get_basket_command_service
from cart.cart_core import Basket
from menu.menu_core import Menu, CategoryMenu
from cart.cart_infra_container import get_basket_repository, get_basket_uow
from config.snowflake_generator import get_snowflake_generator
from database.session import async_session_maker
from menu.menu_application_container import get_menu_query_service

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
    path="/websocket",
)
async def cart_websocket(
        websocket: WebSocket,
):
    try:

        await websocket.accept()

        retrieve_cart_request = RetrieveCartRequest.model_validate(await websocket.receive_json())

        cart_id = retrieve_cart_request.cart_id

        async with async_session_maker() as session:

            retrieve_cart_response = await find_menu_info_list(session=session, cart_id=int(cart_id))

            await websocket.send_json(retrieve_cart_response.model_dump())

            await session.close()

        while True:
            update_cart_request: UpdateCartRequest = UpdateCartRequest.model_validate(await websocket.receive_json())

            async with async_session_maker() as session:
                basket_command_service = get_basket_command_service(
                    get_basket_uow(session),
                    get_snowflake_generator()
                )

                await basket_command_service.update_basket(
                    basket_id=int(cart_id),
                    item_ids=[int(item.id) for item in update_cart_request.items],
                    counts=[int(item.count) for item in update_cart_request.items],
                )

                retrieve_cart_response = await find_menu_info_list(session=session, cart_id=int(cart_id))

                await websocket.send_json(retrieve_cart_response.model_dump())

                await session.close()

    except WebSocketDisconnect as e:
        print(f"WebSocket 종료됨 (code={e.code})")


async def find_menu_info_list(
        session: AsyncSession,
        cart_id: int,
) -> RetrieveCartResponse:
    basket_query_service = get_basket_query_service(
        basket_repository=get_basket_repository(session=session)
    )

    menu_query_service = get_menu_query_service(
        session=session
    )

    basket: Basket = await basket_query_service.retrieve_basket(cart_id)

    item_ids: list[int] = [item.id_ for item in basket.items]
    counts: list[int] = [item.count for item in basket.items]

    category_menus: list[CategoryMenu] = await menu_query_service.retrieve_menus_by_cafe_id(
        cafe_id=basket.cafe_id)

    menu_map: dict[int, Menu] = {}

    for category_menu in category_menus:
        for menu in category_menu.menus:
            menu_map[menu.id_] = menu

    return RetrieveCartResponse(
        cart_id=str(basket.id_),
        items=[ItemResponse(
            name=menu_map[int(item_id)].name,
            img=menu_map[int(item_id)].img,
            count=count
        ) for item_id, count in zip(item_ids, counts)]
    )

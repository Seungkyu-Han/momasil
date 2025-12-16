from fastapi import APIRouter, Path

from menu.menu_application_container import MenuQueryServiceDep
from menu.menu_core.models.category_menu import CategoryMenu

menu_router = APIRouter(
    prefix="/menus",
)

@menu_router.get(
    path="{/cafeId}",
)
async def retrieve_menu_by_cafe_id_api(
        cafe_id: str = Path(..., title="CafeId"),
        menu_query_service = MenuQueryServiceDep,
):
    category_menus: list[CategoryMenu] = await menu_query_service.retrieve_menus_by_cafe_id(cafe_id=cafe_id)


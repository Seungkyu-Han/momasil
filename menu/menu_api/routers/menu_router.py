from fastapi import APIRouter, Path

from menu.menu_api.dto.response.category_menu_list_response import CategoryMenuListResponse, CategoryResponse, \
    MenuResponse
from menu.menu_application_container import MenuQueryServiceDep
from menu.menu_core.models.category_menu import CategoryMenu

menu_router = APIRouter(
    prefix="/menus",
    tags=["menu"]
)

@menu_router.get(
    path="/{cafeId}",
    description="해당 카페의 카테고리와 메뉴를 조회",
)
async def retrieve_menu_by_cafe_id_api(
        menu_query_service: MenuQueryServiceDep,
        cafe_id: str = Path(..., alias="cafeId"),
) -> CategoryMenuListResponse:
    cafe_id_ = int(cafe_id)
    category_menus: list[CategoryMenu] = await menu_query_service.retrieve_menus_by_cafe_id(cafe_id=cafe_id_)

    category_menu_responses: list[CategoryResponse] = []

    for category_menu in category_menus:
        category_menu_responses.append(
            CategoryResponse(
                name=category_menu.category.name,
                sort_order=category_menu.category.sort_order,
                menus=[
                    MenuResponse(
                        id=str(menu.id_),
                        nameKr=menu.name,
                        nameEn="",
                        sortOrder=menu.sort_order,
                        img=menu.img,
                    )
                    for menu in category_menu.menus
                ]
            )
        )

    return CategoryMenuListResponse(categories=category_menu_responses)
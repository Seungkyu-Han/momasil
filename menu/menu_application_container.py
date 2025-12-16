from typing import Annotated

from fastapi import Depends

from database import SessionDep
from menu.menu_application import MenuQueryServiceImpl
from menu.menu_core import MenuQueryService
from menu.menu_infra_container import get_category_repository, get_menu_repository


def get_menu_query_service(
        session: SessionDep,
) -> MenuQueryService:
    return MenuQueryServiceImpl(
        category_repository = get_category_repository(session),
        menu_repository = get_menu_repository(session)
    )

MenuQueryServiceDep = Annotated[MenuQueryService, Depends(get_menu_query_service)]
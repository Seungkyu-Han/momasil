from typing import Annotated

from fastapi import Depends

from database import SessionDep
from menu.menu_application import MenuQueryServiceImpl
from menu.menu_core import MenuQueryService
from menu.menu_infra_container import get_category_repository, get_menu_repository


def get_menu_query_service(
        session = SessionDep,
        category_repository_factory = get_category_repository,
        menu_repository_factory = get_menu_repository,
) -> MenuQueryService:
    return MenuQueryServiceImpl(
        category_repository = category_repository_factory(session),
        menu_repository = menu_repository_factory(session)
    )

MenuQueryServiceDep = Annotated[MenuQueryService, Depends(get_menu_query_service)]
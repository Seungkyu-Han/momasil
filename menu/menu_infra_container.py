from typing import Annotated

from fastapi import Depends

from database import SessionDep
from menu.menu_core import CategoryRepository, MenuRepository, MenuUow
from menu.menu_infra import CategoryRepositoryImpl, MenuRepositoryImpl, SqlMenuUow


def get_category_repository(session: SessionDep) -> CategoryRepository:
    return CategoryRepositoryImpl(session=session)

CategoryRepositoryDep = Annotated[CategoryRepository, Depends(get_category_repository)]

def get_menu_repository(session: SessionDep) -> MenuRepository:
    return MenuRepositoryImpl(session=session)

MenuRepositoryImplDep = Annotated[MenuRepositoryImpl, Depends(get_menu_repository)]

def get_menu_uow(
        session: SessionDep,
) -> MenuUow:
    return SqlMenuUow(
        session=session,
        category_repository_factory=get_category_repository,
        menu_repository_factory=get_menu_repository,
    )

MenuUowDep = Annotated[MenuUow, Depends(get_menu_uow)]
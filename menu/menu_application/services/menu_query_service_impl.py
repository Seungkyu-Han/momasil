from menu.menu_core import MenuQueryService, CategoryRepository, MenuRepository, CategoryMenu, Category, Menu
from menu.menu_core.domains.category import Category
from collections import defaultdict
from typing import Dict


class MenuQueryServiceImpl(MenuQueryService):

    def __init__(
            self,
            category_repository: CategoryRepository,
            menu_repository: MenuRepository,
    ):
        self.category_repository = category_repository
        self.menu_repository = menu_repository

    async def retrieve_menus_by_cafe_id(self, cafe_id: int) -> list[CategoryMenu]:
        categories: list[Category] = await self.category_repository.find_by_cafe_id(cafe_id=cafe_id)
        menus: list[Menu] = await self.menu_repository.find_by_category_id_in(category_ids=[category.id_ for category in categories])

        menu_category_map: Dict[int, list[Menu]] = defaultdict(list)

        for menu in menus:
            menu_category_map[menu.category_id].append(menu)

        category_menus: list[CategoryMenu] = []

        for category in categories:
            menu_list: list[Menu] = menu_category_map.get(category.id_, [])
            category_menus.append(
                CategoryMenu(
                    category=category,
                    menus=menu_list
                )
            )

        return category_menus
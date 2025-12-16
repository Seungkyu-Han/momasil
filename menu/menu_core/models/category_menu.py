from menu.menu_core.domains.category import Category
from menu.menu_core.domains.menu import Menu


class CategoryMenu:

    def __init__(
            self,
            category: Category,
            menus: list[Menu],
    ):
        self.category = category
        self.menus = menus
from menu.menu_core import Menu
from menu.menu_infra.entities.menu_entity import MenuEntity


def to_domain(menu_entity: MenuEntity) -> Menu:
    return Menu(
        id_=menu_entity.id_,
        category_id=menu_entity.category_id,
        name=menu_entity.name,
        img=menu_entity.img,
        sort_order=menu_entity.sort_order,
    )


def to_entity(menu: Menu) -> MenuEntity:
    return MenuEntity(
        id_=menu.id_,
        category_id=menu.category_id,
        name=menu.name,
        img=menu.img,
        sort_order=menu.sort_order,
    )
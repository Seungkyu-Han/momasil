from menu.menu_core import Category
from menu.menu_infra.entities.category_entity import CategoryEntity


def to_domain(category_entity: CategoryEntity) -> Category:
    return Category(
        id_=category_entity.id_,
        name=category_entity.name,
        sort_order=category_entity.sort_order,
        cafe_id=category_entity.cafe_id,
    )

def to_entity(category: Category) -> CategoryEntity:
    return CategoryEntity(
        id_=category.id_,
        name=category.name,
        sort_order=category.sort_order,
        cafe_id=category.cafe_id,
    )
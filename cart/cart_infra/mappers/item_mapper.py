from cart.cart_core import Item
from cart.cart_infra.entities.item_entity import ItemEntity


def to_domain(item_entity: ItemEntity) -> Item:
    return Item(
        id_=item_entity.id_,
        basket_id=item_entity.basket_id,
        menu_id=item_entity.menu_id,
        count=item_entity.count,
    )


def to_entity(item: Item) -> ItemEntity:
    return ItemEntity(
        id_=item.id_,
        basket_id=item.basket_id,
        menu_id=item.menu_id,
        count=item.count,
    )
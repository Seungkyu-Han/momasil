from cart.cart_core import Basket
from cart.cart_infra.entities.basket_entity import BasketEntity
from cart.cart_infra.mappers import item_mapper


def to_domain(basket_entity: BasketEntity) -> Basket:
    return Basket(
        id_=basket_entity.id_,
        cafe_id=basket_entity.cafe_id,
        name=basket_entity.name,
        items=[item_mapper.to_domain(item_entity) for item_entity in basket_entity.item_entities],
    )


def to_entity(basket: Basket) -> BasketEntity:
    return BasketEntity(
        id_=basket.id_,
        cafe_id=basket.cafe_id,
        name=basket.name,
        item_entities=[item_mapper.to_entity(item) for item in basket.items],
    )
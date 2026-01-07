from cart.cart_core.domains.item import Item


class Basket:

    id_: int
    cafe_id: int
    name: str
    items: list[Item]

    def __init__(
            self,
            id_: int,
            cafe_id: int,
            name: str,
            items: list[Item]  | None = None
    ):
        self.id_ = id_
        self.cafe_id = cafe_id
        self.name = name
        self.items = items or []
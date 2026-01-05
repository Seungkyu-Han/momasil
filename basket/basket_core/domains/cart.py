from basket.basket_core.domains.item import Item


class Cart:

    id_: int
    cafe_id: int
    name: str
    items: list[Item]

    def __init__(
            self,
            id_: int,
            cafe_id: int,
            name: str,
            items: list[Item]
    ):
        self.id_ = id_
        self.cafe_id = cafe_id
        self.name = name
        self.items = items
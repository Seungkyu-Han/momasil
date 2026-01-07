class Item:
    id_: int
    basket_id: int
    menu_id: int
    count: int

    def __init__(
            self,
            id_: int,
            basket_id: int,
            menu_id: int,
            count: int,
    ):
        self.id_ = id_
        self.basket_id = basket_id
        self.menu_id = menu_id
        self.count = count



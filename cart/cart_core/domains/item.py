class Item:
    id_: int
    menu_id: int
    count: int

    def __init__(
            self,
            id_: int,
            menu_id: int,
            count: int,
    ):
        self.id_ = id_
        self.menu_id = menu_id
        self.count = count



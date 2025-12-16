class Menu:

    def __init__(
            self,
            id_: int,
            category_id: int,
            name: str,
            img: str,
            sort_order: int
    ):
        self.id_ = id_
        self.category_id = category_id
        self.name = name
        self.img = img
        self.sort_order = sort_order

    def __eq__(self, other):
        return isinstance(other, Menu) and self.id_ == other.id_

    def __hash__(self):
        return hash(self.id_)
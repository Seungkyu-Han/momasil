class Category:

    def __init__(
            self,
            id_: int,
            name: str,
            sort_order: int,
            cafe_id: int,
    ):
        self.id_ = id_
        self.name = name
        self.sort_order = sort_order
        self.cafe_id = cafe_id

    def __eq__(self, other):
        return isinstance(other, Category) and self.id_ == other.id_

    def __hash__(self):
        return hash(self.id_)
class Cafe:

    def __init__(
            self,
            id_: int,
            name: str,
            img: str
    ):
        self.id_ = id_
        self.name = name
        self.img = img

    def __eq__(self, other):
        if isinstance(other, Cafe):
            return self.id_ == other.id_
        return False

    def __hash__(self):
        return self.id_
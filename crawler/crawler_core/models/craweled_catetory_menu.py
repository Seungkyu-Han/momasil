class CrawledCategory:

    def __init__(self, name: str, sort_order: int):
        self.name = name
        self.sort_order = sort_order

    def __repr__(self):
        return f"name: {self.name}, sort_order: {self.sort_order}"


class CrawledMenu:

    def __init__(
            self,
            name: str,
            img: str,
            sort_order: int
    ):
        self.name = name
        self.img = img
        self.sort_order = sort_order

    def __repr__(self):
        return f"name: {self.name}, img:{self.img}, sort_order: {self.sort_order}"


class CrawledCategoryMenu:

    def __init__(self, crawled_category: CrawledCategory, crawled_menus: list[CrawledMenu]):
        self.crawled_category = crawled_category
        self.crawled_menus = crawled_menus

    def __repr__(self):

        return f"crawled_category: {self.crawled_category}, crawled_menus: [{self.crawled_menus}]"

from snowflake import SnowflakeGenerator

from cafe.cafe_core import CafeUow, Cafe
from menu.menu_core import MenuUow, Category, Menu
from crawler.crawler_core import CrawlerSyncService, CafeSymbol, CrawlerClient


class CrawlerSyncServiceImpl(CrawlerSyncService):

    def __init__(
            self,
            cafe_uow: CafeUow,
            menu_uow: MenuUow,
            mmth_crawler_client_map: dict[CafeSymbol, CrawlerClient],
            snowflake_generator: SnowflakeGenerator,
    ):
        self.cafe_uow = cafe_uow
        self.menu_uow = menu_uow
        self.mmth_crawler_client_map = mmth_crawler_client_map
        self.snowflake_generator = snowflake_generator

    def select_crawler(self, cafe_symbol: CafeSymbol) -> CrawlerClient:
        return self.mmth_crawler_client_map.get(cafe_symbol)

    async def update_cafe_menu(
            self,
            cafe_id: int,
            cafe_symbol: CafeSymbol
    ):
        cafe: Cafe = await self.cafe_uow.cafe_repository.find_by_id(id_=cafe_id)
        cafe_crawler = self.select_crawler(cafe_symbol=cafe_symbol)

        if cafe is None:
            raise Exception

        crawled_category_menus = await cafe_crawler.retrieve_menu()

        async with self.menu_uow as uow:

            categories = await self.menu_uow.category_repository.find_by_cafe_id(cafe_id)

            menus = await self.menu_uow.menu_repository.find_by_category_id_in(category_ids=[category.id_ for category in categories])

            await self.menu_uow.menu_repository.delete_all(menus)

            await self.menu_uow.category_repository.delete_by_cafe_id(cafe_id)

            for crawled_category_menu in crawled_category_menus:
                crawled_category = crawled_category_menu.crawled_category
                crawled_menus = crawled_category_menu.crawled_menus

                category = Category(
                    id_=next(self.snowflake_generator),
                    name=crawled_category.name,
                    sort_order=crawled_category.sort_order,
                    cafe_id=cafe.id_
                )

                await uow.category_repository.save(category)

                for crawled_menu in crawled_menus:
                    menu: Menu = Menu(
                        id_=next(self.snowflake_generator),
                        category_id=category.id_,
                        name=crawled_menu.name,
                        img=crawled_menu.img,
                        sort_order=crawled_menu.sort_order
                    )

                    await uow.menu_repository.save(menu)




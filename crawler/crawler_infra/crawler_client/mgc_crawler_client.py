import ssl

import aiohttp
import certifi
from bs4 import BeautifulSoup, ResultSet

from crawler.crawler_core import CrawlerClient, CrawledCategory
from crawler.crawler_core.models.craweled_catetory_menu import CrawledCategoryMenu, CrawledMenu


class MGCCrawlerClient(CrawlerClient):

    def __init__(self):
        self.BASE_URL = 'https://www.mega-mgccoffee.com'

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
        }

        self.ssl_context = ssl.create_default_context(cafile=certifi.where())


    def make_menu_url(self, category: int, page: int) -> str:
        return f'{self.BASE_URL}/menu/menu.php?page={page}&category={category}&menu_category1=1&menu_category2=1'

    async def get_category_value(self) -> list[tuple[int, str]]:
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(f'{self.BASE_URL}/menu/?menu_category1=1&menu_category2=1', ssl=self.ssl_context) as response:
                html = await response.text()
        soup = BeautifulSoup(html, "html.parser")
        checkboxes = soup.select("div.checkbox_wrap.list_checkbox")

        result: list[tuple[int, str]] = []

        for checkbox in checkboxes:
            input_tag = checkbox.find("input", {"type": "checkbox"})
            value: int = int(input_tag.get("value"))

            label_text = checkbox.find("div", class_="checkbox_text").get_text(strip=True)

            result.append((value, label_text))

        return result

    async def retrieve_menu(self) -> list[CrawledCategoryMenu]:
        crawled_category_menus: list[CrawledCategoryMenu] = []
        category_value_map: list[tuple[int, str]] = await self.get_category_value()
        menu_sort_order = 1

        for category_sort_order, category_name in category_value_map:
            crawled_menus: list[CrawledMenu] = []
            for cur_page in range(1, 100):

                async with aiohttp.ClientSession(headers=self.headers) as session:
                    async with session.get(self.make_menu_url(category=category_sort_order, page=cur_page),
                                   headers=self.headers, ssl=self.ssl_context) as response:
                        html = await response.text()

                soup = BeautifulSoup(html, "html.parser")

                items: ResultSet = soup.select('.cont_gallery_list_box')

                if len(items) == 0:
                    break

                for item in items:
                    name_kr = item.select_one('.cont_text_title b').get_text(strip=True)
                    name_en = item.select_one('.cont_text_info .text1').get_text(strip=True)
                    img = item.select_one('img')['src']

                    crawled_menus.append(CrawledMenu(name=name_kr, img=img, sort_order=menu_sort_order))

                    menu_sort_order += 1

            crawled_category = CrawledCategory(
                name=category_name,
                sort_order=category_sort_order,
            )

            crawled_category_menu = CrawledCategoryMenu(
                crawled_category=crawled_category,
                crawled_menus=crawled_menus,
            )

            crawled_category_menus.append(crawled_category_menu)

        return crawled_category_menus
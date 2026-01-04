import ssl

import aiohttp
import certifi
from bs4 import BeautifulSoup

from crawler.crawler_core import CrawlerClient, CrawledCategory
from crawler.crawler_core.models.craweled_catetory_menu import CrawledCategoryMenu, CrawledMenu


class TheVentiCrawlerClient(CrawlerClient):

    def __init__(self):
        self.BASE_URL = 'https://www.theventi.co.kr'

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
        }


        self.ssl_context = ssl.create_default_context(cafile=certifi.where())

    async def category_link_mapper(self, link: str) -> list[tuple[str, str]]:

        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(link, ssl=self.ssl_context) as response:
                html = await response.text()

        soup = BeautifulSoup(html, "html.parser")

        result: list[tuple[str, str]] = []

        for a_tag in soup.select("ul.tab.box li a"):
            name = a_tag.get_text(strip=True)
            href = a_tag.get("href")

            result.append((name, f'{link}{href}'))

        return result

    async def retrieve_menu(self) -> list[CrawledCategoryMenu]:

        category_link_map: list[tuple[str, str]] = await self.category_link_mapper(f'{self.BASE_URL}/new2022/menu/all.html')

        category_sort_order = 1
        menu_sort_order = 1
        crawled_category_menus: list[CrawledCategoryMenu] = []

        for category_name, category_url in category_link_map:

            async with aiohttp.ClientSession(headers=self.headers) as session:
                async with session.get(category_url,
                                       headers=self.headers, ssl=self.ssl_context) as response:
                    html = await response.text()

            soup = BeautifulSoup(html, "html.parser")

            crawled_menus: list[CrawledMenu] = []

            for item in soup.select("li.item"):
                img_tag = item.select_one(".img_bx img")
                img = img_tag.get('src')

                name_tag = item.select_one(".txt_bx p.tit")
                name = name_tag.get_text(strip=True) if name_tag else None

                crawled_menus.append(CrawledMenu(name=name, img=img, sort_order=menu_sort_order))
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
            category_sort_order += 1
        return crawled_category_menus
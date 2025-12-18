import ssl

import aiohttp
import certifi
from bs4 import BeautifulSoup

from crawler.crawler_core import CrawlerClient, CrawledCategoryMenu, CrawledMenu, CrawledCategory
from crawler.crawler_core.models.craweled_catetory_menu import CrawledCategoryMenu, CrawledMenu


class MMTHCrawlerClient(CrawlerClient):
    BASE_URL = 'https://mmthcoffee.com'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }

    ssl_context = ssl.create_default_context(cafile=certifi.where())

    async def retrieve_menu(self) -> list[CrawledCategoryMenu]:

        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(f'{self.BASE_URL}/sub/menu/list.html', ssl=self.ssl_context) as response:
                html = await response.text()

        soup = BeautifulSoup(html, 'html.parser')
        crawled_category_menus: list[CrawledCategoryMenu] = []

        category_sort_order = 1
        menu_sort_order = 1

        for cate_div in soup.select("div.cate"):
            category = cate_div.select_one("div.c_tit strong").text.strip()
            crawled_menus: list[CrawledMenu] = []

            for li in cate_div.select("ul.clear > li"):
                name_kr = li.select_one("div.txt_wrap strong").text.strip()
                name_en = li.select_one("div.txt_wrap p.eng").text.strip()
                img = li.select_one("div.img_wrap img")["src"]

                crawled_menus.append(CrawledMenu(name=name_kr, img=img, sort_order=menu_sort_order))

                menu_sort_order += 1

                crawled_category = CrawledCategory(name=category, sort_order=category_sort_order)

                crawled_category_menu = CrawledCategoryMenu(
                    crawled_category=crawled_category,
                    crawled_menus=crawled_menus,
                )

                crawled_category_menus.append(crawled_category_menu)

            category_sort_order += 1

        return crawled_category_menus

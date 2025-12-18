from abc import ABC

from crawler.crawler_core.output.crawler_client.crawler_client import CrawlerClient
from crawler.crawler_core.symbol.cafe_symbol import CafeSymbol


class CrawlerSyncService(ABC):

    def select_crawler(self, cafe_symbol: CafeSymbol) -> CrawlerClient:
        ...

    def update_cafe_menu(self, cafe_symbol: CafeSymbol):
        ...
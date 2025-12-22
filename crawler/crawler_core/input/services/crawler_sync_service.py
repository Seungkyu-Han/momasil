from abc import ABC, abstractmethod

from crawler.crawler_core.output.crawler_client.crawler_client import CrawlerClient
from crawler.crawler_core.symbol.cafe_symbol import CafeSymbol


class CrawlerSyncService(ABC):

    @abstractmethod
    def select_crawler(self, cafe_symbol: CafeSymbol) -> CrawlerClient:
        ...

    @abstractmethod
    async def update_cafe_menu(
            self,
            cafe_id: int,
            cafe_symbol: CafeSymbol,
    ):
        ...
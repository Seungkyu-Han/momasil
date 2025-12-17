from abc import ABC, abstractmethod

from crawler.crawler_core.models.craweled_catetory_menu import CrawledCategoryMenu


class CrawlerClient(ABC):

    @abstractmethod
    async def retrieve_menu(self) -> CrawledCategoryMenu:
        ...
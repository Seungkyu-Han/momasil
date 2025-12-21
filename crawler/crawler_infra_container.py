from typing import Annotated

from crawler.crawler_core import CrawlerClient
from crawler.crawler_infra import MMTHCrawlerClient


def get_mmth_crawler_client(
) -> CrawlerClient:
    return MMTHCrawlerClient()

MMTHCrawlerClientDep = Annotated[CrawlerClient, get_mmth_crawler_client]
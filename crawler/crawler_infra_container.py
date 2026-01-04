from functools import lru_cache
from typing import Annotated

from fastapi import Depends

from crawler.crawler_core import CrawlerClient
from crawler.crawler_infra import MMTHCrawlerClient, MGCCrawlerClient
from crawler.crawler_infra.crawler_client.mgc_crawler_client import MGCCrawlerClient


@lru_cache
def get_mmth_crawler_client(
) -> CrawlerClient:
    return MMTHCrawlerClient()

MMTHCrawlerClientDep = Annotated[CrawlerClient, Depends(get_mmth_crawler_client)]

@lru_cache
def get_mgc_crawler_client() -> CrawlerClient:
    return MGCCrawlerClient()

MGCCrawlerClientDep = Annotated[CrawlerClient, Depends(get_mgc_crawler_client)]
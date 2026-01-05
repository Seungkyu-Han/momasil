from functools import lru_cache
from typing import Annotated

from fastapi import Depends

from crawler.crawler_core import CrawlerClient
from crawler.crawler_infra import MMTHCrawlerClient, MGCCrawlerClient, TheVentiCrawlerClient, ComposeCrawlerClient


@lru_cache
def get_mmth_crawler_client(
) -> CrawlerClient:
    return MMTHCrawlerClient()

MMTHCrawlerClientDep = Annotated[CrawlerClient, Depends(get_mmth_crawler_client)]

@lru_cache
def get_mgc_crawler_client() -> CrawlerClient:
    return MGCCrawlerClient()

MGCCrawlerClientDep = Annotated[CrawlerClient, Depends(get_mgc_crawler_client)]

@lru_cache
def get_the_venti_crawler_client() -> CrawlerClient:
    return TheVentiCrawlerClient()

TheVentiCrawlerClientDep = Annotated[CrawlerClient, Depends(get_the_venti_crawler_client)]

@lru_cache
def get_compose_crawler_client() -> CrawlerClient:
    return ComposeCrawlerClient()

ComposeCrawlerClientDep = Annotated[CrawlerClient, Depends(get_compose_crawler_client)]


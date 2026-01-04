from typing import Annotated

from fastapi import Depends

from cafe.cafe_infra_container import CafeUowDep
from config.snowflake_generator import SnowflakeGeneratorDep
from crawler.crawler_core import CrawlerSyncService, CafeSymbol
from crawler.crawler_application import CrawlerSyncServiceImpl
from crawler.crawler_infra_container import MMTHCrawlerClientDep, MGCCrawlerClientDep, TheVentiCrawlerClientDep
from menu.menu_infra_container import MenuUowDep


def get_crawler_sync_service(
        cafe_uow: CafeUowDep,
        menu_uow: MenuUowDep,
        mmth_crawler_client: MMTHCrawlerClientDep,
        mgc_crawler_client: MGCCrawlerClientDep,
        the_venti_crawler_client: TheVentiCrawlerClientDep,
        snowflake_generator: SnowflakeGeneratorDep,
) -> CrawlerSyncService:
    return CrawlerSyncServiceImpl(
        cafe_uow=cafe_uow,
        menu_uow=menu_uow,
        mmth_crawler_client_map={
            CafeSymbol.MMTH: mmth_crawler_client,
            CafeSymbol.MGC: mgc_crawler_client,
            CafeSymbol.THE_VENTI: the_venti_crawler_client,
        },
        snowflake_generator=snowflake_generator,
    )

CrawlerSyncServiceDep = Annotated[CrawlerSyncService, Depends(get_crawler_sync_service)]
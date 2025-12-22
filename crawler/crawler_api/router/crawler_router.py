from fastapi import APIRouter, status, Response
from starlette.status import HTTP_204_NO_CONTENT

from crawler.crawler_api.dto.update_menu_request import UpdateMenuRequest
from crawler.crawler_application_container import CrawlerSyncServiceDep

crawler_router = APIRouter(
    prefix="/crawler",
    tags=["crawler"]
)

@crawler_router.post(
    path="",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="카페의 메뉴를 업데이트 해줍니다.",
)
async def update_menu_api(
        crawler_sync_service_dep: CrawlerSyncServiceDep,
        update_menu_request: UpdateMenuRequest,
):
    cafe_id = int(update_menu_request.cafe_id)
    await crawler_sync_service_dep.update_cafe_menu(
        cafe_id=cafe_id,
        cafe_symbol=update_menu_request.cafe_type,
    )

    return Response(status_code=HTTP_204_NO_CONTENT)
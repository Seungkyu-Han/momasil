from fastapi import APIRouter

from cafe.cafe_api.dto.resposne.cafe_list_response import CafeListResponse

cafe_router = APIRouter(
    prefix="/cafes",
)

@cafe_router.get(
    path="",
    summary="카페들의 전체 목록을 조회합니다.",
)
async def get_cafes() -> CafeListResponse:
    return CafeListResponse(
        cafes=[]
    )
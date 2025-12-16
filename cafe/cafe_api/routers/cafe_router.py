from fastapi import APIRouter, status

from cafe.cafe_api.dto.request.create_cafe_request import CreateCafeRequest
from cafe.cafe_api.dto.resposne.cafe_list_response import CafeListResponse
from cafe.cafe_api.dto.resposne.cafe_response import CafeResponse
from cafe.cafe_application_container import CafeQueryServiceDep, CafeCommandServiceDep
from cafe.cafe_core import Cafe

cafe_router = APIRouter(
    prefix="/cafes",
    tags=["cafe"]
)

@cafe_router.get(
    path="",
    summary="카페들의 전체 목록을 조회합니다.",
    status_code=status.HTTP_200_OK,
    response_model=CafeListResponse,
)
async def retrieve_cafes_apo(
        cafe_query_service: CafeQueryServiceDep,
) -> CafeListResponse:

    cafes: list[Cafe] = await cafe_query_service.find_all()

    return CafeListResponse(
        cafes=[
            CafeResponse(
                id=str(cafe.id_),
                name=cafe.name,
                img=cafe.img,
                banner=cafe.banner,
            ) for cafe in cafes
        ]
    )

@cafe_router.post(
    path="",
    summary="새로운 카페를 등록합니다",
    response_model=CafeResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_cafe_api(
        create_cafe_request: CreateCafeRequest,
        cafe_command_service: CafeCommandServiceDep,
) -> CafeResponse:

    cafe = await cafe_command_service.save(
        name=create_cafe_request.name,
        img=create_cafe_request.img,
        banner=create_cafe_request.banner,
    )

    return CafeResponse(
        id=str(cafe.id_),
        name=cafe.name,
        img=cafe.img,
        banner=cafe.banner
    )
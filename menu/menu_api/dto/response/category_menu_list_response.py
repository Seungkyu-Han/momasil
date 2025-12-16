from pydantic import BaseModel, Field


class MenuResponse(BaseModel):

    id: str = Field(..., description="메뉴 고유 아이디")
    nameKr: str = Field(..., description="메뉴 한글명")
    nameEn: str | None = Field("", description="메뉴 영문명")
    sortOrder: int = Field(..., description="메뉴 정렬 순서")
    img: str = Field(..., description="메뉴 이미지")

class CategoryResponse(BaseModel):
    name: str = Field(..., description="카테고리 명")
    sort_order: int = Field(..., description="카테고리 정렬 순서")
    menus: list[MenuResponse] = Field(..., description="해당 카테고리의 메뉴")

class CategoryMenuListResponse(BaseModel):
    categories: list[CategoryResponse] = Field(..., description="해당 카페의 카테고리")
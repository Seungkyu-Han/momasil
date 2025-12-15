from pydantic import BaseModel, Field


class CafeResponse(BaseModel):

    id: str = Field(description="해당 카페의 ID")
    name: str = Field(description="해당 카페의 이름")
    img: str = Field(description="해당 카페의 로고의 이미지")
    banner: str = Field(description="해당 카페의 배너 이미지")


from pydantic import BaseModel, Field

from cafe.cafe_api.dto.resposne.cafe_response import CafeResponse


class CafeListResponse(BaseModel):

    cafes: list[CafeResponse] = Field()
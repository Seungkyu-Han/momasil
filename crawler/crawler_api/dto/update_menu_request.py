from pydantic import BaseModel, Field

from crawler.crawler_core import CafeSymbol


class UpdateMenuRequest(BaseModel):

    cafe_id: str = Field(..., description="업데이트 할 카페 아이디")
    cafe_type: CafeSymbol = Field(..., description="크롤링 할 카페의 심볼")
from pydantic import BaseModel, Field


class CreateCartRequest(BaseModel):

    cafe_id: str = Field(..., description="카트를 생성할 카페의 아이디")

from pydantic import BaseModel, Field


class RetrieveCartRequest(BaseModel):

    cart_id: str = Field(..., description="조회할 카페의 아이디")
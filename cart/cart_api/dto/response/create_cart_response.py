from pydantic import BaseModel, Field


class CreateCartResponse(BaseModel):

    cart_id: str = Field(description="생성된 카트의 아이디")
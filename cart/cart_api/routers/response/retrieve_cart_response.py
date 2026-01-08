from pydantic import BaseModel, Field

from cart.cart_api.routers.response.item_response import ItemResponse


class RetrieveCartResponse(BaseModel):

    cart_id: str = Field(description="사용한 카트의 아이디")
    items: list[ItemResponse] = Field(...)
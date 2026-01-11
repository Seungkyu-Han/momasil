from pydantic import BaseModel, Field

from cart.cart_api.dto.request.item_request import ItemRequest


class UpdateCartRequest(BaseModel):

    items: list[ItemRequest] = Field(...)
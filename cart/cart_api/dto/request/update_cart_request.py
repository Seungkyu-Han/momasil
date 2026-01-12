from pydantic import BaseModel, Field

from cart.cart_api.dto.request.item_request import ItemRequest


class UpdateCartRequest(BaseModel):
    """
    장바구니를 업데이트하기 위한 소켓 DTO
    """

    items: list[ItemRequest] = Field(...)
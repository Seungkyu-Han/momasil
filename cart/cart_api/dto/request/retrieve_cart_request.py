from pydantic import BaseModel, Field


class RetrieveCartRequest(BaseModel):
    """
    소켓에 연결하면 바로 보내야하는 dto
    """

    cart_id: str = Field(..., description="조회할 카페의 아이디")
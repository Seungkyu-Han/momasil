from pydantic import BaseModel, Field


class CreateCafeRequest(BaseModel):
    name: str = Field(..., )
    img: str = Field(..., )
    banner: str = Field(..., )

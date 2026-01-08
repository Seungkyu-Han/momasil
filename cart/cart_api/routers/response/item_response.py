from pydantic import BaseModel, Field


class ItemResponse(BaseModel):

    name: str = Field(...)
    img: str = Field(...)
    count: int = Field(...)
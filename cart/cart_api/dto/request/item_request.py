from pydantic import BaseModel, Field


class ItemRequest(BaseModel):

    id: str = Field(...)
    count: int = Field(...)
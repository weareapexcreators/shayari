from pydantic import BaseModel
from typing import Optional


class ItemBase(BaseModel):
    text: Optional[str] = ""
    type: Optional[str] = ""
    author: Optional[str] = ""


class Item(ItemBase):
    _id: str

    class Config:
        from_attributes = True

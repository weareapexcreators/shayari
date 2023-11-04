from typing import List
from fastapi import APIRouter, HTTPException
from ..models.item import Item
from ..database import get_database
import pprint

router = APIRouter()


@router.post("/add")
def add_item():
    pass


@router.delete("/delete/{id}")
def delete_item():
    pass


@router.get("/all-item", response_model=List[Item])
async def read_item() -> List[Item]:
    db = await get_database()
    items = db.test.find()
    if items:
        res = []
        for item in await items.to_list(length=100):
            res.append(item)
        return res
    raise HTTPException(status_code=404, detail="Item not found")


@router.get("/all-item/{id}", response_model=Item)
async def read_item_id() -> Item:
    db = await get_database()
    item = await db.test.find_one({"_id": id})
    pprint.pprint(item)
    if item:
        return item
    raise HTTPException(status_code=404, detail="Item not found")

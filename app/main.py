from fastapi import FastAPI, HTTPException
from .database import create_db
from .models import Item
from .crud import (
    create_item,
    get_items,
    get_item,
    update_item,
    delete_item,
)

app = FastAPI(title="Simple CRUD API")


@app.on_event("startup")
def on_startup():
    create_db()


@app.post("/items", response_model=Item)
def add_item(item: Item):
    return create_item(item)


@app.get("/items", response_model=list[Item])
def list_items():
    return get_items()


@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    item = get_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.put("/items/{item_id}", response_model=Item)
def edit_item(item_id: int, item: Item):
    updated = update_item(item_id, item)
    if not updated:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated


@app.delete("/items/{item_id}")
def remove_item(item_id: int):
    deleted = delete_item(item_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted"}

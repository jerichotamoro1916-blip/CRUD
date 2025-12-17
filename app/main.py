from fastapi import FastAPI
from .database import create_db
from .models import Item
from .crud import create_item, get_items

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

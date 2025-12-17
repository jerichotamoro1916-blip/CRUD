from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .database import create_db
from .models import Product
from .crud import (
    create_product,
    get_products,
    get_product,
    update_product,
    delete_product,
)

app = FastAPI(title="Product CRUD API")

# 🔥 CORS (required for Angular)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    create_db()


@app.post("/products", response_model=Product)
def add_product(product: Product):
    return create_product(product)


@app.get("/products", response_model=list[Product])
def list_products():
    return get_products()


@app.get("/products/{product_id}", response_model=Product)
def read_product(product_id: int):
    product = get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@app.put("/products/{product_id}", response_model=Product)
def edit_product(product_id: int, product: Product):
    updated = update_product(product_id, product)
    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated


@app.delete("/products/{product_id}")
def remove_product(product_id: int):
    deleted = delete_product(product_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted"}

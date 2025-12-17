from sqlmodel import Session, select
from .models import Product
from .database import engine


def create_product(product: Product):
    with Session(engine) as session:
        session.add(product)
        session.commit()
        session.refresh(product)
        return product


def get_products():
    with Session(engine) as session:
        return session.exec(select(Product)).all()


def get_product(product_id: int):
    with Session(engine) as session:
        return session.get(Product, product_id)


def update_product(product_id: int, new_product: Product):
    with Session(engine) as session:
        product = session.get(Product, product_id)
        if not product:
            return None

        product.title = new_product.title
        product.price = new_product.price
        product.count = new_product.count

        session.commit()
        session.refresh(product)
        return product


def delete_product(product_id: int):
    with Session(engine) as session:
        product = session.get(Product, product_id)
        if not product:
            return None

        session.delete(product)
        session.commit()
        return True

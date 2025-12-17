from sqlmodel import Session, select
from .models import Item
from .database import engine

def create_item(item: Item):
    with Session(engine) as session:
        session.add(item)
        session.commit()
        session.refresh(item)
        return item

def get_items():
    with Session(engine) as session:
        return session.exec(select(Item)).all()

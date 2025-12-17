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




def get_item(item_id: int):
    with Session(engine) as session:
        return session.get(Item, item_id)




def update_item(item_id: int, new_item: Item):
    with Session(engine) as session:
        item = session.get(Item, item_id)
        if not item:
            return None
        item.name = new_item.name
        item.description = new_item.description
        session.add(item)
        session.commit()
        session.refresh(item)
        return item


def delete_item(item_id: int):
    with Session(engine) as session:
        item = session.get(Item, item_id)
        if not item:
            return None
        session.delete(item)
        session.commit()
        return True

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
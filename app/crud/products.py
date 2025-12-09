from sqlmodel import Session
from app.db.models import Product
#from app.models import Product

# Generic getter — list all records
def return_from_db(db: Session, modelClass):
    return db.query(modelClass).all()


# Generic getter — return single record by ID
def return_item_by_id(db: Session, model, record_id: int):
    result = db.query(model).filter(model.id == record_id).first()
    return result if result else None


def get_product_list(db: Session):
    products = return_from_db(db, Product)
    product_names = [
        product.name if product.name else None
        for product in products
    ]
    return product_names

from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session

templates = Jinja2Templates(directory="assets/templates")
router_products = APIRouter()


#from data import schemas, models
from data.db import get_db
from data.models import Product
from data.schemas import ProductSchema, ProductCreate
### Products ###

# Add Product
@router_products.post("/ingredients/", response_model=ProductSchema)
def create_ingredient(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = Product(code=product.code, name=product.name, volumeUnit=product.volumeUnit, volumeQty=product.volumeQty)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# API View Products
@router_products.get("/ingredients/", response_model=list[ProductSchema])
def list_ingredients(db: Session = Depends(get_db)):
    return db.query(Product).all()

# HTML View All Products
@router_products.get("/inventory", response_class=HTMLResponse)
def list_inventory(request: Request, db: Session = Depends(get_db)):
    #ingredients = db.query(models.Product).all()
    ingredients = [ingredient.to_dict() for ingredient in db.query(Product).all()]
    return templates.TemplateResponse("inventory.html", {"request": request, "ingredients": ingredients})
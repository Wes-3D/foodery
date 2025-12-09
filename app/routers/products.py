from fastapi import APIRouter, Request, Depends, UploadFile, File
from fastapi.responses import HTMLResponse, JSONResponse
from sqlmodel import Session
from pyzbar.pyzbar import decode
import cv2
import numpy as np
import openfoodfacts

from app.db.db import get_db
from app.db.models import Product, ProductSchema, ProductCreate
#from app.models import Product, ProductSchema, ProductCreate

food_api = openfoodfacts.API(user_agent="MyAwesomeApp/1.0", country=openfoodfacts.Country.us, timeout=10)
router_products = APIRouter()



##############################
#####     API Routes     #####
##############################


"""
curl -k -X POST "https://127.0.0.1:5000/products/" \
     -H "Content-Type: application/json" \
     -d '{"name": "Grapes", "volumeUnit": "g", "volumeQty": 8, "code": "2545433"}'
"""
# API Add Product
@router_products.post("/products/", response_model=ProductSchema)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = Product(code=product.code, name=product.name, volumeUnit=product.volumeUnit, volumeQty=product.volumeQty)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# API View Products
@router_products.get("/products/", response_model=list[ProductSchema])
def list_products(db: Session = Depends(get_db)):
    return db.query(Product).all()




##############################
#####     HTML Views     #####
##############################

# HTML View All Products
@router_products.get("/inventory", response_class=HTMLResponse)
def list_inventory(request: Request, db: Session = Depends(get_db)):
    #ingredients = [ingredient.to_dict() for ingredient in db.query(Product).all()]
    products = db.query(Product).all()
    return request.app.state.templates.TemplateResponse("products.html", {"request": request, "products": products})

# Add Product
@router_products.get("/product-add", response_class=HTMLResponse)
async def add_product(request: Request):
    return request.app.state.templates.TemplateResponse("product-scan.html", {"request": request})




##############################
#####     Scan Utils     #####
##############################

# Lookup from manual code
@router_products.post("/product-lookup")
async def lookup_code(data: dict):
    code = data.get("code")
    if not code:
        return JSONResponse({"error": "No code provided"}, status_code=400)

    product = food_api.product.get(code)
    return {"code": code, "product": product}


# Lookup from Scan Barcode
@router_products.post("/product-scan", response_class=HTMLResponse)
async def scan_product(request: Request, file: UploadFile = File(...)):
    product = None
    try:
        # Read uploaded file & Decode image
        contents = await file.read()
        image = cv2.imdecode(np.frombuffer(contents, np.uint8), cv2.IMREAD_UNCHANGED)
        barcodes = decode(image)
        if barcodes:
            # Decode first barcode found
            code_string = barcodes[0].data.decode("utf-8")
            product = food_api.product.get(code_string)
            return request.app.state.templates.TemplateResponse("product-scan.html", {"request": request, "code_string": code_string, "product": product})

        return request.app.state.templates.TemplateResponse("product-scan.html", {"request": request, "error": "Barcode not detected or is blank/corrupted!"})

    except Exception as e:
        return request.app.state.templates.TemplateResponse("product-scan.html", {"request": request, "error": f"Error: {str(e)}"})

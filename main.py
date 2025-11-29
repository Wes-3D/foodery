from fastapi import FastAPI, Request, Query, Depends, BackgroundTasks, Form, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
import uvicorn
import os
import logging

from core.log import setup_logging
from app.scan import router_scan

from data import schemas, crud, models
from data.db import get_db, SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

# Initialize logging early
setup_logging()
logger = logging.getLogger(__name__)

templates = Jinja2Templates(directory="assets/templates")
app = FastAPI()
#app.mount("/json", StaticFiles(directory="json", html=True), name="root")
app.include_router(router_scan)


@app.post("/ingredients/", response_model=schemas.Product)
def create_ingredient(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_product = models.Product(code=product.code, name=product.name, volumeUnit=product.volumeUnit, volumeQty=product.volumeQty)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product



@app.get("/ingredients/", response_model=list[schemas.Product])
def list_ingredients(db: Session = Depends(get_db)):
    return db.query(models.Product).all()




@app.post("/recipes/", response_model=schemas.Recipe)
def create_recipe(recipe: schemas.RecipeCreate, db: Session = Depends(get_db)):
    return crud.create_recipe(db=db, recipe=recipe)




@app.get("/recipes/", response_model=list[schemas.Recipe])
def read_recipes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_recipes(db, skip=skip, limit=limit)


@app.get("/recipes/{recipe_id}", response_model=schemas.Recipe)
def read_recipe(recipe_id: int, db: Session = Depends(get_db)):
    db_recipe = crud.get_recipe(db, recipe_id)
    if not db_recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return db_recipe


@app.get("/example", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("example.html", {"request": request})


if __name__ == "__main__":
    ssl_keyfile = os.path.join("assets/certs", "key.pem")
    ssl_certfile = os.path.join("assets/certs", "cert.pem")
    #uvicorn.run(app, host="0.0.0.0", port=5000)
    #uvicorn.run("app.main:app", host="0.0.0.0", port=5000, reload=True)
    uvicorn.run(app, host="0.0.0.0", port=5000, ssl_keyfile=ssl_keyfile, ssl_certfile=ssl_certfile)

from fastapi import FastAPI, Request, Query, Depends, BackgroundTasks, Form, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
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


### Ingredients ###

# Add Ingredient
@app.post("/ingredients/", response_model=schemas.Product)
def create_ingredient(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_product = models.Product(code=product.code, name=product.name, volumeUnit=product.volumeUnit, volumeQty=product.volumeQty)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# API View Ingredients
@app.get("/ingredients/", response_model=list[schemas.Product])
def list_ingredients(db: Session = Depends(get_db)):
    return db.query(models.Product).all()

# HTML View All Ingredients
@app.get("/inventory", response_class=HTMLResponse)
def read_pantry(request: Request, db: Session = Depends(get_db)):
    #ingredients = db.query(models.Product).all()
    ingredients = [ingredient.to_dict() for ingredient in db.query(models.Product).all()]
    return templates.TemplateResponse("inventory.html", {"request": request, "ingredients": ingredients})

### Recipes ###

# Post Recipe
@app.post("/recipes/", response_model=schemas.Recipe)
def create_recipe(recipe: schemas.RecipeCreate, db: Session = Depends(get_db)):
    return crud.create_recipe(db=db, recipe=recipe)

# Add Recipe
@app.get("/recipe-add", response_class=HTMLResponse)
def recipe_form(request: Request):
    return templates.TemplateResponse("recipe-add.html", {"request": request})

@app.post("/recipes/create")
def create_recipe(
    request: Request,
    name: str = Form(...),
    description: str = Form(""),
    servings: int = Form(...),
    ingredient_id: list[int] = Form([]),
    quantity: list[float] = Form([]),
    step_number: list[int] = Form([]),
    step_description: list[str] = Form([]),
    db: Session = Depends(get_db),
):

    recipe = models.Recipe(name=name, description=description, servings=servings)
    db.add(recipe)
    db.commit()
    db.refresh(recipe)

    # Add ingredients
    for i_id, qty in zip(ingredient_id, quantity):
        ri = models.RecipeIngredient(
            recipe_id=recipe.id,
            ingredient_id=i_id,
            quantity=qty
        )
        db.add(ri)

    # Add steps
    for num, desc in zip(step_number, step_description):
        step = models.RecipeStep(
            recipe_id=recipe.id,
            step_number=num,
            description=desc
        )
        db.add(step)

    db.commit()

    return RedirectResponse(url=f"/recipes/{recipe.id}", status_code=303)

# API View All Recipes
@app.get("/recipes/", response_model=list[schemas.Recipe])
def read_recipes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_recipes(db, skip=skip, limit=limit)


# API View Recipe
@app.get("/recipes/{recipe_id}", response_model=schemas.Recipe)
def read_recipe(recipe_id: int, db: Session = Depends(get_db)):
    db_recipe = crud.get_recipe(db, recipe_id)
    if not db_recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return db_recipe

# HTML View All Recipes
@app.get("/cookbook", response_class=HTMLResponse)
def read_cookbook(request: Request, db: Session = Depends(get_db)):
    #recipes = crud.get_recipes(db)
    recipes = [recipe.to_dict() for recipe in crud.get_recipes(db)]
    return templates.TemplateResponse("cookbook.html", {"request": request, "recipes": recipes})


### Squirrelf AI Example ###
@app.get("/example", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("example.html", {"request": request})

if __name__ == "__main__":
    ssl_keyfile = os.path.join("assets/certs", "key.pem")
    ssl_certfile = os.path.join("assets/certs", "cert.pem")
    #uvicorn.run(app, host="0.0.0.0", port=5000)
    #uvicorn.run("app.main:app", host="0.0.0.0", port=5000, reload=True)
    uvicorn.run(app, host="0.0.0.0", port=5000, ssl_keyfile=ssl_keyfile, ssl_certfile=ssl_certfile)

from fastapi import APIRouter, Request, Depends, Form, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session


templates = Jinja2Templates(directory="assets/templates")
router_recipes = APIRouter()


from app.data.db import get_db
from app.data import models, schemas, crud
### Recipes ###

# Post Recipe
@router_recipes.post("/recipes/", response_model=schemas.RecipeSchema)
def create_recipe(recipe: schemas.RecipeCreate, db: Session = Depends(get_db)):
    return crud.create_recipe(db=db, recipe=recipe)

# Add Recipe
@router_recipes.get("/recipe-add", response_class=HTMLResponse)
def recipe_form(request: Request):
    return templates.TemplateResponse("recipe-add.html", {"request": request})

@router_recipes.post("/recipes/create")
def create_recipe_form(
    request: Request,
    name: str = Form(...),
    description: str = Form(""),
    servings: int = Form(...),
    #ingredient_id: list[int] = Form([]),
    ingredient_quantity: list[float] = Form([]),
    ingredient_name: list[str] = Form([]),
    ingredient_unit: list[str] = Form([]),
    ingredient_method: list[str] = Form([]),

    step_number: list[int] = Form([]),
    step_description: list[str] = Form([]),
    db: Session = Depends(get_db),
):

    recipe = models.Recipe(name=name, description=description, servings=servings)
    db.add(recipe)
    db.commit()
    db.refresh(recipe)

    # Add ingredients
    #for i_id, qty in zip(ingredient_id, quantity):
    for qty, name, unit, method in zip(ingredient_quantity, ingredient_name, ingredient_unit, ingredient_method):
        ri = models.RecipeIngredient(
            recipe_id=recipe.id,
            #ingredient_id=i_id,
            quantity=qty,
            name=name,
            unit=unit,
            method=method
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
@router_recipes.get("/recipes/", response_model=list[schemas.RecipeSchema])
def read_recipes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_recipes(db, skip=skip, limit=limit)


# API View Recipe
@router_recipes.get("/recipes/{recipe_id}", response_model=schemas.RecipeSchema)
def read_recipe(recipe_id: int, db: Session = Depends(get_db)):
    db_recipe = crud.get_recipe(db, recipe_id)
    if not db_recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return db_recipe

# HTML View All Recipes
@router_recipes.get("/cookbook", response_class=HTMLResponse)
def list_recipes(request: Request, db: Session = Depends(get_db)):
    #recipes = crud.get_recipes(db)
    recipes = [recipe.to_dict() for recipe in crud.get_recipes(db)]
    return templates.TemplateResponse("recipes.html", {"request": request, "recipes": recipes})
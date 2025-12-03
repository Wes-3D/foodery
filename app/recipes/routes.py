from fastapi import APIRouter, Request, Depends, Form, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session


templates = Jinja2Templates(directory="assets/templates")
router_recipes = APIRouter()


from app.data.db import get_db
from app.data import models
from app.recipes import crud
### Recipes ###

# Post Recipe
"""
curl -k -X POST "https://127.0.0.1:5000/recipes/" \
     -H "Content-Type: application/json" \
     -d '{
  "name": "Eggy Toast",
  "description": "Fried egg inside toast AKA toad in a hole",
  "servings": 2,
  "ingredients": [
    {"name": "bread", "quantity": 1, "unit": "unit", "method": ""},
    {"name": "eggs", "quantity": 1, "unit": "unit", "method": ""}
  ],
  "steps": [
    {"step_number": 1, "description": "Cut hole in bread."},
    {"step_number": 2, "description": "Fry egg in middle."}
  ]
}'
"""
@router_recipes.post("/recipes/", response_model=models.RecipeSchema)
def create_recipe_route(recipe: models.RecipeCreate, db: Session = Depends(get_db)):
    return crud.create_recipe(db=db, recipe=recipe)

"""
curl -k -X POST "https://127.0.0.1:5000/recipe-delete/1"
"""
@router_recipes.post("/recipe-delete/{recipe_id}", status_code=204)
def delete_recipe_route(recipe_id: int, db: Session = Depends(get_db)):
    return crud.delete_recipe(db=db, recipe_id=recipe_id)

# Add Recipe
@router_recipes.get("/recipe-add", response_class=HTMLResponse)
def recipe_form(request: Request):
    return templates.TemplateResponse("recipe-add.html", {"request": request})

@router_recipes.post("/recipes/create")
def create_recipe_form_route(
    request: Request,
    name: str = Form(...),
    description: str = Form(""),
    servings: int = Form(...),
    #ingredient_id: list[int] = Form([]),
    ing_qty: list[float] = Form([]),
    ing_name: list[str] = Form([]),
    ing_unit: list[str] = Form([]),
    ing_method: list[str] = Form([]),

    step_num: list[int] = Form([]),
    step_desc: list[str] = Form([]),
    db: Session = Depends(get_db),
):

    crud.create_recipe_form(
        db=db,
        name=name,
        description=description,
        servings=servings,
        #ingredient_id: list[int] = Form([]),
        ing_qty=ing_qty,
        ing_name=ing_name,
        ing_unit=ing_unit,
        ing_method=ing_method,
        step_num=step_num,
        step_desc=step_desc
    )

    return RedirectResponse(url=f"/cookbook", status_code=303) #/{recipe.id}

# API View All Recipes
@router_recipes.get("/recipes/", response_model=list[models.RecipeSchema])
def read_recipes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_recipes(db, skip=skip, limit=limit)


# API View Recipe
@router_recipes.get("/recipes/{recipe_id}", response_model=models.RecipeSchema)
def read_recipe(recipe_id: int, db: Session = Depends(get_db)):
    db_recipe = crud.get_recipe(db, recipe_id)
    if not db_recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return db_recipe

# HTML View All Recipes
@router_recipes.get("/cookbook", response_class=HTMLResponse)
def list_recipes(request: Request, db: Session = Depends(get_db)):
    recipes = crud.get_recipes(db)
    return templates.TemplateResponse("recipes.html", {"request": request, "recipes": recipes})
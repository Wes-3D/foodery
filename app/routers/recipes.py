from fastapi import APIRouter, Request, Depends, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session

from app.db.db import get_db
from app.db.models import RecipeCreate, RecipeSchema, RecipeCreate, RecipeIngredient, RecipeStep
from app.crud.recipes import create_recipe, create_recipe_form, get_recipe, get_recipes, delete_recipe
from app.crud.units import get_display_units

router_recipes = APIRouter()

##############################
#####     API Routes     #####
##############################

# API View All Recipes
@router_recipes.get("/recipes/", response_model=list[RecipeSchema])
def read_recipes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_recipes(db, skip=skip, limit=limit)

# API View Recipe
@router_recipes.get("/recipes/{recipe_id}", response_model=RecipeSchema)
def read_recipe(recipe_id: int, db: Session = Depends(get_db)):
    db_recipe = get_recipe(db, recipe_id)
    if not db_recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return db_recipe

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
# API Post Recipe 
@router_recipes.post("/recipes/", response_model=RecipeSchema)
def create_recipe_route(recipe: RecipeCreate, db: Session = Depends(get_db)):
    return create_recipe(db=db, recipe=recipe)

"""
curl -k -X POST "https://127.0.0.1:5000/recipe-delete/1"
"""
# API Delete Recipe 
@router_recipes.post("/recipe-delete/{recipe_id}", status_code=204)
def delete_recipe_route(recipe_id: int, db: Session = Depends(get_db)):
    return delete_recipe(db=db, recipe_id=recipe_id)



##############################
#####     HTML Views     #####
##############################

# Add Recipe Form
@router_recipes.get("/recipe-add", response_class=HTMLResponse)
def recipe_form(request: Request, db: Session = Depends(get_db)):
    display_units = get_display_units(db)
    return request.app.state.templates.TemplateResponse("recipe-add.html", {"request": request, "display_units": display_units})

# Save Recipe Form
@router_recipes.post("/recipes/create")
def create_recipe_form_route(
    request: Request,
    name: str = Form(...),
    description: str = Form(""),
    image: str = Form(...),
    source: str = Form(...),
    category: str = Form(...),
    servings: int = Form(...),
    time_prep: int = Form(...),
    time_cook: int = Form(...),
    time_total: int = Form(...),
    #ingredient_id: list[int] = Form([]),
    ing_qty: list[float] = Form([]),
    ing_name: list[str] = Form([]),
    ing_unit: list[str] = Form([]),
    ing_method: list[str] = Form([]),

    step_num: list[int] = Form([]),
    step_desc: list[str] = Form([]),
    db: Session = Depends(get_db),
):

    create_recipe_form(
        db=db,
        name=name,
        description=description,
        image=image,
        source=source,
        category=category,
        servings=servings,
        time_prep=time_prep,
        time_cook=time_cook,
        time_total=time_total,
        ing_qty=ing_qty,
        ing_name=ing_name,
        ing_unit=ing_unit,
        ing_method=ing_method,
        step_num=step_num,
        step_desc=step_desc
    )

    return RedirectResponse(url=f"/cookbook", status_code=303) #/{recipe.id}


# HTML View All Recipes
@router_recipes.get("/cookbook", response_class=HTMLResponse)
def list_recipes(request: Request, db: Session = Depends(get_db)):
    recipes = get_recipes(db)
    return request.app.state.templates.TemplateResponse("recipes.html", {"request": request, "recipes": recipes})

# HTML View Recipe Details
@router_recipes.get("/cookbook/{recipe_id}", response_class=HTMLResponse)
def view_recipe(recipe_id: int, request: Request, db: Session = Depends(get_db)):
    recipe = get_recipe(db, recipe_id)
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    
    ingredients = db.query(RecipeIngredient).filter(RecipeIngredient.recipe_id == recipe_id).all()
    steps = db.query(RecipeStep).filter(RecipeStep.recipe_id == recipe_id).order_by(RecipeStep.step_number).all()

    return request.app.state.templates.TemplateResponse("recipe-details.html", {"request": request, "recipe": recipe, "ingredients": ingredients, "steps": steps})


# Scrape Recipe Form
@router_recipes.get("/recipe-scrape", response_class=HTMLResponse)
def recipe_scrape(request: Request):
    return request.app.state.templates.TemplateResponse("alt/recipe-scrape.html", {"request": request})


from fastapi import Query
from recipe_scrapers import scrape_me

@router_recipes.get("/scrape")
def scrape_recipe(url: str = Query(..., description="URL of a recipe page")):
    try:
        scraper = scrape_me(url)
        recipe_json = scraper.to_json()
        return recipe_json

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
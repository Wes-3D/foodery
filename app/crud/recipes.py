from fastapi import HTTPException, Form
from sqlalchemy.orm import Session
from recipe_scrapers import scrape_me

from app.db.models import Recipe, RecipeCreate, RecipeIngredient, RecipeStep, Product


def get_recipe(db: Session, recipe_id: int):
    return db.query(Recipe).filter(Recipe.id == recipe_id).first()


def get_recipes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Recipe).offset(skip).limit(limit).all()


def delete_recipe(db: Session, recipe_id: int):
    # Fetch the recipe
    recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()

    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")

    # Delete related steps and ingredients first
    db.query(RecipeStep).filter(RecipeStep.recipe_id == recipe_id).delete()
    db.query(RecipeIngredient).filter(RecipeIngredient.recipe_id == recipe_id).delete()

    # Delete the recipe
    db.delete(recipe)
    db.commit()

    return

def get_or_create_ingredient(db: Session, name: str):
    ingredient = (db.query(Product).filter(Product.name.ilike(name)).first())

    if ingredient:
        return ingredient

    ingredient = Product(name=name)
    db.add(ingredient)
    db.commit()
    db.refresh(ingredient)
    return ingredient


def create_recipe(db: Session, recipe: RecipeCreate):
    db_recipe = Recipe(
        name=recipe.name,
        description=recipe.description,
        image=recipe.image,
        source=recipe.source,
        category=recipe.category,
        servings=recipe.servings,
        time_prep=recipe.time_prep,
        time_cook=recipe.time_cook,
        time_total=recipe.time_total,
    )
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)

    # Add ingredients
    for item in recipe.ingredients:
        product_ingredient = get_or_create_ingredient(db, item.name)
        db_ri = RecipeIngredient(recipe_id=db_recipe.id, product_id=product_ingredient.id, quantity=item.quantity, name=item.name, unit=item.unit, method=item.method)
        db.add(db_ri)

    # Add steps
    for step in recipe.steps:
        db_step = RecipeStep(recipe_id=db_recipe.id, step_number=step.step_number, description=step.description)
        db.add(db_step)

    db.commit()
    db.refresh(db_recipe)
    return db_recipe


## Scraper
RECIPE1 = "https://www.food.com/recipe/my-copycat-shrimp-paesano-64300"
RECIPE2 = "https://www.allrecipes.com/recipe/158968/spinach-and-feta-turkey-burgers/"

def scrape_recipe_url(url=RECIPE2):
    scraper = scrape_me(url)
    #help(scraper) ## for a complete list of methods:
    #recipe_title = scraper.title()
    #recipe_instructions = scraper.instructions()
    recipe_json = scraper.to_json()

    #print(recipe_json)
    return recipe_json


# Removed 2nd HTML form route, added javascript route to form
"""
def create_recipe_form(
    db: Session,
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
):

    recipe = Recipe(
        name=name, 
        description=description,
        image=image,
        source=source,
        category=category,
        servings=servings,
        time_prep=time_prep,
        time_cook=time_cook,
        time_total=time_total
        )
    db.add(recipe)
    db.commit()
    db.refresh(recipe)

    # Add ingredients
    for qty, name, unit, method in zip(ing_qty, ing_name, ing_unit, ing_method):
        product_ingredient = get_or_create_ingredient(db, name)
        ri = RecipeIngredient(recipe_id=recipe.id, product_id=product_ingredient.id, quantity=qty, name=name, unit=unit, method=method) #ing_id=ing_id,
        db.add(ri)

    # Add steps
    for num, desc in zip(step_num, step_desc):
        step = RecipeStep(recipe_id=recipe.id, step_number=num, description=desc)
        db.add(step)

    db.commit()
"""
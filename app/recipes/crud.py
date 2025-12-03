from fastapi import HTTPException, Form
from sqlalchemy.orm import Session
from app.data import models

def get_recipe(db: Session, recipe_id: int):
    return db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()

def get_recipes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Recipe).offset(skip).limit(limit).all()

def create_recipe(db: Session, recipe: models.RecipeCreate):
    db_recipe = models.Recipe(
        name=recipe.name,
        description=recipe.description,
        servings=recipe.servings,
        time_prep=recipe.time_prep,
        time_cook=recipe.time_cook,
    )
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)

    # Add ingredients
    for item in recipe.ingredients:
        db_ri = models.RecipeIngredient(
            recipe_id=db_recipe.id,
            #ingredient_id=item.ingredient_id,
            quantity=item.quantity,
            name=item.name,
            unit=item.unit,
            method=item.method
        )
        db.add(db_ri)

    # Add steps
    for step in recipe.steps:
        db_step = models.RecipeStep(
            recipe_id=db_recipe.id,
            step_number=step.step_number,
            description=step.description
        )
        db.add(db_step)

    db.commit()
    db.refresh(db_recipe)
    return db_recipe




def delete_recipe(db: Session, recipe_id: int):
    # Fetch the recipe
    recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()

    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")

    # Delete related steps and ingredients first
    db.query(models.RecipeStep).filter(models.RecipeStep.recipe_id == recipe_id).delete()
    db.query(models.RecipeIngredient).filter(models.RecipeIngredient.recipe_id == recipe_id).delete()

    # Delete the recipe
    db.delete(recipe)
    db.commit()

    return





def create_recipe_form(
    db: Session,
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
):

    recipe = models.Recipe(name=name, description=description, servings=servings)
    db.add(recipe)
    db.commit()
    db.refresh(recipe)

    # Add ingredients
    for qty, name, unit, method in zip(ing_qty, ing_name, ing_unit, ing_method):
        ri = models.RecipeIngredient(recipe_id=recipe.id, quantity=qty, name=name, unit=unit, method=method) #ingredient_id=i_id,
        db.add(ri)

    # Add steps
    for num, desc in zip(step_num, step_desc):
        step = models.RecipeStep(recipe_id=recipe.id, step_number=num, description=desc)
        db.add(step)

    db.commit()


"""
def get_or_create_ingredient(db: Session, name: str):
    ingredient = (
        db.query(models.Product)
        .filter(models.Product.name.ilike(name))
        .first()
    )

    if ingredient:
        return ingredient

    ingredient = models.Product(name=name)
    db.add(ingredient)
    db.commit()
    db.refresh(ingredient)
    return ingredient
"""
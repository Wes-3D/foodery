from sqlalchemy.orm import Session
from data import models, schemas

def get_recipe(db: Session, recipe_id: int):
    return db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()

def get_recipes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Recipe).offset(skip).limit(limit).all()

def create_recipe(db: Session, recipe: schemas.RecipeCreate):
    db_recipe = models.Recipe(
        name=recipe.name,
        description=recipe.description,
        servings=recipe.servings,
    )
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)

    # Add ingredients
    for item in recipe.ingredients:
        db_ri = models.RecipeIngredient(
            recipe_id=db_recipe.id,
            ingredient_id=item.ingredient_id,
            quantity=item.quantity
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

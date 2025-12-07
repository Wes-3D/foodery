import json
from sqlalchemy.orm import Session
from app.db.db import SessionLocal, engine
from app.db import models

def import_ingredients_from_json(json_path: str):
    db: Session = SessionLocal()

    with open(json_path, "r") as f:
        data = json.load(f)


    foods = data.get("FoundationFoods")
    count = 0
    for item in foods:
        name = item.get("description")
        if not name:
            continue

        # Get the first foodPortion for unit and gram weight
        volumeUnit = "unit"
        gram_weight = None
        portions = item.get("foodPortions", [])
        if portions and "measureUnit" in portions[0]:
            volumeUnit = portions[0]["measureUnit"].get("name", "unit")
            volumeQty = portions[0]["measureUnit"].get("amount", 1)
            gram_weight = float(portions[0].get("gramWeight"))

        category = item.get("foodCategory", {}).get("description")
        fdc_id = item.get("fdcId")

        # Skip duplicates
        if db.query(models.Product).filter_by(name=name).first():
            continue

        ingredient = models.Product(
            code=fdc_id,
            name=name,
            volumeUnit=volumeUnit,
            volumeQty=volumeQty,
            weightGram=gram_weight,
            category=category
        )
        db.add(ingredient)
        count += 1

    db.commit()
    db.close()
    print(f"Imported {count} ingredients.")




def import_foods_tandoor(json_path: str):
    db: Session = SessionLocal()

    with open(json_path, "r") as f:
        data = json.load(f)


    foods = data.get("FoundationFoods")
    count = 0
    for item in foods:
        name = item.get("description")
        if not name:
            continue

        # Get the first foodPortion for unit and gram weight
        volumeUnit = "unit"
        gram_weight = None
        portions = item.get("foodPortions", [])
        if portions and "measureUnit" in portions[0]:
            volumeUnit = portions[0]["measureUnit"].get("name", "unit")
            volumeQty = portions[0]["measureUnit"].get("amount", 1)
            gram_weight = float(portions[0].get("gramWeight"))

        category = item.get("foodCategory", {}).get("description")
        fdc_id = item.get("fdcId")

        # Skip duplicates
        if db.query(models.Product).filter_by(name=name).first():
            continue

        ingredient = models.Product(
            code=fdc_id,
            name=name,
            volumeUnit=volumeUnit,
            volumeQty=volumeQty,
            weightGram=gram_weight,
            category=category
        )
        db.add(ingredient)
        count += 1

    db.commit()
    db.close()
    print(f"Imported {count} ingredients.")


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python import_ingredients.py <path_to_json>")
        sys.exit(1)
    import_ingredients_from_json(sys.argv[1])

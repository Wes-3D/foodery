
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
from sqlmodel import Session, select

from app.db.models import User, UserCreate, MeasureUnit, Product
from app.crud.user import create_user
from assets.data.units.mealie_units import measure_units
from assets.data.products.tandoor_foods import tandoor_json

def seed_admin(db: Session, settings) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next lines
    # from sqlmodel import SQLModel

    # This works because the models are already imported and registered from app.models
    # SQLModel.metadata.create_all(engine)

    user = db.exec(select(User).where(User.email == settings.FIRST_SUPERUSER)).first()
    if not user:
        user_in = UserCreate(email=settings.FIRST_SUPERUSER, password=settings.FIRST_SUPERUSER_PASSWORD, is_superuser=True)
        user = create_user(session=db, user_create=user_in)





def upsert_measurement_unit(db: Session, key: str, unit_data: dict):
    db_unit = db.query(MeasureUnit).filter(MeasureUnit.key == key).first()

    if db_unit:
        # update existing
        for k, v in unit_data.items():
            setattr(db_unit, k, v)
    else:
        db_unit = MeasureUnit(key=key, **unit_data)
        db.add(db_unit)

    db.commit()
    db.refresh(db_unit)
    return db_unit


def seed_measure_units(db: Session):
    db_unit = db.query(MeasureUnit).all()

    if db_unit:
        return

    for key, unit_data in measure_units.items():
        upsert_measurement_unit(db, key, unit_data)

    return


def seed_products_tandoor(db: Session):
    foods = tandoor_json.get("data")
    count = 0
    for food_id, food in foods.items():
        props = food["properties"]
        name = food_id.removeprefix("food-").replace("-"," ")
        category = food.get("store_category", "").removeprefix("category-").replace("-"," ")
        fdc_id = food.get("fdc_id", "")
        # Get the first foodPortion for unit and gram weight
        #volumeUnit = "unit"
        volumeUnit = props.get("food_unit", "")
        #volumeQty = food.get("food_amount", 1)
        gram_weight = props.get("food_amount", 1)

        # Skip duplicates
        if db.query(Product).filter_by(name=name).first():
            continue

        ingredient = Product(
            code=fdc_id,
            name=name,
            volumeUnit=volumeUnit,
            volumeQty=1,
            weightGram=gram_weight,
            category=category
        )
        db.add(ingredient)
        count += 1

    db.commit()
    db.close()
    print(f"Imported {count} ingredients.")
    #print(f"Foods: {foods}")

    """
    """
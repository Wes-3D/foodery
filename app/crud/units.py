from sqlmodel import Session
from app.db.models import MeasureUnit
#from app.models import MeasureUnit

def get_display_units(db: Session):
    units = db.query(MeasureUnit).all()

    display_units = [
        unit.abbreviation if unit.abbreviation else unit.name
        for unit in units
    ]

    return display_units
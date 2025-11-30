import openfoodfacts
from openfoodfacts import Country


def get_food_api():
    return openfoodfacts.API(user_agent="MyAwesomeApp/1.0", country=Country.us, timeout=10)

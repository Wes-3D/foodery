import openfoodfacts
from openfoodfacts import Country

# User-Agent is mandatory
food_api = openfoodfacts.API(user_agent="MyAwesomeApp/1.0", country=Country.us, timeout=10)
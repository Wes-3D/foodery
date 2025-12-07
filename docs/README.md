**[Products](products.md)** (or Pantry/Ingredients)
- keep track of inventory
- need empty list to match from
- nutrient information
- populate from barcode scanner


**[Recipes](recipes.md)**
- add recipe from manual form
- scrape from url (parse ingredient list & amounts) - [scraper](scraper.md)
- show available recipes from current pantry
- scale recipe to pantry or serving needs


**Meal Plan**
- need category/keyword/diet tags to create


## Functions
- crud/recipes.py
    - get_recipe
    - get_recipes
    - delete_recipe
    - create_recipe
    - create_recipe_form
    - get_or_create_ingredient
    - scrape_recipe_url

- crud/products.py

- crud/user.py

- crud/units.py
    - get_display_units


## Cleanup

- RecipeCreate: 
    - separate functions for accepting HTML form and JSON
    - can they be combined into 1 route or need to stay separate?

- add attributes to Recipe
- templates, settings in app 'request' state
- deleteRecipe function & refresh to page


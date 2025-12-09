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


## Functions/Code

### Main
- HTML
    - index
    - example
- API
    - docs
    - redoc


### Products
- HTML
    - list_inventory /inventory
    - add_product /product-add
    - scan_product /product-scan
- API
    - create_product /products/ POST
    - list_products /products/ GET
    - lookup_code /product-lookup

- CRUD
    - **return_from_db**s
    - **return_item_by_id**
    - get_product_list
        - /routers/recipes.recipe_form

### Recipes

HTML
- list_recipes /cookbook
    - CRUD get_recipes
- view_recipe /cookbook/{recipe_id}
    - CRUD get_recipe
- recipe_form /recipe-add
    - CRUD get_product_list
    - CRUD get_display_units
- recipe_scrape /recipe-scrape

API
- read_recipes /recipes/ GET
    - CRUD get_recipes
- read_recipe /recipes/{recipe_id}
    - CRUD get_recipe
- create_recipe_route /recipes/ POST
    - CRUD create_recipe
- delete_recipe_route /recipe-delete/{recipe_id}
    - CRUD delete_recipe
- scrape_recipe_url /scrape/{url}

- CRUD
    - get_recipe
        - /routers/recipes.read_recipe(recipe_id)
        - /routers/recipes.view_recipe(recipe_id)
    - get_recipes
        - /routers/recipes.list_recipes
        - /routers/recipes.read_recipes
    - delete_recipe
        - /routers/recipes.delete_recipe_route
    - create_recipe
        - /routers/recipes.create_recipe_route
        - get_or_create_ingredient
    - *scrape_recipe_url*


### Units
- CRUD
    - get_display_units
        - /routers/recipes.recipe_form


### User
- CRUD
    - create_user
        - /db/seed.py


## Cleanup

- add attributes to Recipe
- templates, settings in app 'request' state
- deleteRecipe function & refresh to page


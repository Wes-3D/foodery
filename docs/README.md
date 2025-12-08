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


## Routes
- main
    - HTML
        - index
        - example
    - API
        - docs
        - redoc
- products
    - HTML
        - list_inventory /inventory
        - add_product /product-add
        - scan_product /product-scan
    - API
        - create_product /products/ POST
        - list_products /products/ GET
        - lookup_code /product-lookup
- recipes
    - HTML
        - list_recipes /cookbook
        - view_recipe /cookbook/{recipe_id}
        - recipe_form /recipe-add
        - recipe_scrape /recipe-scrape
    - API
        - read_recipes /recipes/ GET
        - read_recipe /recipes/{recipe_id}
        - create_recipe_route /recipes/ POST
        - delete_recipe_route /recipe-delete/{recipe_id}
        - scrape_recipe_url /scrape/{url}


## Functions
- recipes
    - get_recipe
        - /routers/recipes.py
    - get_recipes
        - /routers/recipes.py
    - delete_recipe
        - /routers/recipes.py
    - create_recipe
        - /routers/recipes.py
        - get_or_create_ingredient
    - *scrape_recipe_url*

- products
    - **return_from_db**s
    - **return_item_by_id**
    - get_product_list
        - /routers/recipes.py

- units
    - get_display_units
        - /routers/recipes.py

- user
    - create_user
        - /db/seed.py


## Cleanup

- RecipeCreate: 
    - separate functions for accepting HTML form and JSON
    - can they be combined into 1 route or need to stay separate?

- add attributes to Recipe
- templates, settings in app 'request' state
- deleteRecipe function & refresh to page


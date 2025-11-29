## Recipe Functions
- Step by step recipe method
- Make notes against a recipe
- Convert ingredient units (e.g. oz to grams)
- Alter the servings for any recipe

## Recipe Formats
https://schema.org/Recipe

- cookTime:
    - Duration
    - The time it takes to actually cook the dish, in ISO 8601 duration format.
- cookingMethod
    - Text
    - The method of cooking, such as Frying, Steaming, ...
- nutrition
 	- NutritionInformation
    - Nutrition information about the recipe or menu item.
- recipeCategory
    - Text
    - The category of the recipe—for example, appetizer, entree, etc.
- recipeCuisine
    - Text
    - The cuisine of the recipe (for example, French or Ethiopian).
- recipeIngredient
    - ItemList  or PropertyValue  or Text
    - An ingredient or ordered list of ingredients and potentially quantities used in the recipe, e.g. 1 cup of sugar, flour or garlic.
    - The ingredients can be represented as free text or more structured values.
- recipeInstructions
    - CreativeWork  or ItemList  or Text
    - A step in making the recipe, in the form of a single item (document, video, etc.) or an ordered list with HowToStep and/or HowToSection items.
- recipeYield
    - QuantitativeValue  or Text
    - The quantity produced by the recipe (for example, number of people served, number of servings, etc).
- suitableForDiet
    - RestrictedDiet
    - Indicates a dietary restriction or guideline for which this recipe or menu item is suitable, e.g. diabetic, halal etc.

- estimatedCost
    - MonetaryAmount  or Text
    - The estimated cost of the supply or supplies consumed when performing instructions.
- performTime
    - Duration
    - The length of time it takes to perform instructions or a direction (not including time to prepare the supplies), in ISO 8601 duration format.
- prepTime
    - Duration
    - The length of time it takes to prepare the items to be used in instructions or a direction, in ISO 8601 duration format.
- step
    - CreativeWork  or HowToSection  or HowToStep  or Text
    - A single step item (as HowToStep, text, document, video, etc.) or a HowToSection. Supersedes steps.
- supply
    - HowToSupply  or Text
    - A sub-property of instrument. A supply consumed when performing instructions or a direction.
- tool
    - HowToTool  or Text
    - A sub property of instrument. An object used (but not consumed) when performing instructions or a direction.
- totalTime
    - Duration
    - The total time required to perform instructions or a direction (including time to prepare the supplies), in ISO 8601 duration format.
- yield
    - QuantitativeValue  or Text
    - The quantity that results by performing instructions. For example, a paper airplane, 10 personalized candles. 

## Scrapers
https://github.com/hhursev/recipe-scrapers



"""
{
'site_name': 'Food.com',
'host': 'food.com',
'canonical_url': 'https://www.food.com/recipe/my-copycat-shrimp-paesano-64300',
'image': 'https://img.sndimg.com/food/image/upload/q_92,fl_progressive,w_1200,c_scale/v1/img/recipes/64/30/0/489JmgiQu2QEdDjkMX3a_DSC05268-2.jpg',
'title': 'My Copycat Shrimp Paesano',

'description': "This is my copycat version of Paesano's Restaurant signature dish. You will love this garlic shrimp dish. Paesano's Restaurant is on the Riverwalk in San Antonio, Texas.",
'author': 'Miss Annie',
'category': 'One Dish Meal',
'keywords': ['Savory', '< 60 Mins', 'Stove Top'],
'language': 'en',

'cook_time': 20,
'prep_time': 20,
'total_time': 40,
'yields': '4 servings'

'ratings': 5.0,
'ratings_count': 45,

'ingredient_groups': [
    {'ingredients': [
        '2 pints half-and-half cream',
        'salt & pepper, to taste',
        '1 lb jumbo shrimp, peeled, deveined, tails left on (about 20)',
        '2 cups flour',
        '2 tablespoons vegetable oil',
        '1 egg yolk',
        '1 1/2 cups butter, cold, cut into 1 inch pieces',
        '1 medium lemon, juice of',
        '4 garlic cloves, minced',
        '3 tablespoons fresh parsley, minced',
        '3 tablespoons fresh chives, chopped'
    ],
    'purpose': None}
],
'ingredients': [
    '2 pints half-and-half cream',
    'salt & pepper, to taste',
    '1 lb jumbo shrimp, peeled, deveined, tails left on (about 20)',
    '2 cups flour',
    '2 tablespoons vegetable oil',
    '1 egg yolk',
    '1 1/2 cups butter, cold, cut into 1 inch pieces',
    '1 medium lemon, juice of',
    '4 garlic cloves, minced',
    '3 tablespoons fresh parsley, minced',
    '3 tablespoons fresh chives, chopped'
],
'nutrients': {
    'calories': '1311.8', 
    'fatContent': '106.3', 
    'saturatedFatContent': '62.4', 
    'cholesterolContent': '456.4', 
    'sodiumContent': '1354', 
    'carbohydrateContent': '61.3', 
    'fiberContent': '1.9', 
    'sugarContent': '1', 
    'proteinContent': '30.7'
},

'instructions': 'Pre-heat oven to 400º F.\nSoak shrimp in half& half for 30 minutes.\nDrain shrimp and dust lightly in flour.\nSauté shrimp for 5 minutes on one side.\nYou will have to do in batches so that you do not overcrowd.\nDo not turn shrimp.\nRemove shrimp and place in a baking dish, sautéd side down, and place in pre-heated oven.\nTurn to BROIL and broil for 5 minutes.\nMeanwhile, mix egg yolk and lemon juice in half the butter and stir over low heat until butter is melted; take off heat.\nAdd garlic and remaining butter and return pan to heat. Stir briskly until butter melts and sauce thickens.\n(Add a small amount of half& half to thicken more if you like.) Add chives and parsley.\nPool sauce in plates and top with shrimp.\nServe immediately.',
'instructions_list': [
    'Pre-heat oven to 400º F.',
    'Soak shrimp in half& half for 30 minutes.',
    'Drain shrimp and dust lightly in flour.',
    'Sauté shrimp for 5 minutes on one side.',
    'You will have to do in batches so that you do not overcrowd.',
    'Do not turn shrimp.',
    'Remove shrimp and place in a baking dish, sautéd side down, and place in pre-heated oven.',
    'Turn to BROIL and broil for 5 minutes.',
    'Meanwhile, mix egg yolk and lemon juice in half the butter and stir over low heat until butter is melted; take off heat.',
    'Add garlic and remaining butter and return pan to heat. Stir briskly until butter melts and sauce thickens.',
    '(Add a small amount of half& half to thicken more if you like.) Add chives and parsley.',
    'Pool sauce in plates and top with shrimp.',
    'Serve immediately.'
],
}
"""


- author
    - from recipe_scrapers._abstract.AbstractScraper
    - Author of the recipe.

- canonical_url(self) 
    - from recipe_scrapers._abstract.AbstractScraper
    - Canonical or original URL of the recipe.
 
- category(self)
    - from recipe_scrapers._abstract.AbstractScraper
    - Category of the recipe.

- cook_time(self) from recipe_scrapers._abstract.AbstractScraper
 |      Cooking time in minutes.
 |
 |  cooking_method(self) from recipe_scrapers._abstract.AbstractScraper
 |      The method of cooking the recipe
 |
 |  cuisine(self) from recipe_scrapers._abstract.AbstractScraper
 |      Cuisine of the recipe.
 |
 |  description(self) from recipe_scrapers._abstract.AbstractScraper
 |      Description of the recipe.
 |
 |  dietary_restrictions(self) from recipe_scrapers._abstract.AbstractScraper
 |      The specified dietary restrictions or guidelines for which this recipe is suitable
 |
 |  equipment(self) from recipe_scrapers._abstract.AbstractScraper
 |      Equipment needed for the recipe.
 |
 |  image(self) from recipe_scrapers._abstract.AbstractScraper
 |      An image URL for the recipe.
 |
 |  ingredient_groups(self) -> list[recipe_scrapers._grouping_utils.IngredientGroup] from recipe_scrapers._abstract.AbstractScraper
 |      List of ingredient groups with purpose and ingredients.
 |
 |  ingredients(self) from recipe_scrapers._abstract.AbstractScraper
 |      Ingredients of the recipe.
 |
 |  instructions(self) -> str from recipe_scrapers._abstract.AbstractScraper
 |      Instructions to prepare the recipe.
 |
 |  instructions_list(self) -> list[str] from recipe_scrapers._abstract.AbstractScraper
 |      Instructions to prepare the recipe as a list.
 |
 |  keywords(self) from recipe_scrapers._abstract.AbstractScraper
 |      Keywords or tags used to describe the recipe
 |
 |  language(self) from recipe_scrapers._abstract.AbstractScraper
 |      Language the recipe is written in.
 |
 |  links(self) from recipe_scrapers._abstract.AbstractScraper
 |      Links found in the recipe.
 |
 |  nutrients(self) from recipe_scrapers._abstract.AbstractScraper
 |      Nutrients of the recipe.
 |
 |  prep_time(self) from recipe_scrapers._abstract.AbstractScraper
 |      Preparation time in minutes.
 |
 |  ratings(self) from recipe_scrapers._abstract.AbstractScraper
 |      Ratings of the recipe.
 |
 |  ratings_count(self) from recipe_scrapers._abstract.AbstractScraper
 |      Total number of ratings of the recipe.
 |
 |  site_name(self) from recipe_scrapers._abstract.AbstractScraper
 |      Name of the website.
 |
 |  title(self) from recipe_scrapers._abstract.AbstractScraper
 |      Title of the recipe.
 |
 |  to_json(self) from recipe_scrapers._abstract.AbstractScraper
 |      Recipe information in JSON format.
 |
 |  total_time(self) from recipe_scrapers._abstract.AbstractScraper
 |      Total time needed to prepare and cook the recipe in minutes.
 |
 |  yields(self) from recipe_scrapers._abstract.AbstractScraper
 |      Total servings or items in the recipe.






https://github.com/jadkins89/Recipe-Scraper
https://github.com/clarklab/chowdown
https://apps.nextcloud.com/apps/cookbook

from recipe_scrapers import scrape_me

RECIPE1 = "https://www.food.com/recipe/my-copycat-shrimp-paesano-64300"
RECIPE_TEST = "https://www.allrecipes.com/recipe/158968/spinach-and-feta-turkey-burgers/"
TEST1 = "https://www.pepperdelight.com/kerala-chicken-curry-with-coconut-milk/"
TEST2 = "https://www.malabartearoom.com/blog/tellicherry-prawn-biryani-recipe"

scraper = scrape_me(TEST1)

recipe_title = scraper.title()
recipe_instructions = scraper.instructions()
recipe_json = scraper.to_json()
# for a complete list of methods:
#help(scraper)

print(recipe_json)

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

#help_methods = 
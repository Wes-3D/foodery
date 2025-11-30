from recipe_scrapers import scrape_me

RECIPE1 = "https://www.food.com/recipe/my-copycat-shrimp-paesano-64300"
RECIPE_TEST = "https://www.allrecipes.com/recipe/158968/spinach-and-feta-turkey-burgers/"
TEST2 = "https://www.malabartearoom.com/blog/tellicherry-prawn-biryani-recipe"

scraper = scrape_me(RECIPE_TEST)
# for a complete list of methods:
#help(scraper)

recipe_title = scraper.title()
recipe_instructions = scraper.instructions()
recipe_json = scraper.to_json()

print(recipe_json)


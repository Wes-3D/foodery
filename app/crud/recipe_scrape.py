from recipe_scrapers import scrape_me

RECIPE1 = "https://www.food.com/recipe/my-copycat-shrimp-paesano-64300"
RECIPE2 = "https://www.allrecipes.com/recipe/158968/spinach-and-feta-turkey-burgers/"

def scrape_recipe_url(url=RECIPE2):
    scraper = scrape_me(url)
    #help(scraper) ## for a complete list of methods:

    recipe_title = scraper.title()
    recipe_instructions = scraper.instructions()
    recipe_json = scraper.to_json()

    print(recipe_json)
    return recipe_json


if __name__ == "__main__":
    recipe_json = scrape_recipe_url()
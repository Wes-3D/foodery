let step_num = 0;

function addInputCell(div, title, inputName, type, value, style="border p-1", id) {
    const label = document.createElement('label');
    const input = document.createElement('input');
    label.textContent = title;
    input.type = type;
    input.name = inputName;
    if (value) {
        input.value = value;
    }
    if (style && style.length > 0) {
        input.className = style;
    }
    if (id) {
        input.step = id
    }
    div.appendChild(label);
    div.appendChild(input);
}

function addIngredient(ingredient) {
    const div = document.createElement("div");
    div.textContent = ingredient;
    addInputCell(div, title="Quantity:", inputName="ing_qty", type="number", value=null, style="border p-1", step="0.001"); // step="any" // "0.001" // "0.1"  // alternatively we make it a text type, and manage the input in js after, so that "1/4" is allowed
    addInputCell(div, title="Ingredient:", inputName="ing_name", type="text");
    addInputCell(div, title="Unit:", inputName="ing_unit", type="text"); // we need a dropdown or autocomplete 
    addInputCell(div, title="Method:", inputName="ing_method", type="text");
    document.getElementById("ingredients").appendChild(div);
}

function scrapeIngredient(ingredient) {
    const div = document.createElement("div");
    div.textContent = ingredient;
    //addInputCell(div, title="Quantity:", inputName="ing_qty", type="number", value=null, style="border p-1", step="0.001"); // step="any" // "0.001" // "0.1"  // alternatively we make it a text type, and manage the input in js after, so that "1/4" is allowed
    //addInputCell(div, title="Ingredient:", inputName="ing_name", type="text");
    //addInputCell(div, title="Unit:", inputName="ing_unit", type="text"); // we need a dropdown or autocomplete 
    //addInputCell(div, title="Method:", inputName="ing_method", type="text");
    document.getElementById("ingredients").appendChild(div);
}

function addStep(step) {
    step_num+=1
    const div = document.createElement("div");
    addInputCell(div, title="Step #:", inputName="step_num", type="number", value=step_num);
    addInputCell(div, title="Description:", inputName="step_desc", type="text", value=step, style="border p-1 w-full");
    document.getElementById("steps").appendChild(div);
}

function scrapeStep(step, index) {
    const div = document.createElement("div");
    addInputCell(div, title="Step #:", inputName="step_num", type="number", value=index);
    addInputCell(div, title="Description:", inputName="step_desc", type="text", value=step, style="border p-1 w-full");
    document.getElementById("steps").appendChild(div);
}

const divUrl = document.getElementById('divUrl');
const buttonScrape = document.getElementById('buttonScrape');
const recipeName = document.getElementById('recipeName');
const recipeDescription = document.getElementById('recipeDescription');
const recipeServings = document.getElementById('recipeServings');
const recipeImage = document.getElementById('recipeImage');
const recipeGraphic = document.getElementById('recipeGraphic');
const recipeTimePrep = document.getElementById('recipeTimePrep');
const recipeTimeCook = document.getElementById('recipeTimeCook');
const recipeTimeTotal = document.getElementById('recipeTimeTotal');


function createScraper() {
    const searchUrl = `/scrape?url=${encodeURIComponent(divUrl.value)}`;

    buttonScrape.onclick = async function() {
        const recipe = await fetchRecipeUrl(searchUrl);
        console.log('Recipe ingredients:', recipe.ingredients);

        recipeName.value = recipe.title;
        recipeDescription.value = recipe.description;

        recipeImage.value = recipe.image;
        recipeGraphic.src = recipe.image;

        recipeServings.value = recipe.yields;
        recipeTimePrep.value = recipe.prep_time;
        recipeTimeCook.value = recipe.cook_time;
        recipeTimeTotal.value = recipe.total_time;

        const recipeIngredients = recipe.ingredients;
        const recipeSteps = recipe.instructions_list;

        recipeIngredients.forEach(function(ingredient, index) {
            if (ingredient) {
                scrapeIngredient(ingredient);
            }
        });

        recipeSteps.forEach(function(step, index) {
            if (step) {
                scrapeStep(step, index+1);
            }
        });

    }
}

// Fetch coordinates from Scraper endpoint //
async function fetchRecipeUrl(recipeUrl) {
    try {
        const response = await fetch(recipeUrl);
        const data = await response.json();
        console.log('Recipe data:', data);
        if (data) { //&& data.length > 0
            return data;
        } else {
            console.log('No recipe returned for the URL.');
            return null;
        }

    } catch (error) {
        console.error('Error:', error);
        return null;
    }
};


document.addEventListener('DOMContentLoaded', async () => {
    try {
        await createScraper();
    } catch (error) {
        console.error('Error:', error);
    }
});
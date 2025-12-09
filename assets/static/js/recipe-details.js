function createDeleteRecipeBlock(recipeId) {
    // Outer container
    const container = document.createElement("div");
    container.className = "bg-white rounded-lg shadow p-8";

    // Form element
    const form = document.createElement("form");
    form.method = "post";
    form.action = `/recipe-delete/${recipeId}`;

    // Equivalent to the onsubmit confirm()
    form.addEventListener("submit", function (event) {
        const ok = confirm("Are you sure you want to delete this recipe?");
        if (!ok) {
            event.preventDefault(); // Cancel submit
        }
    });

    // Button element
    const button = document.createElement("button");
    button.type = "submit";
    button.className = "bg-red-600 hover:bg-red-700 text-white font-bold py-2 px-6 rounded";
    button.textContent = "Delete Recipe";

    // Assemble
    form.appendChild(button);
    container.appendChild(form);

    return container;
}


// document.getElementById('deleteRecipe')
//const deleteRecipeButton = document.getElementById('deleteRecipe');
// Example usage:
//document.body.appendChild(createDeleteRecipeBlock(123));







function createRecipeDetails(recipeData) {
    const recipeDetailsDiv = document.getElementById('recipeDetails');
    const recipeDiv = document.getElementById('recipeDiv');

    const nameElement = document.createElement("h1");
    nameElement.classList.add("text-4xl", "font-bold", "mb-2");
    nameElement.textContent = recipeData.name;

    recipeDetailsDiv.appendChild(nameElement);
    
    if (recipeData.description) {
        const descriptionElement = document.createElement("p");
        descriptionElement.classList.add("text-gray-600", "text-lg", "mb-4");
        descriptionElement.textContent = recipeData.description;
        recipeDetailsDiv.appendChild(descriptionElement);
    }

    const divRecipeInfo = document.createElement("div");
    divRecipeInfo.classList.add("flex", "gap-8", "text-sm", "text-gray-600", "mt-6");
    recipeDetailsDiv.appendChild(divRecipeInfo);


    if (recipeData.servings) {
        const servingsElement = document.createElement("span");
        servingsElement.classList.add("flex", "items-center");
        servingsElement.innerHTML = `<span class="mr-2">🍽️</span><span><strong>${ recipeData.servings }</strong> servings</span>`;
        recipeDetailsDiv.appendChild(servingsElement);
    }

    if (recipeData.time_prep) {
        const timePrepElement = document.createElement("span");
        timePrepElement.classList.add("flex", "items-center");
        timePrepElement.innerHTML = `<span class="mr-2">⏱️</span><span>Prep: <strong>${ recipeData.time_prep }</strong> min</span>`;
        recipeDetailsDiv.appendChild(timePrepElement);
    }

    if (recipeData.time_cook) {
        const timeCookElement = document.createElement("span");
        timeCookElement.classList.add("flex", "items-center");
        timeCookElement.innerHTML = `<span class="mr-2">🔥</span><span>Cook: <strong>${ recipeData.time_cook }</strong> min</span>`;
        recipeDetailsDiv.appendChild(timeCookElement);
    }


    if (recipeData.ingredients) {
        //const ingredientsDiv = document.createElement("div");
        //ingredientsDiv.classList.add("bg-white", "rounded-lg", "shadow", "p-8", "mb-6");
        const ingredientsDiv = document.getElementById('recipeIngredients');
        ingredientsDiv.style.display = "block";

        const ingredientsHeader = document.createElement("h2");
        ingredientsHeader.classList.add("text-2xl", "font-bold", "mb-6", "pb-3", "border-b-2", "border-blue-600");
        ingredientsHeader.textContent = "📋 Ingredients";
        ingredientsDiv.appendChild(ingredientsHeader);

        const ingredientsList = document.createElement("ul");
        ingredientsList.classList.add("space-y-3");
        ingredientsDiv.appendChild(ingredientsList);

        recipeData.ingredients.forEach(ingredient => {
            const li = document.createElement("li");
            li.classList.add("flex", "items-center", "text-gray-700");

            const spanIngQty = document.createElement("span");
            spanIngQty.classList.add("w-24", "font-bold", "text-blue-600");
            spanIngQty.textContent = ingredient.quantity;
            li.appendChild(spanIngQty);

            const spanIngUnit = document.createElement("span");
            spanIngUnit.classList.add("w-20", "text-gray-600");
            spanIngUnit.textContent = ingredient.unit;
            li.appendChild(spanIngUnit);

            const spanIngName = document.createElement("span");
            spanIngName.classList.add("flex-1");
            spanIngName.textContent = ingredient.name;
            li.appendChild(spanIngName);

            if (ingredient.method) {
                const spanIngMethod = document.createElement("span");
                spanIngMethod.classList.add("text-sm", "text-gray-500", "italic");
                spanIngMethod.textContent = `(${ingredient.method})`;
                li.appendChild(spanIngMethod);
            }
            //li.textContent = `${ingredient.quantity} ${ingredient.unit} ${ingredient.name} ${ingredient.method ? `(${ingredient.method})` : ''}`;
            ingredientsList.appendChild(li);
        });
        //recipeDiv.appendChild(ingredientsDiv);
    }

    if (recipeData.steps) {
        //const stepsDiv = document.createElement("div");
        //stepsDiv.classList.add("bg-white", "rounded-lg", "shadow", "p-8", "mb-6");
        const stepsDiv = document.getElementById('recipeSteps');
        stepsDiv.style.display = "block";

        const stepsHeader = document.createElement("h2");
        stepsHeader.classList.add("text-2xl", "font-bold", "mb-6", "pb-3", "border-b-2", "border-blue-600");
        stepsHeader.textContent = "👨‍🍳 Instructions";
        stepsDiv.appendChild(stepsHeader);

        const stepsList = document.createElement("div");
        stepsList.classList.add("space-y-4");
        stepsDiv.appendChild(stepsList);

        recipeData.steps.forEach(step => {
            const stepDiv = document.createElement("div");
            stepDiv.classList.add("border-l-4", "border-blue-600", "pl-6", "py-2", "bg-blue-50", "rounded");

            const stepHeader = document.createElement("div");
            stepHeader.classList.add("font-bold", "text-blue-600", "mb-2");
            stepHeader.textContent = `Step ${step.step_number}`;
            stepDiv.appendChild(stepHeader);

            const stepDescription = document.createElement("p");
            stepDescription.classList.add("text-gray-700", "leading-relaxed");
            stepDescription.textContent = step.description;
            stepDiv.appendChild(stepDescription);

            stepsList.appendChild(stepDiv);
        });
        //recipeDiv.appendChild(stepsDiv);
    }

}

document.addEventListener('DOMContentLoaded', async function() {
    createRecipeDetails(recipeData)
});

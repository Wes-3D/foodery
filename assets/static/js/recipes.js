
async function populateRecipesTable(dataRecipes) {
    try {
        const container = document.getElementById("bodyContainer");
        container.innerHTML = '';

        // Create table element
        const table = document.createElement("table");
        table.id = "tableRecipes";
        table.className = "min-w-full bg-white border border-gray-200";

        // Create thead element
        const thead = document.createElement("thead");
        thead.className = "bg-gray-100 text-gray-700 uppercase text-xs text-left";
        const headRow = document.createElement("tr");
        const headers = ["ID", "Recipe", "Description", "Servings"];
        headers.forEach(text => {
            const th = document.createElement("th");
            th.className = "px-4 py-2";
            th.textContent = text;
            headRow.appendChild(th);
        });
        thead.appendChild(headRow);
        table.appendChild(thead);


        // Create tbody element
        const tbody = document.createElement("tbody");
        tbody.id = "bodyRecipes";


        dataRecipes.forEach(function(recipe, index) {
            if (recipe) {
                const row = tbody.insertRow();
                row.className = "border-t hover:bg-gray-50";

                // Insert cells directly
                let cellName = row.insertCell();
                cellName.textContent = recipe.name;
                cellName.className = "px-4 py-2";

                let cellId = row.insertCell();
                cellId.textContent = recipe.id;
                cellId.className = "px-4 py-2";

                let cellDescription = row.insertCell();
                cellDescription.textContent = recipe.description;
                cellDescription.className = "px-4 py-2";

                let cellServings = row.insertCell();
                cellServings.textContent = recipe.servings;
                cellServings.className = "px-4 py-2";
            }
        });

        // Add the table to the page
        table.appendChild(tbody);
        container.appendChild(table);
    } catch (error) {
        console.error('Error rendering table:', error);
    }
}



async function fetchRecipes() {
    try {
        fetch("/recipes")
            .then(res => res.json())
            .then(recipes => {
                // build table here…
                populateRecipesTable(recipes);
            });

    } catch (error) {
        console.error('Error fetching from /recipes:', error);
    }
}



document.addEventListener('DOMContentLoaded', async function() {
    //await populateRecipesTable();
    await fetchRecipes();
});


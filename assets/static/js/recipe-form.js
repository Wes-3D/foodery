function saveRecipeForm() {
    document.getElementById('recipeForm').addEventListener('submit', async function(e) {
        e.preventDefault(); // Stop the standard HTML form submit

        const timePrep = parseInt(document.getElementsByName('time_prep')[0].value) || 0;
        const timeCook = parseInt(document.getElementsByName('time_cook')[0].value) || 0;
        // Gather Basic Data
        const formData = {
            name: document.getElementsByName('name')[0].value,
            description: document.getElementsByName('description')[0].value,
            image: document.getElementsByName('image')[0].value,
            source: document.getElementsByName('source')[0].value,
            category: document.getElementsByName('category')[0].value,
            servings: parseInt(document.getElementsByName('servings')[0].value) || 0,
            time_prep: timePrep,
            time_cook: timeCook,
            time_total: timePrep + timeCook,
            ingredients: [],
            steps: []
        };

        // Gather Ingredients
        document.querySelectorAll('.ingredient-item').forEach(item => {
            const ingredientName = item.querySelector("input[name='ing_name']").value.trim();
            const ingredientValue = item.querySelector("input[name='ing_qty']").value.trim();
            const ingredientQty = normalizeFraction(ingredientValue)
            //console.log("ingredientQty:", ingredientQty);
            // Check if the name field is empty. If it is, skip this item.
            if (ingredientName === '' || !ingredientQty) {
                return;
            }
            // If the name is present, gather all ingredient details
            formData.ingredients.push({
                name: ingredientName,
                quantity: ingredientQty,
                unit: item.querySelector("select[name='ing_unit']").value,
                method: item.querySelector("input[name='ing_method']").value
            });
        });

        // Gather Steps
        document.querySelectorAll('.step-item').forEach((item, index) => {
            const stepItem = item.querySelector("input[name='step_desc']").value.trim();
            // Check if the name field is empty. If it is, skip this item.
            if (stepItem === '') {
                return;
            }
            formData.steps.push({
                step_number: index + 1, // Auto-numbering based on order
                description: stepItem
            });
        });

        // 4. Send Data to FastAPI
        try {
            const response = await fetch('/recipes/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json' // Crucial!
                },
                body: JSON.stringify(formData)
            });

            if (response.ok) {
                const result = await response.json();
                alert('Recipe saved successfully: ' + result.name);
                // Optionally redirect or clear form
                window.location.href = "/cookbook"; 
            } else {
                const err = await response.json();
                alert('Error: ' + JSON.stringify(err));
            }
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred while saving.');
        }
    });

}


function normalizeFraction(value) {
    try {
        if (value.includes("/")) {
            // Split by spaces to handle mixed fractions like "1 1/2"
            const parts = value.trim().split(/\s+/);

            let total = 0;
            for (const part of parts) {
                if (part.includes("/")) {
                    const [num, den] = part.split("/").map(Number);
                    if (isNaN(num) || isNaN(den) || den === 0) return null;
                    total += num / den;
                } else {
                    // Whole number
                    const w = Number(part);
                    if (isNaN(w)) return null;
                    total += w;
                }
            }
            return total;
        }
        // No fraction, just a number
        const num = Number(value);
        return isNaN(num) ? null : num;

    } catch (err) {
        return null;
    }
}



saveRecipeForm();

/*
        suggestion.click(async function() {
            const ingName = querySelector("input[name='ing_name']");
            const ingImg = document.getElementsByName('image')[0];
            ingName.value = suggestionStr;
            suggestionBox.empty();
            divConfBox.appendChild(createIcon('fa-check', 'green'));
            divConfBtn.style.display = 'block';
            inputLocale.style.display = 'block';
            inputLocale.value = selectLocale;
            inputStreet.value = fullStreet;
            inputCoords.value = `${selectLng},${selectLat}`;
            inputCity.value = selectCity;
            inputState.value = selectState;
            inputZip.value = selectZip;
        });
*/
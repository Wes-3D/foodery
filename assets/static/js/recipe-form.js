
function saveRecipeForm() {

    document.getElementById('recipeForm').addEventListener('submit', async function(e) {
        e.preventDefault(); // Stop the standard HTML form submit

        // Gather Basic Data
        const formData = {
            name: document.getElementsByName('name')[0].value,
            description: document.getElementsByName('description')[0].value,
            image: document.getElementsByName('image')[0].value,
            source: document.getElementsByName('source')[0].value,
            category: document.getElementsByName('category')[0].value,
            servings: parseInt(document.getElementsByName('servings')[0].value) || 0,
            time_prep: document.getElementsByName('time_prep')[0].value,
            time_cook: document.getElementsByName('time_cook')[0].value,
            time_total: document.getElementsByName('time_total')[0].value,
            ingredients: [],
            steps: []
        };

        // Gather Ingredients
        document.querySelectorAll('.ingredient-item').forEach(item => {
            formData.ingredients.push({
                name: item.querySelector("input[name='ing_name']").value,
                quantity: item.querySelector("input[name='ing_qty']").value,
                unit: item.querySelector("select[name='ing_unit']").value,
                method: item.querySelector("input[name='ing_method']").value
            });
        });

        // Gather Steps
        document.querySelectorAll('.step-item').forEach((item, index) => {
            formData.steps.push({
                step_number: index + 1, // Auto-numbering based on order
                description: item.querySelector("input[name='step_desc']").value
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




saveRecipeForm();

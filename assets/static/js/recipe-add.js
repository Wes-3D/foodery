
function addIngredient() {
    const div = document.createElement("div");
    div.innerHTML = `
        <label>Quantity:</label><input type="number" name="ingredient_quantity" class="border p-1">
        <label>Ingredient:</label><input type="number" name="ingredient_name" class="border p-1">
        <label>Unit:</label><input type="number" name="ingredient_unit" class="border p-1">
        <label>Method:</label><input type="number" name="ingredient_method" class="border p-1">
    `;
    document.getElementById("ingredients").appendChild(div);
}

var step_num = 1

function addStep() {
    step_num+=1

    const div = document.createElement("div");
    div.innerHTML = `
        <label>Step #:</label>
        <input type="number" name="step_number" class="border p-1">

        <label>Description:</label>
        <input type="text" name="step_description" class="border p-1 w-full">
    `;
    document.getElementById("steps").appendChild(div);
}
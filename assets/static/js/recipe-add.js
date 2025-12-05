
function addIngredient() {
    const div = document.createElement("div");
    div.innerHTML = `
        <label>Quantity:</label><input type="number" name="ing_qty" class="border p-1">
        <label>Ingredient:</label><input type="text" name="ing_name" class="border p-1">
        <label>Unit:</label><input type="text" name="ing_unit" step="any" class="border p-1">
        <label>Method:</label><input type="text" name="ing_method" class="border p-1">
    `;
    document.getElementById("ingredients").appendChild(div);
}

var step_num = 1

function addStep() {
    step_num+=1

    const div = document.createElement("div");
    div.innerHTML = `
        <label>Step #:</label>
        <input type="number" name="step_num" class="border p-1">

        <label>Description:</label>
        <input type="text" name="step_desc" class="border p-1 w-full">
    `;
    document.getElementById("steps").appendChild(div);
}
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

function populateUnitDropdown(div, inputName) {
    const select = document.createElement("select");
    //select.innerHTML = ""; // Clear existing
    select.name = inputName;

    displayUnits.forEach(unit => {
        const option = document.createElement("option");
        option.value = unit;
        option.textContent = unit;
        select.appendChild(option);
    });

    div.appendChild(select);
}

function addIngredient() {
    const div = document.createElement("div");

    addInputCell(div, title="Quantity:", inputName="ing_qty", type="number", value=null, style="border p-1", step="0.001"); // step="any" // "0.001" // "0.1"  // alternatively we make it a text type, and manage the input in js after, so that "1/4" is allowed
    populateUnitDropdown(div, nputName="ing_unit"); // we need a dropdown or autocomplete 
    addInputCell(div, title="Ingredient:", inputName="ing_name", type="text");
    addInputCell(div, title="Method:", inputName="ing_method", type="text");

    document.getElementById("ingredients").appendChild(div);
}

function addStep() {
    step_num+=1
    const div = document.createElement("div");

    addInputCell(div, title="Step #:", inputName="step_num", type="number", value=step_num);
    addInputCell(div, title="Description:", inputName="step_desc", type="text", value=null, style="border p-1 w-full");

    document.getElementById("steps").appendChild(div);
}

document.addEventListener('DOMContentLoaded', async function() {
    addIngredient();
    addStep();
});


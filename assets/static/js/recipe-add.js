let step_num = 0;

function addInputCell(div, title, inputName, type, value, style="border p-1 m-1", id) {
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

function populateUnitDropdown(div, inputName, style="border p-1 m-1") {
    const select = document.createElement("select");
    select.name = inputName;
    const blank = document.createElement("option");
    blank.value = "unit";
    blank.textContent = "unit";
    select.appendChild(blank);
    displayUnits.forEach(unit => {
        const option = document.createElement("option");
        option.value = unit;
        option.textContent = unit;
        select.appendChild(option);
    });
    if (style && style.length > 0) {
        select.className = style;
    }
    div.appendChild(select);
}

function addIngredient() {
    const div = document.createElement("div");
    //addInputCell(div, title="Ingredient:", inputName="ing_name", type="text");
    addAutocompleteIngredient(div, title="Ingredient:", inputName="ing_name", type="text");
    populateUnitDropdown(div, inputName="ing_unit"); // we need a dropdown or autocomplete 
    addInputCell(div, title="Quantity:", inputName="ing_qty", type="number", value=null, style="border p-1", step="0.001"); // step="any" // "0.001" // "0.1"  // alternatively we make it a text type, and manage the input in js after, so that "1/4" is allowed
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



function addAutocompleteIngredient(div, title, inputName, type, style="border p-1") {
    //const input = document.querySelector(`input[name="${inputName}"]`);
    const label = document.createElement('label');
    const input = document.createElement('input');
    label.textContent = title;
    input.type = type;
    input.name = inputName;
    input.className = style;

    // Wrapper for suggestions
    const suggestionBox = document.createElement("div");
    suggestionBox.className = "autocomplete-suggestions border bg-white absolute z-50";
    suggestionBox.style.display = "none";
    suggestionBox.style.position = "absolute";
    suggestionBox.style.maxHeight = "150px";
    suggestionBox.style.overflowY = "auto";
    //suggestionBox.style.width = input.offsetWidth + "px";

    div.appendChild(suggestionBox);

    input.addEventListener("input", function () {
        const query = this.value.toLowerCase();
        suggestionBox.innerHTML = "";

        if (!query) {
            suggestionBox.style.display = "none";
            return;
        }

        const matches = productList.filter(item =>
            item.toLowerCase().includes(query)
        );

        if (matches.length === 0) {
            suggestionBox.style.display = "none";
            return;
        }

        matches.forEach(match => {
            const option = document.createElement("div");
            option.textContent = match;
            option.className = "p-1 cursor-pointer hover:bg-gray-200";
            option.addEventListener("click", function () {
                input.value = match;
                suggestionBox.style.display = "none";
            });
            suggestionBox.appendChild(option);
        });

        suggestionBox.style.display = "block";
    });

    div.appendChild(label);
    div.appendChild(input);

    // Hide when clicking outside
    document.addEventListener("click", (e) => {
        if (!input.contains(e.target) && !suggestionBox.contains(e.target)) {
            suggestionBox.style.display = "none";
        }
    });
}


document.addEventListener('DOMContentLoaded', async function() {
    addIngredient();
    addStep();
});


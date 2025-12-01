
async function populateProductsTable(dataProducts) {
    try {
        const container = document.getElementById("bodyContainer");
        container.innerHTML = '';

        // Create table element
        const table = document.createElement("table");
        table.id = "tableProducts";
        table.className = "min-w-full bg-white border border-gray-200";

        // Create thead element
        const thead = document.createElement("thead");
        thead.className = "bg-gray-100 text-gray-700 uppercase text-xs text-left";
        const headRow = document.createElement("tr");
        const headers = ["ID", "Ingredient", "Code", "Unit", "Qty", "Weight (g)"];
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
        tbody.id = "bodyProducts";


        dataProducts.forEach(function(product, index) {
            if (product) {
                const row = tbody.insertRow();
                row.className = "border-t hover:bg-gray-50";

                // Insert cells directly
                let cellId = row.insertCell();
                cellId.textContent = product.id;
                cellId.className = "px-4 py-2";

                let cellName = row.insertCell();
                cellName.textContent = product.name;
                cellName.className = "px-4 py-2";

                let cellCode = row.insertCell();
                cellCode.textContent = product.code;
                cellCode.className = "px-4 py-2";

                let cellUnit = row.insertCell();
                cellUnit.textContent = product.volumeUnit;
                cellUnit.className = "px-4 py-2";

                let cellVolume = row.insertCell();
                cellVolume.textContent = product.volumeQty;
                cellVolume.className = "px-4 py-2";

                let cellWeight = row.insertCell();
                cellWeight.textContent = product.weightGram;
                cellWeight.className = "px-4 py-2";
            }
        });

        // Add the table to the page
        table.appendChild(tbody);
        container.appendChild(table);
    } catch (error) {
        console.error('Error rendering table:', error);
    }
}



async function fetchProducts() {
    try {
        fetch("/ingredients")
            .then(res => res.json())
            .then(products => {
                console.log("Products dataset:", products);
                // build table here…
                populateProductsTable(products);
            });

    } catch (error) {
        console.error('Error fetching from /products:', error);
    }
}



document.addEventListener('DOMContentLoaded', async function() {
    //await populateProductsTable();
    await fetchProducts();
});


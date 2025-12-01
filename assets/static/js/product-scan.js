
const style = document.createElement("style");
style.textContent = `
label, button {
    display: block;
}
`;
document.head.appendChild(style);


document.getElementById("barcodeForm").addEventListener("submit", async (event) => {
    event.preventDefault();

    const code = document.getElementById("barcode").value.trim();
    const status = document.getElementById("status");

    const product_form = document.getElementById("productForm");
    const product_name = document.getElementById("product_name");
    const product_brand = document.getElementById("product_brand");
    const serving_qty = document.getElementById("serving_qty");
    const serving_unit = document.getElementById("serving_unit");
    //const product_name = product_form.elements['product_name'];
    //const product_brand = product_form.elements['product_brand'];

    if (!code) {
        status.textContent = "Please enter a barcode.";
        return;
    }

    status.textContent = "Looking up product...";

    try {
        const response = await fetch("/lookup", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ code })
        });

        if (!response.ok) {
            const err = await response.json();
            status.textContent = `Error: ${err.detail || response.statusText}`;
            return;
        }

        const data = await response.json();
        //const product = data.product;
        console.log("product dataset:", data.product);
        status.textContent = "Lookup success!";
        //status.textContent = `✅ Saved to database!\n\nName: ${data.product.product_name || "Unknown"}\nBrand: ${data.product.brands || "Unknown"}\nCategory: ${data.product.product_type || "Unknown"}`;
        status.textContent = "Lookup success!";
        product_name.value = data.product.product_name;
        product_brand.value = data.product.brands;
        serving_qty.value = data.product.serving_quantity;
        serving_unit.value = data.product.serving_quantity_unit;
    } catch (error) {
        console.error(error);
        status.textContent = "Error contacting server.";
    }
});
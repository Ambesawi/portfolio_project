// Function to search for a product and display it
function searchProduct() {
    const searchTerm = document.getElementById("search-input").value.toLowerCase();
    const products = document.querySelectorAll(".product");

    // Loop through the products and find a match
    for (const product of products) {
        const productName = product.querySelector("h2").textContent.toLowerCase();
        
        if (productName.includes(searchTerm)) {
            // Show the matching product
            product.style.display = "block";
        } else {
            // Hide non-matching products
            product.style.display = "none";
        }
    }
}

// Event listener for the search button
const searchButton = document.getElementById("search-button");
searchButton.addEventListener("click", searchProduct);

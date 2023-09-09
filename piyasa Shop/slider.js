// slider.js

// Function to handle sliding through the product listings
function slideProducts(direction) {
    const slider = document.querySelector('.product-slider');
    const products = slider.querySelectorAll('.product');
    
    // Calculate the width of a single product container
    const productWidth = products[0].offsetWidth + parseFloat(getComputedStyle(products[0]).marginLeft) + parseFloat(getComputedStyle(products[0]).marginRight);

    // Calculate the maximum scroll position
    const maxScroll = (products.length - 3) * productWidth; // Show 3 products at a time

    // Get the current scroll position
    let currentScroll = slider.scrollLeft;

    // Calculate the new scroll position based on the direction
    if (direction === 'next') {
        currentScroll += productWidth;
        if (currentScroll > maxScroll) {
            currentScroll = maxScroll;
        }
    } else if (direction === 'prev') {
        currentScroll -= productWidth;
        if (currentScroll < 0) {
            currentScroll = 0;
        }
    }

    // Animate the scroll position
    slider.scrollTo({
        left: currentScroll,
        behavior: 'smooth'
    });
}

// Event listeners for slide buttons
const prevButton = document.querySelector('.slide-button.prev');
const nextButton = document.querySelector('.slide-button.next');

prevButton.addEventListener('click', () => slideProducts('prev'));
nextButton.addEventListener('click', () => slideProducts('next'));

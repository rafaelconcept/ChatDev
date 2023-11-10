(function() {
    /*
    This script handles the increment functionality of the number when the button is clicked.
    */
    // Get the number element
    const numberElement = document.getElementById('number');
    // Get the increment button
    const incrementButton = document.getElementById('incrementButton');
    // Initialize the counter
    let counter = 0;
    // Function to increment the counter and update the number element
    function incrementCounter() {
        counter++;
        numberElement.textContent = counter;
        numberElement.classList.add('changed'); // Add the 'changed' class
        setTimeout(() => {
            numberElement.classList.remove('changed'); // Remove the 'changed' class after a delay
        }, 300);
    }
    // Add event listener to the increment button
    incrementButton.addEventListener('click', incrementCounter);
})();
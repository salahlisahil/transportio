
'use strict';

let numberElements = document.querySelectorAll('.num');
let numbers = [];
let isCounterIncremented = false;

numberElements.forEach(num => {
    numbers.push(num.getAttribute('data-count'));
});

function incrementCounter() {
    numbers.forEach((element, index) => {
        for (let i = 0; i <= element; i++) {
            setTimeout(() => {
                numberElements[index].textContent = i;
            }, i * 10);
        }
    });
}

window.addEventListener("scroll", function () {
    if (!isCounterIncremented && this.window.scrollY >= 2000) {
        incrementCounter();
        isCounterIncremented = true;
    }
});

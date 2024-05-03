'use strict'


let openBtn = document.querySelector(".burger-menu img");
let menu = document.querySelector('.navbar');
let closeBtn = document.querySelector('.close-button');
let overlay = document.querySelector('.overlay');


openBtn.addEventListener("click", function () {
    menu.classList.toggle('active')
    overlay.style.opacity = '1'
    overlay.style.visibility = 'visible'
})

overlay.addEventListener("click", function () {
    menu.classList.toggle('active')
    overlay.style.opacity = '0'
    overlay.style.visibility = 'hidden'
})

closeBtn.addEventListener("click", function () {
    menu.classList.toggle('active')
    overlay.style.opacity = '0'
    overlay.style.visibility = 'hidden'
})



let header = document.querySelector('.header-container');

window.addEventListener('scroll', function () {
    if (this.window.scrollY >= 100) {
        header.classList.add('active')
    }
    else {
        header.classList.remove('active')
    }
})


let backToTopBtn = document.querySelector('.back-top-btn');

window.addEventListener("scroll", function () {
    if (window.scrollY > 100) {
        backToTopBtn.classList.add("active")
    }
    else {
        backToTopBtn.classList.remove("active")
    }
})



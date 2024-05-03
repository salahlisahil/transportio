

let accordions = document.querySelectorAll('.accordion');
let openAccordion = null;

accordions.forEach(function (accordion) {
    let header = accordion.querySelector('.accordion-header');
    let icon = accordion.querySelector('.fa-eye-slash');
    let faEye = accordion.querySelector('.fa-eye');
    let content = accordion.querySelector('.accordion-content');

    header.addEventListener('click', function () {
        debugger

        if (openAccordion && openAccordion !== accordion) {
            let openContent = openAccordion.querySelector('.accordion-content');
            openContent.classList.remove('d-block');
            openContent.classList.add('d-none');
            openAccordion.querySelector('.fa-eye-slash').classList.remove('d-block');
            openAccordion.querySelector('.fa-eye').classList.add('d-block');
            openAccordion.querySelector('.accordion-header').classList.remove('active-accordion');
        }

        if (content.classList.contains('d-block')) {
            content.classList.remove('d-block');
            content.classList.add('d-none');
            icon.classList.add('d-none');
            icon.classList.remove('d-block');
            faEye.classList.remove('d-none');
            header.classList.remove('active-accordion');
            openAccordion = null;
        } else {
            content.classList.add('d-block');
            content.classList.remove('d-none');
            header.classList.add('active-accordion');
            icon.classList.add('d-block');
            faEye.classList.remove('d-block');
            faEye.classList.add('d-none');
            openAccordion = accordion;
        }
    });
});



var tabMenus = document.querySelectorAll(".tab-menu-heading");
var contents = document.querySelectorAll(".left .content");

for (var menuu of tabMenus) {
    menuu.addEventListener("click", function () {
        let index = this.getAttribute("data-index");
        document.querySelector(".tab-menu-area .active").classList.remove("active");
        this.classList.add("active");

        for (let content of contents) {
            content.classList.add("d-none");
            if (content.getAttribute("data-index") === index) {
                content.classList.remove("d-none");
            }
        }
    });
}



const services = [
    {
        id: 1,
        name: "Air Freight",
        icon: "./assets/imgs/service-icon-3.png",
        img: "./assets/imgs/air_freight.jpg",
        description: ` <p>
        It is a long established fact that a reader will be distracted by the readable content of a
        page when looking at its layout. The point of using Lorem Ipsum is that it has a
        more-or-less normal distribution of letters, as opposed to using 'Content here, content
        here', making it look like readable English. packages and web page editors now use Lorem
        Ipsum as their default model.
        </p>
        <p>Packages and web page editors now use Lorem Ipsum as their default model textlayout. The
        point of using are Ipsum is that it has a more-or-less normal distribution of letters, as
        opposed to using 'Content here content normal distribution of letters as opposed to here
        making readable making.
        </p>`,
        video: "https://www.youtube.com/watch?v=6mkoGSqTqFI",
    },
    {
        id: 2,
        name: "Road Freight",
        icon: "./assets/imgs/service-icon-1.png",
        img: "./assets/imgs/road-freight.jpg",
        description: ` <p>
        Chinara It is a long established fact that a reader will be distracted by the readable content of a
        page when looking at its layout. The point of using Lorem Ipsum is that it has a
        more-or-less normal distribution of letters, as opposed to using 'Content here, content
        here', making it look like readable English. packages and web page editors now use Lorem
        Ipsum as their default model.
        </p>
        <p>Packages and web page editors now use Lorem Ipsum as their default model textlayout. The
        point of using are Ipsum is that it has a more-or-less normal distribution of letters, as
        opposed to using 'Content here content normal distribution of letters as opposed to here
        making readable making.
        </p>`,
        video: "https://www.youtube.com/watch?v=6mkoGSqTqFI",
    },
    {
        id: 3,
        name: "Ocean Freight",
        icon: "./assets/imgs/service-icon-2.png",
        img: "./assets/imgs/ocean_freight.jpg",
        description: ` <p>
        salam It is a long established fact that a reader will be distracted by the readable content of a
        page when looking at its layout. The point of using Lorem Ipsum is that it has a
        more-or-less normal distribution of letters, as opposed to using 'Content here, content
        here', making it look like readable English. packages and web page editors now use Lorem
        Ipsum as their default model.
        </p>
        <p>Packages and web page editors now use Lorem Ipsum as their default model textlayout. The
        point of using are Ipsum is that it has a more-or-less normal distribution of letters, as
        opposed to using 'Content here content normal distribution of letters as opposed to here
        making readable making.
        </p>`,
        video: "https://www.youtube.com/watch?v=6mkoGSqTqFI",
    },
    {
        id: 4,
        name: "Rail Freight",
        icon: "./assets/imgs/service-icon-4.png",
        img: "./assets/imgs/rail_freight.jpg",
        description: ` <p>
        eleykim It is a long established fact that a reader will be distracted by the readable content of a
        page when looking at its layout. The point of using Lorem Ipsum is that it has a
        more-or-less normal distribution of letters, as opposed to using 'Content here, content
        here', making it look like readable English. packages and web page editors now use Lorem
        Ipsum as their default model.
        </p>
        <p>Packages and web page editors now use Lorem Ipsum as their default model textlayout. The
        point of using are Ipsum is that it has a more-or-less normal distribution of letters, as
        opposed to using 'Content here content normal distribution of letters as opposed to here
        making readable making.
        </p>`,
        video: "https://www.youtube.com/watch?v=6mkoGSqTqFI",
    },
    {
        id: 5,
        name: "Warehousing",
        icon: "./assets/imgs/service-icon-5.png",
        img: "./assets/imgs/warehousing.jpg",
        description: ` <p>
        necesen It is a long established fact that a reader will be distracted by the readable content of a
        page when looking at its layout. The point of using Lorem Ipsum is that it has a
        more-or-less normal distribution of letters, as opposed to using 'Content here, content
        here', making it look like readable English. packages and web page editors now use Lorem
        Ipsum as their default model.
        </p>
        <p>Packages and web page editors now use Lorem Ipsum as their default model textlayout. The
        point of using are Ipsum is that it has a more-or-less normal distribution of letters, as
        opposed to using 'Content here content normal distribution of letters as opposed to here
        making readable making.
        </p>`,
        video: "https://www.youtube.com/watch?v=6mkoGSqTqFI",
    },
    {
        id: 6,
        name: "Project Cargo",
        icon: "./assets/imgs/service-icon-6.png",
        img: "./assets/imgs/project_cargo.jpg",
        description: ` <p>
        yaxsiyam It is a long established fact that a reader will be distracted by the readable content of a
        page when looking at its layout. The point of using Lorem Ipsum is that it has a
        more-or-less normal distribution of letters, as opposed to using 'Content here, content
        here', making it look like readable English. packages and web page editors now use Lorem
        Ipsum as their default model.
        </p>
        <p>Packages and web page editors now use Lorem Ipsum as their default model textlayout. The
        point of using are Ipsum is that it has a more-or-less normal distribution of letters, as
        opposed to using 'Content here content normal distribution of letters as opposed to here
        making readable making.
        </p>`,
        video: "https://www.youtube.com/watch?v=6mkoGSqTqFI",
    },
]


localStorage.setItem("services", JSON.stringify(services))

let servicesDetail = JSON.parse(localStorage.getItem('services'))

let btns = document.querySelectorAll('#service .btn-link')


btns.forEach(btn => {
    btn.addEventListener("click", function () {
        for (const service of servicesDetail) {
            if (btn.parentElement.getAttribute('id') == service.id) {
                localStorage.setItem("clickedService", JSON.stringify(service))
            }
        }
    })
})

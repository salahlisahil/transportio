var map;
var startPoint;
var endPoint;

map = L.map('map').setView([51.505, -0.09], 13);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);


function initMap(data) {
    map.off();
    map.remove();
    map = L.map('map').setView([51.505, -0.09], 13);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);


    startPoint = L.latLng(data.from_latitude, data.from_longitude);
    endPoint = L.latLng(data.to_latitude, data.to_longitude);

    marker1 = L.marker(startPoint).addTo(map);
    marker2 = L.marker(endPoint).addTo(map);

    L.Routing.control({
        waypoints: [
            startPoint,
            endPoint
        ]
    }).addTo(map);
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


$.ajaxSetup({
    headers: {
        'X-CSRFToken': getCookie('csrftoken')
    }
});

$('.trackBtn').on('click', function (){
    let track_id = $('#track_id').val();
    $.ajax({
        url: ajaxUrl,
        method: 'POST',
        data: { track_id: track_id},
        success: function (data) {
            if(data.status === 'error'){
                Swal.fire({
                  title: 'Notification',
                  text: data.message,
                  icon: 'error',
                  confirmButtonText: 'ОК'
                });
            }

            else{
                console.log(map)
                initMap(data)
            }

        },
        error: function (xhr, status, error) {
            Swal.fire({
              title: 'Notification',
              text: error,
              icon: 'error',
              confirmButtonText: 'ОК'
            });
        }
    });
});


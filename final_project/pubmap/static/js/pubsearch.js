

function initAutocomplete(listener) {
    var input = document.getElementById('searchbar');
    var autocomplete = new google.maps.places.Autocomplete(input);
    autocomplete.addListener('place_changed', function () {
        var place = autocomplete.getPlace();
        if (!place.geometry) {
            window.alert("Nie mogę znaleźć miejsca: '" + place.name + "'");
            return;
            }
        document.getElementById('id_name').value = place["name"];
        document.getElementById('id_formatted_address').value = place["formatted_address"];
        document.getElementById('id_formatted_phone_number').value = place["formatted_phone_number"];
        document.getElementById('id_website').value = place["website"];
        document.getElementById('id_place_id').value = place["place_id"];
        document.getElementById('id_latitude').value = place.geometry.location.lat();
        document.getElementById('id_longitude').value = place.geometry.location.lng();
        document.getElementById('id_opening_hours').value = JSON.stringify(place.opening_hours.weekday_text);


    })
}

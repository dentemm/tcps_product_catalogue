$('.modalDelete').on('click', function(e) {

	//e.preventDefault();
	console.log("Delete knop gedrukt!");
	var item_slug = $(this).attr('id').split(/-(.+)/)[1]; //Get slug via id, split achter eerste dash
	console.log(item_slug);
	$('#vulin').text(item_slug);

});

$('#confirmDelete').on('click', function(e) {

	console.log("Confirm delete knop gedrukt");
	var item_slug = $('#vulin').text();
	console.log(item_slug)
	delete_item(item_slug);
});



function delete_item(slug) {
	console.log("Delete functie opgeroepen");
	console.log("products/category/delete/"+slug) // sanity check
	$.ajax({
		url: "/products/category/delete/" + slug,
		type: "DELETE",
		data: {
			test: "test"
		},
		success: function(json){
			console.log(json);
			$('#myModaal').modal('hide')
			console.log(slug);
			$('#item-'+slug).parents('tr').remove();
		}
	});

};

/*
Onderstaande code is nodig voor de CSRF token die Django vereist toe te voegen aan 
Ajax calls
*/

// This function gets cookie with a given name
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

/*
The functions below will create a header with csrftoken
*/

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            // Send the token to same-origin, relative URLs only.
            // Send the token only if the method warrants CSRF protection
            // Using the CSRFToken value acquired earlier
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
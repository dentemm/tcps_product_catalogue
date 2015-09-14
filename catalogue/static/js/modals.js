$('.subcategory-modal').on('click', function(e) {

    e.preventDefault();
    console.log('Subcategory!');
    var subcategory_slug = $(this).attr('id').split(/-(.+)/)[1]; //Get slug via id, split achter eerste dash
    console.log(subcategory_slug);
    
    ajax_subcategory(subcategory_slug);

});

$('.supplier-modal').on('click', function(e) {

    e.preventDefault();
    console.log('Supplier!');
    var supplier_slug = $(this).attr('id').split(/-(.+)/[1]);
    console.log(supplier_slug);

    ajax_supplier(supplier_slug);

});

function ajax_subcategory(category_slug) {
    
    //console.log("ajax call opgeroepen");
    //console.log("url: products/subcategory/" + category_slug) // sanity check

    $.ajax({
        url: "/products/subcategory/" + category_slug + "/",
        type: "GET",
        dataType: "html",
        success: success_handler //Improved readability by creating handler function
    });
};

function ajax_supplier(supplier_slug) {

    $.ajax({
        url: "/products/supplier/" + supplier_slug + "/",
        type: "GET",
        dataType: "html",
        success: success_handler
    });
};

function success_handler(html) {

    //console.log(html);

    $("#modal").html(html);
    $('#modal').modal('show');

    // Start Owl Carousel
    $("#owl-demo").owlCarousel({

        navigation : true, // Show next and prev buttons
        navigationText:["Vorige","Volgende"],
        slideSpeed : 300,
        paginationSpeed : 400,
        singleItem:true
    }); 
}


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
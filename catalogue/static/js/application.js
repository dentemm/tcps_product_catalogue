$('button.category').on('click', function(e) {

	//e.preventDefault();
	console.log('Toggle!!!');

	if($(this).hasClass('active')) {
		// Add the necessary tags 

		console.log('category removed');
		

		categorie = $.trim($(this).text());
		console.log(categorie);
		console.log('spatie');

		//ajax_call(categorie);
	}

	else {
		// Remove the necessary tags
		console.log('category added');

		categorie = $.trim($(this).text());

		console.log(categorie)

		ajax_call(categorie);



		//var myClass = $(this).attr("class");
   		//alert(myClass);
	}

	function ajax_call(category_name) {

		$.ajax({
			//url:"/products/overview/products/",
			url:"/products/overview/all/",
			type: "GET",
			//contentType: 'application/json',
			//contentType: 'html',
			data: {
				selected: category_name
			},
			success: my_handler,

			error: function(xhr, ajaxOptions, thrownError) {
				console.log(xhr.status);
				alert(thrownError);
			}
		});
	};

	function my_handler(json) {

		console.log("successful handled");
		console.log(json);

		/*var categories = json['subcategories']
		var suppliers = json['suppliers']

		console.log(categories)
		console.log(suppliers)*/
	};

	function create_subcategory_buttons() {

	};
});
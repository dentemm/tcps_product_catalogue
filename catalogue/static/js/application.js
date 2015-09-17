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
		ajax_call(categorie);



		//var myClass = $(this).attr("class");
   		//alert(myClass);
	}

	function ajax_call(category_name) {

		$.ajax({
			url:"/products/test/tim/",
			type: "GET",
			data: {
				test: category_name
			},
			success: my_handler
		});


		/*$.ajax({
		url: "/products/dashboard/categorie/delete/" + slug,
		type: "DELETE",
		data: {
			test: "test"
		},
		success: function(json){
			console.log(json);
			$('#myModaal').modal('hide')
			console.log(slug);
			$('#item-'+slug).parents('tr').remove(); //Remove tr visueel, zodat page refresh niet nodig is
		}
	});*/

	};

	function my_handler(json) {

		console.log("successful handled");
		console.log(json);


	};

});
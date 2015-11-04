$(function() {

	// Initialize tagsort 
	$('div.tagsort-tags-container').tagSort({
		selector:'.tagsort-item',
		tagWrapper: 'button',
		displaySelector: '.test',
	});

	// Fix for bootstrap modal window caching
	$('body').on('hidden.bs.modal', '.modal', function () {
  		$(this).removeData('bs.modal');
	});


	$('button.category').click(function() {


		// 1. Add active class to currently clicked button, and remove active class from others
		$('button.category').removeClass('active');
		$(this).addClass('active');

		// 2. Ajax call for currently chosen category
		slug = $(this).data('slug');

		//console.log($(this).text());
		//console.log($(this).data('slug'))

		ajax_call(slug);

	});

	function ajax_call(slug) {

		$.ajax({
			//url:"/products/overview/products/",
			url:"/products/",
			type: "GET",
			//contentType: 'application/json',
			//contentType: 'html',
			data: {
				selected: slug
			},
			success: my_handler,

			error: function(xhr, ajaxOptions, thrownError) {
				console.log(xhr.status);
				alert(thrownError);
			}
		});
	};

	function my_handler (data) {
		//console.log('successfull ajax call!');
		//console.log(data);

		$('div.products-container').html(data);

		$('div.tagsort-tags-container').tagSort({
  			selector:'.tagsort-item',
  			tagWrapper: 'button',
  			displaySelector: '.test',
		});
	};
});



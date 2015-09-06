
/******************
* = Gallery hover *
******************/
jQuery(document).ready(function ($) {
	//Cache some variables
	var images = $('#slide-product a');
	
	images.hover(
		function(e) {
			var asta = $(this).find('img');
			$('#slide-product img').not( asta ).stop(false, false).animate(
				{
					opacity: .5
				},
				'fast',
				'linear'
			);
			var zoom = $('<div class="zoom"></div>');
			if ( $(this).hasClass('video') ) {
				zoom.addClass('video');
			}
			$(this).prepend(zoom);
		},
		function(e) {
			$('#slide-product img').stop(false, false).animate(
				{
					opacity: 1
				},
				'fast',
				'linear'
			);
			$('.zoom').remove();
		}
	);
});


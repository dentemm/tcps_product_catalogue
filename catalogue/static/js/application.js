$('button.category').on('click', function(e) {

	//e.preventDefault();
	console.log('Toggle!!!');

	if($(this).hasClass('active')) {
		console.log('active');
		var myClass = $(this).attr("class");
   		alert(myClass);
	}

	else {
		console.log('nope');
		var myClass = $(this).attr("class");
   		alert(myClass);
	}

});
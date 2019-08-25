/*Dropdown menu*/
$(document).ready(function(){
	if($(window).width() >= '992'){
		$('body').on('mouseenter mouseleave', '.navbar .dropdown', function (e) {
			
			    var dropdown = $(e.target).closest('.navbar .dropdown');
			    var menu = $('>.dropdown-menu', dropdown);
			    dropdown.addClass('show');
			    menu.addClass('show');
			    setTimeout(function () {
			        dropdown[dropdown.is(':hover') ? 'addClass' : 'removeClass']('show');
			        menu[dropdown.is(':hover') ? 'addClass' : 'removeClass']('show');
			    }, 100);
		    
		});
	}
});
// IIFE - Immediately Invoked Function Expression
(function(yourcode) {
  // The global jQuery object is passed as a parameter
	yourcode(window.jQuery, window, document);
}(function($, window, document) {
 // The $ is now locally scoped
 // Listen for the jQuery ready event on the document
 $(function() {
   // The DOM is ready!
 });

	let this_file = $('#player_name_dropdown')


	var alreadyFilled = false;
	var players = JSON.parse(this_file.attr("players_list"));


	function initDialog() {
			clearDialog();
			for (var i = 0; i < players.length; i++) {
					$('.dialog').append('<div>' + players[i] + '</div>');
			}
	}

	function clearDialog() {
			$('.dialog').empty();
	}

	$('.autocomplete input').click(function() {
			if (!alreadyFilled) {
					$('.dialog').addClass('open');
			}
	});

	$('body').on('click', '.dialog > div', function() {
			$('.autocomplete input').val($(this).text()).focus();
			$('.autocomplete .close').addClass('visible');
			alreadyFilled = true;
	});

	$('.autocomplete .close').click(function() {
			alreadyFilled = false;
			$('.dialog').addClass('open');
			$('.autocomplete input').val('').focus();
			$(this).removeClass('visible');
	});

	function match(str) {
			str = str.toLowerCase();
			clearDialog();
			for (var i = 0; i < players.length; i++) {
					if (players[i].toLowerCase().startsWith(str)) {
							$('.dialog').append('<div>' + players[i] + '</div>');
					}
			}
	}

	$('.autocomplete input').on('input', function() {
			$('.dialog').addClass('open');
			alreadyFilled = false;
			match($(this).val());
	});

	$('body').click(function(e) {
			if (!$(e.target).is("input, .close")) {
					$('.dialog').removeClass('open');
			}
	});

	initDialog();


}));

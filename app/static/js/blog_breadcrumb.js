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

	let active = $(".active");
	let breadcrumb = $(".breadcrumb-item");

	breadcrumb.click(function() {
		breadcrumb.removeClass("active")
  	$(this).toggleClass("active");

	})

}));

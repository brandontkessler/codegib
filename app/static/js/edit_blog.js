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

	let this_file = $('#blog_content');
	let blog_content = this_file.attr("blog_content");
	let blog_headline = this_file.attr("blog_headline");
  let blog_content_form_area = $('#blog-content');
	let blog_headline_form_area = $(".blog-headline");

  blog_content_form_area.val(blog_content)
	blog_headline_form_area.val(blog_headline)

}));

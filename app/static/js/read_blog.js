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
  let blog_content_div = $('.blog-content-container');
	let start_delete = $('#start-delete-btn');
	let delete_btn = $('#delete-btn');
	let cancel_btn = $('#cancel-btn');

	delete_btn.hide()
	cancel_btn.hide()
  blog_content_div.html(blog_content)

	start_delete.on('click', function(){
		$(this).hide()
		delete_btn.show()
		cancel_btn.show()
	})

	cancel_btn.on('click', function(){
		$(this).hide()
		delete_btn.hide()
		start_delete.show()
	})

}));

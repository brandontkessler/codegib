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

	let this_file = $('#blog_titles');
	let blogs = this_file.attr("blog_titles");
  let this_blog_post_form = $("#blog-post-form");

  // CHECK IF BLOG TITLE ALREADY EXISTS
  this_blog_post_form.submit(function(e) {

    let this_blog_title = $("#blog-title").val();

    $("#javascript-error-check").empty();

    if(blogs.indexOf(this_blog_title) !== -1) {
      e.preventDefault();
      $("#javascript-error-check").append(
        `<div class="alert alert-warning">
          That title has been taken
        </div>`
      );
      $(window).scrollTop(0);
    } else {
      return;
    }

  })

}));

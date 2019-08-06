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

	let this_file = $('#post_blog_js');
	let blogs = this_file.attr("blog_titles");
  let this_blog_post_form = $("#blog-post-form");

	let blog_viewer_btn = $("#blog-viewer_btn")
	let blog_content = $("#blog-content");

	let viewer_div = $(".blog_viewer")
	let viewer_title = $("#viewer_title");
	let viewer_date = $("#viewer_date");
	let viewer_headline = $("#viewer_headline");
	let viewer_content = $("#viewer_content");

	viewer_div.hide();

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

  });
	// END OF BLOG CHECKER

	// SETUP THE BLOG VIEWER
	blog_viewer_btn.on("click", function(){
		viewer_title.empty();
		viewer_date.empty();
		viewer_headline.empty();
		viewer_content.empty()

		let this_content = blog_content.val();
		this_blog_post_form.toggle();
		viewer_div.toggle();

		let d = new Date();
		let strDate = d.getFullYear() + "/" + (d.getMonth()+1) + "/" + d.getDate();

		viewer_title.append($("#blog-title").val());
		viewer_date.append(strDate);
		viewer_headline.append($(".blog-headline").val());
		viewer_content.html(blog_content.val());
	})


}));

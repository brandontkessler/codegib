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

 let path = window.location.pathname;
 let page_location = path.split("/")[1];
 let home_nav = $('.home-nav');
 let about_nav = $('.about-nav');
 let media_nav = $('.media-nav');
 let api_nav = $('.api-nav');


 if (page_location === '') {
   home_nav.children().css("text-decoration", "underline");
 } else if (page_location === 'about') {
   about_nav.css("text-decoration", "underline");
 } else if (page_location === 'media') {
   media_nav.css("text-decoration", "underline");
 } else if (page_location === 'api') {
   api_nav.css("text-decoration", "underline");
 }

}));

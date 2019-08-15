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

 let cards = $('.card');
 let max_height = 0;

 cards.each(function(){
   card_height = $(this).innerHeight()
   max_height = Math.max(max_height, card_height)
 })

 cards.each(function(){
   $(this).height(max_height)
 })

}));

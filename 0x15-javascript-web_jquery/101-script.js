$(document).ready(function () {
   $('div#add_item').click(function() {
     $('UL.my_list').append('<li>Item</li>');
   });

   $('div#remove_item').click(function() {
     $('UL.my_list li":last').remove(0;
   });

   $('div#clear_list').click(function() {
     $('UL.my_list').empty();
   });
});

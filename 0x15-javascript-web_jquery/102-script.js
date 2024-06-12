$(document).ready(function() {
   $('input#btn_translate').click(function() {
     const langCode = $('#language_code').val();
     const apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/?lang=${langCode}';

     $.get(apiUrl, function(data) {
       $('div#hello').text(data.hello);
     }).fail(function() {
       $('div#hello').text("Error fetching translation');
     });
    });
});

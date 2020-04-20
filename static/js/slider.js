$(document).ready(function()
{
	x = 0;
    y = 0;
    $('#slider ul').html('<li class="bg-img" style="background-image: url(' + document._scd['data']['slides'][x] + ');"></li>');
    setInterval(function () {
        nextSlide();
    }, 5000);
    $('.phrase-' + y%2 ).show();
    setInterval(function () {
        nextPhrase();
    }, 10000);

    function nextPhrase() {
      $('.phrase-' + y%2 ).fadeOut(0);
        y++;
        $('.phrase-' + y%2 ).fadeIn(0);
    };

    function nextSlide() {
		$('#slider ul li').fadeOut(1000, function(){
			$(this).remove();
		})
		x++;
		if (x > 5)
		{
			x = 0;
		}
		$('#slider ul').append('<li class="bg-img" style="background-image: url(' + document._scd['data']['slides'][x] + '); display: none;"></li>');
		$('#slider ul li:last-of-type').fadeIn(1200);
	};

});
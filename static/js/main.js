$(document).ready(function()
{
	$(window).load(function() {
		// Animate loader off screen
		$(".se-pre-con").fadeOut("slow");
	});
    x = 1;
    y = 0;
    $('#slider ul li:nth-child(' + x + ')').show();
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
      $('#slider ul li:nth-child(' + x + ')').fadeOut(1000);
      if (x > 5)
      {
        x = 0;
      }
        x++;
        $('#slider ul li:nth-child(' + x + ')').fadeIn(1200);
    };
    var navbar = document.getElementById("navbar");
    var sticky = navbar.offsetTop;
    myFunction()
    window.onscroll = function() {myFunction()};

    function myFunction() {
      if (window.pageYOffset > sticky) {
        navbar.classList.add("sticky")
      } else {
        navbar.classList.remove("sticky");
      }
    }
    var $root = $('html, body');

    $('a[href^="#"]').click(function () {
        $root.animate({
            scrollTop: $( $.attr(this, 'href') ).offset().top
        }, 500);

        return false;
    });

    $( ".hamburger" ).click(function() {
        $('.mobile-menu').toggle();
    })
});


(function($) {

  // Open Lightbox
  $('.open-lightbox').on('click', function(e) {
    e.preventDefault();
    var image = $(this).attr('href');
    var id = parseInt($(this).parent().index())+1
    var last = parseInt($('.slideshow-container .img').last().index())+1
    $('html').addClass('no-scroll');
    $('body').append('<div class="lightbox-opened"><img data-key="'+ id +'" src="' + image + '"></div>');
    addNav(id, last)
  });

  // Close Lightbox
    $('body').on('click', '.lightbox-opened', function()
    {
        $('html').removeClass('no-scroll');
        $('.lightbox-opened').remove();
        $('.gal-nav').remove();
    });

})(jQuery);

function plusSlides(n)
{
    $('.lightbox-opened').remove();
    $('.gal-nav').remove();
    var className = '#img_' + n
    var url = $(className + ' a').attr('href');
    var id = parseInt($(className).index())+1
    var last = parseInt($('.slideshow-container .img').last().index())+1
    $('body').append('<div class="lightbox-opened"><img data-key="'+ id +'" src="' + url + '"></div>');
    addNav(id, last)
}

function addNav(id, last)
{
    $('body').find('.lightbox-opened').append('<div class="gal-nav"></div>');
    if(id != 0 )
    {
        var n = id-1
        $('body').find('.gal-nav').append('<a class="prev" onkeydown="plusSlides(' + n + ')" onclick="plusSlides(' + n + ')">&#10094;</a>');
    }
    if(id != last)
    {
        var n = id+1
        $('body').find('.gal-nav').append('<a class="next" onkeydown="plusSlides(' + n + ')" onclick="plusSlides(' + n + ')">&#10095;</a>');
    }
}

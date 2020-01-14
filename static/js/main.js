
$(document).ready(function()
{
  stopmusic = false;
  $( "#musicplay" ).click(function() {
    $.post(document._scd['routing']['music_play'], function( data ) {
        console.log("success");
    });
    audio.play();
    audio.muted = false;
    stopmusic = false;
  });
  $( "#musicpause" ).click(function() {
    $.post(document._scd['routing']['music_stop'], function( data ) {
        console.log("success");
    });
    audio.pause();
    audio.muted = true;
    stopmusic = true;
  });

    if(document._scd['data']['music']) {
        playPromise = audio.play();
    	if (playPromise !== undefined) {
        setTimeout(function() {
        	  playPromise.then(function() {
              audio.muted = false;
        			console.log('started');
        	  }).catch(function(error) {
        			console.log('error');
              $( "#musicplay" ).trigger('click');
        	  });
        }, 3000);
    	}
      setInterval(function(){
        if( !stopmusic )
        {
        	audio.currentTime = 0;
        	audio.play();
          audio.muted = false;
        }
      }, 30700);

    }
	$(window).load(function() {
		// Animate loader off screen
		$(".se-pre-con").fadeOut("slow");
	});
    x = 1;
    $('#slider ul li:nth-child(' + x + ')').show();
    setInterval(function () {
        nextSlide();
    }, 5000);

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
    $('body').append('<div class="gal-nav"></div>');
    console.log(id, last)
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

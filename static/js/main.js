
$(document).ready(function()
{
  stopmusic = false;
  $( "#musicplay" ).click(function() {
    audio.play();
    audio.muted = false;
    stopmusic = false;
  });
  $( "#musicpause" ).click(function() {
    audio.pause();
    audio.muted = true;
    stopmusic = true;
  });

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
  setInterval(function()
  {
    if( !stopmusic )
    {
    	audio.currentTime = 0;
    	audio.play();
      audio.muted = false;
    }
  }, 30700);

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
});

// // Next/previous controls
// function plusSlides(n) {
//   showSlides(data['slideIndex'] += n);
// }
//
// // Thumbnail image controls
// function currentSlide(n) {
//   showSlides(data['slideIndex'] = n);
// }
//
// function showSlides(n) {
//   var i;
//   var slides = document.getElementsByClassName("mySlides");
//   var dots = document.getElementsByClassName("dot");
//   if (n > slides.length) {data['slideIndex'] = 1}
//   if (n < 1) {data['slideIndex'] = slides.length}
//   for (i = 0; i < slides.length; i++) {
//       slides[i].style.display = "none";
//   }
//   for (i = 0; i < dots.length; i++) {
//       dots[i].className = dots[i].className.replace(" active", "");
//   }
//   slides[data['slideIndex']-1].style.display = "block";
//   dots[data['slideIndex']-1].className += " active";
// }


(function($) {

  // Open Lightbox
  $('.open-lightbox').on('click', function(e) {
    e.preventDefault();
    var image = $(this).attr('href');
    var id = parseInt($(this).parent().index())+1
    var last = parseInt($('.slideshow-container .img').last().index())+1
    $('html').addClass('no-scroll');
    $('body').append('<div class="lightbox-opened"><img src="' + image + '"></div>');
    $('body').append('<div class="gal-nav"></div>');
    console.log(id, id-1)
    if(id != 1 )
    {
        var n = id-1
        $('body').find('.gal-nav').append('<a class="prev" onclick="plusSlides(' + n + ')">&#10094;</a>');
    }
    if(id != last+1)
    {
        var n = id+1
        $('body').find('.gal-nav').append('<a class="next" onclick="plusSlides(' + n + ')">&#10095;</a>');
    }

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
    console.log(url)
    var id = parseInt($(className).index())+1
    var last = parseInt($('.slideshow-container .img').last().index())+1
    $('body').append('<div class="lightbox-opened"><img src="' + url + '"></div>');
    $('body').append('<div class="gal-nav"></div>');
    if(id != 0 )
    {
        var n = id-1
        $('body').find('.gal-nav').append('<a class="prev" onclick="plusSlides(' + n + ')">&#10094;</a>');
    }
    if(id != last)
    {
        var n = id+1
        $('body').find('.gal-nav').append('<a class="next" onclick="plusSlides(' + n + ')">&#10095;</a>');
    }
}

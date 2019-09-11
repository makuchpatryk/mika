
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
  }, 30500);

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

// Next/previous controls
function plusSlides(n) {
  showSlides(data['slideIndex'] += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(data['slideIndex'] = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {data['slideIndex'] = 1}
  if (n < 1) {data['slideIndex'] = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[data['slideIndex']-1].style.display = "block";
  dots[data['slideIndex']-1].className += " active";
}

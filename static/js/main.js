$(document).ready(function()
{
  var audio = new Audio();
  audio.src = data['source'];
  audio.id = 'audio';

  audio.volume = 0.05;
  audio.autoplay = true;
  audio.loop = true;


		playPromise = audio.play();
		if (playPromise !== undefined) {
		  playPromise.then(function() {
				console.log('started');
		  }).catch(function(error) {
				console.log('error');
        audio.play();
		  });
		}

    audio.addEventListener('ended', function() {
      this.currentTime = 0;
      this.play();
    }, false);

  $( "#musicplay" ).click(function() {
    audio.play();
  });
  $( "#musicpause" ).click(function() {
    audio.pause();
  });

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

$(document).ready(function()
{
  var audio = new Audio();
  audio.src = data['source'];
  audio.id = 'audio';

  audio.volume = 0.05;
  audio.autoplay = true;
  audio.loop = true;
  audio.play();

  $( "#musicplay" ).click(function() {
    audio.play();
  });
  $( "#musicpause" ).click(function() {
    audio.pause();
  });
    x = 1;
    $('#slider ul li:nth-child(' + x + ')').show();
    setInterval(function () {
        nextSlide();
    }, 5000);

    function nextSlide() {
      $('#slider ul li:nth-child(' + x + ')').hide();
      if (x > 5)
      {
        x = 0;
      }
        x++;
        $('#slider ul li:nth-child(' + x + ')').fadeIn('fast');
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

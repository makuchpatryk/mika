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
});
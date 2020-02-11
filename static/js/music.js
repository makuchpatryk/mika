$(document).ready(function()
{
	var tillPlayed = getCookie('timePlayed');
	var stopPlayed = getCookie('stopPlayed');
	console.log("tillPlayed", tillPlayed, "stopPlayed", stopPlayed)
	if (!stopPlayed || stopPlayed=='undefined')
	{
		stopmusic = false;
	}
	else
	{
		stopmusic = true;
	}

	$( "#musicplay" ).click(function() {
		setCookie('stopPlayed', false);
		audio.play();
		audio.muted = false;
		stopmusic = false;
	});
	$( "#musicpause" ).click(function() {
		setCookie('stopPlayed', false);
		audio.pause();
		audio.muted = true;
		stopmusic = true;
	});
	if(!stopmusic)
	{
		playPromise = audio.play();
		audio.currentTime = 0;
		if (playPromise !== undefined)
		{
			setTimeout(function() {
				playPromise.then(function() {
					audio.muted = false;
					console.log('started');
				}).catch(function(error) {
					console.log('error');
					$( "#musicplay" ).trigger('click');
				});
			}, 100);
		}
		setInterval(function(){
			audio.currentTime = 0;
			audio.play();
			audio.muted = false;
		}, 30700);
		setInterval(function(){
			update_time_song(audio)
		},1000);
	}

});

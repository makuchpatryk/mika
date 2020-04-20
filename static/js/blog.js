$(document).ready(function()
{
	$('body').on('postLike', function(e, $element)
    {
    	// checking if already like base on cookies
    	var pk = $element.data('pk');
    	var number = $element.data('number');
    	var once = true;

		if (getCookie('likePost_' + pk))
		{
			likeOff($element);
		}

    	$element.find('.icon').click(function() {
			if (getCookie('likePost_' + pk)) {
				return;
			}
			callAjax();
		});

    	$element.find('.icon').mouseover(function(){
    		likeOff();
    	})
    	$element.find('.icon').mouseout(function(){
    		if (!getCookie('likePost_' + pk))
			{
    			likeOn();
    		}
    	})

    	// func
    	function callAjax()
    	{
    		if (!once) {
    			return;
    		}
    		once = false;

			likeOff();
            likeNumberUp();
			$.ajax({
                method: 'POST',
                url: document._scd['routing']['like_post'],
                data: {'uid': pk},
            }).done(function(response) {
            	setCookie('likePost_' + pk, false);
            })
            .fail(function(response) {
            	console.log(response, 'fail');
            });
    	}
		function likeNumberUp()
		{
			var newNumber = number+1;
			$element.find(".number").html('' + newNumber + '');
		}
		function likeOff()
		{
			$element.find("i").removeClass('fa-heart-o')
			$element.find("i").addClass('fa-heart')
		}
		function likeOn()
		{
			$element.find("i").removeClass('fa-heart')
			$element.find("i").addClass('fa-heart-o')
		}

    });

});
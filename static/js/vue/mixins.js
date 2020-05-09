var VueFormMixin = {
	methods: {
	    displayError: function(key, value) {
            if (key == 'thread_type') {
                key = 'topic';
            }

            if ((_.keys(this.error).indexOf(key)) == -1) {
                key = 'general';
            }
            if (typeof this.error_message != "undefined" && this.error_message[key]) {
                value = this.error_message[key]
            }
            if ((this.error[key].indexOf(value)) != -1) {
                return
            }

            this.error[key].push(value)
        },
        handleErrors: function(response) {
            self = this;
            var errorResponse, keyLabel;
            if (response.status == 500)
            {
                self.displayError('general', "Internal Server Error")
            }
            else
            {
                try {
                    errorResponse = response.responseJSON['errors']
                    _.each(errorResponse, function(errors, key) {

                        if(key == 'answers') {
                            self.displayError(key, 'Please add at least 2 valid answers to your poll.')
                        } else {
                            _.each(errors, function(value) {
                                self.displayError(key, value)
                            })
                        }
                    })
                }
                catch (err)
                {
                    throw "No Internet Connection!";
                }
            }
        },
        clearForm: function () {
            this.obj.name = ''
            this.obj.content = ''
        },
		showPostPreloader: function($element) {
			$($element).find(".form-submit").prepend('<span class="preloader-small"></span>');
			$($element).find("input[type='submit']").attr("disabled", true);
			$($element).find("input[type='submit']").css("opacity", "0");
			$($element).find('textarea').css("background-color", "#f7f7f7");
			$($element).find("textarea").attr("disabled", true);
			$($element).find("input[type='text']").attr("disabled", true);
			$($element).find("input[type='text']").css("background-color", "#f7f7f7");
			$($element).find(".emoji-wysiwyg-editor").css("background-color", "#f7f7f7");

		},

		hidePostPreloader: function($element) {
			$($element).find(".preloader-small").remove();
			$($element).find("input[type='submit']").attr("disabled", false);
			$($element).find("input[type='submit']").css("opacity", "1");
			$($element).find('textarea').css("background-color", "#ffffff");
			$($element).find("textarea").attr("disabled", false);
			$($element).find("input[type='text']").css("background-color", "#ffffff");
			$($element).find("input[type='text']").attr("disabled", false);
			$($element).find(".emoji-wysiwyg-editor").css("background-color", "#ffffff");

		},
	}
}
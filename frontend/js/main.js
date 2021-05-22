// Set up Ajax to look for the CSRF_TOKEN and set that cookie so we don’t have to set it up on every single Ajax request
$.ajaxSetup({
	beforeSend: function beforeSend(xhr, settings) {
		function getCookie(name) {
			let cookieValue = null;

			if (document.cookie && document.cookie !== "") {
				const cookies = document.cookie.split(";");

				for (let i = 0; i < cookies.length; i += 1) {
					const cookie = jQuery.trim(cookies[i]);

					// Does this cookie string begin with the name we want?
					if (cookie.substring(0, name.length + 1) === `${name}=`) {
						cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
						break;
					}
				}
			}

			return cookieValue;
		}

		if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
			// Only send the token to relative URLs i.e. locally.
			xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
		}
	},
});

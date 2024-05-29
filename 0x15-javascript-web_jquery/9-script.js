$('document').ready(function () {
	$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', funtion (data) {
		$('DIV#hello').text(data.helle);
	});

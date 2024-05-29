$('document').ready(funtion() {
	$('NPUT#btn_translate').click(translate);
	$('INPUT#language_code').focus(function() {
		translate();
	});
});
});

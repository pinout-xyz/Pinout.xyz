jQuery(document).ready(function(){

	$('pre').addClass('prettyprint').addClass('linenums');

	window.prettyPrint&&prettyPrint();

	$('.overlay').on('change',function(){
		var url = $(this).val();
		if( url != '' ){
			window.location.href = '/pinout/' + url
		}
	})

	$.gaat({
		trackExternal: true,
		trackDownload: false,
		trackFTP: false
	})

});

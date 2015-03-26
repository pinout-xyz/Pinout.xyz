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

	$('article p').each(function(){
		html = $(this).html();

		html = html.replace(
			/Physical\ Pin\ ([0-9]{1,2})/gi,
			function(str, c1){
				return '<span class="pin-hover" data-pin="' + c1 + '">' + str + '</span>';
			}
		)

		$(this).html(html);
	});

	$('article p .pin-hover').hover(function(){
		var pin = $(this).data('pin');
		$('li.pin' + pin).addClass('hover-pin');
	},function(){
		var pin = $(this).data('pin');
		$('li.pin' + pin).removeClass('hover-pin');
	});

	$('article p').on('click','.pin-hover',function(){
		var pin = $(this).data('pin');
		$('li.pin' + pin + ' a').trigger('click');
	})

});

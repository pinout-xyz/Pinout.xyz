jQuery(document).ready(function(){
	var overlay = $('.drop-down .overlay');
	var overlay_slideUp;

	$('pre').addClass('prettyprint').addClass('linenums');

	window.prettyPrint&&prettyPrint();

	$('.drop-down').on('click',function(e){
		e.stopPropagation();
		overlay.slideDown(100);
	});
	$('#container').on('click',function(){
		overlay.slideUp(100);
	})

	$('.drop-down').hover(function(){
		clearTimeout(overlay_slideUp);
		overlay_slideUp = setTimeout(function(){overlay.slideDown(100);}, 200);
	},function(){
		clearTimeout(overlay_slideUp);
		overlay_slideUp = setTimeout(function(){overlay.slideUp(100);}, 500);
	});

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

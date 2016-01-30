jQuery(document).ready(function(){
	var overlay_slideUp;
	var dropdowns = $('#sections ul li div');

	$('pre').addClass('prettyprint').addClass('linenums');

	window.prettyPrint&&prettyPrint();


	$('#container').on('click',function(){
		dropdowns.slideUp(100);
	})

	$('#sections > ul > li').hover(function(){
		var dropdown = $(this).find('div');
		clearTimeout(overlay_slideUp);
		if(dropdowns.filter(':visible').length){
			dropdowns.hide();
			dropdown.show();
		}
		else
		{
			overlay_slideUp = setTimeout(function(){dropdowns.slideUp(100);dropdown.slideDown(100);}, 300);
		}
	},function(){
		var dropdown = $(this).find('div');
		clearTimeout(overlay_slideUp);
		overlay_slideUp = setTimeout(function(){dropdown.slideUp(100);}, 500);
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

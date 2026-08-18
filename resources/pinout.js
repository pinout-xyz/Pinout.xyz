jQuery(document).ready(function(){

	$('#pinout-view').removeAttr('hidden');

	$('#gpio').on('animationend', function(event){
		if (event.target === this) {
			$(this).removeClass('flipping rotating');
		}
	});

	$('#pinout-view button').on('click', function(){
		var view = $(this).hasClass('mirror') ? 'mirror' : 'rotate';
		var pressed = !$('#gpio').hasClass(view);
		var gpio = $('#gpio');

		gpio.toggleClass(view, pressed).removeClass('flipping rotating');
		gpio[0].offsetWidth;
		gpio.addClass(view === 'mirror' ? 'flipping' : 'rotating');

		$(this).attr('aria-pressed', pressed);
	});

	$('pre').addClass('prettyprint').addClass('linenums');

	window.prettyPrint&&prettyPrint();

	$('article p,article li').each(function(){
		html = $(this).html();

		html = html.replace(
			/Physical\ Pin\ ([0-9]{1,2})/gi,
			function(str, c1){
				return '<span class="pin-hover" data-pin="' + c1 + '">' + str + '</span>';
			}
		)

		html = html.replace(
			/GPIO\ ([0-9]{1,2})/gi,
			function(str, c1){
				var pin = $("#gpio li").filter(function(){return $(this).find("span.name").text() == "GPIO " + c1}).find('.pin').text();
				return '<span title="Click for details about pin ' + pin + '" class="pin-hover" data-pin="' + pin + '">' + str + '</span>';
			}
		)

		$(this).html(html);
	});

	$('article p .pin-hover, article li .pin-hover').hover(function(){
		var pin = $(this).data('pin');
		$('li.pin' + pin).addClass('hover-pin');
	},function(){
		var pin = $(this).data('pin');
		$('li.pin' + pin).removeClass('hover-pin');
	});

	$('article').on('click', '.pin-hover', function(){
		var pin = $(this).data('pin');
		window.location = $('li.pin' + pin + ' a').attr('href');
	});

});

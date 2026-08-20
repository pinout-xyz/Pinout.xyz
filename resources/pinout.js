jQuery(document).ready(function(){

	$('#pinout-view').removeAttr('hidden');

	$('.pin-function-tabs').each(function(){
		var group = $(this);
		var tabs = group.find('[role="tab"]');
		var panels = group.find('[role="tabpanel"]');

		function activate(tab, focus){
			tabs.attr({'aria-selected': 'false', tabindex: '-1'});
			panels.attr('hidden', 'hidden');

			$(tab).attr('aria-selected', 'true').removeAttr('tabindex');
			$('#' + $(tab).attr('aria-controls')).removeAttr('hidden');

			if (focus) {
				$(tab).trigger('focus');
			}
		}

		tabs.on('click', function(){
			activate(this, false);
		});

		tabs.on('keydown', function(event){
			var index = tabs.index(this);

			if (event.key === 'ArrowRight') {
				activate(tabs.get((index + 1) % tabs.length), true);
			}

			if (event.key === 'ArrowLeft') {
				activate(tabs.get((index - 1 + tabs.length) % tabs.length), true);
			}
		});

		group.addClass('tabbed');
		group.find('.tabs').removeAttr('hidden');

		activate(tabs.filter('[aria-selected="true"]').get(0) || tabs.get(0), false);
	});

	$('#gpio').on('animationend', function(event){
		if (event.target === this) {
			$(this).removeClass('flipping rotating rotating-back');
		}
	});

	$('#pinout-view button').on('click', function(){
		var view = $(this).hasClass('mirror') ? 'mirror' : 'rotate';
		var pressed = !$('#gpio').hasClass(view);
		var gpio = $('#gpio');

		gpio.toggleClass(view, pressed).removeClass('flipping rotating rotating-back');
		gpio[0].offsetWidth;
		gpio.addClass(view === 'mirror' ? 'flipping' : (pressed ? 'rotating' : 'rotating rotating-back'));

		$(this).attr('aria-pressed', pressed);
	});

	$('pre').addClass('prettyprint').addClass('linenums');

	window.prettyPrint&&prettyPrint();

	$('article p,article li,article td').each(function(){
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
				var pin = $("#gpio li").filter(function(){return $(this).find("span.name").text() == "GPIO " + c1}).find('.phys').text();
				return '<span title="Click for details about pin ' + pin + '" class="pin-hover" data-pin="' + pin + '">' + str + '</span>';
			}
		)

		$(this).html(html);
	});

	$('article p .pin-hover, article li .pin-hover, article td .pin-hover').hover(function(){
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

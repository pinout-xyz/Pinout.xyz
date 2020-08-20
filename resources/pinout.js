jQuery(document).ready(function(){
	var overlay_slideUp;
	var dropdowns = $('#sections ul li .dropdown');

	$('pre').addClass('prettyprint').addClass('linenums');

	$('#gpio li').each(function(){
		var gpio = $(this).find('.default .phys').text();
		var bcm = $(this).find('.default .name').text().replace('BCM ', '').trim();
		$(this).find('.default .name').text(bcm);
		$(this).data('gpio', gpio);
		$(this).data('bcm', bcm);
	});

	$('#mode').show().find('li').on('click', function(e){
		e.preventDefault();
		e.stopPropagation();
		$(this).parents('ul').find('li').removeClass('selected');
		$(this).addClass('selected');

		$('li .phys').text('');

		switch($(this).text()) {
			case 'GPIO':
				$('#gpio li').each(function(){
					var gpio = $(this).data('gpio');
					var bcm = $(this).data('bcm');
					if($(this).hasClass('gpio')) {
						$(this).find('.name').text(gpio);
					}
					$(this).find('.phys').text(bcm);
				});
				break;
			case 'BCM':
				$('#gpio li').each(function(){
					var gpio = $(this).data('gpio');
					var bcm = $(this).data('bcm');
					if($(this).hasClass('gpio')) {
						$(this).find('.name').text(bcm);
					}
					$(this).find('.phys').text(gpio);
				});
				break;
		}
	});

	window.prettyPrint&&prettyPrint();

	var groups = $('#sections .boards .group');
	var group_nav = $('#sections .boards .group-nav li');
	
	groups.hide().filter(':eq(0)').show();
	group_nav.removeClass('active').filter(':eq(0)').addClass('active');

	group_nav.on('click',function(e){
		group_nav.removeClass('active');
		$(this).addClass('active');
		groups.hide();

		var group = $(this).data('group');

		groups.filter('.group_' + group).show();
	})

	$('#container').on('click',function(){
		dropdowns.slideUp(100);
	});

	$('#sections > ul > li > a').on('click',function(e){
		e.preventDefault();
		e.stopPropagation();
		var dropdown = $(this).parent().find('.dropdown');
		dropdowns.hide();
		dropdown.show();
	});

	$('#sections > ul > li > a').hover(function(e){
		e.preventDefault();
		var dropdown = $(this).parent().find('.dropdown');
		clearTimeout(overlay_slideUp);
		if(dropdowns.filter(':visible').length){
			dropdowns.hide();
			dropdown.show();
		}
		else
		{
			overlay_slideUp = setTimeout(function(){dropdowns.slideUp(100);dropdown.slideDown(100);}, 300);
		}
	},function(e){
		e.preventDefault();
		var dropdown = $(this).parent().find('.dropdown');
		clearTimeout(overlay_slideUp);
		overlay_slideUp = setTimeout(function(){dropdown.slideUp(100);}, 100);
	});

	dropdowns.on('click',function(e){
		e.stopPropagation();
	})

	dropdowns.hover(function(e){
		clearTimeout(overlay_slideUp);
	},function(e){
		e.preventDefault();
		var dropdown = $(this);
		clearTimeout(overlay_slideUp);
		overlay_slideUp = setTimeout(function(){dropdown.slideUp(100);}, 100);
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

jQuery(document).ready(function(){
	var overlay_slideUp;
	var dropdowns = $('#sections ul li .dropdown');

	$('pre').addClass('prettyprint').addClass('linenums');

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
				var pin = $("#gpio li").filter(function(){return $(this).find("span.name").text() == "GPIO " + c1}).find('.phys').text();
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

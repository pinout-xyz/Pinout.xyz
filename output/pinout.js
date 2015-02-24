jQuery(document).ready(function(){
	var History = window.History;

	var homepage = jQuery('article.homepage').index();
	var pincount = 40;

	History.Adapter.bind(window,'statechange',function(){
		var State = History.getState();
		var url = State.url.replace('http://pi.gadgetoid.com','');
		if( url == '/pinout' )
		{
			jQuery('h1').click();
		}
		else
		{
			jQuery('a[href="' + url + '"]').click();
		}
	})

	window.prettyPrint&&prettyPrint();

	jQuery('#pages').cycle({
		timeout:0,
		slideExpr:'article',
		startingSlide:homepage,
		speed:200,
		containerResize:0
	});

	jQuery('.legend li a').on('click',function(e){
		e.preventDefault();
		jQuery('nav#gpio li').removeClass('legend active');
		var title = jQuery(this).attr('title');
		var url = jQuery(this).attr('href');

		jQuery('span.default').show();
		jQuery('span.alternate').hide();

		var legend = jQuery(this).parent().attr('class');
		var page = jQuery('article.' + legend).index();
		var pins = [];
		if( jQuery(this).parent().data('pins') ){
			pins = jQuery(this).parent().data('pins').split(',');
		}
		
		jQuery('span.' + legend).show().parent().parent().addClass('legend').find('span.default').hide();

		var x = pins.length;
		while(x--){
			jQuery('.pin' + pins[x]).addClass('legend');
		}
		jQuery('#pages').cycle(page);

		History.pushState({legend:jQuery(this).attr('class'),url:jQuery(this).attr('href')}, 'Raspberry Pi Pinout - ' + title, url)
	});

	function showPage(object,offset){
		jQuery('span.default').show();
		jQuery('span.alternate').hide();
		jQuery('nav#gpio li').removeClass('legend active');
		jQuery('#pages').cycle(offset+object.parent().index());
		object.parent().addClass('active');
		title = 'Pin ' + object.find('span.default').text().replace(' ',': ');
		History.pushState({pin:offset+object.parent().index(),url:object.attr('href')}, title, object.attr('href'));
	}

	jQuery('nav#gpio ul.bottom a').on('click',function(e){
		e.preventDefault();showPage(jQuery(this),0);});
	jQuery('nav#gpio ul.top a').on('click',function(e){
		e.preventDefault();showPage(jQuery(this),pincount/2);});

	jQuery('h1').on('click',function(){
		jQuery('span.default').show();
		jQuery('span.alternate').hide();
		jQuery('nav#gpio li').removeClass('legend active');
		jQuery('#pages').cycle(homepage);
		History.pushState({pin:homepage,url:'http://pi.gadgetoid.com/pinout'}, 'Raspberry Pi Pinout', '/pinout');
	});

	url = window.location.href.replace('http://pi.gadgetoid.com/','/');

	jQuery('a[href="' + url + '"]').click();
});
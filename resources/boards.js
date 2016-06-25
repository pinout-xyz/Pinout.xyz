var dom_boards = $('#boards .board');

var facets = {};
var filters = {};

dom_boards.each(function(idx, obj){
	var obj = $(obj);
	for (var key in obj.data()){
		if(typeof(key) !== 'undefined'){

			if(typeof(facets[key]) == 'undefined'){
				facets[key] = {
					'title':key.split(/(?=[A-Z])/).join(" ").toLowerCase(),
					'key':key,
					'items':[]
				};
				filters[key] = '';
			}

			var vals = obj.data(key).split(',');

			for(var idx in vals){
				var val = vals[idx];

				if(facets[key].items.indexOf(val) == -1){
					facets[key].items.push(val);
					facets[key].items.sort();
				}
			}
		}
	}
})

var dom_facets = $('<div>').addClass('facets').insertBefore('#boards');

dom_facets.on('click','li',function(e){
	var val = $(this).data('val');
	var key = $(this).data('key');
	console.log(val,key);

	if(filters[key] != val){
		filters[key] = val;
		$(this).parents('ul').find('li').removeClass('selected');
		$(this).addClass('selected');
	}
	else
	{
		filters[key] = '';
		//filters[key].splice(filters[key].indexOf(val), 1);
		$(this).removeClass('selected');
	}

	update_filters()
});

for (var facet in facets){
	var title = facets[facet].title;
	var items = facets[facet].items;
	var key = facets[facet].key;

	console.log(title, items, key);

	$('<h4>').text(title).appendTo(dom_facets);
	var dom_facet = $('<ul>').addClass('facet').appendTo(dom_facets);

	for(var idx in items){
		var val = items[idx];
		$('<li>')
			.addClass('item')
			.data('key',key)
			.data('val',val)
			.text(val)
			.appendTo(dom_facet);
	}
}

function update_filters(){
	dom_boards.each(function(idx, obj){
		var obj = $(obj);
		var hide = false;

		for(var key in filters){
			console.log('Filter key',key);
			var selected = filters[key];

			if(selected.length > 0){
				if(obj.data(key).split(',').indexOf(selected) == -1){
					hide = true;
				}
			}
		}

		if(hide) {
			obj.hide();
		}
		else
		{
			obj.show();
		}
	})
}
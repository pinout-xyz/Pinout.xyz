$(document).ready(function(){   
    var pin_size = 10;
    
    $('a').each(function(idx, obj){
        var href = $(obj).attr('href');
        if( href.indexOf('http://pi.gadgetoid.com/pinout/pin') == 0){
            var pin = parseInt(href.replace('http://pi.gadgetoid.com/pinout/pin','').split('_')[0]);
            console.log(href,pin);
            $(obj).data('pin', pin).css({position:'relative'});
            $(obj).hover(
                function(){$(this).find('.pinout_popup').slideDown(100);},
                function(){$(this).find('.pinout_popup').slideUp(100);}
            );
            var w = ( pin_size + 4 ) * 2;
            var pinout_popup = $('<div>')
            .css({
                position: 'absolute',
                width: w,
                overflow: 'hidden',
                marginLeft: -(w/2),
                left: '50%',
                top:  $(this).css('line-height'),
                background: '#073642',
                padding: 2,
                border: '5px solid #5F8645',
                borderLeft: '10px solid #5F8645'
            })
            .addClass('pinout_popup')
            .hide();
            
            for( var x = 1; x <= 40; x++ ){
                var bgcol = '#859900';
                
                if( $.inArray(x, [1,8,10,17]) > -1 ){
                    bgcol = '#B58900';
                }
                else if(  $.inArray(x, [3,5,27,28]) > -1 ){
                    bgcol = '#268BD2';
                }
                else if(  $.inArray(x, [2, 4]) > -1 ){
                    bgcol = '#DC322F';
                }
                else if( $.inArray(x, [19,21,23,24,26,35,38,40]) > -1 ){
                    bgcol = '#D33682';
                }
                else if( $.inArray(x, [6,9,14,20,25,30,34,39]) > -1 ){
                    bgcol = '#002B36';
                }
                
                
                $('<div>')
                .css({
                    float: 'left',
                    width: pin_size-2,
                    height: pin_size-2,
                    margin: 2,
                    background: x==pin ? '#FFFFFF' : bgcol,
                    borderRadius:x==1 ? 0 : pin_size/2,
                    border: '1px solid #FFFFFF',
                    boxShadow : x==pin ? '0px 0px 10px #FFFFFF' : 'none'
                })
                .appendTo(pinout_popup);
            }
            
            $(obj).append(pinout_popup);
        }
    });
});

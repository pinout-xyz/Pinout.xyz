// gaat - Google Analytics Advanced Tracker
// (c)2010 Further Search Marketing
// Developers:
//      Philip Howard - https://github.com/gadgetoid/
//      Andrew Hawken - https://github.com/andiih/
//
// Version: 1.1 - Updated to check for and use _gaq
// Version: 1.2 - Changed to use .prop() for hostname,search,
//                pathname and protocol which are now considered
//                properties in jQ
//              - Also added check for lack of prop() function in
//                earlier versions of jQuery, and patched with a
//                simple redirect to attr()
// Version: 2.0 - Updated to remove pageTracker support.
//                Now uses _gaq's _trackEvent method for
//                correctly tracking events without creating fake
//                page views in Google Analytics
//              - Prefix paths for fake folders are now deprecated
//                  : email, downloads, external properties
// Version: 2.1 - Changed to catch-all handling using jQuery(document).on(event,element,fn...
//              - Added selectorAnchor and selectorForm options to select specific a/form tags
//              - Added selectAll option to override selectors and bind to all a/form tags
//
// Usage:
//
// Normal:
// jQuery.gaat();
// This will track according to the default options below
//
// Advanced:
// jQuery.gaat({
//		trackEmail: true,
//      trackExternal: false,
//      trackDownloads: true,
//		extensions: ['pdf','doc']
//	});
//
//

(function(jQuery){

    jQuery.gaat = function(opts){

        opts = jQuery.extend({
            extensions:     ['doc','eps','svg','xls','ppt','pdf','xls','zip','txt','vsd','vxd','js','css','rar','exe','wma','mov','avi','wmv','mp3'],
            trackEmail:     true,
            trackExternal: 	true,
            trackDownload: 	true,
            trackFTP:       true,
            hostname:       location.host,
            selectorAnchor: 'a[data-group="gaat_tracked"]',
            selectorForm:   'form[data-group="gaat_tracked"]',
            respectExistingEvents:  true,
            selectAll:      true,
            debug:          false,

            defaultTrack:   true,
            defaultDefer:   true
        }, opts);

        opts.extensions = new RegExp('\\.(?:' + opts.extensions.join('|') + ')($|\\&|\\?)');

        /* Add the prop function for jQuery < 1.6 */
        if( !jQuery.fn.prop )
        {
            jQuery.fn.extend({
                prop: function(property){
                    return jQuery(this).attr(property);
                }
            });
        }

        /* Double check the status of gaq */
        function trackEvent(category, action, opt_label, opt_value, opt_noninteraction)
        {
            if (typeof(_gaq) 	== "object")
            {
                var tracking_event = ['_trackEvent', category, action, opt_label, opt_value, opt_noninteraction];
                if (opts.debug) alert(tracking_event);
                _gaq.push(tracking_event);
            }
        }

        function trackFormPost(e,obj)
        {
            var action = jQuery(obj).attr('action');
            var method = jQuery(obj).prop('method');

            if( method.toLowerCase() == 'post' )
            {
                trackEvent('Form','Submit', action, 0, true);
            }
        }

        function trackFTP(e,obj)
        {
            if(opts.debug) e.preventDefault();

            var href = jQuery(obj).attr('href');

            trackEvent('Link','FTP',href,0,true);
        }

        /* Defer link action, allowing the _gaq queue to process */
        function deferLinkAction(e, obj) {
            // Avoid deferring link action on any link with a target
            if (jQuery(obj).attr('target') == undefined || jQuery(obj).attr('target').toLowerCase() == '_self' || jQuery(obj).attr('target').toLowerCase() == '') {

                //alert(jQuery._data(obj, 'events'));
                //alert(jQuery._data(obj, 'events').click.length);


                // Avoid deferring link action on any link with existing onclick events
                if (opts.respectExistingEvents &&
                    ( (jQuery(obj).attr('onclick') != undefined && jQuery(obj).attr('onclick') != '') ||
                        ( jQuery._data(obj, 'events') != undefined && jQuery._data(obj, 'events').click.length > 0 ) ) ) return true;

                setTimeout(function () { location.href = obj.href; }, 400);
                if (opts.debug) alert('Deferring link action');
                return false;
            }
        }

        /* Track email addresses with the email prefix from opts */
        function trackEmail(e,obj)
        {
            var options = getDataOptions(obj);
            if ( options.track )
            {
                if(opts.debug) e.preventDefault();

                var href = jQuery(obj).attr('href');
                var mailto = href.substring(7);

                trackEvent('Link','Email',mailto, 0, false);
            }
        }

        function trackDownload(e,obj)
        {
            var options = getDataOptions(obj);

            if(opts.debug) e.preventDefault();

            if( options.track )
            {

                var pathname	= jQuery(obj).prop('pathname');
                var search	 = jQuery(obj).prop('search');

                var link 	= (pathname.charAt(0) == "/") ? pathname : "/" + pathname;

                if (search && pathname.indexOf(search) == -1) link += search;

                var sub_category = 'Other';

                // pdf files
                if (link.match(/\.(?:pdf)/)) {
                    sub_category = 'PDF';
                }

                // music files
                if (link.match(/\.(?:wma|mp3|flac|ogg|wav)/)) {
                    sub_category = 'Audio';
                }

                // excel files
                if (link.match(/\.(?:xls|xlsx)/)) {
                    sub_category = 'Excel';
                }

                // document files
                if (link.match(/\.(?:doc|docx)/)) {
                    sub_category = 'Document';
                }

                // archive files
                if (link.match(/\.(?:zip|gzip|7z)/)) {
                    sub_category = 'Zip';
                }

                trackEvent('Download',sub_category,link, 0, false);

            }
        }

        function getDataOptions(obj)
        {

            var options_string = jQuery(obj).attr('data-gaat-options');

            var options = {};

            if (!options_string == '')
            {
                if (!options_string.indexOf('"') > -1)
                {
                    // Expand JSON with quotes
                    options_string = options_string
                        .replace('{','{"')
                        .replace('}','"}')
                        .replace(':','":"')
                        .replace(',','","')
                        .replace('"true"','true')
                        .replace('"false"','false');
                }

                options = JSON.parse(options_string);
            }

            options = jQuery.extend({
                    defer:      opts.defaultDefer,
                    track:      opts.defaultTrack,
                    trackAs:    ''
                },
            options)

            return options;
        }

        function trackExternal(e,obj)
        {
            var options = getDataOptions(obj);

            if (options.track)
            {

                if(opts.debug) e.preventDefault();

                var pathname	= jQuery(obj).prop('pathname');
                var hostname 	= jQuery(obj).prop('hostname');
                var search	= jQuery(obj).prop('search');

                var link 	= (pathname.charAt(0) == "/") ? pathname : "/" + pathname;

                if (search && pathname.indexOf(search) == -1) link += search;

                link		= hostname + link;

                trackEvent('Link','External',link,0,true);

                if (options.defer)
                    return deferLinkAction(e,obj);

            }
        }

        function addLinkTracking()
        {

            var selector_anchor = 'a';
            var selector_form = 'form'

            if(!opts.selectAll)
            {
                selector_anchor = opts.selectorAnchor;
                selector_form = opts.selectorForm;
            }

            // Catch all click events on existing and dynamically created "a" tags
            jQuery(document).on('click', selector_anchor,
                function(e){
                    //try{
                    //alert('handled');
                        var href 	    = jQuery(this).prop('href');
                        var hostname 	= jQuery(this).prop('hostname');
                        var protocol 	= jQuery(this).prop('protocol');
                        var pathname	= jQuery(this).prop('pathname');
                        var search	    = jQuery(this).prop('search');
                        var path	    = pathname + search;

                        if ( (href.match(/^javascript:/) || href == '#' || href == '') ){
                            return true; // Don't handle empty or javascript links
                        }

                        if(protocol == "mailto:")
                        {
                            trackEmail(e,this);
                        }
                        else if(protocol == "ftp:")
                        {
                            trackFTP(e,this);
                        }
                        else if(hostname == opts.hostname && path.match(opts.extensions)) // Track links with matching hostnames as internal
                        {
                            trackDownload(e,this);
                        }
                        else if(hostname != opts.hostname) // Track anything that doesn't match the hostname as external
                        {
                            trackExternal(e,this);
                        }

                    //}
                    //catch(e)
                    //{
                    //}
                }
            );

            jQuery(document).on('submit',selector_form,
                function(e){
                    trackFormPost(e,this);
                }
            );


            jQuery(document).on('click','a[data-group="gaat_force_tracking"]',
                function(){

                    var options = getDataOptions(this);

                    switch(options.trackAs)
                    {
                        case 'download':
                            jQuery(this).click(function(e){trackDownload(e,this)});
                            break;
                        case 'email':
                            jQuery(this).click(function(e){trackEmail(e,this)});
                            break;
                        case 'ftp':
                            jQuery(this).click(function(e){trackFTP(e,this)});
                            break;
                        case 'external':
                            jQuery(this).click(function(e){trackExternal(e,this)});
                            break;
                    }

                });

        }

        if (typeof(_gaq) == "object")
        {
            if(opts.debug) alert("GAAT initializing, found _gaq");
            addLinkTracking();
        }
        else
        {
            if(opts.debug) alert("Unable to initialise GAAT, missing Google Analytics ga.js with gaq");
            return false;
        }

    };

})(jQuery);

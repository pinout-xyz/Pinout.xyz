import os

from . import boards, details, render

TRANSLATE_BANNER = '<p class="translate-me"><a href="https://github.com/pinout-xyz/Pinout.xyz">{}</a></p>'


def page_content(site, overlay):
    if not overlay['translated']:
        overlay['long_description'] = TRANSLATE_BANNER.format(
            site.strings['translate_msg']) + overlay['long_description']

    overlay['long_description'] = details.describe(site, overlay, site.report.warn)
    return render.article(overlay['name'], overlay['long_description'])


def overlay_pages(site):
    pages = {}
    tiles = []

    for overlay in site.overlays:
        site.report.notice('>> Rendering: {}'.format(overlay['source']))

        overlay['content'] = page_content(site, overlay)
        overlay['nav'] = render.nav(site, overlay['page_url'], overlay, site.report.warn)
        pages[overlay['page_url']] = overlay

        if 'class' not in overlay or 'type' not in overlay:
            continue

        if overlay['class'] == 'board':
            tiles.append((overlay['name'].lower(), render.board_tile(
                site, overlay,
                boards.types(site, overlay, site.report.warn),
                boards.formfactor(site, overlay, site.report.warn))))

    return pages, [tile for _, tile in sorted(tiles)]


def index_pages(site, tiles):
    return {
        'boards': {'content': ''.join(tiles), 'src': 'boards'},
        'index': {'content': render.article('Index', site.markdown('template/index.md')), 'src': 'index'},
        '404': {'content': render.article('404', site.markdown('template/404.md'))},
    }


def render_page(site, url, page, interfaces, default_nav):
    template = site.templates.boards if url == 'boards' else site.templates.page
    src = page.get('src')

    return site.templates.render(
        template,
        site.strings,
        site.settings,
        opengraph=True,
        lang_links=render.lang_nav(site, render.lang_links(site, src) if src else []),
        hreflang='\n\t\t'.join(render.hreflang(site, src) if src else []),
        nav=page.get('nav') or default_nav,
        content=page['content'],
        resource_url=site.resource_url,
        description=page.get('description') or site.strings['default_desc'],
        title=page['name'] + site.strings['title_suffix'] if 'name' in page else site.strings['default_title'],
        langcode=site.lang,
        interfaces=render.interfaces_menu(site, page),
        body_class=body_class(url, page),
        crumbtrail=render.crumbtrail(site, page),
        api_image='https://pinout.xyz/v1/img/{}.png'.format(url))


def body_class(url, page):
    if url == 'boards':
        return 'boards-page'
    if page.get('class') == 'board':
        return 'board'
    return ''


def render_pin_page(site, number, interfaces):
    url, content, title = render.pin_page(site, number)
    if url is None:
        return None, None

    html = site.templates.render(
        site.templates.page,
        site.strings,
        site.settings,
        lang_links=render.lang_nav(site, render.lang_links(site, 'pin{}'.format(number))),
        hreflang='\n\t\t'.join(render.hreflang(site, 'pin{}'.format(number))),
        nav=render.nav(site, url),
        content=content,
        resource_url=site.resource_url,
        description=site.strings['default_desc'],
        title=title + site.strings['title_suffix'],
        langcode=site.lang,
        interfaces=interfaces,
        body_class='pin',
        crumbtrail=render.crumbtrail(site))

    return url, html


def output_path(site, url, page):
    output = os.path.join(site.root, 'output', site.lang)

    if url == 'boards':
        return os.path.join(output, 'boards', 'index.html')
    if url in ('index', '404'):
        return os.path.join(output, '{}.html'.format(url))
    return os.path.join(output, 'pinout', '{}.html'.format(url))


def write(path, html):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as handle:
        handle.write(html)


def build(site):
    site.report.info('\nRendering overlay pages...')
    pages, tiles = overlay_pages(site)
    pages.update(index_pages(site, tiles))

    interfaces = render.interfaces_menu(site, None)
    default_nav = render.nav(site, 'pinout')

    site.report.info('\nRendering pin pages...')
    for number in site.pins.numbers():
        url, html = render_pin_page(site, number, interfaces)
        if url is None:
            continue
        site.report.notice('>> Saving: pinout/{}/index.html'.format(url))
        write(os.path.join(site.root, 'output', site.lang, 'pinout', url, 'index.html'), html)

    site.report.info('\nSaving overlay and index pages...')
    for url, page in pages.items():
        html = render_page(site, url, page, interfaces, default_nav)
        path = output_path(site, url, page)
        if 'source' in page:
            site.report.notice('>> Saving: {} => {}'.format(page['source'], os.path.relpath(path)))
        write(path, html)

    site.report.info('\nAll done!')

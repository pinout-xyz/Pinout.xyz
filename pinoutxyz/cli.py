import argparse
import os
import shutil
import sys

from . import drafts, overlays, settings, translations, urls
from .build import build
from .site import Reporter, Site

SITE_DIR = 'output/site'
SHARED_DIRS = ('resources', 'phatstack')


def resolve(root, requested):
    available = settings.languages(root)

    if not requested:
        return available

    unknown = [lang for lang in requested if lang not in available]
    if unknown:
        sys.exit("No such language '{}', expected one of: {}".format(unknown[0], ', '.join(available)))

    return requested


def build_languages(root, languages, verbose=False):
    reporter = Reporter(verbose)
    source = overlays.load_source(root, reporter.warn)
    alternates = urls.alternates(root, source)

    for lang in languages:
        reporter.info('\nBuilding {}...'.format(lang))
        build(Site(root, lang, alternates, reporter, source))

    return reporter


def assemble(root, languages):
    site = os.path.join(root, SITE_DIR)
    shutil.rmtree(site, ignore_errors=True)

    for lang in languages:
        source = os.path.join(root, 'output', lang)
        target = site if lang == 'en' else os.path.join(site, lang)
        shutil.copytree(source, target, dirs_exist_ok=True)

    for shared in SHARED_DIRS:
        shutil.copytree(os.path.join(root, shared), os.path.join(site, shared), dirs_exist_ok=True)


def command_build(args):
    languages = resolve(args.root, args.languages)
    reporter = build_languages(args.root, languages, args.verbose)

    if args.site:
        assemble(args.root, languages)
        print('\nAssembled {}'.format(os.path.join(args.root, SITE_DIR)))

    return 1 if args.strict and reporter.warnings else 0


def command_serve(args):
    from .server import serve

    languages = resolve(args.root, [args.lang] if args.lang else ['en'])
    build_languages(args.root, languages, args.verbose)
    assemble(args.root, languages)

    return serve(args.root, languages, args.port, args.watch)


def command_translations_list(args):
    return translations.report_list(args.root, settings.languages(args.root))


def command_translations_check(args):
    return translations.report_check(args.root, resolve(args.root, args.languages))


def command_translations_listing(args):
    return translations.report_listing(args.root, resolve(args.root, [args.lang])[0], args.action)


def command_boards_list(args):
    for board in drafts.available(args.root):
        print('{:38} {}'.format(board, drafts.check(args.root, board) or 'ready to publish'))
    return 0


def command_boards_publish(args):
    error = drafts.check(args.root, args.board) if args.check else None
    if error is None:
        error = drafts.publish(args.root, args.board)
    if error is not None:
        sys.exit(error)
    return 0


def command_boards_unpublish(args):
    error = drafts.unpublish(args.root, args.board)
    if error is not None:
        sys.exit(error)
    return 0


def parser():
    root = argparse.ArgumentParser(prog='pinoutxyz', description='Build and maintain Pinout.xyz')
    root.add_argument('--root', default='.', help='repository root')
    root.add_argument('-v', '--verbose', action='store_true', help='report every page')
    commands = root.add_subparsers(dest='command', required=True)

    build_command = commands.add_parser('build', help='render one or more languages')
    build_command.add_argument('languages', nargs='*', help='language codes, default all')
    build_command.add_argument('--site', action='store_true', help='assemble output/site')
    build_command.add_argument('--strict', action='store_true', help='fail on warnings')
    build_command.set_defaults(handler=command_build)

    serve_command = commands.add_parser('serve', help='build and serve one language')
    serve_command.add_argument('--lang', default='en')
    serve_command.add_argument('--port', type=int, default=8080)
    serve_command.add_argument('--watch', action='store_true', help='rebuild when src changes')
    serve_command.set_defaults(handler=command_serve)

    translations_command = commands.add_parser('translations', help='translation coverage and drift')
    translations_actions = translations_command.add_subparsers(dest='action', required=True)

    action = translations_actions.add_parser('list', help='coverage per language')
    action.set_defaults(handler=command_translations_list)

    action = translations_actions.add_parser('check', help='report frontmatter drift')
    action.add_argument('languages', nargs='*')
    action.set_defaults(handler=command_translations_check)

    for name, help_text in (('outstanding', 'overlays with no translation at all'),
                            ('partial', 'overrides that carry no translated text'),
                            ('translated', 'overlays with translated text')):
        action = translations_actions.add_parser(name, help=help_text)
        action.add_argument('lang')
        action.set_defaults(handler=command_translations_listing)

    boards_command = commands.add_parser('boards', help='manage draft board overlays')
    boards_actions = boards_command.add_subparsers(dest='action', required=True)

    action = boards_actions.add_parser('list', help='drafts awaiting publication')
    action.set_defaults(handler=command_boards_list)

    action = boards_actions.add_parser('publish', help='move a draft into src/en')
    action.add_argument('board')
    action.add_argument('--no-check', dest='check', action='store_false', help='skip draft validation')
    action.set_defaults(handler=command_boards_publish)

    action = boards_actions.add_parser('unpublish', help='return a board to draft')
    action.add_argument('board')
    action.set_defaults(handler=command_boards_unpublish)

    return root


def main(argv=None):
    args = parser().parse_args(argv)
    return args.handler(args)

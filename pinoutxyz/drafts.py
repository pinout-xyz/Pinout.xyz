import glob
import os
import shutil

from . import boards, documents, overlays, settings

DRAFT_OVERLAYS = 'draft/overlay'
DRAFT_BOARDS = 'draft/boards'
BOARD_IMAGES = 'resources/boards'


def available(root):
    return sorted(os.path.basename(path)[:-len('.md')]
                  for path in glob.glob(os.path.join(root, DRAFT_OVERLAYS, '*.md'))
                  if os.path.basename(path) != 'template.md')


def publish(root, board):
    draft = os.path.join(root, DRAFT_OVERLAYS, '{}.md'.format(board))

    if not os.path.exists(draft):
        return 'No draft at {}'.format(draft)

    published = os.path.join(root, 'src', 'en', 'overlay', '{}.md'.format(board))
    shutil.move(draft, published)
    print('Published {}'.format(published))

    image = os.path.join(root, DRAFT_BOARDS, '{}.png'.format(board))
    if os.path.exists(image):
        shutil.move(image, os.path.join(root, BOARD_IMAGES, '{}.png'.format(board)))
        print('Moved {}.png into {}'.format(board, BOARD_IMAGES))

    return None


def unpublish(root, board):
    published = os.path.join(root, 'src', 'en', 'overlay', '{}.md'.format(board))

    if not os.path.exists(published):
        return 'No board at {}'.format(published)

    shutil.move(published, os.path.join(root, DRAFT_OVERLAYS, '{}.md'.format(board)))
    print('Returned {} to {}'.format(board, DRAFT_OVERLAYS))

    for lang in settings.languages(root):
        if lang == 'en':
            continue
        path = os.path.join(root, 'src', lang, 'overlay', '{}.md'.format(board))
        if os.path.exists(path):
            os.remove(path)
            print('Removed {}'.format(path))

    image = os.path.join(root, BOARD_IMAGES, '{}.png'.format(board))
    if os.path.exists(image):
        shutil.move(image, os.path.join(root, DRAFT_BOARDS, '{}.png'.format(board)))
        print('Moved {}.png into {}'.format(board, DRAFT_BOARDS))

    return None


def check(root, board):
    path = os.path.join(root, DRAFT_OVERLAYS, '{}.md'.format(board))

    if not os.path.exists(path):
        return 'No draft at {}'.format(path)

    data = documents.frontmatter(path) or {}

    missing = [key for key in ('name', 'class', 'type', 'description') if key not in data]
    if missing:
        return 'Missing: {}'.format(', '.join(missing))

    names = boards.type_names('en')
    unknown = [token.strip() for token in str(data.get('type', '')).split(',')
               if boards.sanitize_type(names, token) is None]
    if unknown:
        return 'Unsupported type: {}'.format(', '.join(unknown))

    published = os.path.join(root, 'src', overlays.SOURCE, 'overlay', '{}.md'.format(board))
    if os.path.exists(published):
        return 'Already published as {}'.format(published)

    image = data.get('image')
    if image is None:
        return 'No image key'

    if not any(image in os.listdir(os.path.join(root, directory))
               for directory in (DRAFT_BOARDS, BOARD_IMAGES)):
        return 'image {!r} is in neither {} nor {}'.format(image, DRAFT_BOARDS, BOARD_IMAGES)

    return None

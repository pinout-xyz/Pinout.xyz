import glob
import os
import shutil

from . import documents, settings

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

    for lang in settings.languages(root):
        if lang == 'en':
            continue
        if os.path.exists(os.path.join(root, 'src', lang, 'overlay', '{}.md'.format(board))):
            continue
        copy = os.path.join(root, 'src', lang, 'translate', '{}.md'.format(board))
        shutil.copy(published, copy)
        print('Copied to {}'.format(copy))

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
        for subdir in ('overlay', 'translate'):
            path = os.path.join(root, 'src', lang, subdir, '{}.md'.format(board))
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

    data = documents.load(path)['data'] or {}
    missing = [key for key in ('name', 'class', 'type', 'description') if key not in data]

    if missing:
        return 'Draft is missing: {}'.format(', '.join(missing))

    if not os.path.exists(os.path.join(root, DRAFT_BOARDS, '{}.png'.format(board))) and 'image' not in data:
        return 'Draft has no image in {} and no image key'.format(DRAFT_BOARDS)

    return None

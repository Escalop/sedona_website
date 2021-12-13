from garpixcms.settings import *  # noqa

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


INSTALLED_APPS += [  # noqa
    'home',
    'hotels',
]

BOOKING_EVENT = 1

NOTIFY_EVENTS = {
    BOOKING_EVENT: {
        'title': 'Сообщение отправлено',
    },
}

CHOICES_NOTIFY_EVENT = [(k, v['title']) for k, v in NOTIFY_EVENTS.items()]

MENU_TYPE_HEADER_MENU = 'header_menu'


MENU_TYPES = {
    MENU_TYPE_HEADER_MENU: {
        'title': 'Верхнее меню',
            },
    MENU_TYPE_FOOTER_MENU: {
        'title': 'Нижнее меню',
    },
}

CHOICE_MENU_TYPES = [(k, v['title']) for k, v in MENU_TYPES.items()]


STATIC_URL = '/static/'
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'frontend', 'public', 'media/')
STATIC_ROOT = os.path.join(BASE_DIR, '..', 'frontend', 'public', 'static/')
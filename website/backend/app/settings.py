from garpixcms.settings import *  # noqa


INSTALLED_APPS += [  # noqa
    'home',
    'contacts',
    'news',
   # 'search',
]

FEEDBACK_EVENT = 1

NOTIFY_EVENTS = {
    FEEDBACK_EVENT: {
        'title': 'Обратная связь',
    },
}

CHOICES_NOTIFY_EVENT = [(k, v['title']) for k, v in NOTIFY_EVENTS.items()]
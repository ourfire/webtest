import os

from bitsapiens.settings import BASE_DIR

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, '/home/bitsapiens/webtest/templates'),
        ],
        'APP_DIRS': True,
        # other options...
    },
]